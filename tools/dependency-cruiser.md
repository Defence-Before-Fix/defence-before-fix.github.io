---
title: dependency-cruiser and Defence Before Fix
summary: Named rules with comments meet 4.1, 4.3 and section 6; the baseline is opt-in so 7.1 holds; 4.2 needs a one-rule config workaround
---

# dependency-cruiser

**Language**: JavaScript and TypeScript · **Kind**: tool · **Readiness**: 🟡 · **Detector conformance**: 🟡 · **Checked**: 2026-09-08, version 18.2.0

dependency-cruiser validates the import graph of a JavaScript or TypeScript project against rules the project writes itself: which modules may depend on which, what must not be circular, what must not be orphaned. It is the natural home for architectural defences that a per-file linter cannot see, and in a pipeline it runs after linting as the structural check.

## How it is conformant

Bespoke rules are the entire product. A `forbidden` rule in `.dependency-cruiser.js` carries a `name`, described as an ESLint-style short identifier, a `comment` for the reasoning and a `severity`, and the reporters print the rule name with each violation ([rules reference](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md)). That gives clauses 4.1 and 4.3, since the name is chosen once by the author and printed unaltered. It runs locally, a file path on the command line cruises from that file, and findings are the command's output with nothing held back for a service, so clauses 5.1 to 5.4 hold ([CLI](https://github.com/sverweij/dependency-cruiser/blob/main/doc/cli.md)). Section 6 holds because there is no bundled catalogue to resolve: `--init` writes its starter rules into the project's own configuration with a `comment` on each, so every rule dependency-cruiser runs is the project's, its documentation sits beside its `name` in one file on disk, and the identifier is printed unaltered, which is all clause 6.1 asks of a detector for a project's own rule. Clause 7.1 holds because the only suppression route, the known-violations baseline, is opt-in: it is written by `--baseline` and read only when `--ignore-known` or the matching option is given ([CLI](https://github.com/sverweij/dependency-cruiser/blob/main/doc/cli.md)), so a project that never enables it has disabled it.

## How it is not conformant

The clause 4.2 harness needs a workaround: there is no flag to run one named rule, so a practitioner points `--config` at a configuration containing only the rule under test, or filters the output. The detector supplies `--config` but leaves the project to build the one-rule configuration, which is the condition the specification's governing principle names, so 4.2 is partial and readiness is amber for the same reason. Clause 7.2 fails: `--baseline` writes every current violation to `.dependency-cruiser-known-violations.json` and `--ignore-known` lowers each to severity ignore, with no justification per entry. Clause 4.4 fails because a rule without a `name` is accepted and prints `unnamed`, and the `allowed` section's rules carry no `name` at all, so an allowed-list violation prints `not-in-allowed` for every rule alike.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                               |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Detector | 4.1    | Yes          | Rules are written by the project ([rules reference](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md))                  |
| Detector | 4.2    | Partial      | No single-rule flag; a one-rule config via `--config` is the workaround ([CLI](https://github.com/sverweij/dependency-cruiser/blob/main/doc/cli.md))   |
| Detector | 4.3    | Yes          | `name` chosen by the author and printed by reporters; unnamed rules print `unnamed`                                                                    |
| Detector | 4.4    | No           | A rule without a `name` is accepted                                                                                                                    |
| Detector | 5.1    | Yes          | `npx depcruise` runs locally                                                                                                                           |
| Detector | 5.2    | Yes          | A file path cruises from that file                                                                                                                     |
| Detector | 5.3    | Yes          | Findings are the command's output                                                                                                                      |
| Detector | 5.4    | Yes          | Same rules everywhere                                                                                                                                  |
| Detector | 6.1    | Yes          | No bundled rules; a project rule's `name` is printed unaltered and its `comment` sits beside it                                                        |
| Detector | 6.2    | Yes          | The config, and the `comment` in it, are on disk                                                                                                       |
| Detector | 6.3    | Yes          | Rule and comment are one object in one file; `--init` starter rules become the project's                                                               |
| Detector | 6.4    | Not verified | Not documented                                                                                                                                         |
| Detector | 7.1    | Yes          | The known-violations baseline is read only when `--ignore-known` is given ([CLI](https://github.com/sverweij/dependency-cruiser/blob/main/doc/cli.md)) |
| Detector | 7.2    | No           | No justification per baseline entry                                                                                                                    |

## Notes for a practitioner

Give every rule a `name` and a `comment` that says what it forbids and why, and prove it red by cruising a fixture with a configuration that contains only that rule. Do not use `--baseline`; where an exception is genuine, express it as a `pathNot` on the rule itself so the exception and its reason live next to the rule.
