# Run 37: TOOLING-SPEC.md, defined terms, second run

- **Document**: TOOLING-SPEC.md
- **Pull request**: not yet opened; branch `editor/defined-terms` at b1e7145, the commit the
  readers were given. The change is be546ea (Harness renamed Rule harness, Remediation linked, the
  section 3 table's [Remediation docs] cell). The revision after
  [run 33](033-defined-terms-toolchain-run-1.md) is b6e8c2b and b1e7145:
  - section 2 now glosses every borrowed term, with a paragraph after the table on undocumented
    rules;
  - clause 4.2 has sentences on one unresolved identifier and on the forms a lookup may take;
  - clause 4.3 has a new heading;
  - clause 9.1 has sentences on what the artefact grade counts;
  - clause 9.2 has sentences on whom the gap record binds. The question set and key changed only
    in the 4.3 link anchor.
- **Cohort**: five readers, none reused from run 33, model alias `haiku`; every reader reported
  `claude-haiku-5-5` in its JSON output
- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, in a fresh empty directory made by `mktemp -d` outside the
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt is byte for byte the question set, the document and the
  fixture at b1e7145, in that order, each preceded by one `===== FILE: <name> =====` line, and
  that each sheet is the `result` of its reader's JSON output (one turn, `is_error` false)
- **Run within the pull request**: 2
- **Marked by**: a delegated marker that saw neither the drafting nor the review, against
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/toolchain/KEY.md`
  at b1e7145, with the judgements of run 33
- **Verdict**: FAIL on application item 4.3, with misses traceable to the clause's untouched
  body. It also fails on two passages found confusing by two or more readers: one is the clause
  9.2 sentence the revision added, and one is the section 2 sentence directly after the revision's
  new paragraph.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3             | 4.4 | 4.5 | 5.1 | 5.2 | 5.3 | 6.1 | 6.2 | 6.3 | Section 9 | Agent support | Section 8 | Declaration | Q4 passages |
| ------ | ------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --------- | ----------- | ----------- |
| 1      | correct | ok  | ok  | ok  | No  | No  | Partial, miss T | Yes | Yes | No  | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | two         |
| 2      | correct | ok  | ok  | ok  | No  | No  | Yes             | Yes | Yes | No  | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | two         |
| 3      | correct | ok  | ok  | ok  | No  | No  | Yes             | Yes | Yes | No  | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | four        |
| 4      | correct | ok  | ok  | ok  | No  | No  | Partial, miss T | Yes | Yes | No  | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | three       |
| 5      | correct | ok  | ok  | ok  | No  | No  | Yes             | Yes | Yes | No  | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | three       |

`T` marks a miss whose reasoning quotes or states what the document requires. Every 5.1 grade of
No counts the two `(none)` routes, and every 6.2 grade of No mentions the generic-justification
requirement.

### Question 1

Five of five correct, each with at least four bullets the key lists. None says the toolchain must
be a single product, that a declaration is required, or that the agent summary is a MUST. Readers
2, 3, 4 and 5 say section 7 is SHOULD-level.

### Question 2

All five readers get 2a, 2b and 2c, each quoting the key's sentences or section 1's "A
[Toolchain] is measured at the project level". Readers 1 and 2 quote only that sentence for 2a and
state "whatever the project assembles" in their own words (run 33's judgement J1).

### Question 3

- **4.2**, five of five No, against three of five in run 33. Readers 1, 2 and 5 quote or restate
  the new "One [Identifier] that does not resolve fails this clause, however many others do".
- **4.3**, three of five (readers 2, 3 and 5, Yes). Readers 1 and 4 grade Partial for the same
  reason: the fixture names only the inline route, and the clause reaches every route that
  bypasses the record. Reader 1 says the fixture "does not establish that no other route, such as
  a baseline or a rule disabled in config, bypasses the record". Reader 4 says "this MUST covers
  every route". Each reasoning states what the clause requires, so each is traceable (run 33's
  J2). The miss traces to the clause body's "every such route in every [Detector] the
  [Toolchain] routes a [Defence] through", which neither the change nor the revision touched. The
  revision rewrote only the 4.3 heading, and no reader this run quotes the heading or puts it
  against the body. Readers 2, 3 and 5 note the same silence on baselines and grade Yes "on the
  description".
- **Section 9**, **agent support**, **section 8** and **declaration**: five of five give the key's
  answers. None applies section 8 to Zigpipe.

### Judgements made in marking

Run 33's judgements J1 to J4 are applied unchanged. Under J4 (the same passage is the same
sentence), clause 9.1 is two single-reader notes: reader 2 quotes its MUST sentence and reader 5
its first sentence. Read by paragraph, they would be one passage named by two readers and would
also block, in a paragraph the revision added two sentences to. The verdict is FAIL either way.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                | Clause | Readers        | Text                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "The gap record above is part of it: the duty to record a gap there binds a project or artefact that declares a version, and one that declares none makes no claim for a gap record to qualify."                       | 9.2    | three: 1, 4, 5 | Added by the revision                                                                                                                                      |
| "These are additional."                                                                                                                                                                                                | 2      | two: 3, 4      | Untouched base sentence. The revision put its new paragraph directly before it and changed the table's lead-in to say the table covers every borrowed term |
| "A project or artefact that has learnt that it fails a MUST of the document it declares against MUST record that gap alongside the version", set against the added 9.2 sentence                                        | 9.2    | one: 5         | Untouched base, quoted together with the added sentence above                                                                                              |
| "The two verdicts MUST be graded and declared separately, and neither implies the other.", set against 9.2's "The declaration is optional."                                                                            | 9.1    | one: 2         | Untouched base, in the paragraph the revision added to                                                                                                     |
| "As a project, it ... is graded against this document and section 7 of the method specification on that basis."                                                                                                        | 9.1    | one: 5         | Untouched base, in the paragraph the revision added to                                                                                                     |
| "stop the levels below it from being treated as meaningful, in the order method section 5 states."                                                                                                                     | 4.5    | one: 1         | Untouched base                                                                                                                                             |
| "That document's MUSTs, in brief, are six," set against "every MUST of sections 4 to 7"                                                                                                                                | 4.1    | one: 2         | Untouched base                                                                                                                                             |
| "It is self-contained for grading a [Toolchain]."                                                                                                                                                                      | 1      | one: 3         | Untouched base                                                                                                                                             |
| Point 1's "The [Detector] together with that wrapping is then what the [Practitioner] uses and what is judged." set against point 2's "The [Detector]'s own verdict under that document is unchanged by the wrapping." | 4.1    | one: 3         | Untouched base, point 1 after the sentence the change edited                                                                                               |
| "A [Toolchain] [Conforms] with [Agent] support if it additionally satisfies section 7."                                                                                                                                | 9      | one: 3         | Untouched base                                                                                                                                             |
| "A third-party [Detector]'s native catalogue, which the [Toolchain] orchestrates without claiming as its own, is resolved under that document's clause 6 and is not re-shipped here."                                  | 4.2    | one: 4         | Untouched base; reader 4 sets it against the revision's paragraph after the section 2 table                                                                |
| "meeting its content requirements in full."                                                                                                                                                                            | 5.3    | one: 5         | Untouched base                                                                                                                                             |

Notes on the two blocking passages:

- **9.2, the added sentence.** Readers 1 and 4 could not tell what "qualify" modifies. Reader 5
  sets the sentence's first half against the gap MUST two sentences earlier and reads one as
  unconditional and the other as conditional.
- **Section 2, "These are additional."** Both readers could not tell which entries the sentence
  refers to.

Run 33's other blocking passages are clear in this run:

- clause 4.3's heading set against its body (four readers in run 33);
- the section 2 [Defence] row (three);
- clause 9.1's "nothing else built around it" (two).

No reader quotes the 4.3 heading, the [Defence] row, the paragraph after the table, the new
clause 4.2 sentences or the new clause 9.1 sentences. Only reader 2's 9.1 MUST sentence and
reader 5's 9.1 first sentence are near the new 9.1 sentences. No reader quotes the Rule harness
rows, the [Remediation docs] cell or clause 4.5's [Remediation] link.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: not met. 4.3 three of
  five; every other item five of five.
- A wrong answer traceable to the text, none: not met. 4.3 for readers 1 and 4, tracing to the
  clause's untouched body.
- A passage found confusing by two or more, none outstanding: not met. Clause 9.2's added sentence
  (three readers). Section 2's "These are additional." (two readers), an untouched sentence whose
  surroundings the revision changed.
- From one reader only, recorded: the ten other passages above.

**FAIL.** The 4.3 misses trace to untouched base text. One blocking passage is a sentence the
revision added (9.2). The other is an untouched base sentence directly after the revision's new
paragraph in section 2. None is in text the change made.
