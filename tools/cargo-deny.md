---
title: cargo-deny and Defence Before Fix
summary: Dependency auditor with fixed checks so 4.1 fails; deny.toml is read for 8.1; reason optional so 8.2 fails
---

# cargo-deny

**Language**: Rust · **Kind**: tool · **Readiness**: 🔴 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 0.20.2

cargo-deny is a dependency auditor rather than a code linter. It reads the Cargo lock file and checks the dependency graph for security advisories, licence compliance, banned or duplicated crates and untrusted sources, driven by a `deny.toml` in the project ([configuration](https://embarkstudios.github.io/cargo-deny/checks/cfg.html)). In a pipeline it runs beside Clippy as the check on what the project depends on rather than what it wrote. It does not read source code, so a bespoke defence in the method's sense cannot be hosted in it, and readiness is graded on that fact.

## How it is conformant

cargo-deny runs locally, with `--offline` and `--disable-fetch` documented for a run without network access ([common options](https://embarkstudios.github.io/cargo-deny/cli/common.html)), and prints its diagnostics in the command's own output with an exit code that encodes which checks failed ([check](https://embarkstudios.github.io/cargo-deny/cli/check.html)), meeting 5.1, 5.3 and 5.4. Each check type can be run alone, `cargo deny check advisories`, which is the subset invocation of 5.2 in the only sense that applies to a graph. Every diagnostic carries a stable code such as `vulnerability`, `unmaintained` or `yanked`, documented per check ([advisory diagnostics](https://embarkstudios.github.io/cargo-deny/checks/advisories/diags.html)), and those codes can be individually raised or lowered with `-A`, `-W` and `-D` (4.3, for bundled codes). `deny.toml` is a project record the tool reads (8.1), and its `ignore` entries accept a `reason` field ([advisories configuration](https://embarkstudios.github.io/cargo-deny/checks/advisories/cfg.html)). Defaults for every setting are documented (8.5).

## How it is not conformant

Clause 4.1 is failed: the checks are the four built-in types and the configuration page offers no way to add one, so 4.2 and 4.4 do not apply. Clause 8.2 is failed: the `reason` on an ignore entry is "entirely optional and serves as documentation", so an exception without a justification is accepted. There is no inline suppression, so 8.3 is met by omission, but there is nothing that lists active checks with a terse statement and the `ignore` entries together as one operation (7.1, 8.4). Diagnostic codes are documented on the website, and no command resolves a printed code from the installed binary (6.1 partial, 6.2 not met). No version is declared (11.1).

## Clause by clause

| Clause | Result       | Evidence                                                                                                             |
| ------ | ------------ | -------------------------------------------------------------------------------------------------------------------- |
| 4.1    | No           | Four fixed check types ([configuration](https://embarkstudios.github.io/cargo-deny/checks/cfg.html))                 |
| 4.2    | No           | Not applicable                                                                                                       |
| 4.3    | Yes          | Codes stable and documented ([diagnostics](https://embarkstudios.github.io/cargo-deny/checks/advisories/diags.html)) |
| 4.4    | No           | None                                                                                                                 |
| 5.1    | Yes          | `cargo deny check` locally, `--offline` supported                                                                    |
| 5.2    | Partial      | Per check type, not per file; the graph is the unit                                                                  |
| 5.3    | Yes          | Diagnostics printed with codes ([check](https://embarkstudios.github.io/cargo-deny/cli/check.html))                  |
| 5.4    | Yes          | All checks runnable locally                                                                                          |
| 6.1    | Partial      | Website pages keyed on code                                                                                          |
| 6.2    | No           | No offline resolver                                                                                                  |
| 6.3    | No           | Documentation on the website only                                                                                    |
| 7.1    | No           | No listing with statements                                                                                           |
| 7.2    | No           | See 7.1                                                                                                              |
| 7.3    | No           | No project checks exist                                                                                              |
| 8.1    | Yes          | `deny.toml` is read by the tool                                                                                      |
| 8.2    | No           | `reason` optional ([advisories cfg](https://embarkstudios.github.io/cargo-deny/checks/advisories/cfg.html))          |
| 8.3    | Yes          | No inline suppression exists                                                                                         |
| 8.4    | No           | None                                                                                                                 |
| 8.5    | Yes          | Defaults documented                                                                                                  |
| 9.1    | No           | None                                                                                                                 |
| 9.2    | No           | None                                                                                                                 |
| 10.1   | Not verified | No release gate documented                                                                                           |
| 10.2   | Not verified | The project runs cargo-deny on itself; no release gate documented                                                    |
| 11.1   | No           | No declaration                                                                                                       |

## Notes for a practitioner

cargo-deny is the right instrument when the class is "a dependency with property X", and a `bans.deny` or `licenses` entry in `deny.toml` is a legitimate off-the-shelf rule under method clause 3.2, proven by adding the offending crate to a fixture workspace. Fill the `reason` field on every `ignore` entry with the hazard and scope even though the tool does not insist, and review `deny.toml` as the project's exception record.
