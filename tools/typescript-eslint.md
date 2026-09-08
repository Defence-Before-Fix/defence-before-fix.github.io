---
title: typescript-eslint and Defence Before Fix
summary: RuleCreator and RuleTester meet 4.1 to 4.3, ESLint supplies section 5 and 7.1; bundled rule pages are online only, failing 6.2 and 6.3
language: JavaScript and TypeScript
kind: tool
readiness: 🟢
detector: 🟡
checked: 2026-09-08, version 8.70.0
---

# typescript-eslint

{% include tool-grades.html %}

typescript-eslint is the parser, rule set and rule-authoring kit that lets ESLint understand TypeScript and, with type information, reason about it. It is a plugin rather than a toolchain, so it inherits ESLint's mechanisms for everything outside rule authoring, and its detector conformance grade follows ESLint's. Its readiness grade is its own, because it is the best place in the ecosystem to write a bespoke type-aware defence.

## How it is conformant

`RuleCreator` from `@typescript-eslint/utils` is a factory that takes a function mapping a rule name to its documentation URL, so every rule built with it carries a `meta.docs.url` by construction; the documentation discourages `RuleCreator.withoutDocs` and tells authors to "include a descriptive error message and link to informative documentation" ([custom rules](https://typescript-eslint.io/developers/custom-rules)). That gives clause [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it) and, because ESLint prints the rule as `@typescript-eslint/rule-name` with the namespace assigned once in the plugin, clause [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding). The `RuleTester` from `@typescript-eslint/rule-tester` runs a single rule against supplied code, with `projectService` for type-aware rules, which is the clause [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code) harness. Section [5](../DETECTOR-SPEC.md#5-reporting) is met through ESLint: a local run, a single file, findings in the command's output and nothing withheld for a service. Clause [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) is met through ESLint's `linterOptions.noInlineConfig`, and the `ban-ts-comment` rule additionally defends against the compiler's own suppression route, with `allow-with-description`, `minimumDescriptionLength` and `descriptionFormat` letting a project require a justification of a given shape ([ban-ts-comment](https://typescript-eslint.io/rules/ban-ts-comment/)).

## How it is not conformant

The failing clauses are [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access) and [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together). Every bundled rule carries a URL, so a printed identifier resolves to documentation under clause [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation), but the pages live on typescript-eslint.io rather than in the installed package, so resolution needs the network and the documentation does not ship with the rule. Clause [4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own) is not met: `RuleCreator` insists on a documentation URL by its signature, which is a different property from a stable identifier, and no rule checks the identifier itself. Clause [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason) is met only for the compiler's directives through `ban-ts-comment`; the reason on an `eslint-disable` comment remains optional and no typescript-eslint rule requires one.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                                          |
| -------- | ------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)    | Yes          | `RuleCreator` for bespoke rules, including type-aware ones ([custom rules](https://typescript-eslint.io/developers/custom-rules))                                 |
| Detector | [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)    | Yes          | `@typescript-eslint/rule-tester` ([custom rules](https://typescript-eslint.io/developers/custom-rules))                                                           |
| Detector | [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)    | Yes          | Rule name chosen by the author under an assigned namespace, printed by ESLint                                                                                     |
| Detector | [4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own)    | No           | `RuleCreator` requires a docs URL by its signature; nothing checks the identifier                                                                                 |
| Detector | [5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure)    | Yes          | Runs through ESLint locally                                                                                                                                       |
| Detector | [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file)    | Yes          | Single file through ESLint                                                                                                                                        |
| Detector | [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)    | Yes          | Findings are the command's output                                                                                                                                 |
| Detector | [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)    | Yes          | Same rules everywhere                                                                                                                                             |
| Detector | [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)    | Yes          | Every bundled rule carries a URL keyed on its name in `meta.docs.url`; bespoke identifiers print unaltered                                                        |
| Detector | [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)    | No           | Bundled rule documentation is on the website                                                                                                                      |
| Detector | [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)    | No           | Docs versioned with the release, not shipped in the package                                                                                                       |
| Detector | [6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation)    | Not verified | The project generates its rule docs from rule metadata; whether a missing page blocks a release is not documented                                                 |
| Detector | [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)    | Yes          | ESLint's `noInlineConfig` disables inline directives; `ban-ts-comment` sees the compiler's ([ban-ts-comment](https://typescript-eslint.io/rules/ban-ts-comment/)) |
| Detector | [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)    | Partial      | `ban-ts-comment` can require a described reason for `@ts-` directives; `eslint-disable` needs none                                                                |

## Notes for a practitioner

Build the bespoke rule with `RuleCreator` pointing at a documentation page in your own repository, prove it red with the typescript-eslint `RuleTester`, and turn on `ban-ts-comment` with `descriptionFormat` so that any remaining compiler suppression states its reason. Everything else the method needs, the record, the listing and the lookup, has to come from the toolchain around it.
