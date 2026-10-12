# Run 66: DETECTOR-SPEC.md, detector route rule, third run

- **Document**: DETECTOR-SPEC.md
- **Pull request**: [23](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/23), opened after the run from branch
  `editor/detector-route-rule`. The readers read commit 44fdd9e. Change: clause 7.1's detectable
  route is a bespoke rule the project writes for the detector under clause 4.1, with a paragraph
  on what detectable means; clause 8.1's gap duty falls only on a detector that declares a
  version; clause 5.3 says what the remainder is; clause 6.1 says it asks for the mechanism, a
  missing page failing clause 6.3, and that a path in the message is not enough on its own;
  section 2's table gains a Message row. Revised after run 63 in clause 5.3's sentence on a
  fuller report elsewhere.
- **Run within the pull request**: 3 (runs 60 and 63 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `5f991fd47d3b8d092464ca41bfdfd9f5707647f46e3b274929a0c5a44f5a50c4`) is
  `QUESTIONS.md`, `DETECTOR-SPEC.md` and `fixtures/lintomatic.md` at 44fdd9e, each after one
  `===== FILE: <name> =====` line, one blank line between files; the marker rebuilt it from that
  commit and it matched byte for byte.
- **Readers set aside**: none. Every reader's output has `is_error` false, subtype `success`,
  non-empty answer text and the cohort's model.
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

Question 1: correct bullets per reader 6, 6, 6, 6 and 6, one for each line of the key's list
(4.1; 4.2; 4.3; 5.1 to 5.4; 6.1 to 6.3; 7.1). Readers 2 and 3 add to their sixth bullet that a
detector conforms when it meets every MUST in sections 4 to 7, which the key says states what
conformance means and is neither correct nor wrong; the bullet still names 7.1. Reader 4's
fourth bullet says every finding goes in the command's output, which the key says names 5.3 and
is not marked wrong for the plural. Reader 5's fifth bullet adds that a project rule's
identifier is printed unaltered, which is 4.3 restated inside the 6.1 to 6.3 bullet. No bullet
asserts anything the key marks wrong.

Question 2: every reader states every required element of each item and quotes the document.
For 2a all five state that conformance is every MUST in sections 4 to 7 and that a detector
predating the document can conform, quoting section 8's definition or clause 8.1's "A Detector
that predates this document, or whose maintainer has never read it, MAY be graded Conforming on
evidence". For 2b all five name both things, disableable by configuration or detectable, and
that either is enough, quoting clause 7.1's "For each one it MUST do at least one of two
things, and either alone satisfies this clause". Readers 1, 3, 4 and 5 add that the bespoke-rule
way of detection is closed to a detector whose rules never see comments, which is the
document's own sentence and is not among the key's wrong assertions for 2b (removing or
forbidding the route, or requiring a reason). For 2c readers 1 to 4 state the installed copy, a
version tracked together and no network access, quoting the 6.2 and 6.3 headings; reader 5
states all three in its own words (citing the headings without quotation marks) and quotes
clause 6.3's "Every [Identifier] a [Bundled rule] can print MUST resolve, under clause 6.1, to a
page in that shipped documentation", which quotes the document.

Question 3: all five give every accepted grade. Readers 1 to 5 add caveats to 4.2 (the fixture
does not say `--only` prints finding lines) and 4.3 (no machine-readable format described);
reader 5 adds to 4.2 "If it does not, this is No", and reader 3 adds to its 6.3 No that the
grade would need revisiting if its reading of the fixture were wrong. Each gives the accepted
grade as its grade for the fixture as written, and the key says a reader who adds a caveat about
what the fixture does not say and still gives the accepted grade is correct. S8: all five say
Lintomatic does not conform, naming 6.3. 6.4: all five say it does not change the verdict,
because it is a SHOULD.

### Misses

