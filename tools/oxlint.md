---
title: oxlint and Defence Before Fix
summary: JS plugins are alpha so 4.1 is partial; built-in documentation is online only, failing 6.2 and 6.3; oxlint-disable cannot be switched off, failing 7.1
---

# oxlint

**Language**: JavaScript and TypeScript · **Kind**: tool · **Readiness**: 🟡 · **Detector conformance**: 🟡 · **Checked**: 2026-09-08, version 1.82.0

oxlint is the Rust linter from the Oxc project. It ships several hundred built-in rules ported from ESLint and its plugin ecosystem and runs them fast enough to sit in front of everything else in a pipeline as a pre-filter. Since March 2026 it can also load JavaScript plugins written against an ESLint-compatible API, which is the route by which a project's own defences reach it.

## How it is conformant

Bespoke rules are possible through the JS plugin mechanism: a plugin is registered under the `jsPlugins` key of `.oxlintrc.json`, and its rules are configured and printed as `plugin-name/rule-name` ([JS plugins](https://oxc.rs/docs/guide/usage/linter/js-plugins)). The prefix is a namespace the author assigns in the plugin, not something derived from the file's location, so clause 4.3 holds. The command line takes a single file as a positional argument, and `-A all -D <rule>` accumulates from left to right so that one rule can be run alone ([CLI](https://oxc.rs/docs/guide/usage/linter/cli.html)); that is a workable clause 4.2 harness and satisfies 5.1 and 5.2. Findings are the command's own output and nothing is reserved for a hosted mode, meeting 5.3 and 5.4. Built-in rules link to their pages on oxc.rs by identifier, which is a clause 6.1 lookup for the bundled catalogue.

## How it is not conformant

The documentation states that JS plugins "are currently in alpha, and remain under active development", and that type-aware rules and custom parsers are not supported ([JS plugins](https://oxc.rs/docs/guide/usage/linter/js-plugins)). Clause 4.1 is therefore only partly met, and readiness is amber for the same reason: the route exists but a practitioner cannot yet rely on it for every class of defence. Clauses 6.2 and 6.3 fail because the built-in rules' documentation lives on the website and does not ship in the binary. Clause 7.1 fails: `oxlint-disable`, `oxlint-disable-line` and `oxlint-disable-next-line` are built-in directives, no option switches them off, and `--report-unused-disable-directives` reports only the directives that had no effect ([CLI](https://oxc.rs/docs/guide/usage/linter/cli.html)); the documentation describes no mechanical check that sees the others. Clause 7.2 fails with it, since a directive needs no reason.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                                                   |
| -------- | ------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Partial      | JS plugins are supported but in alpha ([JS plugins](https://oxc.rs/docs/guide/usage/linter/js-plugins))                                                                    |
| Detector | 4.2    | Partial      | `-A all -D <rule> <file>` runs one rule on one file; not verified for a plugin rule and no rule tester of its own ([CLI](https://oxc.rs/docs/guide/usage/linter/cli.html)) |
| Detector | 4.3    | Yes          | `plugin-name/rule-name` under an assigned namespace, printed with each finding ([JS plugins](https://oxc.rs/docs/guide/usage/linter/js-plugins))                           |
| Detector | 4.4    | No           | No rule over the rules                                                                                                                                                     |
| Detector | 5.1    | Yes          | Single binary, runs locally                                                                                                                                                |
| Detector | 5.2    | Yes          | Positional path argument ([CLI](https://oxc.rs/docs/guide/usage/linter/cli.html))                                                                                          |
| Detector | 5.3    | Yes          | Findings are the command's output                                                                                                                                          |
| Detector | 5.4    | Yes          | Same rules everywhere                                                                                                                                                      |
| Detector | 6.1    | Yes          | Built-in rules link to oxc.rs pages by identifier; a bespoke identifier is printed unaltered                                                                               |
| Detector | 6.2    | No           | Built-in documentation is on the website                                                                                                                                   |
| Detector | 6.3    | No           | Built-in docs are versioned with the release, not shipped in it                                                                                                            |
| Detector | 6.4    | Not verified | Not documented                                                                                                                                                             |
| Detector | 7.1    | No           | `oxlint-disable` directives cannot be disabled; only unused ones are reported ([CLI](https://oxc.rs/docs/guide/usage/linter/cli.html))                                     |
| Detector | 7.2    | No           | No reason required on a directive                                                                                                                                          |

## Notes for a practitioner

Use oxlint as the fast pre-filter and keep the bespoke defence in an ESLint plugin, which oxlint can then load through `jsPlugins` once the alpha limitations stop mattering for your rule. Ban the `oxlint-disable` family with a rule of your own, because the defence otherwise has an escape hatch nobody reviews; ts-qa-ci's `no-eslint-disable` covers those forms already.
