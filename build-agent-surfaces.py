#!/usr/bin/env python3
"""Build the agent-facing surfaces of the site from the documents and _data/site.yml.

Committed outputs, checked in CI with --check:
  defence-before-fix-project-prompt.md   the prompt an agent is asked to read, generated from
                                         SPEC.md Appendix A with the term links stripped, plus
                                         where the raw documents are and how to declare
  llms.txt                               the llms.txt index: what exists, in raw markdown, for
                                         a model that has landed on the site

Deploy-time outputs, written into the built site with --site DIR by the pages workflow:
  DIR/raw/<name>.md                      every primary document as raw markdown
  DIR/defence-before-fix-project-prompt.md
  DIR/llms.txt
  DIR/llms-full.txt                      the prompt and every raw document in one file

Edit SPEC.md or _data/site.yml, never the outputs.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).parent
PROMPT = HERE / "defence-before-fix-project-prompt.md"
LLMS = HERE / "llms.txt"
RAW_DOCS = ["SPEC.md", "TOOLING-SPEC.md", "PRIMER.md", "PROVENANCE.md", "CHANGELOG.md"]
TERM_LINK = re.compile(r"\[([^\]]+)\]\((?:[A-Z-]+\.md)?#[a-z0-9-]+\)")


def load_data() -> dict:
    import yaml

    return yaml.safe_load((HERE / "_data" / "site.yml").read_text())


def appendix_a(spec: str) -> str:
    m = re.search(r"^## Appendix A: Instructing an agent\n(.*?)^## ", spec, re.S | re.M)
    if m is None:
        raise SystemExit("SPEC.md: Appendix A not found")
    quote = [l[2:] if l.startswith("> ") else l[1:] for l in m.group(1).splitlines() if l.startswith(">")]
    return TERM_LINK.sub(r"\1", "\n".join(quote)).strip() + "\n"


def prompt(data: dict, spec: str) -> str:
    c = data["canonical_url"].rstrip("/")
    v = data["versions"]
    return f"""# Defence Before Fix: project prompt for agents

You are working in a project that follows Defence Before Fix, method specification {v["method"]}.
This file is generated from that specification and is the short form; the specification governs
where they differ. Read it once at the start of a task that involves fixing a defect.

## The method, when you find a defect

{appendix_a(spec)}
## Where the full documents are, as raw markdown

- Method specification {v["method"]}: {c}/raw/SPEC.md
- Toolchain specification {v["toolchain"]}: {c}/raw/TOOLING-SPEC.md
- Primer: {c}/raw/PRIMER.md
- Provenance: {c}/raw/PROVENANCE.md
- Changelog: {c}/raw/CHANGELOG.md
- Index of everything: {c}/llms.txt (and {c}/llms-full.txt for all of it in one file)

The rendered site is {c}/. The US spelling, Defense Before Fix, is the same method.

## What to expect from the toolchain

A toolchain that conforms to the toolchain specification gives you: a way to write a bespoke rule
in the project; a harness that runs one rule against one file; a stable identifier printed with
every finding; a command that resolves a printed identifier to its documentation without network
access; a listing of every defence active in the project, derived from the live configuration,
with the project's recorded exceptions in the same listing; and a manifest entry declaring the
specification version it conforms to. Use those commands rather than guessing. The two reference
toolchains and their commands are listed at {c}/tools/. If the project's toolchain lacks one of
these, say so in your report; that gap belongs to the toolchain's owner under clause 3.2 of the
method specification.

## How the project declares it

The project's manifest names the method specification version it follows and, for a toolchain, the
toolchain specification version, in the form its ecosystem uses for dependencies (for example
`extra.defence-before-fix` in composer.json or `defenceBeforeFix` in package.json), together with a
known-gap record that must be empty for conformance to be claimed. Do not add or change that
declaration yourself; report what you found.

## Citation

Edmonds, Joseph. *Defence Before Fix*, version {v["method"]}. First published {data["coined"]}.
{c}/
"""


def llms(data: dict) -> str:
    c = data["canonical_url"].rstrip("/")
    lines = [
        f"# {data['name']}",
        "",
        f"> {data['definition']}",
        "",
        f"A method by {data['author']['name']} of {data['organisation']['name']}, first published "
        f"{data['coined']}. Method specification {data['versions']['method']} and toolchain "
        f"specification {data['versions']['toolchain']}, published {data['versions']['published']}, "
        f"under {data['licence']['name']}. The method specification is the source of truth; where "
        "anything else disagrees with it, the specification is correct.",
        "",
        "## Start here if you are an agent",
        "",
        f"- [Project prompt]({c}/defence-before-fix-project-prompt.md): the method in the form to "
        "follow when you find a defect, generated from the specification's Appendix A.",
        "",
        "## Documents, raw markdown",
        "",
    ]
    for p in data["pages"]:
        if p.get("raw"):
            lines.append(f"- [{p['heading']}]({c}/raw/{p['raw']}): {p['blurb']}")
    lines += [
        "",
        "## Rendered pages",
        "",
    ]
    for p in data["pages"]:
        lines.append(f"- [{p['heading']}]({c}{p['path']}): {p['blurb']}")
    lines += [
        "",
        "## Optional",
        "",
        f"- [Everything in one file]({c}/llms-full.txt)",
        f"- [Source repository]({data['repository_url']})",
        f"- [Original article]({data['article_url']}): where the term was first published, on "
        f"{data['coined']}.",
        "",
    ]
    return "\n".join(lines)


def write_site(site: Path, data: dict) -> None:
    raw = site / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    for name in RAW_DOCS:
        shutil.copy(HERE / name, raw / name)
    shutil.copy(PROMPT, site / PROMPT.name)
    shutil.copy(LLMS, site / LLMS.name)
    parts = [PROMPT.read_text()] + [(HERE / n).read_text() for n in RAW_DOCS]
    (site / "llms-full.txt").write_text("\n\n---\n\n".join(parts))
    print(f"site: raw documents, prompt, llms.txt and llms-full.txt written under {site}")


def main() -> int:
    data = load_data()
    spec = (HERE / "SPEC.md").read_text()
    outputs = {PROMPT: prompt(data, spec), LLMS: llms(data)}
    if "--check" in sys.argv:
        stale = [p.name for p, text in outputs.items() if not p.exists() or p.read_text() != text]
        if stale:
            print(f"agent surfaces stale: {', '.join(stale)}; run build-agent-surfaces.py")
            return 1
        print("agent surfaces: current")
    else:
        for p, text in outputs.items():
            p.write_text(text)
        print("agent surfaces: rebuilt")
    if "--site" in sys.argv:
        write_site(Path(sys.argv[sys.argv.index("--site") + 1]), data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
