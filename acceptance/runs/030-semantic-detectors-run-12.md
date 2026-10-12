# Run 30: DETECTOR-SPEC.md, semantic detectors, twelfth run in pull request 14

- **Document**: DETECTOR-SPEC.md
- **Pull request**: [14](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14),
  editor's branch `editor/semantic-detectors` at db47301; the question set, key and fixture read
  at the same commit
- **Cohort**: five readers, model alias `haiku`; every reader reported `claude-haiku-5-5`, as the
  editor supplied in the cohort's model list and as each reader's own JSON output shows
- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, which only reattaches the session's credential and passes
  arguments through verbatim, in a fresh empty directory made by `mktemp -d` outside any
  repository, with the packet on standard input, with no tools, no settings, no project context
  and no saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt is byte for byte the question set, the document and the
  fixture at db47301, in that order, each preceded by one `===== FILE: <name> =====` line, with the
  files separated by one blank line and nothing else added, the same form as the packets of runs
  22, 24, 26 and 28
- **Managed (policy) settings**: none; the machine applies no managed settings and no managed
  settings file is present, as the editor supplied
- **The rest of the isolation**: attested by the editor
- **Readers set aside**: none. The editor reports none set aside for a cause the sheets cannot
  show; every sheet has answer text, no process reports an error (`is_error` false, subtype
  `success`), and every reported model is the cohort's model
- **Run within the pull request**: 12, counting void runs; run 29, made at the same time, does not
  bear on this document
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) dispatched with
  the editor's instruction and its agent definition, `.claude/agents/dbf-spec-editor.md`, having
  seen neither the drafting nor the review

## Marks

| Reader | Q1      | 2a  | 2b   | 2c   | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | Section 8 | Kind       | 6.4 | Q4 entries |
| ------ | ------- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ---------- |
| 1      | correct | ok  | miss | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 1          |
| 2      | miss    | ok  | miss | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 1          |
| 3      | correct | ok  | miss | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 1          |
| 4      | correct | ok  | miss | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 4          |
| 5      | correct | ok  | miss | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 2          |

"Q4 entries" counts the entries each reader lists under question 4; the words each quotes are in
the table of passages below. Every miss under question 2 is traceable to the text: each answer's
sentence states what the document requires, and each quotes the document in support. The miss
under question 1 is the reader's own: the bullet it turns on quotes nothing. No question was left
unanswered.

### Question 1

Every restatement names four or more obligations from the key's list. Readers 1, 3, 4 and 5 assert
no obligation the document does not state: correct. Reader 1's sixth bullet and reader 5's sixth
name the duty to name the kind on a verdict, which the key marks correct; reader 3's sixth and
reader 5's sixth also say what conformance means, which names no obligation and asserts none the
document does not state. Readers 1, 3 and 5 say a printed identifier must resolve to its
documentation, in the generality of 6.1's heading, as run 28 held (judgement 4). Readers 1, 2, 3, 4
and 5 say that each rule carries, needs or has a stable identifier (judgement 3). Reader 3's "put
the results in the output of the command the user ran" and reader 5's "findings must appear in the
output of the command the practitioner ran" are plain plurals, as run 26 held. Reader 2's fifth
bullet says "Each finding, with its location and identifier, must appear in the output of the
command the practitioner ran (5.3)"; 5.3 says "The summary need not list every finding", so the
bullet asserts an obligation the document does not state: incorrect (judgement 2). Correct, four of
five.

### Question 2

The key's answers state these elements:

- 2a: (a) Conformance is satisfying every MUST in sections 4 to 7; (b) judged on evidence; (c) a
  detector that predates the document can conform; (d) the declaration is optional.
- 2b: (a) make the route disableable by configuration, or (b) detectable by a Rule the project can
  write or a mechanical check the Detector documents; (c) the detector is not required to remove or
  forbid it.
- 2c: (a) with the rule; (b) in the installed copy; (c) at a version tracked together; (d) yes,
  reachable offline.

Each answer is read as its sentence and its quotation together, for the gist of each element.

