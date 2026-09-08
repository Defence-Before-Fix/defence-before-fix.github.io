---
title: Psalm and Defence Before Fix
summary: Plugin issues are first class but the harness is third party; fails 8.3 on psalm-suppress and the baseline, 8.2 and 6.2.
---

# Psalm

**Language**: PHP · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 6.16.1

Psalm is a static analyser for PHP with a strong type system and a plugin API. In a pipeline it plays the same role as PHPStan, and many projects run both; for this method it is a detector that can host a bespoke rule through a plugin.

## How it is conformant

Clause 4.1 is met: a plugin hooks into analysis events and can emit an issue of its own by extending `Psalm\Issue\PluginIssue` ([authoring plugins](https://psalm.dev/docs/running_psalm/plugins/authoring_plugins/)). Clause 4.3 is met in part, because a plugin issue carries a name the author chooses, that name is what `@psalm-suppress` and `<PluginIssue name="...">` key on, and it is printed as the issue type. Clauses 5.1 and 5.2 hold: `vendor/bin/psalm file1.php` runs locally on a named file ([command line usage](https://psalm.dev/docs/running_psalm/command_line_usage/)). The `<issueHandlers>` block in the configuration is a record Psalm reads itself, which is the shape clause 8.1 asks for ([dealing with code issues](https://psalm.dev/docs/running_psalm/dealing_with_code_issues/)).

## How it is not conformant

Clause 4.2 is the readiness gap: Psalm ships no harness that runs one plugin issue over one fixture. The ecosystem's answer is the third-party Codeception module used by the plugin skeleton and by published plugins ([codeception-psalm-module on Packagist](https://packagist.org/packages/weirdan/codeception-psalm-module)), which is a workaround rather than a first class route. Clause 8.3 fails structurally: `@psalm-suppress IssueName` and `@psalm-suppress all` are documented inline suppressions, and `--set-baseline` grandfathers existing errors ([dealing with code issues](https://psalm.dev/docs/running_psalm/dealing_with_code_issues/)). Clause 8.2 fails because neither the annotation nor an issue handler has a field for a reason. Clause 6.1 fails for a bespoke issue, since the built-in issue catalogue is keyed on issue names but is a website, so clause 6.2 fails for bundled issues too. Clause 7.1 fails because no command enumerates active issue types or plugins with what they forbid; `psalm-plugin show` lists installed plugins by package name only ([using plugins](https://psalm.dev/docs/running_psalm/plugins/using_plugins/)). There is no declaration under clause 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                                                           |
| ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes          | Plugins emit `PluginIssue` subclasses, [authoring plugins](https://psalm.dev/docs/running_psalm/plugins/authoring_plugins/)        |
| 4.2    | Partial      | Only through a third-party Codeception module, [Packagist](https://packagist.org/packages/weirdan/codeception-psalm-module)        |
| 4.3    | Partial      | Issue name is author-chosen and printed as the type; no separate identifier field                                                  |
| 4.4    | No           | Nothing enforces an identifier on a plugin issue                                                                                   |
| 5.1    | Yes          | `vendor/bin/psalm` runs locally, [command line usage](https://psalm.dev/docs/running_psalm/command_line_usage/)                    |
| 5.2    | Yes          | File arguments accepted, [command line usage](https://psalm.dev/docs/running_psalm/command_line_usage/)                            |
| 5.3    | Yes          | Findings print to the terminal; `--report` adds a file                                                                             |
| 5.4    | Yes          | No CI-only mode                                                                                                                    |
| 6.1    | Partial      | Built-in issues documented by name online; nothing resolves a plugin issue                                                         |
| 6.2    | No           | Documentation is on psalm.dev, not installed                                                                                       |
| 6.3    | No           | Same                                                                                                                               |
| 7.1    | No           | `psalm-plugin show` lists packages, not issues, [using plugins](https://psalm.dev/docs/running_psalm/plugins/using_plugins/)       |
| 7.2    | No           | Follows from 7.1                                                                                                                   |
| 7.3    | No           | Follows from 7.1                                                                                                                   |
| 8.1    | Partial      | `<issueHandlers>` is read by Psalm but competes with inline suppression and the baseline                                           |
| 8.2    | No           | No reason field anywhere, [dealing with code issues](https://psalm.dev/docs/running_psalm/dealing_with_code_issues/)               |
| 8.3    | No           | `@psalm-suppress` and `--set-baseline`, [dealing with code issues](https://psalm.dev/docs/running_psalm/dealing_with_code_issues/) |
| 8.4    | No           | Follows from 7.1                                                                                                                   |
| 8.5    | Partial      | Error levels are documented defaults only                                                                                          |
| 9.1    | No           | No agent summary                                                                                                                   |
| 9.2    | No           | No delivery mechanism                                                                                                              |
| 10.1   | Not verified | No release gate over issue documentation was found                                                                                 |
| 10.2   | Not verified | Psalm analyses itself; whether plugin hooks are exercised was not checked                                                          |
| 11.1   | No           | No declaration                                                                                                                     |

## Notes for a practitioner

Write the defence as a plugin issue with a name you will never change, prove it with the Codeception Psalm module and a fixture, and sweep with a single-file run. Forbid `@psalm-suppress` in your own coding standard and keep every exception in `<issueHandlers>` with a comment beside it, because Psalm will not ask for one.
