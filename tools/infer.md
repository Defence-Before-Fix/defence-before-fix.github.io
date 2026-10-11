---
title: Infer and Defence Before Fix
summary: TOPL properties meet 4.1, but every one prints TOPL_ERROR, leaving 4.3 partial; one bundled issue type runs alone only by filtering a checker, 4.2 partial; help-issue-type resolves most types offline but printable developer types have no documentation, leaving 6.1 and 6.2 partial and failing 6.3; --no-suppressions closes the ignore comments, meeting 7.1
language: C and C++
kind: tool
readiness: 🟡
detector: 🟡
checked: 2026-10-10, version v1.3.0
---

# Infer

{% include tool-grades.html %}

Infer is an interprocedural static analyser for C, C++, Objective-C, Java and other languages, run by wrapping the build, as `infer run -- clang -c a.c` or `infer run -- make`. Its checkers, chiefly Pulse, report issue types such as `NULLPTR_DEREFERENCE`, `MEMORY_LEAK_C` and `DEAD_STORE`. In a pipeline it is the slow, deep check beside the compiler and a linter, and its route for a project's own rule is TOPL, a language of state machines over calls. The v1.3.0 release binary needs glibc 2.38, so it ran here in a Debian 13 user space.

## How it is conformant

A project writes a TOPL property, an automaton whose transitions match calls, and runs it with `--topl --topl-properties <file>`; TOPL support for C, C++ and Objective-C is marked experimental ([TOPL](https://github.com/facebook/infer/blob/v1.3.0/website/docs/checker-topl.md)). A probe property `ProjNoStrcpy`, with the message `proj.no-strcpy: use a bounded copy` and a transition to `error` on `strcpy(D, S, R)`, reported `t.c:2: error: Topl Error(TOPL_ERROR)` with that message, ran (4.1). `--topl-only` runs TOPL with every other checker disabled ([infer manual](https://github.com/facebook/infer/blob/v1.3.0/infer/man/man1/infer-full.txt)), which ran the property alone on a single file. Bundled issue types are assigned once by the maintainers, and the type was printed unaltered in every format: on the console and in `report.txt` in parentheses after its human name, `Null Dereference(NULLPTR_DEREFERENCE)`, a separately delimited token under reading 6, as `bug_type` in `report.json`, as `ruleId` in the SARIF that `--sarif` writes, and in the `--issues-tests` file, ran. Infer runs locally on a single file, with the findings and a count by issue type printed in the command's own output by default, and it is open source with no paid tier (5.1, 5.2, 5.4).

Inline suppression has a switch. `// @infer-ignore DEAD_STORE` and `// @infer-ignore-every DEAD_STORE` hid the dead stores in their fixtures, and the run said `No issues found`; with `--no-suppressions` the same run reported both, ran ([suppressions](https://github.com/facebook/infer/blob/v1.3.0/website/docs/01-suppressions.md)). The route is detectable as well: each suppressed issue stayed in `report.json` with `"suppressed": true`, ran (7.1). `--disable-issue-type`, the `--report-block-list-*` options and `--censor-report` are configuration the project passes or not.

Resolution works offline for most types. `infer help --help-issue-type NULLPTR_DEREFERENCE` printed the type's name, its checker and several paragraphs of documentation under `unshare -rn`, keyed on the identifier exactly as printed, and `infer help --list-issue-types` lists every type with its human name, checker and default, ran.

## How it is not conformant

Clause 4.3 is partial. A TOPL property cannot carry an identifier of its own: every property reports `TOPL_ERROR`, or `TOPL_ERROR_LATENT`, and its name or message appears only in the message text, `qualifier` in `report.json`, ran. Bundled types carry stable identifiers, so the clause holds for them and fails for the rules a defence is written as. A project can put its own identifier at the start of the message, as the probe did, which answers readiness under reading 2 but not the clause.

Clause 4.2 is partial. A bundled issue type cannot be run alone: `--<checker>-only` runs one checker, and a checker reports several types, as `--pulse-only` printed both `NULLPTR_DEREFERENCE` and `MEMORY_LEAK_C` on one fixture, ran. Narrowing the result to one type takes `--disable-issue-type` for the others, which the manual says filters reports "once the checkers have run" and "does not make the corresponding checker not run" ([infer manual](https://github.com/facebook/infer/blob/v1.3.0/infer/man/man1/infer-full.txt)). The TOPL property, which `--topl-only` runs alone, meets the clause.

Clauses 6.1 and 6.2 are partial and 6.3 fails. Of the 160 types `--list-issue-types` names, four print `No documentation` from `--help-issue-type`: `CONDITION_ALWAYS_FALSE`, `CONDITION_ALWAYS_TRUE`, `DO_NOT_REPORT` and `UNREACHABLE_CODE`, ran. They are developer types, hidden by default, but the documented `--debug-exceptions` option reveals them, and with it the bufferoverrun checker printed `u2.c:4: warning: Condition Always True(CONDITION_ALWAYS_TRUE)`, ran, so a bundled checker prints an identifier that resolves to nothing shipped. The release shipped with those four undocumented, so no gate blocks it (6.4). Some documentation that does resolve links on to other types at site-relative addresses such as `/docs/next/all-issue-types#nil_block_call`, which lead nowhere from the installed copy.

Clause 5.3 is partial under reading 8: with `-q` (`--quiet`, "Do not print anything on standard output") the run printed nothing at all, neither a count nor where the findings went, whilst they were written to `infer-out/report.txt` and `report.json`, ran. Suppression comments may sit under a comment giving a reason, but nothing requires one (7.2). There is no rule over the rules (4.4).

Readiness is 🟡: a bespoke TOPL property and a run of it alone hold, but it prints no identifier of its own. The detector grade is 🟡 because of 4.2, 4.3, 5.3, 6.1, 6.2 and 6.3, with the SHOULDs 4.4, 6.4 and 7.2 not met. Infer declares no version of this document.

## Clause by clause

| Document | Clause | Result  | Evidence                                                                                                                                                                                                             |
| -------- | ------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Yes     | TOPL property reported on C, ran; experimental for C ([TOPL](https://github.com/facebook/infer/blob/v1.3.0/website/docs/checker-topl.md))                                                                            |
| Detector | 4.2    | Partial | `--topl-only` runs a property alone, ran; a bundled type only by filtering its checker's other types ([infer manual](https://github.com/facebook/infer/blob/v1.3.0/infer/man/man1/infer-full.txt))                   |
| Detector | 4.3    | Partial | Bundled types unaltered in console, `report.txt`, JSON, SARIF and `--issues-tests`, ran; every TOPL property prints `TOPL_ERROR`, ran                                                                                |
| Detector | 4.4    | No      | None                                                                                                                                                                                                                 |
| Detector | 5.1    | Yes     | `infer run -- clang -c <file>` locally, ran                                                                                                                                                                          |
| Detector | 5.2    | Yes     | One file, ran                                                                                                                                                                                                        |
| Detector | 5.3    | Partial | Findings and a count on the console by default; `-q` printed nothing whilst writing `infer-out/report.txt` (reading 8), ran                                                                                          |
| Detector | 5.4    | Yes     | Open source, no paid tier                                                                                                                                                                                            |
| Detector | 6.1    | Partial | `infer help --help-issue-type <type>` keyed on the type as printed; four printable types print `No documentation`, ran                                                                                               |
| Detector | 6.2    | Partial | The same lookup under `unshare -rn`, ran                                                                                                                                                                             |
| Detector | 6.3    | No      | `CONDITION_ALWAYS_TRUE`, printed under `--debug-exceptions`, resolves to nothing shipped, ran                                                                                                                        |
| Detector | 6.4    | No      | Released with four printable types undocumented                                                                                                                                                                      |
| Detector | 7.1    | Yes     | `--no-suppressions` reported both suppressed fixtures; suppressed issues kept in JSON with `"suppressed": true`, ran ([suppressions](https://github.com/facebook/infer/blob/v1.3.0/website/docs/01-suppressions.md)) |
| Detector | 7.2    | No      | A reason comment is allowed, not required ([suppressions](https://github.com/facebook/infer/blob/v1.3.0/website/docs/01-suppressions.md))                                                                            |

## Notes for a practitioner

Write the class as a TOPL property whose `message` starts with the project's identifier, since the printed type is `TOPL_ERROR` for every property, and read the identifier from the message or the JSON `qualifier`. Prove it with `--topl-only --topl-properties <file>` on a fixture; TOPL is experimental for C and C++, and in the probe it reported at the line of the enclosing function rather than at the call. Run the enforced invocation with `--no-suppressions`, or audit `"suppressed": true` in `report.json`, and with `--fail-on-issue`, because Infer exits 0 on findings; a file that does not compile exits 1. The installed manual names the comment keywords `@infer-disable` under `--no-suppressions`, whilst the suppressions page and the runs use `@infer-ignore`. A single `@infer-ignore` at the end of a line hid the finding on the next line too, ran.

## Attributes

| Attribute      | Value                                                                                                    | Source                                                                                      |
| -------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Kind           | Detector (interprocedural static analyser)                                                               | [infer manual](https://github.com/facebook/infer/blob/v1.3.0/infer/man/man1/infer-full.txt) |
| Depth          | Semantic, with data flow across procedures, bundled and bespoke                                          | [TOPL](https://github.com/facebook/infer/blob/v1.3.0/website/docs/checker-topl.md)          |
| Rule form      | TOPL automata over calls, in a property file; experimental for C and C++                                 | [TOPL](https://github.com/facebook/infer/blob/v1.3.0/website/docs/checker-topl.md)          |
| Output formats | Console text, `report.txt`, `report.json`, SARIF under `--sarif`, `--issues-tests`; SARIF native         | ran                                                                                         |
| Exit codes     | 0 on a finding, 2 under `--fail-on-issue`; 1 on a usage error; 1 on a file that does not compile         | ran                                                                                         |
| Report file    | `infer-out/report.txt` and `report.json` on every run whilst the console prints the findings and a count | ran                                                                                         |
| Cache          | `--reactive` and `--changed-files-index` analyse from changed files                                      | [infer manual](https://github.com/facebook/infer/blob/v1.3.0/infer/man/man1/infer-full.txt) |
| Baseline       | `infer reportdiff` splits two reports into introduced, fixed and preexisting issues                      | ran (`--help`)                                                                              |
| Rule listing   | `infer help --list-issue-types`, with each type's checker and default                                    | ran                                                                                         |
| Licence        | MIT                                                                                                      | [LICENSE](https://github.com/facebook/infer/blob/v1.3.0/LICENSE)                            |