| Reader | 2a                                                                                                | 2b                                                                                                                  | 2c                                                                           |
| ------ | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 1      | ok: all four; (b) and (d) from the 8.1 quotation                                                  | miss: (c) not stated (judgement 5); (b) by the defined term (judgement 6)                                           | ok: all four; (a) and (c) from the 6.3 quotation                             |
| 2      | ok: all four; (b) and (d) from the 8.1 quotation                                                  | miss: (c) not stated (judgement 5); (b) by the defined term (judgement 6); its quotation drops a word (judgement 8) | miss: (c) not stated; only 6.2 quoted (judgement 9)                          |
| 3      | ok: all four; (b) and (d) from the section 8 quotation                                            | miss: (c) not stated (judgement 5); (b) as "make every use of it detectable"                                        | miss: (c) not stated; only 6.2 quoted (judgement 9)                          |
| 4      | ok: all four; (d) as "without a declaration", (b) as "the verdict rests on checking the detector" | miss: (c) not stated (judgement 5); (b) by the defined term (judgement 6)                                           | ok: all four; (a) and (c) from the 6.3 quotation                             |
| 5      | ok: all four; (b) and (d) from the 8.1 quotation                                                  | miss: (c) stated only as "does not have to remove the route" (judgement 7); (b) by the defined term                 | ok: all four; (a) and (c) from the 6.3 quotation, (b) from the 6.2 quotation |

No answer asserts anything the document does not state or that the key says makes an answer
wrong: none says a declaration is required, that partial satisfaction is conformance, that the
detector must forbid the route or require a reason, or that a website will do. Every quotation but
reader 2's under 2b is verbatim apart from letter case, link and emphasis markup and a closing
punctuation mark.

### Question 3

The key's intended verdicts are Yes for every clause but 6.3, which is No; the section 8 verdict
is "does not conform", because 6.3 fails; 6.4 does not change the verdict.

- **Every clause**: all five readers give the intended verdict on every clause, 4.1 to 7.1. On
  6.3 each cites that one unresolved identifier fails the clause, all five quoting 6.3's "One
  [Identifier] that does not resolve fails this clause, however many others do"; no reader grades
  it Partial on the grounds that thirty-eight resolve. Readers 1 to 5 add caveats on 4.2 or 4.3
  about what the fixture does not say, and grade Yes.
- **Section 8**: all five say Lintomatic does not conform, because 6.3 fails.
- **Kind**: all five say the fixture does not let them name the kind and name none, so none is
  marked on it. Readers 2, 3 and 5 call the verdict short of that duty; none makes the verdict turn
  on the kind, and all five say it does not change the verdict or the conformance finding.
- **6.4**: all five say it does not change the verdict, because it is a SHOULD. Reader 3 adds
  that 7.2 is an unmet SHOULD and that a declaration would record the 6.3 gap (judgement 10).

### Judgements made in marking

01. **How an open judgement is made.** As `ACCEPTANCE.md` at 598908b says: as a careful reader of
    the document would, with the reason stated. Where a rule settles a mark, it is applied as
    written.
02. **Question 1, reader 2's "Each finding ... must appear".** Runs 22, 24 and 28 marked incorrect
    bullets saying every finding, or each finding, must appear in the output, because 5.3 says "The
    summary need not list every finding" and "If it leaves any finding out, the output MUST also
    say where the rest can be read". Reader 2's bullet is the same claim about each finding.
    Incorrect. The bullet quotes nothing, so the miss is the reader's. Reader 2 also gives seven
    bullets where the question asks for at most six; the key does not make that wrong, and the mark
    does not turn on it.
03. **Question 1, "each rule carries a stable identifier".** Clause 4.3's heading asks the detector
    to "allow a rule to carry a stable identifier", and its body says "The [Detector] MUST print it,
    unaltered, alongside every finding the [Rule] reports". A detector can print an identifier with
    every finding of every rule only if each rule carries one, and the key's own bullet joins the
    two. A careful reader takes these bullets as 4.3, not as a further obligation. Correct. Read the
    other way, readers 1, 3, 4 and 5 would all miss question 1 and the second criterion would fail
    too; the verdict is FAIL either way.
04. **Question 1, "a printed identifier must resolve".** As run 28 held: the bullets speak at the
    level of 6.1's heading, "The detector MUST provide a mechanism that resolves a printed
    identifier to its documentation", and the key's bullet is in the same words. Correct.
