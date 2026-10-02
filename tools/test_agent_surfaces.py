"""Tests for the deploy-time output of build-agent-surfaces.py --site."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"

_spec = importlib.util.spec_from_file_location("build_agent_surfaces", ROOT / "build-agent-surfaces.py")
surfaces = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(surfaces)


class SiteOutput(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.site = Path(self.tmp.name)
        surfaces.write_site(self.site, {})

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_every_primary_document_is_published_raw(self) -> None:
        for name in surfaces.RAW_DOCS:
            self.assertEqual((self.site / "raw" / name).read_text(), (ROOT / name).read_text(), name)

    def test_every_tools_register_page_is_published_raw(self) -> None:
        pages = sorted(TOOLS.glob("*.md"))
        self.assertTrue(pages, "no register pages found under tools/")
        for page in pages:
            published = self.site / "raw" / "tools" / page.name
            self.assertTrue(published.is_file(), f"/raw/tools/{page.name} missing from the built site")
            self.assertEqual(published.read_text(), page.read_text(), page.name)

    def test_register_json_is_published_raw(self) -> None:
        published = self.site / "raw" / "tools" / "register.json"
        self.assertTrue(published.is_file(), "/raw/tools/register.json missing from the built site")
        self.assertEqual(published.read_text(), (TOOLS / "register.json").read_text())


if __name__ == "__main__":
    unittest.main()
