"""Tests for tools/style.py: house style over the specification prose."""

from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
style = importlib.import_module("style")


def kinds(findings: list[str]) -> list[str]:
    return [style.kind_of(f) for f in findings]


class DashTest(unittest.TestCase):
    def test_em_dash_is_a_finding(self) -> None:
        f = style.check_text("SPEC.md", "A sentence — with an em dash.\n")
        self.assertEqual(kinds(f), ["em-dash"])
        self.assertIn("SPEC.md:1:", f[0])

    def test_en_dash_is_a_finding(self) -> None:
        self.assertEqual(kinds(style.check_text("SPEC.md", "pages 3–4\n")), ["en-dash"])

    def test_spaced_hyphen_is_fine(self) -> None:
        self.assertEqual(style.check_text("SPEC.md", "A sentence - with a spaced hyphen.\n"), [])

    def test_code_spans_and_fences_are_ignored(self) -> None:
        text = "Use `a — b` here.\n```\nx — y\n```\n"
        self.assertEqual(style.check_text("SPEC.md", text), [])


class SpellingTest(unittest.TestCase):
    def test_while_wants_whilst(self) -> None:
        f = style.check_text("SPEC.md", "Do this while waiting.\n")
        self.assertEqual(kinds(f), ["while"])
        self.assertIn("whilst", f[0])

    def test_whilst_and_meanwhile_pass(self) -> None:
        self.assertEqual(style.check_text("SPEC.md", "Do this whilst waiting, and meanwhile rest.\n"), [])

    def test_ize_spelling(self) -> None:
        f = style.check_text("SPEC.md", "We organize and prioritize; the organization agrees.\n")
        self.assertEqual(kinds(f), ["ize-spelling", "ize-spelling", "ize-spelling"])

    def test_ize_allowlist(self) -> None:
        self.assertEqual(style.check_text("SPEC.md", "The size of the prize; seize it; capsize; resize.\n"), [])

    def test_american_spelling(self) -> None:
        f = style.check_text("SPEC.md", "The behavior and color of the defense.\n")
        self.assertEqual(kinds(f), ["us-spelling", "us-spelling", "us-spelling"])

    def test_declared_us_spelling_line_is_exempt(self) -> None:
        self.assertEqual(style.check_text("SPEC.md", "US spelling: **Defense Before Fix**.\n"), [])

    def test_proper_nouns_in_links_and_code_are_exempt(self) -> None:
        self.assertEqual(style.check_text("SPEC.md", "See [Defense Before Fix](https://x/defense) and `color`.\n"), [])


class WhitespaceTest(unittest.TestCase):
    def test_trailing_whitespace_and_tabs(self) -> None:
        f = style.check_text("SPEC.md", "trailing \n\tindented\n")
        self.assertEqual(kinds(f), ["trailing-whitespace", "tab"])


class NumberingTest(unittest.TestCase):
    def test_sections_and_clauses_in_sequence_pass(self) -> None:
        text = "## 1. One\n### 1.1 A\n### 1.2 B\n## 2. Two\n### 2.1 C\n## Appendix A\n"
        self.assertEqual(style.check_text("SPEC.md", text), [])

    def test_skipped_section_number(self) -> None:
        f = style.check_text("SPEC.md", "## 1. One\n## 3. Three\n")
        self.assertEqual(kinds(f), ["section-sequence"])

    def test_clause_numbered_under_wrong_section(self) -> None:
        f = style.check_text("SPEC.md", "## 1. One\n### 2.1 Wrong\n")
        self.assertEqual(kinds(f), ["clause-sequence"])

    def test_skipped_clause_number(self) -> None:
        f = style.check_text("SPEC.md", "## 1. One\n### 1.1 A\n### 1.3 C\n")
        self.assertEqual(kinds(f), ["clause-sequence"])


if __name__ == "__main__":
    unittest.main()
