---
title: checkbashisms and Defence Before Fix
summary: A fixed set of Perl patterns with no identifiers fails 4.1, 4.2 and 4.3, and leaves nothing for section 6 to resolve; runs locally on one file, meeting section 5; no suppression route, so 7.1 holds
language: Shell
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-10-10, version devscripts 2.26.13
---

# checkbashisms

{% include tool-grades.html %}

checkbashisms is the Debian devscripts check for bashisms: a single Perl script, derived from a lintian check, that reads scripts meant for `/bin/sh` and reports shell features POSIX does not require, such as `[[ ]]`, `echo -e`, `source` and arrays. It also checks the reverse, reporting a script with a bash shebang that uses no bashism at all. In a pipeline it is the portability step for `#!/bin/sh` scripts, beside ShellCheck with `-s sh`. It ships only inside devscripts, with no release of its own, and has a fixed set of patterns and no identifiers.

## How it is conformant

checkbashisms meets section 5. `checkbashisms posix.sh` runs locally on one file, and `-` reads standard input (5.1, 5.2, ran), every finding is printed in the command's own output, on standard error by default and on standard output under `--lint` (5.3), and nothing is held back for a service or tier (5.4). The [manual page at the tag](https://salsa.debian.org/debian/devscripts/-/blob/v2.26.13/scripts/checkbashisms.1) documents the exit value as a sum: 1 when a possible bashism was found, 2 when a file was skipped, 4 when a bash script used no bashism; a run with one finding, one clean file and one missing file exited 3, and a bad option exited 255 (ran).

There is no suppression route. The [manual page](https://salsa.debian.org/debian/devscripts/-/blob/v2.26.13/scripts/checkbashisms.1) lists none, and the [script](https://salsa.debian.org/debian/devscripts/-/blob/v2.26.13/scripts/checkbashisms.pl) strips comments before matching and reads no directive or ignore file (7.1). What it checks depends on the shebang: a script whose interpreter is not `sh`, `dash`, `posh` or bash is skipped with `does not appear to be a /bin/sh script; skipping` and exit 2 (ran), and `-f` forces the check. That is the tool's scope, printed when it applies, not a route that hides a finding.

## How it is not conformant

Clause 4.1 fails. The patterns are Perl hashes inside [`checkbashisms.pl`](https://salsa.debian.org/debian/devscripts/-/blob/v2.26.13/scripts/checkbashisms.pl), each mapping a regular expression to an explanation, and no option loads another; a project cannot add one without editing the script. Clause 4.2 is graded on the bundled patterns and fails too: the options are `-n`, `-p`, `-f`, `-l`, `-x` and `-e`, which widen the checks or change the output, and none selects one check (manual page, ran).

Clause 4.3 fails. A finding prints the explanation in place of an identifier: `possible bashism in posix.sh line 2 (alternative test command ([[ foo ]] should be [ foo ])):` followed by the line, and under `--lint` `posix.sh:2:1: warning: possible bashism; echo -e` (ran). The explanation is prose that changes whenever its wording does, so no check carries a stable identifier, and clauses 6.1 to 6.3 have nothing to resolve: the man page documents the options, not the checks. Clauses 4.4 and 6.4 have nothing to apply to, and there is no inline route to require a reason on (7.2).

A file checkbashisms cannot parse exits 0. For an unterminated quote it printed `error: bad.sh: Unterminated quoted string found, EOF reached. Wanted: <">, opened in line 2` and exited 0 (ran). Under reading 9 this is not graded under 5.3, since the message reaches the practitioner, but a pipeline that reads only the exit code passes the file.

Readiness is 🔴 because no bespoke rule can be written and findings carry no identifier. The detector grade is 🔴 because 4.1, 4.2 and 4.3 fail, all structural under reading 1. checkbashisms declares no version of this document.

## Clause by clause

| Document | Clause | Result         | Evidence                                                                                                                                              |
| -------- | ------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | No             | Patterns are Perl hashes in [`checkbashisms.pl`](https://salsa.debian.org/debian/devscripts/-/blob/v2.26.13/scripts/checkbashisms.pl); no load option |
| Detector | 4.2    | No             | No option selects one check ([manual page](https://salsa.debian.org/debian/devscripts/-/blob/v2.26.13/scripts/checkbashisms.1); ran)                  |
| Detector | 4.3    | No             | A finding prints its explanation text and no identifier, in both formats (ran)                                                                        |
| Detector | 4.4    | Not applicable | No rules of the project's own and no identifiers to enforce                                                                                           |
| Detector | 5.1    | Yes            | Ran locally, no infrastructure                                                                                                                        |
| Detector | 5.2    | Yes            | Ran on one file and on standard input                                                                                                                 |
| Detector | 5.3    | Yes            | Findings on standard error, or standard output with `-l`; exit 1 on a finding (ran)                                                                   |
| Detector | 5.4    | Yes            | Every check runs in the local script                                                                                                                  |
| Detector | 6.1    | No             | No identifier to resolve                                                                                                                              |
| Detector | 6.2    | No             | Same                                                                                                                                                  |
| Detector | 6.3    | No             | Same; the man page documents options, not checks                                                                                                      |
| Detector | 6.4    | Not applicable | No identifiers to document                                                                                                                            |
| Detector | 7.1    | Yes            | No suppression route in the [manual page](https://salsa.debian.org/debian/devscripts/-/blob/v2.26.13/scripts/checkbashisms.1) or the script           |
| Detector | 7.2    | Not applicable | No inline route to require a reason on                                                                                                                |

## Notes for a practitioner

checkbashisms is worth running over every `#!/bin/sh` script for its catalogue, but cannot hold a defence and gives a finding nothing to look up. Pin the devscripts version, since the patterns and their wording change with it, and treat any non-zero exit as a failure, remembering that 2 means a file was skipped. Check the parse separately, with `sh -n` or ShellCheck, because a file it cannot parse exits 0. For a project's own portability rule, use a pattern engine with a bash grammar such as [ast-grep](ast-grep.md).

## Attributes

| Attribute      | Value                                                                                                                        | Source                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Kind           | Detector                                                                                                                     | ran                                                                                                       |
| Depth          | Lexical (regular expressions over lines, with quotes and comments stripped)                                                  | [`checkbashisms.pl`](https://salsa.debian.org/debian/devscripts/-/blob/v2.26.13/scripts/checkbashisms.pl) |
| Output formats | Default prose on standard error; `--lint` as `file:line:1: warning: ...` on standard output; no SARIF                        | ran                                                                                                       |
| Exit codes     | Sum of 1 (bashism), 2 (file skipped or missing) and 4 (bash script with no bashism); 0 on a parse error; 255 on a bad option | [manual page](https://salsa.debian.org/debian/devscripts/-/blob/v2.26.13/scripts/checkbashisms.1), ran    |
| Report file    | None                                                                                                                         | manual page                                                                                               |
| Fix mode       | None                                                                                                                         | manual page                                                                                               |
| Baseline       | None                                                                                                                         | manual page                                                                                               |
| Licence        | GPL-2.0-or-later                                                                                                             | `checkbashisms --version`, ran                                                                            |
