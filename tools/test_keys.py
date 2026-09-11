"""Tests for tools/keys.py: the acceptance answer keys quote the current document."""

from __future__ import annotations

import importlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
keys = importlib.import_module("keys")

DOC = """# Spec

## 3. The method

### 3.4 Sweep the codebase

The [Practitioner](#practitioner) MUST run the [Rule](#rule) across the entire codebase and
record the total [Instance] count before fixing anything.

[instance]: #instance
"""

KEY = """# Answer key

- **2a.** Quote: "The Practitioner MUST run the Rule across the entire
  codebase and record the total Instance count before fixing anything". See
  [3.4](../../SPEC.md#34-sweep-the-codebase).
"""


def kinds(findings: list[str]) -> list[str]:
    return sorted(keys.kind_of(f) for f in findings)


class QuoteTest(unittest.TestCase):
    def test_flatten_strips_links_emphasis_and_collapses_space(self) -> None:
        self.assertEqual(keys.flatten("**The [Rule](#rule)** and  [Instances]\ncount"), "The Rule and Instances count")

    def test_quotations_are_extracted_across_lines(self) -> None:
        q = keys.quotations(KEY)
        self.assertEqual(len(q), 1)
        self.assertTrue(q[0][1].startswith("The Practitioner MUST run"))

    def test_short_quotations_are_ignored(self) -> None:
        self.assertEqual(keys.quotations('A "short one" here.'), [])


class CheckTest(unittest.TestCase):
    def test_verbatim_quote_is_clean(self) -> None:
        self.assertEqual(keys.check_key("acceptance/method/KEY.md", KEY, {"SPEC.md": DOC}, "SPEC.md"), [])

    def test_stale_quote_is_a_finding(self) -> None:
        doc = DOC.replace("total [Instance] count", "total [Instance] count, corroborated,")
        f = keys.check_key("acceptance/method/KEY.md", KEY, {"SPEC.md": doc}, "SPEC.md")
        self.assertEqual(kinds(f), ["key-quote-stale"])
        self.assertIn("acceptance/method/KEY.md:3:", f[0])

    def test_dead_anchor_is_a_finding(self) -> None:
        key = KEY.replace("#34-sweep-the-codebase", "#34-sweep-everything")
        f = keys.check_key("acceptance/method/KEY.md", key, {"SPEC.md": DOC}, "SPEC.md")
        self.assertEqual(kinds(f), ["key-dead-anchor"])


class RepoTest(unittest.TestCase):
    def test_check_walks_the_acceptance_tree(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "SPEC.md").write_text(DOC)
            (root / "acceptance" / "method").mkdir(parents=True)
            (root / "acceptance" / "method" / "KEY.md").write_text(KEY.replace("before fixing anything", "before fixing nothing"))
            f = keys.check(root)
            self.assertEqual(kinds(f), ["key-quote-stale"])


if __name__ == "__main__":
    unittest.main()
