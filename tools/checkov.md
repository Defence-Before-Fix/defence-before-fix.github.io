---
title: Checkov and Defence Before Fix
summary: Custom policies with printed ids meet sections 4 and 5; online-only Guide links fail 6.2 and 6.3; inline skips fail 7.1
---

# Checkov

**Language**: Multi-language · **Kind**: tool · **Readiness**: 🟢 · **Detector conformance**: 🔴 · **Checked**: 2026-09-08, version 3.3.16

Checkov is a policy-as-code scanner for infrastructure definitions: Terraform, CloudFormation, Kubernetes, Helm, Dockerfiles, GitHub Actions and others. It ships a large catalogue of checks with identifiers such as `CKV_AWS_20` and is maintained by Palo Alto Networks as the open-source engine behind Prisma Cloud. In a pipeline it runs against the infrastructure directory before plan or apply, and its custom policies are the route by which a project's own infrastructure conventions become blocking checks.

## How it is conformant

Bespoke checks are first class (4.1) in two forms: a Python class extending the check base classes, or a YAML policy of attribute and connection conditions, both loaded with `--external-checks-dir` ([Python custom policies](https://www.checkov.io/3.Custom%20Policies/Python%20Custom%20Policies.html), [YAML custom policies](https://www.checkov.io/3.Custom%20Policies/YAML%20Custom%20Policies.html)). The author sets the `id` and it is printed with every finding, in the terminal output and in JSON, SARIF, JUnit, CSV and GitLab formats ([CLI reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html)), satisfying 4.3 and 5.3. A single check runs against a single file with `checkov -f <file> --check <id>` together with the external checks directory, which is a harness in the sense the detector specification defines, one rule against supplied code with its findings observed and no other rule obscuring them (4.2), and it meets 5.2 outright; the Python documentation walks through running a new check against a sample file to see it fail, which is the red run. The core scanner needs no API key (5.1): with `--skip-download` it makes no network call at all, at the cost of omitting the "Guide" links and severities the platform supplies ([CLI reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html)). `checkov --list` enumerates the bundled checks with identifier, name, resource type and framework, and the published [policy index](https://www.checkov.io/5.Policy%20Index/all.html) is keyed on the identifier, which is the online half of 6.1 for the bundled catalogue.

## How it is not conformant

Clause 7.1 is failed, and it is the structural failure that decides the grade: the inline `checkov:skip=<id>:<comment>` form cannot be switched off by any documented option, and because custom checks see parsed resources rather than comments, the tool documents no rule or mechanical check by which a project could see the route being used ([suppressing policies](https://www.checkov.io/2.Basics/Suppressing%20and%20Skipping%20Policies.html)). The comment on a skip is optional, `--skip-check` and the configuration file take no reason, and `--create-baseline` writes a `.checkov.baseline` so that "future runs will not re-flag the same noise" with no reason per entry ([CLI reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html)), so 7.2 is not met either; the baseline at least is opt-in, since a run only honours it with `--baseline`. Resolution of a bundled check is online only: each finding prints a "Guide" URL fetched from Prisma Cloud at run time, a custom policy's optional `guideline` field is likewise a URL ([YAML custom policies](https://www.checkov.io/3.Custom%20Policies/YAML%20Custom%20Policies.html)), and nothing on disk resolves `CKV_AWS_20` to its documentation, so 6.2 and 6.3 are failed and with `--skip-download` the links vanish altogether. No release gate on check documentation is documented (6.4) and there is no rule over the checks (4.4). Platform policies and severity filtering are available only with a Prisma Cloud API key, so findings from that part of the catalogue exist only through a hosted service and 5.4 is partial.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                                                    |
| -------- | ------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Yes          | `--external-checks-dir` Python and YAML ([Python custom policies](https://www.checkov.io/3.Custom%20Policies/Python%20Custom%20Policies.html))                              |
| Detector | 4.2    | Yes          | `-f <file> --check <id>` runs one check against supplied code; no fixture assertion beyond a unit test                                                                      |
| Detector | 4.3    | Yes          | Author-set `id`, printed on every finding ([YAML custom policies](https://www.checkov.io/3.Custom%20Policies/YAML%20Custom%20Policies.html))                                |
| Detector | 4.4    | No           | No rule over the checks                                                                                                                                                     |
| Detector | 5.1    | Yes          | `--skip-download` runs with no network ([CLI reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html))                                                    |
| Detector | 5.2    | Yes          | `-f <file>` ([CLI reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html))                                                                               |
| Detector | 5.3    | Yes          | `-o cli`, `json`, `sarif`, `junitxml`, `csv`, `gitlab_sast`                                                                                                                 |
| Detector | 5.4    | Partial      | Platform policies and severity filters need an API key                                                                                                                      |
| Detector | 6.1    | Partial      | "Guide" URL per finding and the online [policy index](https://www.checkov.io/5.Policy%20Index/all.html); nothing keyed offline                                              |
| Detector | 6.2    | No           | Links fetched from Prisma Cloud; gone with `--skip-download`                                                                                                                |
| Detector | 6.3    | No           | Bundled check documentation lives online                                                                                                                                    |
| Detector | 6.4    | Not verified | No documented release gate on check documentation                                                                                                                           |
| Detector | 7.1    | No           | Inline skips cannot be disabled and no detecting check is documented ([suppressing policies](https://www.checkov.io/2.Basics/Suppressing%20and%20Skipping%20Policies.html)) |
| Detector | 7.2    | No           | Skip comment optional; baseline entries carry no reason                                                                                                                     |

## Notes for a practitioner

Checkov will run the six clauses for infrastructure code: write the check under `--external-checks-dir`, prove it red with `-f` on the offending file, sweep with `-d` over the whole infrastructure tree, and let the non-zero exit block. Run with `--skip-download` in the project entry point so the result is reproducible offline, keep a markdown file per identifier in the repository because the printed Guide link will not be there, and add a separate check outside Checkov, a grep in the same entry point will do, that fails on any `checkov:skip` comment, since the tool can neither disable them nor see them.
