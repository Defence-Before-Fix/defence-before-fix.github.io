---
title: Rector and Defence Before Fix
summary: Custom rules with fixtures and only meet 4.1 and 4.2, skips are configuration only under 7.1; the class name printed as identifier fails 4.3.
---

# Rector

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Detector conformance**: 🔴 · **Checked**: 2026-09-08, version 2.6.6

Rector is an automated refactoring tool built on the PHP parser and PHPStan's type inference. Its job in a pipeline is to rewrite code, but in `--dry-run` mode it is a detector that reports every place a rule would change, and a custom rule can express any pattern the AST exposes, so it can host a bespoke defence whose fix is mechanical.

## How it is conformant

Clause 4.1 is met: a project extends `AbstractRector`, declares the node types and the refactoring, and registers the class with `withRules()` in `rector.php` ([custom rule](https://getrector.com/documentation/custom-rule)). Clause 4.2 is met twice over: `AbstractRectorTestCase` runs a rule over a `.php.inc` fixture with a before and after section ([custom rule](https://getrector.com/documentation/custom-rule)), and `--only="Fully\Qualified\Rule"` runs one registered rule from the command line ([run single rule](https://getrector.com/documentation/run-single-rule)). Clauses 5.1 to 5.4 hold: the tool runs locally, accepts a path, and prints the diff and rule name to the terminal. Clause 7.1 is met, and this is unusual: the inline `@noRector` annotation was removed in Rector 0.15 precisely because it hid context, and the only skip route is `withSkip()` in the configuration, which is visible ([pull request 3148](https://github.com/rectorphp/rector-src/pull/3148), [ignoring rules or paths](https://getrector.com/documentation/ignoring-rules-or-paths)).

## How it is not conformant

Clause 4.3 fails, and it decides the grade: the string printed with a finding is the rule's fully qualified class name, which the clause forbids as an identifier because a rename or a namespace move changes it, and there is no field for the author to choose one. Clauses 6.1 to 6.3 fail: nothing resolves a printed name for a bespoke rule, and for bundled rules the catalogue is keyed on class name and lives on the website. Clause 7.2 has no inline route to apply to, and `withSkip()` takes classes and paths with no field for a reason ([ignoring rules or paths](https://getrector.com/documentation/ignoring-rules-or-paths)). Clause 4.4 is not met and clause 6.4 was not verified.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                  |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Yes          | `AbstractRector` and `withRules()`, [custom rule](https://getrector.com/documentation/custom-rule)                        |
| Detector | 4.2    | Yes          | `AbstractRectorTestCase` fixtures and `--only`, [run single rule](https://getrector.com/documentation/run-single-rule)    |
| Detector | 4.3    | No           | Prints the rule class name, which the clause forbids                                                                      |
| Detector | 4.4    | No           | Nothing enforces an identifier                                                                                            |
| Detector | 5.1    | Yes          | `vendor/bin/rector --dry-run` runs locally                                                                                |
| Detector | 5.2    | Yes          | Path argument accepted                                                                                                    |
| Detector | 5.3    | Yes          | Diff and rule name print to the terminal                                                                                  |
| Detector | 5.4    | Yes          | No CI-only mode                                                                                                           |
| Detector | 6.1    | No           | No resolver keyed on a printed identifier                                                                                 |
| Detector | 6.2    | No           | Bundled rule catalogue is on the website                                                                                  |
| Detector | 6.3    | No           | Same                                                                                                                      |
| Detector | 6.4    | Not verified | Not found                                                                                                                 |
| Detector | 7.1    | Yes          | `@noRector` removed; skips are configuration only, [pull request 3148](https://github.com/rectorphp/rector-src/pull/3148) |
| Detector | 7.2    | No           | No inline route; `withSkip()` carries no reason field                                                                     |

## Notes for a practitioner

Rector suits a defence whose remedy is a transformation you can state exactly: write the rule, prove it with a fixture under `AbstractRectorTestCase`, sweep with `--dry-run`, and enforce with `--dry-run` failing the build. Treat the class name as the identifier and never move it, and put a comment beside every `withSkip()` entry because the configuration will not ask for one.
