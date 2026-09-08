---
title: ts-qa-ci and Defence Before Fix
summary: Every MUST verified by running rule, rule-doc and rules; declares method 1.0.0 and toolchain 0.1.0 with an empty gap record; 4.4 and 9.2 open
---

# ts-qa-ci

**Language**: JavaScript and TypeScript · **Kind**: toolchain · **Readiness**: 🟢 · **Conformance**: 🟢 · **Checked**: 2026-09-08, version 0.1.0 at commit 4203dc8

ts-qa-ci is an orchestrated QA pipeline for TypeScript and React projects, published as `@longtermsupport/ts-qa-ci` ([repository](https://github.com/LongTermSupport/ts-qa-ci)). One command runs oxlint as a pre-filter, then Prettier, ESLint with a bundled plugin of Component-Driven Development rules, the TypeScript compiler, dependency-cruiser, knip and the test suite, auto-fixing locally and failing the gate on anything it cannot fix. It is the reference toolchain for this specification in the JavaScript ecosystem, and the grades below were checked by running its commands rather than by reading its README.

## Tools it bundles

The pipeline runs in five phases, fail-fast between them. For each tool: whether it can host a bespoke defence under the method, and which of the toolchain's own mechanisms wrap it.

- **Phase 0, fast fail: eslintConfigParity.** A check of the toolchain's own that the project's ESLint configuration matches what the pipeline resolves. Not a defence host. Reported through the pipeline verdict only.
- **Phase 0, fast fail: supplyChain.** A dependency bake-window audit. Not a defence host. Reported through the pipeline verdict only.
- **Phase 0, fast fail: oxlint.** Can host a bespoke defence through its JS plugin mechanism, though ts-qa-ci uses it as a pre-filter with built-in rules only. Its `oxlint-disable` directives are banned by the bundled `ts-qa/no-eslint-disable` rule; `ts-qa rule`, `ts-qa rule-doc` and `ts-qa rules` do not cover oxlint findings.
- **Phase 1, code modification: prettier.** A formatter; cannot host a defence. Not wrapped.
- **Phase 1, code modification: eslintFix.** ESLint in write mode over the same resolved configuration as the report lane; hosts bespoke defences, and is wrapped by all three of `ts-qa rule`, `ts-qa rule-doc` and `ts-qa rules`.
- **Phase 2, lint and validation: eslintReport.** ESLint in report mode; the lane every bundled and bespoke defence runs in, and the one `ts-qa rule` narrows to a single identifier. Wrapped by `ts-qa rule`, `ts-qa rule-doc` and `ts-qa rules`.
- **Phase 2, lint and validation: remarkValidateLinks.** A Markdown link checker; a fixed catalogue, cannot host a defence. Not wrapped.
- **Phase 2, lint and validation: knip.** Unused file, export and dependency detection; a fixed catalogue, cannot host a defence. Not wrapped.
- **Phase 3, static analysis: tsc.** The compiler's fixed catalogue; cannot host a defence. Its `@ts-` directives are banned by `ts-qa/no-eslint-disable`. Not otherwise wrapped.
- **Phase 3, static analysis: dependencyCruiser.** Can host a bespoke architectural defence in its own configuration, with its own identifier and comment; not wrapped by `ts-qa rule`, `ts-qa rule-doc` or `ts-qa rules`, so a dependency-cruiser rule does not appear in the derived listing.
- **Phase 4, tests: vitest.** A test runner; cannot host a defence. Runs the toolchain's own self-audit test under clause 10.1. Not wrapped.
- **Phase 4, tests: playwright.** An end-to-end test runner; cannot host a defence. Not wrapped.

The three conformance mechanisms therefore cover the ESLint lanes in full and nothing else. A bespoke defence written for dependency-cruiser or oxlint is real but lives outside the listing, the lookup and the harness, which is worth knowing before choosing where to put a rule.

## How it is conformant

Bespoke rules under clause 4.1 enter through `tsQaConfig/eslint.config.js`, which is merged into the resolved flat config, so any ESLint plugin object the project writes is a first-class defence. Clause 4.2 is met by `ts-qa rule <identifier> <path>`, which runs the ordinary lint lane over one path and reports whether that one rule fired, exiting 1 with locations when it did; a fixture with an `eslint-disable` comment placed in the source tree made `ts-qa/no-eslint-disable` fire and a clean rule stay silent. Identifiers are `ts-qa/<name>`, chosen once in the plugin map and printed by ESLint with every finding, which is clause 4.3. Sections 5 and 7 are met by `npx ts-qa`, its `-p <path>` subset flag and `ts-qa rules`, which walks the resolved configuration and prints each active defence's identifier, severity, a terse description and the on-disk documentation route, then the project record beneath it in the same listing; that satisfies 7.1 to 7.3 and 8.4 in one command. Clause 6.1 and 6.2 are met by `ts-qa rule-doc <identifier>`, which resolves the identifier exactly as printed to its section in the shipped `docs/cdd-rules.md` and prints it. The project record under 8.1 is `tsQaConfig/tier-a-exemptions.json`, loaded by the toolchain itself; an entry without a justification throws, and a justification that names neither the hazard nor the scope, or matches a documented list of vacuous phrases, is rejected with the entry named ([configuration](https://github.com/LongTermSupport/ts-qa-ci/blob/main/docs/configuration.md)), which is 8.2. Clause 8.3 is met by the bundled `ts-qa/no-eslint-disable` rule, which bans every `eslint-disable`, `oxlint-disable` and `@ts-` directive form and points the reader at the project record. Clause 10.1 is a test in the suite that asserts every bundled identifier resolves to a section of the shipped documentation, and 10.2 is the continuous integration workflow, which runs `npx ts-qa` on the package itself and fails on anything it cannot fix. Clause 11.1 is the `defenceBeforeFix` key in `package.json`, declaring method 1.0.0 and toolchain 0.1.0 with an empty `knownGaps` array.

## How it is not conformant

No MUST was found failing. Two SHOULDs are open. Clause 4.4, a rule over the rules that fails a defence reporting without a stable identifier, is not present. Clause 9.2 is met only in part: `ts-qa deploy-skills` copies static skill and agent files into a consuming project, but the generated rule summary from `ts-qa rules` is not written into the file the project's agents load, so the summary exists and the delivery channel exists without the one flowing through the other.

## Clause by clause

| Clause | Result  | Evidence                                                                                                                                                    |
| ------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes     | `tsQaConfig/eslint.config.js` merged into the resolved config                                                                                               |
| 4.2    | Yes     | `ts-qa rule ts-qa/no-eslint-disable src/probe.ts` exited 1 with the location; a non-firing rule exited 0                                                    |
| 4.3    | Yes     | `ts-qa/<name>` chosen in the plugin map, printed by ESLint                                                                                                  |
| 4.4    | No      | No rule over the rules                                                                                                                                      |
| 5.1    | Yes     | `npx ts-qa`                                                                                                                                                 |
| 5.2    | Yes     | `-p <path>` and the single-path `rule` command                                                                                                              |
| 5.3    | Yes     | Verdict table in the command's output with the path to `last-run.json`                                                                                      |
| 5.4    | Yes     | Same pipeline locally and in CI                                                                                                                             |
| 6.1    | Yes     | `ts-qa rule-doc ts-qa/no-eslint-disable` printed the summary and the shipped section                                                                        |
| 6.2    | Yes     | `docs/` is in the package `files` list and the printed route is a local path                                                                                |
| 6.3    | Yes     | Every bundled rule has a section in `docs/cdd-rules.md`, shipped at the same version                                                                        |
| 7.1    | Yes     | `ts-qa rules` printed eighteen active defences with identifier, description and route                                                                       |
| 7.2    | Yes     | The listing walks the resolved ESLint configuration                                                                                                         |
| 7.3    | Yes     | The project's own rules, including the toolchain's self-only rule, appear in the same listing                                                               |
| 8.1    | Yes     | `tsQaConfig/tier-a-exemptions.json`, loaded by the toolchain                                                                                                |
| 8.2    | Yes     | Missing or vacuous justification throws with the entry named ([configuration](https://github.com/LongTermSupport/ts-qa-ci/blob/main/docs/configuration.md)) |
| 8.3    | Yes     | `ts-qa/no-eslint-disable` bans every directive form, including oxlint's                                                                                     |
| 8.4    | Yes     | The project record is printed by `ts-qa rules` beneath the defences                                                                                         |
| 8.5    | Yes     | The always-on tier and its reasoning are documented in `docs/coding-standards.md`                                                                           |
| 9.1    | Partial | `ts-qa rules` output is one line per defence with identifier and route, phrased as a description                                                            |
| 9.2    | Partial | `deploy-skills` delivers static skills, not the generated summary                                                                                           |
| 10.1   | Yes     | Test asserting every bundled identifier resolves, run by the pipeline in CI                                                                                 |
| 10.2   | Yes     | CI runs `npx ts-qa --write` on the package itself and fails on unfixable findings                                                                           |
| 11.1   | Yes     | `package.json` `defenceBeforeFix`: method 1.0.0, toolchain 0.1.0, `knownGaps` empty                                                                         |

## Notes for a practitioner

Install the package, run `npx ts-qa init` to scaffold `tsQaConfig/`, and write your defence as a rule in `tsQaConfig/eslint.config.js` with a section in your own documentation. Prove it with `ts-qa rule <identifier> <fixture>`, check it appears in `ts-qa rules`, and put any irreducible exception in `tier-a-exemptions.json` with the hazard and scope written down, since the toolchain will reject anything less.
