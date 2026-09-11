"""Tests for tools/changes.py: what a change to a specification must bring with it."""

from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
changes = importlib.import_module("changes")

BASE = """**Version**: 1.0.1, published 2026-09-08

## 2. Scope

The [Practitioner] MUST attempt the [Rule]. Prose without a keyword.

## 3. Method

### 3.1 Name

The [Practitioner] MUST name the [Class].
"""


def kinds(findings: list[str]) -> list[str]:
    return sorted(changes.kind_of(f) for f in findings)


class NormativeSentencesTest(unittest.TestCase):
    def test_extracts_keyword_sentences_from_numbered_sections_only(self) -> None:
        text = "Intro MUST not count.\n\n## 1. One\n\nA MUST here. Plain. A SHOULD there.\n\n## Appendix A\n\nAn appendix MAY.\n"
        self.assertEqual(
            changes.normative_sentences(text),
            ["A MUST here.", "A SHOULD there.", "An appendix MAY."],
        )

    def test_link_syntax_is_flattened(self) -> None:
        self.assertEqual(changes.normative_sentences("## 1. X\n\nThe [Rule](#rule) MUST fire.\n"), ["The Rule MUST fire."])


class ChangeSetTest(unittest.TestCase):
    def test_no_spec_change_is_clean(self) -> None:
        f = changes.check_set(
            base={"SPEC.md": BASE, "CHANGELOG.md": "old"},
            head={"SPEC.md": BASE, "CHANGELOG.md": "old", "README.md": "new"},
        )
        self.assertEqual(f, [])

    def test_wording_change_needs_a_changelog_entry(self) -> None:
        head = BASE.replace("Prose without a keyword.", "Prose with a new word.")
        f = changes.check_set(base={"SPEC.md": BASE, "CHANGELOG.md": "old"}, head={"SPEC.md": head, "CHANGELOG.md": "old"})
        self.assertEqual(kinds(f), ["change-unlogged"])

    def test_wording_change_with_changelog_entry_is_clean(self) -> None:
        head = BASE.replace("Prose without a keyword.", "Prose with a new word.")
        f = changes.check_set(base={"SPEC.md": BASE, "CHANGELOG.md": "old"}, head={"SPEC.md": head, "CHANGELOG.md": "old\nnew"})
        self.assertEqual(f, [])

    def test_new_obligation_on_a_published_version_needs_a_bump(self) -> None:
        head = BASE.replace("Prose without a keyword.", "The [Practitioner] MUST record it.")
        f = changes.check_set(base={"SPEC.md": BASE, "CHANGELOG.md": "old"}, head={"SPEC.md": head, "CHANGELOG.md": "old\nnew"})
        self.assertEqual(kinds(f), ["change-unversioned"])
        self.assertIn("MUST record it", f[0])

    def test_removed_obligation_also_needs_a_bump(self) -> None:
        head = BASE.replace("The [Practitioner] MUST name the [Class].\n", "")
        f = changes.check_set(base={"SPEC.md": BASE, "CHANGELOG.md": "old"}, head={"SPEC.md": head, "CHANGELOG.md": "old\nnew"})
        self.assertEqual(kinds(f), ["change-unversioned"])

    def test_new_obligation_with_prerelease_version_is_clean(self) -> None:
        head = BASE.replace("Prose without a keyword.", "The [Practitioner] MUST record it.").replace(
            "**Version**: 1.0.1, published 2026-09-08", "**Version**: 1.1.0-dev, unpublished"
        )
        f = changes.check_set(base={"SPEC.md": BASE, "CHANGELOG.md": "old"}, head={"SPEC.md": head, "CHANGELOG.md": "old\nnew"})
        self.assertEqual(f, [])

    def test_new_obligation_with_bumped_version_is_clean(self) -> None:
        head = BASE.replace("Prose without a keyword.", "The [Practitioner] MUST record it.").replace("1.0.1", "1.1.0")
        f = changes.check_set(base={"SPEC.md": BASE, "CHANGELOG.md": "old"}, head={"SPEC.md": head, "CHANGELOG.md": "old\nnew"})
        self.assertEqual(f, [])

    def test_reworded_obligation_with_same_count_is_a_wording_change(self) -> None:
        head = BASE.replace("MUST name the [Class]", "MUST name the [Class] first")
        f = changes.check_set(base={"SPEC.md": BASE, "CHANGELOG.md": "old"}, head={"SPEC.md": head, "CHANGELOG.md": "old\nnew"})
        self.assertEqual(kinds(f), ["change-obligation-reworded"])

    def test_added_document_counts_as_changed(self) -> None:
        f = changes.check_set(base={"CHANGELOG.md": "old"}, head={"SPEC.md": BASE, "CHANGELOG.md": "old"})
        self.assertEqual(kinds(f), ["change-unlogged"])


if __name__ == "__main__":
    unittest.main()
