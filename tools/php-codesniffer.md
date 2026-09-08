---
title: PHP_CodeSniffer and Defence Before Fix
summary: Custom sniffs and single-sniff runs meet 4.1, 4.2 and section 5; the code is path-derived under 4.3 and nothing resolves it, failing 6.1 to 6.3.
---

# PHP_CodeSniffer

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Detector conformance**: 🟡 · **Checked**: 2026-09-08, version 4.0.4

PHP_CodeSniffer tokenises PHP and runs sniffs over the token stream, reporting violations of a coding standard and fixing many of them with `phpcbf`. It is usually the style gate in a pipeline, but a sniff can detect any token-level pattern, so it is a serviceable host for a bespoke defence.

## How it is conformant

Clause 4.1 is met: a project defines a standard with a `ruleset.xml` and a `Sniffs` directory, and each sniff subscribes to tokens and reports through `addError` with a code of its own ([coding standard tutorial](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Coding-Standard-Tutorial)). Clause 4.2 is met by the command line: `--sniffs=Standard.Category.Sniff` restricts a run to one sniff, and a file path restricts it to one file, so a red run against a fixture needs no test suite ([advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage)). Clauses 5.1 to 5.4 hold for the same reason: the run is local, takes a single file and prints its report to the terminal. Clause 7.1 is met because `--ignore-annotations` disables every `phpcs:ignore` and `phpcs:disable` comment, the ruleset can hard-code that flag with `<arg name="ignore-annotations"/>`, and the tokeniser exposes the annotations as their own tokens so a project sniff can detect them ([advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage), [annotated ruleset](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Annotated-Ruleset)).

## How it is not conformant

Clause 4.3 is the readiness gap and a failing MUST. The printed code is `Standard.Category.Sniff.ErrorCode`, and the tutorial states it is derived from the directory structure and class name, which is exactly what the clause forbids; only the final segment is the author's to choose, and renaming the sniff file renames every reference. The code is also printed only with `-s`, which the ruleset can hard-code with `<arg value="s"/>` but the default output omits. Clauses 6.1 to 6.3 fail: nothing resolves a printed code to documentation, `-e` lists names without remedy text, and the bundled standards are documented on the wiki rather than on disk. Clause 7.2 fails because a note after `--` on an ignore comment is optional rather than required ([advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage)). Clause 4.4 is not met, since `addError` requires a code but nothing checks that it is stable, and clause 6.4 was not verified.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                                                          |
| -------- | ------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Yes          | Custom standard and sniffs, [coding standard tutorial](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Coding-Standard-Tutorial)                                           |
| Detector | 4.2    | Yes          | `--sniffs` plus a file path, [advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage)                                                              |
| Detector | 4.3    | Partial      | Code derived from path and class name; printed only with `-s`, [advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage)                            |
| Detector | 4.4    | No           | `addError` requires a code, but the code need not be stable                                                                                                                       |
| Detector | 5.1    | Yes          | `phpcs` runs locally                                                                                                                                                              |
| Detector | 5.2    | Yes          | `phpcs /path/to/file`                                                                                                                                                             |
| Detector | 5.3    | Yes          | Report prints to the terminal                                                                                                                                                     |
| Detector | 5.4    | Yes          | No CI-only mode                                                                                                                                                                   |
| Detector | 6.1    | No           | No lookup keyed on the printed code                                                                                                                                               |
| Detector | 6.2    | No           | Bundled standards documented on the wiki                                                                                                                                          |
| Detector | 6.3    | No           | Same                                                                                                                                                                              |
| Detector | 6.4    | Not verified | No release gate over sniff documentation found                                                                                                                                    |
| Detector | 7.1    | Yes          | `--ignore-annotations` disables inline routes; annotations are tokens a sniff can detect, [advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage) |
| Detector | 7.2    | No           | Reason after `--` is optional, [advanced usage](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Advanced-Usage)                                                            |

## Notes for a practitioner

Put `<arg value="s"/>` in the ruleset so every finding carries its code, never rename a sniff once its code has been printed, and prove a new sniff with `phpcs --sniffs=... fixture.php`. Set `--ignore-annotations` in the ruleset or ban `phpcs:ignore` with a sniff of your own, and keep exclusions as ruleset `<exclude-pattern>` entries with a comment above each.
