---
title: Deptrac and Defence Before Fix
summary: Custom collectors and violation subscribers with project-named layers; fails 5.2 on single files, 8.3 on the baseline formatter, 8.2 on reasons.
---

# Deptrac

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 4.7.1

Deptrac is a dependency analyser: it assigns classes to layers with collectors and fails when a layer depends on one the ruleset does not allow. In a pipeline it enforces architecture rather than code style, and a defence hosted in it is a rule about which layers may know about which.

## How it is conformant

Clause 4.1 is met in two ways. A project can write a collector implementing `CollectorInterface`, and Deptrac loads it as soon as the configuration references an unknown collector type ([collectors](https://deptrac.github.io/deptrac/collectors/)); and an event subscriber implementing `ViolationCreatingInterface` can create violations of its own, with a rule name and description the interface exists to expose ([extending Deptrac](https://deptrac.github.io/deptrac/extending_deptrac/)). Clause 4.3 is met in part, since the console formatter names both layers on every violation, and layer names are chosen by the project in its configuration rather than derived from a class ([formatters](https://deptrac.github.io/deptrac/formatters/)). Clauses 5.1 and 5.3 hold: `deptrac analyse` runs locally and prints its findings. `skip_violations` is a record the tool reads itself, which is clause 8.1's shape ([configuration](https://deptrac.github.io/deptrac/configuration/)).

## How it is not conformant

Clause 5.2 fails: analysis runs over the configured paths, and the only per-file entry point is the experimental `changed-files` command, which reports layers rather than violations ([debugging](https://deptrac.github.io/deptrac/debugging/)). Clause 4.2 is therefore met only by the workaround of a fixture configuration pointing at fixture paths. Clause 8.3 fails structurally: the baseline formatter writes a `skip_violations` block for every current violation with no justification ([formatters](https://deptrac.github.io/deptrac/formatters/)), and clause 8.2 fails because a `skip_violations` entry is a pair of class names and nothing more. Clause 6.1 fails because no mechanism resolves a layer or rule name to documentation. Clause 7.1 is met in part by the `debug:layer` and `debug:dependencies` commands, which are derived from the configuration, but they list layers and tokens rather than rules with what each forbids. There is no declaration under clause 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                                                        |
| ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | Custom collectors and violation-creating subscribers, [extending Deptrac](https://deptrac.github.io/deptrac/extending_deptrac/) |
| 4.2    | Partial      | Fixture configuration only; no single-rule harness                                                                              |
| 4.3    | Partial      | Layer names are project-chosen and printed, [formatters](https://deptrac.github.io/deptrac/formatters/)                         |
| 4.4    | No           | Nothing to enforce                                                                                                              |
| 5.1    | Yes          | `deptrac analyse` runs locally                                                                                                  |
| 5.2    | No           | Only `changed-files`, experimental, [debugging](https://deptrac.github.io/deptrac/debugging/)                                   |
| 5.3    | Yes          | Console formatter to the terminal                                                                                               |
| 5.4    | Yes          | No CI-only mode                                                                                                                 |
| 6.1    | No           | No resolver                                                                                                                     |
| 6.2    | No           | Documentation on the website                                                                                                    |
| 6.3    | No           | Same                                                                                                                            |
| 7.1    | Partial      | `debug:layer` lists layer members, not rules, [debugging](https://deptrac.github.io/deptrac/debugging/)                         |
| 7.2    | Yes          | Debug output is derived from the configuration                                                                                  |
| 7.3    | Yes          | All rules are the project's own                                                                                                 |
| 8.1    | Yes          | `skip_violations` is read by the tool, [configuration](https://deptrac.github.io/deptrac/configuration/)                        |
| 8.2    | No           | No reason on a skipped violation                                                                                                |
| 8.3    | No           | Baseline formatter, [formatters](https://deptrac.github.io/deptrac/formatters/)                                                 |
| 8.4    | No           | Skips are not listed with the rules                                                                                             |
| 8.5    | No           | Not documented                                                                                                                  |
| 9.1    | No           | No agent summary                                                                                                                |
| 9.2    | No           | No delivery mechanism                                                                                                           |
| 10.1   | Not verified | Not found                                                                                                                       |
| 10.2   | Not verified | Deptrac analyses itself; coverage not checked                                                                                   |
| 11.1   | No           | No declaration                                                                                                                  |

## Notes for a practitioner

Name layers as if they were identifiers and document each one in the repository under that name. Prove a new ruleset entry with a fixture configuration whose paths contain a deliberate violation, and keep every `skip_violations` entry with a comment above it, never generated by the baseline formatter.
