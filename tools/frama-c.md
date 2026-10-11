---
title: Frama-C and Defence Before Fix
summary: MetAcsl meta-properties meet 4.1, and -meta-set runs one, but no bundled alarm kind runs alone, leaving 4.2 partial; alarm kinds missing from the default output and meta names altered leave 4.3 partial; nothing installed resolves an alarm kind, failing 6.1 to 6.3; admit is listed by -report, meeting 7.1
language: C and C++
kind: tool
readiness: 🟡
detector: 🟡
checked: 2026-10-10, version 33.0 (Arsenic)
---

# Frama-C

{% include tool-grades.html %}

Frama-C is a platform for the analysis of C code, built in OCaml around a kernel that parses C and the ACSL specification language, with analyses as plug-ins: Eva, an abstract interpreter that reports every possible undefined behaviour as an alarm, WP for deductive proof against ACSL contracts, RTE, which writes the runtime-error checks as annotations, and MetAcsl, which turns a property stated once over many functions into annotations at every place it applies. It is a verification tool rather than a linter: it needs an entry point and a whole program, or a stubbed one, and in a pipeline it sits after the compiler and the linters, on the code whose absence of undefined behaviour must be shown. Graded here is the Linux binary package of 33.0, which bundles MetAcsl 0.11 and the Report and Markdown Report plug-ins.

## How it is conformant

A project's own rule can be written in the bundled MetAcsl plug-in as a meta-property, `meta \prop, \name(proj_no_secret_write), \targets(\ALL), \context(\writing), \separated(\written, &secret);`, which forbids every write to `secret` in every function ([MetAcsl README](https://git.frama-c.com/pub/meta/-/blob/0.11/README.md)). At 33.0, `frama-c -meta m.c -then-last -eva` printed `[eva:alarm] m.c:3: Warning: check 'proj_no_secret_write,meta' got status invalid.` for the function that writes it, beside Eva's own alarms (ran). A plug-in in OCaml against the kernel's API is the other route, described in the [plug-in development guide](https://frama-c.com/download/plugin-development-guide-33.0-Arsenic.pdf); it was not built here, because the binary package ships no OCaml compiler (4.1). For a project's rules, `-meta-set=<name>` processes only the named meta-property: on a file with two, `-meta-set=proj_no_other_write` processed one and printed only its check (ran).

Frama-C runs locally on a single file, `frama-c -eva u.c`, with no service and no licence tier, and prints each alarm and an analysis summary in the command's own output (5.1, 5.2, 5.4; ran). `-mdr-gen sarif -mdr-out <file>`, `-report-csv <file>` and `-<plug-in>-log` write files as well, and the console still carried the alarms and the summary (ran) ([user manual](https://frama-c.com/download/user-manual-33.0-Arsenic.pdf), sections 3.3.7 and 11) (5.3).

