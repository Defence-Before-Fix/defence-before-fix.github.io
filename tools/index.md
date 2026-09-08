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

| Grade | Readiness                                                       | Detector, toolchain and project conformance                                       |
| ----- | --------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 🟢    | All three of bespoke rules, single-rule run, printed identifier | Every MUST holds, on evidence; a declaration with an empty gap record confirms it |
| 🟡    | Possible with a workaround, a plugin ecosystem, or two of three | Most MUSTs hold; the failing clauses are named                                    |
| 🔴    | No bespoke rules, or no stable identifier on findings           | A structural MUST fails, such as no bespoke rules or no local run                 |

Every grade is against the detector specification 1.0.0 and, for a toolchain, the toolchain
specification 0.2.0; each page's clause table names the clauses that decided it.

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
| [php-qa-ci](php-qa-ci.md) | toolchain | 🟢 | 🟡 | 🟡 | 🟡 | Harness, resolver, derived listing and justified record verified by running them; fails toolchain 4.1 through its PHPArkitect tier and identifier-less lanes, 4.2 on fifteen rules without a page, 4.3 on two baseline routes; declares 0.2.0 with eight recorded gaps. | 2026-09-08, branch php8.4 at commit e25aba4, declaration merged at 4d9b2ba |
| [Deptrac](deptrac.md) | tool | 🟡 | 🔴 | · | · | Custom collectors and violation subscribers meet 4.1; no single-file run fails 5.2, layer names only partly meet 4.3, nothing resolves them for section 6. | 2026-09-08, version 4.7.1 |
| [Infection](infection.md) | tool | 🟡 | 🔴 | · | · | A mutation tester, not a detector; custom mutators only partly meet 4.1, the class name printed fails 4.3, infection-ignore-all fails 7.1. | 2026-09-08, version 0.35.4 |
| [PHP-CS-Fixer](php-cs-fixer.md) | tool | 🟡 | 🟡 | · | · | A formatter whose Vendor rule names and describe command meet 4.1, 4.2 and section 6; the name prints only with verbose, failing 4.3. | 2026-09-08, version 3.95.24 |
| [PHP_CodeSniffer](php-codesniffer.md) | tool | 🟡 | 🟡 | · | · | Custom sniffs and single-sniff runs meet 4.1, 4.2 and section 5; the code is path-derived under 4.3 and nothing resolves it, failing 6.1 to 6.3. | 2026-09-08, version 4.0.4 |
| [PHPArkitect](phparkitect.md) | tool | 🟡 | 🔴 | · | · | Custom expressions and runOnlyThis meet 4.1 and 4.2; no identifier beyond the because text fails 4.3, directory-only class sets fail 5.2. | 2026-09-08, version 1.3.0 |
| [PHPMD](phpmd.md) | tool | 🟡 | 🟡 | · | · | Custom rules and one-rule rulesets meet 4.1 and 4.2; the name is absent from default output under 4.3, documentation online only fails 6.2 and 6.3. | 2026-09-08, version 2.15.0 |
| [PHPStan](phpstan.md) | tool | 🟢 | 🟡 | · | · | Bespoke rules, RuleTestCase harness, printed identifiers and a detectable ignore route meet 4.1 to 5.4 and 7.1; bundled documentation online only fails 6.2 and 6.3. | 2026-09-08, version 2.2.13 |
| [Psalm](psalm.md) | tool | 🟡 | 🟡 | · | · | Plugin issues meet 4.1 and section 5; the harness under 4.2 is third party, bundled documentation online only fails 6.2 and 6.3, psalm-suppress weakens 7.1. | 2026-09-08, version 6.16.1 |
| [Rector](rector.md) | tool | 🟡 | 🔴 | · | · | Custom rules with fixtures and only meet 4.1 and 4.2, skips are configuration only under 7.1; the class name printed as identifier fails 4.3. | 2026-09-08, version 2.6.6 |

### JavaScript and TypeScript

