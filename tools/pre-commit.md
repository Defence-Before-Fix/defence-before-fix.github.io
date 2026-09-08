---
title: pre-commit and Defence Before Fix
summary: A host, not a detector; local hooks run one at a time with a printed id meet sections 4 and 5, and it offers no inline route for 7.1
---

# pre-commit

**Language**: Multi-language · **Kind**: tool · **Readiness**: 🟢 · **Detector conformance**: 🟢 · **Checked**: 2026-09-08, version 4.6.2

pre-commit is a framework for managing git hooks. It installs each hook's language runtime in an isolated environment, runs the hooks over staged files at commit time, and can run them over the whole repository on demand. It detects nothing itself; it is assessed here as a host for defences, the place a project registers the detectors it wants run, and its grades describe what the host adds to or withholds from whatever runs inside it. A green grade here says nothing about the detectors it hosts, each of which is graded on its own page.

## How it is conformant

A project-authored hook is first class (4.1): `repo: local` hooks are declared in `.pre-commit-config.yaml` with an `id`, `name`, `language` and `entry`, and the `pygrep` language turns a single regular expression into a blocking hook with no code at all ([repository local hooks](https://pre-commit.com/#repository-local-hooks), [pygrep](https://pre-commit.com/#pygrep)). A single hook can be run against a single file with `pre-commit run <hook-id> --files <path>` ([pre-commit run](https://pre-commit.com/#pre-commit-run)), which is a harness as the detector specification defines one, one rule against supplied code with its output observed and no other hook running alongside (4.2), and it meets 5.2. The `id` is required, chosen by the author, and printed on failure as `- hook id: <id>` together with the exit code ([usage](https://pre-commit.com/#usage)); pre-commit offers no machine-readable format of its own, so that is every output it has, and 4.3 holds for the hook identifier. Everything runs locally with no hosted service or licence tier; remote hook repositories are cloned once and local hooks need no network ([install-hooks](https://pre-commit.com/#pre-commit-install-hooks)), meeting 5.1 and 5.4. A failing hook's stdout and stderr are shown in the command output, and `verbose: true` shows them always ([verbose](https://pre-commit.com/#config-verbose)), meeting 5.3. pre-commit bundles no rules, so what it owes under 6.1 is the identifier printed unaltered for the project's own hooks, which it does; 6.2, 6.3 and 6.4 have nothing to apply to. It ships no inline suppression route of any kind, no ignore comment, directive or baseline, so 7.1 is met as written.

## How it is not conformant

Only the SHOULD clauses are open, and one bypass deserves stating even though 7.1 does not reach it. There is no rule over the hooks (4.4), and no fixture assertion beyond the practitioner running the hook by hand ([try-repo](https://pre-commit.com/#pre-commit-try-repo) exercises a hook repository without asserting a red result). The `SKIP` environment variable disables any hook by id and `git commit --no-verify` bypasses the framework entirely ([temporarily disabling hooks](https://pre-commit.com/#temporarily-disabling-hooks)); neither is an inline route in the source, so neither is what 7.1 governs, and pre-commit cannot see them because they act before it runs. Since no route takes a reason, 7.2 has nothing to require. The `description` field of a hook is "used for metadata purposes only" ([hooks description](https://pre-commit.com/#hooks-description)) and no command displays it, so the lookup from a printed hook id to its documentation is left entirely to the project's toolchain, which is where the detector specification places it.

## Clause by clause

| Document | Clause | Result         | Evidence                                                                                                                                          |
| -------- | ------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Yes            | `repo: local` and `pygrep` ([local hooks](https://pre-commit.com/#repository-local-hooks))                                                        |
| Detector | 4.2    | Yes            | `run <id> --files` runs one hook against supplied files ([run](https://pre-commit.com/#pre-commit-run))                                           |
| Detector | 4.3    | Yes            | Required `id`, printed as `- hook id:` on failure ([usage](https://pre-commit.com/#usage))                                                        |
| Detector | 4.4    | No             | No rule over the hooks                                                                                                                            |
| Detector | 5.1    | Yes            | Local hooks need no network ([install-hooks](https://pre-commit.com/#pre-commit-install-hooks))                                                   |
| Detector | 5.2    | Yes            | `--files` and `--all-files` ([run](https://pre-commit.com/#pre-commit-run))                                                                       |
| Detector | 5.3    | Yes            | Hook output shown on failure ([verbose](https://pre-commit.com/#config-verbose))                                                                  |
| Detector | 5.4    | Yes            | Every hook runs locally                                                                                                                           |
| Detector | 6.1    | Yes            | No bundled rules; hook ids printed unaltered, which is what the clause asks of a detector for a project's own rule                                |
| Detector | 6.2    | Not applicable | No bundled rules                                                                                                                                  |
| Detector | 6.3    | Not applicable | No bundled rules                                                                                                                                  |
| Detector | 6.4    | Not applicable | No bundled rules                                                                                                                                  |
| Detector | 7.1    | Yes            | No inline route offered; `SKIP` and `--no-verify` act outside the source ([disabling hooks](https://pre-commit.com/#temporarily-disabling-hooks)) |
| Detector | 7.2    | Not applicable | No inline route to require a reason on                                                                                                            |

## Notes for a practitioner

Use pre-commit as the entry point clause 3.5 of the method asks you to demonstrate through, and put the detector that carries the rule inside a `repo: local` hook whose `id` is the rule's identifier. Prove the rule red by running that hook alone with `--files` on the offending file, and sweep with `--all-files`. Nothing here resolves an identifier or records an exception, so keep a `docs/rules/<id>.md` file per hook and treat `SKIP` and `--no-verify` as forbidden in CI, where the same hooks must run again without a git hook to bypass.
