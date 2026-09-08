---
title: golangci-lint and Defence Before Fix
summary: Bespoke analyzers only via custom binary build; analysistest harness passes 4.2; fails 8.3 on nolint and new-from-rev
---

# golangci-lint

**Language**: Go · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version v2.13.2

golangci-lint is the standard aggregator for Go: one binary that runs staticcheck, go vet, errcheck, unused and around a hundred other linters over a shared parse, configured from a single `.golangci.yml`. In a pipeline it is usually the only lint entry point a Go project has, so it is the natural place for a bespoke defence, and it does support one, at the cost of building a custom binary.

## How it is conformant

Bespoke rules are supported through the [module plugin system](https://golangci-lint.run/docs/plugins/module-plugins/): a project writes a `go/analysis` analyzer, lists it in `.custom-gcl.yml`, builds a custom binary with `golangci-lint custom`, and enables it under `linters.settings.custom` with `type: module` (4.1). The analyzer's `Name` is chosen once by its author and is what golangci-lint prints in parentheses after each finding (4.3), and the `go/analysis` framework's `analysistest` package runs a single analyzer against `testdata` with `// want` comments as the red proof ([analysistest](https://pkg.go.dev/golang.org/x/tools/go/analysis/analysistest), 4.2). `golangci-lint run file1.go` runs locally on one file, and `--default=none --enable <name>` runs one linter ([quick start](https://golangci-lint.run/docs/welcome/quick-start/)), meeting 5.1, 5.2 and 5.4, with every finding in the command's own output (5.3). `golangci-lint help linters` lists every linter with its enabled state and description, derived from the configuration (7.1, 7.2 for linters). The `nolintlint` linter's `require-explanation` and `require-specific` settings ([reference configuration](https://github.com/golangci/golangci-lint/blob/main/.golangci.reference.yml)) are a genuine, if optional, defence of the kind clause 8.3 asks for.

## How it is not conformant

Clause 8.3 is failed as shipped: `//nolint` and `//nolint:linter` suppress inline and file-wide with no justification by default ([false positives](https://golangci-lint.run/docs/linters/false-positives/)), `nolintlint` is off unless enabled, and even with `require-explanation` the route is still an inline comment outside any record. The `issues.new-from-rev` and `new-from-merge-base` options are silent baselines. The exclusion rules in `linters.exclusions.rules` are a project record the tool reads (8.1), but they match on message text or path rather than identifier and carry no justification (8.2), and nothing enumerates them beside the active linters (8.4). Readiness is 🟡 rather than 🟢 because the bespoke route requires a custom build rather than a configuration entry, and because the identifier printed is the linter name, so a plugin carrying several rules prints one name for all of them unless it registers each as its own analyzer. Clause 6.1 is partial: `help linters` describes a linter, but findings from wrapped tools print that tool's own code, such as `SA1019`, which golangci-lint does not itself resolve. No version is declared (11.1).

## Clause by clause

| Clause | Result       | Evidence                                                                                                         |
| ------ | ------------ | ---------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | [Module plugins](https://golangci-lint.run/docs/plugins/module-plugins/) via a custom binary                     |
| 4.2    | Yes          | [`analysistest`](https://pkg.go.dev/golang.org/x/tools/go/analysis/analysistest)                                 |
| 4.3    | Partial      | Analyzer name printed; one name per plugin linter                                                                |
| 4.4    | No           | None                                                                                                             |
| 5.1    | Yes          | `golangci-lint run` locally ([quick start](https://golangci-lint.run/docs/welcome/quick-start/))                 |
| 5.2    | Yes          | `golangci-lint run file1.go`                                                                                     |
| 5.3    | Yes          | Findings printed with linter name                                                                                |
| 5.4    | Yes          | `--default=none --enable <name>`                                                                                 |
| 6.1    | Partial      | `help linters` resolves a linter name, not a wrapped tool's code                                                 |
| 6.2    | Partial      | Linter descriptions in the binary; rule docs on the website                                                      |
| 6.3    | Partial      | Custom analyzer `Doc` ships with the analyzer                                                                    |
| 7.1    | Yes          | `golangci-lint help linters`                                                                                     |
| 7.2    | Yes          | Derived from configuration                                                                                       |
| 7.3    | Yes          | Custom linters appear in the same listing                                                                        |
| 8.1    | Partial      | `linters.exclusions.rules` read, without justification                                                           |
| 8.2    | No           | No reason required                                                                                               |
| 8.3    | No           | `//nolint` ([false positives](https://golangci-lint.run/docs/linters/false-positives/)); `new-from-rev` baseline |
| 8.4    | No           | None                                                                                                             |
| 8.5    | Yes          | Default linter set documented                                                                                    |
| 9.1    | No           | None                                                                                                             |
| 9.2    | No           | None                                                                                                             |
| 10.1   | Not verified | No release gate documented                                                                                       |
| 10.2   | Not verified | The project lints itself, but no release gate documented                                                         |
| 11.1   | No           | No declaration                                                                                                   |

## Notes for a practitioner

Write the class as a `go/analysis` analyzer with a chosen `Name`, prove it with `analysistest` against a `testdata` fixture, and ship it through a module plugin so the project's usual `golangci-lint run` enforces it. Enable `nolintlint` with `require-explanation` and `require-specific` from day one, and do not use `new-from-rev`, so that every suppression is at least visible and reasoned even though it sits in the code rather than a record.
