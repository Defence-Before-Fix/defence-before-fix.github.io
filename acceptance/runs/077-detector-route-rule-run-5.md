# Run 77: DETECTOR-SPEC.md, detector route rule, fifth run

- **Document**: DETECTOR-SPEC.md
- **Pull request**: [23](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/23), from branch
  `editor/detector-route-rule`. The readers read commit dbdf841. Change: clause 7.1's detectable
  route is a bespoke rule the project writes for the detector under clause 4.1, with a paragraph
  on what detectable means; clause 8.1's gap duty falls only on a detector that declares a
  version; clause 5.3 says what the remainder is; clause 6.1 says it asks for the mechanism, a
  missing page failing clause 6.3, and that a path in the message is not enough on its own;
  section 2's table gains a Message row. Revised after run 73 in the two paragraphs its findings
  named: clause 5.3's paragraph now defines a usable summary (each finding carries where it is
  and its Identifier) and the remainder (the findings the summary leaves out; none where the
  output prints every finding; a fuller report written elsewhere is not one and need not be
  named), and clause 7.1's second paragraph now states the two ways a route is detectable in one
  paragraph (a bespoke Rule registered under clause 4.1, or a mechanical check the Detector
  documents); so this is a fresh run.
- **Run within the pull request**: 5 (runs 60, 63, 66 and 73 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `2a96d5b0c6339f5402c9883018d35c0353c42dfad581c94d9b80a8b428882bc9`) is
  `QUESTIONS.md`, `DETECTOR-SPEC.md` and `fixtures/lintomatic.md` at dbdf841, each after one
  `===== FILE: <name> =====` line, one blank line between files; the marker rebuilt it from that
  commit and it matched byte for byte.
- **Readers set aside**: none. Every reader's output has `is_error` false, subtype `success`,
  non-empty answer text and the cohort's model.
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  marking instruction and its agent definition, having seen neither the drafting nor the review.

## Marks

Readers are numbered 1 to 5 as their sheets are. Question 3 columns: the eleven clauses, then
the two answers (S8 conformance under section 8, 6.4 whether clause 6.4 changes the verdict).

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2  | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | S8  | 6.4 |
| ------ | ------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1      | correct | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 2      | correct | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 3      | correct | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 4      | correct | ok  | ok  | ok  | ok  | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 5      | correct | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |

Question 1: correct bullets among the first six, per reader, 6, 6, 6, 5 and 6. Readers 1 and 5
give one bullet per line of the key's list. Reader 2 joins 4.1 and 4.2 in its first bullet and
splits 5.1 to 5.3 from 5.4. Reader 3 gives seven bullets; only the first six are marked (4.1,
4.2, 4.3, 5.1 to 5.3, 5.4, 6.1 to 6.3), and its seventh, on 7.1, is not marked. Reader 4 gives
five bullets, each naming a line of the key's list. Readers 1, 2 and 4 say the command's output
carries each finding with its location and identifier, which names 5.3 and is not marked wrong
for the plural. No bullet asserts anything the key marks wrong.

Question 2: every reader states every required element of each item and quotes the document.
For 2a all five state that conformance is every MUST in sections 4 to 7 and that a detector
predating the document can conform, quoting section 8's definition and clause 8.1's "A Detector
that predates this document, or whose maintainer has never read it, MAY be graded Conforming on
evidence"; readers 1 and 4 also quote "a Detector without one can still be found to Conform".
For 2b all five name both things, disableable by configuration or detectable, and that either
alone is enough, quoting clause 7.1's "For each one it MUST do at least one of two things, and
either alone satisfies this clause" (reader 2 with an ellipsis; its longest verbatim run is well
over six words). Reader 4 adds that a detector whose rules never see comments has only the
documented mechanical check, the document's own sentence, which is not among the key's wrong
assertions for 2b. For 2c all five state that the documentation ships with the rule in the
installed copy, at a version tracked together, and is reachable without network access,
quoting the 6.2 and 6.3 headings; readers 3, 4 and 5 add clause 6.3's "Every Identifier a
Bundled rule can print MUST resolve", which agrees with the key.

