#!/usr/bin/env python3
"""Build the register from the per-tool pages: the table in tools/index.md and register.json.

Each tools/<slug>.md carries its grades in front matter:
  summary:    one line of notes, clause numbers as plain text
  language:   PHP | JavaScript and TypeScript | Python | Go | Rust | Multi-language
  kind:       tool | toolchain
  readiness, detector: a grade, one of the three marks
  toolchain, project:  a grade, toolchains only
  checked:    date, version or commit
The page renders them through _includes/tool-grades.html. The table is grouped by
language, toolchains first within a group, with every clause number in the notes
linked to its heading, and is written between the REGISTER markers in index.md.
register.json carries the same rows for the register application, notes as text
and link segments so the application never renders HTML it did not write. Run it
after any page changes; CI fails when either output is stale.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import clauses

HERE = Path(__file__).parent
INDEX = HERE / "index.md"
JSON_OUT = HERE / "register.json"
START = "<!-- REGISTER:START -->"
END = "<!-- REGISTER:END -->"
LANGUAGE_ORDER = [
    "PHP",
    "JavaScript and TypeScript",
    "Python",
    "Go",
    "Rust",
    "Multi-language",
]
GRADES = {"🟢": "green", "🟡": "amber", "🔴": "red"}


def parse(page: Path) -> dict[str, str]:
    text = page.read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if m is None:
        raise SystemExit(f"{page.name}: no front matter")
    front = {k.strip(): v.strip() for k, v in (line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)}
    for key in ("summary", "language", "kind", "readiness", "detector", "checked"):
        if key not in front:
            raise SystemExit(f"{page.name}: front matter lacks {key}")
    title = re.search(r"^# (.+)$", text[m.end():], re.M)
    if title is None:
        raise SystemExit(f"{page.name}: missing title")
    if front["kind"] == "toolchain":
        for key in ("toolchain", "project"):
            front.setdefault(key, "not yet graded")
    else:
        for key in ("toolchain", "project"):
            front[key] = "·"
    return {"slug": page.stem, "name": title.group(1), **front}


def ordered(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    languages = sorted(
        {r["language"] for r in rows},
        key=lambda l: (LANGUAGE_ORDER.index(l) if l in LANGUAGE_ORDER else 99, l),
    )
    out: list[dict[str, str]] = []
    for language in languages:
        group = [r for r in rows if r["language"] == language]
        group.sort(key=lambda r: (r["kind"] != "toolchain", r["name"].lower()))
        out.extend(group)
    return out


def table(rows: list[dict[str, str]]) -> str:
    out: list[str] = []
    language = None
    for r in rows:
        if r["language"] != language:
            language = r["language"]
            if out:
                out.append("")
            out.append(f"### {language}")
            out.append("")
            out.append("| Tool | Kind | Readiness | Detector | Toolchain | Project | Notes | Checked |")
            out.append("| ---- | ---- | --------- | -------- | --------- | ------- | ----- | ------- |")
        default = "toolchain" if r["kind"] == "toolchain" else "detector"
        notes = clauses.linkify(r["summary"], default, "../")
        out.append(
            f"| [{r['name']}]({r['slug']}.md) | {r['kind']} | {r['readiness']} "
            f"| {r['detector']} | {r['toolchain']} "
            f"| {r['project']} | {notes} | {r['checked']} |"
        )
    return "\n".join(out).rstrip() + "\n"


def register(rows: list[dict[str, str]]) -> str:
    def grade(value: str) -> dict[str, str]:
        return {"mark": value, "level": GRADES.get(value, "none" if value == "·" else "ungraded")}

    items = []
    for r in rows:
        default = "toolchain" if r["kind"] == "toolchain" else "detector"
        items.append(
            {
                "slug": r["slug"],
                "name": r["name"],
                "page": f"/tools/{r['slug']}.html",
                "language": r["language"],
                "kind": r["kind"],
                "readiness": grade(r["readiness"]),
                "detector": grade(r["detector"]),
                "toolchain": grade(r["toolchain"]),
                "project": grade(r["project"]),
                "notes": clauses.segments(r["summary"], default, "/"),
                "checked": r["checked"],
            }
        )
    return json.dumps({"languages": LANGUAGE_ORDER, "tools": items}, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    check = "--check" in sys.argv
    pages = sorted(p for p in HERE.glob("*.md") if p.name != "index.md")
    rows = ordered([parse(p) for p in pages])
    text = INDEX.read_text()
    if START not in text or END not in text:
        raise SystemExit("index.md lacks the REGISTER markers")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    outputs = {
        INDEX: f"{head}{START}\n{table(rows)}{END}{tail}",
        JSON_OUT: register(rows),
    }
    stale = [p.name for p, new in outputs.items() if not p.exists() or p.read_text() != new]
    if not stale:
        print(f"register: current ({len(pages)} tools)")
        return 0
    if check:
        print(f"register: stale ({', '.join(stale)}); run tools/build-register.py")
        return 1
    for p, new in outputs.items():
        p.write_text(new)
    print(f"register: rebuilt ({len(pages)} tools)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
