---
title: Pylint and Defence Before Fix
summary: Custom checkers, test harness and author-chosen ids; help-msg and list-msgs resolve and list; fails 8.3 on inline disable comments
---

# Pylint

**Language**: Python · **Kind**: tool · **Readiness**: 🟢 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 4.0.8

Pylint is the oldest general-purpose Python linter still in wide use, built on the astroid AST library and organised as a set of checkers that emit messages with numeric identifiers such as `W0611` and symbolic names such as `unused-import`. In a pipeline it is slower than Ruff and is kept for its deeper inference and, above all, for the fact that a project can write its own checkers and register them alongside the bundled ones.

## How it is conformant

Pylint is the strongest Python tool on section 4. The [custom checker guide](https://pylint.readthedocs.io/en/stable/development_guide/how_tos/custom_checkers.html) shows a project subclassing `BaseChecker`, declaring a `msgs` dictionary that maps a chosen identifier and symbolic name to the message text and description, and enabling it through `load-plugins` in the configuration (4.1). The identifier is chosen once by the rule author and is not derived from the class or file name (4.3), and the same guide describes `CheckerTestCase` with `assertAddsMessages` for proving a checker against a fixture without running the project's tests (4.2). Locally, `pylint mymodule.py` runs on a single file, and `--disable=all --enable=<symbol>` runs one rule in isolation ([running Pylint](https://pylint.readthedocs.io/en/stable/user_guide/usage/run.html)), which meets 5.1, 5.2 and 5.4. Every message is printed with its identifier in the command's output (5.3). `pylint --help-msg=<msg-id>` resolves a printed identifier to its description offline (6.1, 6.2), and because a custom checker's description lives in its own `msgs` entry, the same command resolves project identifiers too (6.3). `--list-msgs` enumerates every message the active configuration knows, bundled and custom alike, with its terse text (7.1, 7.2, 7.3).

## How it is not conformant

Clause 8.3 is failed: `# pylint: disable=<symbol>` suppresses any message inline with no justification and no bundled defence against it ([message control](https://pylint.readthedocs.io/en/stable/user_guide/usage/run.html)). The `disable=` list in the configuration file is the nearest thing to a project record, but Pylint attaches no justification to an entry (8.1, 8.2) and nothing lists the disabled set next to the active one as one operation (8.4). Nothing under section 9 exists. Pylint runs its own checks on its own source, but no release-blocking audit that every bundled message has documentation is published (10.1 not verified). No method specification version is declared (11.1).

## Clause by clause

| Clause | Result       | Evidence                                                                                                                     |
| ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | [Custom checkers](https://pylint.readthedocs.io/en/stable/development_guide/how_tos/custom_checkers.html) via `load-plugins` |
| 4.2    | Yes          | `CheckerTestCase` in the same guide                                                                                          |
| 4.3    | Yes          | `msgs` id and symbolic name chosen by the author                                                                             |
| 4.4    | No           | No rule requiring identifiers on checkers                                                                                    |
| 5.1    | Yes          | `pylint <module>` ([running Pylint](https://pylint.readthedocs.io/en/stable/user_guide/usage/run.html))                      |
| 5.2    | Yes          | Single file accepted                                                                                                         |
| 5.3    | Yes          | Messages with ids printed to stdout                                                                                          |
| 5.4    | Yes          | `--disable=all --enable=<symbol>`                                                                                            |
| 6.1    | Yes          | `--help-msg=<msg-id>`                                                                                                        |
| 6.2    | Yes          | Works from the installed package                                                                                             |
| 6.3    | Yes          | Description travels in the checker's `msgs`                                                                                  |
| 7.1    | Yes          | `--list-msgs`                                                                                                                |
| 7.2    | Yes          | Derived from loaded checkers                                                                                                 |
| 7.3    | Yes          | Plugin messages appear in the same listing                                                                                   |
| 8.1    | Partial      | Configuration `disable=` is read, but carries no justification                                                               |
| 8.2    | No           | No reason required                                                                                                           |
| 8.3    | No           | `# pylint: disable=` inline                                                                                                  |
| 8.4    | No           | Disabled set not listed with active set as one operation                                                                     |
| 8.5    | Yes          | Default enabled set documented                                                                                               |
| 9.1    | No           | None                                                                                                                         |
| 9.2    | No           | None                                                                                                                         |
| 10.1   | Not verified | No published release gate found                                                                                              |
| 10.2   | Not verified | Pylint lints itself, but no release gate documented                                                                          |
| 11.1   | No           | No declaration                                                                                                               |

## Notes for a practitioner

Write the class as a checker under `load-plugins`, choose a message id in the custom range the guide recommends, prove it with `CheckerTestCase` and then with `--disable=all --enable=<symbol>` on the originating file. Forbid `# pylint: disable` in the project's own checker or in review, since Pylint will not, and keep every configuration-level `disable=` entry beside a comment naming the hazard and scope.