Question 3: readers 1, 2, 3 and 5 give every accepted grade, several with caveats on 4.2 (the
fixture does not say `--only` prints finding lines) and 4.3 (no machine-readable format
described); the key says a caveat with the accepted grade is correct. Readers 1, 3 and 5 state
that they read the two undocumented rules as bundled; reader 3 adds what would follow if they
were project rules, but gives No as its grade without condition. All five grade 5.3 Yes, every
finding being printed so no remainder needs naming, and 6.1 Yes. S8: all five say Lintomatic
does not conform, naming 6.3. 6.4: all five say it does not change the verdict, because it is a
SHOULD.

### Misses

- **Reader 4, clause 4.2: Partial** (accepted: Yes). Reasoning: `--only` runs a single rule and
  exits 1 when it fires, which covers "whether the Rule fired", but the fixture never says a
  single-rule run prints its findings, so "what it printed" is not established. The reasoning
  quotes four and three words of clause 4.2, below the six that `ACCEPTANCE.md` defines as
  quoting the document, so it does not quote the document; it puts the gap on the fixture's
  silence. The key names no wrong reading for 4.2. A single miss, the reader's, tolerated by the
  threshold.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..dbdf841 adds,
rewords, moves or deletes a sentence in the paragraph, or changes a word, term or link in it.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                                       | Readers    | Changed by the diff |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ------------------- |
| 1   | Clause 5.3, first paragraph: "The remainder is the findings the summary leaves out: where the output prints every finding there is none, and a fuller report written elsewhere, such as a page with a code snippet for each finding, is not one and need not be named."; what "is not one" refers to (the remainder or the summary), and the double negative | 2, 3, 4, 5 | yes                 |
| 2   | Clause 7.1, second paragraph: "The first way needs the [Detector]'s [Rules] to be able to match the route's text, so a [Detector] whose [Rules] never see comments offers only the second for an ignore comment."; how the project's bespoke rule relates to the detector's matching, given "need not ship itself"                                           | 1          | yes                 |
| 3   | Clause 6.4, Why paragraph: "Where the [Detector] is shipped inside a [Toolchain], the [toolchain specification]'s self-audit makes this check a MUST for the [Toolchain]; a [Detector] released on its own is asked for it as a SHOULD."; whether a detector inside a toolchain keeps the SHOULD                                                             | 1          | yes                 |
| 4   | Clause 6.1, "For a project's own [Rule]" paragraph: "The lookup for such a [Rule] is an obligation on the project's assembled [Toolchain], under clause 4.2 of the [toolchain specification]"; the referenced clause could not be checked                                                                                                                    | 3          | no                  |
| 5   | Clause 7.1, Why paragraph: "the method specification's position is that [Suppression] is an [Owner] decision under its clause 3.4 and section 4"; it depends on definitions in SPEC.md                                                                                                                                                                       | 3          | no                  |

Notes, not passages: reader 1's third item is about the fixture's `explain` paragraph and its
last paragraph (whether the two rules printing `No documentation declared` are bundled), not a
passage of the document. Reader 2 notes that defined terms link to SPEC.md, which was not
supplied: a remark about another document.

## Findings and where they lie

- **Finding A, passage 1, clause 5.3 first paragraph** (readers 2, 3, 4 and 5): the diff
  9e914fe..dbdf841 rewords this paragraph's obligation sentence and adds the sentences after it,
  including the one all four readers quote. Text the change wrote. Blocks.

Passages 2 to 5 are each named by one reader: recorded, not findings. Passages 2 and 3 lie in
changed paragraphs but are single. Nothing is routed to `acceptance/ROUTED.md` from this run.

## Points the rules did not settle

1. **Reader 3's passages 4 and 5.** Each quotes six or more words of the document with its
   clause number, which `ACCEPTANCE.md` counts as naming a passage, but the confusion stated is
   that SPEC.md or TOOLING-SPEC.md was not supplied, which it records as a note and not a
   passage. Under the open-point rule, an open point on whether a reader named a passage counts
   the passage, so both are listed as passages. Each is named by reader 3 alone, so the verdict
   does not turn on the point.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit bc6ae14, named before the readers started.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item but
  4.2, which is four of five. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: one (finding A).
  Not met.
- Passages named by two or more readers elsewhere: none.

## Findings applied

None at the time of marking; finding A is on the change's own text, to be fixed there before a
fresh cohort.

## Verdict

FAIL. Every keyed item passed its threshold and no miss counts against the document, but
finding A (clause 5.3, first paragraph, the sentence defining the remainder, named by four of
five readers) lies in text the change wrote, and blocks.

## Answer sheets

Posted on the pull request: LINK PLACEHOLDER.
