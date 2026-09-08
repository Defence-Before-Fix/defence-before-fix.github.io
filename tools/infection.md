---
title: Infection and Defence Before Fix
summary: A mutation tester, not a detector; custom mutators only partly meet 4.1, the class name printed fails 4.3, infection-ignore-all fails 7.1.
---

# Infection

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Detector conformance**: 🔴 · **Checked**: 2026-09-08, version 0.35.4

Infection is a mutation testing framework: it alters the code under test and reports mutants the test suite fails to kill. It is not a detector in the method's sense, because it judges the strength of tests rather than a pattern in code, and the method rules out a test as the net. It is graded here on whether a custom mutator can host a bespoke defence at all.

## How it is conformant

Clause 4.1 is met in the narrow sense that a project can write a class implementing `Infection\Mutator\Mutator` and enable it by class name in `infection.json5` ([custom mutators](https://infection.github.io/guide/custom-mutators.html)). Clause 4.2 is met in part by `--mutators="App\Mutator\Name" --show-mutations`, which the guide recommends for quick feedback on a new mutator, and a positional file path narrows the run to one source file ([command line options](https://infection.github.io/guide/command-line-options.html)). Clauses 5.1 to 5.4 hold: the run is local, takes a file path, prints the report to the terminal with log files on request, and has no CI-only mode. Clause 6.1 is met for bundled mutators, whose catalogue on the website is keyed on the printed name.

## How it is not conformant

A mutator is not a defence: it says nothing about whether a pattern is present, only whether a test would notice its absence, so clause 3.2 of the method cannot be satisfied through it and clause 4.1 is at best partly met. Clause 4.3 fails, and it decides the grade: the printed identifier is the mutator class name, which the clause forbids. Clause 4.2 is only partly met because running Infection at all requires the project's test suite, which the harness definition excludes. Clauses 6.2 and 6.3 fail because the mutator catalogue is a web page. Clause 7.1 fails: `@infection-ignore-all` is a documented inline annotation at class, method and statement level with no switch to disable it and no documented check that finds it ([usage](https://infection.github.io/guide/usage.html)). Clause 7.2 fails because neither the annotation nor the `ignore` configuration takes a reason. Clause 4.4 has nothing to enforce, and clause 6.4 was not verified.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                       |
| -------- | ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Partial      | Custom mutators, but a mutator is not a detector, [custom mutators](https://infection.github.io/guide/custom-mutators.html)                    |
| Detector | 4.2    | Partial      | `--mutators` and a path, but the project's tests must run, [command line options](https://infection.github.io/guide/command-line-options.html) |
| Detector | 4.3    | No           | Class name printed                                                                                                                             |
| Detector | 4.4    | No           | Nothing to enforce                                                                                                                             |
| Detector | 5.1    | Yes          | Runs locally                                                                                                                                   |
| Detector | 5.2    | Yes          | Positional file path, [command line options](https://infection.github.io/guide/command-line-options.html)                                      |
| Detector | 5.3    | Yes          | Report to the terminal, log files on request                                                                                                   |
| Detector | 5.4    | Yes          | No CI-only mode                                                                                                                                |
| Detector | 6.1    | Yes          | Bundled mutators documented online keyed on the printed name                                                                                   |
| Detector | 6.2    | No           | Website only                                                                                                                                   |
| Detector | 6.3    | No           | Same                                                                                                                                           |
| Detector | 6.4    | Not verified | Not found                                                                                                                                      |
| Detector | 7.1    | No           | `@infection-ignore-all` has no switch and no documented check, [usage](https://infection.github.io/guide/usage.html)                           |
| Detector | 7.2    | No           | No reason field on the annotation or the `ignore` configuration                                                                                |

## Notes for a practitioner

Keep Infection for what it is: proof that the reproduction test under clause 2 of the method actually constrains the fix. Build the defence itself in PHPStan or another detector, and if you use Infection's ignore configuration, forbid `@infection-ignore-all` with a rule elsewhere and write the reason beside each entry.
