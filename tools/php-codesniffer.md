---
title: PHP_CodeSniffer and Defence Before Fix
summary: Custom sniffs and single-sniff runs; the code is derived from path and printed only with -s; fails 8.3 on phpcs ignore, 8.2, 6.1.
---

# PHP_CodeSniffer

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 4.0.4

PHP_CodeSniffer tokenises PHP and runs sniffs over the token stream, reporting violations of a coding standard and fixing many of them with `phpcbf`. It is usually the style gate in a pipeline, but a sniff can detect any token-level pattern, so it is a serviceable host for a bespoke defence.

## How it is conformant

Clause 4.1 is met: a project defines a standard with a `ruleset.xml` and a `Sniffs` directory, and each sniff subscribes to tokens and reports through `addError` with a code of its own ([coding standard tutorial](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Coding-Standard-Tutorial)). Clause 4.2 is met by the command line: `--sniffs=Standard.Category.Sniff` restricts a run to one sniff, and a file path restricts it to one file, so a red run against a fixture needs no test suite ([advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage)). Clauses 5.1 to 5.4 hold for the same reason. Clause 7.1 is met in part by `phpcs -e`, which lists the sniffs in a standard by code, and by `<arg value="s"/>` in the ruleset, which makes codes print on every finding ([annotated ruleset](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Annotated-Ruleset)). Per-sniff `<exclude-pattern>` entries in the ruleset are a record the tool reads itself, which is clause 8.1's shape.

## How it is not conformant

Clause 4.3 is the readiness gap. The printed code is `Standard.Category.Sniff.ErrorCode`, and the tutorial states it is derived from the directory structure and class name, which is exactly what the clause forbids; only the final segment is the author's to choose, and renaming the sniff file renames every reference. The code is also printed only with `-s`, which the ruleset can hard-code but the default does not. Clause 8.3 fails structurally: `// phpcs:ignore` and `// phpcs:disable` are documented inline routes, and a note after `--` is optional rather than required, so clause 8.2 fails with it ([advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage)). Clause 6.1 fails because nothing resolves a printed code to documentation; `-e` lists names without remedy text, and the bundled standards are documented on the wiki rather than on disk, so 6.2 and 6.3 fail. There is no declaration under clause 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                                                                               |
| ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 4.1    | Yes          | Custom standard and sniffs, [coding standard tutorial](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Coding-Standard-Tutorial)                |
| 4.2    | Yes          | `--sniffs` plus a file path, [advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage)                                   |
| 4.3    | Partial      | Code derived from path and class name; printed only with `-s`, [advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage) |
| 4.4    | No           | `addError` requires a code, but the code need not be stable                                                                                            |
| 5.1    | Yes          | `phpcs` runs locally                                                                                                                                   |
| 5.2    | Yes          | `phpcs /path/to/file`                                                                                                                                  |
| 5.3    | Yes          | Report prints to the terminal                                                                                                                          |
| 5.4    | Yes          | No CI-only mode                                                                                                                                        |
| 6.1    | No           | No lookup keyed on the printed code                                                                                                                    |
| 6.2    | No           | Bundled standards documented on the wiki                                                                                                               |
| 6.3    | No           | Same                                                                                                                                                   |
| 7.1    | Partial      | `phpcs -e` lists sniff codes without what each forbids, [advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage)        |
| 7.2    | Yes          | `-e` is derived from the standard actually loaded                                                                                                      |
| 7.3    | Yes          | Project sniffs appear in `-e` alongside bundled ones                                                                                                   |
| 8.1    | Partial      | Ruleset `<exclude-pattern>` is read by the tool, [annotated ruleset](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Annotated-Ruleset)         |
| 8.2    | No           | Reason after `--` is optional, [advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage)                                 |
| 8.3    | No           | `phpcs:ignore` and `phpcs:disable`, [advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage)                            |
| 8.4    | No           | Exclusions are not listed with the sniffs                                                                                                              |
| 8.5    | No           | Not documented                                                                                                                                         |
| 9.1    | No           | No agent summary                                                                                                                                       |
| 9.2    | No           | No delivery mechanism                                                                                                                                  |
| 10.1   | Not verified | No release gate over sniff documentation found                                                                                                         |
| 10.2   | Not verified | The project runs its own standard in CI; coverage of every sniff was not checked                                                                       |
| 11.1   | No           | No declaration                                                                                                                                         |

## Notes for a practitioner

Put `<arg value="s"/>` in the ruleset so every finding carries its code, never rename a sniff once its code has been printed, and prove a new sniff with `phpcs --sniffs=... fixture.php`. Ban `phpcs:ignore` with a sniff of your own and keep exclusions as ruleset `<exclude-pattern>` entries with a comment above each.
