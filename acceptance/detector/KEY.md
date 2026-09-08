# Answer key for DETECTOR-SPEC.md

Marked against the document at the version named in the changelog entry that records the run.
Quotations below are from the document; when a clause is reworded, update the quotation here in
the same commit.

## 1. Restatement

A bullet is correct when it names one of these obligations. Four or more correct bullets, and no
bullet asserting an obligation the document does not state, is a correct restatement.

- Support bespoke rules written by the project (4.1).
- Provide a harness that runs a single rule against supplied code (4.2).
- Allow a stable identifier per rule and print it, unaltered, with every finding (4.3).
- Be invocable locally by the practitioner, over a subset down to one file, with the result in
  the command's own output and never only through a hosted service or CI-only mode (5.1 to 5.4).
- Resolve a printed identifier to documentation; for bundled rules from the installed copy,
  offline, with the documentation shipped and versioned with the rule (6.1 to 6.3).
- Make any inline suppression route detectable or disableable (7.1).

Wrong if it asserts: the detector must enforce a project's suppression policy; the detector must
declare a version to conform; the detector must list a project's active defences or produce an
agent summary (those belong to the toolchain specification).

## 2. Load-bearing statements

- **2a.** Conformance is satisfying every MUST in sections 4 to 7, judged on evidence; a detector
  that predates the document can conform, and the declaration is optional. Key quotation, section
  8: "A Detector Conforms if it satisfies every MUST in sections 4 to 7." Supporting, 8.1: "A
  maintainer MAY declare the version of this document the detector conforms to". An answer that
  says a declaration is required, or that partial satisfaction is conformance, is wrong.
- **2b.** It must make the route either disableable by configuration or detectable by a rule the
  project can write or a mechanical check it documents; it is not required to remove or forbid
  it. Key quotation, 7.1: "It MUST make each one either disableable by configuration, or
  detectable by a Rule the project can write in the Detector itself or by a mechanical check the
  Detector documents". An answer that says the detector must forbid the route, or must require a
  reason (7.2 is SHOULD), is wrong.
- **2c.** With the rule, in the installed copy, at a version tracked together, and yes, offline.
  Key quotations, 6.2: "Resolution of a bundled rule's identifier MUST work from the installed
  copy, without network access"; 6.3: "A bundled rule's documentation MUST ship with the rule, at
  a version tracked together". An answer naming the detector's website as an acceptable location
  is wrong.

## 3. Application: Lintomatic 4.2

| Clause | Intended verdict | Reasoning the fixture supports                                                                                       |
| ------ | ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| 4.1    | Yes              | Project rules via the `Rule` interface, first class in every report                                                  |
| 4.2    | Yes              | `check --only <identifier> <path>` runs one rule, bundled or project, with a distinguishing exit code                |
| 4.3    | Yes              | `LM-NNNN` fixed at first release; project names taken as given, not rewritten; printed on every finding line         |
| 5.1    | Yes              | Local, no account, no server, no network                                                                             |
| 5.2    | Yes              | `check <path>` accepts a single file                                                                                 |
| 5.3    | Yes              | One line per finding on standard output whether or not the HTML report is enabled                                    |
| 5.4    | Yes              | The hosted dashboard shows nothing the command line does not print                                                   |
| 6.1    | Yes              | `explain <identifier>` resolves a printed identifier; project rules resolve to their declared `doc` string           |
| 6.2    | Yes              | `explain` reads the installed package; there is no website                                                           |
| 6.3    | No               | Two of forty bundled rules print `No documentation declared`; every identifier a bundled rule can print MUST resolve |
| 7.1    | Yes              | The ignore comment is disableable with `ignore_comments = false`                                                     |

Section 8 verdict: **does not conform**, because 6.3 fails and partial conformance MUST NOT be
described as conformance. A reader who grades 6.3 Partial on the grounds that thirty-eight resolve
has read the clause differently and that counts against the document; a reader who grades 6.3 Yes
because they missed the last paragraph of the fixture has misread the fixture, not the document.

Clause 6.4: **does not change the verdict**. It is a SHOULD, and Lintomatic's failure to check its
own identifiers in CI is a missed SHOULD, not a further MUST failure; the MUST that fails is 6.3.

A reader who marks 7.1 No because the comment takes no reason has confused 7.1 with 7.2, which is
SHOULD; that counts against the document if the reasoning quotes 7.1 or 7.2.

## 4. Ambiguity

No keyed answer. Record every clause named; two or more readers naming the same clause is a
blocking finding under `ACCEPTANCE.md`.

## 5. Clarity

No keyed answer. Median 4 or above, none below 3.
