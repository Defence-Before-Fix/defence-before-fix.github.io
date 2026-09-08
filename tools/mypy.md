---
title: mypy and Defence Before Fix
summary: Type checker; plugin hooks give partial 4.1 with no harness for 4.2; website-only codes fail 6.2 and 6.3; type ignore fails 7.1
language: Python
kind: tool
readiness: 🟡
detector: 🔴
checked: 2026-09-08, version 2.3.1
---

# mypy

{% include tool-grades.html %}

mypy is a static type checker rather than a rule engine. Its findings are type errors, each tagged with an error code such as `[attr-defined]`, and its role in a pipeline is to enforce the type discipline the project has chosen. It has a plugin system, which is what makes it a candidate for hosting a bespoke defence at all, but the plugin system exists to teach mypy about libraries, not to add lint rules.

## How it is conformant

mypy runs locally and on a single file ([5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure), [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file)), prints every error in its own output with the error code in brackets ([5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran), [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)), and lets a code be enabled or disabled globally or per module ([error codes](https://mypy.readthedocs.io/en/stable/error_codes.html)). The bundled error codes are stable identifiers printed with every finding ([4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding), for bundled codes). [Extending mypy](https://mypy.readthedocs.io/en/stable/extending_mypy.html) documents a plugin mechanism, loaded through `plugins =` in the configuration file, whose hooks receive "an API to create new nodes, new types, emit error messages, etc.", so a project can in principle emit a bespoke error from a hook on a function, method, attribute or class ([4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it), partial).

## How it is not conformant

Clause [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it) is only partly met and [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code) is not. The plugin hooks fire on specific type-checking events, not on arbitrary syntax, so many classes cannot be expressed, and the page states the system is "experimental and prone to change" with "no guarantees about backwards compatibility". Whether a plugin error can carry its own bracketed code was not verified from the documentation, so [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding) is partial for bespoke rules. There is no harness for running one plugin, or one bundled code, against a fixture other than mypy's own test framework: `--enable-error-code` and `--disable-error-code` narrow the set, but the documentation offers no route to run a single code alone ([4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)). Section [6](../DETECTOR-SPEC.md#6-resolving-an-identifier) fails for bundled codes: they are documented on the website, keyed on the code, but no command resolves a code from the installed package ([6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation) partial, [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access) no) and the documentation does not ship with the package ([6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)). Clause [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) is failed: `# type: ignore` and `# type: ignore[code]` suppress inline, the documentation presents that as the primary silencing route ([error codes](https://mypy.readthedocs.io/en/stable/error_codes.html)), no setting disables it, and the plugin hooks cannot see a comment, so a project cannot detect it in mypy itself. `warn_unused_ignores` reports only an ignore that no longer suppresses anything. No reason is asked for ([7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)).

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                              |
| -------- | ------ | ------------ | ----------------------------------------------------------------------------------------------------- |
| Detector | [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)    | Partial      | [Plugins](https://mypy.readthedocs.io/en/stable/extending_mypy.html) can emit errors from typed hooks |
| Detector | [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)    | No           | No single-rule harness documented                                                                     |
| Detector | [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)    | Partial      | Bundled codes stable and printed; plugin-defined codes not verified                                   |
| Detector | [4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own)    | No           | None                                                                                                  |
| Detector | [5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure)    | Yes          | `mypy <file>` locally                                                                                 |
| Detector | [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file)    | Yes          | Single file accepted                                                                                  |
| Detector | [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)    | Yes          | Codes printed in brackets ([error codes](https://mypy.readthedocs.io/en/stable/error_codes.html))     |
| Detector | [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)    | Yes          | All checks runnable locally                                                                           |
| Detector | [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)    | Partial      | Website index keyed on code; no command                                                               |
| Detector | [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)    | No           | Resolution needs the website                                                                          |
| Detector | [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)    | No           | Documentation lives on the website, not in the package                                                |
| Detector | [6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation)    | Not verified | No release gate documented                                                                            |
| Detector | [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)    | No           | `# type: ignore[code]` cannot be disabled or detected in mypy                                         |
| Detector | [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)    | No           | No reason required                                                                                    |

## Notes for a practitioner

Treat mypy as a detector for type-shaped classes only: where the class is "this value can be None here", tightening the configuration is a legitimate off-the-shelf rule under method clause [3.2](../SPEC.md#32-build-the-net), proven by watching the count go red. For any other class, host the defence in Pylint or a Flake8 plugin instead, and enable `warn_unused_ignores` plus a check in a second detector on new `# type: ignore` comments so the inline route stays visible.
