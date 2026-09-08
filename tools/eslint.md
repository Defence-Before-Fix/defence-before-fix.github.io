---
title: ESLint and Defence Before Fix
summary: Bespoke rules, single-rule run and identifiers all first class; fails 8.3 on inline disables and the bulk suppressions file, 6.2 and 11.1 absent
---

# ESLint

**Language**: JavaScript and TypeScript · **Kind**: tool · **Readiness**: 🟢 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 10.10.0

ESLint is the pluggable linter for JavaScript and TypeScript, and the detector most Defence Before Fix work in this ecosystem is built on. It parses source into an AST, runs every configured rule over it and prints each finding with the rule's identifier. In a pipeline it is the host for bespoke rules; on its own it is a detector rather than a toolchain, and the grading below reflects that.

## How it is conformant

Bespoke rules are the core of the design rather than an afterthought. A rule is a module with `meta` and `create`, registered through a plugin object in the flat config, and `meta.docs` carries both a `description` and a `url` ([custom rules](https://eslint.org/docs/latest/extend/custom-rules)), which is what clauses 4.1 and 4.3 ask for. The identifier printed with every finding is the configured rule name, as the stylish formatter's sample output shows with `no-unused-vars` at the end of each line ([formatters](https://eslint.org/docs/latest/use/formatters/)). The harness for the red proof under clause 4.2 exists twice over: `RuleTester` runs one rule against supplied code without the project's test suite, and on the command line `--rule` combined with `--no-config-lookup` runs only the rules named on a single file or on `--stdin` ([command line interface](https://eslint.org/docs/latest/use/command-line-interface)). Clauses 5.1 and 5.2 are met by that same invocation, and 5.3 by the fact that findings land in the command's own output. Suppression has a partial defence: `linterOptions.noInlineConfig` disables every inline directive and `reportUnusedDisableDirectives` can be set to error ([configuring rules](https://eslint.org/docs/latest/use/configure/rules)).

## How it is not conformant

Clause 8.3 fails structurally. `eslint-disable`, `eslint-disable-line` and `eslint-disable-next-line` are a first-class suppression route, and the description after `--` is optional ([configuring rules](https://eslint.org/docs/latest/use/configure/rules)). Since version 9.24 the bulk suppressions feature adds a second route: `--suppress-all` writes every current violation into `eslint-suppressions.json`, and no justification is recorded for any entry ([bulk suppressions](https://eslint.org/docs/latest/use/suppressions)). That is a silent baseline in the sense clause 8.3 names, and no bundled rule bans either mechanism. Clause 6.1 is met only for core rules, whose identifier maps to a page on eslint.org, and that page is on the network rather than on disk, so 6.2 fails; a bespoke rule's `meta.docs.url` is optional and there is no command that resolves a printed identifier to it. Clause 7.1 has `--print-config`, which prints the resolved configuration for a file, but the output is a rule map without descriptions or documentation routes and is not a listing in the sense required. There is no project record under section 8, no self-audit under 10.1 that applies to a consuming project's rules, and no declaration under 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                                                                |
| ------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | Plugin rules are first class ([custom rules](https://eslint.org/docs/latest/extend/custom-rules))                                       |
| 4.2    | Yes          | `RuleTester`, or `--rule` with `--no-config-lookup` on one file ([CLI](https://eslint.org/docs/latest/use/command-line-interface))      |
| 4.3    | Yes          | Rule name chosen by the author, printed with every finding ([formatters](https://eslint.org/docs/latest/use/formatters/))               |
| 4.4    | No           | No bundled rule checks that rules carry an identifier or documentation                                                                  |
| 5.1    | Yes          | `npx eslint` runs locally with no infrastructure                                                                                        |
| 5.2    | Yes          | Positional file paths and `--stdin` ([CLI](https://eslint.org/docs/latest/use/command-line-interface))                                  |
| 5.3    | Yes          | Findings are the command's output                                                                                                       |
| 5.4    | Yes          | Same rules run in every environment                                                                                                     |
| 6.1    | Partial      | Core identifiers map to eslint.org pages; a bespoke rule's `meta.docs.url` is optional and there is no lookup command                   |
| 6.2    | No           | Core rule documentation is on the website, not in the installed package                                                                 |
| 6.3    | Partial      | Core rule docs are versioned with the release but not shipped in it                                                                     |
| 7.1    | Partial      | `--print-config` prints the rule map without descriptions or routes ([CLI](https://eslint.org/docs/latest/use/command-line-interface))  |
| 7.2    | Yes          | `--print-config` is derived from the resolved configuration                                                                             |
| 7.3    | Yes          | Plugin rules from the project appear in `--print-config` alongside core rules                                                           |
| 8.1    | No           | No project record; the configuration file is the only place decisions can live and it does not distinguish exceptions                   |
| 8.2    | No           | Disable comments and `eslint-suppressions.json` need no justification ([suppressions](https://eslint.org/docs/latest/use/suppressions)) |
| 8.3    | No           | Inline directives and bulk suppressions are built in ([configuring rules](https://eslint.org/docs/latest/use/configure/rules))          |
| 8.4    | No           | No listing of exceptions                                                                                                                |
| 8.5    | Partial      | `eslint:recommended` states defaults for rules only                                                                                     |
| 9.1    | No           | No agent summary                                                                                                                        |
| 9.2    | No           | No delivery mechanism                                                                                                                   |
| 10.1   | Not verified | ESLint's own repository has documentation checks; whether a missing rule page blocks a release is not documented on the site            |
| 10.2   | Not verified | The project lints itself; whether that is a release gate is not documented                                                              |
| 11.1   | No           | No declaration of the method or toolchain version                                                                                       |

## Notes for a practitioner

Write the rule as a plugin rule with a `meta.docs.url` pointing at a page in your own repository, prove it red with `RuleTester` or with `--rule` and `--no-config-lookup` on the fixture, and register it in the flat config. Set `linterOptions.noInlineConfig` and do not adopt bulk suppressions, because ESLint alone will not stop either. For the project record, the listing and the identifier lookup you need a toolchain on top, which is what ts-qa-ci supplies.
