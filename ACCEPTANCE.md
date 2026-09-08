# Acceptance test for changes to the specifications

Every change to `SPEC.md`, `DETECTOR-SPEC.md` or `TOOLING-SPEC.md` MUST pass this test before it
is published. It is the specifications' own defence: a document that only a strong reader can
follow is not a specification, and the readers that matter most, coding agents meeting the method
in a failing pipeline, are often the weakest. The test is run with a low-strength model so that
clarity is measured at the floor, not the ceiling.

## The cohort

- **At least five independent readers**, each a fresh instance of a low-strength model (the
  smallest current model in its family, for example Haiku), with no shared context and no
  access to the change history, the critique findings or each other.
- Each reader receives **only the changed document or documents** and the fixed question set
  below. Nothing else is read first.
- Readers are run **after** every stronger review has been applied. They are the last gate, not
  the first draft.

## The question set

Written before the run, with an **answer key** for every keyed question drawn verbatim from the
document, so that marking is mechanical. Each reader answers all of them.

1. **Restatement.** In their own words, what the document asks of its subject, in at most six
   bullets. Keyed against the list of MUST clauses: a bullet is correct when it names an
   obligation the document actually states.
2. **Load-bearing statements.** Three questions, fixed per document, each asking for one
   sentence and a quotation:
   - `SPEC.md`: what a practitioner does before fixing a defect, in order; who may baseline or
     suppress; what "conforms" means for a remediation.
   - `DETECTOR-SPEC.md`: what "conforms" means and whether a tool that predates the document can
     conform; what a detector must do about an inline suppression route; where a bundled rule's
     documentation must live.
   - `TOOLING-SPEC.md`: where conformance is measured; how a grade is assigned when parts come
     from different sources; how many grades a project that ships tooling has.
3. **Application.** A fixture case supplied with the questions, graded clause by clause with
   Yes, Partial or No and one line of reasoning. Keyed against the intended verdicts; a divergence
   counts against the document only when the reader's reasoning shows the clause was read
   differently, not when the fixture was misread.
4. **Ambiguity.** Any clause the reader had to read twice, with what would make it clearer, and
   any two passages that seem to disagree, quoted.
5. **Clarity.** A rating from 1 to 5 with one sentence.

## Pass criteria

The change passes when all of the following hold on a single run:

| Criterion                                                      | Threshold                                                                                                                                                                |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Load-bearing statements (question 2)                           | **5 of 5** readers correct on every one                                                                                                                                  |
| Restatement and application (questions 1 and 3)                | **At least 4 of 5** readers correct on each keyed item                                                                                                                   |
| A wrong answer traceable to the text                           | **None.** A miss whose reasoning quotes the document is a finding, whatever the count                                                                                    |
| Two passages that disagree (question 4b), named by two or more | **None outstanding.** A contradiction is a finding and blocks until fixed                                                                                                |
| A clause read twice (question 4a), named by two or more        | **A finding the editor must disposition** in the record, by a fix or a stated reason; it blocks only when a reader also answered a keyed question on that clause wrongly |
| Anything named by one reader                                   | Recorded; applied at the editor's discretion; does not block                                                                                                             |
| Clarity (question 5)                                           | Median **4 or above**, no reader **below 3**                                                                                                                             |

The asymmetry is deliberate. A load-bearing statement is the sentence the whole document exists
to make, and one reader in five getting it wrong means one agent in five will act on the wrong
reading; unanimity is the only acceptable result there. Everywhere else a single divergent reader
is more likely to be the reader than the text, so four of five is tolerated, but a miss that the
reader can justify from the document is always the document's fault.

Question 4a is treated as a difficulty signal rather than a defect, because the first three runs
of this test showed why: every document has a hardest clause, a low-strength reader asked to name
one will name it whether or not it misled them, and after the asked-for example was added the same
clause was named again with the same ask. A clause that was read twice and then answered correctly
by every reader has cost attention, not understanding. A clause that was read twice and answered
wrongly is ambiguous, and that is what blocks.

## After a failure

Fix the text, never the questions, and run a fresh cohort. Readers are not reused across runs.
The number of runs it took is recorded; a document that needed three runs is telling its editor
something.

## The record

Each published version's changelog entry states: the cohort size and model, the number of runs,
and the findings applied. A version with no such line has not been accepted and MUST NOT be
described as published. The question sets and answer keys live under `acceptance/` in this
repository so that a run can be repeated and compared.
