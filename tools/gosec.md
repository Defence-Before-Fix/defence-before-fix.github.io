---
title: gosec and Defence Before Fix
summary: A fixed catalogue of G rules fails 4.1; the CSV and JUnit formats drop the G code and golint prefixes it, 4.3 partial; gosec -h lists every code with its description offline for 6.1 to 6.3; an output file leaves the command silent, 5.3 partial, and a package is the smallest unit, 5.2 partial; -nosec closes every inline route for 7.1
language: Go
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-10-10, version v2.29.0
---

# gosec

{% include tool-grades.html %}

gosec is the security scanner most Go projects run, a catalogue of 61 rules with identifiers such as `G401` (weak hash) and `G204` (command execution), some of them AST pattern checks and some SSA and taint analyses that follow values through the program ([README at v2.29.0](https://github.com/securego/gosec/blob/v2.29.0/README.md), [RULES.md](https://github.com/securego/gosec/blob/v2.29.0/RULES.md)). In a pipeline it runs on its own or as the `gosec` linter inside golangci-lint. It is a fixed catalogue: a project chooses and tunes rules and cannot add one, so it cannot host a bespoke defence.

## How it is conformant

Graded on its bundled rules, gosec meets 4.2: `-include=G401` runs that rule alone over a package and prints only its findings, and a run of v2.29.0 printed the two `G401` findings in a fixture and nothing from the `G501` and `G505` import rules that fired on the same files without the flag (ran). An unknown code is not a silent pass: `-include=G999` logged `No rules/analyzers are configured` and exited 1 (ran). It runs locally with no infrastructure and prints findings in the command's own output, each with its code: `[a.go:9] - G401 (CWE-328): Use of weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)` (ran), which meets 5.1 and 5.4 together with the default case of 5.3. The optional AI fix suggestions call a hosted model only when `-ai-api-provider` is set ([README](https://github.com/securego/gosec/blob/v2.29.0/README.md)); no finding depends on them.

Section 6 is met by the rule listing. `gosec -h` ends with a `RULES:` section that prints every rule as its code and a one-line description, `G401: Detect the usage of MD5 or SHA1`, generated from the rule and analyser lists compiled into the binary ([`main.go`](https://github.com/securego/gosec/blob/v2.29.0/cmd/gosec/main.go#L203)). That is an index whose entry for each identifier exactly as printed holds its description, under reading 11, and under reading 12 a one-line description is documentation, so 6.1 holds; the 61 codes it listed under `unshare -rn`, with no network, are every code in the rule and analyser sources at the tag, so 6.2 and 6.3 hold as well (ran). The descriptions are brief, and the fuller [RULES.md](https://github.com/securego/gosec/blob/v2.29.0/RULES.md) is in the repository only: the release archive holds the binary, the README and the licence (ran).

Clause 7.1 holds for every route. The inline routes are `#nosec`, `//gosec:disable` and any alternative tag set with `-nosec-tag`; the `-nosec` flag, "Ignores #nosec comments", switched off all three in a run of v2.29.0, which then printed the `G401` findings under a `#nosec`, a `//gosec:disable` and a `-nosec-tag=#falsepositive` comment, and the configuration's `global.nosec` setting does the same ([README](https://github.com/securego/gosec/blob/v2.29.0/README.md)). The exclusion routes, `-exclude`, `-exclude-rules`, `-exclude-dir`, `-exclude-generated` and their configuration forms, are configuration the project can simply not set. Every route is also detectable: `-track-suppressions` lists each suppressed finding in the JSON and SARIF reports with its kind, `inSource` or `external`, and its justification (ran), and `-show-ignored` prints them in text marked `G401 (NoSec)`. Clause 7.2 is met by configuration: `-nosec-require-justification` and `-nosec-require-rules` reject a directive without a `--` reason or without a rule code, and a rejected directive suppresses nothing; a run with both printed `invalid nosec directive: missing rule ID` for a bare `#nosec` and reported the finding under it (ran). Both are off by default.

## How it is not conformant

Clause 4.1 fails: the [README](https://github.com/securego/gosec/blob/v2.29.0/README.md) and [RULES.md](https://github.com/securego/gosec/blob/v2.29.0/RULES.md) describe selecting rules and configuring some of them, such as `G101`'s credential patterns, which changes what an existing rule matches rather than adding one, and the exported `goanalysis` analyser lets another driver run gosec's rules, not add to them. With no project rules, 4.4 does not apply.

Clause 4.3 is partial. The code is assigned once by the maintainers and is stable, and the text, JSON, YAML, SARIF, SonarQube and HTML reports carry it unaltered (ran). Two machine-readable formats drop it: a `-fmt=csv` row is the file, line, message, severity, confidence, code snippet and CWE, and a `-fmt=junit-xml` failure gives the message and `CWE: 328` with no rule code (ran). The `golint` format prints `(Rule:G401, Severity:MEDIUM, Confidence:HIGH)`, a constant prefix joined to the code, which alters it under reading 6.

Clause 5.2 is partial: arguments are package directories or patterns, and a file is refused, `gosec a.go` and `gosec ./a.go` both printing `importing dir "a.go": cannot find package` and exiting 1 (ran), although the README's own example passes `*.go`. The smallest subset is a package, as on the Clippy page. Clause 5.3 is partial under reading 8: with `-out=results.json` the command printed only its log lines to standard error, with no count and no mention of the file (ran); `-stdout` with `-verbose=text` prints the full text report as well.

Clause 6.4 is not verified: the rule list in the help is generated from the same definitions as the rules, but no test or release step that checks every rule's description was found; one test checks the description of `G701` only ([`analyzerslist_test.go`](https://github.com/securego/gosec/blob/v2.29.0/analyzers/analyzerslist_test.go)).

Two behaviours fall outside every clause but matter to a defence routed through gosec. Release v2.29.0 cannot fully analyse code under Go 1.27.2: every package printed `could not import fmt ... export data version 5 is greater than maximum supported version 4`, the SSA and taint rules were skipped (`skipping SSA analysis`), and a fixture with two `G115` findings under Go 1.26.8 reported none under Go 1.27.2, whilst the AST rules still reported (ran). The run exits 1 and prints the errors, so the failure is not hidden. The fault is [issue 1771](https://github.com/securego/gosec/issues/1771), closed upstream on 2026-10-09 and not yet in a release. Under reading 9, a file that does not parse is reported: the syntax error was printed under `Golang errors` and the run exited 1, the code a finding also gets (ran).

The detector grade is 🔴 on 4.1, which is structural under reading 1, with 4.3, 5.2 and 5.3 partial. Readiness is 🔴: no bespoke rules.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                                                                 |
| -------- | ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | No           | Rule selection and per-rule configuration only ([README](https://github.com/securego/gosec/blob/v2.29.0/README.md), [RULES.md](https://github.com/securego/gosec/blob/v2.29.0/RULES.md)) |
| Detector | 4.2    | Yes          | Bundled rules: `-include=G401` printed only that rule's findings; `-include=G999` exited 1 (ran)                                                                                         |
| Detector | 4.3    | Partial      | Code unaltered in text, JSON, YAML, SARIF, SonarQube and HTML; absent from CSV and JUnit XML; `Rule:G401` in golint (ran; reading 6)                                                     |
| Detector | 4.4    | No           | No rules of the project's to enforce on                                                                                                                                                  |
| Detector | 5.1    | Yes          | `gosec ./...` locally ([README](https://github.com/securego/gosec/blob/v2.29.0/README.md))                                                                                               |
| Detector | 5.2    | Partial      | Package directories only; a file argument fails with `cannot find package` (ran)                                                                                                         |
| Detector | 5.3    | Partial      | Default text output carries every finding; `-out` leaves the command with log lines only, no count or file (ran; reading 8)                                                              |
| Detector | 5.4    | Yes          | Every rule runs locally; the AI suggestions are optional and no finding depends on them                                                                                                  |
| Detector | 6.1    | Yes          | `gosec -h` lists each code with its description ([`main.go`](https://github.com/securego/gosec/blob/v2.29.0/cmd/gosec/main.go#L203); reading 11)                                         |
| Detector | 6.2    | Yes          | The listing is compiled in; all 61 codes listed under `unshare -rn` (ran)                                                                                                                |
| Detector | 6.3    | Yes          | The 61 listed codes are every code in the rule and analyser sources at the tag (ran)                                                                                                     |
| Detector | 6.4    | Not verified | No check over every rule's description found; one test covers `G701` ([`analyzerslist_test.go`](https://github.com/securego/gosec/blob/v2.29.0/analyzers/analyzerslist_test.go))         |
| Detector | 7.1    | Yes          | `-nosec` closed `#nosec`, `//gosec:disable` and a `-nosec-tag` alternative; `-track-suppressions` lists every suppression in JSON and SARIF (ran); exclusions are opt-in configuration   |
| Detector | 7.2    | Yes          | `-nosec-require-justification` and `-nosec-require-rules`, off by default; a rejected directive suppressed nothing (ran)                                                                 |

## Notes for a practitioner

gosec is a source of off-the-shelf security rules under method clause 3.2, each provable with `-include=<code>` against a fixture package; a bespoke security class needs a `go/analysis` analyser or a ruleguard rule run through golangci-lint. Pass packages, not files. Run it under Go 1.26 until a release after v2.29.0 carries the importer fix, or check that no `could not import` errors appear, because under Go 1.27.2 the SSA and taint rules stop reporting. In the enforced invocation set `-nosec-require-rules -nosec-require-justification`, and add `-nosec` if inline suppression is forbidden outright; `-track-suppressions` with `-fmt=json` gives the record of every suppression in force. Do not route a report through CSV or JUnit XML, which lose the rule code, and print or count the report after an `-out` run, since the command itself says nothing about it. To look up a code offline, `gosec -h` and find its line.

## Attributes

| Attribute      | Value                                                                                                  | Source                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| Kind           | Detector                                                                                               | [README](https://github.com/securego/gosec/blob/v2.29.0/README.md)        |
| Depth          | Semantic with data flow: AST rules over typed packages, SSA analysers and taint analysis               | [RULES.md](https://github.com/securego/gosec/blob/v2.29.0/RULES.md)       |
| Output formats | text, json, yaml, csv, junit-xml, html, sonarqube, golint, sarif; SARIF native                         | ran                                                                       |
| Exit codes     | 1 on a finding, 1 on a load or parse error, 1 when no rule matches `-include`, 2 on a usage error      | ran                                                                       |
| Report file    | `-out` writes it with nothing on the console; `-stdout -verbose=text` prints the full report beside it | ran                                                                       |
| Fix mode       | No rewrite; optional fix suggestions from a hosted AI model                                            | [README](https://github.com/securego/gosec/blob/v2.29.0/README.md)        |
| Baseline       | No                                                                                                     | [README](https://github.com/securego/gosec/blob/v2.29.0/README.md)        |
| Rule listing   | `gosec -h` lists every rule with its description, not only those enabled                               | ran                                                                       |
| Licence        | Apache 2.0                                                                                             | [LICENSE.txt](https://github.com/securego/gosec/blob/v2.29.0/LICENSE.txt) |
