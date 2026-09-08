# Fixture: Lintomatic 4.2

A fictional detector, described only as far as its documentation would describe it. Grade it
against the document you were given. Where the description does not say, answer from what is
written, not from what a real tool would probably do.

## What the documentation says

Lintomatic is a static analyser for the Zig language. It ships forty rules. A project can add its
own rules by writing a Zig module that implements the `Rule` interface and listing it in
`lintomatic.toml`; project rules are loaded on every run and are first class in every report.

The command `lintomatic check <path>` analyses a directory or a single file and prints one line
per finding to standard output:

```
src/db.zig:41:7  LM-0107  Result of fallible call discarded
src/db.zig:88:3  proj.no-raw-sql  Query built by string concatenation
```

Fuller detail, including a snippet, is written to `.lintomatic/report.html`. The one-line form is
printed whether or not the HTML report is enabled.

`lintomatic check --only <identifier> <path>` runs a single rule. It accepts any rule name,
bundled or project, and exits 1 when the rule fires, 0 when it does not, and 2 when the rule name
is unknown.

Rule identifiers for bundled rules are of the form `LM-NNNN` and are fixed at the rule's first
release. Project rules are identified by the name the project gives them in `lintomatic.toml`,
which the documentation recommends prefixing with `proj.`; Lintomatic does not add or rewrite
any part of the name.

`lintomatic explain <identifier>` prints the documentation for a bundled rule from the installed
package: what the rule finds, why, and the recommended construction. For a project rule it prints
the `doc` string the rule module declares, or `No documentation declared` when there is none.
The documentation is versioned with the package; there is no separate website.

Lintomatic honours the comment `// lintomatic-ignore <identifier>` on the line before a finding.
The comment can be disabled project-wide with `ignore_comments = false` in `lintomatic.toml`.
The comment takes no reason and the documentation does not mention one.

The tool runs locally with no account, no server and no network, and the same binary is what CI
runs. There is a hosted dashboard, sold separately, that aggregates reports across repositories;
every finding it shows is also printed by the command line.

Lintomatic's own repository runs `lintomatic check src` in CI but does not check that every
`LM-NNNN` identifier has an `explain` entry; two of the forty rules currently print
`No documentation declared`.