05. **2b (c), not required to remove or forbid, readers 1 to 4.** As runs 22, 24, 26 and 28 held,
    the key's answer includes what the detector need not do, so (c) answers a part of the question.
    Readers 1, 2, 3 and 4 say the detector must do one of the two things, readers 1, 2 and 4 adding
    that one alone is enough. Each quotes 7.1 from "it MUST do at least one of two things" or, in
    reader 2's case, from "but MUST do"; none quotes the words before it, "it need not remove or
    forbid the route", nor the words after "Either alone satisfies this clause", "neither requires
    the [Detector] to remove or forbid the route". That one alone suffices entails that nothing more
    is required, but an element reached only by inference from another is not among the ways
    `ACCEPTANCE.md` names of stating it. Not stated.
06. **2b (b), the means of detection.** Clause 7.1 defines when a route is detectable in its own
    text; readers 1, 2, 4 and 5 use "detectable" in that sense and so state (b), as runs 22 to 28
    held. It decides no mark.
07. **2b (c), reader 5's "It does not have to remove the route."** The element is that the
    detector is not required to remove or forbid the route, and 7.1 says so twice in those words.
    Removing a route and forbidding it are different things: the first takes the route out of the
    detector, the second stops its use whilst it stays; and the answer the key names as wrong is
    that the detector "must forbid the route". Reader 5 states the first half and leaves the second
    open, and its quotation, from "but it MUST do at least one of two things", does not carry it.
    A careful reader does not take half of the element as its gist. Not stated: a miss, traceable,
    since the sentence states what the document requires. Read the other way, reader 5 would be
    correct on 2b and the third criterion would lose one finding; the verdict does not turn on this
    judgement, since 2b fails the first and third criteria by four readers whichever way it is made.
08. **2b, reader 2's quotation.** Reader 2 quotes "but MUST do at least one of two things: ...",
    where the document has "but it MUST do". The words from "MUST do" to "detectable" are a run of
    the document's consecutive words, verbatim; the quotation as given is not, since it drops a
    word. The mark does not turn on it: the answer misses (c) either way, and the miss is traceable
    because its sentence states, in the reader's own words, what 7.1 requires.
09. **2c (c), at a version tracked together, readers 2 and 3.** As run 22 held for a reader whose
    only quotation was 6.2, element (c) answers where the documentation must live, as part of the
    key's answer to that part. Reader 2's sentence says the documentation "must ship with the
    installed rule and be reachable offline", reader 3's that it "must ship with the installed rule,
    and it must be reachable without network access", and each quotes only 6.2. Each states (a),
    (b) and (d); neither says the documentation is versioned with the rule. Not stated: a miss, and
    traceable, since each sentence states what the document requires and each quotes 6.2.
10. **Asides outside the keyed answer.** Reader 3's notes on 7.2 and on what a declaration would
    record, and the remarks of readers 1, 2, 4 and 5 on Lintomatic missing 6.4, are not keyed
    items; each sheet's answer to whether 6.4 changes the verdict is the key's, and is marked so.
11. **Question 4, reader 4's entry on documents not given.** Reader 4 writes "Several terms and
    clauses are defined in documents I was not given, for example" and quotes "Terms from the method
    specification carry over unchanged" and "the toolchain specification's self-audit" in 6.4. The
    entry quotes, and its description names no place in the document: it says what the reader
    lacked, and its quotations are the places it names. A careful reader takes the passages as the
    two quoted, in section 2's first paragraph and in 6.4's Why paragraph. Read the other way, as
    every sentence that uses a term or cites a clause of the other specifications, it would cover
    sentences of nearly every paragraph, among them 6.1's paragraph beginning "For a project's own
    [Rule]", which would then not be cleared; the fourth criterion fails either way, and the
    verdict does not turn on it.
12. **Question 4, closing punctuation.** Reader 4's "... that [Conformance] is judged on." ends with
    a full stop where the document has a colon; reader 5's "... in sections 4 to 7." ends with a
    full stop where the sentence goes on. The words are consecutive and verbatim; the punctuation
    mark that follows them is not a word, so each is a quotation, as runs 26 and 28 held.
