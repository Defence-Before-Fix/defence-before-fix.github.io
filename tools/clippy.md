---
title: Clippy and Defence Before Fix
summary: Lints only by upstream contribution so 4.1 fails; allow_attributes lints meet 7.1 and 7.2; offline resolution for 6.2 not verified
---

# Clippy

**Language**: Rust · **Kind**: tool · **Readiness**: 🔴 · **Detector conformance**: 🔴 · **Checked**: 2026-09-08, version Rust 1.98.1

Clippy is the official Rust linter, shipped as a rustup component and run as `cargo clippy`. It carries over eight hundred lints with names such as `clippy::needless_return`, grouped by level, and it is the single lint step in almost every Rust pipeline. It is a fixed catalogue: lints are added by contributing to the Clippy repository, and a project cannot register its own.

## How it is conformant

Clippy meets the reporting clauses. `cargo clippy` runs locally with no infrastructure and over one package with `-p` ([usage](https://doc.rust-lang.org/clippy/usage.html)), and every finding is printed in the command's own output with its lint name, which meets 5.1, 5.3 and 5.4. Lint names are stable identifiers documented in the [lint list](https://rust-lang.github.io/rust-clippy/master/index.html), which meets 4.3 for the bundled lints. Because 4.1 fails, 4.2 is graded on the bundled lints, and `cargo clippy -- -A clippy::all -W clippy::useless_format` runs one lint against a crate with the rest silent ([configuration](https://doc.rust-lang.org/clippy/configuration.html)), which is a usable harness (4.2). Section 7 is met and met well: `#[allow(clippy::...)]` is the inline route, the bundled restriction lint `allow_attributes` detects every use of it, and `allow_attributes_without_reason` rejects one that carries no `reason`, so a project can forbid the route or demand a sentence on it by raising either lint to `deny` (7.1, 7.2).

## How it is not conformant

Clause 4.1 is failed: the [adding lints](https://doc.rust-lang.org/clippy/development/adding_lints.html) guide is entirely about contributing to the Clippy repository, and no documentation offers a route for a consuming project to write a lint of its own. The [dylint](https://github.com/trailofbits/dylint) project exists precisely because Clippy "runs a predetermined, static set of lints", and a project that adopts it is using a different detector. Clause 5.2 is partial, since the unit of invocation is the crate rather than a single file. Section 6 is not shown to hold: the lint list on the website is keyed on the exact name, but no official page documents a command that resolves a lint from the installed toolchain, so 6.1 is partial and 6.2 and 6.3 are not verified. The two defending lints are allow-by-default, so 7.2 is met by configuration rather than as shipped. No release gate over the generated lint list is documented (6.4, not verified).

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                    |
| -------- | ------ | ------------ | --------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | No           | [Adding lints](https://doc.rust-lang.org/clippy/development/adding_lints.html) is upstream contribution only                |
| Detector | 4.2    | Yes          | Bundled lints: `-A clippy::all -W <lint>` on a crate ([configuration](https://doc.rust-lang.org/clippy/configuration.html)) |
| Detector | 4.3    | Yes          | Bundled names stable and printed ([lint list](https://rust-lang.github.io/rust-clippy/master/index.html))                   |
| Detector | 4.4    | No           | None                                                                                                                        |
| Detector | 5.1    | Yes          | `cargo clippy` locally ([usage](https://doc.rust-lang.org/clippy/usage.html))                                               |
| Detector | 5.2    | Partial      | Per crate with `-p`, not per file                                                                                           |
| Detector | 5.3    | Yes          | Findings printed with lint name                                                                                             |
| Detector | 5.4    | Yes          | Every lint runnable locally                                                                                                 |
| Detector | 6.1    | Partial      | Website list keyed on name; no documented offline command                                                                   |
| Detector | 6.2    | Not verified | No official documentation of a `--explain` command found                                                                    |
| Detector | 6.3    | Not verified | Docs generated from lint source; offline delivery not documented                                                            |
| Detector | 6.4    | Not verified | Lint list is generated from source; no release gate documented                                                              |
| Detector | 7.1    | Yes          | `allow_attributes` restriction lint detects `#[allow]`                                                                      |
| Detector | 7.2    | Yes          | `allow_attributes_without_reason`, allow-by-default                                                                         |

## Notes for a practitioner

Clippy can carry an off-the-shelf defence, and raising a lint to `deny` in `[lints.clippy]` is a recorded, proven change, but it cannot host a bespoke one; for that, dylint is the ecosystem's answer and should be graded on its own. Whichever you use, set `allow_attributes_without_reason` to `deny` so every suppression carries a reason, and prefer `#[expect]` so a suppression that stops firing is reported.
