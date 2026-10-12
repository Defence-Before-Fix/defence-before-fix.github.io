# Run 74: DETECTOR-SPEC.md, semantic detectors, fifteenth run

- **Document**: DETECTOR-SPEC.md
- **Pull request**: 14, open on branch `editor/semantic-detectors`. The readers read commit
  f7e55e1. Change: a new clause 8.2, that a verdict on a detector names its kind, semantic,
  syntactic or textual, in each configuration it grades; section 9's sentence on that
  obligation; section 2's table row for the three kinds. Since run 71 the branch has merged
  `editor/detector-route-rule` (pull request 23), whose rework of clauses 5.3, 6.1, 7.1 and 8.1
  and whose Message row in section 2 are that change's text, not this one's; clause 8.2's
  sentence on which configuration's kind is named was reworded after run 71.
- **Run within the pull request**: 15 (runs 19 to 30, 70 and 71 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `003d030ade886b2008da3abc90e75d8c62be8f02f79c3b4aec05818379bcc550`) is
  `QUESTIONS.md`, `DETECTOR-SPEC.md` and `fixtures/lintomatic.md` at f7e55e1, each after one
  `===== FILE: <name> =====` line, one blank line between files; the marker rebuilt it from that
  commit and it matched byte for byte.
- **Readers set aside**: none. Every reader's output has `is_error` false, subtype `success`,
  non-empty answer text and the cohort's model; each sheet is that output's `result`.
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  marking instruction and its agent definition, having seen neither the drafting nor the review.

## Marks

Readers are numbered 1 to 5 as their sheets are. Question 3 columns: the eleven clauses, then
the two answers (S8 conformance under section 8, 6.4 whether clause 6.4 changes the verdict).

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | S8  | 6.4 |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 2      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 3      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 4      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 5      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |

Question 1: readers 1, 3 and 4 name, one bullet each, the key's lines for 4.1; 4.2; 4.3; 5.1 to
5.4; 6.1 to 6.3; and 7.1. Reader 2 names the same six, its sixth bullet adding what conformance
means, which the key says is neither correct nor wrong; its fourth says every finding must
appear in the command's output, which the key says is not marked wrong for the plural. Reader 5
names 4.1 with 4.2, 4.3, 5.1 to 5.4, 6.1 to 6.3 and 7.1, and its sixth bullet says any verdict
on a detector must name its kind, which names the 8.2 line and does not put the duty on the
detector. No bullet asserts anything the key marks wrong.

