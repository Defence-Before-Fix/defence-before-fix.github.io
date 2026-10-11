"""The scripts that write into the repository refuse an argument they do not know, rather than
taking it for a request to rewrite their outputs."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WRITERS = ["tools/link-clauses.py", "tools/build-register.py", "build-agent-surfaces.py"]


class UnknownArgumentTest(unittest.TestCase):
    def test_an_unknown_argument_is_refused(self) -> None:
        for script in WRITERS:
            with self.subTest(script=script):
                r = subprocess.run([sys.executable, script, "--no-such-flag"], cwd=ROOT, capture_output=True, text=True)
                self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
                self.assertIn("--no-such-flag", r.stderr)

    def test_help_prints_usage(self) -> None:
        for script in WRITERS:
            with self.subTest(script=script):
                r = subprocess.run([sys.executable, script, "--help"], cwd=ROOT, capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertIn("usage:", r.stdout)


if __name__ == "__main__":
    unittest.main()
