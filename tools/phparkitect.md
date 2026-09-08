---
title: PHPArkitect and Defence Before Fix
summary: Custom expressions and runOnlyThis, but no identifier beyond the because text; fails 4.3, 5.2 on single files, 8.3 and 8.2 on the baseline.
---

# PHPArkitect

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 1.3.0

PHPArkitect enforces architectural constraints: a rule selects a set of classes with `that()`, states what they should satisfy with `should()`, and carries a reason in `because()`. It runs as its own step in a pipeline and is the natural home for a defence about dependencies, naming or placement rather than about a line of code.

## How it is conformant

Clause 4.1 is met: a project's rules are written in `phparkitect.php`, and where the built-in expressions do not cover a check, a class implementing the `Expression` interface plugs into `that()` or `should()` like any built-in ([README](https://github.com/phparkitect/arkitect), [custom rules](https://github.com/phparkitect/arkitect/blob/master/docs/custom-rules.md)). Clause 4.2 is met by `runOnlyThis()`, which the README describes as running only that rule during `check`, and the `--config` option lets a fixture configuration point at a fixture class set. Clauses 5.1 and 5.3 hold: `phparkitect check` runs locally and prints every violation with the class name, the broken rule and the `because()` text. The remediation text therefore has a place to live, which is what clause 3 of the toolchain specification asks the tool to provide.

## How it is not conformant

Clause 4.3 fails: a rule has no identifier field, and what is printed is the rule's description and its `because()` prose. Edit the wording and every reference to it breaks, which is the failure the clause names. Clause 8.3 fails structurally: `generate-baseline` and `--use-baseline` silence existing violations without a word of justification, and `prune-baseline` maintains that file ([README](https://github.com/phparkitect/arkitect)). Clause 8.2 fails with it. Clause 5.2 fails: a class set is a directory, and no option restricts a run to one file. Clause 6.1 fails because there is no identifier to resolve, and clause 7.1 fails because no command lists the configured rules without running them. There is no declaration under clause 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                                              |
| ------ | ------------ | --------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | Custom `Expression` classes, [custom rules](https://github.com/phparkitect/arkitect/blob/master/docs/custom-rules.md) |
| 4.2    | Yes          | `runOnlyThis()` and `--config`, [README](https://github.com/phparkitect/arkitect)                                     |
| 4.3    | No           | No identifier; output carries the `because()` text only                                                               |
| 4.4    | No           | Nothing to enforce                                                                                                    |
| 5.1    | Yes          | `phparkitect check` runs locally                                                                                      |
| 5.2    | No           | Class sets are directories; no single-file run documented                                                             |
| 5.3    | Yes          | Text, JSON and GitLab formats to the terminal, [README](https://github.com/phparkitect/arkitect)                      |
| 5.4    | Yes          | No CI-only mode                                                                                                       |
| 6.1    | No           | Nothing to key a lookup on                                                                                            |
| 6.2    | No           | Same                                                                                                                  |
| 6.3    | Partial      | Built-in expression descriptions ship in the package; no rule-level documentation                                     |
| 7.1    | No           | No listing command                                                                                                    |
| 7.2    | No           | Follows from 7.1                                                                                                      |
| 7.3    | No           | Follows from 7.1                                                                                                      |
| 8.1    | Partial      | Baseline file is read by the tool                                                                                     |
| 8.2    | No           | Baseline entries carry no reason                                                                                      |
| 8.3    | No           | `generate-baseline` and `--use-baseline`, [README](https://github.com/phparkitect/arkitect)                           |
| 8.4    | No           | Not enumerable with the rules                                                                                         |
| 8.5    | No           | Not documented                                                                                                        |
| 9.1    | No           | No agent summary                                                                                                      |
| 9.2    | No           | No delivery mechanism                                                                                                 |
| 10.1   | Not verified | Not found                                                                                                             |
| 10.2   | Not verified | Not checked                                                                                                           |
| 11.1   | No           | No declaration                                                                                                        |

## Notes for a practitioner

Begin every `because()` string with an identifier of your own, such as `ARCH-007`, and keep an index keyed on it in the repository; that is the only way a printed violation resolves. Prove a rule with `runOnlyThis()` against a fixture class set, and refuse the baseline, since it is the one suppression route and it records nothing.
