#!/usr/bin/env python3
"""The acceptance answer keys quote the document they mark against.

Each KEY.md under acceptance/ says its quotations are from the document and must be
updated in the same commit as any rewording. A stale quotation makes a reader who
answers from the current text fail the key, which is the test failing rather than the
document. Quotations of six words or more are checked for a verbatim match after link
syntax is flattened and whitespace collapsed; shorter ones are too common to be quotes.

Findings:
  key-quote-stale   a quotation in a key does not appear in the document
  key-dead-anchor   a key links to a heading the document does not have
"""

from __future__ import annotations

import re
from pathlib import Path

KEY_DOC = {"method": "SPEC.md", "detector": "DETECTOR-SPEC.md", "toolchain": "TOOLING-SPEC.md"}
QUOTE = re.compile(r'"([^"]{20,}?)"', re.S)
LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)|\[([^\]]+)\](?:\[[^\]]*\])?")
ANCHOR_LINK = re.compile(r"\]\((?:\.\./)*([A-Z-]+\.md)#([^)]+)\)")
HEADING = re.compile(r"^#{1,6} (.+)$", re.M)
MIN_WORDS = 6
FINDING_KIND = re.compile(r":\d+: ([a-z-]+)")


def kind_of(finding: str) -> str:
    m = FINDING_KIND.search(finding)
    return m.group(1) if m else "other"


def flatten(text: str) -> str:
    text = LINK.sub(lambda m: m.group(1) or m.group(2), text)
    text = text.replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", text).strip()


def anchor(heading: str) -> str:
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading).lower()
    return re.sub(r"[^a-z0-9 -]", "", text).replace(" ", "-")


def quotations(text: str) -> list[tuple[int, str]]:
    out = []
    for m in QUOTE.finditer(text):
        q = flatten(m.group(1))
        if len(q.split()) >= MIN_WORDS:
            out.append((text.count("\n", 0, m.start()) + 1, q))
    return out


def check_key(path: str, key: str, docs: dict[str, str], doc: str) -> list[str]:
    out: list[str] = []
    flat = flatten(docs[doc])
    for line, q in quotations(key):
        if q not in flat:
            out.append(f"{path}:{line}: key-quote-stale — not in {doc}: '{q[:80]}'")
    anchors = {d: {anchor(h) for h in HEADING.findall(t)} for d, t in docs.items()}
    for n, raw in enumerate(key.splitlines(), 1):
        for m in ANCHOR_LINK.finditer(raw):
            target, frag = m.group(1), m.group(2)
            if target in anchors and frag not in anchors[target]:
                out.append(f"{path}:{n}: key-dead-anchor — {target}#{frag}")
    return out


def check(root: Path) -> list[str]:
    docs = {d: (root / d).read_text() for d in KEY_DOC.values() if (root / d).exists()}
    out: list[str] = []
    for kind, doc in KEY_DOC.items():
        key = root / "acceptance" / kind / "KEY.md"
        if key.exists() and doc in docs:
            out += check_key(str(key.relative_to(root)), key.read_text(), docs, doc)
    return out
