# Defence Before Fix (DBF)

> **Defence Before Fix (DBF)** is a phase that runs *before* a defect is fixed. Rather than dropping
> straight into remediating the specific instance in front of you, you first treat that instance
> as evidence of a class, and you build the automated defence that detects every occurrence of
> that class across the whole codebase. The defence is only trusted once it has been seen to fire.

Six clauses, in order:

1. **Attribute the defect to a class.** Not "what went wrong here" but "what kind of thing is
   this an instance of", within a lower bound and an upper bound that are both checkable.
2. **Build the net.** A rule that reads code, in whatever detector the toolchain offers, bespoke
   where nothing off the shelf will take it.
3. **Prove the net by making the rule fire.** Red before green, on the originating instance,
   committed before the fix.
4. **Sweep the codebase, then fix every instance.** The count is the finding; the fix addresses
   the hazard, not the rule.
5. **Enforce permanently, and block.** Through the project's own entry point for accepting
   changes, failing rather than warning.
6. **Make the failure message terse, and point it at real documentation.** Versioned with the
   rule, resolvable from the identifier as printed.

## The documents

| Document                             | What it is                                                                                                          | Version |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------- | ------- |
| [SPEC.md](SPEC.md)                   | The method. Normative. What a practitioner does when a defect is found.                                             | 1.0.1   |
| [DETECTOR-SPEC.md](DETECTOR-SPEC.md) | The detector. What a tool that reads code must offer so that a rule can be written, proven, run and resolved in it. | 1.0.0   |
| [TOOLING-SPEC.md](TOOLING-SPEC.md)   | The toolchain. What a project's assembled tooling must offer beyond its detectors, measured at the project level.   | 0.2.0   |
| [PRIMER.md](PRIMER.md)               | The short introduction.                                                                                             |         |
| [PROVENANCE.md](PROVENANCE.md)       | Who coined the term, when, and what is and is not claimed.                                                          |         |
| [CHANGELOG.md](CHANGELOG.md)         | Changes to each document, versioned independently.                                                                  |         |

The method specification is the source of truth for what the method is. Where anything else
describing Defence Before Fix disagrees with it, including the article in which the term was first
published, the specification is correct.

## Tools that implement it

- [php-qa-ci](https://github.com/LongTermSupport/php-qa-ci), the PHP toolchain
- [ts-qa-ci](https://github.com/LongTermSupport/ts-qa-ci), the TypeScript toolchain

Each records the toolchain specification version it conforms to.

## Checking the documents

`spec-qa.py` is the repository's own defence: every defined term is a heading in the terminology
section, every use in the body is a capitalised link to it, and a bare occurrence of a defined
word is a finding. It runs in CI on every push.

```
python3 spec-qa.py
```

A change to any of the three specifications must also pass the acceptance test in
[ACCEPTANCE.md](ACCEPTANCE.md): a cold cohort of at least five low-strength model readers
answers a fixed question set for each changed document, marked against the keys under
[acceptance/](acceptance/), and the run's record under `acceptance/runs/` is what lets the
change merge. A version whose changelog entry records no cohort is not published.

## Contributing

Pull requests target `next` and follow [CONTRIBUTING.md](CONTRIBUTING.md). A proposed
obligation must pass the five tests in [SCOPE.md](SCOPE.md) before its wording is discussed;
proposals that fail are listed in [DECLINED.md](DECLINED.md). Releases are cut from `next` as
described in [PUBLISHING.md](PUBLISHING.md).

## Agent-facing surfaces

The site is meant to be read by agents as well as people, and every agent surface is generated so
that it cannot drift from the documents:

| Surface                                 | What it is                                                                                                                                    | Generated from                            |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| `/defence-before-fix-project-prompt.md` | Raw markdown: the method as an agent follows it, plus where the raw documents are, what a conforming toolchain offers, how a project declares | `SPEC.md` Appendix A and `_data/site.yml` |
| `/llms.txt`                             | The llms.txt index of everything on the site                                                                                                  | `_data/site.yml`                          |
| `/llms-full.txt`                        | The prompt and every document in one file                                                                                                     | the documents                             |
| `/raw/<name>.md`                        | Every primary document as raw markdown                                                                                                        | the documents                             |
| `<link rel="alternate">` on each page   | Points a fetcher at the raw markdown and at llms.txt                                                                                          | `_data/site.yml`                          |

`build-agent-surfaces.py` writes the prompt and `llms.txt` into the repository, and CI fails when
they are stale (`--check`). The Pages workflow runs the same script with `--site ./_site` after
the Jekyll build to copy the raw documents and write `llms-full.txt` into the deployed site. To
change any of it, edit `SPEC.md` or `_data/site.yml` and run the script.

Both toolchains print the canonical URL in their failure output, so an agent that meets the
method in a failing pipeline can fetch the prompt from the line it has just read.

## Attribution

Coined by [Joseph Edmonds](https://ltscommerce.dev) of
[Edmonds Commerce](https://edmondscommerce.co.uk). First published 22 February 2026 in
[Defence Before Fix: Preventing Bug Classes with Static Analysis](https://ltscommerce.dev/articles/defence-before-fix-static-analysis).
US spelling: Defense Before Fix.

The documents are licensed under
[Creative Commons Attribution 4.0 International](LICENSE). `spec-qa.py` is under the same
licence.
