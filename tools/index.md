---
title: Tools and Defence Before Fix
permalink: /tools/
---

# Tools and Defence Before Fix (DBF)

A register of QA tools graded against DBF. Each tool has a page saying how it is and is
not conformant, clause by clause against [the detector specification](../DETECTOR-SPEC.md) and,
for a toolchain, [the toolchain specification](../TOOLING-SPEC.md).

**Readiness** asks whether a practitioner can follow the six clauses of
[the method specification](../SPEC.md) with this tool alone: bespoke rules written by the project,
a single rule runnable against a single file, and a stable identifier printed with every finding.
**Detector conformance** is graded on evidence against the detector specification, declared or
not: every MUST in its sections 4 to 7. **Toolchain conformance** applies to a toolchain as the
artefact it ships to consumers, against the toolchain specification. **Project conformance**
applies to a toolchain's own repository as a project following the method with its own assembled
tooling. Partial conformance is never called conformance; a tool that meets most of a document is
in a normal and respectable condition, and the page says exactly what is missing.

| Grade | Readiness                                                       | Detector, toolchain and project conformance                          |
| ----- | --------------------------------------------------------------- | -------------------------------------------------------------------- |
| 🟢    | All three of bespoke rules, single-rule run, printed identifier | Every MUST holds, on evidence; a declaration with an empty gap record confirms it |
| 🟡    | Possible with a workaround, a plugin ecosystem, or two of three | Most MUSTs hold; the failing clauses are named                        |
| 🔴    | No bespoke rules, or no stable identifier on findings           | A structural MUST fails, such as no bespoke rules or no local run    |

A grade marked (0.1.0) was given against the toolchain specification before the detector
specification was split from it and has not yet been regraded; its page still cites the old
clause numbers.

