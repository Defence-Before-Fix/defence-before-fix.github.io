---
title: Prettier and Defence Before Fix
summary: Formatter; plugins cannot report diagnostics so 4.1 and 4.3 fail; prettier-ignore cannot be switched off, failing 7.1
---

# Prettier

**Language**: JavaScript and TypeScript · **Kind**: tool · **Readiness**: 🔴 · **Detector conformance**: 🔴 · **Checked**: 2026-09-08, version 3.9.6

Prettier is an opinionated formatter. It rewrites source to a canonical layout and, in `--check` mode, reports which files differ from that layout. It is not a detector and it has no rules: its whole value is that there is nothing to configure or defend. In a pipeline it runs first so that every later tool sees canonical code, and it removes the class of formatting disagreement from the review entirely.

## How it is conformant

Section 5 is met: Prettier runs locally, accepts a single file, `--check` reports in the command's output and nothing is held back for a service. Its plugin API contributes parsers, printers and languages ([plugins](https://prettier.io/docs/plugins)), which is enough for a project to teach it a new file type.

## How it is not conformant

Clause 4.1 fails structurally because the plugin API cannot report a diagnostic; a plugin changes how code is printed, not what is flagged ([plugins](https://prettier.io/docs/plugins)). A `--check` finding is the file name with no identifier, so 4.3 fails as well, there is nothing for a clause 4.2 harness to run, and readiness is red because there is no bespoke defence to host. Section 6 has nothing to resolve. `// prettier-ignore` and `.prettierignore` are built-in suppression routes that no option switches off and nothing reports ([ignoring code](https://prettier.io/docs/ignore)), which fails 7.1, and no reason is required on either, which fails 7.2.

## Clause by clause

| Document | Clause | Result | Evidence                                                                                                                  |
| -------- | ------ | ------ | ------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | No     | Plugins add parsers and printers, not diagnostics ([plugins](https://prettier.io/docs/plugins))                           |
| Detector | 4.2    | No     | Nothing to harness                                                                                                        |
| Detector | 4.3    | No     | A `--check` finding is a file name                                                                                        |
| Detector | 4.4    | No     | Not applicable                                                                                                            |
| Detector | 5.1    | Yes    | Runs locally                                                                                                              |
| Detector | 5.2    | Yes    | Single file path                                                                                                          |
| Detector | 5.3    | Yes    | Output of the command                                                                                                     |
| Detector | 5.4    | Yes    | Same everywhere                                                                                                           |
| Detector | 6.1    | No     | Nothing to resolve                                                                                                        |
| Detector | 6.2    | No     | Same                                                                                                                      |
| Detector | 6.3    | No     | Same                                                                                                                      |
| Detector | 6.4    | No     | Not applicable                                                                                                            |
| Detector | 7.1    | No     | `prettier-ignore` and `.prettierignore` cannot be disabled or reported ([ignoring code](https://prettier.io/docs/ignore)) |
| Detector | 7.2    | No     | No reason on `prettier-ignore`                                                                                            |

## Notes for a practitioner

Run Prettier in write mode locally and in check mode in the gate, and keep it out of the method otherwise: a formatting difference is not a hazard and a formatter is not where a defence lives. Ban `prettier-ignore` with a lint rule if you find it being used to hide something a real defence should catch.
