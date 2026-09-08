---
title: Stryker and Defence Before Fix
summary: Mutation tester, not a detector; fails 4.1 since no plugin kind adds a rule; fails 8.3 on disable comments with an optional reason
---

# Stryker

**Language**: JavaScript and TypeScript · **Kind**: tool · **Readiness**: 🔴 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 10.0.0

StrykerJS is a mutation tester. It applies a fixed set of mutations to source code and runs the test suite against each mutant to measure whether the tests would notice. It is not a detector in the sense the method uses: it does not look for a pattern in the code, it measures the strength of the tests. In a pipeline it is the check on the checks, and it has a role in clause 3.3 of the method, since a test that survives mutation is a red proof that never went red.

## How it is conformant

Very little of the toolchain specification applies. Stryker runs locally with no infrastructure, `mutate` accepts a single file and even a line range within it ([configuration](https://stryker-mutator.io/docs/stryker-js/configuration/)), and its report reaches the practitioner in the command's output and the HTML report it names. Each mutator has a stable name, which is what the disable comment and `excludedMutations` key on.

## How it is not conformant

Clause 4.1 fails structurally. The plugin kinds are test runners, reporters, checkers and ignorers ([plugins](https://stryker-mutator.io/docs/stryker-js/plugins/)); none of them lets a project add a mutation of its own or a pattern it wants forbidden, so there is no bespoke defence to host and readiness is red on that ground rather than on any weakness in the tool. Clause 8.3 fails too: `// Stryker disable` comments are built in and the reason after the colon is optional ([disable mutants](https://stryker-mutator.io/docs/stryker-js/disable-mutants/)), and the incremental file is a baseline of results. There is no identifier resolution, no listing, no project record and no declaration under 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                                       |
| ------ | ------------ | -------------------------------------------------------------------------------------------------------------- |
| 4.1    | No           | No plugin kind adds a rule or mutator ([plugins](https://stryker-mutator.io/docs/stryker-js/plugins/))         |
| 4.2    | No           | Nothing to harness                                                                                             |
| 4.3    | Partial      | Mutator names are stable but they name a mutation, not a defence                                               |
| 4.4    | No           | Not applicable                                                                                                 |
| 5.1    | Yes          | Runs locally                                                                                                   |
| 5.2    | Yes          | `mutate` takes a file and a range ([configuration](https://stryker-mutator.io/docs/stryker-js/configuration/)) |
| 5.3    | Yes          | Summary in the command's output, report path named                                                             |
| 5.4    | Yes          | Same everywhere                                                                                                |
| 6.1    | No           | No lookup                                                                                                      |
| 6.2    | No           | Documentation is on the website                                                                                |
| 6.3    | No           | Not applicable to a bundled defence                                                                            |
| 7.1    | No           | No listing                                                                                                     |
| 7.2    | No           | Same                                                                                                           |
| 7.3    | No           | Same                                                                                                           |
| 8.1    | No           | No project record                                                                                              |
| 8.2    | No           | Disable reason is optional ([disable mutants](https://stryker-mutator.io/docs/stryker-js/disable-mutants/))    |
| 8.3    | No           | `// Stryker disable` is built in and undefended                                                                |
| 8.4    | No           | No listing                                                                                                     |
| 8.5    | Partial      | Default thresholds are documented                                                                              |
| 9.1    | No           | No agent summary                                                                                               |
| 9.2    | No           | No delivery mechanism                                                                                          |
| 10.1   | Not verified | Not documented                                                                                                 |
| 10.2   | Not verified | Not documented                                                                                                 |
| 11.1   | No           | No declaration                                                                                                 |

## Notes for a practitioner

Use Stryker to check that the tests around a defect actually fail when the defect is reintroduced, which is the method's red proof applied to a test rather than a rule. Host the defence itself in a linter. If you must disable a mutant, write the reason after the colon and ban the bare form with a lint rule, because Stryker will not require it.
