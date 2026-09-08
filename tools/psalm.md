---
title: Psalm and Defence Before Fix
summary: Plugin issues meet 4.1 and section 5; the harness under 4.2 is third party, bundled documentation online only fails 6.2 and 6.3, psalm-suppress weakens 7.1.
---

# Psalm

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Detector conformance**: 🟡 · **Checked**: 2026-09-08, version 6.16.1

Psalm is a static analyser for PHP with a strong type system and a plugin API. In a pipeline it plays the same role as PHPStan, and many projects run both; for this method it is a detector that can host a bespoke rule through a plugin.

## How it is conformant

Clause 4.1 is met: a plugin hooks into analysis events and can emit an issue of its own by extending `Psalm\Issue\PluginIssue` ([authoring plugins](https://psalm.dev/docs/running_psalm/plugins/authoring_plugins/)). Clause 4.3 is met in part, because a plugin issue carries a name the author chooses, that name is what `@psalm-suppress` and `<PluginIssue name="...">` key on, and it is printed as the issue type with every finding. Clauses 5.1 to 5.4 hold: `vendor/bin/psalm file1.php` runs locally on a named file and prints its findings to the terminal, with `--report` adding a file rather than replacing the output ([command line usage](https://psalm.dev/docs/running_psalm/command_line_usage/)). Clause 6.1 is met for bundled issues, whose catalogue on psalm.dev is keyed on the printed issue name, which is the URL form the clause accepts. Clause 7.1 is met for the baseline, which is active only whilst the configuration names an `errorBaseline` file ([dealing with code issues](https://psalm.dev/docs/running_psalm/dealing_with_code_issues/)).

## How it is not conformant

Clause 4.2 is the readiness gap and a failing MUST: Psalm ships no harness that runs one plugin issue over one fixture. The ecosystem's answer is the third-party Codeception module used by the plugin skeleton and by published plugins ([codeception-psalm-module on Packagist](https://packagist.org/packages/weirdan/codeception-psalm-module)), which is a workaround rather than a route the detector provides. Clause 4.3 is only partly met because the issue name has no separate identifier field and is tied to the issue class, so a rename of the class renames the printed type. Clauses 6.2 and 6.3 fail: the issue catalogue is a website, nothing installed resolves a printed name, and the documentation is not tracked at the installed version. Clause 7.1 is only partly met for the inline route, since `@psalm-suppress IssueName` and `@psalm-suppress all` have no documented switch and Psalm documents no check that finds them, though a plugin hooking file analysis can read the source. Clause 7.2 fails because neither the annotation nor an issue handler has a field for a reason. Clause 4.4 is not met and clause 6.4 was not verified.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                                                             |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Detector | 4.1    | Yes          | Plugins emit `PluginIssue` subclasses, [authoring plugins](https://psalm.dev/docs/running_psalm/plugins/authoring_plugins/)                                                          |
| Detector | 4.2    | Partial      | Only through a third-party Codeception module, [Packagist](https://packagist.org/packages/weirdan/codeception-psalm-module)                                                          |
| Detector | 4.3    | Partial      | Issue name is author-chosen and printed as the type; no separate identifier field, so it is tied to the class                                                                        |
| Detector | 4.4    | No           | Nothing enforces an identifier on a plugin issue                                                                                                                                     |
| Detector | 5.1    | Yes          | `vendor/bin/psalm` runs locally, [command line usage](https://psalm.dev/docs/running_psalm/command_line_usage/)                                                                      |
| Detector | 5.2    | Yes          | File arguments accepted, [command line usage](https://psalm.dev/docs/running_psalm/command_line_usage/)                                                                              |
| Detector | 5.3    | Yes          | Findings print to the terminal; `--report` adds a file                                                                                                                               |
| Detector | 5.4    | Yes          | No CI-only mode                                                                                                                                                                      |
| Detector | 6.1    | Yes          | Built-in issues documented online keyed on the printed name; a plugin issue owes only the unaltered name                                                                             |
| Detector | 6.2    | No           | Documentation is on psalm.dev, not installed                                                                                                                                         |
| Detector | 6.3    | No           | Same                                                                                                                                                                                 |
| Detector | 6.4    | Not verified | No release gate over issue documentation was found                                                                                                                                   |
| Detector | 7.1    | Partial      | Baseline is opt-in by configuration; `@psalm-suppress` has no switch or documented check, [dealing with code issues](https://psalm.dev/docs/running_psalm/dealing_with_code_issues/) |
| Detector | 7.2    | No           | No reason field anywhere, [dealing with code issues](https://psalm.dev/docs/running_psalm/dealing_with_code_issues/)                                                                 |

## Notes for a practitioner

Write the defence as a plugin issue with a name you will never change, prove it with the Codeception Psalm module and a fixture, and sweep with a single-file run. Forbid `@psalm-suppress` in your own coding standard and keep every exception in `<issueHandlers>` with a comment beside it, because Psalm will not ask for one.
