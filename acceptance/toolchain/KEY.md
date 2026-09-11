# Answer key for TOOLING-SPEC.md

Marked against the document at the version named in the changelog entry that records the run.
Quotations below are from the document; when a clause is reworded, update the quotation here in
the same commit.

## 1. Restatement

A bullet is correct when it names one of these obligations. Four or more correct bullets, and no
bullet asserting an obligation the document does not state, is a correct restatement.

- Route defences only through detectors that conform to the detector specification, wrapping
  permitted ([4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification)).
- Resolve every identifier a routed defence can print, including the project's own, offline,
  to documentation stating the correct construction ([4.2](../../TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-it-routes-can-print-from-the-installed-copy-without-network-access)).
- Forbid, by disabling or by a blocking defence, every suppression route that bypasses the
  project record ([4.3](../../TOOLING-SPEC.md#43-the-toolchain-must-forbid-through-a-defence-of-its-own-every-suppression-route-that-bypasses-the-project-record)).
- The toolchain's own entry point meets the detector reporting clauses and prints identifiers
  unaltered ([4.4](../../TOOLING-SPEC.md#44-the-toolchains-own-invocation-must-satisfy-the-detector-specifications-reporting-clauses-for-every-defence-it-routes)), and runs detectors before runners, stopping on a detector failure ([4.5](../../TOOLING-SPEC.md#45-the-toolchains-entry-point-must-run-detectors-before-runners-and-must-stop-on-a-detector-failure)).
- List the active defences, derived from configuration, including the project's own ([5.1](../../TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) to
  [5.3](../../TOOLING-SPEC.md#53-a-projects-own-defences-must-appear-in-the-listing-alongside-bundled-ones)).
- Define and read a project record whose exceptions each carry a justification, enumerable the
  same way as the defences ([6.1](../../TOOLING-SPEC.md#61-the-toolchain-must-define-a-location-for-the-project-record-and-must-read-it-itself) to [6.3](../../TOOLING-SPEC.md#63-the-project-record-must-be-enumerable-by-the-same-means-as-the-defences)).
- A shipped toolchain also fails its release on undocumented bundled defences and runs its own
  defences on its own source ([8.1](../../TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation), [8.2](../../TOOLING-SPEC.md#82-a-shipped-toolchain-must-run-its-own-bundled-defences-on-its-own-source)).

Wrong if it asserts: the toolchain must be a single product; a declaration is required to
conform; the agent summary (section [7](../../TOOLING-SPEC.md#7-agent-context)) is a MUST.

## 2. Load-bearing statements

- **2a.** At the project level; the toolchain is whatever the project has assembled from
  third-party, first-party and project-level parts. Key quotation, section [9](../../TOOLING-SPEC.md#9-conformance): "A project's
  Toolchain Conforms if every MUST in sections [4](../../TOOLING-SPEC.md#4-the-detectors-a-toolchain-routes-defences-through) to [6](../../TOOLING-SPEC.md#6-the-project-record) holds across the assembled parts, wherever
  each part came from". An answer that says conformance is graded per tool, or that only a
  packaged product can conform, is wrong.
- **2b.** One grade; which part satisfied each clause is evidence, not a grade of its own. Key
  quotation, section [9](../../TOOLING-SPEC.md#9-conformance): "The project-level verdict is a single grade; which part of the Toolchain
  satisfied each clause is evidence for that grade, not a second grade."
- **2c.** Two, graded and declared separately, and neither implies the other. Key quotation,
  [9.1](../../TOOLING-SPEC.md#91-a-project-that-ships-a-detector-or-a-toolchain-has-two-levels-of-conformance-graded-separately): "The two verdicts MUST be graded and declared separately, and neither implies the other."
  An answer giving one grade, or saying the artefact grade follows from the project grade, is
  wrong.

## 3. Application: the Zigpipe project

| Clause                                                                                                                                                                                   | Intended verdict   | Reasoning the fixture supports                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification)                                                         | No                 | Lintomatic fails detector [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together) on two undocumented bundled rules and nothing in the wrapping closes that gap                                                                                                                                                                                            |
| [4.2](../../TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-it-routes-can-print-from-the-installed-copy-without-network-access)                                 | No                 | `zq.*` and `proj.*` resolve offline, but the two enabled bundled rules resolve to `(none)`                                                                                                                                                                                                                                                                                                                              |
| [4.3](../../TOOLING-SPEC.md#43-the-toolchain-must-forbid-through-a-defence-of-its-own-every-suppression-route-that-bypasses-the-project-record)                                          | Yes                | Ignore comments disabled project-wide; exceptions only through the record the toolchain reads                                                                                                                                                                                                                                                                                                                           |
| [4.4](../../TOOLING-SPEC.md#44-the-toolchains-own-invocation-must-satisfy-the-detector-specifications-reporting-clauses-for-every-defence-it-routes)                                     | Yes                | `zig-qa run` is local, prints Lintomatic's output unchanged, one line per finding                                                                                                                                                                                                                                                                                                                                       |
| [4.5](../../TOOLING-SPEC.md#45-the-toolchains-entry-point-must-run-detectors-before-runners-and-must-stop-on-a-detector-failure)                                                         | Yes                | Lintomatic, then the tests, stopping on a Lintomatic failure                                                                                                                                                                                                                                                                                                                                                            |
| [5.1](../../TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them)                                                              | Yes, Partial or No | `zig-qa list` prints identifier, summary and documentation path without running the rules; Partial or No is accepted where the reasoning counts the two `(none)` routes, since 5.1 says the listing MUST provide the route and [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) point 2 says a gap may be named again by a later clause |
| [5.2](../../TOOLING-SPEC.md#52-the-listing-must-be-derived-from-the-active-configuration)                                                                                                | Yes                | Derived from `lintomatic.toml`, not hand-maintained                                                                                                                                                                                                                                                                                                                                                                     |
| [5.3](../../TOOLING-SPEC.md#53-a-projects-own-defences-must-appear-in-the-listing-alongside-bundled-ones)                                                                                | Yes                | The `proj.*` rules appear in the same listing                                                                                                                                                                                                                                                                                                                                                                           |
| [6.1](../../TOOLING-SPEC.md#61-the-toolchain-must-define-a-location-for-the-project-record-and-must-read-it-itself)                                                                      | Yes                | `quality-exceptions.toml` is a defined path that `zig-qa run` loads                                                                                                                                                                                                                                                                                                                                                     |
| [6.2](../../TOOLING-SPEC.md#62-every-exception-in-the-project-record-must-carry-a-written-justification-that-names-the-hazard-and-the-scope-and-the-toolchain-must-reject-a-generic-one) | Partial or No      | A justification is required and an empty one rejected, but nothing rejects a justification that could be pasted onto any entry                                                                                                                                                                                                                                                                                          |
| [6.3](../../TOOLING-SPEC.md#63-the-project-record-must-be-enumerable-by-the-same-means-as-the-defences)                                                                                  | Yes                | `zig-qa list --exceptions` uses the same format and operation as the rule listing                                                                                                                                                                                                                                                                                                                                       |

Either Partial or No is accepted for [6.2](../../TOOLING-SPEC.md#62-every-exception-in-the-project-record-must-carry-a-written-justification-that-names-the-hazard-and-the-scope-and-the-toolchain-must-reject-a-generic-one); the reasoning must mention the generic-justification
requirement. A Yes on [6.2](../../TOOLING-SPEC.md#62-every-exception-in-the-project-record-must-carry-a-written-justification-that-names-the-hazard-and-the-scope-and-the-toolchain-must-reject-a-generic-one) with reasoning that quotes only the first sentence of the clause is a
finding against the document.

Section [9](../../TOOLING-SPEC.md#9-conformance) verdict: **does not conform**, because [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) and [4.2](../../TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-it-routes-can-print-from-the-installed-copy-without-network-access) fail; partial conformance MUST NOT be
described as conformance. **Not with agent support**, because section [7](../../TOOLING-SPEC.md#7-agent-context) is not met (no summary).
**Section [8](../../TOOLING-SPEC.md#8-self-audit) does not apply**, because Zigpipe ships nothing to other projects; a reader who applies
[8.1](../../TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation) to Zigpipe on the basis that Zigpipe's tooling includes a shipped package (zig-qa) has read
section [8](../../TOOLING-SPEC.md#8-self-audit)'s shipped-toolchain clauses as reaching the consuming project, and that counts against the document. The
correct reading is that section [8](../../TOOLING-SPEC.md#8-self-audit) bears on zig-qa's own artefact grade, not on Zigpipe.

Declaration: **does not affect the verdict**. Key quotation, [9.2](../../TOOLING-SPEC.md#92-the-declaration-is-the-claim-and-the-known-gap-record-not-a-condition-of-conformance): "The declaration is optional."
A reader who says Zigpipe cannot be graded without one has read [9.2](../../TOOLING-SPEC.md#92-the-declaration-is-the-claim-and-the-known-gap-record-not-a-condition-of-conformance) wrongly.

A reader who grades [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) Yes on the grounds that Lintomatic "mostly" conforms has read either [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification)
or the detector document's section [8](../../DETECTOR-SPEC.md#8-conformance) differently; it counts against this document only if the
reasoning quotes [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification). A reader who grades [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) Yes because they missed the two undocumented rules
has misread the fixture.

## 4. Confusion

No keyed answer. Record every passage quoted. Two or more readers quoting the same passage is a
finding that blocks until the text is changed and a fresh cohort no longer quotes it. What to
change is the editor's decision; the reader is not asked and any suggestion it volunteers is
discarded unread.
