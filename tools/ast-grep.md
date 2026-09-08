---
title: ast-grep and Defence Before Fix
summary: Bespoke YAML rules, a test harness and printed ids meet every MUST in 4 and 5; kind and regex rules make ast-grep-ignore detectable for 7.1
---

# ast-grep

**Language**: Multi-language · **Kind**: tool · **Readiness**: 🟢 · **Detector conformance**: 🟢 · **Checked**: 2026-09-08, version 0.45.3

ast-grep is a single-binary, tree-sitter based structural search and lint tool that matches code by its syntax tree rather than by text, across a few dozen languages. It ships no rule catalogue of its own: every rule is a YAML file the project writes, so in a pipeline it is a bespoke-rule engine sitting beside the language's conventional linter, and it is well suited to the class defence the method asks for because writing a rule for one pattern is its whole purpose.

## How it is conformant

Bespoke rules are the product (4.1). A project declares `ruleDirs` in `sgconfig.yml` and every YAML file found there is a rule, as described in [the sgconfig reference](https://ast-grep.github.io/reference/sgconfig.html). A single rule can be run against a single path with `ast-grep scan --rule <file> [paths]`, with no configuration file at all, and `--filter` narrows a configured run by rule identifier ([scan reference](https://ast-grep.github.io/reference/cli/scan.html)); that satisfies 5.2. There is a purpose-built proving harness (4.2): `ast-grep test` runs test YAML files carrying `valid` and `invalid` cases against a rule, with snapshots for the matched spans, per [the test guide](https://ast-grep.github.io/guide/test-rule.html), which is exactly the fixture-based red run clause 3.3 of the method wants. Every rule carries a required `id` field, "unique, descriptive identifier", taken from the field rather than the file name ([YAML reference](https://ast-grep.github.io/reference/yaml.html)); the default terminal report prints it unaltered with the message, in the form `error[no-eval]: ...` followed by file, line and span ([scan a project](https://ast-grep.github.io/guide/scan-project.html)), and the JSON output carries it as `ruleId` beside `message`, `severity` and `note` ([JSON guide](https://ast-grep.github.io/guide/tools/json.html)); that is 4.3 and 5.3. Nothing needs a server, a login or a licence tier (5.1, 5.4). Because ast-grep bundles no rules, the resolution it owes under 6.1 is the half a detector can give for a project's own rule, the identifier printed unaltered, and it gives it; 6.2, 6.3 and 6.4 have no bundled rule to apply to. The inline `// ast-grep-ignore` and `// ast-grep-ignore: rule-id` comments cannot be switched off, but they are detectable by a rule written in ast-grep itself: the `kind` atomic rule matches any tree-sitter node kind, including a grammar's comment node, and `regex` matches the node's text ([atomic rules](https://ast-grep.github.io/guide/rule-config/atomic-rule.html)), so a project that forbids the route can fail on it, which is what 7.1 requires. The built-in `no-suppress-all` rule, enabled with `--error=no-suppress-all`, already flags the blanket form ([severity guide](https://ast-grep.github.io/guide/project/severity.html)). A rule with `severity: error` makes the scan exit non-zero, so enforcement under clause 3.5 of the method is direct.

## How it is not conformant

Only the SHOULD clauses are open. There is no rule over the rules that fails a rule reporting without a stable identifier (4.4), though `id` is required so the case is hard to reach. Neither `ast-grep-ignore: rule-id` nor the blanket form takes a reason, and `no-suppress-all` asks for a rule identifier rather than a sentence, so 7.2 is not met. The `url` field on a rule is documented as "displayed in editor extension if supported" and no subcommand shows a rule by its identifier ([CLI reference](https://ast-grep.github.io/reference/cli.html)), so the lookup from a printed identifier to the project's own documentation is left to the project's toolchain, which is where the detector specification places it.

## Clause by clause

| Document | Clause | Result         | Evidence                                                                                                                                                              |
| -------- | ------ | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Yes            | `ruleDirs` in [sgconfig.yml](https://ast-grep.github.io/reference/sgconfig.html)                                                                                      |
| Detector | 4.2    | Yes            | `ast-grep test` with `valid`/`invalid` cases ([test guide](https://ast-grep.github.io/guide/test-rule.html))                                                          |
| Detector | 4.3    | Yes            | Required `id`, printed as `error[id]` and as JSON `ruleId` ([JSON guide](https://ast-grep.github.io/guide/tools/json.html))                                           |
| Detector | 4.4    | No             | No rule over the rules                                                                                                                                                |
| Detector | 5.1    | Yes            | Single binary, no server ([CLI reference](https://ast-grep.github.io/reference/cli.html))                                                                             |
| Detector | 5.2    | Yes            | `scan --rule <file> [paths]` ([scan reference](https://ast-grep.github.io/reference/cli/scan.html))                                                                   |
| Detector | 5.3    | Yes            | Findings on stdout; `--json`, `--format github` and SARIF                                                                                                             |
| Detector | 5.4    | Yes            | Every rule runs locally                                                                                                                                               |
| Detector | 6.1    | Yes            | No bundled rules; project ids printed unaltered, which is what the clause asks of a detector for a project's own rule                                                 |
| Detector | 6.2    | Not applicable | No bundled rules                                                                                                                                                      |
| Detector | 6.3    | Not applicable | No bundled rules                                                                                                                                                      |
| Detector | 6.4    | Not applicable | No bundled rules                                                                                                                                                      |
| Detector | 7.1    | Yes            | `kind` and `regex` match the ignore comment ([atomic rules](https://ast-grep.github.io/guide/rule-config/atomic-rule.html)); `no-suppress-all` flags the blanket form |
| Detector | 7.2    | No             | `ast-grep-ignore: rule-id` takes no reason ([severity guide](https://ast-grep.github.io/guide/project/severity.html))                                                 |

## Notes for a practitioner

ast-grep is one of the easiest tools on which to run the six clauses today: write the rule, prove it red with `ast-grep test`, sweep with `scan`, set `severity: error`. Put the remediation text in the rule's `note` and keep a markdown file per rule identifier beside the rule directory, since the tool will not resolve the identifier for you. Add a rule on the comment kind that matches `ast-grep-ignore` and set it to error, run with `--error=no-suppress-all`, and keep exceptions in `sgconfig.yml` with a stated reason, because nothing in the tool demands one.
