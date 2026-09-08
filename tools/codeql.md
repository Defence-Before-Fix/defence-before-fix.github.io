---
title: CodeQL and Defence Before Fix
summary: Custom packs and a test harness meet section 4; database build and licence weaken 5.1; no id lookup for 6.1; inline suppression fails 8.3
---

# CodeQL

**Language**: Multi-language · **Kind**: tool · **Readiness**: 🟡 · **Conformance**: 🔴 · **Checked**: 2026-09-08, version CLI 2.26.4

CodeQL is GitHub's semantic code analysis engine. It extracts a relational database from a codebase and runs queries written in the QL language against it, and it is the engine behind GitHub code scanning. In a pipeline it is the deep, slow security check rather than the on-every-edit linter, and its licence binds it tightly to GitHub: outside open-source code it may only be used with a GitHub Advanced Security licence.

## How it is conformant

Bespoke queries are first class (4.1): a project writes `.ql` files with `@id` and `@kind` metadata in its own pack declared by `qlpack.yml`, per [using custom queries](https://docs.github.com/en/code-security/codeql-cli/using-the-codeql-cli/using-custom-queries-with-the-codeql-cli). There is a real proving harness (4.2): `codeql test run` takes a `.qlref` beside example code and an `.expected` file, builds a test database from the example files alone, and reports the diff ([testing custom queries](https://docs.github.com/en/code-security/codeql-cli/using-the-codeql-cli/testing-custom-queries)). The identifier is author-chosen and stable (4.3): `@id` is required and unique, lowercase letters and digits with `/` or `-` ([query metadata](https://codeql.github.com/docs/writing-codeql-queries/metadata-for-codeql-queries/)), and it appears as `ruleId` on every SARIF result ([SARIF support](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)). Query help travels with the query as a `.qhelp` or `.md` file and can be rendered by `codeql generate query-help` or embedded with `--sarif-include-query-help` ([generate query-help](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help)), which meets 6.3 for bundled queries. The CLI bundle is self-contained and documented for machines without internet access ([setting up the CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli)). The github/codeql repository runs its own queries on itself, runs `codeql test run` in CI and checks for duplicate `@id` values, which satisfies 10.2 and part of 10.1.

## How it is not conformant

Clause 5.1 is met technically and failed in practice for most projects. No server is required, but every run needs a database built first, with a full build for most compiled languages unless `--build-mode none` applies ([creating databases](https://docs.github.com/en/code-security/codeql-cli/using-the-codeql-cli/creating-codeql-databases)), and [the CLI licence](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md) forbids use on private codebases without a paid GitHub Advanced Security licence. That licence condition is what puts the readiness grade at amber: a practitioner on private code cannot legally follow the method with this tool alone. Clause 5.2 is partial: analysis targets a whole database, and only the test harness targets a directory of snippets. Clause 5.3 is partial: `database analyze` writes CSV or SARIF to a mandatory `--output` file with no terminal text format ([database analyze](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-analyze)), and whether `query run` prints the `@id` is not verified. Clause 6.1 is failed: no command resolves a printed `@id` to its help, and the [query help site](https://codeql.github.com/codeql-query-help/) is online; resolution is by file path. Clause 7.1 is failed: `codeql resolve queries` lists paths only, with no identifier or description ([resolve queries](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-queries)). Section 8 is failed: `// codeql[query-id]` comments suppress inline, and although suppression can be disabled by omitting the alert-suppression query from the suite, that is stated in a repository discussion rather than documentation ([discussion](https://github.com/github/codeql/discussions/10940)); the GitHub dismissal flow requires a reason from a list but the free-text comment is optional ([resolving alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts)), and no project record exists that the CLI reads. No method specification version is declared (11.1).

## Clause by clause

| Clause | Result  | Evidence                                                                                                                                                             |
| ------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes     | Custom packs with `qlpack.yml` ([custom queries](https://docs.github.com/en/code-security/codeql-cli/using-the-codeql-cli/using-custom-queries-with-the-codeql-cli)) |
| 4.2    | Yes     | `codeql test run` with `.qlref` and `.expected` ([testing](https://docs.github.com/en/code-security/codeql-cli/using-the-codeql-cli/testing-custom-queries))         |
| 4.3    | Yes     | Required unique `@id` ([metadata](https://codeql.github.com/docs/writing-codeql-queries/metadata-for-codeql-queries/)); SARIF `ruleId`                               |
| 4.4    | Partial | Duplicate-id CI check in github/codeql, not shipped to consumers                                                                                                     |
| 5.1    | Partial | No server, but database build required and licence limits private use ([licence](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md))                |
| 5.2    | Partial | Whole database; snippets only via the test harness                                                                                                                   |
| 5.3    | Partial | `database analyze` writes to `--output` only ([manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/database-analyze))                      |
| 5.4    | Yes     | Every query runs from the CLI                                                                                                                                        |
| 6.1    | No      | No lookup keyed on `@id`; resolution is by path                                                                                                                      |
| 6.2    | Partial | Help files ship in packs as markdown; not verified for every pack                                                                                                    |
| 6.3    | Yes     | `.qhelp`/`.md` beside each query ([generate query-help](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/generate-query-help))                  |
| 7.1    | No      | `resolve queries` prints paths only ([manual](https://docs.github.com/en/code-security/codeql-cli/codeql-cli-manual/resolve-queries))                                |
| 7.2    | Partial | Derived from the suite, but see 7.1                                                                                                                                  |
| 7.3    | Partial | Custom packs resolve in the same listing, paths only                                                                                                                 |
| 8.1    | No      | No project record read by the CLI                                                                                                                                    |
| 8.2    | No      | Dismissal comment optional ([resolving alerts](https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/resolving-code-scanning-alerts)) |
| 8.3    | No      | `// codeql[id]` inline suppression ([changelog 2.12.0](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.12.0/))                          |
| 8.4    | No      | No enumeration of exceptions with the queries                                                                                                                        |
| 8.5    | Partial | Default suites documented; no method calibrations                                                                                                                    |
| 9.1    | No      | No agent summary                                                                                                                                                     |
| 9.2    | No      | No delivery mechanism                                                                                                                                                |
| 10.1   | Partial | Duplicate `@id` check in CI; no documented gate on missing help                                                                                                      |
| 10.2   | Yes     | `codeql-analysis.yml` and `codeql test run` in [repository CI](https://github.com/github/codeql/tree/main/.github/workflows)                                         |
| 11.1   | No      | No declaration                                                                                                                                                       |

## Notes for a practitioner

On open-source code or with an Advanced Security licence, CodeQL can carry the method: write the query in a project pack, prove it red with `codeql test run` on a snippet that carries the hazard, sweep by analysing the full database, and keep the `.md` help beside the query. Emit SARIF and read `ruleId` from it, because the CLI prints no identifier to the terminal. Omit the alert-suppression query from your suite so inline `codeql[...]` comments have no effect, and record exceptions in the config file's `paths-ignore` with a stated reason.
