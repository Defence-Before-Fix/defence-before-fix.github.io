---
title: Biome and Defence Before Fix
summary: GritQL plugin diagnostics carry no identifier of their own, failing 4.3; fails 8.3 on biome-ignore; biome explain meets 6.1 and 6.2 for built-ins only
---

# Biome

**Language**: JavaScript and TypeScript · **Kind**: tool · **Readiness**: 🔴 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version 2.5.12

Biome is a single Rust binary that formats and lints JavaScript, TypeScript, JSON, CSS and, since 2.4, HTML. It is fast, has a large catalogue of built-in rules with excellent shipped documentation, and since 2.0 accepts linter plugins written in GritQL. In a pipeline it replaces Prettier and much of ESLint at once, which is its appeal and also the reason it hosts bespoke defences poorly.

## How it is conformant

The built-in catalogue does several things this method wants. Every finding prints its rule as `group/ruleName`, `biome lint --only=<rule>` runs one rule alone and the command accepts a single file path ([CLI reference](https://biomejs.dev/reference/cli/)), so a built-in rule can be run in isolation on a fixture. `biome explain <rule>` prints the rule's documentation from the installed binary ([CLI reference](https://biomejs.dev/reference/cli/)), which is a genuine clause 6.1 and 6.2 mechanism, offline and keyed on the identifier as printed. Bespoke patterns can be expressed as GritQL plugins registered under `plugins` in `biome.json`, with `register_diagnostic()` carrying a message and severity ([linter plugins](https://biomejs.dev/linter/plugins/)). Suppression comments require an explanation after the colon ([suppressions](https://biomejs.dev/analyzer/suppressions/)), which is more than ESLint asks.

## How it is not conformant

The plugin route fails clause 4.3. A plugin diagnostic is reported under the generic `lint/plugin` category and suppressed with `lint/plugin` comments; the plugin documentation describes no way for a plugin to declare a rule identifier of its own ([linter plugins](https://biomejs.dev/linter/plugins/)). A bespoke defence in Biome therefore prints a message but no stable identifier, which is the condition the readiness grade calls red, and `biome explain` cannot resolve what was never printed. `--only` cannot select one plugin either, so the red proof under 4.2 is only available for built-in rules. Clause 8.3 fails structurally: `biome-ignore`, `biome-ignore-all` and the range forms are built in, the required explanation is free text with no validation, and nothing bundled bans the comments ([suppressions](https://biomejs.dev/analyzer/suppressions/)). There is no project record, no listing of active rules with routes, and no declaration under 11.1.

## Clause by clause

| Clause | Result       | Evidence                                                                                                                          |
| ------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Partial      | GritQL plugins for pattern matching only ([linter plugins](https://biomejs.dev/linter/plugins/))                                  |
| 4.2    | Partial      | `--only` works for built-in rules, not for a plugin ([CLI reference](https://biomejs.dev/reference/cli/))                         |
| 4.3    | No           | Plugin diagnostics carry the generic `lint/plugin` category ([linter plugins](https://biomejs.dev/linter/plugins/))               |
| 4.4    | No           | No rule over the rules                                                                                                            |
| 5.1    | Yes          | Single binary, runs locally                                                                                                       |
| 5.2    | Yes          | `biome lint <file>` ([CLI reference](https://biomejs.dev/reference/cli/))                                                         |
| 5.3    | Yes          | Findings are the command's output                                                                                                 |
| 5.4    | Yes          | Same rules everywhere                                                                                                             |
| 6.1    | Partial      | `biome explain <rule>` resolves built-in identifiers only ([CLI reference](https://biomejs.dev/reference/cli/))                   |
| 6.2    | Yes          | `biome explain` reads from the installed binary                                                                                   |
| 6.3    | Yes          | Built-in documentation ships inside the binary at the same version                                                                |
| 7.1    | No           | No command lists the active rules with descriptions and routes                                                                    |
| 7.2    | No           | Same                                                                                                                              |
| 7.3    | No           | Same                                                                                                                              |
| 8.1    | No           | No project record                                                                                                                 |
| 8.2    | Partial      | Suppression comments require an explanation, but it is not validated ([suppressions](https://biomejs.dev/analyzer/suppressions/)) |
| 8.3    | No           | `biome-ignore` family is built in and undefended ([suppressions](https://biomejs.dev/analyzer/suppressions/))                     |
| 8.4    | No           | No listing of exceptions                                                                                                          |
| 8.5    | Partial      | Recommended rule set is documented                                                                                                |
| 9.1    | No           | No agent summary                                                                                                                  |
| 9.2    | No           | No delivery mechanism                                                                                                             |
| 10.1   | Not verified | Not documented                                                                                                                    |
| 10.2   | Not verified | Not documented                                                                                                                    |
| 11.1   | No           | No declaration                                                                                                                    |

## Notes for a practitioner

Use Biome for what it is good at, the built-in catalogue with `biome explain` for lookup, and host bespoke defences in an ESLint plugin alongside it until Biome plugins can carry an identifier. If you do write a GritQL plugin, put a hand-chosen identifier at the start of the diagnostic message so that something stable reaches the reader, and keep the documentation for it in your own repository.
