# Run 73: DETECTOR-SPEC.md, detector route rule, fourth run

- **Document**: DETECTOR-SPEC.md
- **Pull request**: [23](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/23), from branch
  `editor/detector-route-rule`. The readers read commit d67174c. Change: clause 7.1's detectable
  route is a bespoke rule the project writes for the detector under clause 4.1, with a paragraph
  on what detectable means; clause 8.1's gap duty falls only on a detector that declares a
  version; clause 5.3 says what the remainder is; clause 6.1 says it asks for the mechanism, a
  missing page failing clause 6.3, and that a path in the message is not enough on its own;
  section 2's table gains a Message row. Revised after run 69 (a cohort of another change with
  this one merged in) in clause 5.3's obligation sentence, the location of the remainder owed
  only where the summary leaves a finding out, and in clause 8.1's second paragraph, where a
  practitioner's record of a gap lives and that a detector without a declaration can still be
  found to conform; so this is a fresh run.
- **Run within the pull request**: 4 (runs 60, 63 and 66 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `0df0b01c02c5d2fd83b37d218f88785980384c3a0ecadce92abf7088211c9249`) is
  `QUESTIONS.md`, `DETECTOR-SPEC.md` and `fixtures/lintomatic.md` at d67174c, each after one
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
| 3      | correct | ok  | ok  | ok  | ok  | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 4      | correct | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 5      | correct | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |

Question 1: correct bullets per reader 6, 6, 6, 6 and 6. Readers 1, 2, 3 and 5 give one bullet
per line of the key's list (4.1; 4.2; 4.3; 5.1 to 5.4; 6.1 to 6.3; 7.1). Reader 4 splits 5.1 to
5.3 from 5.4, which are different clauses of one line and each count, and joins 6.1 to 6.3 with
7.1 in its sixth bullet. Reader 2's fourth bullet says every finding must reach the command's
output, which the key says names 5.3 and is not marked wrong for the plural; its fifth bullet
says every identifier the detector can print must have a page, which names the 6.1 to 6.3 line
and is not among the key's wrong assertions. Reader 5 adds, after its six bullets, a line on
what conformance means; it is not among the first six bullets and states no obligation. No
bullet asserts anything the key marks wrong.

Question 2: every reader states every required element of each item and quotes the document.
For 2a all five state that conformance is every MUST in sections 4 to 7 and that a detector
predating the document can conform; readers 1 to 4 quote section 8's definition, and all five
quote clause 8.1's "A Detector that predates this document, or whose maintainer has never read
it, MAY be graded Conforming on evidence" (reader 5 also its "a Detector without one can still
be found to Conform"). For 2b all five name both things, disableable by configuration or
detectable, and that either alone is enough, quoting clause 7.1's "For each one it MUST do at
least one of two things, and either alone satisfies this clause". Readers 2, 3 and 5 add that
the bespoke-rule way is closed to a detector whose rules never see comments, the document's own
sentence, which is not among the key's wrong assertions for 2b. For 2c all five state that the
documentation ships with the rule (in the installed copy), at a version tracked together, and
is reachable without network access, quoting the 6.2 and 6.3 headings; reader 4 adds clause
6.2's sentence that a website catalogue is the wrong place, which agrees with the key.

Question 3: readers 1, 2, 4 and 5 give every accepted grade, each with caveats on 4.2 (the
fixture does not say `--only` prints finding lines) and 4.3 (no machine-readable format
described); the key says a caveat with the accepted grade is correct. S8: all five say
Lintomatic does not conform, naming 6.3. 6.4: all five say it does not change the verdict,
because it is a SHOULD.

### Misses

- **Reader 3, clause 4.2: Partial** (accepted: Yes). Reasoning: `--only` runs one rule and exits
  1 when it fires, but the clause requires the harness to report "what it printed" and the
  fixture never says `--only` prints the finding line; "it becomes Yes if `--only` output
  includes the finding". The reasoning quotes three words of the document, below the six that
  `ACCEPTANCE.md` defines as quoting it, so it does not quote the document. The key names no
  wrong reading for 4.2. A single miss, the reader's, tolerated by the threshold. Reader 3's
  question 4 note puts the close call on the fixture, not the document.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..d67174c adds,
rewords, moves or deletes a sentence in the paragraph, or changes a word, term or link in it.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                   | Readers | Changed by the diff |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ------------------- |
| 1   | Clause 8.1, first paragraph: "The same declaration is where a gap against this document is recorded once it is known: a [Detector] that declares a version and has learnt… that it fails a MUST in sections 4 to 7 MUST record that gap…"; whether a MUST in section 8 counts toward conformance                         | 1       | yes                 |
| 2   | Clause 5.3, first paragraph: "the invoked command's own output MUST carry a usable summary" (2, what makes a summary usable); "The remainder is the findings the summary leaves out." (5, whether a fuller HTML report is a remainder, settled only by the sentences after)                                              | 2, 5    | yes                 |
| 3   | Clause 7.1, second paragraph: "a [Detector] whose [Rules] never see comments cannot make an ignore comment detectable this way" (2, whether a property of the detector's API or of its rules); "That way is open only where the [Detector]'s [Rules] can see the route: …" (4, whether the route was open to Lintomatic) | 2, 4    | yes                 |
| 4   | Section 1, "The governing principle" paragraph: "a [Conforming] [Detector] MUST make that possible without the project building the mechanism first"; an unnumbered MUST outside sections 4 to 7, and whether it bears on conformance                                                                                    | 4       | no                  |
| 5   | Clause 4.2, first paragraph: "a [Detector] failing 4.1 is graded here on its [Bundled rules]", set beside the sentence before it that the clause applies to every rule                                                                                                                                                   | 5       | no                  |

Notes, not passages: reader 3 wrote "none", adding that its 4.2 close call came from the fixture
not stating what `--only` prints, not from the document.

## Findings and where they lie

- **Finding A, passage 2, clause 5.3 first paragraph** (readers 2 and 5): the diff 9e914fe..d67174c
  rewords this paragraph's obligation sentence and adds its three following sentences, so it is
  text the change wrote or altered. Reader 2's words ("usable summary") are in the part of the
  sentence the change kept, but the rule is by paragraph. Blocks.
- **Finding B, passage 3, clause 7.1 second paragraph** (readers 2 and 4): the diff adds this
  paragraph. Text the change wrote. Blocks.

Passages 1, 4 and 5 are each named by one reader: recorded, not findings. Passage 1 lies in a
changed paragraph but is single. Nothing is routed to `acceptance/ROUTED.md` from this run.

## Points the rules did not settle

1. **Reader 3's 4.2 grade carries a condition for another grade.** `ACCEPTANCE.md` reads a grade
   given on a stated condition as the grade for the case the fixture presents where the key says
   which case that is, and otherwise as unanswered; the key says no row carries a condition.
   Reader 3 gives Partial as its grade and states the condition only for Yes. Marked as Partial,
   the grade given; read either way (Partial, or unanswered) the item is a miss, so the mark does
   not turn on the point.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit bc6ae14, named before the readers started.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item but
  4.2, which is four of five. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: two (findings A and
  B). Not met.
- Passages named by two or more readers elsewhere: none.

## Findings applied

None at the time of marking; findings A and B are on the change's own text, to be fixed there
before a fresh cohort.

## Verdict

FAIL. Every keyed item passed its threshold and no miss counts against the document, but
findings A (clause 5.3, first paragraph) and B (clause 7.1, second paragraph) lie in text the
change wrote or altered, and each blocks.

## Answer sheets

Posted on the pull request: LINK PLACEHOLDER.
