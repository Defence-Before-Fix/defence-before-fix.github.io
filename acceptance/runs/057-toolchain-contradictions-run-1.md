# Run 57: TOOLING-SPEC.md, toolchain contradictions, first run

- **Document**: TOOLING-SPEC.md
- **Pull request**: [25](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25), opened later from branch
  `editor/toolchain-contradictions`. The readers read commit 4d6ebbd. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
- **Run within the pull request**: 1
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `00f3043ad8fef7967b0915398bcfaca27d646f8112b0b6df4f9d7d75065eda60`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at 4d6ebbd, each after one
  `===== FILE: <name> =====` line; the marker rebuilt it from that commit and the hash matched.
- **Readers set aside**: none. Every reader's output has `is_error` false, subtype `success`,
  non-empty answer text and the cohort's model.
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  marking instruction and its agent definition, having seen neither the drafting nor the review.
- **Process change**: the run was made under the acceptance process change of pull request 22
  before it merged, following all of it at commit c31d49a, named before the readers started.
- **Verdict**: FAIL

## Marks

Readers are numbered 1 to 5 as their sheets are. Question 3 columns: the eleven clauses, then
the four answers (S9 conformance under section 9, AS agent support, S8 whether section 8
applies, Decl whether the absence of a declaration affects the verdict).

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3          | 4.4 | 4.5 | 5.1 | 5.2 | 5.3 | 6.1 | 6.2 | 6.3 | S9  | AS  | S8  | Decl |
| ------ | ------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
| 1      | correct | ok  | ok  | ok  | ok  | ok  | miss (Part.) | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |
| 2      | correct | ok  | ok  | ok  | ok  | ok  | miss (Part.) | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |
| 3      | correct | ok  | ok  | ok  | ok  | ok  | ok           | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |
| 4      | correct | ok  | ok  | ok  | ok  | ok  | ok           | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |
| 5      | correct | ok  | ok  | ok  | ok  | ok  | ok           | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |

Grades given, for the items the key accepts more than one: 5.1 Partial (1, 2, 5), No (3, 4);
6.1 Yes (1, 4, 5), Partial (2, 3), both Partials mentioning that no place is given for
calibrations or conventions; 6.2 No (all five), each mentioning that nothing rejects a generic
justification.

Question 1: correct bullets per reader 4, 5, 5, 5 and 5 (reader 1: 4.1, 4.2, 4.3 with 4.4 and
4.5, sections 5 and 6). No bullet asserts anything the key marks wrong.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote the section 1 sentence "It is whatever the project assembles to run its
checks through", which states element (2).

### Misses

- **Reader 1, 4.3, Partial.** The inline `// lintomatic-ignore` route is disabled, but "the
  fixture is silent on any other route, such as a baseline, so 'every route' is not shown". The
  reasoning does not quote the document (its only quotation is two words).
- **Reader 2, 4.3, Partial.** The inline route is disabled and exceptions go to the record, but
  the fixture does not say whether Lintomatic has a baseline or another route, "and the clause
  covers every route. I cannot confirm the list is complete." The reasoning does not quote the
  document.

The key accepts Yes only for 4.3 and names no wrong reading for it, so neither miss counts
against the document on its own; two misses on one item fail the threshold for questions 1 and
3\. Readers 3, 4 and 5 also noted the fixture's silence on baselines and graded Yes on what is
written. No miss matches a wrong reading the key names.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..4d6ebbd adds,
rewords or deletes a sentence in the paragraph.