| Tool | Kind | Readiness | Detector | Toolchain | Project | Notes | Checked |
| ---- | ---- | --------- | -------- | --------- | ------- | ----- | ------- |
| [ts-qa-ci](ts-qa-ci.md) | toolchain | 🟢 | 🟡 | 🟡 | 🟡 | Harness, resolver, derived listing and justified record all hold for the ESLint lane; the dependency-cruiser defence is outside all three, an eslint-suppressions.json silences a bundled defence, and a Tier A rule is never enabled; declares toolchain 0.2.0 at both levels with the gaps recorded | 2026-09-08, main at commit 46fac6a, declaration merged at ea2020b |
| [Biome](biome.md) | tool | 🔴 | 🔴 | · | · | GritQL plugin diagnostics carry no identifier, failing 4.3; biome-ignore cannot be switched off, failing 7.1; biome explain meets 6.1 to 6.3 for built-ins | 2026-09-08, version 2.5.12 |
| [dependency-cruiser](dependency-cruiser.md) | tool | 🟡 | 🟡 | · | · | Named rules with comments meet 4.1, 4.3 and section 6; the baseline is opt-in so 7.1 holds; 4.2 needs a one-rule config workaround | 2026-09-08, version 18.2.0 |
| [ESLint](eslint.md) | tool | 🟢 | 🟡 | · | · | Bespoke rules, harness and printed identifiers meet 4.1 to 4.3; noInlineConfig meets 7.1; core rule documentation is online only, failing 6.2 and 6.3 | 2026-09-08, version 10.10.0 |
| [oxlint](oxlint.md) | tool | 🟡 | 🟡 | · | · | JS plugins are alpha so 4.1 is partial; built-in documentation is online only, failing 6.2 and 6.3; oxlint-disable cannot be switched off, failing 7.1 | 2026-09-08, version 1.82.0 |
| [Prettier](prettier.md) | tool | 🔴 | 🔴 | · | · | Formatter; plugins cannot report diagnostics so 4.1 and 4.3 fail; prettier-ignore cannot be switched off, failing 7.1 | 2026-09-08, version 3.9.6 |
| [Stryker](stryker.md) | tool | 🔴 | 🔴 | · | · | Mutation tester, not a detector; no plugin kind adds a rule, failing 4.1; Stryker disable comments cannot be switched off, failing 7.1 | 2026-09-08, version 10.0.0 |
| [The TypeScript compiler (tsc)](tsc.md) | tool | 🔴 | 🔴 | · | · | No custom diagnostics, failing 4.1; a file argument discards tsconfig so 5.2 is partial; @ts- directives cannot be disabled, failing 7.1 | 2026-09-08, version 7.0.2 |
| [typescript-eslint](typescript-eslint.md) | tool | 🟢 | 🟡 | · | · | RuleCreator and RuleTester meet 4.1 to 4.3, ESLint supplies section 5 and 7.1; bundled rule pages are online only, failing 6.2 and 6.3 | 2026-09-08, version 8.70.0 |

### Python

| Tool | Kind | Readiness | Detector | Toolchain | Project | Notes | Checked |
| ---- | ---- | --------- | -------- | --------- | ------- | ----- | ------- |
| [Bandit](bandit.md) | tool | 🟢 | 🟡 | · | · | Plugin entry point, test id decorator and -t selection meet 4.1 to 4.3; ignore-nosec meets 7.1; no resolver so 6.1 and 6.2 fail | 2026-09-08, version 1.9.4 |
| [Flake8](flake8.md) | tool | 🟢 | 🟡 | · | · | Entry point plugins with author-chosen prefix meet 4.1 to 4.3; disable-noqa meets 7.1; no resolver so 6.1 and 6.2 fail | 2026-09-08, version 7.3.0 |
| [mypy](mypy.md) | tool | 🟡 | 🔴 | · | · | Type checker; plugin hooks give partial 4.1 with no harness for 4.2; website-only codes fail 6.2 and 6.3; type ignore fails 7.1 | 2026-09-08, version 2.3.1 |
| [Pylint](pylint.md) | tool | 🟢 | 🟢 | · | · | Custom checkers, CheckerTestCase and author-chosen ids meet 4.1 to 4.3; help-msg meets 6.1 to 6.3; disable comments detectable under 7.1 | 2026-09-08, version 4.0.8 |
| [Pyright](pyright.md) | tool | 🔴 | 🔴 | · | · | Type checker with no plug-in mechanism so 4.1 fails; some diagnostics carry no rule for 4.3; website-only docs fail 6.2 | 2026-09-08, version 1.1.411 |
| [Ruff](ruff.md) | tool | 🔴 | 🔴 | · | · | No third-party rules so 4.1 fails; select and rule meet 4.2 and 6.1 to 6.3 for bundled rules; specific noqa fails 7.1 | 2026-09-08, version 0.16.6 |

