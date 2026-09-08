#!/usr/bin/env python3
"""Clause references on the pages that talk about the specifications.

Every page other than the three specifications themselves must link each clause or
section number it mentions to that heading on the specification page. This module is
the one place that knows how: it reads the numbered headings of the three documents,
derives each heading's anchor the way the site renderer does, resolves a reference to
a document, and either rewrites the text with links (`linkify`, `segments`) or reports
what is unlinked or dead (`check`).

A reference is resolved to a document by, in order: a table row whose first cell names
the document; a qualifier before the number (`detector 6.3`, `toolchain clause 4.1`,
`method specification section 7`); the most recent qualifier in the same sentence, so a
list such as `detector clauses 4.2, 5.2 and 6.1` links every member; and otherwise the
page's default document. Numbers that are not a heading in the resolved document are
left alone, which keeps version numbers and licence names out of it.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = {"method": "SPEC.md", "detector": "DETECTOR-SPEC.md", "toolchain": "TOOLING-SPEC.md"}
FILE_TO_DOC = {v: k for k, v in DOCS.items()}

HEADING = re.compile(r"^(#{2,3}) (\d+(?:\.\d+)?)\.? (.+)$", re.M)
MD_LINK_TEXT = re.compile(r"\[([^\]]*)\]\([^)]*\)")
# What the site renderer keeps of a heading when it makes the id.
NON_ID = re.compile(r"[^a-z0-9 -]")

QUALIFIER = r"(?P<doc>method|detector|toolchain)(?:[ '’]s|['’]s)?(?: specification(?:['’]s)?| document(?:['’]s)?)?"
WORD = r"(?P<word>clauses?|sections?)"
NUMBER = r"(?P<num>\d+\.\d+|\d+)"
# A number that is a clause or section reference and not a version, a licence or a year:
# not preceded by a word character, a dot or a digit, and not followed by another dot-number.
BARE = r"(?<![\w.])" + NUMBER + r"(?![\w.]\w|\.\d)"
REFERENCE = re.compile(
    rf"(?:{QUALIFIER}\s+)?(?:{WORD}\s+)?{BARE}",
    re.I,
)
PROTECTED = re.compile(r"`[^`]*`|\[[^\]]*\]\([^)]*\)|\[[^\]]*\]\[[^\]]*\]|https?://\S+")
# A number after one of these is a version, a licence or a release, never a clause. Lintomatic is
# the acceptance fixture's detector, whose name carries its version.
VERSION_WORDS = re.compile(r"(?:version|v|since|from|at|php|python|node|go|zig|rust|typescript|attribution|lintomatic)\s*$", re.I)
SENTENCE_END = re.compile(r"[.;:!?]\s|\n")
TABLE_DOC = re.compile(r"^\|\s*(Method|Detector|Toolchain)\s*\|", re.I)
LINK = re.compile(r"\[([^\]]+)\]\(([^)#]*)#([^)]+)\)")


def anchor(heading: str) -> str:
    """The id the site renderer gives a heading: lowercase, only letters, digits, spaces and
    hyphens kept, spaces to hyphens. Link syntax inside a heading contributes its text."""
    text = MD_LINK_TEXT.sub(r"\1", heading).lower()
    return NON_ID.sub("", text).replace(" ", "-")


@lru_cache(maxsize=None)
def headings() -> dict[str, dict[str, str]]:
    """{doc: {number: anchor}} for every numbered section and clause heading."""
    out: dict[str, dict[str, str]] = {}
    for doc, name in DOCS.items():
        text = (ROOT / name).read_text()
        out[doc] = {m.group(2): anchor(m.group(0).lstrip("# ")) for m in HEADING.finditer(text)}
    return out


@dataclass
class Ref:
    start: int
    end: int
    number: str
    doc: str


def _protected_spans(text: str) -> list[tuple[int, int]]:
    return [(m.start(), m.end()) for m in PROTECTED.finditer(text)]


def _inside(pos: int, spans: list[tuple[int, int]]) -> bool:
    return any(s <= pos < e for s, e in spans)


def references(text: str, default: str) -> list[Ref]:
    """Every clause or section number in `text` that resolves to a heading, with its document,
    excluding numbers inside code, links and URLs."""
    spans = _protected_spans(text)
    table_doc = None
    m = TABLE_DOC.match(text)
    if m:
        table_doc = m.group(1).lower()
    refs: list[Ref] = []
    carried: str | None = None
    carried_until = -1
    sections_until = -1
    for m in REFERENCE.finditer(text):
        num_start = m.start("num")
        if _inside(num_start, spans):
            continue
        before = text[: m.start()]
        if VERSION_WORDS.search(before[-14:]) and m.group("doc") is None and m.group("word") is None:
            continue
        number = m.group("num")
        if m.group("doc"):
            # A qualifier governs the rest of the paragraph, until the next qualifier.
            doc = m.group("doc").lower()
            carried, carried_until = doc, len(text)
        elif table_doc and not refs:
            # The document column governs the clause column, not the evidence cell after it.
            doc = table_doc
        elif carried and num_start <= carried_until:
            doc = carried
        else:
            doc = default
        if "." not in number:
            # A bare integer is a section only after the word "section(s)", or in the list that word opens.
            if m.group("word") and m.group("word").lower().startswith("section"):
                end = SENTENCE_END.search(text, m.end())
                sections_until = end.start() if end else len(text)
            elif num_start > sections_until:
                continue
        if number not in headings()[doc]:
            continue
        refs.append(Ref(num_start, m.end("num"), number, doc))
    return refs


def target(ref: Ref, rel: str) -> str:
    return f"{rel}{DOCS[ref.doc]}#{headings()[ref.doc][ref.number]}"


def linkify(text: str, default: str, rel: str) -> str:
    """Markdown with every resolvable reference turned into a link relative to `rel`."""
    out = []
    pos = 0
    for line in text.splitlines(keepends=True):
        body = line
        for ref in reversed(references(body, default)):
            body = body[: ref.start] + f"[{ref.number}]({target(ref, rel)})" + body[ref.end :]
        out.append(body)
        pos += len(line)
    return "".join(out)


def segments(text: str, default: str, base: str) -> list[dict[str, str]]:
    """The text as plain and linked segments, for a renderer that must not take HTML."""
    segs: list[dict[str, str]] = []
    pos = 0
    for ref in references(text, default):
        if ref.start > pos:
            segs.append({"text": text[pos : ref.start]})
        page = DOCS[ref.doc].replace(".md", ".html")
        segs.append({"text": ref.number, "href": f"{base}{page}#{headings()[ref.doc][ref.number]}"})
        pos = ref.end
    if pos < len(text):
        segs.append({"text": text[pos:]})
    return segs


@dataclass
class Finding:
    kind: str
    line: int
    detail: str


def check(text: str, default: str, rel: str) -> list[Finding]:
    """`unlinked-clause` for every reference outside a link; `dead-clause-link` for every link
    into a specification whose fragment is not a heading there."""
    findings: list[Finding] = []
    for n, line in enumerate(text.splitlines(), 1):
        for ref in references(line, default):
            findings.append(Finding("unlinked-clause", n, f"{ref.number} should link to {target(ref, rel)}"))
        for m in LINK.finditer(line):
            name = Path(m.group(2)).name
            if name not in FILE_TO_DOC:
                continue
            doc = FILE_TO_DOC[name]
            if m.group(3) not in headings()[doc].values() and m.group(3) not in _term_anchors(doc):
                findings.append(Finding("dead-clause-link", n, f"[{m.group(1)}]({m.group(2)}#{m.group(3)}) points at no heading"))
    return findings


# --------------------------------------------------------------------------- pages

# Every page that talks about the specifications, with the document an unqualified number
# refers to there. The specifications themselves are not on this list: their own text is
# governed by the acceptance test, and their cross-references carry their own links.
PAGE_DEFAULTS = {
    "index.md": "method",
    "README.md": "method",
    "PRIMER.md": "method",
    "PROVENANCE.md": "method",
    "PUBLISHING.md": "method",
    "ACCEPTANCE.md": "method",
    "CHANGELOG.md": "method",
    "acceptance/README.md": "method",
    "acceptance/method/QUESTIONS.md": "method",
    "acceptance/method/KEY.md": "method",
    "acceptance/detector/QUESTIONS.md": "detector",
    "acceptance/detector/KEY.md": "detector",
    "acceptance/toolchain/QUESTIONS.md": "toolchain",
    "acceptance/toolchain/KEY.md": "toolchain",
    "tools/index.md": "detector",
}
SECTION_SWITCH = re.compile(r"^## (Method|Detector|Toolchain) specification", re.I)
KIND = re.compile(r"^kind: (tool|toolchain)\b", re.M)


def pages() -> list[Path]:
    """Every page the clause-link rule covers, relative to the repository root."""
    listed = [Path(p) for p in PAGE_DEFAULTS]
    tool_pages = sorted(p.relative_to(ROOT) for p in (ROOT / "tools").glob("*.md") if p.name != "index.md")
    return listed + tool_pages


def page_default(path: Path) -> str:
    """The document an unqualified number refers to on this page."""
    key = str(path)
    if key in PAGE_DEFAULTS:
        return PAGE_DEFAULTS[key]
    if path.parts[0] == "tools":
        m = KIND.search((ROOT / path).read_text())
        return "toolchain" if m and m.group(1) == "toolchain" else "detector"
    raise ValueError(f"{path}: not a page the clause rule covers")


def rel_for(path: Path) -> str:
    """The relative prefix from this page to the repository root, for markdown links."""
    return "../" * (len(path.parts) - 1)


def page_findings(path: Path) -> list[Finding]:
    """`check` over a page, switching the default document at the changelog's per-document
    headings so its entries resolve to the document they describe."""
    text = (ROOT / path).read_text()
    default = page_default(path)
    rel = rel_for(path)
    findings: list[Finding] = []
    in_front_matter = False
    for n, line in enumerate(text.splitlines(), 1):
        # Front matter stays plain text: the register generator links the summary itself.
        if n == 1 and line.strip() == "---":
            in_front_matter = True
            continue
        if in_front_matter:
            in_front_matter = line.strip() != "---"
            continue
        m = SECTION_SWITCH.match(line)
        if m:
            default = m.group(1).lower()
        if line.startswith("#"):
            continue
        for f in check(line, default, rel):
            findings.append(Finding(f.kind, n, f.detail))
    return findings


def link_page(path: Path) -> str:
    """The page with every resolvable reference linked, the same way `page_findings` reads it."""
    text = (ROOT / path).read_text()
    default = page_default(path)
    rel = rel_for(path)
    out = []
    in_front_matter = False
    for i, line in enumerate(text.splitlines(keepends=True)):
        if i == 0 and line.strip() == "---":
            in_front_matter = True
            out.append(line)
            continue
        if in_front_matter:
            out.append(line)
            if line.strip() == "---":
                in_front_matter = False
            continue
        m = SECTION_SWITCH.match(line)
        if m:
            default = m.group(1).lower()
        out.append(linkify(line, default, rel) if not line.startswith("#") else line)
    return "".join(out)


@lru_cache(maxsize=None)
def _term_anchors(doc: str) -> set[str]:
    """Every other heading anchor in a document, so links to terms are not reported as dead."""
    text = (ROOT / DOCS[doc]).read_text()
    return {anchor(m.group(1)) for m in re.finditer(r"^#{1,6} (.+)$", text, re.M)}