| #   | Passage (clause, words or description)                                                                                                                                                                       | Readers       | Changed by the diff |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ------------------- |
| 1   | Section 2 terminology table, [Defence] row: "A [Rule] with its documentation, in force and [Blocking]", set against clause 4.2's first paragraph                                                             | 1, 2, 3, 5    | no                  |
| 2   | Clause 4.2, first paragraph: "A [Blocking] [Rule] whose documentation is missing ... graded here as a [Defence] with a gap" (1, 2, 3, 5); "covers every [Identifier] the project can see" (4)                | 1, 2, 3, 4, 5 | yes                 |
| 3   | Clause 4.2, second paragraph: "A third-party [Detector]'s native catalogue ... is resolved under that document's clause 6 and is not re-shipped here", set against the first paragraph                       | 3, 4          | no                  |
| 4   | Section 1, "How to read this document": "It is self-contained for grading a [Toolchain]" (2, set against clause 4.1's "every one of"); "The table in section 2 glosses every term it borrows" (3)            | 2, 3          | no                  |
| 5   | Clause 9.1, first paragraph: "as it stands when installed into a [Consuming project] with nothing else built around it" (1); "is graded against this document and section 7 of the method specification" (5) | 1, 5          | no                  |
| 6   | Section 9, second paragraph: "A [Toolchain] [Conforms] with [Agent] support if it additionally satisfies section 7", section 7 being all SHOULDs                                                             | 3, 5          | no                  |
| 7   | Clause 4.1, first paragraph: requires "every one of" the detector specification's MUSTs in its sections 4 to 7                                                                                               | 2             | yes                 |
| 8   | Section 9, first paragraph: "assembled parts, wherever each part came from"                                                                                                                                  | 1             | yes                 |
| 9   | Clause 4.1, point 1: "is then what the [Practitioner] uses and what is judged"                                                                                                                               | 1             | no                  |
| 10  | Section 2 terminology, [Bundled defence] entry: "with its documentation, [Blocking], and routed through the [Toolchain]'s own entry point"                                                                   | 4             | no                  |
| 11  | Clause 8.1, first paragraph: "a [Bundled defence] whose documentation is missing is still a [Bundled defence] for this clause"                                                                               | 4             | yes                 |
| 12  | Section 3 table, [Identifier] resolution row, routing [Bundled rules] to the detector specification                                                                                                          | 3             | no                  |
| 13  | Clause 4.3, first paragraph: "MUST disable every [Suppression] route ... or MUST run a [Blocking] [Defence] that fails on its use"                                                                           | 3             | no                  |
| 14  | Clause 4.3, second paragraph: "This clause is where the project's decision is made and enforced, and the decision is no."                                                                                    | 3             | no                  |

## Findings and where they lie

- **Finding A, passage 2, clause 4.2 first paragraph** (five readers): text the change wrote.
  Blocks.
- **Finding B, passage 1, section 2 [Defence] row** (four readers): every reader naming it sets
  it against clause 4.2's first paragraph, which the change altered. Blocks.
- **Finding C, passage 3, clause 4.2 second paragraph** (readers 3 and 4): both set it against
  clause 4.2's first paragraph, which the change altered. Blocks.
- **Finding D, passage 4, section 1 "How to read this document"** (readers 2 and 3): reader 2
  sets it against clause 4.1's first paragraph, which the change altered. Blocks.
- **Finding E, passage 5, clause 9.1 first paragraph** (readers 1 and 5): reader 1 sets it
  against section 9's first paragraph, which the change altered. Blocks.
- **Finding F, passage 6, section 9 second paragraph** (readers 3 and 5): neither reader sets it
  against a paragraph the change altered; both set it against section 7, which is unchanged.
  Routed to `acceptance/ROUTED.md`; does not block.

Passages 7 to 14 are each named by one reader: recorded, not findings.

## Points the rules did not settle

1. **Reader 5, clause 9.1.** The reader quotes "is graded against this document and section 7 of
   the method specification" and says it could not resolve the reference because it had only
   this document. That is close to the example of a remark that is not about a passage (another
   document not supplied), but it quotes the document and names its clause. Marked by the
   open-point rule: an open point on whether a reader named a passage counts the passage. It
   therefore counts, and with reader 1 makes finding E.
2. **Question 1 bullets that state how conformance is measured rather than what the toolchain
   must do**: reader 1's first and sixth ("judged on the whole toolchain"; "one project-level
   grade"), reader 2's first, reader 4's first sentence ("a single conformance grade"), reader
   5's first and reader 3's sixth ("Self-audit (8) and the two-grade split (9.1) apply only to a
   toolchain that a project ships"). They are on neither of the key's lists. Marked by the rule
   for a bullet on neither list: not counted either way. Every reader has four or more correct
   bullets without them, so no mark turns on it. For the key to settle.
3. **Section 7 described as "all SHOULDs"** (readers 3 and 5) is a description of a whole
   section, which identifies no sentence or paragraph, so under the definition of naming it is
   not a passage of its own; it is the reason both readers give for naming section 9's second
   paragraph (passage 6). Had it counted, it would be a passage the change did not touch and
   would be routed, not block.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item except
  4.3, which is three of five. Not met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: five (findings A
  to E). Not met.
- Passages named by two or more readers elsewhere: one (finding F), routed to
  `acceptance/ROUTED.md`.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125956319); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125955854); [the prompt](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125956709).
