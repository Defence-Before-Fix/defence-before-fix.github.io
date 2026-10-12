# Run 28: DETECTOR-SPEC.md, semantic detectors, tenth run in pull request 14

- **Document**: DETECTOR-SPEC.md
- **Pull request**: [14](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14),
  editor's branch `editor/semantic-detectors` at 1db0c67; the question set, key and fixture read
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
  fixture at 1db0c67, in that order, each preceded by one `===== FILE: <name> =====` line, with the
  files separated by one blank line and nothing else added, the same form as the packets of runs
  22, 24 and 26
- **Managed (policy) settings**: none; the machine applies no managed settings and no managed
  settings file is present, as the editor supplied
- **The rest of the isolation**: attested by the editor
- **Readers set aside**: none. The editor reports none set aside for a cause the sheets cannot
  show; every sheet has answer text, no process reports an error (`is_error` false, subtype
  `success`), and every reported model is the cohort's model
- **Run within the pull request**: 10, counting void runs; run 27, made at the same time, does not
  bear on this document
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) dispatched with
  the editor's instruction and its agent definition, `.claude/agents/dbf-spec-editor.md`, having
  seen neither the drafting nor the review

## Marks

| Reader | Q1      | 2a   | 2b   | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | Section 8 | Kind       | 6.4 | Q4 entries |
| ------ | ------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ---------- |
| 1      | correct | ok   | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 2          |
| 2      | miss    | ok   | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 2          |
| 3      | correct | ok   | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 2          |
| 4      | correct | miss | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 2          |
| 5      | correct | ok   | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 2          |

"Q4 entries" counts the entries each reader lists under question 4; the words each quotes are in
the table of passages below. Every miss under question 2 is traceable to the text: each answer
quotes the document in support. The miss under question 1 is the reader's own: the bullet it turns
on quotes nothing. No question was left unanswered.

### Question 1

Every restatement names four or more obligations from the key's list. Readers 1, 3, 4 and 5 assert
no obligation the document does not state: correct. Reader 3's bullet that "a verdict must name the
detector's kind, Semantic, Syntactic or Textual (section 8)" is the obligation the key marks correct
on a verdict, and its bullet that "Inline suppressions should require a written reason (7.2,
SHOULD)" states a recommendation the document makes, as a recommendation (judgement 3). Reader 4's
first bullet and the last sentence of reader 2's sixth state what conformance is; they name no
obligation and assert none the document does not state. Readers 1 and 5 say a printed identifier
must resolve to its documentation, in the generality of 6.1's heading, as the key's own bullet does
(judgement 4). Reader 2's fourth bullet says "every finding must appear in the output of the command
the practitioner ran"; 5.3 says "The summary need not list every finding", so the bullet asserts an
obligation the document does not state: incorrect (judgement 2). Correct, four of five.

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

| Reader | 2a                                                                                     | 2b                                                                                  | 2c                                                                   |
| ------ | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 1      | ok: all four; (d) from the sentence, "not on a declaration", and the 8.1 quotation     | miss: (c) not stated (judgement 5); (b) by the defined term (judgement 6)           | ok: all four; (a) and (c) from the 6.3 quotation                     |
| 2      | ok: all four; (a) from the section 8 quotation, (b) from the 8.1 quotation             | ok: all three; (c) from the 7.1 quotation, "it need not remove or forbid the route" | ok: all four; (b) from the 6.2 quotation, (c) from the 6.3 quotation |
| 3      | ok: all four                                                                           | miss: (c) not stated (judgement 5); (b) by the defined term (judgement 6)           | ok: all four; (c) from the 6.3 quotation                             |
| 4      | miss: (a) not stated, "judged on evidence against the MUSTs" (judgement 7); (d) stated | miss: (c) not stated (judgement 5); (b) by the defined term (judgement 6)           | ok: all four                                                         |
| 5      | ok: all four                                                                           | ok: all three; (c) from the 7.1 quotation; (b) as "make every use of it detectable" | ok: all four; (b) from the 6.2 quotation                             |

No answer asserts anything the document does not state or that the key says makes an answer
wrong: none says a declaration is required, that partial satisfaction is conformance, that the
detector must forbid the route or require a reason, or that a website will do. Every quotation is
verbatim apart from letter case, link and emphasis markup and a closing punctuation mark; reader 4's
8.1 quotation stops before the colon of its sentence, and reader 1's 2a quotation is the whole of
8.1's sentence.

### Question 3

The key's intended verdicts are Yes for every clause but 6.3, which is No; the section 8 verdict
is "does not conform", because 6.3 fails; 6.4 does not change the verdict.

