#!/usr/bin/env python3
"""House style over the specification prose, checked mechanically.

The specifications are written in British English with a spaced hyphen where other
writers reach for a dash, and numbered so that a clause reference resolves. None of that
needs a reader to check; this module reports it line by line so the reviewer's attention
goes on what only a reader can judge.

Findings:
  em-dash              an em dash; use a spaced hyphen, a colon or a full stop
  en-dash              an en dash; use a spaced hyphen or 'to'
  while                'while' where the documents write 'whilst'
  ize-spelling         an -ize spelling; the documents use -ise
  us-spelling          an American spelling of a word the documents spell the British way
  trailing-whitespace  a line ending in spaces
  tab                  a tab character
  section-sequence     a '## N.' heading out of sequence
  clause-sequence      a '### N.M' heading whose N is not the enclosing section or whose M skips

Code spans, fenced code, link targets and a line that declares the US spelling of the
method's name are exempt.
"""

from __future__ import annotations

import re

EM_DASH = "—"
EN_DASH = "–"

IZE = re.compile(r"\b\w+(?:ize|izes|ized|izing|ization|izations)\b", re.I)
IZE_ALLOWED = {"size", "sizes", "sized", "sizing", "resize", "resizes", "resized", "resizing", "oversize", "oversized", "prize", "prizes", "prized", "seize", "seizes", "seized", "seizing", "capsize", "capsized", "capsizing", "downsize", "downsized", "downsizing"}

US_SPELLINGS = {
    "behavior": "behaviour", "behaviors": "behaviours",
    "color": "colour", "colors": "colours",
    "defense": "defence", "defenses": "defences",
    "center": "centre", "centers": "centres",
    "analyze": "analyse", "analyzes": "analyses", "analyzed": "analysed", "analyzing": "analysing",
    "catalog": "catalogue", "catalogs": "catalogues",
    "favor": "favour", "favors": "favours",
    "honor": "honour", "honors": "honours",
    "labor": "labour",
    "gray": "grey",
    "judgment": "judgement",
    "fulfill": "fulfil", "fulfills": "fulfils",
    "canceled": "cancelled", "canceling": "cancelling",
    "modeling": "modelling", "modeled": "modelled",
    "traveled": "travelled", "traveling": "travelling",
    "artifact": "artefact", "artifacts": "artefacts",
}
US_WORD = re.compile(r"\b(" + "|".join(sorted(US_SPELLINGS, key=len, reverse=True)) + r")\b", re.I)

PROTECT = re.compile(r"`[^`]*`|\]\([^)]*\)|https?://\S+|(?i:Defense Before Fix)")
SECTION = re.compile(r"^## (\d+)\. ")
CLAUSE = re.compile(r"^### (\d+)\.(\d+) ")
FINDING_KIND = re.compile(r":\d+: ([a-z-]+)")


def kind_of(finding: str) -> str:
    m = FINDING_KIND.search(finding)
    return m.group(1) if m else "other"


def prose_lines(text: str):
    """(line number, line) for every line outside fenced code."""
    in_code = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            yield n, line


def blank_protected(line: str) -> str:
    return PROTECT.sub(lambda m: " " * len(m.group()), line)


def check_text(doc: str, text: str) -> list[str]:
    out: list[str] = []
    section = 0
    clause = 0
    for n, raw in prose_lines(text):
        where = f"{doc}:{n}:"
        if raw.rstrip() != raw:
            out.append(f"{where} trailing-whitespace")
        if "\t" in raw:
            out.append(f"{where} tab")

        m = SECTION.match(raw)
        if m:
            number = int(m.group(1))
            if number != section + 1:
                out.append(f"{where} section-sequence — '## {number}.' follows section {section}")
            section = number
            clause = 0
        m = CLAUSE.match(raw)
        if m:
            major, minor = int(m.group(1)), int(m.group(2))
            if major != section:
                out.append(f"{where} clause-sequence — '### {major}.{minor}' sits under section {section}")
            elif minor != clause + 1:
                out.append(f"{where} clause-sequence — '### {major}.{minor}' follows clause {major}.{clause}")
            clause = minor if major == section else clause

        line = blank_protected(raw)
        if EM_DASH in line:
            out.append(f"{where} em-dash — use a spaced hyphen, a colon or a full stop")
        if EN_DASH in line:
            out.append(f"{where} en-dash — use a spaced hyphen or 'to'")
        if re.search(r"\bwhile\b", line, re.I):
            out.append(f"{where} while — the documents write 'whilst'")
        for m in IZE.finditer(line):
            if m.group().lower() not in IZE_ALLOWED:
                out.append(f"{where} ize-spelling '{m.group()}' — use -ise")
        if "US spelling" in raw:
            continue
        for m in US_WORD.finditer(line):
            out.append(f"{where} us-spelling '{m.group()}' — use {US_SPELLINGS[m.group().lower()]}")
    return out
