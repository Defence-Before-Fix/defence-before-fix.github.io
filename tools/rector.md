---
title: Rector and Defence Before Fix
summary: Custom rules with fixtures and --only; passes 8.3 since noRector was removed; fails 4.3 on class-name identifiers, 8.2, 6.1.
---

# Rector

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 2.6.6

Rector is an automated refactoring tool built on the PHP parser and PHPStan's type inference. Its job in a pipeline is to rewrite code, but in `--dry-run` mode it is a detector that reports every place a rule would change, and a custom rule can express any pattern the AST exposes, so it can host a bespoke defence whose fix is mechanical.

## How it is conformant

Clause 4.1 is met: a project extends `AbstractRector`, declares the node types and the refactoring, and registers the class with `withRules()` in `rector.php` ([custom rule](https://getrector.com/documentation/custom-rule)). Clause 4.2 is met twice over: `AbstractRectorTestCase` runs a rule over a `.php.inc` fixture with a before and after section ([custom rule](https://getrector.com/documentation/custom-rule)), and `--only="Fully\Qualified\Rule"` runs one registered rule from the command line ([run single rule](https://getrector.com/documentation/run-single-rule)). Clauses 5.1 and 5.2 hold: the tool runs locally and accepts a path. Clause 8.3 is met, and this is unusual: the inline `@noRector` annotation was removed in Rector 0.15 precisely because it hid context, and the only skip route is `withSkip()` in the configuration, which is visible ([pull request 3148](https://github.com/rectorphp/rector-src/pull/3148), [ignoring rules or paths](https://getrector.com/documentation/ignoring-rules-or-paths)). That configuration is also a record Rector reads itself, which meets clause 8.1.

## How it is not conformant

Clause 4.3 fails: the string printed with a finding is the rule's fully qualified class name, which the clause forbids as an identifier because a rename or a namespace move changes it. Clause 8.2 fails structurally: `withSkip()` takes classes and paths and has no field for a reason ([ignoring rules or paths](https://getrector.com/documentation/ignoring-rules-or-paths)). Clause 6.1 fails for a bespoke rule, and for bundled rules the catalogue is keyed on class name and lives on the website, so clauses 6.2 and 6.3 fail. Clause 7.1 fails because no command lists the rules a configuration activates with what each does; `--only` requires the rule to be registered but does not enumerate. There is no declaration under clause 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                                                               |
| ------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | `AbstractRector` and `withRules()`, [custom rule](https://getrector.com/documentation/custom-rule)                                     |
| 4.2    | Yes          | `AbstractRectorTestCase` fixtures and `--only`, [run single rule](https://getrector.com/documentation/run-single-rule)                 |
| 4.3    | No           | Prints the rule class name, which the clause forbids                                                                                   |
| 4.4    | No           | Nothing enforces an identifier                                                                                                         |
| 5.1    | Yes          | `vendor/bin/rector --dry-run` runs locally                                                                                             |
| 5.2    | Yes          | Path argument accepted                                                                                                                 |
| 5.3    | Yes          | Diff and rule name print to the terminal                                                                                               |
| 5.4    | Yes          | No CI-only mode                                                                                                                        |
| 6.1    | No           | No resolver keyed on a printed identifier                                                                                              |
| 6.2    | No           | Bundled rule catalogue is on the website                                                                                               |
| 6.3    | No           | Same                                                                                                                                   |
| 7.1    | No           | No listing command                                                                                                                     |
| 7.2    | No           | Follows from 7.1                                                                                                                       |
| 7.3    | No           | Follows from 7.1                                                                                                                       |
| 8.1    | Yes          | `withSkip()` in `rector.php` is read by Rector, [ignoring rules or paths](https://getrector.com/documentation/ignoring-rules-or-paths) |
| 8.2    | No           | No reason field on a skip                                                                                                              |
| 8.3    | Yes          | `@noRector` removed; skips are configuration only, [pull request 3148](https://github.com/rectorphp/rector-src/pull/3148)              |
| 8.4    | No           | Skips are not enumerable with the rules                                                                                                |
| 8.5    | No           | Not documented                                                                                                                         |
| 9.1    | No           | No agent summary                                                                                                                       |
| 9.2    | No           | No delivery mechanism                                                                                                                  |
| 10.1   | Not verified | Not found                                                                                                                              |
| 10.2   | Not verified | Rector runs on itself; coverage not checked                                                                                            |
| 11.1   | No           | No declaration                                                                                                                         |

## Notes for a practitioner

Rector suits a defence whose remedy is a transformation you can state exactly: write the rule, prove it with a fixture under `AbstractRectorTestCase`, sweep with `--dry-run`, and enforce with `--dry-run` failing the build. Treat the class name as the identifier and never move it, and put a comment beside every `withSkip()` entry because the configuration will not ask for one.
