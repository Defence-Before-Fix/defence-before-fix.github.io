---
title: cargo-deny and Defence Before Fix
summary: Dependency auditor with fixed checks so 4.1 fails; per-check runs leave 4.2 and 5.2 partial; website-only codes fail 6.2
---

# cargo-deny

**Language**: Rust · **Kind**: tool · **Readiness**: 🔴 · **Detector conformance**: 🔴 · **Checked**: 2026-09-08, version 0.20.2

cargo-deny is a dependency auditor rather than a code linter. It reads the Cargo lock file and checks the dependency graph for security advisories, licence compliance, banned or duplicated crates and untrusted sources, driven by a `deny.toml` in the project ([configuration](https://embarkstudios.github.io/cargo-deny/checks/cfg.html)). In a pipeline it runs beside Clippy as the check on what the project depends on rather than what it wrote. It does not read source code, so a bespoke defence in the method's sense cannot be hosted in it, and readiness is graded on that fact.

## How it is conformant

cargo-deny runs locally, with `--offline` and `--disable-fetch` documented for a run without network access ([common options](https://embarkstudios.github.io/cargo-deny/cli/common.html)), and prints its diagnostics in the command's own output with an exit code that encodes which checks failed ([check](https://embarkstudios.github.io/cargo-deny/cli/check.html)), meeting 5.1, 5.3 and 5.4. Every diagnostic carries a stable code such as `vulnerability`, `unmaintained` or `yanked`, documented per check ([advisory diagnostics](https://embarkstudios.github.io/cargo-deny/checks/advisories/diags.html)) and printed in the text and JSON formats, and those codes can be individually raised or lowered with `-A`, `-W` and `-D` (4.3, for bundled codes). Clause 7.1 holds by omission: there is no inline suppression route, and an `ignore` entry in `deny.toml` is a configuration record rather than a comment in code.

## How it is not conformant

Clause 4.1 is failed: the checks are the four built-in types and the configuration page offers no way to add one, so 4.4 does not apply. Graded on its bundled checks, 4.2 is partial: `cargo deny check advisories` runs one check type alone against a fixture workspace, but a single diagnostic code cannot be isolated other than by lowering every other code with `-A`, and the unit is always the whole dependency graph, which is also why 5.2 is partial. Section 6 fails for bundled codes: they are documented on the website keyed on the code (6.1 partial), and no command resolves a printed code from the installed binary (6.2), so the documentation does not ship with the check (6.3). The `reason` on an `ignore` entry is "entirely optional and serves as documentation" ([advisories configuration](https://embarkstudios.github.io/cargo-deny/checks/advisories/cfg.html)), so the nearest thing to a suppression carries no required sentence (7.2).

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                        |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | No           | Four fixed check types ([configuration](https://embarkstudios.github.io/cargo-deny/checks/cfg.html))                            |
| Detector | 4.2    | Partial      | Bundled checks: one check type per run ([check](https://embarkstudios.github.io/cargo-deny/cli/check.html)); no single-code run |
| Detector | 4.3    | Yes          | Codes stable, documented and printed ([diagnostics](https://embarkstudios.github.io/cargo-deny/checks/advisories/diags.html))   |
| Detector | 4.4    | No           | None                                                                                                                            |
| Detector | 5.1    | Yes          | `cargo deny check` locally, `--offline` supported                                                                               |
| Detector | 5.2    | Partial      | Per check type, not per file; the graph is the unit                                                                             |
| Detector | 5.3    | Yes          | Diagnostics printed with codes ([check](https://embarkstudios.github.io/cargo-deny/cli/check.html))                             |
| Detector | 5.4    | Yes          | All checks runnable locally                                                                                                     |
| Detector | 6.1    | Partial      | Website pages keyed on code                                                                                                     |
| Detector | 6.2    | No           | No offline resolver                                                                                                             |
| Detector | 6.3    | No           | Documentation on the website only                                                                                               |
| Detector | 6.4    | Not verified | No release gate documented                                                                                                      |
| Detector | 7.1    | Yes          | No inline suppression route exists; `ignore` lives in `deny.toml`                                                               |
| Detector | 7.2    | No           | `reason` optional ([advisories cfg](https://embarkstudios.github.io/cargo-deny/checks/advisories/cfg.html))                     |

## Notes for a practitioner

cargo-deny is the right instrument when the class is "a dependency with property X", and a `bans.deny` or `licenses` entry in `deny.toml` is a legitimate off-the-shelf rule under method clause 3.2, proven by adding the offending crate to a fixture workspace. Fill the `reason` field on every `ignore` entry with the hazard and scope even though the tool does not insist, and review `deny.toml` as the project's exception record.
