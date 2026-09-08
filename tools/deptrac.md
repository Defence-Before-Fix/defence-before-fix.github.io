---
title: Deptrac and Defence Before Fix
summary: Custom collectors and violation subscribers meet 4.1; no single-file run fails 5.2, layer names only partly meet 4.3, nothing resolves them for section 6.
---

# Deptrac

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Detector conformance**: 🔴 · **Checked**: 2026-09-08, version 4.7.1

Deptrac is a dependency analyser: it assigns classes to layers with collectors and fails when a layer depends on one the ruleset does not allow. In a pipeline it enforces architecture rather than code style, and a defence hosted in it is a rule about which layers may know about which.

## How it is conformant

Clause 4.1 is met in two ways. A project can write a collector implementing `CollectorInterface`, and Deptrac loads it as soon as the configuration references an unknown collector type ([collectors](https://deptrac.github.io/deptrac/collectors/)); and an event subscriber implementing `ViolationCreatingInterface` can create violations of its own, with a rule name and description the interface exists to expose ([extending Deptrac](https://deptrac.github.io/deptrac/extending_deptrac/)). Clause 4.3 is met in part, since the console formatter names both layers on every violation, and layer names are chosen by the project in its configuration rather than derived from a class ([formatters](https://deptrac.github.io/deptrac/formatters/)). Clauses 5.1, 5.3 and 5.4 hold: `deptrac analyse` runs locally with no CI-only mode and prints its findings to the terminal. Clause 7.1 is met: there is no inline suppression, `skip_violations` lives in the configuration where it is visible, and the baseline formatter writes only when asked ([configuration](https://deptrac.github.io/deptrac/configuration/), [formatters](https://deptrac.github.io/deptrac/formatters/)).

## How it is not conformant

Clause 5.2 fails, and it decides the grade: analysis runs over the configured paths, and the only per-file entry point is the experimental `changed-files` command, which reports layers rather than violations ([debugging](https://deptrac.github.io/deptrac/debugging/)). Clause 4.2 is therefore met only by the workaround of a fixture configuration pointing at fixture paths, which is a route the project builds rather than one the detector provides. Clause 4.3 is only partly met because a layer pair names the rule that was broken rather than an identifier the author chose for it, and a bespoke violation from a subscriber has no separate identifier field. Clauses 6.1 to 6.3 fail because no mechanism resolves a layer or rule name to documentation, and the bundled collector documentation is on the website. Clause 7.2 fails because a `skip_violations` entry is a pair of class names and nothing more, and the baseline formatter writes one for every current violation with no justification. Clause 4.4 has nothing to enforce, and clause 6.4 was not verified.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                 |
| -------- | ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Yes          | Custom collectors and violation-creating subscribers, [extending Deptrac](https://deptrac.github.io/deptrac/extending_deptrac/)          |
| Detector | 4.2    | Partial      | Fixture configuration only; no single-rule harness                                                                                       |
| Detector | 4.3    | Partial      | Layer names are project-chosen and printed; no identifier field on a rule, [formatters](https://deptrac.github.io/deptrac/formatters/)   |
| Detector | 4.4    | No           | Nothing to enforce                                                                                                                       |
| Detector | 5.1    | Yes          | `deptrac analyse` runs locally                                                                                                           |
| Detector | 5.2    | No           | Only `changed-files`, experimental, [debugging](https://deptrac.github.io/deptrac/debugging/)                                            |
| Detector | 5.3    | Yes          | Console formatter to the terminal                                                                                                        |
| Detector | 5.4    | Yes          | No CI-only mode                                                                                                                          |
| Detector | 6.1    | No           | No resolver                                                                                                                              |
| Detector | 6.2    | No           | Documentation on the website                                                                                                             |
| Detector | 6.3    | No           | Same                                                                                                                                     |
| Detector | 6.4    | Not verified | Not found                                                                                                                                |
| Detector | 7.1    | Yes          | No inline route; `skip_violations` and the baseline are configuration, [configuration](https://deptrac.github.io/deptrac/configuration/) |
| Detector | 7.2    | No           | No reason on a skipped violation; baseline formatter writes none, [formatters](https://deptrac.github.io/deptrac/formatters/)            |

## Notes for a practitioner

Name layers as if they were identifiers and document each one in the repository under that name. Prove a new ruleset entry with a fixture configuration whose paths contain a deliberate violation, and keep every `skip_violations` entry with a comment above it, never generated by the baseline formatter.
