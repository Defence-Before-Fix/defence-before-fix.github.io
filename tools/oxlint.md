---
title: oxlint and Defence Before Fix
summary: JS plugins are documented as alpha, so 4.1 is partial; fails 8.3 on oxlint-disable directives, 6.1 and 6.2 absent for bespoke rules
---

# oxlint

**Language**: JavaScript and TypeScript · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 1.82.0

oxlint is the Rust linter from the Oxc project. It ships several hundred built-in rules ported from ESLint and its plugin ecosystem and runs them fast enough to sit in front of everything else in a pipeline as a pre-filter. Since March 2026 it can also load JavaScript plugins written against an ESLint-compatible API, which is the route by which a project's own defences reach it.

## How it is conformant

Bespoke rules are possible through the JS plugin mechanism: a plugin is registered under the `jsPlugins` key of `.oxlintrc.json`, and its rules are configured and printed as `plugin-name/rule-name` ([JS plugins](https://oxc.rs/docs/guide/usage/linter/js-plugins)), which satisfies the identifier requirement of clause 4.3. The command line takes a single file as a positional argument, and `-A all -D <rule>` accumulates from left to right so that one rule can be run alone ([CLI](https://oxc.rs/docs/guide/usage/linter/cli.html)); together those give a workable harness for clause 4.2 and satisfy 5.1 and 5.2. `--rules` lists every registered rule, and the plugin's `meta.docs` travels with the plugin.

## How it is not conformant

The documentation states that JS plugins "are currently in alpha, and remain under active development", and that type-aware rules and custom parsers are not supported ([JS plugins](https://oxc.rs/docs/guide/usage/linter/js-plugins)). That is why readiness is amber rather than green: the route exists but a practitioner cannot yet rely on it for every class of defence. Clause 8.3 fails structurally, because `oxlint-disable`, `oxlint-disable-line` and `oxlint-disable-next-line` are supported inline directives and the JS plugin page lists "inline disable directives" as a supported feature; nothing bundled bans them, and `--report-unused-disable-directives` reports only the unused ones ([CLI](https://oxc.rs/docs/guide/usage/linter/cli.html)). There is no project record, no justification requirement, no listing that includes descriptions and documentation routes, no offline resolution of a printed identifier and no declaration under 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                                                                             |
| ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Partial      | JS plugins are supported but in alpha ([JS plugins](https://oxc.rs/docs/guide/usage/linter/js-plugins))                                              |
| 4.2    | Partial      | `-A all -D <rule> <file>` runs one rule on one file; no rule tester of its own ([CLI](https://oxc.rs/docs/guide/usage/linter/cli.html))              |
| 4.3    | Yes          | `plugin-name/rule-name` printed with each finding ([JS plugins](https://oxc.rs/docs/guide/usage/linter/js-plugins))                                  |
| 4.4    | No           | No rule over the rules                                                                                                                               |
| 5.1    | Yes          | Single binary, runs locally                                                                                                                          |
| 5.2    | Yes          | Positional path argument ([CLI](https://oxc.rs/docs/guide/usage/linter/cli.html))                                                                    |
| 5.3    | Yes          | Findings are the command's output                                                                                                                    |
| 5.4    | Yes          | Same rules everywhere                                                                                                                                |
| 6.1    | Partial      | Built-in rules link to oxc.rs pages; no lookup for a bespoke identifier                                                                              |
| 6.2    | No           | Built-in documentation is on the website                                                                                                             |
| 6.3    | Partial      | Built-in docs are versioned with the release, not shipped in it                                                                                      |
| 7.1    | Partial      | `--rules` lists registered rules, not the active configuration with descriptions and routes ([CLI](https://oxc.rs/docs/guide/usage/linter/cli.html)) |
| 7.2    | Partial      | `--rules` is derived from the binary, not from the project's resolved configuration                                                                  |
| 7.3    | Not verified | Whether `--rules` includes JS plugin rules is not documented                                                                                         |
| 8.1    | No           | No project record                                                                                                                                    |
| 8.2    | No           | No justification mechanism                                                                                                                           |
| 8.3    | No           | `oxlint-disable` directives are built in and undefended ([CLI](https://oxc.rs/docs/guide/usage/linter/cli.html))                                     |
| 8.4    | No           | No listing of exceptions                                                                                                                             |
| 8.5    | Partial      | Default rule categories are documented                                                                                                               |
| 9.1    | No           | No agent summary                                                                                                                                     |
| 9.2    | No           | No delivery mechanism                                                                                                                                |
| 10.1   | Not verified | Not documented                                                                                                                                       |
| 10.2   | Not verified | Not documented                                                                                                                                       |
| 11.1   | No           | No declaration                                                                                                                                       |

## Notes for a practitioner

Use oxlint as the fast pre-filter and keep the bespoke defence in an ESLint plugin, which oxlint can then load through `jsPlugins` once the alpha limitations stop mattering for your rule. Ban the `oxlint-disable` family with a rule of your own, because the defence otherwise has an escape hatch nobody reviews; ts-qa-ci's `no-eslint-disable` covers those forms already.
