---
title: Flake8 and Defence Before Fix
summary: Entry point plugins with author-chosen prefix meet 4.1 to 4.3; disable-noqa meets 7.1; no resolver so 6.1 and 6.2 fail
---

# Flake8

**Language**: Python · **Kind**: tool · **Readiness**: 🟢 · **Detector conformance**: 🟡 · **Checked**: 2026-09-08, version 7.3.0

Flake8 is a thin driver that runs pyflakes, pycodestyle and mccabe and, more importantly, any plugin registered through a Python entry point. It is the origin of the letter-plus-digits code convention that Ruff later adopted, and its plugin ecosystem is why it survives Ruff: a project that needs a rule nobody has written can write it as a small package and Flake8 will run it beside everything else.

## How it is conformant

Bespoke rules are the design. [Registering plugins](https://flake8.pycqa.org/en/latest/plugin-development/registering-plugins.html) shows the `flake8.extension` entry point whose name "acts as a prefix to the error codes produced by your plugin", so the rule author chooses a code such as `X101` once and it is neither the class name nor the file path, and Flake8 prints it with every finding in its default and machine-readable formats (4.1, 4.3). `flake8 --select X101 fixture.py` runs one code against supplied code with every other code silent ([selecting violations](https://flake8.pycqa.org/en/latest/user/violations.html)), which is the harness clause 4.2 asks for, and it serves bundled and bespoke codes alike (4.2). Flake8 runs locally on one file and every plugin runs locally (5.1, 5.2, 5.4), with every finding printed with its code in the command's output (5.3). Clause 7.1 holds: `# noqa` is the inline route and the `--disable-noqa` option makes Flake8 ignore every such comment ([violations](https://flake8.pycqa.org/en/latest/user/violations.html)), so a project that forbids the route can switch it off in the enforced invocation.

## How it is not conformant

Section 6 fails for the bundled codes. There is no command that resolves a printed code to its documentation, so the practitioner must know which plugin owns the prefix and find its documentation (6.1), and for the bundled pyflakes, pycodestyle and mccabe codes that documentation is on the web rather than in the installed copy (6.2, 6.3). A bespoke plugin can ship its own descriptions, but that is the project's doing and not Flake8's. No reason is asked for on a `# noqa` comment (7.2), and there is no rule over the rules that fails a plugin without a stable prefix (4.4). No release gate over bundled documentation is documented (6.4, not verified).

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                               |
| -------- | ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Yes          | [Entry point plugins](https://flake8.pycqa.org/en/latest/plugin-development/registering-plugins.html)                  |
| Detector | 4.2    | Yes          | `--select <code>` on a fixture file ([violations](https://flake8.pycqa.org/en/latest/user/violations.html))            |
| Detector | 4.3    | Yes          | Prefix chosen by the author, printed with each finding                                                                 |
| Detector | 4.4    | No           | None                                                                                                                   |
| Detector | 5.1    | Yes          | `flake8 <file>` locally                                                                                                |
| Detector | 5.2    | Yes          | Single file accepted                                                                                                   |
| Detector | 5.3    | Yes          | Codes printed to stdout                                                                                                |
| Detector | 5.4    | Yes          | All plugins runnable locally                                                                                           |
| Detector | 6.1    | No           | No resolver keyed on the code                                                                                          |
| Detector | 6.2    | No           | Bundled code documentation is on the web                                                                               |
| Detector | 6.3    | No           | pyflakes, pycodestyle and mccabe docs do not ship keyed on the code                                                    |
| Detector | 6.4    | Not verified | No release gate documented                                                                                             |
| Detector | 7.1    | Yes          | `--disable-noqa` switches the inline route off ([violations](https://flake8.pycqa.org/en/latest/user/violations.html)) |
| Detector | 7.2    | No           | No reason on `# noqa`                                                                                                  |

## Notes for a practitioner

Write the class as a small plugin with its own prefix, register it through `flake8.extension`, and prove it with `flake8 --select <code> fixture.py` before sweeping. Run with `--disable-noqa` in the enforced invocation so inline suppressions have no effect, and keep the plugin's README in the repository next to its source so the code resolves by convention even though Flake8 offers no resolver.
