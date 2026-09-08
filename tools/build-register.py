#!/usr/bin/env python3
"""Build the register table in tools/index.md from the per-tool pages.

Each tools/<slug>.md carries a `summary:` line in its front matter and an
opening line of the form
  **Language**: X · **Kind**: tool|toolchain · **Readiness**: G · **Detector conformance**: G
  [· **Toolchain conformance**: G · **Project conformance**: G, toolchains only] · **Checked**: date, version v
The table is grouped by language, toolchains first within a group, and is
written between the REGISTER markers in index.md. Run it after any page
changes; CI fails when the committed table is stale.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
INDEX = HERE / "index.md"
START = "<!-- REGISTER:START -->"
END = "<!-- REGISTER:END -->"
FIELD = re.compile(r"\*\*([\w ]+?)\*\*: ([^·]+?)(?: · |$)")
LANGUAGE_ORDER = [
    "PHP",
    "JavaScript and TypeScript",
    "Python",
    "Go",
    "Rust",
    "Multi-language",
]


def parse(page: Path) -> dict[str, str]:
    text = page.read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if m is None:
        raise SystemExit(f"{page.name}: no front matter")
    front = dict(
        line.split(":", 1) for line in m.group(1).splitlines() if ":" in line
    )
    front = {k.strip(): v.strip() for k, v in front.items()}
    if "summary" not in front:
        raise SystemExit(f"{page.name}: no summary in front matter")
    body = text[m.end():]
    title = re.search(r"^# (.+)$", body, re.M)
    header = re.search(r"^\*\*Language\*\*: .+$", body, re.M)
    if title is None or header is None:
        raise SystemExit(f"{page.name}: missing title or header line")
    fields = {k: v.strip() for k, v in FIELD.findall(header.group(0))}
    if "Detector conformance" not in fields and "Conformance" in fields:
        # Graded against toolchain specification 0.1.0, before the split; shown until regraded.
        fields["Detector conformance"] = fields.pop("Conformance") + " (0.1.0)"
    for key in ("Language", "Kind", "Readiness", "Detector conformance", "Checked"):
        if key not in fields:
            raise SystemExit(f"{page.name}: header lacks {key}")
    if fields["Kind"] == "toolchain":
        for key in ("Toolchain conformance", "Project conformance"):
            fields.setdefault(key, "not yet graded")
    else:
        for key in ("Toolchain conformance", "Project conformance"):
            fields[key] = "·"
    return {
        "slug": page.stem,
        "name": title.group(1),
        "summary": front["summary"],
        **fields,
    }


def build(rows: list[dict[str, str]]) -> str:
    out: list[str] = []
    languages = sorted(
        {r["Language"] for r in rows},
        key=lambda l: (LANGUAGE_ORDER.index(l) if l in LANGUAGE_ORDER else 99, l),
    )
    for language in languages:
        group = [r for r in rows if r["Language"] == language]
        group.sort(key=lambda r: (r["Kind"] != "toolchain", r["name"].lower()))
        out.append(f"### {language}")
        out.append("")
        out.append("| Tool | Kind | Readiness | Detector | Toolchain | Project | Notes | Checked |")
        out.append("| ---- | ---- | --------- | -------- | --------- | ------- | ----- | ------- |")
        for r in group:
            out.append(
                f"| [{r['name']}]({r['slug']}.md) | {r['Kind']} | {r['Readiness']} "
                f"| {r['Detector conformance']} | {r['Toolchain conformance']} "
                f"| {r['Project conformance']} | {r['summary']} | {r['Checked']} |"
            )
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    check = "--check" in sys.argv
    pages = sorted(p for p in HERE.glob("*.md") if p.name != "index.md")
    table = build([parse(p) for p in pages])
    text = INDEX.read_text()
    if START not in text or END not in text:
        raise SystemExit("index.md lacks the REGISTER markers")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = f"{head}{START}\n{table}{END}{tail}"
    if new == text:
        print(f"register: current ({len(pages)} tools)")
        return 0
    if check:
        print("register: stale; run tools/build-register.py")
        return 1
    INDEX.write_text(new)
    print(f"register: rebuilt ({len(pages)} tools)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
