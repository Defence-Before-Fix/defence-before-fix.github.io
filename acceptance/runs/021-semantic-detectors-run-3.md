# Run 21: SPEC.md, semantic detectors, third run in pull request 14

- **Document**: SPEC.md
- **Pull request**: [14](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14),
  branch `editor/semantic-detectors` at 3aefdd1, the commit the readers were given; the question
  set, key and fixture read at the same commit
- **Cohort**: five readers, model alias `haiku`; every reader reported `claude-haiku-5-5`, as the
  editor supplied in the cohort's model list and as each reader's own JSON output shows
- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, which only reattaches the session's credential and passes
  arguments through verbatim, in a fresh empty directory made by `mktemp -d` outside any
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt is the question set, the document and the fixture at
  3aefdd1, in that order, each preceded by one `===== FILE: <name> =====` line, with nothing
  else added apart from one blank line between the end of each file and the next file's marker
  line.
- **Managed (policy) settings**: none; the machine applies no managed settings to the readers and
  no managed settings file is present, as the editor supplied
- **The rest of the isolation**: attested by the editor
- **Readers set aside**: none. Every sheet has answer text, no process reports an error
  (`is_error` false, subtype `success`), and every reported model is the cohort's model. The
  editor reports no reader set aside for a cause the sheets cannot show.
- **Run within the pull request**: 3, counting void runs; runs in the pull request so far: 3 (19,
  20 and this one). Run 22, on DETECTOR-SPEC.md, is made at the same time and does not bear on
  this document.
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) dispatched with
  the editor's instruction and its agent definition, `.claude/agents/dbf-spec-editor.md`, having
  seen neither the drafting nor the review. It read `ACCEPTANCE.md` and
  `acceptance/runs/README.md` in this worktree, which differ from commit 204f95b only by this pull
  request's question-set line adding 2d for SPEC.md; the document, question set, key and fixture
  at 3aefdd1; runs 19 and 20; and, for the fourth pass-criteria row, SPEC.md at 5b6093f, the
  document run 19 read.

## Marks

`ok` is correct, `miss` is a miss; `T` marks a miss traceable to the text. Judgements J1 to J8
are set out below.

| Reader | Q1      | 2a     | 2b  | 2c  | 2d     | 3.1     | 3.2     | 3.3            | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 | Q4 passages |
| ------ | ------- | ------ | --- | --- | ------ | ------- | ------- | -------------- | --- | --- | --- | ----------- | ------- | --------- | ----------- |
| 1      | correct | miss T | ok  | ok  | miss T | Partial | Partial | Yes ok         | No  | No  | No  | ok          | ok      | ok        | four        |
| 2      | correct | ok     | ok  | ok  | miss T | Partial | Partial | Partial miss T | No  | No  | No  | ok          | ok      | ok        | four        |
| 3      | correct | miss T | ok  | ok  | miss T | Partial | Partial | Partial miss T | No  | No  | No  | ok          | ok      | ok        | two         |
| 4      | correct | miss T | ok  | ok  | miss T | Partial | Partial | Yes ok         | No  | No  | No  | ok          | ok      | ok        | two         |
| 5      | correct | ok     | ok  | ok  | miss T | Partial | Partial | Yes ok         | No  | No  | No  | ok          | ok      | ok        | three       |

Every grade under 3.1, 3.2 and 3.4 to 3.6 is one the key accepts, and every 3.1 grade of Partial
notes that no independent search technique is recorded.

### Question 1

Five of five correct. Every sheet has at least four bullets naming obligations the key lists, and
no bullet asserts an obligation the document does not state. Reader 3's "Write a custom rule" is
Appendix A's own wording ("Write a custom [Rule] that detects the [Class]"), and the "only then"
of readers 1 and 4, that the original defect is fixed last with a reproducing test, is Appendix
A's closing sentence.

### Question 2

Every reader quoted words of the document for every item, so every miss here is traceable to the
text.

- **2a**, two of five (readers 2 and 5). Every reader quotes the section 2 sentence "When it can,
  building the [Defence] is not optional and MUST be attempted before the [Defect] is fixed.", which
  states no order and no sweep, so each answer stands or falls on its sentence.
  - Reader 1: "attributes it to a class, builds and proves a rule for that class, then sweeps and
    counts before fixing (clauses 3.1 to 3.4). The original defect is fixed last"; the fix of
    every instance is not stated, and naming clause 3.4 does not state it.
  - Reader 2: class, "builds and proves the net", "sweeps and fixes every instance", in order;
    correct (J2).
  - Reader 3: "builds the defence before fixing the defect"; no class, no proof, no sweep, no fix
    of every instance.
  - Reader 4: "attributes the defect to a class and attempts the rule before fixing the defect, in
    the order of section 3"; no proof, no sweep, no fix of every instance.
  - Reader 5: class, rule, proof, "sweep and fix every instance", in order; correct.