- **Every clause**: all five readers give the intended verdict on every clause, 4.1 to 7.1. On
  6.3 each cites that one unresolved identifier fails the clause, readers 1, 2 and 3 quoting 6.3's
  "One [Identifier] that does not resolve fails this clause"; no reader grades it Partial on the
  grounds that thirty-eight resolve. Readers 1, 2, 3 and 4 add caveats on 4.2 or 4.3 about what the
  fixture does not say, and grade Yes.
- **Section 8**: all five say Lintomatic does not conform, because 6.3 fails.
- **Kind**: all five say the fixture does not let them name the kind and name none, so none is
  marked on it. Reader 3 calls the verdict incomplete on that duty and reader 4 says it cannot
  complete the verdict from the fixture; none makes the verdict turn on the kind, and readers 1, 2,
  3 and 5 say outright that it does not change the verdict or the outcome.
- **6.4**: all five say it does not change the verdict, because it is a SHOULD. Readers 2 and 3 add
  that 7.2 is an unmet SHOULD, reader 2 that a declaration would record the 6.3 gap, and reader 1
  that the toolchain MUST of 6.4's Why paragraph does not apply (judgement 8).

### Judgements made in marking

01. **How an open judgement is made.** As `ACCEPTANCE.md` at 598908b says: as a careful reader of
    the document would, with the reason stated. Where a rule settles a mark, it is applied as
    written.
02. **Question 1, reader 2's "every finding must appear".** Runs 22 and 24 marked incorrect bullets
    saying every finding, or each finding, must appear in the output, because 5.3 says "The summary
    need not list every finding" and "If it leaves any finding out, the output MUST also say where
    the rest can be read". Run 26 marked correct a plain plural, "findings", as 5.3's heading.
    Reader 2's "every finding" is the first case, not the second: a careful reader takes it as a
    claim about each finding, which 5.3 contradicts. Incorrect. The bullet quotes nothing, so the
    miss is the reader's.
03. **Question 1, reader 3's two further statements.** The kind bullet is the obligation the key
    marks correct on a verdict, as run 26 held for the same words. The 7.2 statement is labelled a
    SHOULD and is what 7.2 says, "The [Detector] SHOULD reject, or be configurable to reject, an
    inline [Suppression] that carries no reason"; unlike run 26's reader 4, who called a MAY a
    SHOULD, it asserts nothing the document does not state. Correct.
04. **Question 1, "a printed identifier must resolve", readers 1 and 5.** For a project's own rule
    6.1 asks only that the identifier be printed unaltered. The bullets speak at the level of 6.1's
    heading, "The detector MUST provide a mechanism that resolves a printed identifier to its
    documentation", and the key's bullet is in the same words, so a careful reader takes them as
    that obligation. Correct.
05. **2b (c), not required to remove or forbid, readers 1, 3 and 4.** As runs 22, 24 and 26 held,
    the key's answer includes what the detector need not do, so (c) answers a part of the question.
    Readers 1, 3 and 4 say the detector must do one of the two things. Each quotes 7.1 from "it MUST
    do at least one of two things", which follows the words "it need not remove or forbid the
    route"; reader 1 adds in its sentence that either alone is enough, and readers 3 and 4 quote on
    to "Either alone satisfies this clause." That either alone suffices entails that nothing more is required, but
    does not say that removing or forbidding the route is not required, and an element reached only
    by inference from another is not among the ways `ACCEPTANCE.md` names of stating it. Marked not
    stated, as the earlier runs marked the same element. Readers 2 and 5 quote the clause from "For
    each route it ships, it need not remove or forbid the route", and so state it.
06. **2b (b), the means of detection.** Clause 7.1 defines when a route is detectable in its own
    text; readers 1, 3 and 4 use "detectable" in that sense and so state (b), as runs 22, 24 and 26
    held. It decides no mark, since each of those answers misses (c).
07. **2a (a), reader 4's "judged on evidence against the MUSTs".** The question asks what it means to
    conform. The key's element is that conformance is satisfying every MUST in sections 4 to 7, and
    it says an answer that partial satisfaction is conformance is wrong, so the element's gist is the
    threshold, every MUST, not only what is measured. Reader 4's sentence says what conformance is
    judged against, which is as true of a detector that fails one MUST as of one that meets them all,
    and its quotations, section 8's second sentence and 8.1's sentence on a detector that predates
    the document, do not carry "every MUST in sections 4 to 7" either. A careful reader does not
    take "judged against the MUSTs" as saying all of them must be met. Not stated: a miss, and since
    the answer quotes the document, traceable. Read the other way, the answer would be correct and
    the third criterion would lose one finding; the verdict does not turn on this judgement, since
    2b fails the first and third criteria by three readers whichever way it is made.
