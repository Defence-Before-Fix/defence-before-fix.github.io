---
title: HTMLHint and Defence Before Fix
summary: Rules from --rulesdir run alone with --rules, meeting 4.1 and 4.2; checkstyle and HTML reports leave 4.3 partial; rule pages online only fail 6.3; a stripped first-line ruleset comment leaves 7.1 partial
language: HTML
kind: tool
readiness: 🟢
detector: 🟡
checked: 2026-10-10, version 1.9.2
---

# HTMLHint

{% include tool-grades.html %}

HTMLHint is a small static analyser for HTML written in JavaScript. It runs an event parser over the markup, not a DOM, and reports findings from a set of rules with short identifiers such as `id-unique` and `tag-pair`; the default ruleset is a handful of them. In a pipeline it is a fast first check on hand-written HTML, and it accepts rules a project writes in JavaScript.

## How it is conformant

A bespoke rule is a module that calls `HTMLHint.addRule()` with an `id`, a `description` and an `init(parser, reporter)` that listens on parser events, loaded with `--rulesdir` ([options](https://htmlhint.com/usage/options/)). A rule with `id: "proj-no-b"` loaded that way ran beside the bundled rules ([4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)), and `htmlhint -R rules --rules proj-no-b a.html` ran it alone on the fixture, ignoring the `.htmlhintrc`, and printed only its finding; `--rules id-unique` did the same for a bundled rule ([4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)). The identifier is the `id` the author writes into the rule, printed unaltered as `(proj-no-b)` in the default output and the compact, JUnit and markdown formats, as `[error/proj-no-b]` in unix, and as `rule.id` and `ruleId` in JSON and SARIF.

Section [5](../DETECTOR-SPEC.md#5-reporting) holds. HTMLHint ran locally with no infrastructure, on a single file and on standard input as `htmlhint stdin` ([CLI](https://htmlhint.com/usage/cli/)), and every finding was printed in the command's output with exit 1 ([5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure) to [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)).

For [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation), a bundled identifier resolves by a URL keyed on it, `https://htmlhint.com/rules/<id>`, which the JSON output carries as `rule.link` and SARIF as `helpUri`; all 44 bundled identifiers in the installed package returned HTTP 200 there. `htmlhint --list` prints every bundled identifier with its one-line description from the installed package, without the network.

## How it is not conformant

Clause [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding) is partial. The checkstyle format prints only `source="htmlhint.proj-no-b"`, a prefixed form, with no identifier in the message, and the HTML report format prints the file, line and message with no identifier at all.

Clause [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access) is partial: `--list` gives a sentence per rule offline, but the rule pages are on the website. Clause [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together) fails: the package ships `bin` and `dist` only ([source at the tag](https://github.com/htmlhint/HTMLHint/tree/v1.9.2)), so no page travels with a rule. For a project rule HTMLHint builds the same URL from the identifier ([reporter at the tag](https://github.com/htmlhint/HTMLHint/blob/v1.9.2/src/core/reporter.ts)), so JSON and SARIF printed `https://htmlhint.com/rules/proj-no-b`, which returned HTTP 404: a dangling link the project did not write and cannot change. Project rules are also absent from `--list`.

Clause [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) is partial. Three inline routes exist ([configuration](https://htmlhint.com/configuration/)): `<!-- htmlhint-disable-next-line rule -->`, `<!-- htmlhint-disable -->` until `<!-- htmlhint-enable -->`, and a ruleset comment on the first line, `<!-- htmlhint rule:false -->`. All three are parsed unconditionally ([core at the tag](https://github.com/htmlhint/HTMLHint/blob/v1.9.2/src/core/core.ts)) and no option turns them off. A project rule on the parser's `comment` event reported the line-level directive, so that route is detectable, but `<!-- htmlhint-disable -->` hid the rule's report of that same comment and of everything after it. The first-line ruleset comment is removed from the source before parsing, so no rule ever sees it: a file starting `<!-- htmlhint proj-no-b:false -->` switched the project rule off, the rule watching for directives did not report the comment, and the run printed nothing and exited 0. No reason is asked for on any directive ([7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)). There is no rule over the rules, and a rule added with an empty `id` ran and reported under an empty identifier ([4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own)). No release gate over the rule pages was found ([6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation), not verified).

A nonexistent file printed "Scanned 0 files, no errors found" and exited 0; the summary is in the output, but a check that reads only the exit status passes.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                                           |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Detector | [4.1](../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)    | Yes          | Ran a `--rulesdir` rule, `proj-no-b` ([options](https://htmlhint.com/usage/options/))                                                                              |
| Detector | [4.2](../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)    | Yes          | Ran `--rules proj-no-b` and `--rules id-unique` alone on a fixture                                                                                                 |
| Detector | [4.3](../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)    | Partial      | Ran the default and all eight `-f` formats: unaltered in default, compact, unix, JSON, SARIF, JUnit and markdown; `htmlhint.proj-no-b` in checkstyle; none in HTML |
| Detector | [4.4](../DETECTOR-SPEC.md#44-the-detector-should-enforce-43-with-a-rule-of-its-own)    | No           | No rule over the rules; ran a rule with an empty `id`, accepted                                                                                                    |
| Detector | [5.1](../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure)    | Yes          | Ran locally, no infrastructure                                                                                                                                     |
| Detector | [5.2](../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file)    | Yes          | Ran on one file and on `stdin` ([CLI](https://htmlhint.com/usage/cli/))                                                                                            |
| Detector | [5.3](../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)    | Yes          | Findings in the command's output, exit 1                                                                                                                           |
| Detector | [5.4](../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)    | Yes          | Every rule runs in the local package                                                                                                                               |
| Detector | [6.1](../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)    | Yes          | `https://htmlhint.com/rules/<id>` in JSON and SARIF; all 44 bundled identifiers returned HTTP 200                                                                  |
| Detector | [6.2](../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)    | Partial      | `--list` gives one-line descriptions offline; pages online                                                                                                         |
| Detector | [6.3](../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)    | No           | Package ships `bin` and `dist` only; a project rule is given a 404 link                                                                                            |
| Detector | [6.4](../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation)    | Not verified | No release gate over rule pages found                                                                                                                              |
| Detector | [7.1](../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)    | Partial      | Ran: line directive detectable by a project rule; `htmlhint-disable` hides the report; first-line ruleset comment invisible to rules, no switch                    |
| Detector | [7.2](../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)    | No           | No reason asked for on any directive                                                                                                                               |

## Notes for a practitioner

Write the rule with `HTMLHint.addRule()` in a `--rulesdir` folder, choose an identifier with the project's own prefix, and prove it with `--rules <id>` on the fixture. Use the default, unix, compact or JSON output where the identifier matters, ignore the `link` HTMLHint attaches to a project rule, and keep the rule's documentation in the project. Because HTMLHint cannot switch its directives off and a rule cannot see all of them, forbid `htmlhint` comments with a search in the project's own checks, and run it on files you know exist, since a missing path passes.
