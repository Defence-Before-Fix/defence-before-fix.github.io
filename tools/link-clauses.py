#!/usr/bin/env python3
"""Link every clause and section reference on the pages spec-qa.py's clause rule covers.

    tools/link-clauses.py            rewrite the pages in place
    tools/link-clauses.py --diff     print what would change, change nothing

The resolution is tools/clauses.py's; where a page's prose leaves the document ambiguous
the page default applies, and the rewritten page is for a reader to check, since a link
to the wrong document is well-formed markdown in the wrong sense.
"""

from __future__ import annotations

import difflib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import clauses


def main() -> int:
    diff = "--diff" in sys.argv
    changed = 0
    for page in clauses.pages():
        before = (clauses.ROOT / page).read_text()
        after = clauses.link_page(page)
        if after == before:
            continue
        changed += 1
        if diff:
            sys.stdout.writelines(difflib.unified_diff(before.splitlines(True), after.splitlines(True), str(page), str(page)))
        else:
            (clauses.ROOT / page).write_text(after)
            print(f"linked: {page}")
    print(f"{changed} page(s) {'would change' if diff else 'changed'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
