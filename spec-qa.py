#!/usr/bin/env python3
"""Detector for the Defence Before Fix specification documents.

The convention: every defined term is a '#### Term' heading in the terminology
section, and every use of a defined term in the body is a capitalised link to
that heading, e.g. [Class](#class) or [Classes](#class). A bare occurrence of a
defined word is therefore either an unlinked use of the term or the ordinary
English word, and the documents forbid both. The detector and toolchain
documents inherit the method specification's terms and link them across
documents, e.g. [Rule](SPEC.md#rule); the toolchain document inherits the
detector document's terms the same way.

    spec-qa.py         report findings, exit 1 on any

There is deliberately no fixer. The documents are hand-written prose, and a
mechanical linker's failures are well-formed markdown in the wrong sense, which
only a reader catches. Each finding names the edit; a person makes it.

Findings:
  glossary-missing   a document has no terminology headings
  bare-term          a defined word appears outside a link to its definition
  lowercase-link     a link to a term whose text is not capitalised
  wrong-anchor       a link to a term points at the wrong anchor
  dead-anchor        an internal link points at no heading
  never-used         a defined term is never linked to from the body
  scope-leak         a concept the method spec puts out of scope
  synonym            a second word for a term of record
  phrase-link        a term link inside a protected phrase (the method's name)
  rfc-placement      an RFC 2119 keyword outside a numbered section
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = ["SPEC.md", "DETECTOR-SPEC.md", "TOOLING-SPEC.md"]
# A document links a parent's terms as PARENT.md#slug; parents are searched in order.
INHERITS = {
    "DETECTOR-SPEC.md": ["SPEC.md"],
    "TOOLING-SPEC.md": ["SPEC.md", "DETECTOR-SPEC.md"],
}

SCOPE_LEAKS = {
    r"\bgates?\b": "'gate' is a pipeline concept; say the rule fires or the defence blocks",
    r"\b(the|a|every|each|any) build\b|\bbuild (fails|script|artefact)\b|\bfails the build\b": "'build' as a noun is a pipeline concept",
    r"\bpipelines?\b": "pipelines are out of scope by section 8",
    r"\bCI\b": "CI is out of scope by section 8",
    r"\bQA\b": "undefined shorthand; name the thing",
}
SYNONYMS = {
    r"\btooling\b": "toolchain",
    r"\btools?\b(?! that)": "toolchain, or detector/runner where the kind matters",
    r"\bstatic analysis\b|\banalysers?\b|\blinters?\b": "detector",
    r"\bremediation documentation\b": "remediation docs",
    r"\bexemptions?\b": "exception",
}

# Surface forms a term may take in prose. The link text keeps the surface form
# (capitalised); the anchor is always the term's own.
INFLECTIONS = {
    "conform": r"conform(?:s|ing|ance)?",
    "blocking": r"blocking",
    "narrowing": r"narrowing",
    "coverage": r"coverage",
    "remediation docs": r"remediation docs",
}

# Phrases in which a defined word appears in a sense that is NOT the term:
# the method's own name, and the unrelated security term it disclaims.
PHRASES = [r"Defen[cs]e Before Fix", r"defence in depth"]
PROTECT = r"`[^`]*`|\[[^\]]*\]\([^)]*\)|(?i:" + "|".join(PHRASES) + ")"


def slug(term: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-")


def pattern_for(term: str) -> str:
    if term in INFLECTIONS:
        return INFLECTIONS[term]
    return re.escape(term) + r"(?:s|es)?"


def glossary(text: str) -> list[str]:
    m = re.search(r"^## \d+\. Terminology\n(.*?)(?=^## )", text, re.S | re.M)
    if not m:
        return []
    return [t.strip().lower() for t in re.findall(r"^#### (.+)$", m.group(1), re.M)]


def terms_for(doc: str, own: dict[str, list[str]]) -> dict[str, str]:
    terms = {t: f"#{slug(t)}" for t in own[doc]}
    for parent in INHERITS.get(doc, []):
        for t in own[parent]:
            terms.setdefault(t, f"{parent}#{slug(t)}")
    return terms


def body_lines(text: str) -> list[tuple[int, str]]:
    out, in_code = [], False
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code or line.startswith("#"):
            continue
        out.append((n, line))
    return out


def blank_protected(line: str) -> str:
    return re.sub(PROTECT, lambda m: " " * len(m.group()), line)


# --------------------------------------------------------------------------- check


def check(here: Path) -> list[str]:
    findings: list[str] = []
    texts = {d: (here / d).read_text() for d in DOCS}
    own = {d: glossary(t) for d, t in texts.items()}
    anchors = {d: {slug(h) for h in re.findall(r"^#{1,6} (.+)$", t, re.M)} for d, t in texts.items()}

    for doc in DOCS:
        text = texts[doc]
        if not own[doc]:
            findings.append(f"{doc}: glossary-missing — no '#### Term' headings under the Terminology section")
        terms = terms_for(doc, own)
        ordered = sorted(terms, key=len, reverse=True)
        body = body_lines(text)

        for n, line in body:
            scrubbed = blank_protected(line)
            for term in ordered:
                for m in re.finditer(r"\b" + pattern_for(term) + r"\b", scrubbed, re.I):
                    findings.append(f"{doc}:{n}: bare-term '{m.group()}' → [{m.group().capitalize()}]({terms[term]})")
                    scrubbed = scrubbed[: m.start()] + " " * len(m.group()) + scrubbed[m.end():]

        for n, line in body:
            for phrase in PHRASES:
                first, rest = phrase.split(" ", 1)
                if re.search(r"\[" + first + r"\]\(#[a-z-]+\) " + rest, line, re.I):
                    findings.append(f"{doc}:{n}: phrase-link — a term link inside a protected phrase")

        used: set[str] = set()
        for n, line in body:
            for txt, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", line):
                if not (target.startswith("#") or ".md#" in target):
                    continue
                for term in ordered:
                    if re.fullmatch(pattern_for(term), txt, re.I):
                        if target != terms[term]:
                            findings.append(f"{doc}:{n}: wrong-anchor '{txt}' → {target}, expected {terms[term]}")
                        if txt[0] != txt[0].upper():
                            findings.append(f"{doc}:{n}: lowercase-link '[{txt}]' → '[{txt[0].upper() + txt[1:]}]'")
                        used.add(term)
                        break
                tdoc, _, frag = target.partition("#")
                tdoc = tdoc or doc
                if tdoc in anchors and frag not in anchors[tdoc]:
                    findings.append(f"{doc}:{n}: dead-anchor {target}")
        for term in own[doc]:
            if term not in used:
                findings.append(f"{doc}: never-used '{term}'")

        for n, line in body:
            plain = blank_protected(line)
            if "out of scope" in plain.lower():
                continue
            for pat, why in SCOPE_LEAKS.items():
                if re.search(pat, plain):
                    findings.append(f"{doc}:{n}: scope-leak — {why}")
            for pat, canonical in SYNONYMS.items():
                if re.search(pat, plain):
                    findings.append(f"{doc}:{n}: synonym — use '{canonical}'")

        section = ""
        for n, line in enumerate(text.splitlines(), 1):
            if line.startswith("## "):
                section = line
            if re.search(r"\b(MUST|SHOULD|MAY)\b", line) and "RFC 2119" not in line:
                if not re.match(r"^## (\d|Appendix)", section):
                    findings.append(f"{doc}:{n}: rfc-placement in '{section.strip('# ')}'")
    return findings



# --------------------------------------------------------------------------- main


def main(argv: list[str]) -> int:
    here = Path(__file__).resolve().parent
    findings = check(here)
    if findings:
        kinds: dict[str, int] = {}
        for f in findings:
            k = re.search(r": ([a-z-]+)( |'|—)", f)
            key = k.group(1) if k else "other"
            kinds[key] = kinds.get(key, 0) + 1
        print(f"{len(findings)} finding(s): " + ", ".join(f"{k} {v}" for k, v in sorted(kinds.items())))
        for f in findings:
            print("  " + f)
        return 1
    print("spec-qa: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
