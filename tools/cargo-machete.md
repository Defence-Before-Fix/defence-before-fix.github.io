---
title: cargo-machete and Defence Before Fix
summary: One fixed check for unused dependencies, so 4.1 fails; findings carry no identifier, failing 4.3 and leaving section 6 with nothing to resolve; the ignored list cannot be switched off or listed, failing 7.1
language: Rust
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-10-10, version 0.9.2
---

# cargo-machete

{% include tool-grades.html %}

cargo-machete finds dependencies a Cargo manifest declares that the crate's source never uses. It describes itself as finding them "in a fast yet imprecise way" (`cargo machete --help`, ran): for each dependency it searches the crate's Rust files with regular expressions for the crate name in a `use`, a path or an `extern crate` ([`search_unused.rs` at v0.9.2](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/src/search_unused.rs)), without compiling anything unless `--with-metadata` asks it to call `cargo metadata`. In a pipeline it sits beside cargo-deny as a check on the manifest rather than on the code. It has one check and no way to add another, so it cannot host a bespoke defence.

## How it is conformant

The reporting clauses are met. `cargo machete` runs locally with no infrastructure, over every manifest under the paths it is given ([README at v0.9.2](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/README.md)), and prints each finding to the command's own output, the crate, its manifest path and the unused dependency's name, followed by advice on the `ignored` list (ran, 0.9.2), which meets 5.1, 5.3 and 5.4. Graded on its one bundled check, 4.2 is met: run against a fixture crate whose manifest declared `serde` and whose source never named it, version 0.9.2 printed `serde` under `a -- a/Cargo.toml:` and exited 1, with no other check to obscure the answer and no test suite run.

## How it is not conformant

Clause 4.1 fails: the check is built in ([`main.rs` at v0.9.2](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/src/main.rs)), and the only configuration is the `ignored` and `renamed` tables in `package.metadata.cargo-machete` or `workspace.metadata.cargo-machete` ([README](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/README.md)), which change what the one check reports rather than adding a pattern. Clause 4.3 fails: a finding is a dependency name under a manifest path, with no identifier of any kind, in the only output format there is (ran). With nothing printed to key a lookup on, section 6 has nothing to resolve, and 6.1, 6.2 and 6.3 are No. Clause 5.2 is partial: a path argument is walked for `Cargo.toml` files, so one manifest can be checked alone (`cargo machete a/Cargo.toml` reported the same finding, ran), but the unit is the crate, and a source file given alone found no manifest and printed "didn't find any unused dependencies ... Good job!" with exit 0 (ran).

Clause 7.1 fails. The `ignored` list is the suppression route: a dependency named in it is not reported when unused, no flag or setting stops the list from being applied, and no output lists or counts what it suppressed ([`search_unused.rs`](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/src/search_unused.rs)). The one report touching it is a warning, `log was marked as ignored, but is actually used!`, printed to standard error for a package-level entry that suppresses nothing; it reports a stale entry, not a suppression in force, and version 0.9.2 printed it only when the same crate also had an unused dependency: a crate whose only finding would have been the stale entry printed "Good job!" and exited 0, and a stale entry in `workspace.metadata.cargo-machete` was never reported (ran; the warning is printed inside the loop over crates with findings, [`main.rs`](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/src/main.rs)). Under reading 18 the route is not detectable, since reporting an entry that suppresses nothing does not show what the list suppresses, and a project cannot write a rule in cargo-machete to see it. Clause 7.2 fails: an `ignored` entry is a bare crate name, and the README's reason is a TOML comment the tool neither reads nor requires.

Four behaviours a defence routed through cargo-machete should know of, recorded under reading 9. By default the walk honours `.gitignore` and `.ignore` files, so a crate under an ignored directory is not examined and the run says "Good job!" and exits 0; `--no-ignore` turns that off (ran). A manifest that is not valid TOML printed `error when handling f/Cargo.toml: TOML parse error` and the run still exited 0 with "Good job!" (ran). A Rust source file that does not parse is searched as text all the same: a crate whose only source was `pub fn f( {{{ serde::x` counted `serde` as used and exited 0 with no error (ran). A usage error such as an unknown flag exited 1, the same code as a finding, although the help text gives 2 for an error; a path that does not exist exited 2 (ran).

