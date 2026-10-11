---
title: include-what-you-use and Defence Before Fix
summary: One fixed analysis of #include use, so 4.1 fails; its advice carries no identifier, failing 4.3 and leaving section 6 with nothing to resolve; keep pragmas can be neither switched off nor seen, failing 7.1
language: C and C++
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-10-10, version 0.27
---

# include-what-you-use

{% include tool-grades.html %}

include-what-you-use (IWYU) is a Clang-based tool that reports, for one C or C++ source file and its associated headers, which `#include` lines and forward declarations to add and which to remove, so that each file includes a header for every symbol it uses ([README at 0.27](https://github.com/include-what-you-use/include-what-you-use/blob/0.27/README.md)). It is built against one Clang release; version 0.27 ran here built from the tag against LLVM 23.1.3 and reported `include-what-you-use 0.27 (git:c9cbc83) based on clang version 23.1.3`. In a pipeline it sits beside the compiler as a hygiene check on headers, with `fix_includes.py` to apply its advice. It has one analysis and no way to add another, so it cannot host a bespoke defence.

## How it is conformant

The reporting clauses are met. `include-what-you-use a.c` runs locally on one file with the compiler flags given after it, and with `iwyu_tool.py -p .` it reads a compilation database. On a fixture that included `<stdio.h>` and `<ctype.h>` without using them, it printed `a.c should remove these lines:`, `- #include <ctype.h>  // lines 4-4` and `- #include <stdio.h>  // lines 1-1`, then the full include list, on standard error, the command's own output, ran (5.1, 5.2, 5.3). It is open source and has no paid tier (5.4). Graded on its one bundled analysis, 4.2 is met: the run on one fixture printed only that analysis's advice, with no other check to obscure it and no test suite run.

## How it is not conformant

Clause 4.1 fails. The analysis is built in, and what a project can supply changes how it reasons, not what it looks for: mapping files that say which header provides a symbol ([IWYUMappings.md](https://github.com/include-what-you-use/include-what-you-use/blob/0.27/docs/IWYUMappings.md)), pragmas in the source ([IWYUPragmas.md](https://github.com/include-what-you-use/include-what-you-use/blob/0.27/docs/IWYUPragmas.md)) and options such as `--keep=<glob>` and `--no_fwd_decls` (`--help`, ran). Clause 4.3 fails: the advice is a list of lines to add and remove, with no identifier of any kind, ran; `iwyu_tool.py -o clang` and `-o clang-warning` print the same advice as compiler-style diagnostics, `a.c:1:1: error: superfluous '#include <stdio.h>'`, still with none, ran. With nothing printed to key a lookup on, section 6 has nothing to resolve, and 6.1, 6.2 and 6.3 are No.

Clause 7.1 fails. The pragmas `keep`, `begin_keep` and `end_keep`, and `always_keep` stop IWYU from advising the removal of an include, and `no_include` and `no_forward_declare` stop it advising an addition ([IWYUPragmas.md](https://github.com/include-what-you-use/include-what-you-use/blob/0.27/docs/IWYUPragmas.md)). No option switches them off: `--help` lists none, ran. The default output does not report them: with `<stdlib.h>  // IWYU pragma: keep` in a fixture that used nothing from it, the include was simply listed as kept, ran. At `--verbose=5` the run printed `Marked dep: a.c needs to keep <stdlib.h> (reason: pragma_keep)`, and `begin_keep pragma seen` for a block, ran, but the help documents the flag only as "the higher the level, the more output", so the report of a suppression is an undocumented by-product of debugging output, and under reading 18 the route is not detectable by the detector; a project cannot write a rule in IWYU to see it. Clause 7.2 fails: a pragma takes no reason.

By default the tool exits 0 whatever it advises; `-Xiwyu --error` makes advice exit 1, the same code as a usage error (`FATAL ERROR: unknown flag.`) and as a file it cannot parse, which exited 1 with or without `--error` and printed Clang's errors, ran. A defence routed through IWYU cannot tell those apart by the exit code.

The detector grade is 🔴 on 4.1 and 4.3, both structural under reading 1, with 6.1, 6.2, 6.3, 7.1 and 7.2 failing. Readiness is 🔴: no bespoke rules and no identifier on findings.

## Clause by clause

| Document | Clause | Result         | Evidence                                                                                                                                                                                                                                                         |
| -------- | ------ | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | No             | One built-in analysis; mappings, pragmas and options only adjust it ([IWYUMappings.md](https://github.com/include-what-you-use/include-what-you-use/blob/0.27/docs/IWYUMappings.md))                                                                             |
| Detector | 4.2    | Yes            | Bundled analysis: one fixture gave its advice alone, ran                                                                                                                                                                                                         |
| Detector | 4.3    | No             | Advice is lines to add and remove, no identifier, in every `iwyu_tool.py` format, ran                                                                                                                                                                            |
| Detector | 4.4    | Not applicable | No rules to enforce an identifier on                                                                                                                                                                                                                             |
| Detector | 5.1    | Yes            | `include-what-you-use <file>` locally, ran                                                                                                                                                                                                                       |
| Detector | 5.2    | Yes            | One source file per run, ran                                                                                                                                                                                                                                     |
| Detector | 5.3    | Yes            | Advice on the command's standard error, ran                                                                                                                                                                                                                      |
| Detector | 5.4    | Yes            | Same everywhere; no paid tier                                                                                                                                                                                                                                    |
| Detector | 6.1    | No             | Nothing to resolve                                                                                                                                                                                                                                               |
| Detector | 6.2    | No             | Same                                                                                                                                                                                                                                                             |
| Detector | 6.3    | No             | Same                                                                                                                                                                                                                                                             |
| Detector | 6.4    | Not applicable | No identifiers to document                                                                                                                                                                                                                                       |
| Detector | 7.1    | No             | Keep and no-include pragmas have no switch and are not reported; `--verbose=5` names them only as undocumented debugging output (reading 18), ran ([IWYUPragmas.md](https://github.com/include-what-you-use/include-what-you-use/blob/0.27/docs/IWYUPragmas.md)) |
| Detector | 7.2    | No             | A pragma takes no reason                                                                                                                                                                                                                                         |

## Notes for a practitioner

IWYU is an off-the-shelf rule under method clause 3.2 when the class is "a header included and not used" or "a symbol used through a header the file does not include", proven by a fixture that carries an unused include. It cannot carry a defence of the project's own. Run it with `-Xiwyu --error` so that advice fails the run, and check the output for Clang errors rather than trusting the exit code, since a file that does not parse exits with the same 1. Review every `IWYU pragma: keep` and `no_include` by a text search outside the tool, beside a comment giving the reason, because IWYU will not show them. Pin IWYU to the Clang release it was built for, as each IWYU version follows one Clang release.

## Attributes

| Attribute      | Value                                                                                          | Source                                                                                                     |
| -------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Kind           | Detector (one analysis of `#include` use)                                                      | [README](https://github.com/include-what-you-use/include-what-you-use/blob/0.27/README.md)                 |
| Depth          | Semantic: uses resolved through the Clang syntax tree                                          | [WhatIsAUse.md](https://github.com/include-what-you-use/include-what-you-use/blob/0.27/docs/WhatIsAUse.md) |
| Output formats | IWYU advice text; `iwyu_tool.py -o` also `clang` and `clang-warning`; no SARIF                 | ran                                                                                                        |
| Exit codes     | 0 on advice by default, N under `--error[=N]`; 1 on a usage error; 1 on a file it cannot parse | ran                                                                                                        |
| Report file    | No                                                                                             | ran (`--help`)                                                                                             |
| Fix mode       | `fix_includes.py` applies the advice read from the output                                      | [README](https://github.com/include-what-you-use/include-what-you-use/blob/0.27/README.md)                 |
| Rule listing   | No; one analysis                                                                               | ran (`--help`)                                                                                             |
| Licence        | University of Illinois/NCSA (LLVM release licence)                                             | [LICENSE.TXT](https://github.com/include-what-you-use/include-what-you-use/blob/0.27/LICENSE.TXT)          |
