---
title: Biome and Defence Before Fix
summary: GritQL plugin diagnostics carry no identifier, failing 4.3; biome-ignore cannot be switched off, failing 7.1; biome explain meets 6.1 to 6.3 for built-ins
---

# Biome

**Language**: JavaScript and TypeScript · **Kind**: tool · **Readiness**: 🔴 · **Detector conformance**: 🔴 · **Checked**: 2026-09-08, version 2.5.12

Biome is a single Rust binary that formats and lints JavaScript, TypeScript, JSON, CSS and, since 2.4, HTML. It is fast, has a large catalogue of built-in rules with excellent shipped documentation, and since 2.0 accepts linter plugins written in GritQL. In a pipeline it replaces Prettier and much of ESLint at once, which is its appeal and also the reason it hosts bespoke defences poorly.

## How it is conformant

The built-in catalogue does several things the detector specification wants. Every finding prints its rule as `group/ruleName`, `biome lint --only=<rule>` runs one rule alone and the command accepts a single file path ([CLI reference](https://biomejs.dev/reference/cli/)), so a built-in rule can be run in isolation on a fixture, which meets 4.2 for the bundled catalogue and clauses 5.1 to 5.4. `biome explain <rule>` prints the rule's documentation from the installed binary ([CLI reference](https://biomejs.dev/reference/cli/)), which is a genuine clause 6.1 mechanism, keyed on the identifier as printed, and it meets 6.2 and 6.3 because the documentation is inside the binary at the same version. Bespoke patterns can be expressed as GritQL plugins registered under `plugins` in `biome.json`, with `register_diagnostic()` carrying a message and severity ([linter plugins](https://biomejs.dev/linter/plugins/)). A suppression comment requires an explanation after the colon ([suppressions](https://biomejs.dev/analyzer/suppressions/)), which is what clause 7.2 asks.

## How it is not conformant

The plugin route fails clause 4.3, which is structural. A plugin diagnostic is reported under the generic `lint/plugin` category and suppressed with `lint/plugin` comments; the plugin documentation describes no way for a plugin to declare a rule identifier of its own ([linter plugins](https://biomejs.dev/linter/plugins/)). A bespoke defence in Biome therefore prints a message but no stable identifier, which is the condition the readiness grade calls red, and `biome explain` cannot resolve what was never printed. `--only` cannot select one plugin either, so the clause 4.2 harness is only available for built-in rules, and clause 4.1 is partial because GritQL expresses a pattern match and nothing more. Clause 7.1 fails as well: `biome-ignore`, `biome-ignore-all` and the range forms are built in, no configuration switches them off, and the only diagnostic Biome raises about them is `suppressions/unused` for a comment that had no effect ([suppressions](https://biomejs.dev/analyzer/suppressions/)); the documentation describes no check that sees the rest.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                       |
| -------- | ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Detector | 4.1    | Partial      | GritQL plugins for pattern matching only ([linter plugins](https://biomejs.dev/linter/plugins/))                                               |
| Detector | 4.2    | Partial      | `--only` works for built-in rules, not for a plugin ([CLI reference](https://biomejs.dev/reference/cli/))                                      |
| Detector | 4.3    | No           | Plugin diagnostics carry the generic `lint/plugin` category ([linter plugins](https://biomejs.dev/linter/plugins/))                            |
| Detector | 4.4    | No           | No rule over the rules                                                                                                                         |
| Detector | 5.1    | Yes          | Single binary, runs locally                                                                                                                    |
| Detector | 5.2    | Yes          | `biome lint <file>` ([CLI reference](https://biomejs.dev/reference/cli/))                                                                      |
| Detector | 5.3    | Yes          | Findings are the command's output                                                                                                              |
| Detector | 5.4    | Yes          | Same rules everywhere                                                                                                                          |
| Detector | 6.1    | Partial      | `biome explain <rule>` resolves built-in identifiers; a plugin prints nothing resolvable ([CLI reference](https://biomejs.dev/reference/cli/)) |
| Detector | 6.2    | Yes          | `biome explain` reads from the installed binary                                                                                                |
| Detector | 6.3    | Yes          | Built-in documentation ships inside the binary at the same version                                                                             |
| Detector | 6.4    | Not verified | Not documented                                                                                                                                 |
| Detector | 7.1    | No           | `biome-ignore` family cannot be disabled; only unused comments are reported ([suppressions](https://biomejs.dev/analyzer/suppressions/))       |
| Detector | 7.2    | Yes          | An explanation after the colon is required, though its content is not validated ([suppressions](https://biomejs.dev/analyzer/suppressions/))   |

## Notes for a practitioner

Use Biome for what it is good at, the built-in catalogue with `biome explain` for lookup, and host bespoke defences in an ESLint plugin alongside it until Biome plugins can carry an identifier. If you do write a GritQL plugin, put a hand-chosen identifier at the start of the diagnostic message so that something stable reaches the reader, and keep the documentation for it in your own repository. Ban the `biome-ignore` family with a lint rule elsewhere, since Biome cannot switch it off.
