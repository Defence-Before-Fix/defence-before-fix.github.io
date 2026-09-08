---
title: PHPArkitect and Defence Before Fix
summary: Custom expressions and runOnlyThis meet 4.1 and 4.2; no identifier beyond the because text fails 4.3, directory-only class sets fail 5.2.
---

# PHPArkitect

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Detector conformance**: 🔴 · **Checked**: 2026-09-08, version 1.3.0

PHPArkitect enforces architectural constraints: a rule selects a set of classes with `that()`, states what they should satisfy with `should()`, and carries a reason in `because()`. It runs as its own step in a pipeline and is the natural home for a defence about dependencies, naming or placement rather than about a line of code.

## How it is conformant

Clause 4.1 is met: a project's rules are written in `phparkitect.php`, and where the built-in expressions do not cover a check, a class implementing the `Expression` interface plugs into `that()` or `should()` like any built-in ([README](https://github.com/phparkitect/arkitect), [custom rules](https://github.com/phparkitect/arkitect/blob/master/docs/custom-rules.md)). Clause 4.2 is met by `runOnlyThis()`, which the README describes as running only that rule during `check`, and the `--config` option lets a fixture configuration point at a fixture class set. Clauses 5.1, 5.3 and 5.4 hold: `phparkitect check` runs locally with no CI-only mode and prints every violation with the class name, the broken rule and the `because()` text, in text, JSON and GitLab formats. Clause 7.1 is met: there is no inline suppression, and the baseline is used only when `--use-baseline` names it, so a project forbids the route by never passing it ([README](https://github.com/phparkitect/arkitect)).

## How it is not conformant

Clause 4.3 fails, and it decides the grade: a rule has no identifier field, and what is printed is the rule's description and its `because()` prose. Edit the wording and every reference to it breaks, which is the failure the clause names. Clause 5.2 fails: a class set is a directory, and no option restricts a run to one file. Clauses 6.1 and 6.2 fail because there is no identifier to resolve, and clause 6.3 is only partly met since the built-in expression descriptions ship in the package without any rule-level page. Clause 7.2 fails because a baseline entry carries no reason and nothing asks for one. Clause 4.4 has nothing to enforce, and clause 6.4 was not verified.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                              |
| -------- | ------ | ------------ | --------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Yes          | Custom `Expression` classes, [custom rules](https://github.com/phparkitect/arkitect/blob/master/docs/custom-rules.md) |
| Detector | 4.2    | Yes          | `runOnlyThis()` and `--config`, [README](https://github.com/phparkitect/arkitect)                                     |
| Detector | 4.3    | No           | No identifier; output carries the `because()` text only                                                               |
| Detector | 4.4    | No           | Nothing to enforce                                                                                                    |
| Detector | 5.1    | Yes          | `phparkitect check` runs locally                                                                                      |
| Detector | 5.2    | No           | Class sets are directories; no single-file run documented                                                             |
| Detector | 5.3    | Yes          | Text, JSON and GitLab formats to the terminal, [README](https://github.com/phparkitect/arkitect)                      |
| Detector | 5.4    | Yes          | No CI-only mode                                                                                                       |
| Detector | 6.1    | No           | Nothing to key a lookup on                                                                                            |
| Detector | 6.2    | No           | Same                                                                                                                  |
| Detector | 6.3    | Partial      | Built-in expression descriptions ship in the package; no rule-level documentation                                     |
| Detector | 6.4    | Not verified | Not found                                                                                                             |
| Detector | 7.1    | Yes          | No inline route; baseline only with `--use-baseline`, [README](https://github.com/phparkitect/arkitect)               |
| Detector | 7.2    | No           | Baseline entries carry no reason                                                                                      |

## Notes for a practitioner

Begin every `because()` string with an identifier of your own, such as `ARCH-007`, and keep an index keyed on it in the repository; that is the only way a printed violation resolves. Prove a rule with `runOnlyThis()` against a fixture class set, and refuse the baseline, since it is the one suppression route and it records nothing.