- **2b**, five of five. Readers 1, 2 and 3 say the owner is a human; readers 4 and 5 say "the
  owner of the codebase" and "the owner" (J4). All five quote the key's section 4 sentence and say
  an agent may not.
- **2c**, five of five. Readers 1, 4 and 5 state the reviewer's rerun of the red and green runs,
  reader 4 in its quotation of section 7's closing paragraph; readers 2 and 3 state reproduction,
  not the report (J3). No reader accepts the pull request description as the verdict.
- **2d**, none of five. No answer, sentence and quotation read together, states the two grounds
  on which a weaker kind is allowed: each says only that there are two.
  - Reader 1: "A weaker kind is allowed only on one of two grounds"; its quotations give the order
    and the record with both places, not the grounds.
  - Reader 2: "A weaker kind is allowed only on one of two grounds"; no place for the record of
    the grounds, only for naming the detector and kind (J5).
  - Reader 3: "A weaker kind is allowed only on two grounds"; its second quotation stops before
    the places (J5).
  - Reader 4: "only on one of two grounds", quoting "A weaker kind is allowed on one of two
    grounds only:"; nor does its answer state the order semantic, syntactic, textual, and it names
    no place (J5).
  - Reader 5: "only on one of two grounds"; no place (J5).

### Question 3

- **3.3**, three of five (readers 1, 4 and 5, Yes). Reader 1's caveat, that the description does
  not show how the fixture was excluded from the enforced run, leaves its grade at Yes.
  - Reader 2 grades Partial because "Part B is breached: the `Report::render()` inline ignore is
    a suppression, not a narrowing", and also grades 3.4 No on it. Its reasoning states what the
    document requires of Part B, so the miss is traceable. Part B now opens by saying such an
    ignore is a [Suppression] "and clauses 3.4 and 3.5 and section 4 govern it, not this clause";
    the key's excuse does not cover a reader who attributes it to both (J6).
  - Reader 3 grades Partial because "the enforced run reports the fixture as one of its five
    findings, and Part C says the enforced run 'does not report it'". It quotes clause 3.3's
    sentence on a [Rule]'s [Fixtures], so the miss is traceable.
- **Remediation**: five of five say it does not conform, each naming at least one failing clause
  the key accepts.
- **Defence**: five of five say it does not conform, each naming 3.6.
- **Section 4**: five of five name the inline ignore on `Report::render()`. Readers 1, 2, 4 and 5
  also raise the unbuilt wider rule as a second or less clear decision, which the key accepts
  alongside it.

### Judgements made in marking

Where the rules leave a judgement open, the stricter reading, the one that records more misses or
more passages, is taken. Where a rule settles the point, the record says which.

- **J1. The sentence.** Where a reader wrote more than one sentence before its quotation, all of
  that text is read with the quotation as the answer. No mark turns on it: in each such case the
  quotation states what the later sentences add, or the answer misses an element no sentence
  states.
- **J2. "The net" (reader 2, 2a).** Settled by the rule that an element may be stated in the
  document's words: "Build the net" and "Prove the net by making the rule fire" are the headings
  of clauses 3.2 and 3.3, and the net is the [Rule] in a [Detector]. Read otherwise, reader 2
  would add one traceable miss on 2a; the verdict would not change.
- **J3. "Reproduction" (readers 2 and 3, 2c).** Settled by the rule that each element is read
  for its gist, with sentence and quotation together: both quotations are section 7's sentence
  that the verdict "rests on reproduction, as this section closes by requiring, not on the
  report", and the closing paragraph it points to is the red and green reruns. The key's own
  condition for a wrong answer is one that omits reproduction.
- **J4. "The owner" (readers 4 and 5, 2b).** Settled by the rule that a defined term used in its
  defined sense states what it means: [Owner] is "Always a human", and section 4 and the key
  both call it the owner of the codebase. Reader 4's question 4 doubt whether "whoever owns the
  codebase" is the defined term is not read into its 2b answer, which is its sentence and
  quotation; that doubt is recorded as a passage below.
- **J5. 2d's element (iii) needs a place named.** The key says naming one of the two places "is
  enough", read as requiring at least one, as run 19 read it. No mark turns on it: every sheet
  already misses (ii).
