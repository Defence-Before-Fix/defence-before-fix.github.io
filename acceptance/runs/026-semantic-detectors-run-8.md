# Run 26: DETECTOR-SPEC.md, semantic detectors, eighth run in pull request 14

- **Document**: DETECTOR-SPEC.md
- **Pull request**: [14](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14),
  editor's branch `editor/semantic-detectors` at dfb9b68; the question set, key and fixture read
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
  fixture at dfb9b68, in that order, each preceded by one `===== FILE: <name> =====` line, with the
  files separated by one blank line and nothing else added, the same form as the packets of runs
  22 and 24
- **Managed (policy) settings**: none; the machine applies no managed settings and no managed
  settings file is present, as the editor supplied
- **The rest of the isolation**: attested by the editor
- **Readers set aside**: none. The editor reports none set aside for a cause the sheets cannot
  show; every sheet has answer text, no process reports an error (`is_error` false, subtype
  `success`), and every reported model is the cohort's model
- **Run within the pull request**: 8, counting void runs; run 25, made at the same time, does not
  bear on this document
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) dispatched with
  the editor's instruction and its agent definition, `.claude/agents/dbf-spec-editor.md`, having
  seen neither the drafting nor the review

## Marks

| Reader | Q1      | 2a  | 2b   | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | Section 8 | Kind       | 6.4 | Q4 entries |
| ------ | ------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ---------- |
| 1      | correct | ok  | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 2          |
| 2      | correct | ok  | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 1          |
| 3      | correct | ok  | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 1          |
| 4      | miss    | ok  | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 1          |
| 5      | correct | ok  | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 1          |

"Q4 entries" counts the entries each reader lists under question 4; the words each quotes are in
the table of passages below. Every miss under question 2 is traceable to the text: each answer
quotes the document in support. The miss under question 1 is the reader's own: the bullet it turns
on quotes nothing. No question was left unanswered.

### Question 1

Every restatement names four or more obligations from the key's list. Readers 1, 2, 3 and 5 assert
no obligation the document does not state: correct. Reader 3's last bullet, that "a verdict must
name the rule kind (Semantic, Syntactic, or Textual)", is the obligation the key marks correct on
a verdict (judgement 3). Readers 2 and 5 say findings must appear in, or be put in, the command's
own output, without "each" or "every" (judgement 2). Reader 4's sixth bullet says "The SHOULDs add
a reason requirement for suppressions, a release check for undocumented bundled rules, and a
conformance declaration that records known gaps"; the declaration is a MAY (8.1's heading, and "a
declaration is optional"), so the bullet asserts a recommendation the document does not make:
incorrect (judgement 4). Correct, four of five.

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

| Reader | 2a                                                                    | 2b                                                                        | 2c                                                                   |
| ------ | --------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 1      | ok: all four; (b) and (d) from the 8.1 quotation                      | miss: (c) not stated (judgement 5); (b) by the defined term (judgement 6) | ok: all four; (a) and (c) from the 6.3 quotation                     |
| 2      | ok: all four; (b) and (d) from the 8.1 quotation                      | miss: (c) not stated (judgement 5); (b) by the defined term (judgement 6) | ok: all four; (b) from the 6.2 quotation, (c) from the 6.3 quotation |
| 3      | ok: all four; (d) from the 8.1 quotation                              | miss: (c) not stated (judgement 5); (b) by the defined term (judgement 6) | ok: all four; (a) and (c) from the 6.3 quotation                     |
| 4      | ok: all four; (d) from the section 8 and 8.1 quotations               | miss: (c) not stated (judgement 5)                                        | ok: all four                                                         |
| 5      | ok: all four, in the sentence, which says "a declaration is optional" | miss: (c) not stated (judgement 5)                                        | ok: all four; (b) from the 6.2 quotation                             |

No answer asserts anything the document does not state or that the key says makes an answer
wrong: none says a declaration is required, that partial satisfaction is conformance, that the
detector must forbid the route or require a reason, or that a website will do. Every quotation is
verbatim apart from letter case, link and emphasis markup and a closing punctuation mark; the 2c
quotations of readers 1, 2, 3, 4 and 5 are the headings of 6.2 and 6.3.

