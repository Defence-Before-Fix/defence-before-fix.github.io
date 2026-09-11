#!/usr/bin/env python3
"""Every place a specification's version is written agrees with every other.

A document's version appears in its header, in the companion line of the other two
documents, in the method specification's status paragraph and citation, in the closing
changelog table, in CHANGELOG.md and, for the method specification, in package.json,
which PUBLISHING.md says tracks it. A version with a pre-release suffix such as
`1.1.0-dev` is an editor's draft: its header says `unpublished` rather than naming a
date, and CHANGELOG.md carries an `Unreleased` entry for the document.

Findings:
  version-header      a document has no parseable '**Version**:' line
  version-mention     the status paragraph or citation names a different version
  version-table       the closing changelog table's last row is not the header version
  version-companion   another document's companion line names a different version
  version-changelog   CHANGELOG.md's latest entry for the document is not the header version and date,
                      or a pre-release version has no Unreleased entry
  version-unaccepted  the latest published entry has no cohort record, so it is not published
  version-package     package.json's version, or composer.json's if it carries one, is not the
                      method specification's (Packagist reads tags, so composer.json normally has none)
  version-prerelease  a pre-release version claims a publication date
  manifest-drift      package.json and composer.json disagree on description, licence, homepage or keywords
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

DOCS = ["SPEC.md", "DETECTOR-SPEC.md", "TOOLING-SPEC.md"]
VERSION = r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.]+)?"
HEADER = re.compile(rf"^\*\*Version\*\*: ({VERSION}), (?:published (\d{{4}}-\d{{2}}-\d{{2}})|unpublished)\s*$", re.M)
COMPANION = re.compile(rf"\]\((SPEC\.md|DETECTOR-SPEC\.md|TOOLING-SPEC\.md)\), version ({VERSION})")
STATUS = re.compile(rf"^This is version ({VERSION}) of the specification", re.M)
CITATION = re.compile(rf"^> Edmonds, Joseph\. .*?, version ({VERSION})\.", re.M)
TABLE_ROW = re.compile(rf"^\| ({VERSION})\s+\| (\d{{4}}-\d{{2}}-\d{{2}}) \|", re.M)
CHANGELOG_DOC = re.compile(r"^## .*\((SPEC\.md|DETECTOR-SPEC\.md|TOOLING-SPEC\.md)\)\s*$", re.M)
CHANGELOG_ENTRY = re.compile(rf"^### (?:({VERSION}), (\d{{4}}-\d{{2}}-\d{{2}})|(Unreleased))\s*$", re.M)
COHORT = re.compile(r"\bcohort\b", re.I)
MANIFESTS = ["package.json", "composer.json"]
SHARED_FIELDS = ["description", "license", "homepage", "keywords"]
FINDING_KIND = re.compile(r": ([a-z-]+)( |—|$)")


@dataclass(frozen=True)
class Head:
    version: str
    date: str | None

    @property
    def prerelease(self) -> bool:
        return "-" in self.version


@dataclass(frozen=True)
class Entry:
    version: str | None
    date: str | None
    body: str

    @property
    def unreleased(self) -> bool:
        return self.version is None


def kind_of(finding: str) -> str:
    m = FINDING_KIND.search(finding)
    return m.group(1) if m else "other"


def header(text: str) -> tuple[str, str | None] | None:
    m = HEADER.search(text)
    return (m.group(1), m.group(2)) if m else None


def changelog_entries(text: str) -> dict[str, list[Entry]]:
    """Per document, its entries in file order."""
    out: dict[str, list[Entry]] = {}
    sections = list(CHANGELOG_DOC.finditer(text))
    for i, sec in enumerate(sections):
        end = sections[i + 1].start() if i + 1 < len(sections) else len(text)
        chunk = text[sec.end():end]
        entries = list(CHANGELOG_ENTRY.finditer(chunk))
        rows = []
        for j, e in enumerate(entries):
            body_end = entries[j + 1].start() if j + 1 < len(entries) else len(chunk)
            rows.append(Entry(e.group(1), e.group(2), chunk[e.end():body_end]))
        out[sec.group(1)] = rows
    return out


def check_document(doc: str, text: str, head: Head, versions: dict[str, str]) -> list[str]:
    out: list[str] = []
    if head.prerelease and head.date:
        out.append(f"{doc}: version-prerelease — {head.version} is a pre-release and cannot name a publication date")
    for m in COMPANION.finditer(text):
        other, named = m.group(1), m.group(2)
        if other in versions and named != versions[other]:
            out.append(f"{doc}: version-companion — names {other} {named}, but {other} is {versions[other]}")
    for pat, what in ((STATUS, "status paragraph"), (CITATION, "citation")):
        for m in pat.finditer(text):
            if m.group(1) != head.version:
                out.append(f"{doc}: version-mention — {what} says {m.group(1)}, header says {head.version}")
    rows = TABLE_ROW.findall(text)
    if rows and not head.prerelease:
        last_v, last_d = rows[-1]
        if (last_v, last_d) != (head.version, head.date):
            out.append(f"{doc}: version-table — closing table ends at {last_v} ({last_d}), header says {head.version} ({head.date})")
    return out


def check_changelog(doc: str, head: Head, entries: list[Entry]) -> list[str]:
    if head.prerelease:
        if not any(e.unreleased for e in entries):
            return [f"CHANGELOG.md: version-changelog — {doc} is {head.version} but has no 'Unreleased' entry"]
        return []
    released = [e for e in entries if not e.unreleased]
    if not released:
        return [f"CHANGELOG.md: version-changelog — no entry for {doc}"]
    latest = released[0]
    if (latest.version, latest.date) != (head.version, head.date):
        return [f"CHANGELOG.md: version-changelog — latest {doc} entry is {latest.version} ({latest.date}), header says {head.version} ({head.date})"]
    if not COHORT.search(latest.body):
        return [f"CHANGELOG.md: version-unaccepted — {doc} {head.version} entry records no cohort, so it is not published"]
    return []


def check(root: Path) -> list[str]:
    out: list[str] = []
    texts = {d: (root / d).read_text() for d in DOCS if (root / d).exists()}
    heads: dict[str, Head] = {}
    for d, t in texts.items():
        h = header(t)
        if h is None:
            out.append(f"{d}: version-header — no '**Version**: X, published DATE' or ', unpublished' line")
        else:
            heads[d] = Head(*h)
    versions = {d: h.version for d, h in heads.items()}

    for d, head in heads.items():
        out += check_document(d, texts[d], head, versions)

    changelog = root / "CHANGELOG.md"
    entries = changelog_entries(changelog.read_text()) if changelog.exists() else {}
    for d, head in heads.items():
        out += check_changelog(d, head, entries.get(d, []))

    manifests = {m: json.loads((root / m).read_text()) for m in MANIFESTS if (root / m).exists()}
    if "SPEC.md" in versions:
        for name, data in manifests.items():
            pv = data.get("version")
            if (name == "package.json" or pv is not None) and pv != versions["SPEC.md"]:
                out.append(f"{name}: version-package — {pv}, but SPEC.md is {versions['SPEC.md']}")
    if len(manifests) == 2:
        pkg, composer = manifests["package.json"], manifests["composer.json"]
        for field in SHARED_FIELDS:
            if pkg.get(field) != composer.get(field):
                out.append(f"composer.json: manifest-drift — {field} differs from package.json")
    return out
