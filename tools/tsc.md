---
title: The TypeScript compiler and Defence Before Fix
summary: No custom diagnostics, failing 4.1; a file argument discards tsconfig so 5.2 is partial; @ts- directives cannot be disabled, failing 7.1
language: JavaScript and TypeScript
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-09-08, version 7.0.2
---

# The TypeScript compiler (tsc)

{% include tool-grades.html %}

`tsc` is the TypeScript type checker and compiler. Since 7.0, released on 8 July 2026, the `tsc` in the `typescript` package is the native Go implementation ([announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)). In a Defence Before Fix pipeline it is a defence host in one narrow sense: the type system itself is a fixed catalogue of defences, and many defects are best defended by making the types stricter. It is not a place a project can register a rule of its own.

## How it is conformant

Every diagnostic carries a stable numeric code, printed as `TS2322` and the like ([TSConfig reference](https://www.typescriptlang.org/tsconfig/)), which meets the printing half of clause [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding) for the bundled catalogue. It runs locally with no infrastructure and `--noEmit` gives a check-only invocation, meeting [5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure), and diagnostics are the command's own output with nothing reserved for a service, meeting [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran) and [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally). Compiler options are documented per option in the shipped package's type declarations and on the website ([compiler options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)).

## How it is not conformant

Clause [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it) fails structurally. There is no mechanism for a consuming project to add a diagnostic: the compiler options page documents no rule API, and the `plugins` option is for language service plugins that do not affect `tsc` output ([compiler options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)). TypeScript 7.0 ships without a programmatic API at all, with a new one expected in [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) ([announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)). With nothing to author there is nothing for a clause [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code) harness to run. Clause [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file) is only partly met: passing a file on the command line makes `tsc` ignore `tsconfig.json` entirely, so a single-file check does not run under the project's settings. Clause [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation) fails because no command resolves a printed `TS` code to documentation, and [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access) and [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together) fall with it since the explanatory pages are on the website. Clause [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) fails because `@ts-ignore`, `@ts-expect-error` and `@ts-nocheck` are honoured unconditionally and no compiler option disables them ([TSConfig reference](https://www.typescriptlang.org/tsconfig/)); the defence against them has to come from a linter.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                          |
| -------- | ------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Detector | [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)    | No           | No custom diagnostics ([compiler options](https://www.typescriptlang.org/docs/handbook/compiler-options.html))                    |
| Detector | [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)    | No           | Nothing to harness                                                                                                                |
| Detector | [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)    | Partial      | Stable `TS` codes for the bundled catalogue only ([TSConfig reference](https://www.typescriptlang.org/tsconfig/))                 |
| Detector | [4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own)    | No           | Not applicable                                                                                                                    |
| Detector | [5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure)    | Yes          | `tsc --noEmit` runs locally                                                                                                       |
| Detector | [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file)    | Partial      | A file argument discards `tsconfig.json` ([compiler options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)) |
| Detector | [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)    | Yes          | Diagnostics are the command's output                                                                                              |
| Detector | [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)    | Yes          | Same checker everywhere                                                                                                           |
| Detector | [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)    | No           | No lookup from a printed code to documentation                                                                                    |
| Detector | [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)    | No           | Same                                                                                                                              |
| Detector | [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)    | Partial      | Message text ships with the compiler; explanatory documentation is on the website                                                 |
| Detector | [6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation)    | Not verified | Not documented                                                                                                                    |
| Detector | [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)    | No           | `@ts-ignore` and `@ts-expect-error` cannot be disabled ([TSConfig reference](https://www.typescriptlang.org/tsconfig/))           |
| Detector | [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)    | No           | Directive comments need no reason                                                                                                 |

## Notes for a practitioner

Treat `tsc` as a bundled catalogue you tighten rather than extend: turn on `strict` and the individual strictness flags, and where a defect is a type hole, close it in the types. For a bespoke defence, write a typescript-eslint rule with type information. Ban the `@ts-` directive family with a linter rule, since the compiler will not do it for you; ts-qa-ci's `no-eslint-disable` and typescript-eslint's `ban-ts-comment` both cover them.
