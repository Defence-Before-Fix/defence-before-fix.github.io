---
title: PHPMD and Defence Before Fix
summary: Custom rules and one-rule rulesets meet 4.1 and 4.2; the name is absent from default output under 4.3, documentation online only fails 6.2 and 6.3.
---

# PHPMD

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Detector conformance**: 🟡 · **Checked**: 2026-09-08, version 2.15.0

PHPMD, the PHP Mess Detector, runs rules over the PDepend model of a codebase and reports complexity, naming and design problems. It sits beside the static analysers in a pipeline as a design-level detector, and a project can add rules of its own to it.

## How it is conformant

Clause 4.1 is met: a rule implements `\PHPMD\Rule` or extends `\PHPMD\AbstractRule`, opts into classes, methods or functions through marker interfaces, and is registered in a ruleset XML with a `name` and a `class` ([writing a PHPMD rule](https://phpmd.org/documentation/writing-a-phpmd-rule.html)). Clause 4.2 is met without a test suite: a ruleset XML containing the one rule, run against one file, is a harness in the specification's sense, since PHPMD takes a file list and a ruleset path ([documentation index](https://phpmd.org/documentation/index.html)). Clauses 5.1 to 5.4 hold for the same reason. Clause 4.3 is met in its first half: the ruleset's `name` attribute is chosen by the author and is what `@SuppressWarnings(PHPMD.Name)` keys on, so it is stable and not derived from the class. Clause 6.1 is met in part, since with `--verbose` the text renderer prints a link to each bundled rule's documentation, which is the URL form the clause accepts. Clause 7.1 is met for the baseline, which is only used when the project generates it and keeps it in place ([documentation index](https://phpmd.org/documentation/index.html)).

## How it is not conformant

Clause 4.3's second half fails, and it is the readiness limit: the rule name is not printed by default, because the text renderer prints the configured message, and the name reaches output only through the XML renderer or the verbose link ([writing a PHPMD rule](https://phpmd.org/documentation/writing-a-phpmd-rule.html)). Clauses 6.2 and 6.3 fail because the verbose link points at the website and nothing on disk resolves a name. Clause 7.1 is only partly met: `@SuppressWarnings(PHPMD)` and its per-rule and wildcard forms are documented inline suppressions with no switch to disable them and no documented check that finds them ([suppress warnings](https://phpmd.org/documentation/suppress-warnings.html)). Clause 7.2 fails because neither the annotation nor a baseline entry takes a reason. Clause 4.4 is not met and clause 6.4 was not verified; the last release predates the specification.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                               |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Detector | 4.1    | Yes          | Custom rule class in a ruleset, [writing a PHPMD rule](https://phpmd.org/documentation/writing-a-phpmd-rule.html)                                      |
| Detector | 4.2    | Yes          | One-rule ruleset against one file, [documentation index](https://phpmd.org/documentation/index.html)                                                   |
| Detector | 4.3    | Partial      | `name` is author-chosen but the text renderer prints the message, not the name                                                                         |
| Detector | 4.4    | No           | Nothing enforces a name                                                                                                                                |
| Detector | 5.1    | Yes          | `phpmd` runs locally, [documentation index](https://phpmd.org/documentation/index.html)                                                                |
| Detector | 5.2    | Yes          | Comma-separated file list accepted, [documentation index](https://phpmd.org/documentation/index.html)                                                  |
| Detector | 5.3    | Yes          | Renderer output to the terminal                                                                                                                        |
| Detector | 5.4    | Yes          | No CI-only mode                                                                                                                                        |
| Detector | 6.1    | Partial      | Verbose link per bundled rule only with `--verbose`; nothing for bespoke, [documentation index](https://phpmd.org/documentation/index.html)            |
| Detector | 6.2    | No           | Links point at phpmd.org                                                                                                                               |
| Detector | 6.3    | No           | Same                                                                                                                                                   |
| Detector | 6.4    | Not verified | Not found                                                                                                                                              |
| Detector | 7.1    | Partial      | Baseline is opt-in; `@SuppressWarnings` has no switch or documented check, [suppress warnings](https://phpmd.org/documentation/suppress-warnings.html) |
| Detector | 7.2    | No           | No reason on suppressions or baseline, [suppress warnings](https://phpmd.org/documentation/suppress-warnings.html)                                     |

## Notes for a practitioner

Give every bespoke rule a `name` you will keep, put that name at the start of its message so the text renderer carries it, and prove the rule with a one-rule ruleset against a fixture file. Forbid `@SuppressWarnings` through PHPStan or a sniff, since PHPMD cannot forbid it itself, and do not adopt the baseline.
