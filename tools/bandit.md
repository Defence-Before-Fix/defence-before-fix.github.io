---
title: Bandit and Defence Before Fix
summary: Plugin entry point, test id decorator and -t selection pass 4.1 to 4.3; no resolver for 6.1; fails 8.3 on nosec and baseline
---

# Bandit

**Language**: Python · **Kind**: tool · **Readiness**: 🟢 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 1.9.4

Bandit is a security-oriented static analyser for Python from the PyCQA family. It walks the AST and runs a set of test plugins, each with an identifier such as `B101`, reporting a severity and a confidence with each issue. In a pipeline it runs alongside the general linters as the check for the hazard classes that are specifically about security: shell injection, weak hashes, hard-coded credentials and the like.

## How it is conformant

Bandit's checks are themselves plugins, and a project can add its own through the same route. [Writing tests](https://bandit.readthedocs.io/en/latest/plugins/index.html) documents the `bandit.plugins` entry point, the `@checks` decorator that selects the node types a test inspects, and the `@test_id` decorator by which the author chooses the identifier once (4.1, 4.3). The same guide's process of writing an example file in `examples/` and running Bandit against it is a fixture-based proof, and `-t B101` restricts a run to a single test ([configuration](https://bandit.readthedocs.io/en/latest/config.html)), which meets 4.2 and 5.4. Bandit accepts individual files as targets ([manual page](https://bandit.readthedocs.io/en/latest/man/bandit.html)) and prints each issue with its identifier and a terse description in the command's own output (5.1, 5.2, 5.3). Every bundled test ships its documentation as the plugin's own docstring, so the two are versioned together (6.3).

## How it is not conformant

Clause 8.3 is failed: `# nosec` and `# nosec B101` suppress inline, and the documentation says a reason is "good practice" rather than required ([configuration](https://bandit.readthedocs.io/en/latest/config.html)). The `--ignore-nosec` flag can see through the comments, but nothing bans them. The `-b` baseline option is a silent baseline in the sense the clause names. Clause 6.1 is failed: there is no command that resolves a printed `B` identifier from the installed copy, and the per-test pages are on the website (6.2). The `skips` list in the configuration file is a project record Bandit reads (8.1), but no justification is required and nothing rejects an empty one (8.2), and there is no combined listing of active tests and skips (7.1, 8.4). No version is declared (11.1).

## Clause by clause

| Clause | Result       | Evidence                                                                                       |
| ------ | ------------ | ---------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | [`bandit.plugins` entry point](https://bandit.readthedocs.io/en/latest/plugins/index.html)     |
| 4.2    | Yes          | Example file plus `-t <id>` on a single target                                                 |
| 4.3    | Yes          | `@test_id` chosen by the author and printed                                                    |
| 4.4    | No           | None                                                                                           |
| 5.1    | Yes          | `bandit <targets>` locally ([manual](https://bandit.readthedocs.io/en/latest/man/bandit.html)) |
| 5.2    | Yes          | Individual files accepted                                                                      |
| 5.3    | Yes          | Issues with ids printed to stdout                                                              |
| 5.4    | Yes          | `-t` selects a single test                                                                     |
| 6.1    | No           | No resolver keyed on the id                                                                    |
| 6.2    | No           | Per-test pages on the website                                                                  |
| 6.3    | Yes          | Docstring ships with the plugin                                                                |
| 7.1    | No           | No listing of active tests with descriptions                                                   |
| 7.2    | No           | See 7.1                                                                                        |
| 7.3    | No           | See 7.1                                                                                        |
| 8.1    | Partial      | `skips` in the config file is read, without justification                                      |
| 8.2    | No           | Reason optional ([configuration](https://bandit.readthedocs.io/en/latest/config.html))         |
| 8.3    | No           | `# nosec` and `-b` baseline                                                                    |
| 8.4    | No           | None                                                                                           |
| 8.5    | Yes          | Default test set and severities documented                                                     |
| 9.1    | No           | None                                                                                           |
| 9.2    | No           | None                                                                                           |
| 10.1   | Not verified | No release gate documented                                                                     |
| 10.2   | Not verified | Not documented                                                                                 |
| 11.1   | No           | No declaration                                                                                 |

## Notes for a practitioner

Where the class is a security hazard, write it as a Bandit plugin with a `@test_id` in a range the project reserves, keep the example file as the retained fixture, and prove it with `bandit -t <id> example.py`. Run the enforced invocation with `--ignore-nosec` so inline suppressions do nothing, and put every accepted finding in the configuration `skips` list with a comment naming the hazard and scope.
