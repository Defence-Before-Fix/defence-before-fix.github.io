---
title: PHPMD and Defence Before Fix
summary: Custom rules with stable names the text renderer does not print; fails 8.3 on SuppressWarnings and the baseline, 8.2 on reasons.
---

# PHPMD

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 2.15.0

PHPMD, the PHP Mess Detector, runs rules over the PDepend model of a codebase and reports complexity, naming and design problems. It sits beside the static analysers in a pipeline as a design-level detector, and a project can add rules of its own to it.

## How it is conformant

Clause 4.1 is met: a rule implements `\PHPMD\Rule` or extends `\PHPMD\AbstractRule`, opts into classes, methods or functions through marker interfaces, and is registered in a ruleset XML with a `name` and a `class` ([writing a PHPMD rule](https://phpmd.org/documentation/writing-a-phpmd-rule.html)). Clause 4.3 is met in part: the ruleset's `name` attribute is chosen by the author and is what `@SuppressWarnings(PHPMD.Name)` keys on, so it is stable and not derived from the class. Clause 4.2 is met by a workaround that needs no test suite: a ruleset XML containing the one rule, run against one file, since PHPMD takes a file list and a ruleset path ([documentation index](https://phpmd.org/documentation/index.html)). Clauses 5.1 and 5.2 hold for the same reason. With `--verbose` the text renderer prints a link to each rule's documentation, which gestures at clause 6.1.

## How it is not conformant

The readiness limit is that the rule name is not printed by default: the text renderer prints the configured message, and the rule name reaches output only through the XML renderer or the verbose link ([writing a PHPMD rule](https://phpmd.org/documentation/writing-a-phpmd-rule.html)). Clause 8.3 fails structurally: `@SuppressWarnings(PHPMD)` and its per-rule and wildcard forms are documented inline suppressions, and `--generate-baseline` writes a silent baseline ([suppress warnings](https://phpmd.org/documentation/suppress-warnings.html), [documentation index](https://phpmd.org/documentation/index.html)). Clause 8.2 fails because none of these takes a reason. Clause 6.1 fails for bespoke rules, and for bundled rules the verbose link points at the website, so clauses 6.2 and 6.3 fail. Clause 7.1 fails because nothing lists the rules a ruleset activates with what each forbids. There is no declaration under clause 11.1, and the last release predates the method.

## Clause by clause

| Clause | Result       | Evidence                                                                                                                   |
| ------ | ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | Custom rule class in a ruleset, [writing a PHPMD rule](https://phpmd.org/documentation/writing-a-phpmd-rule.html)          |
| 4.2    | Partial      | One-rule ruleset against one file; no purpose-built harness                                                                |
| 4.3    | Partial      | `name` is author-chosen but the text renderer prints the message, not the name                                             |
| 4.4    | No           | Nothing enforces a name                                                                                                    |
| 5.1    | Yes          | `phpmd` runs locally, [documentation index](https://phpmd.org/documentation/index.html)                                    |
| 5.2    | Yes          | Comma-separated file list accepted, [documentation index](https://phpmd.org/documentation/index.html)                      |
| 5.3    | Yes          | Renderer output to the terminal                                                                                            |
| 5.4    | Yes          | No CI-only mode                                                                                                            |
| 6.1    | Partial      | Verbose link per bundled rule; nothing for bespoke, [documentation index](https://phpmd.org/documentation/index.html)      |
| 6.2    | No           | Links point at phpmd.org                                                                                                   |
| 6.3    | No           | Same                                                                                                                       |
| 7.1    | No           | No listing command                                                                                                         |
| 7.2    | No           | Follows from 7.1                                                                                                           |
| 7.3    | No           | Follows from 7.1                                                                                                           |
| 8.1    | Partial      | Ruleset `exclude` and baseline are read by the tool                                                                        |
| 8.2    | No           | No reason on suppressions or baseline, [suppress warnings](https://phpmd.org/documentation/suppress-warnings.html)         |
| 8.3    | No           | `@SuppressWarnings` and `--generate-baseline`, [suppress warnings](https://phpmd.org/documentation/suppress-warnings.html) |
| 8.4    | No           | Not enumerable                                                                                                             |
| 8.5    | Partial      | Rule thresholds carry documented defaults                                                                                  |
| 9.1    | No           | No agent summary                                                                                                           |
| 9.2    | No           | No delivery mechanism                                                                                                      |
| 10.1   | Not verified | Not found                                                                                                                  |
| 10.2   | Not verified | Not checked                                                                                                                |
| 11.1   | No           | No declaration                                                                                                             |

## Notes for a practitioner

Give every bespoke rule a `name` you will keep, put that name at the start of its message so the text renderer carries it, and prove the rule with a one-rule ruleset against a fixture file. Forbid `@SuppressWarnings` through PHPStan or a sniff, since PHPMD cannot forbid it itself, and do not adopt the baseline.
