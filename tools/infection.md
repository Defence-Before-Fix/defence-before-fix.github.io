---
title: Infection and Defence Before Fix
summary: A mutation tester, not a detector; custom mutators run alone; fails 4.3 on class names, 8.3 on infection-ignore-all, 8.2 on reasons.
---

# Infection

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 0.35.4

Infection is a mutation testing framework: it alters the code under test and reports mutants the test suite fails to kill. It is not a detector in the method's sense, because it judges the strength of tests rather than a pattern in code, and the method rules out a test as the net. It is graded here on whether a custom mutator can host a bespoke defence at all.

## How it is conformant

Clause 4.1 is met in the narrow sense that a project can write a class implementing `Infection\Mutator\Mutator` and enable it by class name in `infection.json5` ([custom mutators](https://infection.github.io/guide/custom-mutators.html)). Clause 4.2 is met by `--mutators="App\Mutator\Name" --show-mutations`, which the guide recommends for quick feedback on a new mutator, and a positional file path narrows the run to one source file ([command line options](https://infection.github.io/guide/command-line-options.html)). Clauses 5.1 and 5.3 hold: the run is local and the report is printed. Clause 8.1 is met in part by the `ignore` and `ignoreSourceCodeByRegex` blocks of the configuration, which Infection reads ([usage](https://infection.github.io/guide/usage.html)).

## How it is not conformant

A mutator is not a defence: it says nothing about whether a pattern is present, only whether a test would notice its absence, so clause 3.2 of the method cannot be satisfied through it. Within the toolchain clauses, 4.3 fails because the printed identifier is the mutator class name. Clause 8.3 fails structurally: `@infection-ignore-all` is a documented inline annotation at class, method and statement level ([usage](https://infection.github.io/guide/usage.html)), and clause 8.2 fails because neither it nor the `ignore` configuration takes a reason. Clause 6.1 is met only for bundled mutators, whose catalogue is a web page, so clauses 6.2 and 6.3 fail. Clause 7.1 fails because no command lists the mutators a configuration enables. Running Infection at all requires a test suite, so it cannot stand alone under clause 4.2's condition. There is no declaration under clause 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                                                                       |
| ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Partial      | Custom mutators, but a mutator is not a detector, [custom mutators](https://infection.github.io/guide/custom-mutators.html)                    |
| 4.2    | Partial      | `--mutators` and a path, but the project's tests must run, [command line options](https://infection.github.io/guide/command-line-options.html) |
| 4.3    | No           | Class name printed                                                                                                                             |
| 4.4    | No           | Nothing to enforce                                                                                                                             |
| 5.1    | Yes          | Runs locally                                                                                                                                   |
| 5.2    | Yes          | Positional file path, [command line options](https://infection.github.io/guide/command-line-options.html)                                      |
| 5.3    | Yes          | Report to the terminal, log files on request                                                                                                   |
| 5.4    | Yes          | No CI-only mode                                                                                                                                |
| 6.1    | Partial      | Bundled mutators documented online by name                                                                                                     |
| 6.2    | No           | Website only                                                                                                                                   |
| 6.3    | No           | Same                                                                                                                                           |
| 7.1    | No           | No listing of enabled mutators                                                                                                                 |
| 7.2    | No           | Follows from 7.1                                                                                                                               |
| 7.3    | No           | Follows from 7.1                                                                                                                               |
| 8.1    | Partial      | `ignore` configuration is read by the tool, [usage](https://infection.github.io/guide/usage.html)                                              |
| 8.2    | No           | No reason field                                                                                                                                |
| 8.3    | No           | `@infection-ignore-all`, [usage](https://infection.github.io/guide/usage.html)                                                                 |
| 8.4    | No           | Not enumerable                                                                                                                                 |
| 8.5    | Partial      | `--min-msi` thresholds are documented defaults                                                                                                 |
| 9.1    | No           | No agent summary                                                                                                                               |
| 9.2    | No           | No delivery mechanism                                                                                                                          |
| 10.1   | Not verified | Not found                                                                                                                                      |
| 10.2   | Not verified | Not checked                                                                                                                                    |
| 11.1   | No           | No declaration                                                                                                                                 |

## Notes for a practitioner

Keep Infection for what it is: proof that the reproduction test under clause 2 of the method actually constrains the fix. Build the defence itself in PHPStan or another detector, and if you use Infection's ignore configuration, forbid `@infection-ignore-all` with a rule elsewhere and write the reason beside each entry.
