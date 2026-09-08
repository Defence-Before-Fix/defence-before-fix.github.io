---
title: Prettier and Defence Before Fix
summary: Formatter; plugins cannot report diagnostics so 4.1 and 4.3 fail; prettier-ignore cannot be switched off, failing 7.1
language: JavaScript and TypeScript
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-09-08, version 3.9.6
---

# Prettier

{% include tool-grades.html %}

Prettier is an opinionated formatter. It rewrites source to a canonical layout and, in `--check` mode, reports which files differ from that layout. It is not a detector and it has no rules: its whole value is that there is nothing to configure or defend. In a pipeline it runs first so that every later tool sees canonical code, and it removes the class of formatting disagreement from the review entirely.

## How it is conformant

Section [5](../DETECTOR-SPEC.md#5-reporting) is met: Prettier runs locally, accepts a single file, `--check` reports in the command's output and nothing is held back for a service. Its plugin API contributes parsers, printers and languages ([plugins](https://prettier.io/docs/plugins)), which is enough for a project to teach it a new file type.

## How it is not conformant

Clause [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it) fails structurally because the plugin API cannot report a diagnostic; a plugin changes how code is printed, not what is flagged ([plugins](https://prettier.io/docs/plugins)). A `--check` finding is the file name with no identifier, so [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding) fails as well, there is nothing for a clause [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code) harness to run, and readiness is red because there is no bespoke defence to host. Section [6](../DETECTOR-SPEC.md#6-resolving-an-identifier) has nothing to resolve. `// prettier-ignore` and `.prettierignore` are built-in suppression routes that no option switches off and nothing reports ([ignoring code](https://prettier.io/docs/ignore)), which fails [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable), and no reason is required on either, which fails [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason).

## Clause by clause

| Document | Clause | Result | Evidence                                                                                                                  |
| -------- | ------ | ------ | ------------------------------------------------------------------------------------------------------------------------- |
| Detector | [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)    | No     | Plugins add parsers and printers, not diagnostics ([plugins](https://prettier.io/docs/plugins))                           |
| Detector | [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)    | No     | Nothing to harness                                                                                                        |
| Detector | [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)    | No     | A `--check` finding is a file name                                                                                        |
| Detector | [4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own)    | No     | Not applicable                                                                                                            |
| Detector | [5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure)    | Yes    | Runs locally                                                                                                              |
| Detector | [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file)    | Yes    | Single file path                                                                                                          |
| Detector | [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)    | Yes    | Output of the command                                                                                                     |
| Detector | [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)    | Yes    | Same everywhere                                                                                                           |
| Detector | [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)    | No     | Nothing to resolve                                                                                                        |
| Detector | [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)    | No     | Same                                                                                                                      |
| Detector | [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)    | No     | Same                                                                                                                      |
| Detector | [6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation)    | No     | Not applicable                                                                                                            |
| Detector | [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)    | No     | `prettier-ignore` and `.prettierignore` cannot be disabled or reported ([ignoring code](https://prettier.io/docs/ignore)) |
| Detector | [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)    | No     | No reason on `prettier-ignore`                                                                                            |

## Notes for a practitioner

Run Prettier in write mode locally and in check mode in the gate, and keep it out of the method otherwise: a formatting difference is not a hazard and a formatter is not where a defence lives. Ban `prettier-ignore` with a lint rule if you find it being used to hide something a real defence should catch.
