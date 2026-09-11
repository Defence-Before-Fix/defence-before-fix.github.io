"""Tests for tools/versions.py: every place a version is written agrees."""

from __future__ import annotations

import importlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
versions = importlib.import_module("versions")

SPEC = """# Defence Before Fix

**Version**: {v}, published {d}
**Companion to**: [the detector specification](DETECTOR-SPEC.md), version {dv}, and [the toolchain specification](TOOLING-SPEC.md), version {tv}

This is version {v} of the specification. It is normative.

## 1. Terminology

## 9. Citation

> Edmonds, Joseph. *Defence Before Fix*, version {cite}. First published 22 February 2026.

## Changelog

| Version | Date       | Change |
| ------- | ---------- | ------ |
| 1.0.0   | 2026-09-08 | Initial |
| {tv_row} | {d} | Later |
"""

DETECTOR = """# Detector

**Version**: {v}, published {d}
**Companion to**: [the method specification](SPEC.md), version {mv}, and [the toolchain specification](TOOLING-SPEC.md), version {tv}
"""

TOOLING = """# Toolchain

**Version**: {v}, published {d}
**Companion to**: [the method specification](SPEC.md), version {mv}, and [the detector specification](DETECTOR-SPEC.md), version {dv}
"""

CHANGELOG = """# Changelog

## Method specification (SPEC.md)

### {mv}, {d}

Accepted by a cold cohort of five Haiku readers.

### 1.0.0, 2026-09-08

Initial.

## Detector specification (DETECTOR-SPEC.md)

### {dv}, {d}

Accepted by a cold cohort of five Haiku readers.

## Toolchain specification (TOOLING-SPEC.md)

### {tv}, {d}

Accepted by a cold cohort of five Haiku readers.
"""


def write_repo(root: Path, *, spec_v="1.0.1", cite=None, table=None, pkg=None, changelog=None, spec_date="2026-09-08") -> None:
    cite = cite or spec_v
    table = table or spec_v
    (root / "SPEC.md").write_text(SPEC.format(v=spec_v, d=spec_date, dv="1.0.0", tv="0.2.0", cite=cite, tv_row=table))
    (root / "DETECTOR-SPEC.md").write_text(DETECTOR.format(v="1.0.0", d="2026-09-08", mv=spec_v, tv="0.2.0"))
    (root / "TOOLING-SPEC.md").write_text(TOOLING.format(v="0.2.0", d="2026-09-08", mv=spec_v, dv="1.0.0"))
    (root / "CHANGELOG.md").write_text(changelog or CHANGELOG.format(mv=spec_v, dv="1.0.0", tv="0.2.0", d=spec_date))
    manifest = {"description": "Spec.", "license": "CC-BY-4.0", "homepage": "https://x", "keywords": ["a", "b"]}
    (root / "package.json").write_text(json.dumps({"name": "@x/y", "version": pkg or spec_v, **manifest}))
    (root / "composer.json").write_text(json.dumps({"name": "x/y", **manifest}))


def kinds(findings: list[str]) -> list[str]:
    return sorted(versions.kind_of(f) for f in findings)


