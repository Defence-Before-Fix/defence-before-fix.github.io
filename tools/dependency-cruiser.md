---
title: dependency-cruiser and Defence Before Fix
summary: Named rules with comments give 4.1 and 4.3; 4.2 needs a one-rule config workaround; fails 8.3 on the justification-free known-violations baseline
---

# dependency-cruiser

**Language**: JavaScript and TypeScript · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 18.2.0

dependency-cruiser validates the import graph of a JavaScript or TypeScript project against rules the project writes itself: which modules may depend on which, what must not be circular, what must not be orphaned. It is the natural home for architectural defences that a per-file linter cannot see, and in a pipeline it runs after linting as the structural check.

## How it is conformant

Bespoke rules are the entire product. A `forbidden` rule in `.dependency-cruiser.js` carries a `name`, described as an ESLint-style short identifier, a `comment` for the reasoning and a `severity`, and the reporters print the rule name with each violation ([rules reference](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md)). That gives clauses 4.1 and 4.3, and the `comment` field beside the `name` is a form of documentation that travels with the rule. It runs locally, and a file path on the command line cruises from that file, so a subset run is available ([CLI](https://github.com/sverweij/dependency-cruiser/blob/main/doc/cli.md)).

## How it is not conformant

The red proof under 4.2 needs a workaround: there is no flag to run one named rule, so a practitioner points `--config` at a configuration containing only the rule under test, or filters the output. Readiness is amber for that reason. Clause 8.3 fails structurally through the baseline: `--baseline` writes every current violation to `.dependency-cruiser-known-violations.json` and `--ignore-known` lowers each to severity ignore, with no justification per entry ([CLI](https://github.com/sverweij/dependency-cruiser/blob/main/doc/cli.md)). That is exactly the silent baseline clause 8.3 names. The `allowed` section defaults to warn and its rules carry no `name`, so an allowed-list violation prints `not-in-allowed` for every rule alike. There is no command that resolves a printed rule name to its `comment`, no listing of active rules, and no declaration under 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                                                                             |
| ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | Rules are written by the project ([rules reference](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md))                |
| 4.2    | Partial      | No single-rule flag; a one-rule config via `--config` is the workaround ([CLI](https://github.com/sverweij/dependency-cruiser/blob/main/doc/cli.md)) |
| 4.3    | Yes          | `name` chosen by the author and printed by reporters; unnamed rules print `unnamed`                                                                  |
| 4.4    | No           | A rule without a `name` is accepted                                                                                                                  |
| 5.1    | Yes          | `npx depcruise` runs locally                                                                                                                         |
| 5.2    | Yes          | A file path cruises from that file                                                                                                                   |
| 5.3    | Yes          | Findings are the command's output                                                                                                                    |
| 5.4    | Yes          | Same rules everywhere                                                                                                                                |
| 6.1    | Partial      | The `comment` sits beside the `name` in the config, but no command resolves a printed name                                                           |
| 6.2    | Yes          | The config, and the `comment` in it, are on disk                                                                                                     |
| 6.3    | Yes          | Rule and comment are one object in one file                                                                                                          |
| 7.1    | No           | No listing command; the config file is the only source                                                                                               |
| 7.2    | No           | Same                                                                                                                                                 |
| 7.3    | No           | Same                                                                                                                                                 |
| 8.1    | No           | The known-violations file is read by the tool but records no decisions, only locations                                                               |
| 8.2    | No           | No justification per baseline entry ([CLI](https://github.com/sverweij/dependency-cruiser/blob/main/doc/cli.md))                                     |
| 8.3    | No           | `--baseline` and `--ignore-known` are a silent baseline                                                                                              |
| 8.4    | No           | No listing                                                                                                                                           |
| 8.5    | Partial      | `depcruise --init` writes a documented default rule set                                                                                              |
| 9.1    | No           | No agent summary                                                                                                                                     |
| 9.2    | No           | No delivery mechanism                                                                                                                                |
| 10.1   | Not verified | Not documented                                                                                                                                       |
| 10.2   | Not verified | Not documented                                                                                                                                       |
| 11.1   | No           | No declaration                                                                                                                                       |

## Notes for a practitioner

Give every rule a `name` and a `comment` that says what it forbids and why, and prove it red by cruising a fixture with a configuration that contains only that rule. Do not use `--baseline`; where an exception is genuine, express it as a `pathNot` on the rule itself so the exception and its reason live next to the rule.
