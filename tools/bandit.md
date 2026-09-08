---
title: Bandit and Defence Before Fix
summary: Plugin entry point, test id decorator and -t selection meet 4.1 to 4.3; ignore-nosec meets 7.1; no resolver so 6.1 and 6.2 fail
language: Python
kind: tool
readiness: 🟢
detector: 🟡
checked: 2026-09-08, version 1.9.4
---

# Bandit

{% include tool-grades.html %}

Bandit is a security-oriented static analyser for Python from the PyCQA family. It walks the AST and runs a set of test plugins, each with an identifier such as `B101`, reporting a severity and a confidence with each issue. In a pipeline it runs alongside the general linters as the check for the hazard classes that are specifically about security: shell injection, weak hashes, hard-coded credentials and the like.

## How it is conformant

Bandit's checks are themselves plugins, and a project can add its own through the same route. [Writing tests](https://bandit.readthedocs.io/en/latest/plugins/index.html) documents the `bandit.plugins` entry point, the `@checks` decorator that selects the node types a test inspects, and the `@test_id` decorator by which the author chooses the identifier once, and that identifier is printed with every issue in the text and JSON formats ([4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it), [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)). The same guide's process of writing an example file in `examples/` and running Bandit against it is a fixture-based proof, and `-t B101` restricts a run to a single test ([configuration](https://bandit.readthedocs.io/en/latest/config.html)), which meets [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code) and [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally). Bandit accepts individual files as targets ([manual page](https://bandit.readthedocs.io/en/latest/man/bandit.html)) and prints each issue with its identifier and a terse description in the command's own output ([5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure), [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file), [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)). Every bundled test ships its documentation as the plugin's own docstring, so the two are versioned together ([6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)). Clause [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) holds: `# nosec` is the inline route and the `--ignore-nosec` flag makes Bandit disregard every such comment, whilst the `-b` baseline is a route only used when the flag is passed, so a project can forbid both.

## How it is not conformant

Section [6](../DETECTOR-SPEC.md#6-resolving-an-identifier) fails on resolution. There is no command that resolves a printed `B` identifier to its documentation from the installed copy ([6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)), and the per-test pages are on the website ([6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)), so the docstring that does ship is reachable only by reading the plugin source. Clause [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason) is not met: the documentation says a reason on `# nosec` is "good practice" rather than required ([configuration](https://bandit.readthedocs.io/en/latest/config.html)), and a baseline entry carries none. There is no rule over the rules that fails a plugin without a `@test_id` ([4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own)), and no release gate over the bundled documentation is documented ([6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation), not verified).

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                |
| -------- | ------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)    | Yes          | [`bandit.plugins` entry point](https://bandit.readthedocs.io/en/latest/plugins/index.html)                                              |
| Detector | [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)    | Yes          | Example file plus `-t <id>` on a single target                                                                                          |
| Detector | [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)    | Yes          | `@test_id` chosen by the author and printed                                                                                             |
| Detector | [4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own)    | No           | None                                                                                                                                    |
| Detector | [5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure)    | Yes          | `bandit <targets>` locally ([manual](https://bandit.readthedocs.io/en/latest/man/bandit.html))                                          |
| Detector | [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file)    | Yes          | Individual files accepted                                                                                                               |
| Detector | [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)    | Yes          | Issues with ids printed to stdout                                                                                                       |
| Detector | [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)    | Yes          | `-t` selects a single test                                                                                                              |
| Detector | [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)    | No           | No resolver keyed on the id                                                                                                             |
| Detector | [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)    | No           | Per-test pages on the website                                                                                                           |
| Detector | [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)    | Yes          | Docstring ships with the plugin                                                                                                         |
| Detector | [6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation)    | Not verified | No release gate documented                                                                                                              |
| Detector | [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)    | Yes          | `--ignore-nosec` disables the inline route; `-b` baseline is opt-in ([manual](https://bandit.readthedocs.io/en/latest/man/bandit.html)) |
| Detector | [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)    | No           | Reason optional ([configuration](https://bandit.readthedocs.io/en/latest/config.html))                                                  |

## Notes for a practitioner

Where the class is a security hazard, write it as a Bandit plugin with a `@test_id` in a range the project reserves, keep the example file as the retained fixture, and prove it with `bandit -t <id> example.py`. Run the enforced invocation with `--ignore-nosec` so inline suppressions do nothing, and put every accepted finding in the configuration `skips` list with a comment naming the hazard and scope.
