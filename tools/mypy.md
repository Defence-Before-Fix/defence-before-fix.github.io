---
title: mypy and Defence Before Fix
summary: Type checker; plugin hooks give partial 4.1 with no harness for 4.2; website-only codes fail 6.2 and 6.3; type ignore fails 7.1
---

# mypy

**Language**: Python · **Kind**: tool · **Readiness**: 🟡 · **Detector conformance**: 🔴 · **Checked**: 2026-09-08, version 2.3.1

mypy is a static type checker rather than a rule engine. Its findings are type errors, each tagged with an error code such as `[attr-defined]`, and its role in a pipeline is to enforce the type discipline the project has chosen. It has a plugin system, which is what makes it a candidate for hosting a bespoke defence at all, but the plugin system exists to teach mypy about libraries, not to add lint rules.

## How it is conformant

mypy runs locally and on a single file (5.1, 5.2), prints every error in its own output with the error code in brackets (5.3, 5.4), and lets a code be enabled or disabled globally or per module ([error codes](https://mypy.readthedocs.io/en/stable/error_codes.html)). The bundled error codes are stable identifiers printed with every finding (4.3, for bundled codes). [Extending mypy](https://mypy.readthedocs.io/en/stable/extending_mypy.html) documents a plugin mechanism, loaded through `plugins =` in the configuration file, whose hooks receive "an API to create new nodes, new types, emit error messages, etc.", so a project can in principle emit a bespoke error from a hook on a function, method, attribute or class (4.1, partial).

## How it is not conformant

Clause 4.1 is only partly met and 4.2 is not. The plugin hooks fire on specific type-checking events, not on arbitrary syntax, so many classes cannot be expressed, and the page states the system is "experimental and prone to change" with "no guarantees about backwards compatibility". Whether a plugin error can carry its own bracketed code was not verified from the documentation, so 4.3 is partial for bespoke rules. There is no harness for running one plugin, or one bundled code, against a fixture other than mypy's own test framework: `--enable-error-code` and `--disable-error-code` narrow the set, but the documentation offers no route to run a single code alone (4.2). Section 6 fails for bundled codes: they are documented on the website, keyed on the code, but no command resolves a code from the installed package (6.1 partial, 6.2 no) and the documentation does not ship with the package (6.3). Clause 7.1 is failed: `# type: ignore` and `# type: ignore[code]` suppress inline, the documentation presents that as the primary silencing route ([error codes](https://mypy.readthedocs.io/en/stable/error_codes.html)), no setting disables it, and the plugin hooks cannot see a comment, so a project cannot detect it in mypy itself. `warn_unused_ignores` reports only an ignore that no longer suppresses anything. No reason is asked for (7.2).

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                              |
| -------- | ------ | ------------ | ----------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Partial      | [Plugins](https://mypy.readthedocs.io/en/stable/extending_mypy.html) can emit errors from typed hooks |
| Detector | 4.2    | No           | No single-rule harness documented                                                                     |
| Detector | 4.3    | Partial      | Bundled codes stable and printed; plugin-defined codes not verified                                   |
| Detector | 4.4    | No           | None                                                                                                  |
| Detector | 5.1    | Yes          | `mypy <file>` locally                                                                                 |
| Detector | 5.2    | Yes          | Single file accepted                                                                                  |
| Detector | 5.3    | Yes          | Codes printed in brackets ([error codes](https://mypy.readthedocs.io/en/stable/error_codes.html))     |
| Detector | 5.4    | Yes          | All checks runnable locally                                                                           |
| Detector | 6.1    | Partial      | Website index keyed on code; no command                                                               |
| Detector | 6.2    | No           | Resolution needs the website                                                                          |
| Detector | 6.3    | No           | Documentation lives on the website, not in the package                                                |
| Detector | 6.4    | Not verified | No release gate documented                                                                            |
| Detector | 7.1    | No           | `# type: ignore[code]` cannot be disabled or detected in mypy                                         |
| Detector | 7.2    | No           | No reason required                                                                                    |

## Notes for a practitioner

Treat mypy as a detector for type-shaped classes only: where the class is "this value can be None here", tightening the configuration is a legitimate off-the-shelf rule under method clause 3.2, proven by watching the count go red. For any other class, host the defence in Pylint or a Flake8 plugin instead, and enable `warn_unused_ignores` plus a check in a second detector on new `# type: ignore` comments so the inline route stays visible.