The inline route is detectable. An ACSL `admit` clause "indicates that the corresponding clause can be readily assumed to hold, without trying to verify it" ([ACSL implementation](https://frama-c.com/download/acsl-implementation-33.0-Arsenic.pdf), section 2.3.2): `//@ admit i != 0;` before `return 100 / i;` removed the division-by-zero alarm, and the analysis summary said `0 alarms generated`, but the bundled Report plug-in, run with `-then -report`, listed it as `[ Extern  ] Admit ("s.c", line 2)  Unverifiable but considered Valid.` (ran) (7.1). Switching alarms off with `-eva-warn-key alarm=inactive`, and classification rules with the `SKIP` action, apply only when the project passes them; under `alarm=inactive`, `-report` still listed the alarm (ran).

## How it is not conformant

Clause 4.2 is partial. It applies "to every Rule the Detector runs", and Eva's bundled rules, its alarm kinds, cannot be run one at a time: Eva emits every kind it finds in one analysis, and the kernel's `-warn-*` options switch only some kinds on or off, such as signed overflow and invalid pointers, with none for division by zero or an index out of bounds (`-kernel-h`, `-eva-h`, ran). The project's meta-properties run alone under `-meta-set`, as above.

Clause 4.3 is partial. An alarm kind is named by the maintainers, `division_by_zero` or `index_bound`, but the default output does not print it: an alarm of unknown status printed `[eva:alarm] u.c:2: Warning: accessing out of bounds index. assert 0 ≤ i;`, where `eva:alarm` is the category shared by every alarm, and the kind appeared only in SARIF, as `ruleId` `index_bound`, and in `-report`, as `Assertion 'Eva,index_bound'` (ran). A meta-property's name is chosen by its author, but MetAcsl adds a second name, `meta`, by default, printed joined to it as `'proj_no_secret_write,meta'`; `-meta-no-add-prefix` printed `'proj_no_secret_write'` alone (ran), which is a stable identifier altered by default and printed unaltered under a documented flag (reading 5). In SARIF every meta-property's result has the `ruleId` `user-spec`, with the name only in the message, `proj_no_secret_write.` (ran).

Clause 4.4 is partial, under reading 7. A meta-property with no `\name` was refused at load, `[kernel:annot-error] m4.c:2: Failure: Invalid property shape. Ignoring global annotation`, and the run stopped with exit 1. But `\name("has space")` was accepted, and the name was then dropped from the output, which printed only `assertion 'meta' got status invalid` (ran).

Resolution fails. Nothing installed is keyed on an alarm kind: no command takes `division_by_zero` or `index_bound` and returns a description, and the manuals that describe the alarms, such as the [Eva manual](https://frama-c.com/download/eva-manual-33.0-Arsenic.pdf), are PDF downloads, not installed by the package, whose `doc` directory holds only plug-in READMEs and licences (ran). `-eva-warn-key help` lists warning categories with a description each, such as `alarm : warning : warnings for each possible undefined behavior detected by the analysis`, but under the plug-in's heading and keyed `alarm`, where the output prints `eva:alarm`, so the printed identifier must be cut to a part first (reading 11); many kernel categories read `No description provided` (ran). The Markdown Report describes each alarm it lists, but only for the alarms of a run, not for an identifier presented alone. So 6.1, 6.2 and 6.3 fail, and no release gate was found (6.4, not verified).

No reason is required: `admit` takes a predicate and an optional name, and `//@ admit i != 0;` was accepted with none (ran) (7.2).

By default the exit code is 0 whatever Eva finds: a sure division by zero and an invalid meta-property both exited 0, and `-eva-warn-key alarm=error` turned each alarm into a `User Error` and the exit code into 1 (ran), as the [user manual](https://frama-c.com/download/user-manual-33.0-Arsenic.pdf) (section 7.2) documents for a category set to `error`. A file Frama-C cannot parse stops the run with `Frama-C aborted: invalid user input.` and exit 1 (ran).

Readiness is 🟡: a bespoke rule is written in MetAcsl and runs alone under `-meta-set`, but its name is printed altered unless `-meta-no-add-prefix` is passed. The detector grade is 🟡 because no structural MUST is No: 4.2 and 4.3 are partial, and 6.1, 6.2 and 6.3 fail. Frama-C declares no version of this document.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                                                |
| -------- | ------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Yes          | MetAcsl meta-property reported by Eva (ran; [MetAcsl README](https://git.frama-c.com/pub/meta/-/blob/0.11/README.md)); OCaml plug-ins documented, not built             |
| Detector | 4.2    | Partial      | `-meta-set=<name>` runs one meta-property (ran); no option runs one bundled alarm kind                                                                                  |
| Detector | 4.3    | Partial      | Alarm kind absent from the default output; `'proj_no_secret_write,meta'` by default, unaltered under `-meta-no-add-prefix`, reading 5; SARIF `ruleId` `user-spec` (ran) |
| Detector | 4.4    | Partial      | A meta-property with no `\name` refused at load; a name with a space accepted and dropped, reading 7 (ran)                                                              |
| Detector | 5.1    | Yes          | Ran locally, no infrastructure                                                                                                                                          |
| Detector | 5.2    | Yes          | Ran on one file                                                                                                                                                         |
| Detector | 5.3    | Yes          | Alarms and summary in the command's output; report files are written as well (ran)                                                                                      |
| Detector | 5.4    | Yes          | Every analysis runs in the local package                                                                                                                                |
| Detector | 6.1    | No           | No mechanism keyed on an alarm kind; `-eva-warn-key help` keyed on `alarm`, not the printed `eva:alarm`, reading 11 (ran)                                               |
| Detector | 6.2    | No           | No mechanism; the manuals are not installed, reading 14 (ran)                                                                                                           |
| Detector | 6.3    | No           | `index_bound` resolves to nothing shipped                                                                                                                               |
| Detector | 6.4    | Not verified | No release gate found                                                                                                                                                   |
| Detector | 7.1    | Yes          | `admit` is listed by `-report` as `Unverifiable but considered Valid` (ran; [ACSL implementation](https://frama-c.com/download/acsl-implementation-33.0-Arsenic.pdf))   |
| Detector | 7.2    | No           | `admit` takes no reason (ran)                                                                                                                                           |

## Notes for a practitioner

Write a project's rule as a MetAcsl meta-property with a `\name` of plain identifier characters, run it with `-meta -meta-no-add-prefix -meta-set=<name>` on a fixture, then `-then-last -eva`, so that the name is printed as written, and read the result from the console or `-report` rather than SARIF, where every meta-property is `user-spec`. Pass `-eva-warn-key alarm=error` in the enforced run, since by default an analysis that finds an alarm exits 0. Run `-then -report` in the same invocation and fail the build on any `Admit` or `Considered valid` line it lists, since that is where an `admit` shows. Keep the Eva and ACSL manuals of the release beside the code, since nothing installed explains an alarm kind.

## Attributes

| Attribute      | Value                                                                                                     | Source                                                                                                                                                                        |
| -------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kind           | Detector (verification platform: abstract interpretation and deductive proof)                             | [user manual](https://frama-c.com/download/user-manual-33.0-Arsenic.pdf)                                                                                                      |
| Depth          | Semantic, with data flow (Eva's value analysis), bundled and bespoke                                      | ran                                                                                                                                                                           |
| Rule form      | ACSL meta-properties in MetAcsl; or OCaml plug-ins against the kernel API                                 | [MetAcsl README](https://git.frama-c.com/pub/meta/-/blob/0.11/README.md), [plug-in development guide](https://frama-c.com/download/plugin-development-guide-33.0-Arsenic.pdf) |
| Output formats | Console log, `-report` text, CSV, classification JSON, Markdown, and native SARIF through Markdown Report | ran                                                                                                                                                                           |
| Exit codes     | 0 on alarms; 1 with `-eva-warn-key alarm=error`; 1 on a usage error; 1 on a file it cannot parse          | ran                                                                                                                                                                           |
| Report file    | `-mdr-out` and `-report-csv` write a file, with the full log still on the console                         | ran                                                                                                                                                                           |
| Rule listing   | `-<plug-in>-warn-key help` lists warning categories; no listing of alarm kinds                            | ran                                                                                                                                                                           |
| Licence        | LGPL-2.1 for most of the sources                                                                          | [LICENSE](https://git.frama-c.com/pub/frama-c/-/blob/33.0/LICENSE)                                                                                                            |
