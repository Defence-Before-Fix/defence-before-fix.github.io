---
title: PHP-CS-Fixer and Defence Before Fix
summary: A formatter; custom fixers carry stable Vendor names printed only with verbose; fails 8.2 on unjustified exclusions and 7.1 on listing.
---

# PHP-CS-Fixer

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 3.95.24

PHP-CS-Fixer is a formatter: it rewrites PHP to a configured style, and in `check` or `--dry-run` mode it reports which files it would change. It is not a detector in the method's sense, because it reports files rather than findings, but a custom fixer can encode a pattern and its correct form together, so it can host a bespoke defence of a narrow kind.

## How it is conformant

Clause 4.1 is met: a project registers classes implementing `FixerInterface` through `registerCustomFixers()` in its configuration ([custom rules](https://cs.symfony.com/doc/custom_rules.html)). Clause 4.3 is met in part, and better than most: a custom rule's name must match `Vendor/rule_name`, and the author chooses it once, so it is stable and not derived from the class. Clause 4.2 is met by `--rules=Vendor/rule_name` on a single file with `--dry-run --diff`, which shows whether the rule would change the fixture ([usage](https://cs.symfony.com/doc/usage.html)). Clauses 5.1 and 5.2 hold: the tool runs locally and accepts a file path. Clause 6.1 is met for the built-in catalogue by `php-cs-fixer describe <rule>`, which resolves a printed rule name to its explanation from the installed copy, so clauses 6.2 and 6.3 hold for bundled rules.

## How it is not conformant

The readiness limit is clause 4.3's second half: the rule name is printed with a finding only under `--verbose`, and the default output lists files without naming the rule ([usage](https://cs.symfony.com/doc/usage.html)). Clause 8.2 fails structurally: exclusions live in the `Finder` and in per-rule configuration with no field for a reason. Clause 8.3 was not verified; no inline suppression is documented on the pages checked, which if true is a point in its favour, but `notPath()` exclusions in the Finder are silent. Clause 7.1 fails because no command lists the rules active in a project's configuration with what each enforces; `list-sets` names sets and `describe` takes one rule at a time. Whether `describe` resolves a custom rule name was not verified. There is no declaration under clause 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                                      |
| ------ | ------------ | ------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | `registerCustomFixers()`, [custom rules](https://cs.symfony.com/doc/custom_rules.html)                        |
| 4.2    | Yes          | `--rules=<one> --dry-run --diff file.php`, [usage](https://cs.symfony.com/doc/usage.html)                     |
| 4.3    | Partial      | `Vendor/name` is author-chosen; printed only with `--verbose`, [usage](https://cs.symfony.com/doc/usage.html) |
| 4.4    | No           | Nothing enforces stability                                                                                    |
| 5.1    | Yes          | Runs locally                                                                                                  |
| 5.2    | Yes          | File path accepted, [usage](https://cs.symfony.com/doc/usage.html)                                            |
| 5.3    | Yes          | Output to the terminal                                                                                        |
| 5.4    | Yes          | No CI-only mode                                                                                               |
| 6.1    | Partial      | `describe` resolves built-in names; custom names not verified, [usage](https://cs.symfony.com/doc/usage.html) |
| 6.2    | Yes          | `describe` works from the installed copy                                                                      |
| 6.3    | Yes          | Bundled rule descriptions ship in the package                                                                 |
| 7.1    | No           | No listing of active rules with what each enforces                                                            |
| 7.2    | No           | Follows from 7.1                                                                                              |
| 7.3    | No           | Follows from 7.1                                                                                              |
| 8.1    | Partial      | Config file and Finder are read by the tool                                                                   |
| 8.2    | No           | No reason field on any exclusion                                                                              |
| 8.3    | Not verified | No inline suppression documented on the pages checked                                                         |
| 8.4    | No           | Exclusions are not enumerable                                                                                 |
| 8.5    | No           | Not documented                                                                                                |
| 9.1    | No           | No agent summary                                                                                              |
| 9.2    | No           | No delivery mechanism                                                                                         |
| 10.1   | Not verified | Not found                                                                                                     |
| 10.2   | Not verified | Not checked                                                                                                   |
| 11.1   | No           | No declaration                                                                                                |

## Notes for a practitioner

Use PHP-CS-Fixer for a defence only where the fix is mechanical and the pattern is syntactic, and run it in `check --verbose` mode so the rule name reaches the output. Prove a custom fixer with `--rules=Vendor/name --dry-run --diff` on a fixture, and prefer PHPStan or PHP_CodeSniffer when the pattern needs a message that teaches rather than a rewrite.
