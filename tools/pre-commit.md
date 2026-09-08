---
title: pre-commit and Defence Before Fix
summary: Local hooks with a printed id meet 4.1, 4.3 and section 5; no id resolution for 6.1; no listing for 7.1; SKIP fails 8.3
---

# pre-commit

**Language**: Multi-language · **Kind**: tool · **Readiness**: 🟢 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 4.6.2

pre-commit is a framework for managing git hooks. It installs each hook's language runtime in an isolated environment, runs the hooks over staged files at commit time, and can run them over the whole repository on demand. It detects nothing itself; it is assessed here as a host for defences, the place a project registers the detectors it wants run, and its grades describe what the host adds to or withholds from whatever runs inside it.

## How it is conformant

A project-authored hook is first class (4.1): `repo: local` hooks are declared in `.pre-commit-config.yaml` with an `id`, `name`, `language` and `entry`, and the `pygrep` language turns a single regular expression into a blocking hook with no code at all ([repository local hooks](https://pre-commit.com/#repository-local-hooks), [pygrep](https://pre-commit.com/#pygrep)). A single hook can be run against a single file with `pre-commit run <hook-id> --files <path>` ([pre-commit run](https://pre-commit.com/#pre-commit-run)), which covers 4.2 in the minimal sense of running one defence in isolation, and 5.2. The `id` is required, chosen by the author, and printed on failure as `- hook id: <id>` together with the exit code ([usage](https://pre-commit.com/#usage)), so 4.3 holds for the hook identifier. Everything runs locally; remote hook repositories are cloned once and local hooks need no network ([install-hooks](https://pre-commit.com/#pre-commit-install-hooks)), meeting 5.1 and 5.4. A failing hook's stdout and stderr are shown in the command output, and `verbose: true` shows them always ([verbose](https://pre-commit.com/#config-verbose)), meeting 5.3. The `.pre-commit-config.yaml` file is the active configuration, and the project's own hooks sit in it beside third-party ones, which is the substance of 7.2 and 7.3. The project runs pre-commit on itself through `tox` and pre-commit.ci ([tox.ini](https://github.com/pre-commit/pre-commit/blob/main/tox.ini)).

## How it is not conformant

There is no proving harness (4.2 in full): `try-repo` exercises a hook repository, but nothing asserts that a hook fails on a fixture ([try-repo](https://pre-commit.com/#pre-commit-try-repo)), so the red run is the practitioner's own manual invocation. Clause 6.1 is failed outright: the `description` field of a hook is "used for metadata purposes only" ([hooks description](https://pre-commit.com/#hooks-description)) and no command displays it or resolves a hook id to anything. Clause 7.1 is failed: there is no listing command, only `validate-config` ([validate-config](https://pre-commit.com/#pre-commit-validate-config)); the configuration file can be read by hand, but it carries no route to documentation. Section 8 is failed structurally: the `SKIP` environment variable disables any hook by id with no reason recorded, `git commit --no-verify` bypasses the framework entirely, and `exclude` is a bare regular expression ([temporarily disabling hooks](https://pre-commit.com/#temporarily-disabling-hooks)); pre-commit cannot defend against any of these because they act before it runs, which is why a host alone can never satisfy 8.3. Clauses 6.3, 10.1 and 10.2 concern bundled defences, and pre-commit bundles none; the separate `pre-commit-hooks` repository is a hook collection, not part of the framework. No method specification version is declared (11.1).

## Clause by clause

| Clause | Result         | Evidence                                                                                                              |
| ------ | -------------- | --------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes            | `repo: local` and `pygrep` ([local hooks](https://pre-commit.com/#repository-local-hooks))                            |
| 4.2    | Partial        | `run <id> --files` isolates a hook; no fixture assertion ([run](https://pre-commit.com/#pre-commit-run))              |
| 4.3    | Yes            | Required `id`, printed as `- hook id:` on failure ([usage](https://pre-commit.com/#usage))                            |
| 4.4    | No             | No rule over the hooks                                                                                                |
| 5.1    | Yes            | Local hooks need no network ([install-hooks](https://pre-commit.com/#pre-commit-install-hooks))                       |
| 5.2    | Yes            | `--files` and `--all-files` ([run](https://pre-commit.com/#pre-commit-run))                                           |
| 5.3    | Yes            | Hook output shown on failure ([verbose](https://pre-commit.com/#config-verbose))                                      |
| 5.4    | Yes            | Every hook runs locally                                                                                               |
| 6.1    | No             | `description` is metadata only ([hooks description](https://pre-commit.com/#hooks-description))                       |
| 6.2    | No             | No resolver exists                                                                                                    |
| 6.3    | Not applicable | No bundled defences                                                                                                   |
| 7.1    | No             | No listing command ([validate-config](https://pre-commit.com/#pre-commit-validate-config))                            |
| 7.2    | Partial        | The config file is the active configuration, readable but not a listing                                               |
| 7.3    | Partial        | Local and remote hooks share the file                                                                                 |
| 8.1    | No             | No project record beyond `exclude` patterns                                                                           |
| 8.2    | No             | `SKIP` and `exclude` take no reason ([disabling hooks](https://pre-commit.com/#temporarily-disabling-hooks))          |
| 8.3    | No             | `SKIP` and `--no-verify` cannot be prevented                                                                          |
| 8.4    | No             | No enumeration of exceptions                                                                                          |
| 8.5    | Partial        | Defaults for `stages` and `fail_fast` documented ([fail_fast](https://pre-commit.com/#top_level-fail_fast))           |
| 9.1    | No             | No agent summary                                                                                                      |
| 9.2    | No             | No delivery mechanism                                                                                                 |
| 10.1   | Not applicable | No bundled defences                                                                                                   |
| 10.2   | Yes            | Runs its own config via tox and pre-commit.ci ([tox.ini](https://github.com/pre-commit/pre-commit/blob/main/tox.ini)) |
| 11.1   | No             | No declaration                                                                                                        |

## Notes for a practitioner

Use pre-commit as the entry point clause 3.5 of the method asks you to demonstrate through, and put the detector that carries the rule inside a `repo: local` hook whose `id` is the rule's identifier. Prove the rule red by running that hook alone with `--files` on the offending file, and sweep with `--all-files`. Nothing here resolves an identifier or records an exception, so keep a `docs/rules/<id>.md` file per hook and treat `SKIP` and `--no-verify` as forbidden in CI, where the same hooks must run again without a git hook to bypass.
