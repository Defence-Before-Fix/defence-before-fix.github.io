# Answer key for TOOLING-SPEC.md

Marked against the document at the version named in the changelog entry that records the run.
Quotations below are from the document; when a clause is reworded, update the quotation here in
the same commit.

## 1. Restatement

A bullet is correct when it names one of these obligations. Four or more correct bullets, and no
bullet asserting an obligation the document does not state, is a correct restatement.

- Route defences only through detectors that conform to the detector specification, wrapping
  permitted (4.1).
- Resolve every identifier a routed defence can print, including the project's own, offline,
  to documentation stating the correct construction (4.2).
- Forbid, by disabling or by a blocking defence, every suppression route that bypasses the
  project record (4.3).
- The toolchain's own entry point meets the detector reporting clauses and prints identifiers
  unaltered (4.4), and runs detectors before runners, stopping on a detector failure (4.5).
- List the active defences, derived from configuration, including the project's own (5.1 to
  5.3).
- Define and read a project record whose exceptions each carry a justification, enumerable the
  same way as the defences (6.1 to 6.3).
- A shipped toolchain also fails its release on undocumented bundled defences and runs its own
  defences on its own source (8.1, 8.2).

Wrong if it asserts: the toolchain must be a single product; a declaration is required to
conform; the agent summary (section 7) is a MUST.

## 2. Load-bearing statements

- **2a.** At the project level; the toolchain is whatever the project has assembled from
  third-party, first-party and project-level parts. Key quotation, section 9: "A project's
  Toolchain Conforms if every MUST in sections 4 to 6 holds across the assembled parts, wherever
  each part came from". An answer that says conformance is graded per tool, or that only a
  packaged product can conform, is wrong.
- **2b.** One grade; which part satisfied each clause is evidence, not a grade of its own. Key
  quotation, section 9: "The project-level verdict is a single grade; which part of the Toolchain
  satisfied each clause is evidence for that grade, not a second grade."
- **2c.** Two, graded and declared separately, and neither implies the other. Key quotation,
  9.1: "The two verdicts MUST be graded and declared separately, and neither implies the other."
  An answer giving one grade, or saying the artefact grade follows from the project grade, is
  wrong.

## 3. Application: the Zigpipe project

| Clause | Intended verdict | Reasoning the fixture supports                                                                                                 |
| ------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 4.1    | No               | Lintomatic fails detector 6.3 on two undocumented bundled rules and nothing in the wrapping closes that gap                    |
| 4.2    | No               | `zq.*` and `proj.*` resolve offline, but the two enabled bundled rules resolve to `(none)`                                     |
| 4.3    | Yes              | Ignore comments disabled project-wide; exceptions only through the record the toolchain reads                                  |
| 4.4    | Yes              | `zig-qa run` is local, prints Lintomatic's output unchanged, one line per finding                                              |
| 4.5    | Yes              | Lintomatic, then the tests, stopping on a Lintomatic failure                                                                   |
| 5.1    | Yes              | `zig-qa list` prints identifier, summary and documentation path without running the rules                                      |
| 5.2    | Yes              | Derived from `lintomatic.toml`, not hand-maintained                                                                            |
| 5.3    | Yes              | The `proj.*` rules appear in the same listing                                                                                  |
| 6.1    | Yes              | `quality-exceptions.toml` is a defined path that `zig-qa run` loads                                                            |
| 6.2    | Partial or No    | A justification is required and an empty one rejected, but nothing rejects a justification that could be pasted onto any entry |
| 6.3    | Yes              | `zig-qa list --exceptions` uses the same format and operation as the rule listing                                              |

Either Partial or No is accepted for 6.2; the reasoning must mention the generic-justification
requirement. A Yes on 6.2 with reasoning that quotes only the first sentence of the clause is a
finding against the document.

Section 9 verdict: **does not conform**, because 4.1 and 4.2 fail; partial conformance MUST NOT be
described as conformance. **Not with agent support**, because section 7 is not met (no summary).
**Section 8 does not apply**, because Zigpipe ships nothing to other projects; a reader who applies
8.1 to Zigpipe on the basis that Zigpipe's tooling includes a shipped package (zig-qa) has read
"the toolchain is one the project ships" differently, and that counts against the document. The
correct reading is that section 8 bears on zig-qa's own artefact grade, not on Zigpipe.

Declaration: **does not affect the verdict**. Key quotation, 9.2: "The declaration is optional."
A reader who says Zigpipe cannot be graded without one has read 9.2 wrongly.

A reader who grades 4.1 Yes on the grounds that Lintomatic "mostly" conforms has read either 4.1
or the detector document's section 8 differently; it counts against this document only if the
reasoning quotes 4.1. A reader who grades 4.1 Yes because they missed the two undocumented rules
has misread the fixture.