### Question 3

The key's intended verdicts are Yes for every clause but 6.3, which is No; the section 8 verdict
is "does not conform", because 6.3 fails; 6.4 does not change the verdict.

- **Every clause**: all five readers give the intended verdict on every clause, 4.1 to 7.1. On
  6.3 each cites that one unresolved identifier fails the clause, or quotes 6.3's "One
  [Identifier] that does not resolve fails this clause, however many others do."; no reader grades
  it Partial on the grounds that thirty-eight resolve. Readers 1, 2, 4 and 5 add caveats on 4.2 or
  4.3 about what the fixture does not say, and grade Yes.
- **Section 8**: all five say Lintomatic does not conform, because 6.3 fails.
- **Kind**: all five say the fixture does not let them name the kind and name none, so none is
  marked on it. Readers 1, 3 and 5 call the verdict incomplete on that point and reader 2 says a
  complete verdict would need it; none makes the verdict turn on it, and readers 3 and 5 say
  outright that it does not change the verdict.
- **6.4**: all five say it does not change the verdict, because it is a SHOULD. Readers 3, 4 and 5
  add asides on what a declaration under 8.1 would record (judgement 7).

### Judgements made in marking

01. **How an open judgement is made.** As `ACCEPTANCE.md` at 598908b says: as a careful reader of
    the document would, with the reason stated. Where a rule settles a mark, it is applied as
    written.
02. **Question 1, "Findings" in the output, readers 2 and 5.** Reader 2 says "Findings must appear
    in the output of the command the practitioner ran"; reader 5 that the detector must "put
    findings in the command's own output". Run 24 marked incorrect a bullet saying "each finding
    must appear", because 5.3 says "The summary need not list every finding". A plain plural
    without "each" or "every" says what 5.3's heading says, "The result MUST reach the
    practitioner in the output of the command they ran", and a careful reader takes it as that
    heading, not as a claim about every finding. Correct.
03. **Question 1, reader 3's "rule kind".** Section 8 puts the naming of the kind on the verdict,
    for each configuration graded; the terminology table defines the three kinds as "What a [Rule]
    can ask in a configuration". The key marks correct a bullet saying a verdict must state the
    detector's kind. "Rule kind" names the same three kinds by what a rule can ask, which the
    document's own definition does, and a careful reader takes the bullet as the key's obligation
    on the verdict. Correct.
04. **Question 1, reader 4's "SHOULDs".** The document defines its key words under RFC 2119, where
    SHOULD recommends and MAY permits, and it says in 8.1 and section 8 that a declaration is
    optional. A careful reader of a document that draws that line takes "The SHOULDs add ... a
    conformance declaration" as stating a recommendation to declare that the document does not
    make, and so an obligation the document does not state. Read the other way, as a loose list of
    the non-MUST provisions, the bullet would be correct; Question 1 would then be five of five, and
    neither reading changes whether the second criterion holds or adds a traceable miss, since the
    bullet quotes nothing.
05. **2b (c), not required to remove or forbid, all five.** The question asks what the detector
    must do about the route; the key's answer includes what it need not do, so (c) answers a part
    of the question. Readers 1, 2 and 3 say the detector must do one of the two things; readers 4
    and 5 add "Either one is enough". That entails that nothing more is required, but it does not
    say that removing or forbidding the route is not required: "Either one is enough" paraphrases
    the first half of 7.1's sentence "Either alone satisfies this clause, and neither requires the
    [Detector] to remove or forbid the route", not its second half, and no reader quotes that half
    or 7.1's first sentence, "The [Detector] does not have to remove or forbid an inline
    [Suppression] route." `ACCEPTANCE.md` names the ways an element is stated: the document's words,
    a paraphrase, a synonym, a defined term in its defined sense. An element reached only by
    inference from another is not among them, and a careful reader of that rule does not add it.
    Marked not stated, as runs 22 and 24 marked the same element. The verdict does not turn on this
    judgement alone: the fourth criterion fails whichever way it is made.
