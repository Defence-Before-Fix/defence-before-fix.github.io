#!/usr/bin/env python3
"""What a change to a specification document must bring with it.

Compared against a base revision, usually the branch a pull request targets. A changed
specification needs a changelog entry in the same change. A change to the set of
normative sentences, the ones carrying an RFC 2119 keyword inside a numbered section or
appendix, is a new or removed obligation and needs the version bumped or marked as a
pre-release, since the published version is the accepted one.

Findings:
  change-unlogged             a specification changed and CHANGELOG.md did not
  change-unversioned          an obligation was added or removed on a published version
  change-obligation-reworded  an obligation's sentence changed; the acceptance key may quote it

    changes.py --base origin/main    compare the working tree with that revision
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ["SPEC.md", "DETECTOR-SPEC.md", "TOOLING-SPEC.md"]
TRACKED = DOCS + ["CHANGELOG.md"]
KEYWORD = re.compile(r"\b(MUST NOT|MUST|SHOULD NOT|SHOULD|MAY)\b")
NUMBERED = re.compile(r"^## (\d+\.|Appendix)")
SECTION = re.compile(r"^## ")
LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)|\[([^\]]+)\](?:\[[^\]]*\])?")
SENTENCE = re.compile(r"(?<=[.!?])\s+(?=[A-Z\[*])")
HEADER = re.compile(r"^\*\*Version\*\*: (\S+?),", re.M)
FINDING_KIND = re.compile(r": ([a-z-]+)( |—|$)")


def kind_of(finding: str) -> str:
    m = FINDING_KIND.search(finding)
    return m.group(1) if m else "other"


def flatten(text: str) -> str:
    text = LINK.sub(lambda m: m.group(1) or m.group(2), text)
    return re.sub(r"\s+", " ", text).strip()


def normative_sentences(text: str) -> list[str]:
    out: list[str] = []
    in_numbered = False
    in_code = False
    paragraph: list[str] = []

    def flush() -> None:
        if paragraph:
            for s in SENTENCE.split(flatten(" ".join(paragraph))):
                if KEYWORD.search(s):
                    out.append(s.strip())
            paragraph.clear()

    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if SECTION.match(line):
            flush()
            in_numbered = bool(NUMBERED.match(line))
            continue
        if not in_numbered or line.startswith("#"):
            flush()
            continue
        if line.strip() == "":
            flush()
        else:
            paragraph.append(line)
    flush()
    return out


def version_of(text: str) -> str | None:
    m = HEADER.search(text)
    return m.group(1) if m else None


def check_set(base: dict[str, str], head: dict[str, str]) -> list[str]:
    """base and head map a file name to its content; a missing key is a missing file."""
    out: list[str] = []
    changed = [d for d in DOCS if base.get(d) != head.get(d)]
    if changed and base.get("CHANGELOG.md") == head.get("CHANGELOG.md"):
        out.append(f"CHANGELOG.md: change-unlogged — {', '.join(changed)} changed without a changelog entry")
    for d in changed:
        before = normative_sentences(base.get(d, ""))
        after = normative_sentences(head.get(d, ""))
        added = [s for s in after if s not in before]
        removed = [s for s in before if s not in after]
        if not added and not removed:
            continue
        version = version_of(head.get(d, ""))
        base_version = version_of(base.get(d, ""))
        bumped = version != base_version or (version is not None and "-" in version)
        if len(added) == len(removed):
            for s in added:
                out.append(f"{d}: change-obligation-reworded — '{s[:90]}'; check the acceptance key still quotes it")
            continue
        if not bumped:
            for s in added:
                out.append(f"{d}: change-unversioned — added on published {version}: '{s[:90]}'")
            for s in removed:
                out.append(f"{d}: change-unversioned — removed on published {version}: '{s[:90]}'")
    return out


def at_revision(rev: str, root: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for name in TRACKED:
        r = subprocess.run(["git", "show", f"{rev}:{name}"], cwd=root, capture_output=True, text=True)
        if r.returncode == 0:
            out[name] = r.stdout
    return out


def working_tree(root: Path) -> dict[str, str]:
    return {name: (root / name).read_text() for name in TRACKED if (root / name).exists()}


def check(root: Path, base: str) -> list[str]:
    return check_set(at_revision(base, root), working_tree(root))


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[0] != "--base":
        print("usage: changes.py --base <revision>", file=sys.stderr)
        return 2
    findings = check(ROOT, argv[1])
    for f in findings:
        print("  " + f)
    print(f"changes: {'clean' if not findings else str(len(findings)) + ' finding(s)'} against {argv[1]}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
