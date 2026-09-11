#!/usr/bin/env python3
"""The acceptance answer keys quote the document they mark against.

Each KEY.md under acceptance/ says its quotations are from the document and must be
updated in the same commit as any rewording. A stale quotation makes a reader who
answers from the current text fail the key, which is the test failing rather than the
document. Quotations of six words or more are checked for a verbatim match after link
syntax and emphasis are flattened and whitespace collapsed; shorter ones are too common
to be quotes. Links from a key into a specification are checked by the clause-link rule
in clauses.py, which lists the keys among its pages.

Findings:
  key-quote-stale   a quotation in a key does not appear in the document
"""

from __future__ import annotations

import re
from pathlib import Path

import clauses

KEY_DOC = {"method": "SPEC.md", "detector": "DETECTOR-SPEC.md", "toolchain": "TOOLING-SPEC.md"}
# A quotation opens after the start, whitespace or an opening bracket and closes before
# whitespace, punctuation or the end, so a short quoted token such as "(none)" cannot
# pair with the next quote along and produce a phantom quotation.
QUOTE = re.compile(r'(?:(?<=^)|(?<=[\s(]))["“]([^"“”]{20,}?)["”](?=[\s.,;:)\]]|$)', re.S)
MIN_WORDS = 6
FINDING_KIND = re.compile(r":\d+: ([a-z-]+)")


def kind_of(finding: str) -> str:
    m = FINDING_KIND.search(finding)
    return m.group(1) if m else "other"


def flatten(text: str) -> str:
    return clauses.flatten(text)


def quotations(text: str) -> list[tuple[int, str]]:
    out = []
    for m in QUOTE.finditer(text):
        q = flatten(m.group(1))
        if len(q.split()) >= MIN_WORDS:
            out.append((text.count("\n", 0, m.start()) + 1, q))
    return out


def check_key(path: str, key: str, docs: dict[str, str], doc: str) -> list[str]:
    flat = flatten(docs[doc])
    return [
        f"{path}:{line}: key-quote-stale — not in {doc}: '{q[:80]}'"
        for line, q in quotations(key)
        if q not in flat
    ]


def check(root: Path) -> list[str]:
    docs = {d: (root / d).read_text() for d in KEY_DOC.values() if (root / d).exists()}
    out: list[str] = []
    for kind, doc in KEY_DOC.items():
        key = root / "acceptance" / kind / "KEY.md"
        if key.exists() and doc in docs:
            out += check_key(str(key.relative_to(root)), key.read_text(), docs, doc)
    return out