06. **2b (b), the means of detection.** Clause 7.1 defines "Detectable" in its own text. Readers 1,
    2 and 3 use "detectable" in that sense, and so state (b), as runs 22 and 24 held; reader 5's
    "make every use of the route detectable" uses the definition's own words. It decides no mark,
    since every 2b answer misses (c).
07. **Asides outside the keyed answer.** Reader 3's statement that 6.4 would not appear in
    `known-gaps`, and readers 4's and 5's that a declaration would record the 6.3 gap, are not keyed
    items; each sheet's answer to whether 6.4 changes the verdict is the key's, and is marked so.
08. **Question 4, a clause number inside a quotation, and context in the reader's explanation.**
    Reader 4's quotation contains "as clause 4.1 lets it", and its explanation speaks of "a rule
    written under 4.1"; reader 1's explanation of its section 8 entry speaks of "section 8's
    conformance test"; reader 3's quotation contains "a [Detector] failing 4.1". Each reader heads
    its entry with the clause it found confusing (7.1, 8 and 4.2) and quotes the words; a careful
    reader takes the other clause as the context of the confusion, not a further passage named.
    Read the other way, each would add a passage named by one reader only, in a paragraph no
    earlier passage of this document left open (clause 4.1 was cleared by run 22, as run 24
    records), and nothing that blocks.
09. **Question 4, reader 5's quoted terms.** Reader 5 heads its entry "Section 2, the terminology
    paragraph" and quotes "Every capitalised term links to its definition," and then the terms
    "[Semantic], [Syntactic] or [Textual]" and "[Conform]" as the ones it found defined only by
    links. `ACCEPTANCE.md` says a quotation covers what an occurrence of its words overlaps "at the
    place the reader names it", and reaches every place the run occurs only "where the reader names
    no place". Reader 5 names section 2's terminology paragraph for the whole entry, and neither
    term's run occurs there (the terminology table, a separate paragraph, reads "[Semantic],
    [Syntactic], [Textual]"). A careful reader takes the entry as the section 2 sentence, with the
    terms as the examples the reader gives of it, so the term quotations cover no further sentence.
    Read the other way, "[Semantic], [Syntactic] or [Textual]" would cover the first sentence of
    section 8's paragraph on kind, and "[Conform]" the sentences of 5.4, 7.1's first paragraph,
    section 8's paragraph on kind, 8.1's Why paragraph and section 9 where that word occurs; that
    would make reader 5 a second reader of section 8's paragraph on kind and of 7.1's first
    paragraph, both of which block already, and the verdict does not turn on it.
10. **Question 4, a reader that resolved its confusion.** Reader 2 says of its 6.1 and 6.3 passage
    "I resolved this with 6.1's own pointer". Question 4 asks for any passage found confusing on
    the one reading, and the reader names it as such "On my first read", so it is recorded.
11. **Question 4, closing punctuation.** Reader 1's "... it grades." ends with a full stop where
    the document has a comma, and reader 5's "... to its definition," and reader 2's "... not for
    every page," end with a comma where the document has a semicolon or a full stop. The words are
    consecutive and verbatim; the punctuation mark that follows them is not a word, so each is a
    quotation.
12. **The open passages.** The passages earlier runs of this document found confusing by two or
    more, and not since cleared, are those run 24 left outstanding or added: 7.1's first paragraph
    (runs 20, 22 and 24), 8.1's second paragraph (runs 20, 22 and 24) and section 8's paragraph
    beginning "A verdict on a [Detector] MUST also name" (run 24, four readers). The text of each
    changed after run 24, in b172fd6, and each is taken as it reads at dfb9b68.

No re-mark.

## Passages quoted as confusing

Grouped by paragraph, as `ACCEPTANCE.md` defines the same passage. A passage blocks when two or
more readers name it, or when it covers a sentence of a paragraph in which one of the open
passages lay (judgement 12), as that paragraph reads at dfb9b68.

