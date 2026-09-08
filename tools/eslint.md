---
title: ESLint and Defence Before Fix
summary: Bespoke rules, harness and printed identifiers meet 4.1 to 4.3; noInlineConfig meets 7.1; core rule documentation is online only, failing 6.2 and 6.3
---

# ESLint

**Language**: JavaScript and TypeScript · **Kind**: tool · **Readiness**: 🟢 · **Detector conformance**: 🟡 · **Checked**: 2026-09-08, version 10.10.0

ESLint is the pluggable linter for JavaScript and TypeScript, and the detector most Defence Before Fix work in this ecosystem is built on. It parses source into an AST, runs every configured rule over it and prints each finding with the rule's identifier. In a pipeline it is the host for bespoke rules; on its own it is a detector rather than a toolchain, and the grading below is against the detector specification alone.

## How it is conformant

Bespoke rules are the core of the design rather than an afterthought. A rule is a module with `meta` and `create`, registered through a plugin object in the flat config, and `meta.docs` carries both a `description` and a `url` ([custom rules](https://eslint.org/docs/latest/extend/custom-rules)), which is what clause 4.1 asks for. The identifier printed with every finding is the configured rule name, as the stylish formatter's sample output shows with `no-unused-vars` at the end of each line ([formatters](https://eslint.org/docs/latest/use/formatters/)), and the JSON formatters carry the same `ruleId`. A plugin rule prints as `plugin/rule`, and that prefix is a namespace the author assigns once in the plugin object rather than anything derived from the file path, so clause 4.3 holds in full. The harness for the red proof under clause 4.2 exists twice over: `RuleTester` runs one rule against supplied code without the project's test suite, and on the command line `--rule` combined with `--no-config-lookup` runs only the rules named on a single file or on `--stdin` ([command line interface](https://eslint.org/docs/latest/use/command-line-interface)). Clauses 5.1 and 5.2 are met by that same invocation, 5.3 by the fact that findings land in the command's own output, and 5.4 because nothing is held back for a hosted service. For clause 7.1, `linterOptions.noInlineConfig` disables every inline directive by configuration, and `reportUnusedDisableDirectives` can be set to error ([configuring rules](https://eslint.org/docs/latest/use/configure/rules)); the bulk suppressions file lives at a documented path, so a project can check for its presence mechanically.

## How it is not conformant

The failing clauses are 6.2 and 6.3, both about the bundled catalogue. Every core rule's identifier maps to a page on eslint.org, and the installed package carries that URL in `meta.docs.url`, so clause 6.1 is met as a URL keyed on the printed identifier; but the page itself is on the network rather than in the installed package, so resolution does not work offline under 6.2 and the documentation does not ship with the rule under 6.3. Clause 4.4 is not met: no bundled rule checks that a rule reports with a stable identifier, although ESLint's registration model makes an identifier hard to omit. Clause 7.2 is not met: the description after `--` in an `eslint-disable` comment is optional, no option makes it mandatory, and the bulk suppressions file written by `--suppress-all` records no justification for any entry ([bulk suppressions](https://eslint.org/docs/latest/use/suppressions)). Both of those are SHOULDs, so they do not decide the grade on their own.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                                                             |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Detector | 4.1    | Yes          | Plugin rules are first class ([custom rules](https://eslint.org/docs/latest/extend/custom-rules))                                                                                    |
| Detector | 4.2    | Yes          | `RuleTester`, or `--rule` with `--no-config-lookup` on one file ([CLI](https://eslint.org/docs/latest/use/command-line-interface))                                                   |
| Detector | 4.3    | Yes          | Rule name chosen by the author; the `plugin/` prefix is an assigned namespace; printed with every finding ([formatters](https://eslint.org/docs/latest/use/formatters/))             |
| Detector | 4.4    | No           | No bundled rule checks that rules carry an identifier                                                                                                                                |
| Detector | 5.1    | Yes          | `npx eslint` runs locally with no infrastructure                                                                                                                                     |
| Detector | 5.2    | Yes          | Positional file paths and `--stdin` ([CLI](https://eslint.org/docs/latest/use/command-line-interface))                                                                               |
| Detector | 5.3    | Yes          | Findings are the command's output                                                                                                                                                    |
| Detector | 5.4    | Yes          | Same rules run in every environment                                                                                                                                                  |
| Detector | 6.1    | Yes          | Core identifiers map to eslint.org pages through `meta.docs.url`; a bespoke identifier is printed unaltered                                                                          |
| Detector | 6.2    | No           | Core rule documentation is on the website, not in the installed package                                                                                                              |
| Detector | 6.3    | No           | Core rule docs are versioned with the release but not shipped in it                                                                                                                  |
| Detector | 6.4    | Not verified | ESLint's repository has documentation checks; whether a missing rule page blocks a release is not documented on the site                                                             |
| Detector | 7.1    | Yes          | `linterOptions.noInlineConfig` disables inline directives; the suppressions file has a documented location ([configuring rules](https://eslint.org/docs/latest/use/configure/rules)) |
| Detector | 7.2    | No           | Disable descriptions are optional and `eslint-suppressions.json` records no reason ([suppressions](https://eslint.org/docs/latest/use/suppressions))                                 |

## Notes for a practitioner

Write the rule as a plugin rule with a `meta.docs.url` pointing at a page in your own repository, prove it red with `RuleTester` or with `--rule` and `--no-config-lookup` on the fixture, and register it in the flat config. Set `linterOptions.noInlineConfig` and do not adopt bulk suppressions, because ESLint will switch the inline route off for you but will not require a reason on it. For the project record, the listing and the identifier lookup you need a toolchain on top, which is what ts-qa-ci supplies.
