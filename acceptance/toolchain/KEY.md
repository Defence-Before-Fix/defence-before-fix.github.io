# Answer key for TOOLING-SPEC.md

Marked against the document at the commit the readers read, with this key, its question set and
fixture at that same commit. Quotations below are from the document; when a clause is reworded,
update the quotation here in the same commit. `ACCEPTANCE.md` says how each item is marked;
`acceptance/README.md` says what each part of this key is for.

## 1. Restatement

A bullet is correct when it names one of these obligations. Four or more correct bullets, with
no bullet making an assertion listed below as wrong, is a correct restatement.

- Route defences only through detectors that conform to the detector specification, wrapping
  permitted ([4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification)).
- Resolve every identifier a routed defence can print, including the project's own, offline,
  to documentation stating the correct construction ([4.2](../../TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-or-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access)).
- Forbid, by disabling or by a blocking defence, every suppression route that bypasses the
  project record ([4.3](../../TOOLING-SPEC.md#43-the-toolchain-must-forbid-every-suppression-route-that-bypasses-the-project-record-by-disabling-it-or-by-a-defence-of-its-own)).
- The toolchain's own entry point meets the detector reporting clauses and prints identifiers
  unaltered ([4.4](../../TOOLING-SPEC.md#44-the-toolchains-own-invocation-must-satisfy-the-detector-specifications-reporting-clauses-for-every-defence-it-routes)), and runs detectors before runners, stopping on a detector failure ([4.5](../../TOOLING-SPEC.md#45-the-toolchains-entry-point-must-run-detectors-before-runners-and-must-stop-on-a-detector-failure)).
- List the active defences, derived from configuration, including the project's own ([5.1](../../TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) to
  [5.3](../../TOOLING-SPEC.md#53-a-projects-own-defences-must-appear-in-the-listing-alongside-bundled-ones)).
- Define and read a project record whose exceptions each carry a justification, enumerable the
  same way as the defences ([6.1](../../TOOLING-SPEC.md#61-the-toolchain-must-define-a-location-for-the-project-record-and-must-read-it-itself) to [6.3](../../TOOLING-SPEC.md#63-the-project-record-must-be-enumerable-by-the-same-means-as-the-defences)).
- A shipped toolchain also fails its release on undocumented bundled defences and runs its own
  defences on its own source ([8.1](../../TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation), [8.2](../../TOOLING-SPEC.md#82-a-shipped-toolchain-must-run-its-own-bundled-defences-on-its-own-source)).
- Make everything the method requires of a practitioner possible without the project building
  the mechanism first (section [1](../../TOOLING-SPEC.md#1-what-this-document-is-for), the governing principle).
- Not describe partial conformance as conformance (section [9](../../TOOLING-SPEC.md#9-conformance)).

Wrong if it asserts: the toolchain must be a single product; a declaration is required to
conform; the agent summary (section [7](../../TOOLING-SPEC.md#7-agent-context)) is a MUST. A bullet that calls agent support or the
self-audit a further condition "where it applies", says that section [7](../../TOOLING-SPEC.md#7-agent-context) is recommended or a
SHOULD, or says a declaration is not a condition, asserts no obligation and is neither correct
nor wrong. So is a bullet that states how
conformance is measured rather than what is required: the toolchain judged as one assembled
whole at the project level (sections [1](../../TOOLING-SPEC.md#1-what-this-document-is-for) and [9](../../TOOLING-SPEC.md#9-conformance)), the project-level verdict a single grade
(section [9](../../TOOLING-SPEC.md#9-conformance)), or a shipped artefact graded separately ([9.1](../../TOOLING-SPEC.md#91-a-project-that-ships-a-detector-or-a-toolchain-has-two-levels-of-conformance-graded-separately)).

Wrong readings the text invites, which count against the document on one reader: none named.

## 2. Load-bearing statements

- **2a.** Required: (1) at the project level; (2) the toolchain is whatever the project has
  assembled to run its checks through, from third-party, first-party and project-level parts.
  Wrong if it says conformance is graded per tool, or that only a packaged product can conform.
  Key quotation, section [9](../../TOOLING-SPEC.md#9-conformance): "A project's Toolchain Conforms if every MUST in sections [4](../../TOOLING-SPEC.md#4-the-detectors-a-toolchain-routes-defences-through) to [6](../../TOOLING-SPEC.md#6-the-project-record)
  holds across the assembled parts, wherever each part came from". An answer that says everything the
  project runs its checks through, or the assembled parts from wherever they came, or that lists
  the three kinds of part, states element (2).
- **2b.** Required: (1) one grade; (2) which part satisfied each clause is evidence for that
  grade, not a grade of its own. Wrong if it gives a grade per part. Key quotation, section [9](../../TOOLING-SPEC.md#9-conformance):
  "The project-level verdict is a single grade; which part of the Toolchain satisfied each
  clause is evidence for that grade, not a second grade."
- **2c.** Required: (1) two; (2) neither implies the other. Wrong if it gives one grade, or says
  the artefact grade follows from the project grade or the reverse. That the two are graded and
  declared separately is explanation; an answer that says it has stated element (1). Key quotation, [9.1](../../TOOLING-SPEC.md#91-a-project-that-ships-a-detector-or-a-toolchain-has-two-levels-of-conformance-graded-separately): "The two verdicts MUST be graded and declared separately, and
  neither implies the other."

## 3. Application: the Zigpipe project

| Clause                                                                                                                                                                                   | Accepted grades    | Condition on the reasoning                                                                                                      | What the fixture supports                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification)                                                         | No                 | None                                                                                                                            | Lintomatic fails detector [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together) on two undocumented bundled rules and nothing in the wrapping closes that gap; a reader who notes that the detector specification was not supplied and grades from this document's summary of it is correct                                                                                                                                                                          |
| [4.2](../../TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-or-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access)              | No                 | None. A No given on the condition that the two bundled rules are blocking is a No: their firing stops `zig-qa run`, so they are | `zq.*` and `proj.*` resolve offline, but the two enabled bundled rules resolve to `(none)`                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [4.3](../../TOOLING-SPEC.md#43-the-toolchain-must-forbid-every-suppression-route-that-bypasses-the-project-record-by-disabling-it-or-by-a-defence-of-its-own)                            | Yes                | None                                                                                                                            | Ignore comments disabled project-wide; exceptions only through the record the toolchain reads                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [4.4](../../TOOLING-SPEC.md#44-the-toolchains-own-invocation-must-satisfy-the-detector-specifications-reporting-clauses-for-every-defence-it-routes)                                     | Yes                | None                                                                                                                            | `zig-qa run` is local, prints Lintomatic's output unchanged, one line per finding                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [4.5](../../TOOLING-SPEC.md#45-the-toolchains-entry-point-must-run-detectors-before-runners-and-must-stop-on-a-detector-failure)                                                         | Yes                | None                                                                                                                            | Lintomatic, then the tests, stopping on a Lintomatic failure                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [5.1](../../TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them)                                                              | Yes, Partial or No | None                                                                                                                            | `zig-qa list` prints identifier, summary and documentation path without running the rules; Partial or No is the reading that counts the two `(none)` routes, since [5.1](../../TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) says the listing MUST provide the route and [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) point 2 says a gap may be named again by a later clause |
| [5.2](../../TOOLING-SPEC.md#52-the-listing-must-be-derived-from-the-active-configuration)                                                                                                | Yes                | None                                                                                                                            | Derived from `lintomatic.toml`, not hand-maintained                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [5.3](../../TOOLING-SPEC.md#53-a-projects-own-defences-must-appear-in-the-listing-alongside-bundled-ones)                                                                                | Yes                | None                                                                                                                            | The `proj.*` rules appear in the same listing                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [6.1](../../TOOLING-SPEC.md#61-the-toolchain-must-define-a-location-for-the-project-record-and-must-read-it-itself)                                                                      | Yes or Partial     | For Partial: mentions that the fixture names a place for exceptions and none for calibrations or conventions                    | `quality-exceptions.toml` is a defined path that `zig-qa run` loads; the project record entry also covers calibrations and conventions                                                                                                                                                                                                                                                                                                                                                                                              |
| [6.2](../../TOOLING-SPEC.md#62-every-exception-in-the-project-record-must-carry-a-written-justification-that-names-the-hazard-and-the-scope-and-the-toolchain-must-reject-a-generic-one) | Partial or No      | Mentions that nothing rejects a generic justification, one that could be pasted onto any entry                                  | A justification is required and an empty one rejected                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [6.3](../../TOOLING-SPEC.md#63-the-project-record-must-be-enumerable-by-the-same-means-as-the-defences)                                                                                  | Yes                | None                                                                                                                            | `zig-qa list --exceptions` uses the same format and operation as the rule listing                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

The four answers the question then asks for, each with the condition its reason must meet:

- **Conformance under section [9](../../TOOLING-SPEC.md#9-conformance).** Accepted answer: does not conform. Condition: the reason
  names [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification), [4.2](../../TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-or-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access) or [6.2](../../TOOLING-SPEC.md#62-every-exception-in-the-project-record-must-carry-a-written-justification-that-names-the-hazard-and-the-scope-and-the-toolchain-must-reject-a-generic-one) among the failing clauses, or points to the grades the reader gave above, as "the
  clauses graded No", where those grades have one of the three at No or Partial; other clauses
  named alongside are not marked.
- **Conformance with agent support.** Accepted answer: no. Condition: the reason says that
  section [7](../../TOOLING-SPEC.md#7-agent-context) is not met, or that there is no summary, or that the toolchain does not conform
  under section [9](../../TOOLING-SPEC.md#9-conformance) at all.
- **Whether section [8](../../TOOLING-SPEC.md#8-self-audit) applies.** Accepted answer: it does not. Condition: the reason says that
  Zigpipe ships nothing to other projects, or that section [8](../../TOOLING-SPEC.md#8-self-audit) bears on zig-qa's own artefact
  grade and not on Zigpipe.
- **Whether the absence of a declaration affects the verdict.** Accepted answer: it does not.
  Condition: the reason says that the declaration is optional, or not a condition of
  conformance, or that a verdict rests on the evidence. Key quotation, [9.2](../../TOOLING-SPEC.md#92-the-declaration-is-the-claim-and-the-known-gap-record-not-a-condition-of-conformance): "The declaration is
  optional."

Wrong readings the text invites, which count against the document on one reader:

- [6.2](../../TOOLING-SPEC.md#62-every-exception-in-the-project-record-must-carry-a-written-justification-that-names-the-hazard-and-the-scope-and-the-toolchain-must-reject-a-generic-one) graded Yes with reasoning that says a justification is required or an empty one rejected
  and does not mention a generic justification, which has not read the sentence on one.
- Section [8](../../TOOLING-SPEC.md#8-self-audit) said to apply to Zigpipe with reasoning that says its tooling includes a shipped
  package, which has read "where the project also ships a Detector or a Toolchain" (section [9](../../TOOLING-SPEC.md#9-conformance))
  as reaching the consuming project.
- [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) graded Yes with reasoning that says Lintomatic mostly or largely conforms and quotes [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification),
  which has read it as admitting a proportion.
- The declaration said to affect the verdict, with reasoning that Zigpipe cannot be graded without
  one, which has read [9.2](../../TOOLING-SPEC.md#92-the-declaration-is-the-claim-and-the-known-gap-record-not-a-condition-of-conformance) as a condition.

A reader who grades [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) Yes because they missed the two undocumented rules has misread the
fixture, which is the reader's miss.

## 4. Confusion

No keyed answer. Record every passage named, as `ACCEPTANCE.md` defines naming and the same
passage. A passage named by two or more readers of the run is a finding: it blocks the change
where it lies in text the change wrote or altered, and is routed to `acceptance/ROUTED.md`
otherwise. What to change is the editor's decision; the reader is not asked and any suggestion
it volunteers is discarded unread.
