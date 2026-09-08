---
title: typescript-eslint and Defence Before Fix
summary: RuleCreator and RuleTester give 4.1, 4.2 and 4.3; fails 8.3 because eslint-disable is undefended, 6.2 and 11.1 absent
---

# typescript-eslint

**Language**: JavaScript and TypeScript · **Kind**: tool · **Readiness**: 🟢 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 8.70.0

typescript-eslint is the parser, rule set and rule-authoring kit that lets ESLint understand TypeScript and, with type information, reason about it. It is a plugin rather than a toolchain, so it inherits ESLint's mechanisms for everything outside rule authoring, and its conformance grade is ESLint's. Its readiness grade is its own, because it is the best place in the ecosystem to write a bespoke type-aware defence.

## How it is conformant

`RuleCreator` from `@typescript-eslint/utils` is a factory that takes a function mapping a rule name to its documentation URL, so every rule built with it carries a `meta.docs.url` by construction; the documentation discourages `RuleCreator.withoutDocs` and tells authors to "include a descriptive error message and link to informative documentation" ([custom rules](https://typescript-eslint.io/developers/custom-rules)). That is clauses 4.1, 4.3 and the shipping half of 6.3 done in one factory. The `RuleTester` from `@typescript-eslint/rule-tester` runs a single rule against supplied code, with `projectService` for type-aware rules, which is the clause 4.2 harness. The `ban-ts-comment` rule defends against the compiler's own suppression route, and its `allow-with-description`, `minimumDescriptionLength` and `descriptionFormat` options let a project require a justification of a given shape ([ban-ts-comment](https://typescript-eslint.io/rules/ban-ts-comment/)). Findings are printed by ESLint with the `@typescript-eslint/rule-name` identifier.

## How it is not conformant

It does not defend against ESLint's own suppression route: `eslint-disable` comments and bulk suppressions remain available and no typescript-eslint rule bans them, so clause 8.3 fails as it does for ESLint. The `RuleCreator` URL is a URL, and the bundled rules' pages live on typescript-eslint.io rather than in the installed package, so 6.1 resolves only over the network and 6.2 fails. There is no listing under section 7 beyond ESLint's `--print-config`, no project record under section 8 and no declaration under 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                                                                                       |
| ------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | `RuleCreator` for bespoke rules, including type-aware ones ([custom rules](https://typescript-eslint.io/developers/custom-rules))                              |
| 4.2    | Yes          | `@typescript-eslint/rule-tester` ([custom rules](https://typescript-eslint.io/developers/custom-rules))                                                        |
| 4.3    | Yes          | Rule name chosen by the author, printed by ESLint                                                                                                              |
| 4.4    | Partial      | `RuleCreator` requires a docs URL by its signature; nothing checks the page exists                                                                             |
| 5.1    | Yes          | Runs through ESLint locally                                                                                                                                    |
| 5.2    | Yes          | Single file through ESLint                                                                                                                                     |
| 5.3    | Yes          | Findings are the command's output                                                                                                                              |
| 5.4    | Yes          | Same rules everywhere                                                                                                                                          |
| 6.1    | Partial      | Every rule carries a URL; no command resolves a printed identifier                                                                                             |
| 6.2    | No           | Bundled rule documentation is on the website                                                                                                                   |
| 6.3    | Partial      | Docs versioned with the release, not shipped in the package                                                                                                    |
| 7.1    | Partial      | ESLint `--print-config` only                                                                                                                                   |
| 7.2    | Yes          | Derived from the resolved configuration                                                                                                                        |
| 7.3    | Yes          | Project plugin rules appear alongside                                                                                                                          |
| 8.1    | No           | No project record                                                                                                                                              |
| 8.2    | Partial      | `ban-ts-comment` can require a described reason of a given format for `@ts-` directives ([ban-ts-comment](https://typescript-eslint.io/rules/ban-ts-comment/)) |
| 8.3    | No           | `eslint-disable` remains undefended                                                                                                                            |
| 8.4    | No           | No listing of exceptions                                                                                                                                       |
| 8.5    | Partial      | `recommended` and `strict` configs state defaults for rules                                                                                                    |
| 9.1    | No           | No agent summary                                                                                                                                               |
| 9.2    | No           | No delivery mechanism                                                                                                                                          |
| 10.1   | Not verified | The project generates its rule docs from rule metadata; whether a missing page blocks a release is not documented                                              |
| 10.2   | Not verified | Not documented                                                                                                                                                 |
| 11.1   | No           | No declaration                                                                                                                                                 |

## Notes for a practitioner

Build the bespoke rule with `RuleCreator` pointing at a documentation page in your own repository, prove it red with the typescript-eslint `RuleTester`, and turn on `ban-ts-comment` with `descriptionFormat` so that any remaining compiler suppression states its reason. Everything else the method needs, the record, the listing and the lookup, has to come from the toolchain around it.
