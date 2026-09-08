"""Tests for tools/clauses.py: clause anchors, resolution and linkification."""

from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
clauses = importlib.import_module("clauses")


class AnchorTest(unittest.TestCase):
    def test_anchor_follows_the_site_renderer(self) -> None:
        self.assertEqual(
            clauses.anchor("6.5 One page MAY document a family of identifiers, and SHOULD name its members so a check can confirm them"),
            "65-one-page-may-document-a-family-of-identifiers-and-should-name-its-members-so-a-check-can-confirm-them",
        )
        self.assertEqual(clauses.anchor("4.4 The toolchain's own invocation"), "44-the-toolchains-own-invocation")
        self.assertEqual(
            clauses.anchor("4.1 Every detector MUST conform to the [detector specification](DETECTOR-SPEC.md)"),
            "41-every-detector-must-conform-to-the-detector-specification",
        )
        self.assertEqual(clauses.anchor("3. The method"), "3-the-method")

    def test_headings_are_read_from_the_documents(self) -> None:
        h = clauses.headings()
        self.assertEqual(h["method"]["3.1"], "31-attribute-the-defect-to-a-class")
        self.assertEqual(h["detector"]["6"], "6-resolving-an-identifier")
        self.assertIn("9.2", h["toolchain"])
        self.assertNotIn("9.3", h["toolchain"])


class LinkifyTest(unittest.TestCase):
    def test_bare_clause_uses_the_default_document(self) -> None:
        out = clauses.linkify("fails 6.2 and 6.3.", default="detector", rel="../")
        self.assertEqual(
            out,
            "fails [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)"
            " and [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together).",
        )

    def test_qualifier_selects_the_document(self) -> None:
        out = clauses.linkify("fails toolchain 4.1 and detector clause 6.3", default="method", rel="")
        self.assertIn("[4.1](TOOLING-SPEC.md#41-", out)
        self.assertIn("[6.3](DETECTOR-SPEC.md#63-", out)

    def test_clause_word_and_sections(self) -> None:
        out = clauses.linkify("clause 3.1 and sections 4 to 7", default="method", rel="")
        self.assertIn("clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class)", out)
        self.assertIn("sections [4](SPEC.md#4-authority-which-decisions-belong-to-whom) to [7](SPEC.md#7-conformance)", out)

    def test_existing_links_code_and_versions_are_left_alone(self) -> None:
        text = "version 2.2.13, PHP 8.4, `rule 4.1`, [4.1](../DETECTOR-SPEC.md#41-x), Attribution 4.0 and 0.2.0"
        self.assertEqual(clauses.linkify(text, default="detector", rel="../"), text)

    def test_table_row_document_column_governs_the_clause_cell_only(self) -> None:
        row = "| Toolchain | 4.1    | No     | as wrapped fails 5.2 |"
        out = clauses.linkify(row, default="detector", rel="../")
        self.assertIn("[4.1](../TOOLING-SPEC.md#41-", out)
        self.assertIn("[5.2](../DETECTOR-SPEC.md#52-", out)

    def test_qualifier_governs_the_rest_of_the_paragraph(self) -> None:
        out = clauses.linkify("Under detector clause 4.1 rules enter. Clause 4.2 is the harness.", default="toolchain", rel="")
        self.assertIn("[4.2](DETECTOR-SPEC.md#42-", out)

    def test_qualifier_carries_across_a_list(self) -> None:
        out = clauses.linkify("detector clauses 4.2, 5.2 and 6.1, which fails toolchain 4.1", default="method", rel="")
        self.assertIn("[5.2](DETECTOR-SPEC.md#52-", out)
        self.assertIn("[6.1](DETECTOR-SPEC.md#61-", out)
        self.assertIn("[4.1](TOOLING-SPEC.md#41-", out)


class CheckTest(unittest.TestCase):
    def test_unlinked_and_dead_links_are_reported(self) -> None:
        text = "fails 6.2 and [6.3](../DETECTOR-SPEC.md#63-wrong) and [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)"
        findings = clauses.check(text, default="detector", rel="../")
        kinds = sorted(f.kind for f in findings)
        self.assertEqual(kinds, ["dead-clause-link", "unlinked-clause"])
        self.assertEqual(findings[0].line, 1)

    def test_segments_for_the_register(self) -> None:
        segs = clauses.segments("fails 6.2; see toolchain 4.1", default="detector", base="/")
        self.assertEqual(segs[0], {"text": "fails "})
        self.assertEqual(segs[1]["text"], "6.2")
        self.assertTrue(segs[1]["href"].startswith("/DETECTOR-SPEC.html#62-"))
        self.assertTrue(segs[3]["href"].startswith("/TOOLING-SPEC.html#41-"))


if __name__ == "__main__":
    unittest.main()
