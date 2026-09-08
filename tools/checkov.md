---
title: Checkov and Defence Before Fix
summary: Custom Python and YAML policies with printed ids meet 4.1, 4.3 and section 5; online-only Guide links fail 6.2; inline skips and baselines fail 8.3
---

# Checkov

**Language**: Multi-language · **Kind**: tool · **Readiness**: 🟢 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 3.3.16

Checkov is a policy-as-code scanner for infrastructure definitions: Terraform, CloudFormation, Kubernetes, Helm, Dockerfiles, GitHub Actions and others. It ships a large catalogue of checks with identifiers such as `CKV_AWS_20` and is maintained by Palo Alto Networks as the open-source engine behind Prisma Cloud. In a pipeline it runs against the infrastructure directory before plan or apply, and its custom policies are the route by which a project's own infrastructure conventions become blocking checks.

## How it is conformant

Bespoke checks are first class (4.1) in two forms: a Python class extending the check base classes, or a YAML policy of attribute and connection conditions, both loaded with `--external-checks-dir` ([Python custom policies](https://www.checkov.io/3.Custom%20Policies/Python%20Custom%20Policies.html), [YAML custom policies](https://www.checkov.io/3.Custom%20Policies/YAML%20Custom%20Policies.html)). The author sets the `id` and it is printed with every finding, in the terminal output and in JSON, SARIF, JUnit, CSV and GitLab formats ([CLI reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html)), satisfying 4.3 and 5.3. A single check runs against a single file with `checkov -f <file> --check <id>` together with the external checks directory, which covers the isolation clause 4.2 asks for and 5.2 outright; the Python documentation walks through running a new check against a sample file to see it fail, which is the red run, though no fixture assertion harness is offered beyond writing your own unit test. The core scanner needs no API key (5.1): with `--skip-download` it makes no network call at all, at the cost of omitting the "Guide" links and severities the platform supplies ([CLI reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html)). `checkov --list` enumerates the checks with identifier, name, resource type and framework without running them, which is the shape of 7.1 for the bundled catalogue.

## How it is not conformant

Resolution is online only (6.1, 6.2, 6.3): each finding prints a "Guide" URL fetched from Prisma Cloud at run time, and a custom policy's optional `guideline` field is likewise a URL ([YAML custom policies](https://www.checkov.io/3.Custom%20Policies/YAML%20Custom%20Policies.html)); nothing on disk resolves `CKV_AWS_20` to its documentation, and with `--skip-download` the links vanish altogether. The listing is partial (7.1, 7.3): `--list` describes the built-in catalogue and, on reading the release source, returns before external checks are loaded, so a project's own checks are absent, and it does not reflect `--check` or `--skip-check` filters; the second point is not verified from documentation. Section 8 is failed structurally: the inline `checkov:skip=<id>:<comment>` form makes the comment optional ([suppressing policies](https://www.checkov.io/2.Basics/Suppressing%20and%20Skipping%20Policies.html)), `--skip-check` and the configuration file take no reason, no option disables inline skips, and `--create-baseline` writes a `.checkov.baseline` so that "future runs will not re-flag the same noise" ([CLI reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html)), which is the silent baseline clause 8.3 names. No project record is read with justifications (8.1, 8.2) and no method specification version is declared (11.1).

## Clause by clause

| Clause | Result       | Evidence                                                                                                                                       |
| ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | `--external-checks-dir` Python and YAML ([Python custom policies](https://www.checkov.io/3.Custom%20Policies/Python%20Custom%20Policies.html)) |
| 4.2    | Partial      | `-f <file> --check <id>` isolates a check; no fixture harness                                                                                  |
| 4.3    | Yes          | Author-set `id`, printed on every finding ([YAML custom policies](https://www.checkov.io/3.Custom%20Policies/YAML%20Custom%20Policies.html))   |
| 4.4    | No           | No rule over the checks                                                                                                                        |
| 5.1    | Yes          | `--skip-download` runs with no network ([CLI reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html))                       |
| 5.2    | Yes          | `-f <file>` ([CLI reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html))                                                  |
| 5.3    | Yes          | `-o cli`, `json`, `sarif`, `junitxml`, `csv`, `gitlab_sast`                                                                                    |
| 5.4    | Partial      | Platform policies and severity filters need an API key                                                                                         |
| 6.1    | Partial      | "Guide" URL per finding; nothing keyed offline                                                                                                 |
| 6.2    | No           | Links fetched from Prisma Cloud; gone with `--skip-download`                                                                                   |
| 6.3    | No           | Bundled check documentation lives online                                                                                                       |
| 7.1    | Partial      | `--list` shows built-in checks only ([CLI reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html))                          |
| 7.2    | Partial      | Not verified to reflect `--check`/`--skip-check`                                                                                               |
| 7.3    | No           | External checks absent from `--list`                                                                                                           |
| 8.1    | No           | `.checkov.yaml` holds skips, not justified exceptions                                                                                          |
| 8.2    | No           | Skip comment optional ([suppressing policies](https://www.checkov.io/2.Basics/Suppressing%20and%20Skipping%20Policies.html))                   |
| 8.3    | No           | Inline skips cannot be disabled; `--create-baseline` exists                                                                                    |
| 8.4    | No           | No enumeration of exceptions with the checks                                                                                                   |
| 8.5    | Partial      | Default check set and severities documented                                                                                                    |
| 9.1    | No           | No agent summary                                                                                                                               |
| 9.2    | No           | No delivery mechanism                                                                                                                          |
| 10.1   | Not verified | No documented release gate on check documentation                                                                                              |
| 10.2   | Partial      | Repository runs pytest over its checks; running checkov on itself not verified                                                                 |
| 11.1   | No           | No declaration                                                                                                                                 |

## Notes for a practitioner

Checkov will run the six clauses for infrastructure code: write the check under `--external-checks-dir`, prove it red with `-f` on the offending file, sweep with `-d` over the whole infrastructure tree, and let the non-zero exit block. Run with `--skip-download` in the project entry point so the result is reproducible offline, keep a markdown file per identifier in the repository because the printed Guide link will not be there, and add a second check that fails on any `checkov:skip` comment whose reason is empty, since the tool accepts one without.
