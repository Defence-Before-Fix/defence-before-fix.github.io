---
title: PHP-CS-Fixer and Defence Before Fix
summary: A formatter whose Vendor rule names and describe command meet 4.1, 4.2 and section 6; the name prints only with verbose, failing 4.3.
language: PHP
kind: tool
readiness: 🟡
detector: 🟡
checked: 2026-09-08, version 3.95.24
---

# PHP-CS-Fixer

{% include tool-grades.html %}

PHP-CS-Fixer is a formatter: it rewrites PHP to a configured style, and in `check` or `--dry-run` mode it reports which files it would change. It is not a detector in the method's sense, because it reports files rather than findings, but a custom fixer can encode a pattern and its correct form together, so it can host a bespoke defence of a narrow kind.

## How it is conformant

Clause [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it) is met: a project registers classes implementing `FixerInterface` through `registerCustomFixers()` in its configuration ([custom rules](https://cs.symfony.com/doc/custom_rules.html)). Clause [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding) is met in its first half, and better than most: a custom rule's name must match `Vendor/rule_name`, and the author chooses it once, so it is stable and not derived from the class. Clause [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code) is met by `--rules=Vendor/rule_name` on a single file with `--dry-run --diff`, which shows whether the rule would change the fixture ([usage](https://cs.symfony.com/doc/usage.html)). Clauses [5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure) to [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally) hold: the tool runs locally, accepts a file path, and prints its result to the terminal with no CI-only mode. Clause [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation) is met for the built-in catalogue by `php-cs-fixer describe <rule>`, which resolves a printed rule name to its explanation from the installed copy, so clauses [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access) and [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together) hold for bundled rules. Clause [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) holds because no inline suppression route is documented on the pages checked; exclusions live in the `Finder` and in per-rule configuration, both of which are visible in the configuration file.

## How it is not conformant

Clause [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)'s second half fails, and it decides the grade: the rule name is printed with a finding only under `--verbose`, and the default output lists files without naming the rule ([usage](https://cs.symfony.com/doc/usage.html)). Whether `describe` resolves a custom rule name was not verified, though clause [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation) asks the detector only for the unaltered name in that case. Clause [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason) does not apply to an inline route the tool does not offer, and the `notPath()` exclusions in the Finder carry no reason. Clause [4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own) is not met, and clause [6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation) was not verified.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                      |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------- |
| Detector | [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)    | Yes          | `registerCustomFixers()`, [custom rules](https://cs.symfony.com/doc/custom_rules.html)                        |
| Detector | [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)    | Yes          | `--rules=<one> --dry-run --diff file.php`, [usage](https://cs.symfony.com/doc/usage.html)                     |
| Detector | [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)    | Partial      | `Vendor/name` is author-chosen; printed only with `--verbose`, [usage](https://cs.symfony.com/doc/usage.html) |
| Detector | [4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own)    | No           | Nothing enforces stability                                                                                    |
| Detector | [5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure)    | Yes          | Runs locally                                                                                                  |
| Detector | [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file)    | Yes          | File path accepted, [usage](https://cs.symfony.com/doc/usage.html)                                            |
| Detector | [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)    | Yes          | Output to the terminal                                                                                        |
| Detector | [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)    | Yes          | No CI-only mode                                                                                               |
| Detector | [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)    | Yes          | `describe` resolves built-in names; custom names not verified, [usage](https://cs.symfony.com/doc/usage.html) |
| Detector | [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)    | Yes          | `describe` works from the installed copy                                                                      |
| Detector | [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)    | Yes          | Bundled rule descriptions ship in the package                                                                 |
| Detector | [6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation)    | Not verified | No release gate over rule descriptions found                                                                  |
| Detector | [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)    | Yes          | No inline suppression documented; Finder and per-rule exclusions are configuration                            |
| Detector | [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)    | No           | No inline route to require a reason on; Finder exclusions carry none                                          |

## Notes for a practitioner

Use PHP-CS-Fixer for a defence only where the fix is mechanical and the pattern is syntactic, and run it in `check --verbose` mode so the rule name reaches the output. Prove a custom fixer with `--rules=Vendor/name --dry-run --diff` on a fixture, and prefer PHPStan or PHP_CodeSniffer when the pattern needs a message that teaches rather than a rewrite.
