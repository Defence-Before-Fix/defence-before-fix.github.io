---
title: vulture and Defence Before Fix
summary: A fixed dead-code check with no plugin interface fails 4.1 and 4.2, and its findings carry no identifier, failing 4.3 and leaving section 6 with nothing to resolve; runs locally on one file, meeting section 5; a noqa comment can be neither switched off nor reported, failing 7.1
language: Python
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-10-10, version 2.16
---

# vulture

{% include tool-grades.html %}

vulture finds unused code in Python: imports, functions, classes, methods, properties, attributes and variables that are defined but never used, and code that cannot be reached after a `return`, `break`, `continue` or `raise` or under an unsatisfiable condition ([README](https://github.com/jendrikseipp/vulture/blob/v2.16/README.md)). It builds an AST of every file it is given, records the names defined and the names used, and reports the difference, ignoring scopes. Each finding carries a confidence between 60% and 100%. In a pipeline it sits beside a linter as a periodic or pre-commit sweep for dead code, usually with a whitelist module of names the project uses dynamically.

## How it is conformant

Section 5 is met. vulture runs locally on any file or directory with no network and no service (ran under `unshare -rn` at 2.16), so clauses 5.1 and 5.4 hold. Clause 5.2 holds: `vulture bad.py` analysed that one file and reported its findings, though the analysis is over whatever it is given, so a function used only from another module is reported unused unless that module is passed as well (at 2.16, `f` in `bad.py` was reported unused alone and not reported with `caller.py` beside it). Clause 5.3 holds: every finding prints in the command's own output as `bad.py:1: unused import 'os' (90% confidence)`, and there is no option that writes the report elsewhere ([`config.py`](https://github.com/jendrikseipp/vulture/blob/v2.16/vulture/config.py)).

## How it is not conformant

Clause 4.1 fails: vulture has no plugin interface and no rule language. Its checks are the fixed kinds of unused code the README lists, and the project can only adjust them, with `--min-confidence`, `--ignore-names`, `--ignore-decorators`, `--exclude` and whitelist modules ([`config.py`](https://github.com/jendrikseipp/vulture/blob/v2.16/vulture/config.py), `vulture --help` at 2.16). Clause 4.2 is graded on the bundled checks and fails too: no option selects one kind of finding. `--min-confidence 100` keeps the 100% kinds only, which are unused arguments and unreachable code together, and nothing narrower exists (ran).

Clause 4.3 fails: a finding prints its location, a description and a confidence, `plain.py:6: unused function 'f' (60% confidence)`, and no identifier, and that line is the only output format (ran). The source holds codes for the kinds, `V101` to `V107` and `V201` ([`core.py`](https://github.com/jendrikseipp/vulture/blob/v2.16/vulture/core.py#L31)), but they are used only to match `# noqa` comments and are never printed. The README's table of them is inside an HTML comment, so it is not shown, and it gives `V105` as a property and `V106` as a method where the source has them the other way round. With nothing printed, clauses 6.1, 6.2 and 6.3 fail: there is no identifier for a mechanism to resolve (reading 14). Clauses 4.4 and 6.4 do not apply, since there are no rules of the project's own and no identifiers.

Clause 7.1 fails. The inline route is a `# noqa` comment, bare or with codes, matched by the expression in [`noqa.py`](https://github.com/jendrikseipp/vulture/blob/v2.16/vulture/noqa.py) and honoured for `V`-codes and for flake8's `F401` and `F841`; at 2.16 `import sys  # noqa: V104`, `import re  # noqa` and `import json  # noqa: F401` were all left unreported. No option or configuration key switches it off: none is in `--help` or [`config.py`](https://github.com/jendrikseipp/vulture/blob/v2.16/vulture/config.py), and a `pyproject.toml` with `noqa = false` was refused with `Unknown configuration key: noqa` and exit 2 (ran). Nor does vulture report it: the default output says nothing, and there are no rules a project could write to see it. `--verbose` prints a debugging trace in which a suppressed item appears as `Ignoring import "sys"` ([`core.py`](https://github.com/jendrikseipp/vulture/blob/v2.16/vulture/core.py#L448)), but the same line is printed for a name matched by `--ignore-names`, the trace does not name the route, and neither `--help` nor the README describes the flag as reporting suppressions; under reading 18 the register does not count it as a check the detector documents. The whitelist module, `--ignore-names` and `--ignore-decorators` apply only where the invocation or `pyproject.toml` names them, so a project that names none has them off. Clause 7.2 is not met: a `# noqa` takes no reason.

The detector grade is 🔴: 4.1 is a structural MUST and fails, and so does 4.2; 4.3, 6.1 to 6.3 and 7.1 fail as well. Readiness is 🔴: there are no bespoke rules and no identifier on a finding. vulture declares no version of this document.

## Clause by clause

| Document | Clause | Result         | Evidence                                                                                                                                                                                                              |
| -------- | ------ | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | No             | Fixed checks; options only adjust them ([`config.py`](https://github.com/jendrikseipp/vulture/blob/v2.16/vulture/config.py))                                                                                          |
| Detector | 4.2    | No             | No option selects one kind of finding; `--min-confidence 100` keeps two kinds (ran)                                                                                                                                   |
| Detector | 4.3    | No             | A finding prints a description and a confidence, no identifier; the `V` codes are never printed ([`core.py`](https://github.com/jendrikseipp/vulture/blob/v2.16/vulture/core.py#L31); ran)                            |
| Detector | 4.4    | Not applicable | No rules of the project's own and no identifiers to enforce                                                                                                                                                           |
| Detector | 5.1    | Yes            | Ran locally with the network removed                                                                                                                                                                                  |
| Detector | 5.2    | Yes            | One file runs; results cover only the files given (ran)                                                                                                                                                               |
| Detector | 5.3    | Yes            | Findings in the command's output; no report file option (ran)                                                                                                                                                         |
| Detector | 5.4    | Yes            | Every check runs locally                                                                                                                                                                                              |
| Detector | 6.1    | No             | No identifier to resolve                                                                                                                                                                                              |
| Detector | 6.2    | No             | Same, reading 14                                                                                                                                                                                                      |
| Detector | 6.3    | No             | Same                                                                                                                                                                                                                  |
| Detector | 6.4    | Not applicable | No identifiers to document                                                                                                                                                                                            |
| Detector | 7.1    | No             | `# noqa` has no switch (`noqa = false` refused, ran) and is not reported; the `--verbose` trace does not name the route ([`noqa.py`](https://github.com/jendrikseipp/vulture/blob/v2.16/vulture/noqa.py)), reading 18 |
| Detector | 7.2    | No             | `# noqa` takes no reason                                                                                                                                                                                              |

## Notes for a practitioner

vulture cannot host a defence: there is nothing to write a rule in and nothing to key a lookup on. It can still be part of a toolchain as a dead-code sweep, with the toolchain supplying what it lacks: an identifier of the toolchain's own attached to its output, a text search outside vulture that fails on `# noqa` comments the project has not approved (vulture honours flake8's `F401` and `F841` codes as well as its own, so a comment written for flake8 silences it too), and a run over the whole package with the whitelist, since a single-file run reports as unused whatever the other files use. A variable whose name begins with an underscore is never reported, by design ([README](https://github.com/jendrikseipp/vulture/blob/v2.16/README.md)); an unused function named that way still is (ran). Exit codes are 3 for dead code, 1 for invalid input and 2 for invalid arguments ([README](https://github.com/jendrikseipp/vulture/blob/v2.16/README.md#exit-codes)), but a run over a file that does not parse beside a file with findings exited 3 (ran), so the parse error does not show in the exit code when there are findings as well.

## Attributes

| Attribute      | Value                                                                              | Source                                                                                  |
| -------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Kind           | Detector (dead-code finder)                                                        | [README](https://github.com/jendrikseipp/vulture/blob/v2.16/README.md)                  |
| Depth          | Syntactic: names defined and used across the given files, scopes ignored           | [README](https://github.com/jendrikseipp/vulture/blob/v2.16/README.md#how-does-it-work) |
| Rule form      | None: no plugin interface                                                          | [`config.py`](https://github.com/jendrikseipp/vulture/blob/v2.16/vulture/config.py)     |
| Output formats | One text line per finding, or a whitelist module with `--make-whitelist`; no SARIF | ran                                                                                     |
| Exit codes     | 3 on a finding, 2 on a usage error, 1 on an unparseable file with no findings      | ran                                                                                     |
| Report file    | None                                                                               | [`config.py`](https://github.com/jendrikseipp/vulture/blob/v2.16/vulture/config.py)     |
| Baseline       | `--make-whitelist` writes a whitelist module of every current finding              | ran                                                                                     |
| Licence        | MIT                                                                                | [LICENSE.txt](https://github.com/jendrikseipp/vulture/blob/v2.16/LICENSE.txt)           |
