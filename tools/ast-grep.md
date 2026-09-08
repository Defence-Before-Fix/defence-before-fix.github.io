---
title: ast-grep and Defence Before Fix
summary: Bespoke YAML rules with a test harness and printed ids meet 4.1 to 5.4; no listing for 7.1 and inline ast-grep-ignore fails 8.3
---

# ast-grep

**Language**: Multi-language · **Kind**: tool · **Readiness**: 🟢 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 0.45.3

ast-grep is a single-binary, tree-sitter based structural search and lint tool that matches code by its syntax tree rather than by text, across a few dozen languages. It ships no rule catalogue of its own: every rule is a YAML file the project writes, so in a pipeline it is a bespoke-rule engine sitting beside the language's conventional linter, and it is well suited to the class defence the method asks for because writing a rule for one pattern is its whole purpose.

## How it is conformant

Bespoke rules are the product (4.1). A project declares `ruleDirs` in `sgconfig.yml` and every YAML file found there is a rule, as described in [the sgconfig reference](https://ast-grep.github.io/reference/sgconfig.html). A single rule can be run against a single path with `ast-grep scan --rule <file> [paths]`, with no configuration file at all, and `--filter` narrows a configured run by rule identifier ([scan reference](https://ast-grep.github.io/reference/cli/scan.html)); that satisfies 4.2 and 5.2. There is a purpose-built proving harness: `ast-grep test` runs test YAML files carrying `valid` and `invalid` cases against a rule, with snapshots for the matched spans, per [the test guide](https://ast-grep.github.io/guide/test-rule.html), which is exactly the fixture-based red run clause 3.3 of the method wants. Every rule carries a required `id` field, "unique, descriptive identifier", taken from the field rather than the file name ([YAML reference](https://ast-grep.github.io/reference/yaml.html)), and the default terminal report prints it with the message, in the form `error[no-eval]: ...` followed by file, line and span ([scan a project](https://ast-grep.github.io/guide/scan-project.html)); that is 4.3, 5.3 and 5.4. Nothing needs a server (5.1). A rule with `severity: error` makes the scan exit non-zero ([severity guide](https://ast-grep.github.io/guide/project/severity.html)), so enforcement under clause 3.5 of the method is direct.

## How it is not conformant

Resolution (6.1) is only half there. A rule may carry `message`, `note` and `url`, and `note` is present in JSON output ([JSON guide](https://ast-grep.github.io/guide/tools/json.html)), but `url` is documented as "displayed in editor extensions" and no subcommand shows a rule by its identifier: the CLI offers `run`, `scan`, `test`, `new`, `outline`, `lsp` and `completions` ([CLI reference](https://ast-grep.github.io/reference/cli.html)). The project can keep documentation on disk beside the rule, which meets 6.2 in substance, but the toolchain supplies no lookup keyed on the printed identifier. There is no listing of active rules without scanning (7.1, 7.2, 7.3); the nearest is `scan --inspect`, which runs the scan. Section 8 is unmet: no project record is read by the tool (8.1), no exception carries a justification (8.2), and inline `// ast-grep-ignore` and `// ast-grep-ignore: rule-id` comments suppress silently with no documented way to disable them ([severity guide](https://ast-grep.github.io/guide/project/severity.html)), which fails 8.3 structurally. Because ast-grep bundles no defences, 6.3, 10.1 and 10.2 have nothing to apply to, and the repository does not run ast-grep rules on its own source. No method specification version is declared (11.1).

## Clause by clause

| Clause | Result         | Evidence                                                                                                              |
| ------ | -------------- | --------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes            | `ruleDirs` in [sgconfig.yml](https://ast-grep.github.io/reference/sgconfig.html)                                      |
| 4.2    | Yes            | `ast-grep test` with `valid`/`invalid` cases ([test guide](https://ast-grep.github.io/guide/test-rule.html))          |
| 4.3    | Yes            | Required `id` field, printed as `error[id]` ([YAML reference](https://ast-grep.github.io/reference/yaml.html))        |
| 4.4    | No             | No rule over the rules                                                                                                |
| 5.1    | Yes            | Single binary, no server ([CLI reference](https://ast-grep.github.io/reference/cli.html))                             |
| 5.2    | Yes            | `scan --rule <file> [paths]` ([scan reference](https://ast-grep.github.io/reference/cli/scan.html))                   |
| 5.3    | Yes            | Findings on stdout; `--json`, `--format github` and SARIF                                                             |
| 5.4    | Yes            | Every rule runs locally                                                                                               |
| 6.1    | Partial        | `note`/`url` fields exist; no lookup by identifier ([YAML reference](https://ast-grep.github.io/reference/yaml.html)) |
| 6.2    | Partial        | Documentation lives with the project's rule; no resolver                                                              |
| 6.3    | Not applicable | No bundled defences                                                                                                   |
| 7.1    | No             | No listing without scanning ([scan reference](https://ast-grep.github.io/reference/cli/scan.html))                    |
| 7.2    | No             | See 7.1                                                                                                               |
| 7.3    | No             | See 7.1                                                                                                               |
| 8.1    | No             | No project record read by the tool                                                                                    |
| 8.2    | No             | No justification mechanism                                                                                            |
| 8.3    | No             | `// ast-grep-ignore` cannot be disabled ([severity guide](https://ast-grep.github.io/guide/project/severity.html))    |
| 8.4    | No             | No enumeration of exceptions                                                                                          |
| 8.5    | Partial        | Default severity `hint` documented; no method calibrations                                                            |
| 9.1    | No             | Docs site ships `llms.txt`, not a per-project summary                                                                 |
| 9.2    | No             | No delivery mechanism                                                                                                 |
| 10.1   | Not applicable | No bundled defences                                                                                                   |
| 10.2   | No             | Repository CI runs cargo tests, not ast-grep on itself                                                                |
| 11.1   | No             | No declaration                                                                                                        |

## Notes for a practitioner

ast-grep is one of the easiest tools on which to run the six clauses today: write the rule, prove it red with `ast-grep test`, sweep with `scan`, set `severity: error`. Put the remediation text in the rule's `note` and keep a markdown file per rule identifier beside the rule directory, since the tool will not resolve the identifier for you. Add a second rule that matches `ast-grep-ignore` comments and ban them, and keep exceptions in `sgconfig.yml` with a stated reason, because nothing in the tool demands one.