Question 2: every reader states every required element of each item and quotes the document.
2a: all five state that conformance is every MUST in sections 4 to 7 and that a detector
predating the document can conform, quoting section 8's definition and clause 8.1's "A Detector
that predates this document, or whose maintainer has never read it, MAY be graded Conforming on
evidence". 2b: all five name both things, disableable by configuration or detectable, and that
either alone is enough, quoting clause 7.1's "For each one it MUST do at least one of two
things, and either alone satisfies this clause" (reader 2 with an ellipsis inside the sentence,
reader 3 ending in an ellipsis; each run before the ellipsis is well over six words). 2c: all
five state that the documentation ships with the rule in the installed copy, at a version
tracked together, and resolves without network access, quoting the 6.2 and 6.3 headings (reader
4 also 6.3's first sentence); readers 3 and 5 add that a website does not satisfy it, which is
not among the key's wrong assertions.

Question 3: every reader gives the accepted grade on all eleven clauses, several with caveats on
what the fixture does not say (what `--only` prints under 4.2, machine-readable formats under
4.3), which the key accepts since no row carries a condition. S8: all five say Lintomatic does
not conform, naming 6.3 or the two undocumented bundled rules; all five say the verdict cannot
name Lintomatic's kind because the fixture does not say it, and that this leaves the
conformance finding standing, which the key does not mark. 6.4: all five say it does not change
the verdict, because it is a SHOULD.

### Misses

None. No answer matches a wrong reading the key names for question 1 or question 3.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "this change's text" means a paragraph the diff
d67174c..f7e55e1 adds, rewords, moves, deletes a sentence from, or changes a word, term or link
in. The diff 9e914fe..f7e55e1 shows this change and the merged detector change together.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                                                                              | Readers | This change's text |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------ |
| 1   | Clause 8.2, first paragraph: "The kind named is the one the [Detector] has in a configuration that needs no hosted service and no licence tier." Reader 2: whether a verdict grading a hosted configuration names the local kind or the hosted one; reader 3: whether it means the strongest kind available locally or the kind of whichever local configuration is named; reader 4 gives no reason | 2, 3, 4 | yes                |
| 2   | Clause 6.1, paragraph "For a project's own Rule": "Where the [Identifier] is itself a URL, as method clause 3.6 allows, the [Detector] prints that URL and has done what this clause asks."; the method specification was not supplied (point 1 below)                                                                                                                                              | 1       | no                 |
| 3   | Clause 8.1, first paragraph: "the method's clause 3.2", given with clause 8.1 as another reference to an unsupplied document (point 1 below)                                                                                                                                                                                                                                                        | 1       | no                 |
| 4   | Clause 6.3, first paragraph: "One [Identifier] that does not resolve fails this clause, however many others do. A page per [Identifier] satisfies this; a page per family of [Identifiers] MAY be used instead, under clause 6.5."; whether a prose-only family page meets 6.3's MUST                                                                                                               | 5       | no                 |
| 5   | Clause 6.5, first paragraph: "Such a page SHOULD let the check clause 6.4 asks for confirm that each member resolves to it."; set against passage 4                                                                                                                                                                                                                                                 | 5       | no                 |
| 6   | Clause 6.5, table row "Says in prose that everything under `LM-01` is documented here": "No: a person can infer it, a check cannot"; set against passage 4                                                                                                                                                                                                                                          | 5       | no                 |
| 7   | Clause 6.1, paragraph "In both, the mechanism is keyed on the Identifier exactly as printed", described, not quoted: "6.1 requires a lookup keyed on the identifier exactly as printed"; set against passage 4 (point 2 below)                                                                                                                                                                      | 5       | no                 |

Notes, not passages: reader 1's general remark that it took references to the method and
toolchain specifications on trust, not having been given them.

## Findings and where they lie

- **Finding A, passage 1, clause 8.2 first paragraph** (readers 2, 3 and 4): the diff
  d67174c..f7e55e1 adds the whole of clause 8.2, and the sentence the readers quote was reworded
  after run 71. Text the change wrote; blocks.

No other passage is named by two or more readers, so nothing is routed to
`acceptance/ROUTED.md` from this run. Passages 2 to 7 are each one reader's and are recorded
only.

## Points the rules did not settle

1. **Reader 1's question 4: passages or a note.** Its subject is that the method specification
   was not given, which reads as a note, but it quotes a sentence of clause 6.1 (passage 2) and
   names "the method's clause 3.2" with clause 8.1, a four-word quotation that occurs in both
   paragraphs of 8.1. Counted, by the open-point rule (an open point on whether a reader named a
   passage counts the passage), as naming clause 6.1's paragraph and clause 8.1's first
   paragraph, where the words first occur; the general remark is recorded as a note. No finding
   turns on this point: no other reader names either paragraph.
2. **Reader 5's description of clause 6.1.** It gives a clause number and a description, not a
   quotation, that identifies the sentence "In both, the mechanism is keyed on the Identifier
   exactly as printed"; counted as a passage by the open-point rule. It is not the paragraph
   reader 1 names in clause 6.1, so no finding turns on it.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit bc6ae14, named before the readers started. `ACCEPTANCE.md`,
`acceptance/README.md` and `acceptance/runs/README.md` are identical at bc6ae14 and f7e55e1.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none. Met.
- Passages named by two or more readers in text the change wrote or altered: one (finding A,
  clause 8.2 first paragraph). Not met.
- Passages named by two or more readers elsewhere: none.

## Findings applied

None at the time of marking.

## Verdict

FAIL. Every keyed item passes, but finding A, named by readers 2, 3 and 4, lies in the first
paragraph of clause 8.2, which the change wrote: the sentence "The kind named is the one the
Detector has in a configuration that needs no hosted service and no licence tier."

## Answer sheets

Posted on the pull request: LINK TO BE ADDED.
