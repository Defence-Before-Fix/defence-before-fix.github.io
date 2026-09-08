---
title: Staticcheck and Defence Before Fix
summary: Fixed catalogue so 4.1 fails; -explain resolves offline for 6.1 and 6.2; fails 8.3 on lint ignore comments
---

# Staticcheck

**Language**: Go · **Kind**: tool · **Readiness**: 🔴 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 2026.2 (v0.8.0)

Staticcheck is the most widely used standalone Go analyser, a curated set of checks with identifiers such as `SA1019` and `S1039` grouped by prefix into bug finding, simplification, style and quick fixes. In a pipeline it runs directly or, more often, inside golangci-lint. It is a fixed catalogue: the project chooses which checks run and cannot add one.

## How it is conformant

Staticcheck is the best example in this register of clause 6 done properly. Every diagnostic is "annotated with the identifier of the specific check that found the issue", and `staticcheck -explain SA1019` prints the check's summary, full explanation, the version it arrived in and a link to the online page, all from the installed binary ([command line](https://staticcheck.dev/docs/running-staticcheck/cli/)), which meets 6.1, 6.2 and 6.3 for the bundled checks and gives them stable identifiers under 4.3. It accepts the same package patterns as `go build`, runs locally with no infrastructure and prints findings in its own output (5.1, 5.2, 5.3, 5.4). The `checks` setting in `staticcheck.conf` is a project record the tool reads ([configuration](https://staticcheck.dev/docs/configuration/)), with documented defaults (8.1 partial, 8.5). The `//lint:ignore Check reason` directive requires its reason: the documentation states that "the reason is a required field", which is more than most tools ask.

## How it is not conformant

Clause 4.1 is failed: the [configuration](https://staticcheck.dev/docs/configuration/) and [checks](https://staticcheck.dev/docs/checks/) pages describe enabling, disabling and tuning the shipped checks only, and there is no route for a consuming project to add one, so 4.2 and 4.4 do not apply. Clause 8.3 is failed despite the required reason, because `//lint:ignore` and `//lint:file-ignore` are inline comments that bypass any record, and nothing defends against them. The `checks` list in `staticcheck.conf` records which checks are off but not why (8.2), and nothing lists active checks with their statements alongside those exclusions (7.1, 8.4). No version is declared (11.1).

## Clause by clause

| Clause | Result       | Evidence                                                                                              |
| ------ | ------------ | ----------------------------------------------------------------------------------------------------- |
| 4.1    | No           | [Configuration](https://staticcheck.dev/docs/configuration/) offers selection only                    |
| 4.2    | No           | Not applicable                                                                                        |
| 4.3    | Yes          | Bundled ids printed with every finding ([CLI](https://staticcheck.dev/docs/running-staticcheck/cli/)) |
| 4.4    | No           | None                                                                                                  |
| 5.1    | Yes          | `staticcheck ./...` locally                                                                           |
| 5.2    | Yes          | `go build` package patterns                                                                           |
| 5.3    | Yes          | Findings printed to stdout                                                                            |
| 5.4    | Yes          | `-checks` selects a subset                                                                            |
| 6.1    | Yes          | `staticcheck -explain <id>`                                                                           |
| 6.2    | Yes          | Works offline from the binary                                                                         |
| 6.3    | Yes          | Explanation ships with the check                                                                      |
| 7.1    | No           | No listing of active checks with statements                                                           |
| 7.2    | No           | See 7.1                                                                                               |
| 7.3    | No           | No project checks exist                                                                               |
| 8.1    | Partial      | `staticcheck.conf` read, without justification                                                        |
| 8.2    | No           | No reason on `checks` exclusions                                                                      |
| 8.3    | No           | `//lint:ignore` inline, reason required but unrecorded                                                |
| 8.4    | No           | None                                                                                                  |
| 8.5    | Yes          | Default `checks` value documented                                                                     |
| 9.1    | No           | None                                                                                                  |
| 9.2    | No           | None                                                                                                  |
| 10.1   | Not verified | Explanations are generated from check source; no release gate documented                              |
| 10.2   | Not verified | Not documented                                                                                        |
| 11.1   | No           | No declaration                                                                                        |

## Notes for a practitioner

Use Staticcheck for the hazards it already names, and use `-explain` as the model of what a resolver should look like when building your own. For a bespoke class, write a `go/analysis` analyzer and run it through `go vet -vettool` or a golangci-lint module plugin, and ban `//lint:ignore` in review so the required reason ends up in a configuration file the team can see.
