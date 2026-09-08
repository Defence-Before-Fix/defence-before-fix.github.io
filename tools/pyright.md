---
title: Pyright and Defence Before Fix
summary: Type checker with no plug-in mechanism so 4.1 fails; some diagnostics carry no rule; fails 8.3 on pyright ignore comments
---

# Pyright

**Language**: Python · **Kind**: tool · **Readiness**: 🔴 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 1.1.411

Pyright is Microsoft's static type checker for Python and the engine behind Pylance. It is a type checker rather than a rule engine, and its findings are grouped under named diagnostic rules such as `reportOptionalMemberAccess` that can each be set to error, warning, information or off. In a pipeline it plays the same role as mypy, usually chosen for speed and for its editor integration.

## How it is conformant

Pyright runs locally on named files, and "if specific files are specified on the command line, it overrides the files or directories specified in the pyrightconfig.json" ([command line](https://github.com/microsoft/pyright/blob/main/docs/command-line.md)), which meets 5.1 and 5.2. The rule name is printed with each diagnostic that has one, in text and in `--outputjson` (5.3, 5.4). The diagnostic rule names are stable, documented identifiers ([configuration](https://github.com/microsoft/pyright/blob/main/docs/configuration.md)), so 4.3 holds for the bundled rules. Defaults for every rule are documented per strictness mode, which meets 8.5.

## How it is not conformant

Clause 4.1 is failed by design. The [mypy comparison](https://github.com/microsoft/pyright/blob/main/docs/mypy-comparison.md) states that "Mypy supports a plug-in mechanism, whereas pyright does not", and gives the maintainers' reasons for declining to add one, so a consuming project cannot host any bespoke defence, and 4.2 and 4.4 do not apply. Clause 8.3 is failed: `# pyright: ignore` and `# pyright: ignore[rule]` suppress inline with no justification, and `# type: ignore` is honoured by default ([comments](https://github.com/microsoft/pyright/blob/main/docs/comments.md)). The command line documentation also notes that "not all diagnostics have an associated diagnostic rule", so some findings print no identifier at all, which fails 4.3 for those. Rule documentation is on the website only, with no offline resolver (6.1, 6.2, 6.3). Nothing lists active rules with their meaning (7.1) and nothing declares a version (11.1).

## Clause by clause

| Clause | Result       | Evidence                                                                                                           |
| ------ | ------------ | ------------------------------------------------------------------------------------------------------------------ |
| 4.1    | No           | [No plug-in mechanism](https://github.com/microsoft/pyright/blob/main/docs/mypy-comparison.md)                     |
| 4.2    | No           | Not applicable                                                                                                     |
| 4.3    | Partial      | Named rules stable; some diagnostics carry no rule                                                                 |
| 4.4    | No           | None                                                                                                               |
| 5.1    | Yes          | `pyright [files...]` locally ([command line](https://github.com/microsoft/pyright/blob/main/docs/command-line.md)) |
| 5.2    | Yes          | Single file accepted                                                                                               |
| 5.3    | Yes          | Rule name in text and JSON output                                                                                  |
| 5.4    | Yes          | All rules runnable locally                                                                                         |
| 6.1    | Partial      | Website configuration page keyed on rule name                                                                      |
| 6.2    | No           | No offline resolution                                                                                              |
| 6.3    | No           | Documentation on the website only                                                                                  |
| 7.1    | No           | No listing with descriptions                                                                                       |
| 7.2    | No           | See 7.1                                                                                                            |
| 7.3    | No           | No project rules                                                                                                   |
| 8.1    | Partial      | Config file read, but no justification field                                                                       |
| 8.2    | No           | No reason required                                                                                                 |
| 8.3    | No           | `# pyright: ignore` ([comments](https://github.com/microsoft/pyright/blob/main/docs/comments.md))                  |
| 8.4    | No           | None                                                                                                               |
| 8.5    | Yes          | Per-mode defaults documented                                                                                       |
| 9.1    | No           | None                                                                                                               |
| 9.2    | No           | None                                                                                                               |
| 10.1   | Not verified | No release gate documented                                                                                         |
| 10.2   | Not verified | Not documented                                                                                                     |
| 11.1   | No           | No declaration                                                                                                     |

## Notes for a practitioner

Pyright can carry an off-the-shelf defence where the class is a type hazard one of its named rules already detects, and raising that rule to `error` in `pyrightconfig.json` is a recorded, proven change. It cannot host anything bespoke, so keep a second detector such as Pylint for the project's own classes, and set `reportUnnecessaryTypeIgnoreComment` so stale suppressions at least surface.