Toolchains are listed first in each group; a toolchain's page also lists the tools it bundles
and which of them can host a bespoke defence. Each page was written against the tool's official
documentation on the date shown, and a grade is only as current as that date. To have a tool
added or a grade corrected, open an issue or a pull request on
[the repository](https://github.com/Defence-Before-Fix/defence-before-fix.github.io).

## The register

<!-- REGISTER:START -->
### PHP

| Tool | Kind | Readiness | Detector | Toolchain | Project | Notes | Checked |
| ---- | ---- | --------- | -------- | --------- | ------- | ----- | ------- |
| [php-qa-ci](php-qa-ci.md) | toolchain | 🟢 | 🟢 (0.1.0) | not yet graded | not yet graded | Harness, resolver, derived listing and justified record all verified by running them; declares toolchain 0.1.0 with an empty gap record; section 9 partial. | 2026-09-08, branch php8.4 at commit 8a45ed0 |
| [Deptrac](deptrac.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | Custom collectors and violation subscribers with project-named layers; fails 5.2 on single files, 8.3 on the baseline formatter, 8.2 on reasons. | 2026-09-08, version 4.7.1 |
| [Infection](infection.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | A mutation tester, not a detector; custom mutators run alone; fails 4.3 on class names, 8.3 on infection-ignore-all, 8.2 on reasons. | 2026-09-08, version 0.35.4 |
| [PHP-CS-Fixer](php-cs-fixer.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | A formatter; custom fixers carry stable Vendor names printed only with verbose; fails 8.2 on unjustified exclusions and 7.1 on listing. | 2026-09-08, version 3.95.24 |
| [PHP_CodeSniffer](php-codesniffer.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | Custom sniffs and single-sniff runs; the code is derived from path and printed only with -s; fails 8.3 on phpcs ignore, 8.2, 6.1. | 2026-09-08, version 4.0.4 |
| [PHPArkitect](phparkitect.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | Custom expressions and runOnlyThis, but no identifier beyond the because text; fails 4.3, 5.2 on single files, 8.3 and 8.2 on the baseline. | 2026-09-08, version 1.3.0 |
| [PHPMD](phpmd.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | Custom rules with stable names the text renderer does not print; fails 8.3 on SuppressWarnings and the baseline, 8.2 on reasons. | 2026-09-08, version 2.15.0 |
| [PHPStan](phpstan.md) | tool | 🟢 | 🔴 (0.1.0) | · | · | First-class bespoke rules, single-rule harness and identifiers; fails 8.3 on inline ignores and the baseline, 8.2 on unjustified ignoreErrors, 7.1 on listing. | 2026-09-08, version 2.2.13 |
| [Psalm](psalm.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | Plugin issues are first class but the harness is third party; fails 8.3 on psalm-suppress and the baseline, 8.2 and 6.2. | 2026-09-08, version 6.16.1 |
| [Rector](rector.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | Custom rules with fixtures and --only; passes 8.3 since noRector was removed; fails 4.3 on class-name identifiers, 8.2, 6.1. | 2026-09-08, version 2.6.6 |

### JavaScript and TypeScript

| Tool | Kind | Readiness | Detector | Toolchain | Project | Notes | Checked |
| ---- | ---- | --------- | -------- | --------- | ------- | ----- | ------- |
| [ts-qa-ci](ts-qa-ci.md) | toolchain | 🟢 | 🟢 (0.1.0) | not yet graded | not yet graded | Every MUST verified by running rule, rule-doc and rules; declares method 1.0.0 and toolchain 0.1.0 with an empty gap record; 4.4 and 9.2 open | 2026-09-08, version 0.1.0 at commit 4203dc8 |
| [Biome](biome.md) | tool | 🔴 | 🔴 (0.1.0) | · | · | GritQL plugin diagnostics carry no identifier of their own, failing 4.3; fails 8.3 on biome-ignore; biome explain meets 6.1 and 6.2 for built-ins only | 2026-09-08, version 2.5.12 |
| [dependency-cruiser](dependency-cruiser.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | Named rules with comments give 4.1 and 4.3; 4.2 needs a one-rule config workaround; fails 8.3 on the justification-free known-violations baseline | 2026-09-08, version 18.2.0 |
| [ESLint](eslint.md) | tool | 🟢 | 🔴 (0.1.0) | · | · | Bespoke rules, single-rule run and identifiers all first class; fails 8.3 on inline disables and the bulk suppressions file, 6.2 and 11.1 absent | 2026-09-08, version 10.10.0 |
| [oxlint](oxlint.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | JS plugins are documented as alpha, so 4.1 is partial; fails 8.3 on oxlint-disable directives, 6.1 and 6.2 absent for bespoke rules | 2026-09-08, version 1.82.0 |
| [Prettier](prettier.md) | tool | 🔴 | 🔴 (0.1.0) | · | · | Formatter; fails 4.1 and 4.3 because plugins cannot report diagnostics; fails 8.3 on prettier-ignore | 2026-09-08, version 3.9.6 |
| [Stryker](stryker.md) | tool | 🔴 | 🔴 (0.1.0) | · | · | Mutation tester, not a detector; fails 4.1 since no plugin kind adds a rule; fails 8.3 on disable comments with an optional reason | 2026-09-08, version 10.0.0 |
| [The TypeScript compiler (tsc)](tsc.md) | tool | 🔴 | 🔴 (0.1.0) | · | · | No custom diagnostics, failing 4.1; a file argument discards tsconfig so 5.2 is partial; fails 8.3 because @ts- directives cannot be disabled | 2026-09-08, version 7.0.2 |
| [typescript-eslint](typescript-eslint.md) | tool | 🟢 | 🔴 (0.1.0) | · | · | RuleCreator and RuleTester give 4.1, 4.2 and 4.3; fails 8.3 because eslint-disable is undefended, 6.2 and 11.1 absent | 2026-09-08, version 8.70.0 |

### Python

| Tool | Kind | Readiness | Detector | Toolchain | Project | Notes | Checked |
| ---- | ---- | --------- | -------- | --------- | ------- | ----- | ------- |
| [Bandit](bandit.md) | tool | 🟢 | 🔴 (0.1.0) | · | · | Plugin entry point, test id decorator and -t selection pass 4.1 to 4.3; no resolver for 6.1; fails 8.3 on nosec and baseline | 2026-09-08, version 1.9.4 |
| [Flake8](flake8.md) | tool | 🟢 | 🔴 (0.1.0) | · | · | Entry point plugins with author-chosen prefix pass 4.1 and 4.3; no resolver for 6.1; fails 8.3 on noqa | 2026-09-08, version 7.3.0 |
| [mypy](mypy.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | Type checker; plugin hooks give partial 4.1 and no harness for 4.2; docs website only for 6.2; fails 8.3 on type ignore | 2026-09-08, version 2.3.1 |
| [Pylint](pylint.md) | tool | 🟢 | 🔴 (0.1.0) | · | · | Custom checkers, test harness and author-chosen ids; help-msg and list-msgs resolve and list; fails 8.3 on inline disable comments | 2026-09-08, version 4.0.8 |
| [Pyright](pyright.md) | tool | 🔴 | 🔴 (0.1.0) | · | · | Type checker with no plug-in mechanism so 4.1 fails; some diagnostics carry no rule; fails 8.3 on pyright ignore comments | 2026-09-08, version 1.1.411 |
| [Ruff](ruff.md) | tool | 🔴 | 🔴 (0.1.0) | · | · | No third-party rules so 4.1 fails; ruff rule resolves offline for 6.1 and 6.2; fails 8.3 on noqa and add-noqa | 2026-09-08, version 0.16.6 |

### Go

| Tool | Kind | Readiness | Detector | Toolchain | Project | Notes | Checked |
| ---- | ---- | --------- | -------- | --------- | ------- | ----- | ------- |
| [go vet](go-vet.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | vettool and analysistest pass 4.1 and 4.2; id in plain output not verified; no project record so 8.1, 8.2 and 8.4 fail | 2026-09-08, version Go 1.27.1 |
| [golangci-lint](golangci-lint.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | Bespoke analyzers only via custom binary build; analysistest harness passes 4.2; fails 8.3 on nolint and new-from-rev | 2026-09-08, version v2.13.2 |
| [Staticcheck](staticcheck.md) | tool | 🔴 | 🔴 (0.1.0) | · | · | Fixed catalogue so 4.1 fails; -explain resolves offline for 6.1 and 6.2; fails 8.3 on lint ignore comments | 2026-09-08, version 2026.2 (v0.8.0) |

### Rust

| Tool | Kind | Readiness | Detector | Toolchain | Project | Notes | Checked |
| ---- | ---- | --------- | -------- | --------- | ------- | ----- | ------- |
| [cargo-deny](cargo-deny.md) | tool | 🔴 | 🔴 (0.1.0) | · | · | Dependency auditor with fixed checks so 4.1 fails; deny.toml is read for 8.1; reason optional so 8.2 fails | 2026-09-08, version 0.20.2 |
| [Clippy](clippy.md) | tool | 🔴 | 🔴 (0.1.0) | · | · | Lints only by upstream contribution so 4.1 fails; explain command not verified for 6.2; fails 8.3 on allow attributes | 2026-09-08, version Rust 1.98.1 |

### Multi-language

| Tool | Kind | Readiness | Detector | Toolchain | Project | Notes | Checked |
| ---- | ---- | --------- | -------- | --------- | ------- | ----- | ------- |
| [ast-grep](ast-grep.md) | tool | 🟢 | 🔴 (0.1.0) | · | · | Bespoke YAML rules with a test harness and printed ids meet 4.1 to 5.4; no listing for 7.1 and inline ast-grep-ignore fails 8.3 | 2026-09-08, version 0.45.3 |
| [Checkov](checkov.md) | tool | 🟢 | 🔴 (0.1.0) | · | · | Custom Python and YAML policies with printed ids meet 4.1, 4.3 and section 5; online-only Guide links fail 6.2; inline skips and baselines fail 8.3 | 2026-09-08, version 3.3.16 |
| [CodeQL](codeql.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | Custom packs and a test harness meet section 4; database build and licence weaken 5.1; no id lookup for 6.1; inline suppression fails 8.3 | 2026-09-08, version CLI 2.26.4 |
| [pre-commit](pre-commit.md) | tool | 🟢 | 🔴 (0.1.0) | · | · | Local hooks with a printed id meet 4.1, 4.3 and section 5; no id resolution for 6.1; no listing for 7.1; SKIP fails 8.3 | 2026-09-08, version 4.6.2 |
| [Semgrep](semgrep.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | Local YAML rules with a test harness meet 4.1 and 4.2; printed ids carry a path-derived prefix so 4.3 is partial; nosemgrep fails 8.3 | 2026-09-08, version 1.176.0 |
| [SonarQube](sonarqube.md) | tool | 🟡 | 🔴 (0.1.0) | · | · | Custom plugin rules meet 4.1; the scanner needs a server and prints no findings so 5.1, 5.3 and 5.4 fail; NOSONAR fails 8.3 | 2026-09-08, version Server 2026.4 |
<!-- REGISTER:END -->
