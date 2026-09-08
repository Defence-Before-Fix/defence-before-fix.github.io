---
title: golangci-lint and Defence Before Fix
summary: Module plugins and analysistest meet 4.1 and 4.2; nolintlint meets 7.1 and 7.2; wrapped tool codes leave 4.3 and 6.1 partial
---

# golangci-lint

**Language**: Go · **Kind**: tool · **Readiness**: 🟡 · **Detector conformance**: 🟡 · **Checked**: 2026-09-08, version v2.13.2

golangci-lint is the standard aggregator for Go: one binary that runs staticcheck, go vet, errcheck, unused and around a hundred other linters over a shared parse, configured from a single `.golangci.yml`. In a pipeline it is usually the only lint entry point a Go project has, so it is the natural place for a bespoke defence, and it does support one, at the cost of building a custom binary.

## How it is conformant

Bespoke rules are supported through the [module plugin system](https://golangci-lint.run/docs/plugins/module-plugins/): a project writes a `go/analysis` analyzer, lists it in `.custom-gcl.yml`, builds a custom binary with `golangci-lint custom`, and enables it under `linters.settings.custom` with `type: module` (4.1). The `go/analysis` framework's `analysistest` package runs a single analyzer against `testdata` with `// want` comments as the red proof ([analysistest](https://pkg.go.dev/golang.org/x/tools/go/analysis/analysistest), 4.2). The linter name is chosen once by its author and is what golangci-lint prints in parentheses after each finding, in text and in every reporter format (4.3, for the linter name). `golangci-lint run file1.go` runs locally on one file, and `--default=none --enable <name>` runs one linter ([quick start](https://golangci-lint.run/docs/welcome/quick-start/)), meeting 5.1, 5.2 and 5.4, with every finding in the command's own output (5.3). `golangci-lint help linters` describes every linter from the binary, and a custom analyzer's `Doc` string ships with it (6.1, 6.2, 6.3 at linter level). Clause 7.1 holds because the inline route is detectable by a bundled rule: the `nolintlint` linter reports `//nolint` directives, and its `require-explanation` and `require-specific` settings ([reference configuration](https://github.com/golangci/golangci-lint/blob/main/.golangci.reference.yml)) reject one without a reason, which is exactly the shape of 7.2. The `issues.new-from-rev` and `new-from-merge-base` baselines are configuration the project can simply not set.

## How it is not conformant

Clause 4.3 is partial: the identifier printed is the linter name, so a plugin carrying several rules prints one name for all of them unless it registers each as its own custom linter, and findings from wrapped tools carry that tool's own code, such as `SA1019`, which is stable but which golangci-lint does not itself resolve. That leaves 6.1 to 6.3 partial as well: `help linters` resolves a linter name, but a wrapped tool's rule code resolves only on that tool's website, not from the golangci-lint binary. `nolintlint` is off unless enabled, so 7.2 is met by configuration rather than by default. There is no rule over the rules under 4.4, and no release gate over bundled documentation is documented (6.4, not verified). Readiness is 🟡 rather than 🟢 because the bespoke route requires a custom build rather than a configuration entry, and because of the one-name-per-plugin-linter limit.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                             |
| -------- | ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Yes          | [Module plugins](https://golangci-lint.run/docs/plugins/module-plugins/) via a custom binary                                                         |
| Detector | 4.2    | Yes          | [`analysistest`](https://pkg.go.dev/golang.org/x/tools/go/analysis/analysistest)                                                                     |
| Detector | 4.3    | Partial      | Linter name printed with every finding; one name per plugin linter; wrapped tool codes pass through unresolved                                       |
| Detector | 4.4    | No           | None                                                                                                                                                 |
| Detector | 5.1    | Yes          | `golangci-lint run` locally ([quick start](https://golangci-lint.run/docs/welcome/quick-start/))                                                     |
| Detector | 5.2    | Yes          | `golangci-lint run file1.go`                                                                                                                         |
| Detector | 5.3    | Yes          | Findings printed with linter name                                                                                                                    |
| Detector | 5.4    | Yes          | `--default=none --enable <name>`                                                                                                                     |
| Detector | 6.1    | Partial      | `help linters` resolves a linter name, not a wrapped tool's code                                                                                     |
| Detector | 6.2    | Partial      | Linter descriptions in the binary; wrapped rule docs on the website                                                                                  |
| Detector | 6.3    | Partial      | Custom analyzer `Doc` ships with the analyzer; wrapped tool docs do not                                                                              |
| Detector | 6.4    | Not verified | No release gate documented                                                                                                                           |
| Detector | 7.1    | Yes          | `nolintlint` detects `//nolint` ([false positives](https://golangci-lint.run/docs/linters/false-positives/)); baselines are opt-in                   |
| Detector | 7.2    | Yes          | `nolintlint` `require-explanation` ([reference config](https://github.com/golangci/golangci-lint/blob/main/.golangci.reference.yml)), off by default |

## Notes for a practitioner

Write the class as a `go/analysis` analyzer with a chosen `Name`, prove it with `analysistest` against a `testdata` fixture, and ship it through a module plugin so the project's usual `golangci-lint run` enforces it. Enable `nolintlint` with `require-explanation` and `require-specific` from day one, and do not set `new-from-rev`, so that every suppression is visible and reasoned even though it sits in the code rather than a record.
