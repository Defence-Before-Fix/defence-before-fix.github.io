---
title: Semgrep and Defence Before Fix
summary: Local YAML rules with a test harness meet 4.1 and 4.2; printed ids carry a path-derived prefix so 4.3 is partial; nosemgrep fails 8.3
---

# Semgrep

**Language**: Multi-language · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 1.176.0

Semgrep is a pattern-based static analyser whose rules are written in YAML using the syntax of the target language itself, across some thirty languages. The open-source command line tool runs locally; the Semgrep AppSec Platform adds a hosted registry, Pro rules, cross-file analysis and triage. In a pipeline it is the usual choice for a project-specific rule that a language linter cannot express cheaply, and its rule-testing harness is one of the best in the field, which makes it a natural detector for the method.

## How it is conformant

Bespoke rules are first class (4.1): a rule is a YAML file anywhere on disk, run with `semgrep scan --config path/to/rule.yaml <target>`, per [running rules](https://docs.semgrep.dev/running-rules), with no login and no server. The proving harness is purpose-built (4.2): `semgrep --test` runs each rule against a test file carrying `# ruleid: <id>` lines where the rule must fire and `# ok: <id>` lines where it must not, entirely locally ([testing rules](https://docs.semgrep.dev/writing-rules/testing-rules)); that is precisely the fixture-based red run clause 3.3 of the method describes. Every rule has a required `id`, "unique, descriptive identifier", and a required `message` ([rule syntax](https://docs.semgrep.dev/writing-rules/rule-syntax)), and the identifier is printed with every finding on the terminal, in JSON and in SARIF ([CLI reference](https://docs.semgrep.dev/cli-reference)), meeting 5.2, 5.3 and 5.4 for local rules. Usage metrics are sent only when registry rules are pulled or the user is logged in, and `--metrics off` disables them ([metrics](https://docs.semgrep.dev/metrics)), so an offline run on local rules is genuinely offline (5.1). The `--validate` flag checks rule files and lints them with a rule set over rules, without searching ([CLI reference](https://docs.semgrep.dev/cli-reference)), which is the nearest any tool in this group comes to 4.4 and part of 7.1. `--disable-nosem` exists, so a project can neutralise inline suppression at the command line. The semgrep-rules repository tests its rules in CI ([semgrep-rules](https://github.com/semgrep/semgrep-rules/blob/develop/README.md)), meeting the spirit of 10.2 for the registry.

## How it is not conformant

Clause 4.3 is only partly met, and it is the reason for the amber readiness. Semgrep prefixes a local rule's identifier with the dotted relative path from the working directory to the rule file ([running rules](https://docs.semgrep.dev/running-rules)), so the printed identifier is derived from the file path, which the clause forbids: moving the rules directory, or running from a different directory, changes every printed identifier and every `nosemgrep: <id>` reference. Resolution (6.1, 6.2) is partial: the `message` and free-form `metadata` travel with the rule, but no command looks up a rule by its printed identifier, and registry rules resolve to online pages at semgrep.dev, which fails 6.2 for bundled rules and 6.3 with them. There is no listing of active rules with identifier and terse statement (7.1); `--validate` confirms the files parse and nothing more. Section 8 is failed: `nosemgrep` and `nosemgrep: <id>` comments and `.semgrepignore` suppress with no reason required ([ignoring code](https://docs.semgrep.dev/ignoring-files-folders-code)), the platform's ignore reason is optional, and although `--disable-nosem` exists it is off by default and nothing in the tool enforces it. No project record is read (8.1) and no method specification version is declared (11.1).

## Clause by clause

| Clause | Result       | Evidence                                                                                                               |
| ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | `--config path/to/rule.yaml` ([running rules](https://docs.semgrep.dev/running-rules))                                 |
| 4.2    | Yes          | `semgrep --test` with `ruleid:` and `ok:` ([testing rules](https://docs.semgrep.dev/writing-rules/testing-rules))      |
| 4.3    | Partial      | Required `id`, but printed with a path-derived prefix ([running rules](https://docs.semgrep.dev/running-rules))        |
| 4.4    | Partial      | `--validate` lints rule files, not identifier stability ([CLI reference](https://docs.semgrep.dev/cli-reference))      |
| 5.1    | Yes          | Local run, `--metrics off` ([metrics](https://docs.semgrep.dev/metrics))                                               |
| 5.2    | Yes          | Any path as target ([running rules](https://docs.semgrep.dev/running-rules))                                           |
| 5.3    | Yes          | Text, `--json`, `--sarif` ([CLI reference](https://docs.semgrep.dev/cli-reference))                                    |
| 5.4    | Partial      | Local rules yes; Pro cross-file rules need the platform                                                                |
| 6.1    | Partial      | `message` and `metadata` in the rule; no lookup by identifier                                                          |
| 6.2    | Partial      | Local rule docs on disk; registry docs online                                                                          |
| 6.3    | No           | Registry rule pages live at semgrep.dev, not in the install                                                            |
| 7.1    | No           | No listing of active rules with identifiers                                                                            |
| 7.2    | No           | See 7.1                                                                                                                |
| 7.3    | No           | See 7.1                                                                                                                |
| 8.1    | No           | No project record read by the tool                                                                                     |
| 8.2    | No           | `nosemgrep` takes no reason ([ignoring code](https://docs.semgrep.dev/ignoring-files-folders-code))                    |
| 8.3    | No           | Inline suppression on by default; `--disable-nosem` opt-in ([CLI reference](https://docs.semgrep.dev/cli-reference))   |
| 8.4    | No           | No enumeration of exceptions                                                                                           |
| 8.5    | Partial      | Default severities and registry defaults documented                                                                    |
| 9.1    | No           | No agent summary                                                                                                       |
| 9.2    | No           | No delivery mechanism                                                                                                  |
| 10.1   | Not verified | Registry rules are tested; no documented gate on missing documentation                                                 |
| 10.2   | Yes          | Rules repository CI tests its rules ([semgrep-rules](https://github.com/semgrep/semgrep-rules/blob/develop/README.md)) |
| 11.1   | No           | No declaration                                                                                                         |

## Notes for a practitioner

Semgrep will carry the six clauses today if you fix two things by convention: always run from the repository root so the path prefix on identifiers is constant, and run with `--disable-nosem` and `--metrics off` in the project's entry point so inline suppression has no effect. Prove each rule with `semgrep --test` against a fixture carrying the hazard, put the remediation in `message` and a markdown file per identifier beside the rule, and keep exceptions in `.semgrepignore` with a stated reason, since the tool asks for none.