08. **Asides outside the keyed answer.** Readers 2's and 3's notes on 7.2, reader 2's on what a
    declaration would record, and reader 1's on the toolchain MUST of 6.4's Why paragraph are not
    keyed items; each sheet's answer to whether 6.4 changes the verdict is the key's, and is marked
    so.
09. **Question 4, reader 4's second entry, named by description.** Reader 4 writes "Clauses 6.1, 6.4,
    7.1 and section 9 refer to clauses in `TOOLING-SPEC.md` and `SPEC.md`, which I was not given",
    with no quotation. `ACCEPTANCE.md` says a passage named without a quotation, by clause number or
    description, covers every sentence of what it names. A careful reader takes what this entry
    names as the references in those clauses to the other two specifications, not every sentence of
    each clause: the clause numbers say where the references are, and the description says which
    sentences confused the reader. So taken, it covers, in 6.1, the sentences of the paragraph
    beginning "For a project's own [Rule]" that cite method clause 3.6 and clause 4.2 of the
    toolchain specification, and the Why paragraph's first sentence; in 6.4, the Why paragraph's
    sentence on the toolchain specification's self-audit; in 7.1, the Why paragraph's sentences
    citing method clause 3.4 and section 4 and clause 4.3 of the toolchain specification; and in
    section 9, the sentences that refer to the method or toolchain specification. Read the other
    way, as every sentence of each clause, it would also cover 7.1's first paragraph, which blocks
    already, and 6.1's heading, which reader 2 also names, making that heading a further passage
    named by two readers; the fourth criterion fails either way, and the verdict does not turn on it.
10. **Question 4, a passage quoted only to set another against it.** Reader 1 quotes 8.1's "A
    [Detector] that predates this document ... MAY be graded [Conforming] on evidence," as what it
    read the 8.1 sentence on a declaration with no gap against. As run 22 held, a quotation under
    question 4 counts whatever it is quoted for; each run of words either side of the ellipsis lies
    in 8.1's second paragraph, at the place the reader names, so it is recorded there.
11. **Question 4, closing punctuation.** Reader 1's "... (TOOLING-SPEC.md)." ends with a full stop
    where the document has a comma; reader 2's "... MUST name its kind," and reader 1's "... on
    evidence," end with a comma where the document has a comma or a colon. The words are consecutive
    and verbatim; the punctuation mark that follows them is not a word, so each is a quotation, as
    run 26 held.
12. **The open passages.** The passages earlier runs of this document found confusing by two or
    more, and not since cleared, are those run 26 left outstanding: 7.1's first paragraph (runs 20,
    22, 24 and 26) and section 8's paragraph on the kind, which at 1db0c67 begins "A verdict on a
    [Detector] MUST name its kind" (runs 24 and 26). The text of each changed after run 26, in
    0b2d190 and e783b64, and each is taken as it reads at 1db0c67. 8.1's first and second paragraphs,
    6.1's paragraph beginning "For a [Bundled rule]" and clause 4.1 were cleared by runs 22, 24 and
    26, and do not reopen when one reader of a later cohort names them.

No re-mark.

## Passages quoted as confusing

Grouped by paragraph, as `ACCEPTANCE.md` defines the same passage. A passage blocks when two or
more readers name it, or when it covers a sentence of a paragraph in which one of the open
passages lay (judgement 12), as that paragraph reads at 1db0c67.