- **J6. The 3.3 excuse is read as written**, covering a reader who attributes the suppression to
  3.3 rather than 3.4, not one who attributes it to both, as run 19 read it.
- **J7. Reader 1's "its owner list".** Reader 1's first passage quotes table row 3.1 and section
  4's first practitioner bullet, and describes section 4's owner list as covering "only the wider
  rule left unbuilt because no instance exists". The description is read as naming the whole
  owner list, its lead-in included, so it covers the wider-rule bullet and the line "Decisions
  that MUST go to whoever owns the codebase:". The narrower reading, the wider-rule bullet alone,
  would leave the lead-in to reader 4 alone and remove one finding below. Reader 1's other
  descriptions are read the same way: "the two grounds" covers both items of clause 3.2's list,
  and "Clause 3.4, first paragraph against the Fixture paragraph" covers 3.4's opening paragraph
  as well as the scope paragraph it quotes. Reader 3's "on the second ground" covers the second
  item of that list.
- **J8. Clause labels.** A clause number given with a quotation, as question 4 asks, is read as
  the quotation's label, not as naming the whole clause. Settled by the rule on quoting: naming a
  clause number is not quoting, and question 4 asks for a quotation "with its clause number".

## Passages quoted as confusing

Same passage as `ACCEPTANCE.md` defines it: sentences in common, or the same paragraph; a list
item or table row is its own paragraph.

