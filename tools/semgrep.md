---
title: Semgrep and Defence Before Fix
summary: Local YAML rules and a test harness meet 4.1 and 4.2; the path-derived prefix fails 4.3; registry rules resolve online only, failing 6.2 and 6.3
---

# Semgrep

**Language**: Multi-language · **Kind**: tool · **Readiness**: 🟡 · **Detector conformance**: 🟡 · **Checked**: 2026-09-08, version 1.176.0

Semgrep is a pattern-based static analyser whose rules are written in YAML using the syntax of the target language itself, across some thirty languages. The open-source command line tool runs locally; the Semgrep AppSec Platform adds a hosted registry, Pro rules, cross-file analysis and triage. In a pipeline it is the usual choice for a project-specific rule that a language linter cannot express cheaply, and its rule-testing harness is one of the best in the field, which makes it a natural detector for the method.

## How it is conformant

Bespoke rules are first class (4.1): a rule is a YAML file anywhere on disk, run with `semgrep scan --config path/to/rule.yaml <target>`, per [running rules](https://docs.semgrep.dev/running-rules), with no login and no server. The proving harness is purpose-built (4.2): `semgrep --test` runs each rule against a test file carrying `# ruleid: <id>` lines where the rule must fire and `# ok: <id>` lines where it must not, entirely locally ([testing rules](https://docs.semgrep.dev/writing-rules/testing-rules)); that is precisely the fixture-based red run clause 3.3 of the method describes, and it works for a single rule file. Every rule has a required `id`, "unique, descriptive identifier", and a required `message` ([rule syntax](https://docs.semgrep.dev/writing-rules/rule-syntax)), and an identifier is printed with every finding on the terminal, in JSON and in SARIF ([CLI reference](https://docs.semgrep.dev/cli-reference)). Any path can be the target, so a single file runs (5.2), and the findings arrive in the command's own output in text, `--json` or `--sarif` (5.3). Usage metrics are sent only when registry rules are pulled or the user is logged in, and `--metrics off` disables them ([metrics](https://docs.semgrep.dev/metrics)), so an offline run on local rules is genuinely offline (5.1). Inline suppression can be switched off outright: `--disable-nosem` makes `nosemgrep` comments inert ([CLI reference](https://docs.semgrep.dev/cli-reference)), which is exactly the disableable route clause 7.1 asks for. The `--validate` flag lints rule files with a rule set over rules, without searching, which is the nearest any tool in this group comes to 4.4.

## How it is not conformant

Clause 4.3 is failed, and it is the reason for the amber readiness. Semgrep prefixes a local rule's identifier with the dotted relative path from the working directory to the rule file ([running rules](https://docs.semgrep.dev/running-rules)), and the clause states in terms that a prefix the detector adds from the invoking directory or the rule's location is derived from the file path: moving the rules directory, or running from a different directory, changes every printed identifier and every `nosemgrep: <id>` reference. Registry rules are bundled rules under the detector specification's definition, because Semgrep fetches them on the practitioner's behalf from a source its maintainer controls, and their documentation lives at semgrep.dev rather than in the install. A registry identifier resolves at `semgrep.dev/r/<id>`, which is a URL keyed on the identifier as printed and so meets the form 6.1 allows, but only with network access, failing 6.2, and nothing ships the rule's page alongside the rule, failing 6.3. Whether the registry's release is gated on every rule having a page is not documented (6.4). For a project's own rule the detector owes the identifier printed unaltered, and the path prefix is the alteration, so 6.1 is only partly met there too. Pro rules and cross-file analysis fire only with a logged-in licence tier ([Pro engine](https://semgrep.dev/docs/semgrep-code/semgrep-pro-engine-intro)), so 5.4 is partial for that part of the catalogue. `nosemgrep` takes no reason and `--disable-nosem` is off by default ([ignoring code](https://docs.semgrep.dev/ignoring-files-folders-code)), so 7.2 is not met.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                          |
| -------- | ------ | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Yes          | `--config path/to/rule.yaml` ([running rules](https://docs.semgrep.dev/running-rules))                            |
| Detector | 4.2    | Yes          | `semgrep --test` with `ruleid:` and `ok:` ([testing rules](https://docs.semgrep.dev/writing-rules/testing-rules)) |
| Detector | 4.3    | No           | Required `id`, but printed with a path-derived prefix ([running rules](https://docs.semgrep.dev/running-rules))   |
| Detector | 4.4    | Partial      | `--validate` lints rule files, not identifier stability ([CLI reference](https://docs.semgrep.dev/cli-reference)) |
| Detector | 5.1    | Yes          | Local run, `--metrics off` ([metrics](https://docs.semgrep.dev/metrics))                                          |
| Detector | 5.2    | Yes          | Any path as target ([running rules](https://docs.semgrep.dev/running-rules))                                      |
| Detector | 5.3    | Yes          | Text, `--json`, `--sarif` ([CLI reference](https://docs.semgrep.dev/cli-reference))                               |
| Detector | 5.4    | Partial      | Local rules yes; Pro rules and cross-file analysis need a logged-in licence tier                                  |
| Detector | 6.1    | Partial      | Registry ids resolve at `semgrep.dev/r/<id>`; local ids are printed altered, see 4.3                              |
| Detector | 6.2    | No           | Registry rule pages need network access                                                                           |
| Detector | 6.3    | No           | Registry rule pages live at semgrep.dev, not in the install                                                       |
| Detector | 6.4    | Not verified | Registry rules are tested in CI; no documented gate on missing documentation                                      |
| Detector | 7.1    | Yes          | `--disable-nosem` switches inline suppression off ([CLI reference](https://docs.semgrep.dev/cli-reference))       |
| Detector | 7.2    | No           | `nosemgrep` takes no reason ([ignoring code](https://docs.semgrep.dev/ignoring-files-folders-code))               |

## Notes for a practitioner

Semgrep will carry the six clauses today if you fix two things by convention: always run from the repository root so the path prefix on identifiers is constant, and run with `--disable-nosem` and `--metrics off` in the project's entry point so inline suppression has no effect. Prove each rule with `semgrep --test` against a fixture carrying the hazard, put the remediation in `message` and a markdown file per identifier beside the rule, and keep exceptions in `.semgrepignore` with a stated reason, since the tool asks for none.
