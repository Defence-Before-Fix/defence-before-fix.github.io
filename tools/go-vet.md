---
title: go vet and Defence Before Fix
summary: vettool and analysistest pass 4.1 and 4.2; id in plain output not verified; no project record so 8.1, 8.2 and 8.4 fail
---

# go vet

**Language**: Go · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version Go 1.27.1

`go vet` is the analyser that ships with the Go toolchain. It runs a set of around forty analyzers from the `go/analysis` framework, such as `printf` and `unusedresult`, and it is the one Go check every project has whether or not it configured anything. Its significance for this method is the `-vettool` flag, which swaps in a different driver and so lets a project run analyzers of its own through the standard command.

## How it is conformant

Bespoke rules are possible. [The go command](https://pkg.go.dev/cmd/go#hdr-Report_likely_mistakes_in_packages) documents that "the -vettool=prog flag selects a different analysis tool with alternative or additional checks", and the [analysis framework](https://pkg.go.dev/golang.org/x/tools/go/analysis) provides `singlechecker` and `multichecker` to build such a tool from analyzers the project writes (4.1). The `analysistest` package runs one analyzer against a `testdata` directory and checks its diagnostics against `// want` comments, which is a purpose-built harness for the red proof ([analysistest](https://pkg.go.dev/golang.org/x/tools/go/analysis/analysistest), 4.2). The analyzer `Name` is chosen once by its author and "must be a valid Go identifier as it may appear in command-line flags, URLs, and so on" (4.3, partial). `go vet` runs locally, accepts the same package patterns as the rest of the go command, and prints findings in its own output (5.1, 5.2, 5.3); setting one analyzer flag such as `-printf=true` runs only that analyzer (5.4). `go tool vet help <name>` prints the analyzer's `Doc` from the installed toolchain, so the bundled identifiers resolve offline and the documentation travels with the analyzer (6.1, 6.2, 6.3), and `go tool vet help` lists them all (7.1, 7.2).

## How it is not conformant

Clause 4.3 is only partly met: the human-readable output does not carry the analyzer name with each line in the documented format, and the [vet documentation](https://pkg.go.dev/cmd/vet) describes `-json` output without stating that the name is included, so this is recorded as not verified for plain output. Section 8 is absent altogether: `go vet` has no configuration file, no exception list and no inline suppression, so there is nothing to record a decision in (8.1, 8.2, 8.4). Clause 8.3 is met by omission, which is unusual and worth noting, since there is no `//nolint` for `go vet` itself. The listing and resolution under sections 6 and 7 cover the bundled analyzers; for a custom `-vettool`, the tool's own `help` subcommand provides the same, but that is the project's driver rather than `go vet` (7.3 partial). No version is declared (11.1). Readiness is 🟡 rather than 🟢 because the bespoke route requires building and installing a separate driver binary, and because the identifier is not verified as printed with plain-text findings.

## Clause by clause

| Clause | Result       | Evidence                                                                                             |
| ------ | ------------ | ---------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | [`-vettool`](https://pkg.go.dev/cmd/go#hdr-Report_likely_mistakes_in_packages) with a project driver |
| 4.2    | Yes          | [`analysistest`](https://pkg.go.dev/golang.org/x/tools/go/analysis/analysistest)                     |
| 4.3    | Partial      | Name chosen by author; printing in plain output not verified                                         |
| 4.4    | No           | None                                                                                                 |
| 5.1    | Yes          | `go vet ./...` locally                                                                               |
| 5.2    | Yes          | Standard package patterns                                                                            |
| 5.3    | Yes          | Findings printed to stderr with non-zero exit                                                        |
| 5.4    | Yes          | Single analyzer flag ([cmd/vet](https://pkg.go.dev/cmd/vet))                                         |
| 6.1    | Yes          | `go tool vet help <name>`                                                                            |
| 6.2    | Yes          | From the installed toolchain                                                                         |
| 6.3    | Yes          | `Doc` field ships in the analyzer                                                                    |
| 7.1    | Yes          | `go tool vet help`                                                                                   |
| 7.2    | Yes          | Derived from the registered analyzers                                                                |
| 7.3    | Partial      | A custom driver lists its own analyzers, separately                                                  |
| 8.1    | No           | No project record exists                                                                             |
| 8.2    | No           | No exceptions exist to justify                                                                       |
| 8.3    | Yes          | No suppression route at all                                                                          |
| 8.4    | No           | Nothing to enumerate                                                                                 |
| 8.5    | Yes          | Default analyzer set documented                                                                      |
| 9.1    | No           | None                                                                                                 |
| 9.2    | No           | None                                                                                                 |
| 10.1   | Not verified | Analyzer `Doc` is mandatory in the framework; no release gate documented                             |
| 10.2   | Not verified | The Go project vets itself; no release gate documented                                               |
| 11.1   | No           | No declaration                                                                                       |

## Notes for a practitioner

Write the class as a `go/analysis` analyzer, prove it with `analysistest`, and build it into a `multichecker` driver the project installs and invokes through `go vet -vettool`. Because there is no suppression route and no exception record, any narrowing must live in the analyzer's own code with its sentence in the `Doc` string, which is where `go tool vet help` will show it.
