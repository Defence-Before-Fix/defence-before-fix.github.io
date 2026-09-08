---
title: PHPStan and Defence Before Fix
summary: First-class bespoke rules, single-rule harness and identifiers; fails 8.3 on inline ignores and the baseline, 8.2 on unjustified ignoreErrors, 7.1 on listing.
---

# PHPStan

**Language**: PHP · **Kind**: tool · **Readiness**: 🟢 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 2.2.13

PHPStan is a static analyser that reads PHP without running it and reports type errors, dead code and any pattern a rule class describes. It is the detector most PHP pipelines already run, and it is the detector both reference toolchains for this method build on, so it is the natural host for a bespoke defence in PHP.

## How it is conformant

Clause 4.1 is met in full: a project registers its own rule class under `rules:` in its configuration, or as a service tagged `phpstan.rules.rule` where the constructor needs arguments, and the rule can express any pattern the AST exposes ([developing rules](https://phpstan.org/developing-extensions/rules)). Clause 4.2 is met by `PHPStan\Testing\RuleTestCase`, a PHPUnit base class that runs one rule over one fixture file and asserts the errors it reports, without the project's own suite ([the same page](https://phpstan.org/developing-extensions/rules)). Clause 4.3 is met by `RuleErrorBuilder::identifier()`, where the author chooses the string once, and the [error identifiers page](https://phpstan.org/error-identifiers) states that the identifier is printed alongside each error. Clauses 5.1 to 5.4 hold: `phpstan analyse` accepts one or more file paths, runs locally, and prints its findings to the terminal ([command line usage](https://phpstan.org/user-guide/command-line-usage)). Clause 8.1 is partly met, in that `ignoreErrors` in the configuration is a record PHPStan itself reads ([ignoring errors](https://phpstan.org/user-guide/ignoring-errors)).

## How it is not conformant

PHPStan is a detector rather than a toolchain, and it makes no claim under clause 11.1, so it could not be graded conforming even if every mechanism were present. Clause 8.3 fails structurally: `@phpstan-ignore` comments are a first class suppression route that bypasses the configuration, and PHPStan ships nothing that forbids them, though `reportIgnoresWithoutComments` at least demands a reason on each one ([ignoring errors](https://phpstan.org/user-guide/ignoring-errors)). The baseline feature is a further bypass, and the [baseline page](https://phpstan.org/user-guide/baseline) says plainly that a reason is not an option when using the baseline. Clause 8.2 fails for the configuration route too, because an `ignoreErrors` entry has keys for message, identifier, path and count and none for a justification. Clause 6.1 is met only for PHPStan's own identifiers, and only online: the catalogue at phpstan.org is keyed on the printed identifier, but nothing on disk resolves a bespoke identifier, so clause 6.2 fails. Clause 7.1 fails because no command lists the loaded rules; the [command line usage page](https://phpstan.org/user-guide/command-line-usage) documents `analyse`, `clear-result-cache`, `diagnose` and `bisect` and nothing that enumerates rules.

## Clause by clause

| Clause | Result       | Evidence                                                                                                                                                     |
| ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 4.1    | Yes          | `rules:` and the `phpstan.rules.rule` service tag, [developing rules](https://phpstan.org/developing-extensions/rules)                                       |
| 4.2    | Yes          | `RuleTestCase` runs one rule over one fixture, [developing rules](https://phpstan.org/developing-extensions/rules)                                           |
| 4.3    | Yes          | `RuleErrorBuilder::identifier()`, printed with each error, [error identifiers](https://phpstan.org/error-identifiers)                                        |
| 4.4    | No           | Nothing fails a rule that reports without an identifier; the builder accepts a message alone                                                                 |
| 5.1    | Yes          | `vendor/bin/phpstan analyse` runs locally, [command line usage](https://phpstan.org/user-guide/command-line-usage)                                           |
| 5.2    | Yes          | Paths may be single files, [command line usage](https://phpstan.org/user-guide/command-line-usage)                                                           |
| 5.3    | Yes          | The table formatter prints findings to the invoking terminal, [output format](https://phpstan.org/user-guide/output-format)                                  |
| 5.4    | Yes          | No mode is CI only; the same command runs anywhere                                                                                                           |
| 6.1    | Partial      | Online catalogue keyed on the identifier for bundled rules only, [error identifiers](https://phpstan.org/error-identifiers)                                  |
| 6.2    | No           | The catalogue is a website; nothing installed resolves an identifier                                                                                         |
| 6.3    | No           | Bundled rule documentation lives on phpstan.org, not in the package                                                                                          |
| 7.1    | No           | No command lists loaded rules, [command line usage](https://phpstan.org/user-guide/command-line-usage)                                                       |
| 7.2    | No           | Follows from 7.1                                                                                                                                             |
| 7.3    | No           | Follows from 7.1                                                                                                                                             |
| 8.1    | Partial      | `ignoreErrors` is read by PHPStan, but it is one record among inline comments and baselines                                                                  |
| 8.2    | No           | `ignoreErrors` entries carry no reason; `reportIgnoresWithoutComments` covers inline only, [ignoring errors](https://phpstan.org/user-guide/ignoring-errors) |
| 8.3    | No           | `@phpstan-ignore` and `--generate-baseline` bypass the record, [baseline](https://phpstan.org/user-guide/baseline)                                           |
| 8.4    | No           | Follows from 7.1                                                                                                                                             |
| 8.5    | Partial      | Rule levels are documented defaults; nothing covers the method's own calibrations                                                                            |
| 9.1    | No           | No agent summary                                                                                                                                             |
| 9.2    | No           | No delivery mechanism                                                                                                                                        |
| 10.1   | Not verified | The online catalogue appears complete; no published release gate was found                                                                                   |
| 10.2   | Not verified | PHPStan analyses itself in CI; whether every bundled rule is active there was not checked                                                                    |
| 11.1   | No           | No declaration of the method version                                                                                                                         |

## Notes for a practitioner

PHPStan alone gives you every mechanism the six clauses of the method need: write the rule class, prove it with `RuleTestCase`, sweep with `phpstan analyse`, and give the error an identifier. What it does not give you is the governance: set `reportIgnoresWithoutComments`, add a rule of your own that forbids `@phpstan-ignore`, keep the identifier index in the repository, and expect to build the listing yourself or adopt a toolchain that has.
