---
title: Pyright and Defence Before Fix
summary: Type checker with no plug-in mechanism so 4.1 fails; some diagnostics carry no rule for 4.3; website-only docs fail 6.2
---

# Pyright

**Language**: Python · **Kind**: tool · **Readiness**: 🔴 · **Detector conformance**: 🔴 · **Checked**: 2026-09-08, version 1.1.411

Pyright is Microsoft's static type checker for Python and the engine behind Pylance. It is a type checker rather than a rule engine, and its findings are grouped under named diagnostic rules such as `reportOptionalMemberAccess` that can each be set to error, warning, information or off. In a pipeline it plays the same role as mypy, usually chosen for speed and for its editor integration.

## How it is conformant

Pyright runs locally on named files, and "if specific files are specified on the command line, it overrides the files or directories specified in the pyrightconfig.json" ([command line](https://github.com/microsoft/pyright/blob/main/docs/command-line.md)), which meets 5.1 and 5.2. The rule name is printed with each diagnostic that has one, in text and in `--outputjson` (5.3, 5.4). The diagnostic rule names are stable, documented identifiers ([configuration](https://github.com/microsoft/pyright/blob/main/docs/configuration.md)), so 4.3 holds for the bundled rules that carry one. Because 4.1 fails, 4.2 is graded on the bundled rules: a configuration with every rule off and one rule on, run against a fixture file, isolates that rule, although Pyright offers no flag to do it in one invocation (4.2, partial). The `enableTypeIgnoreComments` setting switches off `# type: ignore` ([configuration](https://github.com/microsoft/pyright/blob/main/docs/configuration.md)), which is the disableable half of clause 7.1.

## How it is not conformant

Clause 4.1 is failed by design. The [mypy comparison](https://github.com/microsoft/pyright/blob/main/docs/mypy-comparison.md) states that "Mypy supports a plug-in mechanism, whereas pyright does not", and gives the maintainers' reasons for declining to add one, so a consuming project cannot host any bespoke defence, and 4.4 does not apply. The command line documentation notes that "not all diagnostics have an associated diagnostic rule", so some findings print no identifier at all, which fails 4.3 for those. Rule documentation is on the website only, keyed on the rule name, with no resolver from the installed package (6.1 partial, 6.2, 6.3). Clause 7.1 is partial: `# type: ignore` can be disabled, but `# pyright: ignore` and `# pyright: ignore[rule]` cannot ([comments](https://github.com/microsoft/pyright/blob/main/docs/comments.md)), and `reportUnnecessaryTypeIgnoreComment` reports only a comment that no longer suppresses anything, so a project cannot see the ones that do. No reason is asked for (7.2).

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                                                        |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | No           | [No plug-in mechanism](https://github.com/microsoft/pyright/blob/main/docs/mypy-comparison.md)                                                                                  |
| Detector | 4.2    | Partial      | Bundled rules: isolate one rule by configuration; no single-rule flag                                                                                                           |
| Detector | 4.3    | Partial      | Named rules stable; some diagnostics carry no rule                                                                                                                              |
| Detector | 4.4    | No           | None                                                                                                                                                                            |
| Detector | 5.1    | Yes          | `pyright [files...]` locally ([command line](https://github.com/microsoft/pyright/blob/main/docs/command-line.md))                                                              |
| Detector | 5.2    | Yes          | Single file accepted                                                                                                                                                            |
| Detector | 5.3    | Yes          | Rule name in text and JSON output                                                                                                                                               |
| Detector | 5.4    | Yes          | All rules runnable locally                                                                                                                                                      |
| Detector | 6.1    | Partial      | Website configuration page keyed on rule name                                                                                                                                   |
| Detector | 6.2    | No           | No offline resolution                                                                                                                                                           |
| Detector | 6.3    | No           | Documentation on the website only                                                                                                                                               |
| Detector | 6.4    | Not verified | No release gate documented                                                                                                                                                      |
| Detector | 7.1    | Partial      | `enableTypeIgnoreComments` disables one route; `# pyright: ignore` cannot be disabled or detected ([comments](https://github.com/microsoft/pyright/blob/main/docs/comments.md)) |
| Detector | 7.2    | No           | No reason required                                                                                                                                                              |

## Notes for a practitioner

Pyright can carry an off-the-shelf defence where the class is a type hazard one of its named rules already detects, and raising that rule to `error` in `pyrightconfig.json` is a recorded, proven change. It cannot host anything bespoke, so keep a second detector such as Pylint for the project's own classes, set `enableTypeIgnoreComments` to false and `reportUnnecessaryTypeIgnoreComment` to error, and have the second detector flag `# pyright: ignore` since Pyright will not.