The detector grade is 🔴 on 4.1 and 4.3, both structural under reading 1, with 5.2 partial and 6.1, 6.2, 6.3, 7.1 and 7.2 failing. Readiness is 🔴: no bespoke rules and no identifier on findings.

## Clause by clause

| Document | Clause | Result         | Evidence                                                                                                                                                                                                                       |
| -------- | ------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Detector | 4.1    | No             | One built-in check; `ignored` and `renamed` only adjust it ([README](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/README.md))                                                                                           |
| Detector | 4.2    | Yes            | Bundled check: a fixture crate gave the one finding alone, exit 1 (ran, 0.9.2)                                                                                                                                                 |
| Detector | 4.3    | No             | A finding is a dependency name under a manifest path; no identifier (ran)                                                                                                                                                      |
| Detector | 4.4    | Not applicable | No rules to enforce an identifier on                                                                                                                                                                                           |
| Detector | 5.1    | Yes            | `cargo machete` locally ([README](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/README.md))                                                                                                                              |
| Detector | 5.2    | Partial        | One manifest path checks one crate; a source file alone finds no manifest and exits 0 (ran)                                                                                                                                    |
| Detector | 5.3    | Yes            | Findings printed in the command's output (ran)                                                                                                                                                                                 |
| Detector | 5.4    | Yes            | Same everywhere                                                                                                                                                                                                                |
| Detector | 6.1    | No             | Nothing to resolve                                                                                                                                                                                                             |
| Detector | 6.2    | No             | Same                                                                                                                                                                                                                           |
| Detector | 6.3    | No             | Same                                                                                                                                                                                                                           |
| Detector | 6.4    | Not applicable | No identifiers to document                                                                                                                                                                                                     |
| Detector | 7.1    | No             | `ignored` has no switch and is never listed; a stale package entry is warned of only beside another finding, a stale workspace entry never (ran; [`main.rs`](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/src/main.rs)) |
| Detector | 7.2    | No             | An `ignored` entry is a bare name; no reason field                                                                                                                                                                             |

## Notes for a practitioner

cargo-machete is a quick lexical check, useful as an off-the-shelf rule under method clause 3.2 when the class is "a dependency declared and never used", proven by adding an unused dependency to a fixture crate. It cannot carry a defence of the project's own. Run it with `--no-ignore` where any crate might sit under an ignored directory, check that the output names every crate you expect rather than trusting exit 0, and treat a TOML parse error in its output as a failure, since the exit code will not. Keep every `ignored` entry beside a comment giving the reason, and review the list by hand, because the tool will not tell you what it is hiding. For an answer from the build rather than from text, rustc's allow-by-default `unused_crate_dependencies` lint, "crate dependencies that are never used" (`rustc -W help`, Rust 1.99.0), covers the same class.

## Attributes

| Attribute      | Value                                                                                          | Source                                                                                         |
| -------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Kind           | Dependency auditor                                                                             | [README](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/README.md)                        |
| Depth          | Lexical: regular expressions over source text                                                  | [`search_unused.rs`](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/src/search_unused.rs) |
| Output formats | Text only; no SARIF                                                                            | ran                                                                                            |
| Exit codes     | 0 clean, 1 finding, 2 error; 1 on a usage error; 0 on an unparseable manifest or source file   | ran                                                                                            |
| Report file    | No                                                                                             | [`main.rs`](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/src/main.rs)                   |
| Fix mode       | `--fix` removes every flagged dependency, false positives included; no safe and unsafe split   | ran (`--help`)                                                                                 |
| Baseline       | No                                                                                             | [README](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/README.md)                        |
| Unused ignores | In part: a package-level entry, and only beside another finding; never a workspace-level entry | ran                                                                                            |
| Rule listing   | No; one check                                                                                  | ran (`--help`)                                                                                 |
| Licence        | MIT                                                                                            | [README](https://github.com/bnjbvr/cargo-machete/blob/v0.9.2/README.md)                        |
