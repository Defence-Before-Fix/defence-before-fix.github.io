---
title: Clippy and Defence Before Fix
summary: Lints only by upstream contribution so 4.1 fails; explain command not verified for 6.2; fails 8.3 on allow attributes
---

# Clippy

**Language**: Rust · **Kind**: tool · **Readiness**: 🔴 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version Rust 1.98.1

Clippy is the official Rust linter, shipped as a rustup component and run as `cargo clippy`. It carries over eight hundred lints with names such as `clippy::needless_return`, grouped by level, and it is the single lint step in almost every Rust pipeline. It is a fixed catalogue: lints are added by contributing to the Clippy repository, and a project cannot register its own.

## How it is conformant

Clippy meets the reporting clauses. `cargo clippy` runs locally with no infrastructure and over one package with `-p` ([usage](https://doc.rust-lang.org/clippy/usage.html)), and every finding is printed in the command's own output with its lint name, which meets 5.1, 5.3 and 5.4. Lint names are stable identifiers documented in the [lint list](https://rust-lang.github.io/rust-clippy/master/index.html), which meets 4.3 for the bundled lints. A single lint can be run by allowing all and warning one, `cargo clippy -- -A clippy::all -W clippy::useless_format` ([configuration](https://doc.rust-lang.org/clippy/configuration.html)). The `[lints.clippy]` table in `Cargo.toml` and `clippy.toml` are project records the tool reads (8.1 partial), and the default levels of every lint are documented (8.5). Two restriction lints, `allow_attributes` and `allow_attributes_without_reason`, exist to defend against unreasoned suppression, and the second demands a `reason` on every `#[allow]`, which is the closest any tool in this register comes to clause 8.2's requirement.

## How it is not conformant

Clause 4.1 is failed: the [adding lints](https://doc.rust-lang.org/clippy/development/adding_lints.html) guide is entirely about contributing to the Clippy repository, and no documentation offers a route for a consuming project to write a lint of its own. The [dylint](https://github.com/trailofbits/dylint) project exists precisely because Clippy "runs a predetermined, static set of lints", and a project that adopts it is using a different toolchain. Clause 8.3 is failed: `#[allow(clippy::...)]` is inline suppression, the documentation recommends "a generous sprinkling" of it, and the two defending lints are allow-by-default. Clause 5.2 is partial, since the unit of invocation is the crate rather than a single file. Clause 6.1 is partial: the lint list on the website is keyed on the exact name, but whether `cargo clippy --explain <lint>` resolves it from the installed toolchain was not verified from the official documentation, so 6.2 is not verified either. Nothing enumerates active lints with a terse statement (7.1), and no version is declared (11.1).

## Clause by clause

| Clause | Result       | Evidence                                                                                                     |
| ------ | ------------ | ------------------------------------------------------------------------------------------------------------ |
| 4.1    | No           | [Adding lints](https://doc.rust-lang.org/clippy/development/adding_lints.html) is upstream contribution only |
| 4.2    | No           | Not applicable                                                                                               |
| 4.3    | Yes          | Bundled names stable and printed ([lint list](https://rust-lang.github.io/rust-clippy/master/index.html))    |
| 4.4    | No           | None                                                                                                         |
| 5.1    | Yes          | `cargo clippy` locally ([usage](https://doc.rust-lang.org/clippy/usage.html))                                |
| 5.2    | Partial      | Per crate with `-p`, not per file                                                                            |
| 5.3    | Yes          | Findings printed with lint name                                                                              |
| 5.4    | Yes          | `-A clippy::all -W <lint>`                                                                                   |
| 6.1    | Partial      | Website list keyed on name; `--explain` not verified                                                         |
| 6.2    | Not verified | See 6.1                                                                                                      |
| 6.3    | Partial      | Docs generated from lint source; delivery offline not verified                                               |
| 7.1    | No           | No listing of active lints with statements                                                                   |
| 7.2    | No           | See 7.1                                                                                                      |
| 7.3    | No           | No project lints exist                                                                                       |
| 8.1    | Partial      | `[lints.clippy]` and `clippy.toml` read, without justification                                               |
| 8.2    | Partial      | `allow_attributes_without_reason` exists but is allow-by-default                                             |
| 8.3    | No           | `#[allow(clippy::...)]` inline                                                                               |
| 8.4    | No           | None                                                                                                         |
| 8.5    | Yes          | Default levels documented                                                                                    |
| 9.1    | No           | None                                                                                                         |
| 9.2    | No           | None                                                                                                         |
| 10.1   | Not verified | Lint list is generated from source; no release gate documented                                               |
| 10.2   | Not verified | Clippy runs on itself; no release gate documented                                                            |
| 11.1   | No           | No declaration                                                                                               |

## Notes for a practitioner

Clippy can carry an off-the-shelf defence, and raising a lint to `deny` in `[lints.clippy]` is a recorded, proven change, but it cannot host a bespoke one; for that, dylint is the ecosystem's answer and should be graded on its own. Whichever you use, set `allow_attributes_without_reason` to `deny` so every suppression carries a reason, and prefer `#[expect]` so a suppression that stops firing is reported.