| Clause and paragraph                                                                                                                                                                                                                                     | Readers                | Words quoted, verbatim                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Blocks                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 8, the paragraph beginning "A verdict on a [Detector] MUST name its kind", its first, second and fifth sentences                                                                                                                                         | 2, 3, 4, 5             | 2: "A verdict on a [Detector] MUST name its kind," and "the kind is not a level of [Conformance] and does not change the verdict." 3: "each configuration the verdict grades" and "configuration". 4: "A verdict on a [Detector] MUST name its kind" and "The kind is not a level of [Conformance] and does not change the verdict." 5: "A verdict on a [Detector] MUST name its kind", "This duty is on whoever gives the verdict, not on the [Detector]" and "the kind is not a level of [Conformance] and does not change the verdict." (judgement 11) | Yes: four readers, and the open section 8 paragraph of runs 24 and 26 |
| 7.1, first paragraph, the sentence beginning "A route is detectable when"                                                                                                                                                                                | 3                      | "A route is detectable when the project can find every use of it, either with a [Rule] of the project's own that the [Detector] runs, or with a mechanical check the [Detector] documents."                                                                                                                                                                                                                                                                                                                                                               | Yes: the open 7.1 paragraph of runs 20, 22, 24 and 26                 |
| 6.1, the paragraph beginning "For a project's own [Rule]", its first sentence, its sentence beginning "Where the [Identifier] is itself a URL" and its last sentence                                                                                     | 1, 2; 4 by description | 1: "The lookup for such a Rule is an obligation on the project's assembled Toolchain, under clause 4.2 of the [toolchain specification](TOOLING-SPEC.md)." 2: "what it owes is the half it can give: the [Identifier] printed unaltered under clause 4.3, and no transformation of it." 4: no quotation, the references to the other specifications (judgements 9 and 11)                                                                                                                                                                                 | Yes: two readers, three on judgement 9                                |
| 6.1, the heading                                                                                                                                                                                                                                         | 2                      | "The detector MUST provide a mechanism that resolves a printed identifier to its documentation," (judgement 11)                                                                                                                                                                                                                                                                                                                                                                                                                                           | No; on the other reading of judgement 9, reader 4 too                 |
| 8.1, first paragraph, the sentence "A declaration that records no gap claims [Conformance]."                                                                                                                                                             | 1                      | "A declaration that records no gap claims [Conformance]."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No; cleared by run 24 (judgement 12)                                  |
| 8.1, second paragraph, its first sentence                                                                                                                                                                                                                | 1                      | "A [Detector] that predates this document" and "MAY be graded [Conforming] on evidence," (judgements 10 and 11)                                                                                                                                                                                                                                                                                                                                                                                                                                           | No; cleared by run 26 (judgement 12)                                  |
| 3, the table row "Resolution of a project's own [Rule]"                                                                                                                                                                                                  | 5                      | "The documentation and, with the [Toolchain], the lookup."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                                                                    |
| 6.1, the Why paragraph, its first sentence; 6.4, the Why paragraph, its sentence on the toolchain specification's self-audit; 7.1, the Why paragraph, its first and last sentences; 9, the sentences that refer to the method or toolchain specification | 4                      | No quotation; "Clauses 6.1, 6.4, 7.1 and section 9 refer to clauses in `TOOLING-SPEC.md` and `SPEC.md`" (judgement 9)                                                                                                                                                                                                                                                                                                                                                                                                                                     | No                                                                    |

Section 8's paragraph on the kind is named by four readers of this cohort, and 6.1's paragraph on a
project's own rule by two, three on judgement 9. Of the open passages, neither is cleared: this
cohort names passages covering sentences of 7.1's first paragraph and of section 8's paragraph on
the kind, as each reads at 1db0c67.

## Findings applied

Applied to the text, never to a question, threshold, fixture or key, in c6ee1a8 and the commit after
it that settles its review (key quotations kept verbatim in 224579f and that commit). The editor
first read every sheet, in runs 20 to 28, that named each passage, and fixed the cause the sheets
show. DETECTOR-SPEC.md: clause 7.1 says after the two things too that neither requires removing or
forbidding the route, and says what the detector does when the project detects a route with its own
rule; section 8's paragraph on the kind uses "configuration" in one sense and says the kind does not
change the conformance verdict; clause 6.1's paragraph on a project's own rule no longer leans on
cross-references a reader of this document alone cannot follow. A fresh cohort follows.

## Process change

Made under the process change of pull request 13 before it merged, at commit 598908b, named
before the readers started; `ACCEPTANCE.md` and `acceptance/runs/README.md` in this worktree
differ from 598908b only by this pull request's question-set line adding question 2d for SPEC.md,
which does not bear on this document.

## Verdict

- **Load-bearing statements (every reader on every one)**: not met. 2a four of five (all but
  reader 4), 2b two of five (readers 2 and 5), 2c five of five.
- **Restatement and application (all but one on each keyed item)**: met. Question 1 four of five;
  every clause of question 3, the section 8 verdict and 6.4 five of five.
- **A miss traceable to the text (none)**: not met. Four, each a finding: 2b by readers 1, 3 and 4,
  each quoting 7.1 from "it MUST do at least one of two things", none stating that the detector
  need not remove or forbid the route; and 2a by reader 4, quoting section 8's "It is judged on the
  evidence, and a declaration under clause 8.1 is optional." and not stating that conformance is
  satisfying every MUST in sections 4 to 7 (judgement 7).
- **A passage found confusing by two or more (none outstanding)**: not met. Section 8's paragraph on
  the kind is named by readers 2, 3, 4 and 5, and 6.1's paragraph beginning "For a project's own
  [Rule]" by readers 1 and 2 (and 4, judgement 9); the open passages in 7.1's first paragraph
  (reader 3) and section 8's paragraph on the kind are still outstanding.
- **From one reader only**: 6.1's heading, 8.1's first and second paragraphs, the section 3 table
  row on a project's own rule, and the references reader 4 names in 6.1, 6.4, 7.1 and section 9,
  recorded.

FAIL on the first, third and fourth criteria. Answer sheets, the readers' prompt and command, and
the marker's instruction: posted on pull request 14 in [comment 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6091000028), [comment 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6091000433), [comment 3](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6091000975).
