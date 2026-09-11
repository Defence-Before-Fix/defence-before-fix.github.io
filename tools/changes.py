#!/usr/bin/env python3
"""What a change to a specification document must bring with it.

Compared against a base revision, usually the branch a pull request targets. A changed
specification needs a changelog entry in the same change. A change to the set of
normative sentences, the ones carrying an RFC 2119 keyword inside a numbered section or
appendix, is a new or removed obligation and needs the version bumped or marked as a
pre-release, since the published version is the accepted one.

A reworded obligation is one whose sentence still shares most of its words with a
sentence that was there before; it needs no bump, and keys.py catches the stale
quotation if the key still carries the old words.

A changed specification also needs the acceptance run that accepted it, as a new file under
acceptance/runs/ in the same change, per ACCEPTANCE.md. That check needs the list of files the
change adds, so it runs only when one is given.

Findings:
  change-unlogged      a specification changed and CHANGELOG.md did not
  change-unversioned   an obligation was added or removed on a published version
  change-unaccepted    a specification changed and no acceptance run record was added

    changes.py --base origin/main    compare the working tree with that revision
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import clauses

ROOT = Path(__file__).resolve().parent.parent
DOCS = ["SPEC.md", "DETECTOR-SPEC.md", "TOOLING-SPEC.md"]
TRACKED = DOCS + ["CHANGELOG.md"]
RUNS = "acceptance/runs"
KEYWORD = re.compile(r"\b(MUST NOT|MUST|SHOULD NOT|SHOULD|MAY)\b")
NUMBERED = re.compile(r"^## (\d+\.|Appendix)")
SECTION = re.compile(r"^## ")
SENTENCE = re.compile(r"(?<=[.!?])\s+(?=[A-Z\[*0-9`])")
HEADER = re.compile(r"^\*\*Version\*\*: (\S+?),", re.M)
FINDING_KIND = re.compile(r": ([a-z-]+)( |—|$)")
REWORD_OVERLAP = 0.6


def kind_of(finding: str) -> str:
    m = FINDING_KIND.search(finding)
    return m.group(1) if m else "other"


def flatten(text: str) -> str:
    return clauses.flatten(text)


def overlap(a: str, b: str) -> float:
    """Jaccard similarity of the two sentences' word sets."""
    wa, wb = set(re.findall(r"\w+", a.lower())), set(re.findall(r"\w+", b.lower()))
    return len(wa & wb) / len(wa | wb) if wa | wb else 1.0


def keywords(sentence: str) -> list[str]:
    return KEYWORD.findall(sentence)


def pair_rewords(added: list[str], removed: list[str]) -> tuple[list[str], list[str]]:
    """Strip from both lists every added sentence that is a rewording of a removed one: the
    same RFC 2119 keywords, and most of the same words. A keyword flip is never a reword."""
    left_removed = list(removed)
    left_added = []
    for s in added:
        candidates = [r for r in left_removed if keywords(r) == keywords(s)]
        best = max(candidates, key=lambda r: overlap(s, r), default=None)
        if best is not None and overlap(s, best) >= REWORD_OVERLAP:
            left_removed.remove(best)
        else:
            left_added.append(s)
    return left_added, left_removed


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


def check_set(base: dict[str, str], head: dict[str, str], added_files: list[str] | None = None) -> list[str]:
    """base and head map a file name to its content; a missing key is a missing file.
    added_files lists the paths the change adds, when known."""
    out: list[str] = []
    changed = [d for d in DOCS if base.get(d) != head.get(d)]
    if changed and base.get("CHANGELOG.md") == head.get("CHANGELOG.md"):
        out.append(f"CHANGELOG.md: change-unlogged — {', '.join(changed)} changed without a changelog entry")
    if changed and added_files is not None and not any(p.startswith(RUNS + "/") for p in added_files):
        out.append(f"{RUNS}: change-unaccepted — {', '.join(changed)} changed without a new acceptance run record")
    for d in changed:
        before = normative_sentences(base.get(d, ""))
        after = normative_sentences(head.get(d, ""))
        added, removed = pair_rewords([s for s in after if s not in before], [s for s in before if s not in after])
        if not added and not removed:
            continue
        version = version_of(head.get(d, ""))
        base_version = version_of(base.get(d, ""))
        bumped = version != base_version or (version is not None and "-" in version)
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


def added_files(base: str, root: Path) -> list[str]:
    """Paths added since base, in the index and the working tree."""
    r = subprocess.run(["git", "diff", "--name-only", "--diff-filter=A", base], cwd=root, capture_output=True, text=True, check=True)
    tracked = r.stdout.split()
    u = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"], cwd=root, capture_output=True, text=True, check=True)
    return sorted(set(tracked + u.stdout.split()))


def check(root: Path, base: str) -> list[str]:
    return check_set(at_revision(base, root), working_tree(root), added_files(base, root))


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
