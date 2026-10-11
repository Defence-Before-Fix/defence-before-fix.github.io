---
title: Reek and Defence Before Fix
summary: No way to load a project's own smell detector fails 4.1, and smell types taken from the class name fail 4.3, both structural; --smell meets 4.2; an installed file keyed on every smell type meets 6.1 to 6.3 offline; the :reek: comments cannot be switched off or seen, so 7.1 fails
language: Ruby
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-10-10, version 6.6.0
---

# Reek

{% include tool-grades.html %}

Reek is a code smell detector for Ruby: 29 detectors, such as `UtilityFunction`, `FeatureEnvy` and `TooManyStatements`, that walk the parser's syntax tree and report design smells in modules and methods rather than style. In a pipeline it runs beside RuboCop as a second, design-level check, usually through its command or its Rake task, with a `.reek.yml` tuning or excluding detectors per context.

## How it is conformant

`reek --smell UtilityFunction r.rb` runs one detector against one file and printed only its finding, `[3]:UtilityFunction: Foo#bar doesn't depend on instance state`, exit 2 ([command-line options](https://github.com/troessner/reek/blob/v6.6.0/docs/Command-Line-Options.md), ran), and the gem's RSpec matcher `reek_of` tests code for one smell type ([RSpec matchers](https://github.com/troessner/reek/blob/v6.6.0/docs/RSpec-matchers.md)) (4.2, graded on the bundled detectors). Reek runs locally on a single file, or on standard input, with no service and no licence tier, and prints every finding in the command's own output; it has no option that writes the report elsewhere (5.1 to 5.4, ran).

The installed gem carries [`lib/reek/code_climate/code_climate_configuration.yml`](https://github.com/troessner/reek/blob/v6.6.0/lib/reek/code_climate/code_climate_configuration.yml), an index whose entries are labelled with each smell type exactly as printed and hold its explanation, with an example, as `content`; Reek's Code Climate report presents that text for each finding ([`code_climate_formatter.rb`](https://github.com/troessner/reek/blob/v6.6.0/lib/reek/code_climate/code_climate_formatter.rb)). It is a file Reek installs, keyed on the identifier exactly (readings 10 and 11), so a reader holding `UtilityFunction` finds its documentation under that label. A script run with the network removed (`unshare -rn`) loaded the detector registry and the file: all 29 smell types had an entry, none of them shorter than 97 characters, and the file had no entry for anything else (6.1, 6.2 and 6.3). The repository's [specification for that file](https://github.com/troessner/reek/blob/v6.6.0/spec/reek/code_climate/code_climate_configuration_spec.rb) fails when a detector lacks `content` or an entry has no detector, which is an automated check over every bundled name (6.4, partial: it is a test, and the release task from `bundler/gem_tasks` does not run it, [Rakefile](https://github.com/troessner/reek/blob/v6.6.0/Rakefile)).

## How it is not conformant

Clause 4.1 fails. Reek offers no way to load a project's own detector: `reek --help` has no load or require option, and the [guide to writing detectors](https://github.com/troessner/reek/blob/v6.6.0/docs/How-To-Write-New-Detectors.md) is for contributors, placing every detector in `lib/reek/smell_detectors` and asking for the idea to be discussed in an issue first. Detectors register by subclassing the internal `BaseDetector`, whose subclasses the [detector repository](https://github.com/troessner/reek/blob/v6.6.0/lib/reek/detector_repository.rb) collects. A subclass preloaded into the interpreter with `RUBYOPT=-r<file>` did run and print its finding (ran), but that is Ruby loading a file before Reek starts, against a class Reek does not document for this use, not a mechanism Reek supports.

Clause 4.3 fails. A detector's smell type, the identifier printed with each finding, is `name.split('::').last`, the detector's class name ([`base_detector.rb`](https://github.com/troessner/reek/blob/v6.6.0/lib/reek/smell_detectors/base_detector.rb)), which is the derivation 4.3 rules out (reading 5), and with no project detectors there is no rule that carries any other. The smell type is printed unaltered in every format: text, single-line text, YAML and JSON (as `smell_type`), XML (as `source`), HTML and GitHub annotations (ran). There is no rule over the rules (4.4).

The default output prints a documentation link beside each finding, such as `https://github.com/troessner/reek/blob/v6.6.0/docs/Utility-Function.md`, which is the smell type re-spelt with hyphens on the project's website ([`documentation_link.rb`](https://github.com/troessner/reek/blob/v6.6.0/lib/reek/documentation_link.rb)); it is keyed on a transformed address and needs the network, so it resolves nothing under reading 11, and the `docs/` pages it names are left out of the gem ([`reek.gemspec`](https://github.com/troessner/reek/blob/v6.6.0/reek.gemspec)). The installed file above is the route that resolves.

Clause 7.1 fails. A comment above a module or method containing `:reek:` and a smell type, such as `# :reek:UtilityFunction`, disables that detector for it ([smell suppression](https://github.com/troessner/reek/blob/v6.6.0/docs/Smell-Suppression.md)); the comment is parsed by [`code_comment.rb`](https://github.com/troessner/reek/blob/v6.6.0/lib/reek/code_comment.rb) on every run, no option refuses it, no detector reports it, and a project cannot write a detector that would. A file carrying it printed nothing and exited 0 (ran). The baseline is no better seen: `reek --todo` writes `.reek.yml` with an `exclude` entry for each smelly context, Reek loads that file from the working directory on every run, and the run then printed nothing and exited 0; `--show-configuration-path` names the file but not what it excludes (ran). No reason is asked for on a comment (7.2).

A file Reek cannot parse exits 0. `reek broken.rb` printed a banner saying the source "cannot be processed by Reek due to a syntax error" with a backtrace, and exited 0 (ran). Under reading 9 this is not graded under 5.3, but a defence routed through Reek stops defending that file without failing the run. `reek --smell NoSuchSmell r.rb` also exited 0 with no output (ran), so a misspelt smell type in a red proof looks like a pass.

Readiness is 🔴 because no bespoke rule can be written. The detector grade is 🔴 because 4.1 and 4.3 fail, both structural under reading 1; 7.1 fails too. Reek declares no version of this document.

## Clause by clause

| Document | Clause | Result  | Evidence                                                                                                                                                                                                                                |
| -------- | ------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | No      | No load option; detectors live in `lib/reek/smell_detectors` ([writing detectors](https://github.com/troessner/reek/blob/v6.6.0/docs/How-To-Write-New-Detectors.md)); a `RUBYOPT` preload is not Reek's mechanism                       |
| Detector | 4.2    | Yes     | `--smell <type> <file>` ran one detector ([options](https://github.com/troessner/reek/blob/v6.6.0/docs/Command-Line-Options.md); ran); `reek_of` matcher                                                                                |
| Detector | 4.3    | No      | Smell type is the class name ([`base_detector.rb`](https://github.com/troessner/reek/blob/v6.6.0/lib/reek/smell_detectors/base_detector.rb)); printed unaltered in all seven formats (ran)                                              |
| Detector | 4.4    | No      | No rule over the rules                                                                                                                                                                                                                  |
| Detector | 5.1    | Yes     | `reek <file>` locally (ran)                                                                                                                                                                                                             |
| Detector | 5.2    | Yes     | Single file and standard input (ran)                                                                                                                                                                                                    |
| Detector | 5.3    | Yes     | Every finding on standard output; no report-file option (ran)                                                                                                                                                                           |
| Detector | 5.4    | Yes     | Every detector runs from the installed gem                                                                                                                                                                                              |
| Detector | 6.1    | Yes     | Installed [`code_climate_configuration.yml`](https://github.com/troessner/reek/blob/v6.6.0/lib/reek/code_climate/code_climate_configuration.yml) keyed on each printed smell type (readings 10, 11); printed URL is re-spelt and online |
| Detector | 6.2    | Yes     | All 29 entries read with the network removed (ran)                                                                                                                                                                                      |
| Detector | 6.3    | Yes     | 29 of 29 smell types have shipped `content` (ran)                                                                                                                                                                                       |
| Detector | 6.4    | Partial | [Specification](https://github.com/troessner/reek/blob/v6.6.0/spec/reek/code_climate/code_climate_configuration_spec.rb) checks every detector has an entry; not a release step                                                         |
| Detector | 7.1    | No      | `:reek:` comments cannot be switched off and are not reported ([`code_comment.rb`](https://github.com/troessner/reek/blob/v6.6.0/lib/reek/code_comment.rb); ran); the `--todo` file is applied silently (ran)                           |
| Detector | 7.2    | No      | No reason asked for on a `:reek:` comment ([smell suppression](https://github.com/troessner/reek/blob/v6.6.0/docs/Smell-Suppression.md))                                                                                                |

## Notes for a practitioner

Reek is worth running for its design smells, but it cannot hold a project's own defence: put that in RuboCop as a cop, and use Reek alongside it. Treat a smell type as fixed to its class, since a rename upstream renames it. Look a smell type up in the installed `lib/reek/code_climate/code_climate_configuration.yml` rather than following the printed link, which needs the network and a re-spelt name. Search the code for `:reek:` outside Reek, in the build, if the project forbids suppressions, and keep the `.reek.yml` written by `--todo` under review, since Reek reports neither. Check the parse separately, with `ruby -c` or RuboCop's `Lint/Syntax`, because a file Reek cannot parse exits 0, and check the spelling of the smell type given to `--smell`, because a wrong one exits 0 too.

## Attributes

| Attribute      | Value                                                                                                     | Source                                                                                                        |
| -------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Kind           | Detector (code smells)                                                                                    | [README](https://github.com/troessner/reek/blob/v6.6.0/README.md)                                             |
| Depth          | Syntactic (the parser's tree, with module and method contexts)                                            | [`base_detector.rb`](https://github.com/troessner/reek/blob/v6.6.0/lib/reek/smell_detectors/base_detector.rb) |
| Rule form      | None for a project; bundled detectors are Ruby subclasses of an internal class                            | [writing detectors](https://github.com/troessner/reek/blob/v6.6.0/docs/How-To-Write-New-Detectors.md)         |
| Output formats | text (and single-line), yaml, json, xml, html, github; no SARIF                                           | `reek --help`, ran                                                                                            |
| Exit codes     | 2 on a finding (`--failure-exit-code`), 0 when clean; 1 on an unknown option; 0 on a file it cannot parse | ran                                                                                                           |
| Report file    | None                                                                                                      | `reek --help`, ran                                                                                            |
| Fix mode       | None                                                                                                      | `reek --help`, ran                                                                                            |
| Baseline       | `--todo` writes `.reek.yml` with an exclusion per smelly context, applied without report                  | ran                                                                                                           |
| Rule listing   | `reek -l` lists the 29 smell types, names only                                                            | ran                                                                                                           |
| Licence        | MIT                                                                                                       | [`reek.gemspec`](https://github.com/troessner/reek/blob/v6.6.0/reek.gemspec)                                  |