### Go

| Tool | Kind | Readiness | Detector | Toolchain | Project | Notes | Checked |
| ---- | ---- | --------- | -------- | --------- | ------- | ----- | ------- |
| [go vet](go-vet.md) | tool | 🟡 | 🟡 | · | · | vettool and analysistest meet 4.1 and 4.2; help resolves offline for 6.1 to 6.3; analyzer name in plain output unverified so 4.3 partial | 2026-09-08, version Go 1.27.1 |
| [golangci-lint](golangci-lint.md) | tool | 🟡 | 🟡 | · | · | Module plugins and analysistest meet 4.1 and 4.2; nolintlint meets 7.1 and 7.2; wrapped tool codes leave 4.3 and 6.1 partial | 2026-09-08, version v2.13.2 |
| [Staticcheck](staticcheck.md) | tool | 🔴 | 🔴 | · | · | Fixed catalogue so 4.1 fails; checks flag and -explain meet 4.2 and 6.1 to 6.3 for bundled checks; lint ignore fails 7.1 | 2026-09-08, version 2026.2 (v0.8.0) |

### Rust

| Tool | Kind | Readiness | Detector | Toolchain | Project | Notes | Checked |
| ---- | ---- | --------- | -------- | --------- | ------- | ----- | ------- |
| [cargo-deny](cargo-deny.md) | tool | 🔴 | 🔴 | · | · | Dependency auditor with fixed checks so 4.1 fails; per-check runs leave 4.2 and 5.2 partial; website-only codes fail 6.2 | 2026-09-08, version 0.20.2 |
| [Clippy](clippy.md) | tool | 🔴 | 🔴 | · | · | Lints only by upstream contribution so 4.1 fails; allow_attributes lints meet 7.1 and 7.2; offline resolution for 6.2 not verified | 2026-09-08, version Rust 1.98.1 |

### Multi-language

| Tool | Kind | Readiness | Detector | Toolchain | Project | Notes | Checked |
| ---- | ---- | --------- | -------- | --------- | ------- | ----- | ------- |
| [ast-grep](ast-grep.md) | tool | 🟢 | 🟢 | · | · | Bespoke YAML rules, a test harness and printed ids meet every MUST in 4 and 5; kind and regex rules make ast-grep-ignore detectable for 7.1 | 2026-09-08, version 0.45.3 |
| [Checkov](checkov.md) | tool | 🟢 | 🔴 | · | · | Custom policies with printed ids meet sections 4 and 5; online-only Guide links fail 6.2 and 6.3; inline skips fail 7.1 | 2026-09-08, version 3.3.16 |
| [CodeQL](codeql.md) | tool | 🟡 | 🟡 | · | · | Custom packs and a test harness meet 4.1 and 4.2; findings go to a file only, failing 5.3; no id lookup for 6.1 | 2026-09-08, version CLI 2.26.4 |
| [pre-commit](pre-commit.md) | tool | 🟢 | 🟢 | · | · | A host, not a detector; local hooks run one at a time with a printed id meet sections 4 and 5, and it offers no inline route for 7.1 | 2026-09-08, version 4.6.2 |
| [Semgrep](semgrep.md) | tool | 🟡 | 🟡 | · | · | Local YAML rules and a test harness meet 4.1 and 4.2; the path-derived prefix fails 4.3; registry rules resolve online only, failing 6.2 and 6.3 | 2026-09-08, version 1.176.0 |
| [SonarQube](sonarqube.md) | tool | 🟡 | 🔴 | · | · | Custom plugin rules meet 4.1; the scanner needs a server and prints no findings so 5.1, 5.3 and 5.4 fail | 2026-09-08, version Server 2026.4 |
<!-- REGISTER:END -->