None.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..44fdd9e adds,
rewords, moves or deletes a sentence in the paragraph, or changes a word, term or link in it.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Readers | Changed by the diff |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------- |
| 1   | Clause 6.1, "For a project's own Rule" paragraph: "Where the [Identifier] is itself a URL, as method clause 3.6 allows, the [Detector] prints that URL and has done what this clause asks" and "The lookup for such a [Rule] is an obligation on the project's assembled [Toolchain], under clause 4.2 of the [toolchain specification]" (1, could not check the documents cited); "What this clause forbids is a documentation path printed alongside a shorter [Identifier] that cannot be looked up on its own" (3 and 4, what "shorter" is measured against) | 1, 3, 4 | no                  |
| 2   | Clause 4.3, first paragraph: "A prefix the [Detector] adds from the invoking directory or the [Rule]'s location is derived from the file path. A namespace the [Rule author] assigns once in configuration is not." (no reason given)                                                                                                                                                                                                                                                                                                                            | 2       | no                  |
| 3   | Clause 6.3, the "dangling one" paragraph: "The failure to guard against is not the absent document but the **dangling one**", set against the clause's first paragraph, "Every Identifier a Bundled rule can print MUST resolve, under clause 6.1, to a page in that shipped documentation"; whether the MUST covers absent documentation                                                                                                                                                                                                                        | 3       | no                  |
| 4   | Section 2, "These are additional."; what the terms are additional to                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 3       | no                  |
| 5   | Clause 7.1, second paragraph: "That way is open only where the [Detector]'s [Rules] can see the route: a [Detector] whose [Rules] never see comments cannot make an ignore comment detectable this way"; what a bespoke rule can see                                                                                                                                                                                                                                                                                                                             | 4       | yes                 |
| 6   | Clause 7.2, first paragraph: "The [Detector] SHOULD NOT supply a default one, including each entry of a generated [Baseline]"; what "one" refers back to                                                                                                                                                                                                                                                                                                                                                                                                         | 5       | no                  |
| 7   | Clause 8.1, second paragraph: "a gap a [Practitioner] finds is recorded under the method's clause 3.2 in any case", set against the same paragraph's "falls only on a [Detector] that has one"; where the record is kept with no declaration                                                                                                                                                                                                                                                                                                                     | 5       | yes                 |

Notes, not passages: none.

## Findings and where they lie

- **Finding A, passage 1, clause 6.1 "For a project's own Rule" paragraph** (readers 1, 3 and
  4): the diff 9e914fe..44fdd9e changes the paragraph before it ("In both, ...") and the "For a
  Bundled rule" paragraph, but not this one; no reader naming it sets it against a paragraph the
  diff changed (reader 1 points at documents not supplied, readers 3 and 4 at the comparison in
  "shorter"). Not the change's text. Routed to `acceptance/ROUTED.md`, where the paragraph's row
  raised by run 63 is noted as raised again by run 66; does not block.

Passages 2 to 7 are each named by one reader: recorded, not findings. Passages 5 and 7 lie in
changed paragraphs but are single.

## Points the rules did not settle

1. **Finding A, reader 1: a passage named for a reference to a document not supplied.** Reader 1
   quotes two sentences of the paragraph with the clause number, which `ACCEPTANCE.md` defines
   as naming a passage, and its confusion is that method clause 3.6 and the toolchain
   specification were not given. The rule that a remark that another document was not supplied
   is a note covers a remark "not about a passage of the document"; this remark is attached to
   quoted passages. Marked as the open-point rule says: an open point on whether a reader named
   a passage counts the passage. The finding does not turn on this point, since readers 3 and 4
   name the same paragraph, and the finding is routed either way.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit 9907492, named before the readers started.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: none. Met.
- Passages named by two or more readers elsewhere: one (finding A), routed to
  `acceptance/ROUTED.md`.

## Findings applied

None at the time of marking; finding A is for `acceptance/ROUTED.md`.

## Verdict

PASS. Every keyed item passed its threshold, no miss counts against the document, and the one
finding lies outside the text the change wrote or altered.

## Answer sheets

Posted on the pull request in three comments:
[the command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/23#issuecomment-6124587014),
[the answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/23#issuecomment-6124587505) and
[the prompt](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/23#issuecomment-6124587875).