| Passage                                                               | Clause                   | Readers          | Words quoted, verbatim, or the description used                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------- | ------------------------ | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The two grounds and the paragraph after them, "For the second ground" | 3.2                      | four: 1, 2, 3, 5 | 1: "Where no [Detector] of that kind can reach it, the kind cannot express the [Rule], and the first ground holds." and "the two grounds" (J7). 2: "naming the [Detectors] of the stronger kind that were considered, on the [Rule]'s [Remediation docs] and in the description of the commit that adds the [Rule], moves it to another [Detector], or first records the grounds." 3: "The language has such a [Detector] when the project already runs it or the language's own [Detector] ecosystem offers it, the same check section 2 asks for before a [Toolchain] gap is recorded." and "the second ground" (J7). 5: "Where those extension points cannot reach the construct a [Rule] is about, that [Detector] cannot express the [Rule]."; "the stronger kind cannot express the [Rule]" (the first ground's list item); "A stronger configuration of a [Detector] the project runs is one; a [Detector] or configuration of the stronger kind available only through a hosted service or a licence tier is not." Every sentence quoted lies in the one paragraph that begins "For the second ground"; the first list item is named by readers 1 and 5, the second by readers 1 and 3 |
| The bullet on leaving the next wider rule unbuilt                     | 4                        | three: 1, 2, 5   | 2: "Leaving unbuilt the next wider [Rule] that clause 3.1 required the [Practitioner] to name, where it was rejected because no [Instance] of it exists today rather than because the [Hazard] cannot arise there." 5: "it reaches no further than the one wider [Rule] already on the record." 1: by description, "its owner list covers only the wider rule left unbuilt because no instance exists" (J7)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Table row 3.1, the fourth column                                      | 3 (given as 3.1 by both) | two: 1, 2        | 1: "Whether the next wider [Rule] is built". 2: "Whether the next wider [Rule] is built, and whether the [Rule] stays narrower than the search showed"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| The lead-in to the owner's decisions                                  | 4                        | two: 1, 4        | 4: "**Decisions that MUST go to whoever owns the codebase:**", set beside the Owner entry (below). 1: by description, "its owner list" (J7)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| The Owner entry                                                       | 1, Owner                 | one: 4           | "Whoever holds authority over a project's [Exceptions] and [Calibrations]. Always a human." (quoted after "**Owner**: ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| The practitioner's first decision                                     | 4                        | one: 1           | "What [Class] the [Defect] belongs to, and where its bounds sit (clause 3.1)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| The lower bound, the exact value or name                              | 3.1                      | one: 1           | "A [Rule] drawn to the exact value or name found in the [Defect] is the same [Narrowing] however it is spelt."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| The clean run of the rule and saturation                              | 3.1                      | one: 3           | "A clean run of the [Rule] is therefore not evidence of saturation either: "the [Rule] found nothing the reading had missed" is one technique and a [Rule] run, not two techniques, and the stopping criterion cannot be applied to it."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| What is in scope of the sweep, and a rule's own fixtures              | 3.4                      | one: 1           | "Whether vendored dependencies, generated code and test [Fixtures] are in scope is the project's decision" and "A [Rule]'s own [Fixtures] under clause 3.3 are never [Instances]."; by description, also 3.4's first paragraph (J7)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| The three ways out of the method                                      | 2                        | one: 4           | "There are three ways out of the method and they are recorded differently." and "a mechanism gap under clause 3.2, and the [Rule] is still built"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| What a conforming remediation is                                      | 7                        | one: 2           | "A remediation [Conforms] if all six clauses of section 3 were followed for that [Defect], and the verdict that they were rests on reproduction, as this section closes by requiring, not on the report."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

Readers' accounts of what they could not tell are recorded with the passage they attach to and
are not suggestions; none of the sheets proposes a change.

**Earlier passages (the fourth row).** Run 19 found four passages named by two or more readers.
As the paragraphs read in the changed document:

- Clause 3.2's extension-points sentence lay in the paragraph that now begins "For the second
  ground". Readers 1, 2, 3 and 5 of this cohort name sentences of that paragraph, so that
  finding is not cleared.
- Clause 3.1's level paragraph, now "The bounds say how broad the [Class] is", is named by no
  reader. Cleared.
- Section 2's "Attempt rather than pre-judge" paragraph is named by no reader; reader 4's section
  2 passage lies in the next paragraph, "There are three ways out". Cleared.
- Clause 3.4's "Fix them all" paragraph is named by no reader; reader 1's clause 3.4 passage lies
  in the scope paragraph and, by description, the opening paragraph. Cleared.

No sentence kept from one of those paragraphs is named elsewhere in the document.

**Editor's note on the marker's instruction.** The instruction for this run asked for the stricter
reading wherever the rules leave a judgement open, which the process at 204f95b had replaced with
the judgement of a careful reader. The verdict does not turn on it: the findings that fail the run
rest on rules, not on those judgements.

## Findings applied

Applied to the text, never to a question, threshold, fixture or key, in 72f1679 and the commit after
it that settles a review of those edits (key quotations kept verbatim in c5bfd10). SPEC.md: clause
3.2 states both grounds for a weaker kind in the one sentence that allows it, and its paragraph on
the second ground is short and plain; section 2 names the order (attribute, build, prove, sweep,
then fix every instance) where it says the defence comes before the fix; clause 3.3 Part B says an
ignore left over an instance that carries the hazard is not this clause's matter, and Part C says
which run it means; section 4's bullet on the next wider rule, the map's row 3.1 and section 4's
lead-in say plainly what the decision is and who takes it. A fresh cohort follows.

## Process change

Made under a process change before it merged: yes, pull request 13 at commit 204f95b, named
before the readers started.

## Verdict

**FAIL.** Against the criteria in `ACCEPTANCE.md`:

- Load-bearing statements: not met. 2a two of five (readers 1, 3 and 4 miss), 2b five of five,
  2c five of five, 2d none of five: no reader states the two grounds for a weaker kind.
- Restatement and application: not met on 3.3, three of five (readers 2 and 3 miss); question 1
  and every other keyed item five of five.
- Misses traceable to the text, each a finding: 2a for readers 1, 3 and 4, each relying on the
  section 2 sentence "When it can, building the [Defence] is not optional and MUST be attempted
  before the [Defect] is fixed."; 2d for all five readers, on clause 3.2's grounds for a weaker
  kind; 3.3 for reader 2, on Part B and the inline ignore; 3.3 for reader 3, on Part C's
  "the enforced run does not report it".
- Passages found confusing by two or more, each a finding that blocks until the text is changed
  and a fresh cohort no longer names it: clause 3.2's two grounds and the "For the second ground"
  paragraph (four readers), which is also run 19's extension-points finding, not cleared;
  section 4's bullet on leaving the next wider rule unbuilt (three); the fourth column of table
  row 3.1 in section 3 (two); section 4's lead-in "Decisions that MUST go to whoever owns the
  codebase:" (two, on J7).
- Single-reader notes, recorded: the Owner entry (reader 4); section 4's first practitioner
  bullet (reader 1); clause 3.1's lower-bound sentence on the exact value or name (reader 1);
  clause 3.1's clean-run sentence (reader 3); clause 3.4's scope paragraph and opening paragraph
  (reader 1); section 2's three ways out (reader 4); section 7's conforming remediation (reader
  2).

Answer sheets, the reader prompt, the command and the marker's instruction: posted on pull request 14 in [comment 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090464782), [comment 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090465417), [comment 3](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090465825), [comment 4](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090466147).
