---
title: Flake8 and Defence Before Fix
summary: Entry point plugins with author-chosen prefix meet 4.1 to 4.3; disable-noqa meets 7.1; no resolver so 6.1 and 6.2 fail
language: Python
kind: tool
readiness: 🟢
detector: 🟡
checked: 2026-09-08, version 7.3.0
---

# Flake8

{% include tool-grades.html %}

Flake8 is a thin driver that runs pyflakes, pycodestyle and mccabe and, more importantly, any plugin registered through a Python entry point. It is the origin of the letter-plus-digits code convention that Ruff later adopted, and its plugin ecosystem is why it survives Ruff: a project that needs a rule nobody has written can write it as a small package and Flake8 will run it beside everything else.

## How it is conformant

Bespoke rules are the design. [Registering plugins](https://flake8.pycqa.org/en/latest/plugin-development/registering-plugins.html) shows the `flake8.extension` entry point whose name "acts as a prefix to the error codes produced by your plugin", so the rule author chooses a code such as `X101` once and it is neither the class name nor the file path, and Flake8 prints it with every finding in its default and machine-readable formats ([4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it), [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)). `flake8 --select X101 fixture.py` runs one code against supplied code with every other code silent ([selecting violations](https://flake8.pycqa.org/en/latest/user/violations.html)), which is the harness clause [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code) asks for, and it serves bundled and bespoke codes alike ([4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)). Flake8 runs locally on one file and every plugin runs locally ([5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure), [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file), [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)), with every finding printed with its code in the command's output ([5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)). Clause [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) holds: `# noqa` is the inline route and the `--disable-noqa` option makes Flake8 ignore every such comment ([violations](https://flake8.pycqa.org/en/latest/user/violations.html)), so a project that forbids the route can switch it off in the enforced invocation.

## How it is not conformant

Section [6](../DETECTOR-SPEC.md#6-resolving-an-identifier) fails for the bundled codes. There is no command that resolves a printed code to its documentation, so the practitioner must know which plugin owns the prefix and find its documentation ([6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)), and for the bundled pyflakes, pycodestyle and mccabe codes that documentation is on the web rather than in the installed copy ([6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access), [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)). A bespoke plugin can ship its own descriptions, but that is the project's doing and not Flake8's. No reason is asked for on a `# noqa` comment ([7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)), and there is no rule over the rules that fails a plugin without a stable prefix ([4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own)). No release gate over bundled documentation is documented ([6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation), not verified).

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                               |
| -------- | ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Detector | [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)    | Yes          | [Entry point plugins](https://flake8.pycqa.org/en/latest/plugin-development/registering-plugins.html)                  |
| Detector | [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)    | Yes          | `--select <code>` on a fixture file ([violations](https://flake8.pycqa.org/en/latest/user/violations.html))            |
| Detector | [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)    | Yes          | Prefix chosen by the author, printed with each finding                                                                 |
| Detector | [4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own)    | No           | None                                                                                                                   |
| Detector | [5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure)    | Yes          | `flake8 <file>` locally                                                                                                |
| Detector | [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file)    | Yes          | Single file accepted                                                                                                   |
| Detector | [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)    | Yes          | Codes printed to stdout                                                                                                |
| Detector | [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)    | Yes          | All plugins runnable locally                                                                                           |
| Detector | [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)    | No           | No resolver keyed on the code                                                                                          |
| Detector | [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)    | No           | Bundled code documentation is on the web                                                                               |
| Detector | [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)    | No           | pyflakes, pycodestyle and mccabe docs do not ship keyed on the code                                                    |
| Detector | [6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation)    | Not verified | No release gate documented                                                                                             |
| Detector | [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)    | Yes          | `--disable-noqa` switches the inline route off ([violations](https://flake8.pycqa.org/en/latest/user/violations.html)) |
| Detector | [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)    | No           | No reason on `# noqa`                                                                                                  |

## Notes for a practitioner

Write the class as a small plugin with its own prefix, register it through `flake8.extension`, and prove it with `flake8 --select <code> fixture.py` before sweeping. Run with `--disable-noqa` in the enforced invocation so inline suppressions have no effect, and keep the plugin's README in the repository next to its source so the code resolves by convention even though Flake8 offers no resolver.
