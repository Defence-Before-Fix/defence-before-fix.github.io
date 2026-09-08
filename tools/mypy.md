---
title: mypy and Defence Before Fix
summary: Type checker; plugin hooks give partial 4.1 and no harness for 4.2; docs website only for 6.2; fails 8.3 on type ignore
---

# mypy

**Language**: Python · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 2.3.1

mypy is a static type checker rather than a rule engine. Its findings are type errors, each tagged with an error code such as `[attr-defined]`, and its role in a pipeline is to enforce the type discipline the project has chosen. It has a plugin system, which is what makes it a candidate for hosting a bespoke defence at all, but the plugin system exists to teach mypy about libraries, not to add lint rules.

## How it is conformant

mypy runs locally and on a single file (5.1, 5.2), prints every error in its own output with the error code in brackets (5.3, 5.4), and lets a code be enabled or disabled globally or per module ([error codes](https://mypy.readthedocs.io/en/stable/error_codes.html)). The bundled error codes are stable identifiers documented on that page (4.3, for bundled codes). [Extending mypy](https://mypy.readthedocs.io/en/stable/extending_mypy.html) documents a plugin mechanism, loaded through `plugins =` in the configuration file, whose hooks receive "an API to create new nodes, new types, emit error messages, etc.", so a project can in principle emit a bespoke error from a hook on a function, method, attribute or class (4.1, partial). The default configuration is documented, which meets 8.5.

## How it is not conformant

Clause 4.1 is only partly met and 4.2 is not. The plugin hooks fire on specific type-checking events, not on arbitrary syntax, so many classes cannot be expressed, and the page states the system is "experimental and prone to change" with "no guarantees about backwards compatibility". Whether a plugin error can carry its own bracketed code was not verified from the documentation. There is no harness for running one plugin against a fixture other than mypy's own test framework (4.2). Clause 8.3 is failed: `# type: ignore` and `# type: ignore[code]` suppress inline with no justification, and mypy documents that as the primary silencing route ([error codes](https://mypy.readthedocs.io/en/stable/error_codes.html)). Clause 6.1 is failed in the offline sense: error codes are documented on the website, and no command resolves a code from the installed package (6.2 not met). Nothing lists active checks with identifiers (7.1), no project record with justifications exists (8.1, 8.2, 8.4), and no version is declared (11.1).

## Clause by clause

| Clause | Result       | Evidence                                                                                              |
| ------ | ------------ | ----------------------------------------------------------------------------------------------------- |
| 4.1    | Partial      | [Plugins](https://mypy.readthedocs.io/en/stable/extending_mypy.html) can emit errors from typed hooks |
| 4.2    | No           | No single-rule harness documented                                                                     |
| 4.3    | Partial      | Bundled codes stable; plugin-defined codes not verified                                               |
| 4.4    | No           | None                                                                                                  |
| 5.1    | Yes          | `mypy <file>` locally                                                                                 |
| 5.2    | Yes          | Single file accepted                                                                                  |
| 5.3    | Yes          | Codes printed in brackets ([error codes](https://mypy.readthedocs.io/en/stable/error_codes.html))     |
| 5.4    | Yes          | All checks runnable locally                                                                           |
| 6.1    | Partial      | Website index keyed on code; no command                                                               |
| 6.2    | No           | Resolution needs the website                                                                          |
| 6.3    | No           | Documentation lives on the website, not in the package                                                |
| 7.1    | No           | No listing of active codes with descriptions                                                          |
| 7.2    | No           | See 7.1                                                                                               |
| 7.3    | No           | See 7.1                                                                                               |
| 8.1    | Partial      | `disable_error_code` in config is read, without justification                                         |
| 8.2    | No           | No reason required                                                                                    |
| 8.3    | No           | `# type: ignore[code]`                                                                                |
| 8.4    | No           | None                                                                                                  |
| 8.5    | Yes          | Defaults documented                                                                                   |
| 9.1    | No           | None                                                                                                  |
| 9.2    | No           | None                                                                                                  |
| 10.1   | Not verified | No release gate documented                                                                            |
| 10.2   | Not verified | mypy type-checks itself, but no release gate documented                                               |
| 11.1   | No           | No declaration                                                                                        |

## Notes for a practitioner

Treat mypy as a detector for type-shaped classes only: where the class is "this value can be None here", tightening the configuration is a legitimate off-the-shelf rule under method clause 3.2, proven by watching the count go red. For any other class, host the defence in Pylint or a Flake8 plugin instead, and enable `warn_unused_ignores` plus a review ban on new `# type: ignore` comments so the inline route stays visible.
