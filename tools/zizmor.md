---
title: zizmor and Defence Before Fix
summary: Compiled-in audits so 4.1 fails; one audit runs alone only by disabling the rest in configuration, 4.2 partial; SARIF prefixes zizmor/ to the id, 4.3 partial; printed documentation URLs keyed on the id resolve online only, 6.1 partial and 6.2 and 6.3 failing; --no-ignores and ignored counts meet 7.1
language: YAML
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-10-10, version 1.30.1
---

# zizmor

{% include tool-grades.html %}

zizmor is a static security auditor for GitHub Actions, written in Rust: it reads workflows, composite actions, Dependabot and pre-commit configuration and reports 41 classes of risk, such as template injection, dangerous triggers, unpinned actions and credentials persisted by `actions/checkout`, each an audit with an id such as `template-injection`. Some audits are online, querying the GitHub API for facts such as impostor commits and known-vulnerable actions, and need a token. In a pipeline it runs beside actionlint, which checks that a workflow is well formed, as the check of whether it is safe. Its audits are compiled in, and a project tunes them but cannot add one.

## How it is conformant

Each audit's id is chosen once in its source with `audit_meta!` ([`audit/mod.rs`](https://github.com/zizmorcore/zizmor/blob/v1.30.1/crates/zizmor/src/audit/mod.rs)) and printed with every finding: `error[template-injection]: code injection via template expansion` in the default `plain` format, `"ident": "template-injection"` in `json`, and `title=template-injection` in `github` (ran, version 1.30.1). `zizmor --offline w.yml` runs locally on one file, and `-` reads standard input (5.1, 5.2); it ran with the network removed (`unshare -rn`), exit 14. The online audits run from the same local command once a GitHub token is given, and the offline audits run without one, so no finding is held back for a hosted tier (5.4); without a token the online audits are skipped ([usage, operating modes](https://github.com/zizmorcore/zizmor/blob/v1.30.1/docs/usage.md)). Findings are the command's own output, closing with a summary such as `10 findings (1 ignored, 4 suppressed, 2 unsafe fixes)`, and the exit code is 11 to 14 by the highest severity found ([usage, exit codes](https://github.com/zizmorcore/zizmor/blob/v1.30.1/docs/usage.md)), 14 in the run (5.3).

Every finding in `plain` output carries `audit documentation → https://docs.zizmor.sh/audits/#template-injection`, and `json` a `url` field of the same form: the id placed in a fixed address, printed by zizmor (reading 10). The address is built as `concat!("https://docs.zizmor.sh/audits/#", $id)` in [`audit/mod.rs`](https://github.com/zizmorcore/zizmor/blob/v1.30.1/crates/zizmor/src/audit/mod.rs), and all 41 ids declared in the source at the tag have a heading of that name in [`docs/audits.md`](https://github.com/zizmorcore/zizmor/blob/v1.30.1/docs/audits.md) (checked by script), and the published page carried an anchor for each of the 41 when fetched on the checked date. So an id as printed in `plain`, `json` and `github` resolves to its documentation (6.1, for those forms).

Both suppression routes can be closed and are counted. An inline `# zizmor: ignore[template-injection]` comment and a configuration entry under `rules.<id>.ignore` both silenced their finding and were counted in the summary as `1 ignored` and `2 ignored` (ran); `--no-ignores` "Don't honor ignore comments or ignore rules in configuration" (`--help`), and with it the ignored finding was reported again (ran); `--no-config` loads no configuration at all ([configuration](https://github.com/zizmorcore/zizmor/blob/v1.30.1/docs/configuration.md)). Each route is disableable and detectable (7.1). `rules.<id>.disable` turns an audit off and is not counted, as the configuration page warns, but it is configuration the project owns and `--no-config` closes it.

## How it is not conformant

Clause 4.1 fails. `zizmor --help` lists no option that loads an audit, and the audits are Rust modules registered at build time in [`crates/zizmor/src/audit/`](https://github.com/zizmorcore/zizmor/tree/v1.30.1/crates/zizmor/src/audit); a project can configure some audits through `rules.<id>.config`, such as the actions `forbidden-uses` refuses, but cannot express a pattern of its own. Clause 4.4 has nothing to apply to.

Clause 4.2 is graded on the bundled audits and is partial. No option selects one audit; the route is a configuration that sets `rules.<id>.disable: true` for every other one ([configuration](https://github.com/zizmorcore/zizmor/blob/v1.30.1/docs/configuration.md)), and a configuration disabling the other 40 left only the `template-injection` finding (ran), the case of reading 4.

Clause 4.3 is partial. In SARIF the id is joined to a constant prefix, `"ruleId": "zizmor/template-injection"`, with the bare id only in the rule's `name` field (ran), which alters it under reading 6. The same leaves 6.1 partial: the documentation address is keyed on `template-injection`, so the SARIF form resolves only once its prefix is cut, which reading 11 does not allow. The mechanism is a website, so nothing resolves from the installed copy and 6.2 fails, and the documentation ships with neither the wheel, whose files are the binary, its licence and a bill of materials, nor the binary, so 6.3 fails. The repository's CI checks that the configuration schema covers every audit, but nothing checks the documentation ([`ci.yml`](https://github.com/zizmorcore/zizmor/blob/v1.30.1/.github/workflows/ci.yml), 6.4).

An ignore comment "can also have a trailing explanation" ([usage, ignoring results](https://github.com/zizmorcore/zizmor/blob/v1.30.1/docs/usage.md)), but nothing requires one (7.2).

Two behaviours are recorded under reading 9. A workflow that fails to parse inside a directory run is only a `WARN` on standard error and is skipped, the run exiting on the other files' findings (14 in the run), unless `--strict-collection` is given, which exited 1; given alone, the same file exited 3, `no inputs collected` (ran). And `--format sarif` does not use exit codes 11 and above, by design, so a SARIF run exits 0 on findings (ran; [usage, exit codes](https://github.com/zizmorcore/zizmor/blob/v1.30.1/docs/usage.md)).

Readiness is 🔴 because no bespoke audit can be written. The detector grade is 🔴 because 4.1 fails, a structural MUST under reading 1; 4.2, 4.3 and 6.1 are partial, and 6.2, 6.3, 6.4 and 7.2 fail. zizmor declares no version of this document.

## Clause by clause

| Document | Clause | Result  | Evidence                                                                                                                                                                                |
| -------- | ------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | No      | Audits compiled in ([`audit/`](https://github.com/zizmorcore/zizmor/tree/v1.30.1/crates/zizmor/src/audit)); no load option (`--help`)                                                   |
| Detector | 4.2    | Partial | Bundled audits: no select option; `rules.<id>.disable` for the others ran one ([configuration](https://github.com/zizmorcore/zizmor/blob/v1.30.1/docs/configuration.md)), reading 4     |
| Detector | 4.3    | Partial | `template-injection` in plain, json and github; `zizmor/template-injection` in SARIF (ran), reading 6                                                                                   |
| Detector | 4.4    | No      | No bespoke rules for it to apply to                                                                                                                                                     |
| Detector | 5.1    | Yes     | Ran locally with `--offline` and the network removed                                                                                                                                    |
| Detector | 5.2    | Yes     | Ran on one file                                                                                                                                                                         |
| Detector | 5.3    | Yes     | Findings and a summary in the command's output; exit 14 on a high finding (ran)                                                                                                         |
| Detector | 5.4    | Yes     | Offline audits need nothing; online audits run locally with a GitHub token ([usage](https://github.com/zizmorcore/zizmor/blob/v1.30.1/docs/usage.md))                                   |
| Detector | 6.1    | Partial | Printed `https://docs.zizmor.sh/audits/#<id>` resolves all 41 ids (checked against [`audits.md`](https://github.com/zizmorcore/zizmor/blob/v1.30.1/docs/audits.md)); not the SARIF form |
| Detector | 6.2    | No      | The mechanism is a website                                                                                                                                                              |
| Detector | 6.3    | No      | No documentation in the wheel or binary (wheel `RECORD`)                                                                                                                                |
| Detector | 6.4    | No      | CI checks the configuration schema, not documentation ([`ci.yml`](https://github.com/zizmorcore/zizmor/blob/v1.30.1/.github/workflows/ci.yml))                                          |
| Detector | 7.1    | Yes     | Ignore comments and `rules.<id>.ignore` are counted as ignored and closed by `--no-ignores` (ran)                                                                                       |
| Detector | 7.2    | No      | A trailing explanation is optional ([usage](https://github.com/zizmorcore/zizmor/blob/v1.30.1/docs/usage.md))                                                                           |

## Notes for a practitioner

Run zizmor for its audits with `--no-ignores` in the enforced invocation if the project forbids ignores, or with ignores honoured and the summary's ignored count watched if it allows them, and give a token where the online audits matter. Read `plain` or `json` output when the id matters, and strip the `zizmor/` prefix from SARIF before looking an id up. Pass `--strict-collection`, so that a workflow that fails to parse fails the run rather than vanishing from it, and do not gate on the exit code of a SARIF run. A project's own workflow rule belongs in a host that takes one, such as actionlint's library or [Semgrep](semgrep.md) with its YAML support.

## Attributes

| Attribute      | Value                                                                                                                       | Source                                                                        |
| -------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Kind           | Detector                                                                                                                    | ran                                                                           |
| Depth          | Syntactic, with `${{ }}` expressions parsed; online audits add facts from the GitHub API                                    | [`crates/`](https://github.com/zizmorcore/zizmor/tree/v1.30.1/crates), ran    |
| Output formats | `plain`, `json` (v1), `sarif` (native) and `github`                                                                         | `--help`, ran                                                                 |
| Exit codes     | 11 to 14 by highest severity; 0 under SARIF or `--no-exit-codes`; 1 on an error; 2 on a usage error; 3 when no input parsed | [usage](https://github.com/zizmorcore/zizmor/blob/v1.30.1/docs/usage.md), ran |
| Fix mode       | `--fix=safe`, `unsafe-only` or `all`, keeping unsafe fixes apart                                                            | `--help`                                                                      |
| Unused ignores | Not reported: an ignore comment that suppressed nothing passed with exit 0                                                  | ran                                                                           |
| Licence        | MIT                                                                                                                         | [LICENSE](https://github.com/zizmorcore/zizmor/blob/v1.30.1/LICENSE)          |