13. **Question 4, a passage quoted only to set another against it.** Reader 5 quotes "a declaration
    is optional" as what it read 8.1's sentence on a declaration with no gap beside. As runs 22 and
    28 held, a quotation under question 4 counts whatever it is quoted for. The run occurs only in
    8.1's second paragraph, at the place the reader names, and is recorded there.
14. **The open passages, and paragraphs the change split.** The passages earlier runs of this
    document found confusing by two or more, and not since cleared, are those run 28 left
    outstanding or added: 7.1's first paragraph (runs 20 to 28), section 8's paragraph beginning
    "A verdict on a [Detector] MUST name its kind" (runs 24 to 28), and 6.1's paragraph beginning
    "For a project's own [Rule]" (run 28, two readers). At 1db0c67, which run 28 read, 7.1's first
    paragraph and section 8's paragraph on the kind were each one paragraph; between 1db0c67 and
    db47301 the change split each in two, 7.1 at "A route is detectable when", section 8 at "This
    MUST is on whoever gives the verdict". `ACCEPTANCE.md` asks whether a reader names a sentence of
    the paragraph an earlier passage lay in "as that paragraph reads in the changed document"; a
    careful reader takes a split paragraph to read, in the changed document, as the two paragraphs
    the change made of it, not as the first of them alone. So taken, a sentence of 7.1's second
    paragraph, or of section 8's paragraph beginning "This MUST", covers the open passage. Read the
    other way, the open 7.1 passage would be cleared, but 7.1's second paragraph and section 8's
    paragraph beginning "This MUST" are each named by two or more readers of this cohort, and
    reader 5 names the kept first sentence of section 8's paragraph on the kind, so the fourth
    criterion fails either way. 8.1's first and second paragraphs, 6.1's paragraph beginning "For a
    [Bundled rule]" and clause 4.1 were cleared by runs 22, 24 and 26, and do not reopen when one
    reader of a later cohort names them; 8.1's first paragraph is named by two readers of this
    cohort, which is a new finding of this run, not a reopening.

No re-mark.

## Passages quoted as confusing

Grouped by paragraph, as `ACCEPTANCE.md` defines the same passage. A passage blocks when two or
more readers name it, or when it covers a sentence of a paragraph in which one of the open
passages lay (judgement 14), as that paragraph reads at db47301.

| Clause and paragraph                                                                                                                                                                       | Readers | Words quoted, verbatim                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Blocks                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 7.1, second paragraph, its second and third sentences, "The first is a [Rule] ..." and "That way works only where ..."                                                                     | 1, 2, 4 | 1: "That way works only where the [Detector] lets such a [Rule] see every use of the route" 2: "The first is a [Rule] the project writes for itself, under clause 4.1, and the [Detector] runs. That way works only where the [Detector] lets such a [Rule] see every use of the route, and the [Detector] need not ship the [Rule] itself." 4: "That way works only where the [Detector] lets such a [Rule] see every use of the route, and the [Detector] need not ship the [Rule] itself." | Yes: three readers, and the open 7.1 paragraph of runs 20 to 28 (judgement 14)     |
| 8, the paragraph beginning "This MUST is on whoever gives the verdict", its first sentence; and the paragraph beginning "A verdict on a [Detector] MUST name its kind", its first sentence | 4, 5    | 4: "This MUST is on whoever gives the verdict, not on the [Detector], so it is not one of the MUSTs in sections 4 to 7 that [Conformance] is judged on." 5: "A verdict on a [Detector] MUST name its kind, [Semantic], [Syntactic] or [Textual], in each configuration the verdict grades." and "This MUST is on whoever gives the verdict, not on the [Detector], so it is not one of the MUSTs in sections 4 to 7." (judgement 12)                                                          | Yes: two readers, and the open section 8 paragraph of runs 24 to 28 (judgement 14) |
| 8.1, first paragraph, its third sentence, "A gap is a MUST ...", and its last but one, "A declaration that records no gap claims [Conformance]."                                           | 4, 5    | 4: "A gap is a MUST in sections 4 to 7 that the [Detector] fails." 5: "A declaration that records no gap claims [Conformance]."                                                                                                                                                                                                                                                                                                                                                               | Yes: two readers, in the same paragraph                                            |
| 8.1, second paragraph, its first sentence                                                                                                                                                  | 5       | "a declaration is optional" (judgement 13)                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No; cleared by run 26 (judgement 14)                                               |
| 4.3, first paragraph, the sentence beginning "The [Detector] MUST print it, unaltered"                                                                                                     | 3       | "The [Detector] MUST print it, unaltered, alongside every finding the [Rule] reports, in its default output and in every machine-readable format it offers."                                                                                                                                                                                                                                                                                                                                  | No; one reader of run 26 also named it                                             |
| 2, first paragraph, its first sentence                                                                                                                                                     | 4       | "Terms from the method specification carry over unchanged" (judgement 11)                                                                                                                                                                                                                                                                                                                                                                                                                     | No                                                                                 |
| 6.4, the Why paragraph, its sentence beginning "Where the [Detector] is shipped inside a [Toolchain]"                                                                                      | 4       | "the toolchain specification's self-audit" (judgement 11)                                                                                                                                                                                                                                                                                                                                                                                                                                     | No                                                                                 |

