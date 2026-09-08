---
title: Staticcheck and Defence Before Fix
summary: Fixed catalogue so 4.1 fails; checks flag and -explain meet 4.2 and 6.1 to 6.3 for bundled checks; lint ignore fails 7.1
---

# Staticcheck

**Language**: Go · **Kind**: tool · **Readiness**: 🔴 · **Detector conformance**: 🔴 · **Checked**: 2026-09-08, version 2026.2 (v0.8.0)

Staticcheck is the most widely used standalone Go analyser, a curated set of checks with identifiers such as `SA1019` and `S1039` grouped by prefix into bug finding, simplification, style and quick fixes. In a pipeline it runs directly or, more often, inside golangci-lint. It is a fixed catalogue: the project chooses which checks run and cannot add one.

## How it is conformant

Staticcheck is the best example in this register of section 6 done properly. Every diagnostic is "annotated with the identifier of the specific check that found the issue", and `staticcheck -explain SA1019` prints the check's summary, full explanation, the version it arrived in and a link to the online page, all from the installed binary ([command line](https://staticcheck.dev/docs/running-staticcheck/cli/)), which meets 6.1, 6.2 and 6.3 for the bundled checks and gives them stable, printed identifiers under 4.3. Because 4.1 fails, 4.2 is graded on the bundled checks, and `staticcheck -checks SA1019 ./fixture` runs one check against supplied code with the rest silent, which is a usable harness (4.2). It accepts the same package patterns as `go build`, runs locally with no infrastructure and prints findings in its own output (5.1, 5.2, 5.3, 5.4). The `//lint:ignore Check reason` directive requires its reason: the documentation states that "the reason is a required field" ([configuration](https://staticcheck.dev/docs/configuration/)), which meets 7.2 as few tools do.

## How it is not conformant

Clause 4.1 is failed: the [configuration](https://staticcheck.dev/docs/configuration/) and [checks](https://staticcheck.dev/docs/checks/) pages describe enabling, disabling and tuning the shipped checks only, and there is no route for a consuming project to add one, so 4.4 does not apply. Clause 7.1 is failed despite the required reason: `//lint:ignore` and `//lint:file-ignore` are inline routes that no flag or setting switches off, and because a project cannot write a check in Staticcheck it cannot detect them there either; the only documented behaviour is a warning when a directive matches nothing, which does not show the ones that do. No release gate over the generated explanations is documented (6.4, not verified).

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                      |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | No           | [Configuration](https://staticcheck.dev/docs/configuration/) offers selection only                            |
| Detector | 4.2    | Yes          | Bundled checks: `-checks <id>` on a package ([CLI](https://staticcheck.dev/docs/running-staticcheck/cli/))    |
| Detector | 4.3    | Yes          | Bundled ids printed with every finding ([CLI](https://staticcheck.dev/docs/running-staticcheck/cli/))         |
| Detector | 4.4    | No           | None                                                                                                          |
| Detector | 5.1    | Yes          | `staticcheck ./...` locally                                                                                   |
| Detector | 5.2    | Yes          | `go build` package patterns                                                                                   |
| Detector | 5.3    | Yes          | Findings printed to stdout                                                                                    |
| Detector | 5.4    | Yes          | Every check runnable locally                                                                                  |
| Detector | 6.1    | Yes          | `staticcheck -explain <id>`                                                                                   |
| Detector | 6.2    | Yes          | Works offline from the binary                                                                                 |
| Detector | 6.3    | Yes          | Explanation ships with the check                                                                              |
| Detector | 6.4    | Not verified | Explanations are generated from check source; no release gate documented                                      |
| Detector | 7.1    | No           | `//lint:ignore` cannot be disabled or detected ([configuration](https://staticcheck.dev/docs/configuration/)) |
| Detector | 7.2    | Yes          | Reason is a required field on `//lint:ignore`                                                                 |

## Notes for a practitioner

Use Staticcheck for the hazards it already names, and use `-explain` as the model of what a resolver should look like when building your own. For a bespoke class, write a `go/analysis` analyzer and run it through `go vet -vettool` or a golangci-lint module plugin, and have that analyzer or review policy forbid `//lint:ignore`, since Staticcheck can neither switch it off nor report it.