class ConsistentRepoTest(unittest.TestCase):
    def test_consistent_repo_is_clean(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            write_repo(Path(d))
            self.assertEqual(versions.check(Path(d)), [])


class DriftTest(unittest.TestCase):
    def test_status_and_citation_drift(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            write_repo(Path(d), cite="1.0.0")
            self.assertEqual(kinds(versions.check(Path(d))), ["version-mention"])

    def test_closing_table_drift(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            write_repo(Path(d), table="1.0.0")
            self.assertEqual(kinds(versions.check(Path(d))), ["version-table"])

    def test_package_json_drift(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            write_repo(Path(d), pkg="1.0.0")
            self.assertEqual(kinds(versions.check(Path(d))), ["version-package"])

    def test_composer_version_if_present_must_match(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            write_repo(Path(d))
            c = json.loads(Path(d, "composer.json").read_text())
            c["version"] = "1.0.0"
            Path(d, "composer.json").write_text(json.dumps(c))
            self.assertEqual(kinds(versions.check(Path(d))), ["version-package"])

    def test_manifests_must_agree_on_shared_fields(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            write_repo(Path(d))
            c = json.loads(Path(d, "composer.json").read_text())
            c["license"] = "MIT"
            c["keywords"] = ["a"]
            Path(d, "composer.json").write_text(json.dumps(c))
            f = versions.check(Path(d))
            self.assertEqual(kinds(f), ["manifest-drift", "manifest-drift"])
            self.assertIn("license", f[0] + f[1])

    def test_companion_drift(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            write_repo(Path(d))
            root = Path(d)
            root.joinpath("DETECTOR-SPEC.md").write_text(DETECTOR.format(v="1.0.0", d="2026-09-08", mv="1.0.0", tv="0.2.0"))
            f = versions.check(root)
            self.assertEqual(kinds(f), ["version-companion"])
            self.assertIn("DETECTOR-SPEC.md", f[0])

    def test_changelog_latest_entry_must_match_header(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            write_repo(Path(d), changelog=CHANGELOG.format(mv="1.0.0", dv="1.0.0", tv="0.2.0", d="2026-09-08").replace("### 1.0.0, 2026-09-08\n\nAccepted by a cold cohort of five Haiku readers.\n\n### 1.0.0", "### 1.0.0"))
            self.assertEqual(kinds(versions.check(Path(d))), ["version-changelog"])

    def test_changelog_date_must_match_header(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            write_repo(Path(d), changelog=CHANGELOG.format(mv="1.0.1", dv="1.0.0", tv="0.2.0", d="2026-09-08").replace("### 1.0.1, 2026-09-08", "### 1.0.1, 2026-09-09"))
            self.assertEqual(kinds(versions.check(Path(d))), ["version-changelog"])

    def test_published_version_without_cohort_line(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            write_repo(Path(d), changelog=CHANGELOG.format(mv="1.0.1", dv="1.0.0", tv="0.2.0", d="2026-09-08").replace("Accepted by a cold cohort of five Haiku readers.", "Reworded.", 1))
            self.assertEqual(kinds(versions.check(Path(d))), ["version-unaccepted"])


class PreReleaseTest(unittest.TestCase):
    def test_dev_version_is_unpublished_and_has_an_unreleased_entry(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            write_repo(root, spec_v="1.1.0-dev", spec_date="2026-09-08")
            text = root.joinpath("SPEC.md").read_text().replace("**Version**: 1.1.0-dev, published 2026-09-08", "**Version**: 1.1.0-dev, unpublished")
            root.joinpath("SPEC.md").write_text(text)
            root.joinpath("CHANGELOG.md").write_text(
                CHANGELOG.format(mv="1.0.1", dv="1.0.0", tv="0.2.0", d="2026-09-08").replace(
                    "## Method specification (SPEC.md)\n", "## Method specification (SPEC.md)\n\n### Unreleased\n\n- A new obligation.\n"
                )
            )
            self.assertEqual(versions.check(root), [])

    def test_dev_version_must_not_claim_a_publication_date(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            write_repo(root, spec_v="1.1.0-dev")
            self.assertIn("version-prerelease", kinds(versions.check(root)))

    def test_dev_version_needs_an_unreleased_entry(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            write_repo(root, spec_v="1.1.0-dev")
            text = root.joinpath("SPEC.md").read_text().replace("**Version**: 1.1.0-dev, published 2026-09-08", "**Version**: 1.1.0-dev, unpublished")
            root.joinpath("SPEC.md").write_text(text)
            root.joinpath("CHANGELOG.md").write_text(CHANGELOG.format(mv="1.0.1", dv="1.0.0", tv="0.2.0", d="2026-09-08"))
            self.assertEqual(kinds(versions.check(root)), ["version-changelog"])


class ParseTest(unittest.TestCase):
    def test_header_parses_published_and_unpublished(self) -> None:
        self.assertEqual(versions.header("**Version**: 1.0.1, published 2026-09-08\n"), ("1.0.1", "2026-09-08"))
        self.assertEqual(versions.header("**Version**: 1.1.0-dev, unpublished\n"), ("1.1.0-dev", None))
        self.assertIsNone(versions.header("no header\n"))


if __name__ == "__main__":
    unittest.main()