7.1's second paragraph is named by three readers of this cohort, section 8's paragraph beginning
"This MUST is on whoever gives the verdict" by two, and 8.1's first paragraph by two. Of the open
passages, 6.1's paragraph beginning "For a project's own [Rule]" is cleared: its text changed after
run 28 and no reader of this cohort names a passage covering a sentence of it, on the reading of
judgement 11. 7.1's first paragraph and section 8's paragraph on the kind, as each reads at
db47301, are still outstanding (judgement 14).

## Findings applied

None yet. After six cohorts on this pull request the editor has stopped to put a decision to the
owner before changing the text again: the misses that recur in every run (question 2d's order and
grounds, and on the detector document question 2b's "need not remove or forbid") turn on elements of
the keys that the questions do not ask for directly, and on the fourth row keeping a passage open
while any single reader of a fresh cohort names it. Neither can be changed by the editor, since a
question, a key and a threshold may not be changed to let a run pass.

## Process change

Made under the process change of pull request 13 before it merged, at commit 598908b, named
before the readers started; `ACCEPTANCE.md` and `acceptance/runs/README.md` in this worktree
differ from 598908b only by this pull request's question-set line adding question 2d for SPEC.md,
which does not bear on this document.

## Verdict

- **Load-bearing statements (every reader on every one)**: not met. 2a five of five, 2b none of
  five, 2c three of five (readers 1, 4 and 5).
- **Restatement and application (all but one on each keyed item)**: met. Question 1 four of five;
  every clause of question 3, the section 8 verdict and 6.4 five of five.
- **A miss traceable to the text (none)**: not met. Seven, each a finding: 2b by readers 1, 2, 3
  and 4, each quoting 7.1 from "it MUST do at least one of two things" (reader 2 from "but MUST
  do"), none stating that the detector need not remove or forbid the route; 2b by reader 5, saying
  only that the detector "does not have to remove the route" (judgement 7); and 2c by readers 2 and
  3, each quoting only 6.2 and not stating that the documentation ships at a version tracked
  together with the rule (judgement 9).
- **A passage found confusing by two or more (none outstanding)**: not met. 7.1's second paragraph
  is named by readers 1, 2 and 4; section 8's paragraph beginning "This MUST is on whoever gives the
  verdict" by readers 4 and 5; 8.1's first paragraph by readers 4 and 5. The open passages in 7.1's
  first paragraph and section 8's paragraph on the kind are still outstanding (judgement 14); the
  open passage in 6.1's paragraph on a project's own rule is cleared.
- **From one reader only**: 8.1's second paragraph, the 4.3 sentence on machine-readable formats,
  section 2's first sentence and 6.4's Why sentence on the toolchain specification's self-audit,
  recorded.

FAIL on the first, third and fourth criteria. Answer sheets, the readers' prompt and command, and
the marker's instruction: posted on pull request 14 in [comment 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6091188050), [comment 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6091188377), [comment 3](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6091188758).
