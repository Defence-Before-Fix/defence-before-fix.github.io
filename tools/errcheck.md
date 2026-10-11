---
title: errcheck and Defence Before Fix
summary: One fixed check for unchecked errors fails 4.1, and its findings carry no identifier, failing 4.3 and leaving section 6 nothing to resolve; no inline suppression route, and the built-in exclusions switch off with -excludeonly, so 7.1 holds; v1.20.0 stops under Go 1.27.2 with an internal error and exit 1
language: Go
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-10-10, version v1.20.0
---

# errcheck

{% include tool-grades.html %}

errcheck reports calls whose returned error is neither assigned nor explicitly discarded, "silently ignored errors in Go code" ([README at v1.20.0](https://github.com/kisielk/errcheck/blob/v1.20.0/README.md)). It is one of the oldest Go linters and one of golangci-lint's default set, and most projects run it there; on its own it is the `errcheck` command. It has one check, widened by `-blank` and `-asserts` and narrowed by exclusion lists, and no way to add another, so it cannot host a bespoke defence.

## How it is conformant

The reporting clauses are met. `errcheck` runs locally on packages or on a single file, `errcheck ./b.go`, and prints each finding to the command's own output as the position, a tab and the call, `b.go:6:11: os.Remove("d")`, exiting 1 (ran under Go 1.26.8), which meets 5.1 to 5.4; there is no option that writes the findings elsewhere. Graded on its one check, 4.2 is met: a run over a fixture is that check alone, with nothing else to obscure it and no test suite run (ran).

Clause 7.1 holds. errcheck has no inline suppression route: a call carrying `//nolint:errcheck // reason` was reported like any other (ran), and assigning the error to `_` is a change to the code, which `-blank` reports in turn (ran). The exclusion routes are flags, `-exclude <file>`, `-ignorepkg` and the deprecated `-ignore`, which the project can simply not set. The two exclusions errcheck applies by default, a built-in list of calls such as `(*bytes.Buffer).Write` ([`excludes.go`](https://github.com/kisielk/errcheck/blob/v1.20.0/errcheck/excludes.go)) and the whole `fmt` package, are switched off by the documented `-excludeonly`: a fixture with an unchecked `b.Write` and `fmt.Println` printed nothing by default and both findings with `-excludeonly` (ran). With no inline route, 7.2 is not applicable.

## How it is not conformant

Clause 4.1 fails: the README describes one check and flags that adjust what it reports, and the exported `go/analysis` analyser lets another driver run the same check, not add one. Clause 4.3 fails: a finding is a position and the source of the call, with no identifier of any kind, and plain text is the only format (ran). With nothing printed to key a lookup on, section 6 has nothing to resolve, and 6.1, 6.2 and 6.3 are No.

Three behaviours a defence routed through errcheck should know of. Release v1.20.0 does not run under Go 1.27.2: every run printed `internal error: package "os" without types was imported from "example.com/ec"` and exited 1, the code a finding gets, before checking anything (ran); under Go 1.26.8 the same fixtures ran. The fault is open upstream as [issue 289](https://github.com/kisielk/errcheck/issues/289). Under reading 9, a file that does not parse is reported, `error: failed to check packages: errors while loading package`, and exits 2, apart from a finding (ran). The README says `-verbose` shows "the resulting list of added excludes", but a run with `-exclude` and `-verbose` printed only `checking example.com/ec` (ran), so the run does not report what it excluded.

The detector grade is 🔴 on 4.1 and 4.3, both structural under reading 1, with 6.1, 6.2 and 6.3 failing. Readiness is 🔴: no bespoke rules and no identifier on findings.

## Clause by clause

| Document | Clause | Result         | Evidence                                                                                                                                                                                                                      |
| -------- | ------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | No             | One check with flags that adjust it ([README](https://github.com/kisielk/errcheck/blob/v1.20.0/README.md))                                                                                                                    |
| Detector | 4.2    | Yes            | Bundled check: a run over a fixture is the one check alone (ran)                                                                                                                                                              |
| Detector | 4.3    | No             | A finding is a position and the call; no identifier, text only (ran)                                                                                                                                                          |
| Detector | 4.4    | Not applicable | No rules to enforce an identifier on                                                                                                                                                                                          |
| Detector | 5.1    | Yes            | `errcheck ./...` locally ([README](https://github.com/kisielk/errcheck/blob/v1.20.0/README.md))                                                                                                                               |
| Detector | 5.2    | Yes            | `errcheck ./b.go` (ran)                                                                                                                                                                                                       |
| Detector | 5.3    | Yes            | Findings in the command's output (ran)                                                                                                                                                                                        |
| Detector | 5.4    | Yes            | Same everywhere                                                                                                                                                                                                               |
| Detector | 6.1    | No             | Nothing to resolve                                                                                                                                                                                                            |
| Detector | 6.2    | No             | Same                                                                                                                                                                                                                          |
| Detector | 6.3    | No             | Same                                                                                                                                                                                                                          |
| Detector | 6.4    | Not applicable | No identifiers to document                                                                                                                                                                                                    |
| Detector | 7.1    | Yes            | No inline route; `//nolint:errcheck` ignored (ran); exclusions are opt-in flags, and `-excludeonly` turns off the built-in ones (ran; [`excludes.go`](https://github.com/kisielk/errcheck/blob/v1.20.0/errcheck/excludes.go)) |
| Detector | 7.2    | Not applicable | No inline route to require a reason on                                                                                                                                                                                        |

## Notes for a practitioner

errcheck is an off-the-shelf rule under method clause 3.2 for the class "an error return dropped on the floor", proven by a fixture with one unchecked call. Run it with `-blank` where an error assigned to `_` should need a reason, and with `-excludeonly` plus an exclude file of the project's own where the built-in list and the blanket `fmt` exclusion are not wanted, keeping each entry beside a comment that gives the reason. Pin Go 1.26 for it until a release fixes the Go 1.27.2 failure, and read the output rather than the exit code, since the internal error exits 1 like a finding. Through golangci-lint the same check prints `(errcheck)` after each finding and gains the `//nolint` route; see that page.

## Attributes

| Attribute      | Value                                                                                       | Source                                                                    |
| -------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Kind           | Detector                                                                                    | [README](https://github.com/kisielk/errcheck/blob/v1.20.0/README.md)      |
| Depth          | Semantic: type-checked packages                                                             | ran                                                                       |
| Output formats | Plain text only; no SARIF                                                                   | ran (`-h`)                                                                |
| Exit codes     | 1 on a finding, 2 on a load or parse error and on a usage error; 1 on the Go 1.27.2 failure | ran; [README](https://github.com/kisielk/errcheck/blob/v1.20.0/README.md) |
| Report file    | No                                                                                          | ran (`-h`)                                                                |
| Rule listing   | No; one check                                                                               | ran (`-h`)                                                                |
| Licence        | MIT                                                                                         | [LICENSE](https://github.com/kisielk/errcheck/blob/v1.20.0/LICENSE)       |
