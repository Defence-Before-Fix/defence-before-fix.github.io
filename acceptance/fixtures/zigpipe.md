# Fixture: the Zigpipe project

A fictional project and the tooling it has assembled, described only as far as its own
documentation and configuration would show. Grade the project's toolchain against the document
you were given. Where the description does not say, answer from what is written.

## What the project's documentation says

Zigpipe is a Zig service. Its quality checks are assembled from three sources:

- **Lintomatic 4.2**, a third-party detector. It hosts bespoke rules, runs a single rule against
  a single file, prints a stable identifier with every finding, resolves bundled identifiers
  offline with `lintomatic explain`, and its inline `// lintomatic-ignore` comment can be
  disabled project-wide. Two of its forty bundled rules currently have no documentation.
- **zig-qa**, a first-party package the company publishes for all its Zig projects. It ships six
  defences of its own as Lintomatic rules with identifiers `zq.*`, a script `zig-qa run` that
  runs Lintomatic and then the test suite in that order and stops when Lintomatic fails, and a
  script `zig-qa list` that reads `lintomatic.toml` and prints every active rule with its
  identifier, a one-line summary and the path to its documentation. The six `zq.*` rules'
  documentation ships in the package under `docs/rules/`. `zig-qa run` prints Lintomatic's
  output unchanged, one line per finding.
- **Project rules**, four Lintomatic rules the Zigpipe team wrote, identifiers `proj.*`,
  documented in `docs/defences/` in the repository, one page per identifier, each saying what
  the rule forbids, why, and what to write instead. `zig-qa list` includes them.

Zigpipe's `lintomatic.toml` sets `ignore_comments = false`. Exceptions are kept in
`quality-exceptions.toml`, which `zig-qa run` loads before it runs Lintomatic; each entry has an
identifier, a path and a free-text `reason` field. `zig-qa run` refuses to start when an entry's
`reason` is empty. `zig-qa list --exceptions` prints the file's entries in the same format as the
rule listing.

The two undocumented Lintomatic bundled rules are enabled in `lintomatic.toml`; nothing in the
project or in zig-qa provides documentation for them, and `zig-qa list` prints their
documentation path as `(none)`.

Zigpipe does not publish a summary of its defences for an agent and has no `AGENTS.md` or
equivalent. It does not ship any tooling to other projects. It has no machine-readable
declaration of which specification version it follows.
