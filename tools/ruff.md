---
title: Ruff and Defence Before Fix
summary: No third-party rules so 4.1 fails; select and rule meet 4.2 and 6.1 to 6.3 for bundled rules; specific noqa fails 7.1
---

# Ruff

**Language**: Python · **Kind**: tool · **Readiness**: 🔴 · **Detector conformance**: 🔴 · **Checked**: 2026-09-08, version 0.16.6

Ruff is a fast Python linter and formatter written in Rust that reimplements the rule sets of Flake8, its popular plugins, isort, pyupgrade and others as a single binary with over 900 rules. In a pipeline it is the first and cheapest check, run on every edit, and it is often the only linter a Python project has. It is a fixed-catalogue detector: the project selects from what Ruff ships and cannot add to it.

## How it is conformant

Ruff meets section 5 cleanly. It runs locally with no infrastructure (5.1) and over a single file or directory (5.2), and every finding is printed in the command's own output with a stable rule code such as `F401` (5.3, 5.4), as described in [the linter documentation](https://docs.astral.sh/ruff/linter/). Because Ruff fails 4.1, clause 4.2 is graded on its bundled rules, and `ruff check --select F401 fixture.py` runs one bundled rule against supplied code with every other rule silent, which is a usable harness (4.2). The rule codes are governed by a published [versioning policy](https://docs.astral.sh/ruff/versioning/) under which promotion, deprecation and behaviour changes are minor-version events, so a code is a stable identifier across releases for the bundled rules and it is printed with every finding (4.3, for bundled rules). The `ruff rule <code>` subcommand, listed in [the configuration documentation](https://docs.astral.sh/ruff/configuration/) as "Explain a rule (or all rules)", resolves a printed code to its documentation from the installed binary without network access (6.1, 6.2), and that documentation ships inside the same binary as the rule, so the two are versioned together (6.3). The `RUF100` rule reports a `noqa` comment that no longer suppresses anything, and `PGH004` reports a blanket `# noqa` that names no code, which is a documented mechanical check over part of the inline route (7.1, partial).

## How it is not conformant

Clause 4.1 is failed outright. [The FAQ](https://docs.astral.sh/ruff/faq/) states that "Ruff does not yet support third-party plugins, though a plugin system is within-scope for the project", so a consuming project cannot express a pattern of its own, and clause 4.4 has nothing to apply to. Clause 7.1 is not fully met: `# noqa: CODE` comments suppress inline and `--add-noqa` writes them across a whole codebase ([linter documentation](https://docs.astral.sh/ruff/linter/)), no setting or flag makes Ruff ignore them, and whilst `PGH004` catches the blanket form, a `noqa` naming a specific code is neither disableable nor detectable by anything Ruff documents. No reason is asked for on any `noqa` (7.2). Ruff's rule documentation is generated in its build, but no release gate that checks every code resolves is documented (6.4, not verified).

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                           |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------ |
| Detector | 4.1    | No           | [FAQ](https://docs.astral.sh/ruff/faq/): no third-party plugins                                                    |
| Detector | 4.2    | Yes          | Bundled rules: `ruff check --select <code> <file>` ([linter docs](https://docs.astral.sh/ruff/linter/))            |
| Detector | 4.3    | Yes          | Bundled codes stable per [versioning policy](https://docs.astral.sh/ruff/versioning/), printed with every finding  |
| Detector | 4.4    | No           | Not applicable without bespoke rules                                                                               |
| Detector | 5.1    | Yes          | `ruff check` runs locally ([linter docs](https://docs.astral.sh/ruff/linter/))                                     |
| Detector | 5.2    | Yes          | `ruff check path/to/file.py` ([linter docs](https://docs.astral.sh/ruff/linter/))                                  |
| Detector | 5.3    | Yes          | Findings and codes printed to stdout, exit code 1 on violations                                                    |
| Detector | 5.4    | Yes          | Every rule is runnable locally                                                                                     |
| Detector | 6.1    | Yes          | `ruff rule <code>` ([configuration docs](https://docs.astral.sh/ruff/configuration/))                              |
| Detector | 6.2    | Yes          | Explanation ships in the binary                                                                                    |
| Detector | 6.3    | Yes          | Rule and documentation versioned together; every code has a page under [rules](https://docs.astral.sh/ruff/rules/) |
| Detector | 6.4    | Not verified | Rule docs are built from source; no release-blocking check is documented                                           |
| Detector | 7.1    | Partial      | `# noqa` cannot be disabled; [PGH004](https://docs.astral.sh/ruff/rules/blanket-noqa/) detects blanket form only   |
| Detector | 7.2    | No           | No reason on `noqa`; `--add-noqa` writes them in bulk                                                              |

## Notes for a practitioner

Ruff cannot host a bespoke defence, so use it for the industry's known hazards and pair it with a second detector that accepts project rules, such as Pylint or a Flake8 plugin, for the class that the method turns up. Enable `PGH004` and `RUF100`, and forbid the specific `# noqa: CODE` form in the configuration of that second detector or in review policy, since Ruff can neither switch it off nor see it.
