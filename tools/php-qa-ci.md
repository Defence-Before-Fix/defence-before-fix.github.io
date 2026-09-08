---
title: php-qa-ci and Defence Before Fix
summary: Harness, resolver, derived listing and justified record all verified by running them; declares toolchain 0.1.0 with an empty gap record; section 9 partial.
---

# php-qa-ci

**Language**: PHP · **Kind**: toolchain · **Readiness**: 🟢 · **Conformance**: 🟢 · **Checked**: 2026-09-08, branch php8.4 at commit 8a45ed0

php-qa-ci is a Composer plugin that wraps PHPStan, PHPUnit, PHP-CS-Fixer, Infection and a set of its own lanes behind one `bin/qa` entry point, ships a bundle of PHPStan rules with their documentation, and writes an agent-facing block into the consuming project. It is the PHP reference toolchain for this method and the one PHP tool in this register that claims conformance ([repository](https://github.com/LongTermSupport/php-qa-ci)).

## Tools it bundles

php-qa-ci is a toolchain rather than a tool, so the question for each lane it runs is whether that lane can host a bespoke defence under the method, and which of the toolchain's own mechanisms wrap it. Every lane below is registered by `bin/qa`, appears in the `bin/rules` listing, and has its lane identifier resolved by `bin/rule-doc`; `bin/phpstan-rule` wraps PHPStan alone.

- **PHPStan**: hosts bespoke defences; wrapped by `bin/phpstan-rule`, `bin/rule-doc` and `bin/rules`, with the bundled rules and the identifier constant enforced on top.
- **PHPArkitect**: hosts bespoke defences about architecture through `phparkitect.php`; wrapped by `bin/rules` and `bin/rule-doc` at lane level, with no single-rule harness of its own.
- **Rector**: a refactoring tool run in dry-run mode; a project can register a custom rule, but the toolchain wraps it only as a lane in `bin/rules` and `bin/rule-doc`.
- **PHP CS Fixer**: a formatter; cannot host a defence in the method's sense, and is wrapped only as a lane.
- **PSR-4 validation**: a fixed check of autoload mapping; not a host, wrapped as a lane.
- **Composer validation and composer require checker**: fixed checks of the manifest and of undeclared dependencies; not hosts, wrapped as lanes.
- **Package type**: a bundled defence of the toolchain's own, requiring an explicit `type` in `composer.json`; not a host for project rules, documented in `docs/tools/` and resolved by `bin/rule-doc`.
- **Config template ignore-list audit**: a bundled defence over the toolchain's own templates; not a host, resolved by `bin/rule-doc`.
- **Infection config source dirs check**: a bundled defence that `infection.json` names real directories; not a host, resolved by `bin/rule-doc`.
- **Strict types**: a fixed check that every file declares strict types; not a host, wrapped as a lane.
- **PHP lint**: a syntax check; not a host, wrapped as a lane.
- **Markdown links**: a fixed link check; not a host, wrapped as a lane.
- **Branch name policy**: a fixed naming check; not a host, wrapped as a lane.
- **PHPStan ignoreErrors justification**: the clause 8.2 mechanism itself, a bundled defence over the project record; not a host, resolved by `bin/rule-doc`.
- **SensitiveParameter usage**: a bundled defence requiring the attribute somewhere in `src/`; not a host, documented in `docs/tools/` and resolved by `bin/rule-doc`.
- **PHPUnit**: a test runner; cannot host a defence, since the method rules out a test as the net, and is wrapped only as a lane.
- **Infection**: a mutation tester; cannot host a defence, wrapped only as a lane, with its configuration guarded by the source dirs check above.

## How it is conformant

Every mechanism was checked by running it in a checkout rather than by reading the README. Clause 4.1 is inherited from PHPStan: a project's own rule classes go under `rules:` in its `qaConfig/phpstan.neon`. Clause 4.2 is met by `bin/phpstan-rule <identifier> <path>`, whose usage line names a single identifier and a single file, and clause 4.3 by identifier constants of the form `phpqaci.*`, enforced under clause 4.4 by the bundled `RequireRuleIdentifierConstantRule`, which is on by default in `rules-default.neon`. Clauses 5.1 to 5.4 are met by `bin/qa -t <tool> -p <path>`, which runs any single lane over any single path and prints to the terminal. Clause 6.1 is met by `bin/rule-doc <identifier>`, which resolved `phpqaci.nullCoalescingFalse` to its rule class, source path and shipped page; that page lives in `docs/phpstan-rules/` inside the package, which meets 6.2 and 6.3. Clauses 7.1 to 7.3 are met by `bin/rules .`, which walks the resolved PHPStan configuration and the lane registry and printed one line per rule with its identifier and summary, project entries included. Clause 8.1 is met because the record is the `ignoreErrors` block PHPStan itself reads; clause 8.2 by the `pij` lane, which the help text describes as asserting that every entry carries a usable justification; clause 8.3 by the bundled `ForbidInlinePhpstanIgnoreRule`, on by default; and clause 8.4 because the same `bin/rules` listing carries the record. Clause 10.2 is guarded by `SelfCheckRunsBundledRulesTest`, and the package's own `qaConfig/phpstan.neon` includes both bundles. The `composer.json` manifest declares `extra.defence-before-fix` with method 1.0.0, toolchain 0.1.0 and an empty `known-gaps` array, which is clause 11.1.

## How it is not conformant

No MUST failure was found. Two limits are worth stating. Clause 10.1 was verified by the presence of the documentation tests rather than by breaking a page and watching a release fail, and the full pipeline under clause 10.2 was not re-run here; the grade rests on the guarding tests and the declared gap record being empty. Section 9 is only partly met: the agent block is delivered and refreshed, but it does not yet carry the rule summary, so the toolchain conforms without agent support.

## Clause by clause

| Clause | Result  | Evidence                                                                                      |
| ------ | ------- | --------------------------------------------------------------------------------------------- |
| 4.1    | Yes     | PHPStan `rules:` in the project's `qaConfig/phpstan.neon`                                     |
| 4.2    | Yes     | `bin/phpstan-rule <identifier> <path>`, usage confirmed in the checkout                       |
| 4.3    | Yes     | `phpqaci.*` constants, printed by PHPStan with each error                                     |
| 4.4    | Yes     | `RequireRuleIdentifierConstantRule` in `rules-default.neon`                                   |
| 5.1    | Yes     | `bin/qa` runs locally                                                                         |
| 5.2    | Yes     | `bin/qa -t <tool> -p <path>`                                                                  |
| 5.3    | Yes     | Output to the terminal                                                                        |
| 5.4    | Yes     | Same lanes locally and in CI                                                                  |
| 6.1    | Yes     | `bin/rule-doc phpqaci.nullCoalescingFalse` resolved in the checkout                           |
| 6.2    | Yes     | `docs/phpstan-rules/` ships in the package                                                    |
| 6.3    | Yes     | Same                                                                                          |
| 7.1    | Yes     | `bin/rules .` printed every rule with identifier and summary                                  |
| 7.2    | Yes     | Derived from the resolved neon chain and the lane registry                                    |
| 7.3    | Yes     | Project rules appear in the same listing                                                      |
| 8.1    | Yes     | `ignoreErrors` in `qaConfig/phpstan.neon`, read by PHPStan                                    |
| 8.2    | Yes     | `bin/qa -t pij` fails an entry without a justification                                        |
| 8.3    | Yes     | `ForbidInlinePhpstanIgnoreRule` on by default                                                 |
| 8.4    | Yes     | The record appears in `bin/rules` output                                                      |
| 8.5    | Partial | Lane defaults are documented in `docs/tools/`; method calibrations are not                    |
| 9.1    | No      | The agent block carries no rule summary yet                                                   |
| 9.2    | Yes     | Block written and refreshed on install                                                        |
| 10.1   | Yes     | `RuleDocumentationTest` and `RuleDocResolverTest` run in the pipeline                         |
| 10.2   | Yes     | `SelfCheckRunsBundledRulesTest`; own `qaConfig/phpstan.neon` includes both bundles            |
| 11.1   | Yes     | `composer.json` `extra.defence-before-fix`: method 1.0.0, toolchain 0.1.0, `known-gaps` empty |

## Notes for a practitioner

Install the plugin, write the rule under `rules:` with a `phpqaci`-style identifier constant, prove it with `bin/phpstan-rule` on a fixture, sweep with `bin/qa -t phpstan`, and add the documentation page so `bin/rule-doc` resolves it. Run `bin/rules .` first on any project you arrive at: the listing and the justified exceptions are the record the method tells you to read before guessing.
