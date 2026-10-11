---
title: NilAway and Defence Before Fix
summary: One fixed nil-flow analysis fails 4.1; plain output carries no identifier and only -json names the analyser, 4.3 partial, and nothing resolves that name, failing 6.1 to 6.3; an undocumented nolint comment can be neither switched off nor seen, failing 7.1, and one on a single dereference hid another sharing its nil source
language: Go
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-10-10, main at commit acb8859
---

# NilAway

{% include tool-grades.html %}

NilAway, from Uber, tracks nil values across functions and packages and reports each flow that can reach a dereference, with the path from the nil source to the panic site ([README at acb8859](https://github.com/uber-go/nilaway/blob/acb8859b9031bb9496be97e027df5573f9fb5340/README.md)). It has no tagged release: the repository's `main` branch at commit `acb8859` (2026-09-18) is what `go install ...@latest` installs, and the README warns that "false positives and breaking changes can happen". It is a `go/analysis` analyser, run as the standalone `nilaway` command, which the README offers "more for evaluation purposes", or through nogo or a golangci-lint module plugin. This page grades the standalone command. It is one analysis with no way to add another, so it cannot host a bespoke defence.

## How it is conformant

The reporting clauses are met. `nilaway ./...` runs locally, takes files and package patterns as the go command does, and prints each finding to its own output with the flow behind it, exiting 3 (ran; paths shortened):

```text
b.go:8:9: Potential nil panic detected. Observed nil flow from source to dereference point:
    - na/a.go:5:24: literal `nil` returned from `get()` in position 0
    - na/b.go:8:9: result 0 of `get()` accessed field `X` via the assignment(s):
        - `get()` to `t` at na/b.go:6:2
```

`-include-errors-in-files=<path>` limits reporting to one file whilst the package is still analysed, and printed the one finding in that file alone (ran), which meets 5.2; with 5.1, 5.3 and 5.4 it needs no infrastructure and has no option that writes findings elsewhere. Graded on its one analysis, 4.2 is met: a run over a fixture package is that analysis alone, with no test suite run (ran).

## How it is not conformant

Clause 4.1 fails: the [configuration documentation](https://github.com/uber-go/nilaway/blob/acb8859b9031bb9496be97e027df5573f9fb5340/docs/configurations.md) describes flags that choose which packages and files are analysed and reported and that turn on experimental parts of the one analysis, and none that adds a pattern. With no rules of the project's own, 4.4 does not apply.

Clause 4.3 is partial, as on the go vet page. The plain output, pretty-printed or not, names no identifier at all (ran). Only the `-json` output carries one, the analyser's name as the key the framework lists each diagnostic under, `"nilaway": [ ... ]` (ran), so the identifier reaches the practitioner in the machine-readable format and not in the default one; and every kind of finding NilAway reports shares that one name. Nothing resolves it: the command has no help or explain subcommand, `nilaway help nilaway` was taken as package names (ran), `-h` prints a one-line description of the whole tool without taking an identifier, and the documentation is in the repository and on the web, not installed by `go install`. So 6.1, 6.2 and 6.3 are No, and no release check over documentation was found (6.4, not verified).

Clause 7.1 fails. The analyser honours `//nolint`, `//nolint:nilaway` and `//nolint:all` comments over the node they annotate, even across packages ([`nolint.go`](https://github.com/uber-go/nilaway/blob/acb8859b9031bb9496be97e027df5573f9fb5340/diagnostic/nolint.go)). The route is not described in the README or the configuration documentation; no flag in `nilaway -h` switches it off, the run reports nothing about what it suppressed, and with no rules of the project's own nothing in NilAway can see it, so the route can be neither switched off nor seen. Its reach is wider than the line it sits on: in a fixture where two functions dereferenced the result of the same `get()` returning `nil`, a `//nolint:nilaway` on one dereference hid both findings and the run exited 0, because by default NilAway groups findings that share a nil source into one diagnostic, and the comment suppressed the group; with `-group-error-messages=false` the unannotated dereference was printed and the run exited 3 (ran). Clause 7.2 fails: the comment needs no reason, and one without a reason suppressed its finding (ran). The `-exclude-pkgs`, `-exclude-errors-in-files`, `-exclude-file-docstrings` and `-exclude-test-files` flags are configuration the project can simply not set, and `-include-errors-in-files` defaults to the current directory.

Two behaviours outside every clause. `-json` exits 0 with findings, as the go vet page records for its own `-json`, so a gate on the exit code must use the plain form (ran). Under reading 9, a file that does not parse is reported, with the syntax errors and `analysis skipped due to errors in package`, and exits 1, apart from a finding (ran). Under Go 1.27.2 the build at `acb8859` ran normally (ran).

The detector grade is 🔴 on 4.1, structural under reading 1, with 4.3 partial and 6.1, 6.2, 6.3, 7.1 and 7.2 failing. Readiness is 🔴: no bespoke rules, and no identifier on findings in the default output.

## Clause by clause

| Document | Clause | Result         | Evidence                                                                                                                                                                                                                              |
| -------- | ------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | No             | Flags select and tune the one analysis ([configurations](https://github.com/uber-go/nilaway/blob/acb8859b9031bb9496be97e027df5573f9fb5340/docs/configurations.md))                                                                    |
| Detector | 4.2    | Yes            | Bundled analysis: a run over a fixture package is it alone (ran)                                                                                                                                                                      |
| Detector | 4.3    | Partial        | No identifier in plain output; `-json` lists findings under `nilaway`, shared by every kind of finding (ran)                                                                                                                          |
| Detector | 4.4    | Not applicable | No rules of the project's own                                                                                                                                                                                                         |
| Detector | 5.1    | Yes            | `nilaway ./...` locally ([README](https://github.com/uber-go/nilaway/blob/acb8859b9031bb9496be97e027df5573f9fb5340/README.md))                                                                                                        |
| Detector | 5.2    | Yes            | File arguments as for the go command; `-include-errors-in-files` reported one file's finding alone (ran)                                                                                                                              |
| Detector | 5.3    | Yes            | Findings and their flows in the command's output (ran)                                                                                                                                                                                |
| Detector | 5.4    | Yes            | Runs locally                                                                                                                                                                                                                          |
| Detector | 6.1    | No             | No command or installed file resolves `nilaway`; `-h` takes no identifier (ran)                                                                                                                                                       |
| Detector | 6.2    | No             | Same                                                                                                                                                                                                                                  |
| Detector | 6.3    | No             | Same                                                                                                                                                                                                                                  |
| Detector | 6.4    | Not verified   | No release check over documentation found                                                                                                                                                                                             |
| Detector | 7.1    | No             | `//nolint` forms honoured, undocumented, with no switch and no report ([`nolint.go`](https://github.com/uber-go/nilaway/blob/acb8859b9031bb9496be97e027df5573f9fb5340/diagnostic/nolint.go)); one hid a second, grouped finding (ran) |
| Detector | 7.2    | No             | No reason required (ran)                                                                                                                                                                                                              |

## Notes for a practitioner

NilAway is an off-the-shelf rule under method clause 3.2 for the class "a nil value reaching a dereference", proven by a fixture package with one such flow and `-include-pkgs` set to the project's module, as the README advises. Pin the commit, since there are no releases, and expect findings to change between commits. Run it with `-group-error-messages=false` wherever `//nolint` comments may exist, so that a comment on one dereference cannot hide another, and back any ban on the comment with a text search outside NilAway, since nothing inside it will report one. Gate on the plain run's exit code, not on `-json`. A project that keeps a note of why each finding was accepted keeps it beside the comment, because NilAway neither asks for a reason nor shows where the comments are.

## Attributes

| Attribute      | Value                                                                                               | Source                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Kind           | Detector                                                                                            | [README](https://github.com/uber-go/nilaway/blob/acb8859b9031bb9496be97e027df5573f9fb5340/README.md)                 |
| Depth          | Semantic with data flow, across functions and packages                                              | [README](https://github.com/uber-go/nilaway/blob/acb8859b9031bb9496be97e027df5573f9fb5340/README.md)                 |
| Output formats | Plain text, pretty-printed by default; `-json` in the go/analysis form; no SARIF                    | ran (`-h`)                                                                                                           |
| Exit codes     | 3 on a finding, 0 with `-json` whatever it finds, 1 on a package or parse error, 2 on a usage error | ran                                                                                                                  |
| Report file    | No                                                                                                  | ran (`-h`)                                                                                                           |
| Unused ignores | No                                                                                                  | [`nolint.go`](https://github.com/uber-go/nilaway/blob/acb8859b9031bb9496be97e027df5573f9fb5340/diagnostic/nolint.go) |
| Rule listing   | No; one analysis                                                                                    | ran (`-h`)                                                                                                           |
| Licence        | Apache 2.0                                                                                          | [LICENSE](https://github.com/uber-go/nilaway/blob/acb8859b9031bb9496be97e027df5573f9fb5340/LICENSE)                  |
