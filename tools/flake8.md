---
title: Flake8 and Defence Before Fix
summary: Entry point plugins with author-chosen prefix pass 4.1 and 4.3; no resolver for 6.1; fails 8.3 on noqa
---

# Flake8

**Language**: Python · **Kind**: tool · **Readiness**: 🟢 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 7.3.0

Flake8 is a thin driver that runs pyflakes, pycodestyle and mccabe and, more importantly, any plugin registered through a Python entry point. It is the origin of the letter-plus-digits code convention that Ruff later adopted, and its plugin ecosystem is why it survives Ruff: a project that needs a rule nobody has written can write it as a small package and Flake8 will run it beside everything else.

## How it is conformant

Bespoke rules are the design. [Registering plugins](https://flake8.pycqa.org/en/latest/plugin-development/registering-plugins.html) shows the `flake8.extension` entry point whose name "acts as a prefix to the error codes produced by your plugin", so the rule author chooses a code such as `X101` once and it is neither the class name nor the file path (4.1, 4.3). Flake8 runs locally on one file and `--select X101` restricts a run to a single code ([selecting violations](https://flake8.pycqa.org/en/latest/user/violations.html)), which is a usable harness for the red proof against a fixture file and meets 4.2 in practice as well as 5.1, 5.2 and 5.4. Every finding is printed with its code in the command's output (5.3). Because the plugin package ships its own code descriptions, documentation for a bespoke rule travels at the same version as the rule (6.3).

## How it is not conformant

Clause 8.3 is failed: `# noqa` and `# noqa: CODE` suppress inline with no justification, and although `--disable-noqa` exists to see through them, nothing bans them ([violations](https://flake8.pycqa.org/en/latest/user/violations.html)). Clause 6.1 is failed: there is no command that resolves a printed code to its documentation, so the practitioner must know which plugin owns the prefix and find its README, and that is on the network rather than the installed copy (6.2). `--extend-ignore` in the configuration file is the nearest thing to a project record, but it carries no justification and nothing enumerates it alongside the active codes (8.1, 8.2, 8.4). There is no listing of active codes with a terse statement (7.1); `flake8 --version` names the loaded plugins but not their codes. No version of the method specification is declared (11.1).

## Clause by clause

| Clause | Result       | Evidence                                                                                              |
| ------ | ------------ | ----------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | [Entry point plugins](https://flake8.pycqa.org/en/latest/plugin-development/registering-plugins.html) |
| 4.2    | Partial      | `--select <code>` on a fixture file; no dedicated harness                                             |
| 4.3    | Yes          | Prefix chosen by the author, printed with each finding                                                |
| 4.4    | No           | None                                                                                                  |
| 5.1    | Yes          | `flake8 <file>` locally                                                                               |
| 5.2    | Yes          | Single file accepted                                                                                  |
| 5.3    | Yes          | Codes printed to stdout                                                                               |
| 5.4    | Yes          | All plugins runnable locally                                                                          |
| 6.1    | No           | No resolver keyed on the code                                                                         |
| 6.2    | No           | Plugin documentation is wherever the plugin author put it                                             |
| 6.3    | Yes          | Bespoke plugin and its docs share a package                                                           |
| 7.1    | No           | `--version` lists plugins, not codes with statements                                                  |
| 7.2    | Partial      | Plugin list is derived from what is installed                                                         |
| 7.3    | Partial      | Project plugins appear in `--version` alongside bundled ones                                          |
| 8.1    | Partial      | Config file `ignore` read, without justification                                                      |
| 8.2    | No           | No reason required                                                                                    |
| 8.3    | No           | `# noqa` ([violations](https://flake8.pycqa.org/en/latest/user/violations.html))                      |
| 8.4    | No           | None                                                                                                  |
| 8.5    | Yes          | Default ignore list documented                                                                        |
| 9.1    | No           | None                                                                                                  |
| 9.2    | No           | None                                                                                                  |
| 10.1   | Not verified | No release gate documented                                                                            |
| 10.2   | Not verified | Not documented                                                                                        |
| 11.1   | No           | No declaration                                                                                        |

## Notes for a practitioner

Write the class as a small plugin with its own prefix, register it through `flake8.extension`, and prove it with `flake8 --select <code> fixture.py` before sweeping. Run with `--disable-noqa` in the enforced invocation so inline suppressions have no effect, and keep the plugin's README in the repository next to its source so the code resolves by convention even though Flake8 offers no resolver.
