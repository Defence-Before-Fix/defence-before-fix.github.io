---
title: Prettier and Defence Before Fix
summary: Formatter; fails 4.1 and 4.3 because plugins cannot report diagnostics; fails 8.3 on prettier-ignore
---

# Prettier

**Language**: JavaScript and TypeScript · **Kind**: tool · **Readiness**: 🔴 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 3.9.6

Prettier is an opinionated formatter. It rewrites source to a canonical layout and, in `--check` mode, reports which files differ from that layout. It is not a detector and it has no rules: its whole value is that there is nothing to configure or defend. In a pipeline it runs first so that every later tool sees canonical code, and it removes the class of formatting disagreement from the review entirely.

## How it is conformant

Prettier runs locally, accepts a single file, and `--check` reports in the command's output. Its plugin API contributes parsers, printers and languages ([plugins](https://prettier.io/docs/plugins)), which is enough for a project to teach it a new file type.

## How it is not conformant

Clause 4.1 fails structurally because the plugin API cannot report a diagnostic; a plugin changes how code is printed, not what is flagged ([plugins](https://prettier.io/docs/plugins)). A `--check` finding is the file name with no identifier, so 4.3 fails as well, and readiness is red because there is no bespoke defence to host. `// prettier-ignore` and `.prettierignore` are built-in suppression routes with no reason required ([ignoring code](https://prettier.io/docs/ignore)), which fails 8.3. None of sections 6, 7 or 8 has anything to attach to, and there is no declaration under 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                        |
| ------ | ------------ | ----------------------------------------------------------------------------------------------- |
| 4.1    | No           | Plugins add parsers and printers, not diagnostics ([plugins](https://prettier.io/docs/plugins)) |
| 4.2    | No           | Nothing to harness                                                                              |
| 4.3    | No           | A `--check` finding is a file name                                                              |
| 4.4    | No           | Not applicable                                                                                  |
| 5.1    | Yes          | Runs locally                                                                                    |
| 5.2    | Yes          | Single file path                                                                                |
| 5.3    | Yes          | Output of the command                                                                           |
| 5.4    | Yes          | Same everywhere                                                                                 |
| 6.1    | No           | Nothing to resolve                                                                              |
| 6.2    | No           | Same                                                                                            |
| 6.3    | No           | Same                                                                                            |
| 7.1    | No           | No listing; options can be printed but they are not defences                                    |
| 7.2    | No           | Same                                                                                            |
| 7.3    | No           | Same                                                                                            |
| 8.1    | No           | No project record                                                                               |
| 8.2    | No           | No reason on `prettier-ignore` ([ignoring code](https://prettier.io/docs/ignore))               |
| 8.3    | No           | `prettier-ignore` and `.prettierignore` are built in and undefended                             |
| 8.4    | No           | No listing                                                                                      |
| 8.5    | Yes          | Every option has a documented default and the design is to change none of them                  |
| 9.1    | No           | No agent summary                                                                                |
| 9.2    | No           | No delivery mechanism                                                                           |
| 10.1   | Not verified | Not applicable                                                                                  |
| 10.2   | Not verified | Not documented                                                                                  |
| 11.1   | No           | No declaration                                                                                  |

## Notes for a practitioner

Run Prettier in write mode locally and in check mode in the gate, and keep it out of the method otherwise: a formatting difference is not a hazard and a formatter is not where a defence lives. Ban `prettier-ignore` with a lint rule if you find it being used to hide something a real defence should catch.
