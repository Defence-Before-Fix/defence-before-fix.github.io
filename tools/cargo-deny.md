---
title: cargo-deny and Defence Before Fix
summary: Dependency auditor with fixed checks so 4.1 fails; per-check runs leave 4.2 and 5.2 partial; website-only codes fail 6.2
language: Rust
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-09-08, version 0.20.2
---

# cargo-deny

{% include tool-grades.html %}

cargo-deny is a dependency auditor rather than a code linter. It reads the Cargo lock file and checks the dependency graph for security advisories, licence compliance, banned or duplicated crates and untrusted sources, driven by a `deny.toml` in the project ([configuration](https://embarkstudios.github.io/cargo-deny/checks/cfg.html)). In a pipeline it runs beside Clippy as the check on what the project depends on rather than what it wrote. It does not read source code, so a bespoke defence in the method's sense cannot be hosted in it, and readiness is graded on that fact.

## How it is conformant

cargo-deny runs locally, with `--offline` and `--disable-fetch` documented for a run without network access ([common options](https://embarkstudios.github.io/cargo-deny/cli/common.html)), and prints its diagnostics in the command's own output with an exit code that encodes which checks failed ([check](https://embarkstudios.github.io/cargo-deny/cli/check.html)), meeting [5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure), [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran) and [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally). Every diagnostic carries a stable code such as `vulnerability`, `unmaintained` or `yanked`, documented per check ([advisory diagnostics](https://embarkstudios.github.io/cargo-deny/checks/advisories/diags.html)) and printed in the text and JSON formats, and those codes can be individually raised or lowered with `-A`, `-W` and `-D` ([4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding), for bundled codes). Clause [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) holds by omission: there is no inline suppression route, and an `ignore` entry in `deny.toml` is a configuration record rather than a comment in code.

## How it is not conformant

Clause [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it) is failed: the checks are the four built-in types and the configuration page offers no way to add one, so [4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own) does not apply. Graded on its bundled checks, [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code) is partial: `cargo deny check advisories` runs one check type alone against a fixture workspace, but a single diagnostic code cannot be isolated other than by lowering every other code with `-A`, and the unit is always the whole dependency graph, which is also why [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file) is partial. Section [6](../DETECTOR-SPEC.md#6-resolving-an-identifier) fails for bundled codes: they are documented on the website keyed on the code ([6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation) partial), and no command resolves a printed code from the installed binary ([6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)), so the documentation does not ship with the check ([6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)). The `reason` on an `ignore` entry is "entirely optional and serves as documentation" ([advisories configuration](https://embarkstudios.github.io/cargo-deny/checks/advisories/cfg.html)), so the nearest thing to a suppression carries no required sentence ([7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)).

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                        |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| Detector | [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)    | No           | Four fixed check types ([configuration](https://embarkstudios.github.io/cargo-deny/checks/cfg.html))                            |
| Detector | [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)    | Partial      | Bundled checks: one check type per run ([check](https://embarkstudios.github.io/cargo-deny/cli/check.html)); no single-code run |
| Detector | [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)    | Yes          | Codes stable, documented and printed ([diagnostics](https://embarkstudios.github.io/cargo-deny/checks/advisories/diags.html))   |
| Detector | [4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own)    | No           | None                                                                                                                            |
| Detector | [5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure)    | Yes          | `cargo deny check` locally, `--offline` supported                                                                               |
| Detector | [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file)    | Partial      | Per check type, not per file; the graph is the unit                                                                             |
| Detector | [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)    | Yes          | Diagnostics printed with codes ([check](https://embarkstudios.github.io/cargo-deny/cli/check.html))                             |
| Detector | [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)    | Yes          | All checks runnable locally                                                                                                     |
| Detector | [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)    | Partial      | Website pages keyed on code                                                                                                     |
| Detector | [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)    | No           | No offline resolver                                                                                                             |
| Detector | [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)    | No           | Documentation on the website only                                                                                               |
| Detector | [6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation)    | Not verified | No release gate documented                                                                                                      |
| Detector | [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)    | Yes          | No inline suppression route exists; `ignore` lives in `deny.toml`                                                               |
| Detector | [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)    | No           | `reason` optional ([advisories cfg](https://embarkstudios.github.io/cargo-deny/checks/advisories/cfg.html))                     |

## Notes for a practitioner

cargo-deny is the right instrument when the class is "a dependency with property X", and a `bans.deny` or `licenses` entry in `deny.toml` is a legitimate off-the-shelf rule under method clause [3.2](../SPEC.md#32-build-the-net), proven by adding the offending crate to a fixture workspace. Fill the `reason` field on every `ignore` entry with the hazard and scope even though the tool does not insist, and review `deny.toml` as the project's exception record.
