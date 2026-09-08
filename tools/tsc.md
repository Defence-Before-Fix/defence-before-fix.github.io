---
title: The TypeScript compiler and Defence Before Fix
summary: No custom diagnostics, failing 4.1; a file argument discards tsconfig so 5.2 is partial; fails 8.3 because @ts- directives cannot be disabled
---

# The TypeScript compiler (tsc)

**Language**: JavaScript and TypeScript · **Kind**: tool · **Readiness**: 🔴 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 7.0.2

`tsc` is the TypeScript type checker and compiler. Since 7.0, released on 8 July 2026, the `tsc` in the `typescript` package is the native Go implementation ([announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)). In a Defence Before Fix pipeline it is a defence host in one narrow sense: the type system itself is a fixed catalogue of defences, and many defects are best defended by making the types stricter. It is not a place a project can register a rule of its own.

## How it is conformant

Every diagnostic carries a stable numeric code, printed as `TS2322` and the like ([TSConfig reference](https://www.typescriptlang.org/tsconfig/)), which meets the spirit of clause 4.3 for the bundled catalogue. It runs locally with no infrastructure, and `--noEmit` gives a check-only invocation. Compiler options are documented per option in the shipped package's type declarations and on the website ([compiler options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)).

## How it is not conformant

Clause 4.1 fails structurally. There is no mechanism for a consuming project to add a diagnostic: the compiler options page documents no rule API, and the `plugins` option is for language service plugins that do not affect `tsc` output ([compiler options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)). TypeScript 7.0 ships without a programmatic API at all, with a new one expected in 7.1 ([announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)). Clause 5.2 is only partly met: passing a file on the command line makes `tsc` ignore `tsconfig.json` entirely, so a single-file check does not run under the project's settings. Clause 8.3 fails because `@ts-ignore`, `@ts-expect-error` and `@ts-nocheck` are honoured unconditionally and no compiler option disables them ([TSConfig reference](https://www.typescriptlang.org/tsconfig/)); the defence against them has to come from a linter. Clause 6.1 has no command that resolves a `TS` code to documentation from the installed copy.

## Clause by clause

| Clause | Result       | Evidence                                                                                                                          |
| ------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | No           | No custom diagnostics ([compiler options](https://www.typescriptlang.org/docs/handbook/compiler-options.html))                    |
| 4.2    | No           | Nothing to harness                                                                                                                |
| 4.3    | Partial      | Stable `TS` codes for the bundled catalogue only ([TSConfig reference](https://www.typescriptlang.org/tsconfig/))                 |
| 4.4    | No           | Not applicable                                                                                                                    |
| 5.1    | Yes          | `tsc --noEmit` runs locally                                                                                                       |
| 5.2    | Partial      | A file argument discards `tsconfig.json` ([compiler options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)) |
| 5.3    | Yes          | Diagnostics are the command's output                                                                                              |
| 5.4    | Yes          | Same checker everywhere                                                                                                           |
| 6.1    | No           | No lookup from a printed code to documentation                                                                                    |
| 6.2    | No           | Same                                                                                                                              |
| 6.3    | Partial      | Message text ships with the compiler; explanatory documentation is on the website                                                 |
| 7.1    | Partial      | `--showConfig` prints the resolved options, without descriptions or routes                                                        |
| 7.2    | Yes          | `--showConfig` is derived from the configuration                                                                                  |
| 7.3    | No           | A project cannot add defences                                                                                                     |
| 8.1    | No           | No project record                                                                                                                 |
| 8.2    | No           | Directive comments need no justification                                                                                          |
| 8.3    | No           | `@ts-ignore` and `@ts-expect-error` cannot be disabled ([TSConfig reference](https://www.typescriptlang.org/tsconfig/))           |
| 8.4    | No           | No listing                                                                                                                        |
| 8.5    | Partial      | Defaults for every option are documented                                                                                          |
| 9.1    | No           | No agent summary                                                                                                                  |
| 9.2    | No           | No delivery mechanism                                                                                                             |
| 10.1   | Not verified | Not documented                                                                                                                    |
| 10.2   | Not verified | Not documented                                                                                                                    |
| 11.1   | No           | No declaration                                                                                                                    |

## Notes for a practitioner

Treat `tsc` as a bundled catalogue you tighten rather than extend: turn on `strict` and the individual strictness flags, and where a defect is a type hole, close it in the types. For a bespoke defence, write a typescript-eslint rule with type information. Ban the `@ts-` directive family with a linter rule, since the compiler will not do it for you; ts-qa-ci's `no-eslint-disable` and typescript-eslint's `ban-ts-comment` both cover them.
