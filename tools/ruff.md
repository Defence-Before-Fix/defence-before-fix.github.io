---
title: Ruff and Defence Before Fix
summary: No third-party rules so 4.1 fails; ruff rule resolves offline for 6.1 and 6.2; fails 8.3 on noqa and add-noqa
---

# Ruff

**Language**: Python · **Kind**: tool · **Readiness**: 🔴 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 0.16.6

Ruff is a fast Python linter and formatter written in Rust that reimplements the rule sets of Flake8, its popular plugins, isort, pyupgrade and others as a single binary with over 900 rules. In a pipeline it is the first and cheapest check, run on every edit, and it is often the only linter a Python project has. It is a fixed-catalogue detector: the project selects from what Ruff ships and cannot add to it.

## How it is conformant

Ruff meets the reporting clauses cleanly. It runs locally with no infrastructure (5.1) and over a single file or directory (5.2), and every finding is printed in the command's own output with a stable rule code such as `F401` (5.3, 5.4), as described in [the linter documentation](https://docs.astral.sh/ruff/linter/). The rule codes are governed by a published [versioning policy](https://docs.astral.sh/ruff/versioning/) under which promotion, deprecation and behaviour changes are minor-version events, so a code is a stable identifier across releases for the bundled rules (4.3, for bundled rules only). The `ruff rule <code>` subcommand, listed in [the configuration documentation](https://docs.astral.sh/ruff/configuration/) as "Explain a rule (or all rules)", resolves a printed code to its documentation from the installed binary without network access (6.1, 6.2), and that documentation ships inside the same binary as the rule (6.3). Ruff's own rule documentation is part of its build, which is as close as a fixed-catalogue tool comes to clause 10.1, although no self-audit is documented as such.

## How it is not conformant

Clause 4.1 is failed outright. [The FAQ](https://docs.astral.sh/ruff/faq/) states that "Ruff does not yet support third-party plugins, though a plugin system is within-scope for the project", so a consuming project cannot express a pattern of its own, and clauses 4.2 and 4.4 have nothing to apply to. Clause 8.3 is failed: `# noqa` and `# noqa: CODE` comments suppress inline, and `--add-noqa` writes them across a whole codebase, with no justification required and no bundled defence against them ([linter documentation](https://docs.astral.sh/ruff/linter/)). There is no project record in the sense of section 8: `lint.ignore` in the configuration file records exceptions but requires no reason (8.1, 8.2), and nothing enumerates exceptions alongside rules (8.4). Clause 7.1 is met only partially, since the resolved settings can be printed with `--show-settings` but that is a configuration dump rather than a listing of identifiers with what each forbids. Ruff declares no method specification version (11.1).

## Clause by clause

| Clause | Result       | Evidence                                                                              |
| ------ | ------------ | ------------------------------------------------------------------------------------- |
| 4.1    | No           | [FAQ](https://docs.astral.sh/ruff/faq/): no third-party plugins                       |
| 4.2    | No           | No bespoke rules, so no harness applies                                               |
| 4.3    | Partial      | Bundled codes stable per [versioning policy](https://docs.astral.sh/ruff/versioning/) |
| 4.4    | No           | Not applicable without bespoke rules                                                  |
| 5.1    | Yes          | `ruff check` runs locally ([linter docs](https://docs.astral.sh/ruff/linter/))        |
| 5.2    | Yes          | `ruff check path/to/file.py` ([linter docs](https://docs.astral.sh/ruff/linter/))     |
| 5.3    | Yes          | Findings and codes printed to stdout, exit code 1 on violations                       |
| 5.4    | Yes          | Every rule is runnable locally                                                        |
| 6.1    | Yes          | `ruff rule <code>` ([configuration docs](https://docs.astral.sh/ruff/configuration/)) |
| 6.2    | Yes          | Explanation ships in the binary                                                       |
| 6.3    | Yes          | Rule and documentation versioned together                                             |
| 7.1    | Partial      | `--show-settings` dumps configuration, not identifiers with a terse statement         |
| 7.2    | Partial      | Derived from configuration, but see 7.1                                               |
| 7.3    | No           | No project rules exist to list                                                        |
| 8.1    | No           | No project record the tool reads with justifications                                  |
| 8.2    | No           | `lint.ignore` and `noqa` require no reason                                            |
| 8.3    | No           | `# noqa` and `--add-noqa` ([linter docs](https://docs.astral.sh/ruff/linter/))        |
| 8.4    | No           | No enumeration of exceptions                                                          |
| 8.5    | Yes          | Default rule set documented ([rules page](https://docs.astral.sh/ruff/rules/))        |
| 9.1    | No           | No agent summary                                                                      |
| 9.2    | No           | No delivery mechanism                                                                 |
| 10.1   | Not verified | Rule docs are built from source; no release-blocking audit is documented              |
| 10.2   | Not verified | Ruff lints its own Python, but no release gate is documented                          |
| 11.1   | No           | No declaration                                                                        |

## Notes for a practitioner

Ruff cannot host a bespoke defence, so use it for the industry's known hazards and pair it with a second detector that accepts project rules, such as Pylint or a Flake8 plugin, for the class that the method turns up. Forbid `# noqa` in the configuration of that second detector or in review policy, and keep exceptions in `pyproject.toml` with a comment stating the hazard and scope, since Ruff will not require one.
