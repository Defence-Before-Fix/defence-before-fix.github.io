---
title: Shellharden and Defence Before Fix
summary: A quoting rewriter with no rules or identifiers fails 4.1, 4.2 and 4.3, and leaves nothing for section 6 to resolve; --check prints nothing at all, leaving 5.3 partial; no suppression route, so 7.1 holds
language: Shell
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-10-10, version 4.3.2
---

# Shellharden

{% include tool-grades.html %}

Shellharden is a syntax highlighter and rewriter for bash, written in Rust, that adds the quoting ShellCheck asks for: it parses a script and suggests, or applies, changes that stop word splitting and pathname expansion, such as `$foo` to `"$foo"`. By default it prints the script with its suggestions coloured in; `--suggest` prints a diff, `--transform` the rewritten script, `--replace` rewrites the file in place, and `--check` prints nothing and exits 2 when it would change something ([`--help`, from `main.rs`](https://github.com/anordal/shellharden/blob/v4.3.2/src/main.rs)). In a pipeline it sits where a formatter does, as a `--check` gate or a one-off `--replace`. It has one transformation and no rules, so it is graded here as a formatter is.

## How it is conformant

Shellharden runs locally, on one file or on standard input given as `''`, with nothing held back for a service or tier (5.1, 5.2, 5.4; ran, version 4.3.2). It has no suppression route: its source handles no ignore comment or directive ([`src/`](https://github.com/anordal/shellharden/tree/v4.3.2/src)), and a `# shellcheck disable=SC2086` comment above a line did not stop it suggesting quotes on that line (ran `--suggest`), so nothing hides a change (7.1).

## How it is not conformant

There are no rules. Shellharden applies one fixed rewrite, has no way to add a pattern, and has no option that selects a part of the rewrite ([README](https://github.com/anordal/shellharden/blob/v4.3.2/README.md), `--help`), so clauses 4.1 and 4.2 fail, and a suggested change carries no identifier in any mode (4.3). Clauses 6.1 to 6.3 have nothing to resolve, and 4.4 and 6.4 nothing to apply to; there is no inline route to require a reason on (7.2).

Clause 5.3 is partial. `--check`, the mode that fails on a suggestion, printed nothing at all and exited 2, not even the file name (ran), so with several files the practitioner learns only that one of them would change; the source stops at the first such file ([`main.rs`](https://github.com/anordal/shellharden/blob/v4.3.2/src/main.rs)). The modes that print the suggestion, the default and `--suggest`, exited 0 on a script they changed (ran), so they do not fail a check. The result reaches the practitioner only if they run the command twice.

A file Shellharden cannot parse is not told apart under `--check`: an unterminated quote exited 2 with no output, the same as a script it would rewrite, whilst `--suggest` printed `parse.bash: Unexpected end of file` and exited 1 (ran). Under reading 9 this is recorded, not graded. A bad option exited 3 and a missing file 1 (ran).

Readiness is 🔴 because there are no rules and no identifiers. The detector grade is 🔴 because 4.1, 4.2 and 4.3 fail, all structural under reading 1; 5.3 is partial. Shellharden declares no version of this document.

## Clause by clause

| Document | Clause | Result         | Evidence                                                                                                                             |
| -------- | ------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Detector | 4.1    | No             | One fixed rewrite; no way to add a pattern ([README](https://github.com/anordal/shellharden/blob/v4.3.2/README.md), `--help`)        |
| Detector | 4.2    | No             | No option selects part of the rewrite (`--help`, ran)                                                                                |
| Detector | 4.3    | No             | No identifier in any mode (ran)                                                                                                      |
| Detector | 4.4    | Not applicable | No rules or identifiers to enforce                                                                                                   |
| Detector | 5.1    | Yes            | Ran locally, no infrastructure                                                                                                       |
| Detector | 5.2    | Yes            | Ran on one file and on standard input                                                                                                |
| Detector | 5.3    | Partial        | `--check` exits 2 and prints nothing, not even the file (ran); printing modes exit 0 on a change (ran)                               |
| Detector | 5.4    | Yes            | Runs in the local binary                                                                                                             |
| Detector | 6.1    | No             | Nothing to resolve                                                                                                                   |
| Detector | 6.2    | No             | Same                                                                                                                                 |
| Detector | 6.3    | No             | Same                                                                                                                                 |
| Detector | 6.4    | Not applicable | No identifiers to document                                                                                                           |
| Detector | 7.1    | Yes            | No suppression route in [`src/`](https://github.com/anordal/shellharden/tree/v4.3.2/src); rewrote under a ShellCheck directive (ran) |
| Detector | 7.2    | Not applicable | No inline route to require a reason on                                                                                               |

## Notes for a practitioner

Use Shellharden to bring old scripts into ShellCheck's quoting once, with `--replace` and a review of the diff, rather than as a gate: ShellCheck reports the same unquoted expansions with a code and a line. If it is a gate, run `--check` one file at a time so that the failing file is known, and follow a failure with `--suggest` on that file to see why, since exit 2 also means the file did not parse.

## Attributes

| Attribute      | Value                                                                                                                      | Source                                                                           |
| -------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Kind           | Formatter                                                                                                                  | `--help`, ran                                                                    |
| Depth          | Syntactic (its own bash parser)                                                                                            | [`src/`](https://github.com/anordal/shellharden/tree/v4.3.2/src)                 |
| Output formats | Highlighted script, coloured diff, rewritten script, or none under `--check`; no SARIF                                     | `--help`, ran                                                                    |
| Exit codes     | `--check`: 2 on a change and on a parse error; 1 on a missing file or, outside `--check`, a parse error; 3 on a bad option | ran, [`main.rs`](https://github.com/anordal/shellharden/blob/v4.3.2/src/main.rs) |
| Fix mode       | `--transform` prints and `--replace` writes the rewrite; no separation of unsafe changes                                   | `--help`, ran                                                                    |
| Licence        | MPL-2.0                                                                                                                    | [LICENSE](https://github.com/anordal/shellharden/blob/v4.3.2/LICENSE)            |
