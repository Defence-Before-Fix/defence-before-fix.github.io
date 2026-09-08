---
title: php-qa-ci and Defence Before Fix
summary: Harness, resolver, derived listing and justified record verified by running them; fails toolchain 4.1 through its PHPArkitect tier and identifier-less lanes, 4.2 on fifteen rules without a page, 4.3 on two baseline routes; declares 0.2.0 with eight recorded gaps.
---

# php-qa-ci

**Language**: PHP · **Kind**: toolchain · **Readiness**: 🟢 · **Detector conformance**: 🟡 · **Toolchain conformance**: 🟡 · **Project conformance**: 🟡 · **Checked**: 2026-09-08, branch php8.4 at commit e25aba4, declaration merged at 4d9b2ba

php-qa-ci is a Composer plugin that wraps PHPStan, PHPArkitect, PHPUnit, PHP CS Fixer, Rector, Infection and a set of its own lanes behind one `bin/qa` entry point, ships a bundle of PHPStan rules with their documentation, and writes an agent-facing block into the consuming project. It is the PHP reference toolchain for this method, and this page grades it with the same scrutiny as every other entry ([repository](https://github.com/LongTermSupport/php-qa-ci)).

Every mechanism below was checked by running it in a checkout: `bin/qa`, `bin/qa -t <tool> -p <path>`, `bin/rules`, `bin/rule-doc <identifier>` and `bin/phpstan-rule <identifier> <path>`. Detector conformance is graded on the detectors the toolchain routes defences through, each together with the wrapping around it, as toolchain clause 4.1 requires. Toolchain conformance grades the artefact a consuming project installs. Project conformance grades the repository as a project following the method with the toolchain it ships.

## How it is conformant

For its own PHPStan bundle, every detector clause holds. A project's rules go under `rules:` in its `qaConfig/phpstan.neon` (detector 4.1). `bin/phpstan-rule phpqaci.nullCoalescingFalse src/ZzProbe.php` on a probe containing `?? false` printed `FIRED (1)` with the location and exited 1, and the same command for `phpqaci.nestedTernary` printed `did not fire` (4.2). PHPStan prints the `phpqaci.*` identifier under every finding, and `RequireRuleIdentifierConstantRule`, on by default, rejects a magic-string identifier (4.3, 4.4). `bin/qa -t phpstan -p <file>` runs one lane over one file locally with the result in the terminal, and the CI script runs the same `bin/qa` (5.1 to 5.4). `bin/rule-doc phpqaci.nullCoalescingFalse` resolves the identifier as printed to its rule, bundle, source and the shipped page in `docs/phpstan-rules/`, offline (6.1 to 6.3 for the bundle). Inline `@phpstan-ignore` in every form is a finding of `ForbidInlinePhpstanIgnoreRule` (7.1).

At toolchain level, `bin/rules .` lists every rule in the resolved neon chain with identifier, summary and documentation route, derived from the configuration and the lane registry rather than hand-maintained, and the package's contributor-only rules appear in its own listing (5.2, 5.3). The record is the `ignoreErrors` block PHPStan itself loads (6.1); the `pij` lane rejects an entry with no comment, a comment matching a paste-anywhere list such as `legacy` or `needed for now`, or one too short to name a hazard and a scope (6.2 in part); and the same listing enumerates the record beside the defences, including an entry from an included baseline (6.3). The entry point runs coding standards, linting and static analysis before tests and stops on a failure (4.5). The self-check configuration includes both bundled rule sets, guarded by a test, and the PHPArkitect tier runs on the package's own source (8.2). The agent block is written and refreshed on every install (7.2). The manifest declares method 1.0.0 and toolchain 0.2.0 at both levels, with the gaps below recorded against their clauses (9.2).

## How it is not conformant

Toolchain clause 4.1 fails three ways. PHPArkitect, through which the on-by-default rule tier routes bundled defences, prints a violation as prose (`should have a name that matches *Controller because controllers must be named consistently`) with no identifier, has no single-rule or single-file invocation through the lane, and has no resolver for its tier, so as wrapped it fails detector 4.3, 5.2 and 6.1 to 6.3. Five of the toolchain's own lanes, `packageType`, `phpstanIgnoreJustification`, `sensitiveParameterUsage`, `branchNamePolicy` and `phpStrictTypes`, print no identifier on failure. And PHPStan's native identifiers resolve online only: `bin/rule-doc method.notFound` answers `Unknown rule identifier`, so the wrapping does not close detector 6.2 and 6.3 for the detector's own catalogue.

Clause 4.2 is partial: fifteen of the twenty-four bundled PHPStan rules resolve to an index row and no page, so `bin/rule-doc phpqaci.nestedTernary` ends at `Summary: No nested ternary expressions` and states no correct construction. Clause 4.3 is partial: a `phparkitect-baseline.json` generated once is read silently on every later run of the lane, which printed `Baseline file found` and `No violations detected` on a fixture with one violation, and a PHPStan baseline included from `qaConfig/phpstan.neon` is listed by `bin/rules` but not checked by the justification lane, which reads the top-level file alone (also 6.2). Clause 5.1 is partial: lanes are listed without an identifier or a documentation route, even the two that print one. Clause 8.1 is partial: the release guard requires an index row rather than a page, and a lane with no identifier is outside it. Clause 7.1 is not met: the agent block carries a pointer and no rule lines, so the toolchain does not conform with agent support.

Project conformance carries the same gaps, because the repository runs the toolchain it ships. Its own record is one justified entry, enumerable in the listing; its contributor-only rules are listed and run; the fifteen rules without a page are among the ones that run on it.

## Tools it bundles

php-qa-ci is a toolchain rather than a tool, so the question for each lane it runs is whether that lane can host a bespoke defence under the method, and which of the toolchain's own mechanisms wrap it. Every lane below is registered by `bin/qa` and appears in the `bin/rules` listing; `bin/phpstan-rule` and `bin/rule-doc` wrap PHPStan and the two lanes that print an identifier.

- **PHPStan**: hosts bespoke defences; wrapped by `bin/phpstan-rule`, `bin/rule-doc` and `bin/rules`, with the bundled rules and the identifier constant enforced on top. Conforms as wrapped for the `phpqaci.*` bundle; fails 6.2 and 6.3 for its native catalogue.
- **PHPArkitect**: hosts bespoke defences about architecture through `phparkitect.php`; wrapped only as a lane, with no identifier, no single-file run and no resolver. Does not conform as wrapped, and the default tier routes bundled defences through it.
- **Rector**: a refactoring tool run in dry-run mode; a project can register a custom rule, but the toolchain runs it as a check and routes no defence through it.
- **PHP CS Fixer**: a formatter; cannot host a defence in the method's sense, and is run as a check.
- **PSR-4 validation**: a fixed check of autoload mapping; not a host.
- **Composer validation and composer require checker**: fixed checks of the manifest and of undeclared dependencies; not hosts.
- **Package type**: a bundled defence requiring an explicit `type` in `composer.json`; prints no identifier, documented in `docs/tools/`.
- **Config template ignore-list audit**: a bundled defence over the toolchain's own templates; prints `phpqaci.configTemplateIgnoreList`, resolved by `bin/rule-doc`.
- **Infection config source dirs check**: a bundled defence that `infection.json` names real directories; prints `phpqaci.infectionConfigSourceDirectoriesMustExist`, resolved by `bin/rule-doc`.
- **Strict types**: a bundled defence that every file declares strict types; prints no identifier.
- **PHP lint**: a syntax check; not a host.
- **Markdown links**: a fixed link check; not a host.
- **Branch name policy**: a bundled defence over branch naming; prints no identifier.
- **PHPStan ignoreErrors justification**: the clause 6.2 mechanism, a bundled defence over the project record; prints no identifier and reads the top-level record file alone.
- **SensitiveParameter usage**: a bundled defence requiring the attribute somewhere in `src/`; prints no identifier, documented in `docs/tools/`.
- **PHPUnit**: a test runner; cannot host a defence, since the method rules out a test as the net.
- **Infection**: a mutation tester; cannot host a defence, with its configuration guarded by the source dirs check above.

## Clause by clause

Detector rows grade PHPStan as wrapped, with PHPArkitect as wrapped noted where it differs.

| Document  | Clause | Result  | Evidence                                                                                                                                  |
| --------- | ------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Detector  | 4.1    | Yes     | Project rules under `rules:` in `qaConfig/phpstan.neon`; PHPArkitect project rules in `phparkitect.php`                                   |
| Detector  | 4.2    | Yes     | `bin/phpstan-rule <identifier> <path>` fired red on a probe and stayed silent on another rule; PHPArkitect as wrapped has none            |
| Detector  | 4.3    | Yes     | `🪪  phpqaci.nullCoalescingFalse` printed under the finding, identifier in JSON mode too; PHPArkitect prints prose only                   |
| Detector  | 4.4    | Yes     | `RequireRuleIdentifierConstantRule` in `rules-default.neon`                                                                               |
| Detector  | 5.1    | Yes     | Every command ran in the checkout with no service                                                                                         |
| Detector  | 5.2    | Yes     | `bin/qa -t phpstan -p src/ZzProbe.php` scanned that path alone; PHPArkitect's lane is non-path-supporting                                 |
| Detector  | 5.3    | Yes     | Findings in the terminal, archived log named after them                                                                                   |
| Detector  | 5.4    | Yes     | `ci.bash` runs `bin/qa`                                                                                                                   |
| Detector  | 6.1    | Yes     | `bin/rule-doc phpqaci.nullCoalescingFalse` resolved as printed; an unknown identifier exits 1                                             |
| Detector  | 6.2    | Partial | Bundle resolves offline from `docs/phpstan-rules/`; `bin/rule-doc method.notFound` is unknown, PHPStan's catalogue is online only         |
| Detector  | 6.3    | Partial | Bundle pages ship with the package; PHPStan's own rules ship none; PHPArkitect's tier has no page                                         |
| Detector  | 6.4    | Partial | `RuleDocumentationTest` fails the build on a dangling page reference or an unindexed identifier                                           |
| Detector  | 7.1    | Yes     | Inline ignores detectable by a bundled rule; PHPArkitect's baseline disableable by `--skip-baseline`                                      |
| Detector  | 7.2    | No      | `reportIgnoresWithoutComments` not configured; the toolchain's justification lane stands in                                               |
| Toolchain | 4.1    | No      | PHPArkitect as wrapped fails 4.3, 5.2 and 6.1 to 6.3; five lanes print no identifier; PHPStan's native catalogue fails 6.2 and 6.3        |
| Toolchain | 4.2    | Partial | `bin/rules .`: `doc: no documentation page` for 15 of 24 rules; `bin/rule-doc phpqaci.packageType` unknown                                |
| Toolchain | 4.3    | Partial | Inline ignore forbidden; `phparkitect-baseline.json` read silently; an included PHPStan baseline escapes the justification lane           |
| Toolchain | 4.4    | Yes     | `bin/qa -t <tool> -p <path>` for every path-supporting lane                                                                               |
| Toolchain | 4.5    | Yes     | `bin/qa` runs coding standards, linting, static analysis, then tests, failing fast or reporting every failure before the success banner   |
| Toolchain | 5.1    | Partial | Rules listed with identifier, summary and route; lanes listed with `identifier: null` and no route                                        |
| Toolchain | 5.2    | Yes     | Derived from the resolved neon chain and the lane registry                                                                                |
| Toolchain | 5.3    | Yes     | Contributor-only rules in the self-listing                                                                                                |
| Toolchain | 6.1    | Yes     | `ignoreErrors` in `qaConfig/phpstan.neon`, loaded by PHPStan                                                                              |
| Toolchain | 6.2    | Partial | `bin/qa -t pij` requires a comment, rejects the paste-anywhere list and short reasons; reads the top-level file alone                     |
| Toolchain | 6.3    | Yes     | The record, including an included baseline's entries, appears in `bin/rules` output                                                       |
| Toolchain | 6.4    | Partial | Lane defaults in `docs/tools/`; no default for the method's calibrations                                                                  |
| Toolchain | 7.1    | No      | The agent block carries no rule lines                                                                                                     |
| Toolchain | 7.2    | Yes     | Block written and refreshed on install and update                                                                                         |
| Toolchain | 8.1    | Partial | `RuleDocumentationTest` covers rules and identifier-printing lanes; requires an index row, not a page                                     |
| Toolchain | 8.2    | Yes     | `SelfCheckRunsBundledRulesTest`; own `qaConfig/phpstan.neon` includes both bundles; `bin/qa -t arch` runs the tier on `src/`              |
| Toolchain | 9.1    | Yes     | Artefact and project graded separately above                                                                                              |
| Toolchain | 9.2    | Yes     | `composer.json` `extra.defence-before-fix`: method 1.0.0, toolchain 0.2.0, eight gaps; `project` object with the same keys and three gaps |

## Notes for a practitioner

Install the plugin, write the rule under `rules:` with a `phpqaci`-style identifier constant, prove it with `bin/phpstan-rule` on a fixture, sweep with `bin/qa -t phpstan`, and add the documentation page so `bin/rule-doc` resolves it to a correct construction and not only to a summary. Run `bin/rules .` first on any project you arrive at: the listing and the justified exceptions are the record the method tells you to read before guessing. Treat a PHPArkitect violation as a defence with no identifier, keep `phparkitect-baseline.json` out of the repository, and put any PHPStan baseline entries in `qaConfig/phpstan.neon` itself so the justification lane sees them.