| Clause and paragraph                                                                                                               | Readers | Words quoted, verbatim                                                                                                                                                                                                           | Blocks                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| 8, the paragraph beginning "A verdict on a [Detector] MUST also name", its first sentence                                          | 1       | "A verdict on a [Detector] MUST also name the kind of each configuration it grades." (judgement 11)                                                                                                                              | Yes: the open section 8 paragraph of run 24             |
| 7.1, first paragraph, the sentences "Detectable means ...", "There are two ways." and "One is a [Rule] ..."                        | 4       | "Detectable means the project can find every use of the route. There are two ways. One is a [Rule] the project writes and registers with the [Detector], as clause 4.1 lets it." (judgement 8)                                   | Yes: the open 7.1 paragraph of runs 20, 22 and 24       |
| 4.3, first paragraph, the sentence beginning "The [Detector] MUST print it, unaltered"                                             | 1       | "in its default output and in every machine-readable format it offers."                                                                                                                                                          | No                                                      |
| 4.2, first paragraph, its second sentence                                                                                          | 3       | "This applies to every [Rule] the [Detector] runs, bundled or bespoke; a [Detector] failing 4.1 is graded here on its [Bundled rules]." (judgement 8)                                                                            | No; one reader of run 24 also named it                  |
| 6.1, the paragraph beginning "In both", the sentences "This clause asks for the mechanism ..." and "Where the mechanism works ..." | 2       | "This clause asks for the mechanism, not for every page," and "Where the mechanism works but a [Bundled rule]'s [Identifier] has no documentation to resolve to, that fails clause 6.3, not this clause." (judgements 10 and 11) | No; one reader of run 22 also named the second sentence |
| 6.3, first paragraph, its first sentence                                                                                           | 2       | "Every [Identifier] a [Bundled rule] can print MUST resolve, under clause 6.1, to a page in that shipped documentation." (judgement 10)                                                                                          | No                                                      |
| 2, first paragraph, its second sentence                                                                                            | 5       | "Every capitalised term links to its definition," and the terms "[Semantic], [Syntactic] or [Textual]" and "[Conform]" (judgements 9 and 11)                                                                                     | No                                                      |

No passage is named by two or more readers of this cohort, on the reading of judgement 9. Of the
open passages, 8.1's second paragraph is cleared: its text changed after run 24 and no reader of
this cohort names a passage covering a sentence of it, on either reading of judgement 9. 7.1's
first paragraph and section 8's paragraph on kind are still outstanding.

## Against the criteria

- **Load-bearing statements (every reader on every one)**: not met. 2a five of five, 2b none of
  five, 2c five of five.
- **Restatement and application (all but one on each keyed item)**: met. Question 1 four of five;
  every clause of question 3, the section 8 verdict and 6.4 five of five.
- **A miss traceable to the text (none)**: not met. Five, each a finding: 2b by all five readers,
  each quoting 7.1's sentence "For each route it ships, it MUST do at least one of two things: ...",
  none stating that the detector need not remove or forbid the route.
- **A passage found confusing by two or more (none outstanding)**: not met. The open passages in
  7.1's first paragraph (reader 4) and section 8's paragraph on kind (reader 1) are still named by
  this cohort.
- **From one reader only**: the 4.3 sentence on machine-readable formats, the 4.2 sentence on a
  detector failing 4.1, the 6.1 sentences on the mechanism and a missing page, the 6.3 sentence on
  every identifier resolving, and the section 2 sentence on capitalised terms, recorded.

## Findings applied

Applied to the text, never to a question, threshold, fixture or key, in 0b2d190 and the commit after
it that settles its review (key quotations kept verbatim in d07c177 and that commit). DETECTOR-
SPEC.md: clause 7.1's MUST sentence says the detector need not remove or forbid the route, and its
first paragraph is plainer; section 8's paragraph on the kind is shorter. A fresh cohort follows.

## Process change

Made under the process change of pull request 13 before it merged, at commit 598908b, named
before the readers started; `ACCEPTANCE.md` and `acceptance/runs/README.md` in this worktree
differ from 598908b only by this pull request's question-set line adding question 2d for SPEC.md,
which does not bear on this document.

## Verdict

FAIL on the first, third and fourth criteria. Answer sheets, the readers' prompt and command, and
the marker's instruction: posted on pull request 14 in [comment 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090847649), [comment 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090848005), [comment 3](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090848260).
