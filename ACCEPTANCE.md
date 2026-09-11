# Acceptance test for changes to the specifications

Every change to `SPEC.md`, `DETECTOR-SPEC.md` or `TOOLING-SPEC.md` MUST pass this test before it
is merged to `next`, and so before it is published. It is the specifications' own defence: a
document that only a strong reader can follow is not a specification, and the readers that
matter most, coding agents meeting the method in a failing pipeline, are often the weakest. The
test is run with a low-strength model so that clarity is measured at the floor, not the ceiling.

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

4. **Confusion.** Any passage the reader found confusing on its one reading, quoted with its
   clause number, and nothing else: not what would make it clearer, not a proposed change.

The cohort settles one thing: is the document clear, coherent and comprehensive. A reader getting
everything right after one reading proves it; a reader getting confused fails it. The document
is designed by its editor to resolve the comprehension failures the cohort shows; the cohort is
the acceptance layer, not the designer.

## What the cohort is not asked

The cohort may point at what it found confusing. It is never asked to rate the document, to say
what would make a passage clearer, or to suggest any change, and a suggestion it volunteers is
discarded unread. A low-strength reader is there to show whether the text can be followed; it is
not there to design the text, and a document shaped by what its weakest reader says it wants is
a document designed by that reader. The signals this test takes from the cohort are a keyed
answer missed, a wrong verdict reasoned from the document, and a passage pointed at; what to do
about any of them is the editor's decision. An earlier version of this test asked the reader
what would make a clause clearer and for a clarity rating; both were removed on the author's
instruction for that reason, and neither is reinstated.

## Pass criteria

The change passes when all of the following hold on a single run:

| Criterion                                              | Threshold                                                                                                        |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Load-bearing statements (question 2)                   | **5 of 5** readers correct on every one                                                                          |
| Restatement and application (questions 1 and 3)        | **At least 4 of 5** readers correct on each keyed item                                                           |
| A wrong answer traceable to the text                   | **None.** A miss whose reasoning quotes the document is a finding, whatever the count                            |
| A passage found confusing (question 4), by two or more | **None outstanding.** It is a finding and blocks until the text is changed and a fresh cohort no longer names it |
| Anything from one reader only                          | Recorded; applied at the editor's discretion; does not block                                                     |

The asymmetry is deliberate. A load-bearing statement is the sentence the whole document exists
to make, and one reader in five getting it wrong means one agent in five will act on the wrong
reading; unanimity is the only acceptable result there. Everywhere else a single divergent reader
is more likely to be the reader than the text, so four of five is tolerated, but a miss that the
reader can justify from the document is always the document's fault.

## The bar only moves up

No criterion in this document is ever relaxed to let a change through. If the cohort is confused,
the test is working and the text is wrong; the fix is to the text, never to the threshold, the
question, the fixture or the key. A threshold may be raised, a keyed question may be added, and a
key may be corrected where it misquoted the document; none of those makes a failing run pass. The
one time a threshold was relaxed, after three runs, the relaxation was reversed on the author's
instruction and is recorded here so that it is not tried again. Removing the clarity rating and
the request for suggestions was not a relaxation: it changed what the cohort is asked, not how
strictly an answer is marked.

## After a failure

Fix the text, never the questions, and run a fresh cohort. Readers are not reused across runs.
The number of runs it took is recorded; a document that needed three runs is telling its editor
something.

## When it runs

Once per pull request, on the final text, after the editor's rewrite and any key update. It is
the last gate before the merge to `next`, so that every change on `next` is one the cohort has
accepted, and the release branch needs no cohort of its own unless it changes specification text.
A wording change after the run means a fresh run; readers are never reused.

## The record

Each run has a file under `acceptance/runs/`, named `NNN-<slug>.md` with `NNN` the next number in
the one sequence shared by the three documents, stating: the document, the pull request and the
commit read, the cohort size and model, the run number in that pull request, the marks per
reader per question, the findings applied, and whether it passed. The changelog line for the
change names the file. CI refuses a specification change whose pull request adds no run file;
it checks for at least one, and a pull request that changes two documents adds a run for each.

Each published version's changelog entry carries the lines of the changes it contains, so a
version's cohort record is the set of runs those lines name. A version with no such line has not
been accepted and MUST NOT be described as published. The question sets and answer keys live
under `acceptance/` in this repository so that a run can be repeated and compared.
