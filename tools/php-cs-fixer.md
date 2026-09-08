---
title: PHP-CS-Fixer and Defence Before Fix
summary: A formatter whose Vendor rule names and describe command meet 4.1, 4.2 and section 6; the name prints only with verbose, failing 4.3.
---

# PHP-CS-Fixer

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Detector conformance**: 🟡 · **Checked**: 2026-09-08, version 3.95.24

PHP-CS-Fixer is a formatter: it rewrites PHP to a configured style, and in `check` or `--dry-run` mode it reports which files it would change. It is not a detector in the method's sense, because it reports files rather than findings, but a custom fixer can encode a pattern and its correct form together, so it can host a bespoke defence of a narrow kind.

## How it is conformant

Clause 4.1 is met: a project registers classes implementing `FixerInterface` through `registerCustomFixers()` in its configuration ([custom rules](https://cs.symfony.com/doc/custom_rules.html)). Clause 4.3 is met in its first half, and better than most: a custom rule's name must match `Vendor/rule_name`, and the author chooses it once, so it is stable and not derived from the class. Clause 4.2 is met by `--rules=Vendor/rule_name` on a single file with `--dry-run --diff`, which shows whether the rule would change the fixture ([usage](https://cs.symfony.com/doc/usage.html)). Clauses 5.1 to 5.4 hold: the tool runs locally, accepts a file path, and prints its result to the terminal with no CI-only mode. Clause 6.1 is met for the built-in catalogue by `php-cs-fixer describe <rule>`, which resolves a printed rule name to its explanation from the installed copy, so clauses 6.2 and 6.3 hold for bundled rules. Clause 7.1 holds because no inline suppression route is documented on the pages checked; exclusions live in the `Finder` and in per-rule configuration, both of which are visible in the configuration file.

## How it is not conformant

Clause 4.3's second half fails, and it decides the grade: the rule name is printed with a finding only under `--verbose`, and the default output lists files without naming the rule ([usage](https://cs.symfony.com/doc/usage.html)). Whether `describe` resolves a custom rule name was not verified, though clause 6.1 asks the detector only for the unaltered name in that case. Clause 7.2 does not apply to an inline route the tool does not offer, and the `notPath()` exclusions in the Finder carry no reason. Clause 4.4 is not met, and clause 6.4 was not verified.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                      |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Yes          | `registerCustomFixers()`, [custom rules](https://cs.symfony.com/doc/custom_rules.html)                        |
| Detector | 4.2    | Yes          | `--rules=<one> --dry-run --diff file.php`, [usage](https://cs.symfony.com/doc/usage.html)                     |
| Detector | 4.3    | Partial      | `Vendor/name` is author-chosen; printed only with `--verbose`, [usage](https://cs.symfony.com/doc/usage.html) |
| Detector | 4.4    | No           | Nothing enforces stability                                                                                    |
| Detector | 5.1    | Yes          | Runs locally                                                                                                  |
| Detector | 5.2    | Yes          | File path accepted, [usage](https://cs.symfony.com/doc/usage.html)                                            |
| Detector | 5.3    | Yes          | Output to the terminal                                                                                        |
| Detector | 5.4    | Yes          | No CI-only mode                                                                                               |
| Detector | 6.1    | Yes          | `describe` resolves built-in names; custom names not verified, [usage](https://cs.symfony.com/doc/usage.html) |
| Detector | 6.2    | Yes          | `describe` works from the installed copy                                                                      |
| Detector | 6.3    | Yes          | Bundled rule descriptions ship in the package                                                                 |
| Detector | 6.4    | Not verified | No release gate over rule descriptions found                                                                  |
| Detector | 7.1    | Yes          | No inline suppression documented; Finder and per-rule exclusions are configuration                            |
| Detector | 7.2    | No           | No inline route to require a reason on; Finder exclusions carry none                                          |

## Notes for a practitioner

Use PHP-CS-Fixer for a defence only where the fix is mechanical and the pattern is syntactic, and run it in `check --verbose` mode so the rule name reaches the output. Prove a custom fixer with `--rules=Vendor/name --dry-run --diff` on a fixture, and prefer PHPStan or PHP_CodeSniffer when the pattern needs a message that teaches rather than a rewrite.
