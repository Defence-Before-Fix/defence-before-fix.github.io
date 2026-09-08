---
title: Stryker and Defence Before Fix
summary: Mutation tester, not a detector; no plugin kind adds a rule, failing 4.1; Stryker disable comments cannot be switched off, failing 7.1
language: JavaScript and TypeScript
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-09-08, version 10.0.0
---

# Stryker

{% include tool-grades.html %}

StrykerJS is a mutation tester. It applies a fixed set of mutations to source code and runs the test suite against each mutant to measure whether the tests would notice. It is not a detector in the sense the method uses: it does not look for a pattern in the code, it measures the strength of the tests. In a pipeline it is the check on the checks, and it has a role in clause 3.3 of the method, since a test that survives mutation is a red proof that never went red.

## How it is conformant

Section [5](../DETECTOR-SPEC.md#5-reporting) is met. Stryker runs locally with no infrastructure, `mutate` accepts a single file and even a line range within it ([configuration](https://stryker-mutator.io/docs/stryker-js/configuration/)), and its report reaches the practitioner in the command's output together with the path of the HTML report it names, which is the shape clause [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran) asks for. Each mutator has a stable name, which is what the disable comment and `excludedMutations` key on.

## How it is not conformant

Clause [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it) fails structurally. The plugin kinds are test runners, reporters, checkers and ignorers ([plugins](https://stryker-mutator.io/docs/stryker-js/plugins/)); none of them lets a project add a mutation of its own or a pattern it wants forbidden, so there is no bespoke defence to host, nothing for a clause [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code) harness to run, and readiness is red on that ground rather than on any weakness in the tool. The mutator names meet only part of clause [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding), since they identify a mutation rather than a defence. Section [6](../DETECTOR-SPEC.md#6-resolving-an-identifier) has nothing to resolve: no command looks up a mutator name and the documentation is on the website. Clause [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) fails because `// Stryker disable` comments are built in, no option switches them off and nothing reports their presence, and clause [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason) fails because the reason after the colon is optional ([disable mutants](https://stryker-mutator.io/docs/stryker-js/disable-mutants/)). The incremental file is a baseline of results rather than of findings and is not graded here.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                             |
| -------- | ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)    | No           | No plugin kind adds a rule or mutator ([plugins](https://stryker-mutator.io/docs/stryker-js/plugins/))                                               |
| Detector | [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)    | No           | Nothing to harness                                                                                                                                   |
| Detector | [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)    | Partial      | Mutator names are stable but they name a mutation, not a defence                                                                                     |
| Detector | [4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own)    | No           | Not applicable                                                                                                                                       |
| Detector | [5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure)    | Yes          | Runs locally                                                                                                                                         |
| Detector | [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file)    | Yes          | `mutate` takes a file and a range ([configuration](https://stryker-mutator.io/docs/stryker-js/configuration/))                                       |
| Detector | [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)    | Yes          | Summary in the command's output, report path named                                                                                                   |
| Detector | [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)    | Yes          | Same everywhere                                                                                                                                      |
| Detector | [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)    | No           | No lookup                                                                                                                                            |
| Detector | [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)    | No           | Documentation is on the website                                                                                                                      |
| Detector | [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)    | No           | Not applicable to a bundled defence                                                                                                                  |
| Detector | [6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation)    | Not verified | Not documented                                                                                                                                       |
| Detector | [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)    | No           | `// Stryker disable` is built in and cannot be disabled or reported ([disable mutants](https://stryker-mutator.io/docs/stryker-js/disable-mutants/)) |
| Detector | [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)    | No           | Disable reason is optional ([disable mutants](https://stryker-mutator.io/docs/stryker-js/disable-mutants/))                                          |

## Notes for a practitioner

Use Stryker to check that the tests around a defect actually fail when the defect is reintroduced, which is the method's red proof applied to a test rather than a rule. Host the defence itself in a linter. If you must disable a mutant, write the reason after the colon and ban the bare form with a lint rule, because Stryker will not require it.
