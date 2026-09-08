# Answer key for SPEC.md

Marked against the document at the version named in the changelog entry that records the run.
Quotations below are from the document; when a clause is reworded, update the quotation here in
the same commit.

## 1. Restatement

A bullet is correct when it names one of these obligations. Four or more correct bullets, and no
bullet asserting an obligation the document does not state, is a correct restatement.

- Attribute the defect to a class, bounded on both sides, with the hazard stated (3.1).
- Express the class as a rule in a detector that reads code, never a test (3.2).
- Prove the rule fires, against the instance or a fixture, in a commit of its own (3.3).
- Sweep the whole codebase, record the count, then fix every instance (3.4).
- Make the rule permanent and blocking in the project's checks (3.5).
- Make the failure message terse, with a stable identifier resolving to documentation versioned
  with the rule (3.6).

Wrong if it asserts: the practitioner fixes the reported instance first and defends afterwards;
a test may serve as the detector; an agent may baseline the remaining instances.

## 2. Load-bearing statements

- **2a.** Attribute the defect to a class, express it as a detector rule, prove the rule fires,
  then sweep and fix every instance, in that order. Key quotations, section 3: "Six clauses, in
  order."; 3.4: "The Practitioner MUST run the Rule across the entire codebase and record the
  total Instance count before fixing anything, and MUST then fix every Instance found rather
  than only the one". An answer that has the fix before the rule, or the sweep before the proof,
  is wrong.
- **2b.** The owner of the codebase, always a human; an agent may not. Key quotation, section 4:
  "An Agent MUST NOT Baseline, suppress or knowingly leave an Instance unfixed on its own
  authority, whatever the Instance count turns out to be." An answer that lets the practitioner
  decide because the count was small, or because the project recorded no rule, is wrong (the
  default owner paragraph in the terminology entry for Owner still requires a recorded decision).
- **2c.** All six clauses of section 3 were followed for that defect, and the verdict rests on the
  reviewer reproducing the red and green runs, not on the report. Key quotations, section 7: "A
  remediation Conforms if all six clauses of section 3 were followed for that Defect."; "A
  verdict on a remediation or a Defence MUST rest on reproduction, not on the report". An answer
  that accepts the pull request description as the verdict is wrong.

## 3. Application: the ledger remediation

| Clause | Intended verdict   | Reasoning the fixture supports                                                                                                                                                                             |
| ------ | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3.1    | Yes, Partial or No | Class, hazard and the next wider rule are named; Partial or No is accepted where the reader notes that no independent search technique is recorded, which step 2 and the record 3.1 requires both call for |
| 3.2    | Yes                | A rule in the project's static analyser, reading code, not a test                                                                                                                                          |
| 3.3    | Yes                | Commit B is red on the fixture and the originating instance and survives as its own commit                                                                                                                 |
| 3.4    | No or Partial      | Five findings recorded, but one instance was left unfixed behind an inline ignore on the agent's own authority; Partial accepted where the reasoning names that suppression                                |
| 3.5    | Partial or No      | The rule is permanent and blocking, but the suppression was not a recorded decision                                                                                                                        |
| 3.6    | No or Partial      | The message is terse and carries an identifier, but the documentation lives on a wiki, not versioned with the rule; Partial accepted where the reasoning quotes the versioning sentence                    |

Section 7: the **remediation does not conform**, because 3.4 and 3.6 were not followed. The
**defence does not conform** either, because 3.6 fails; a reader who says the defence conforms
because the sweep is what failed has missed 3.6 and that counts against the document only if the
reasoning quotes the section 7 definition of a conforming defence.

Section 4: the **inline ignore on `Report::render()`** was the owner's decision, not the
practitioner's. An answer naming instead the decision not to build the wider rule is half right:
that is also listed in section 4 as the owner's to take, and an answer naming both is correct.
An answer naming neither is wrong.

A reader who grades 3.6 Yes because the URL resolves has read the versioning sentence of 3.6
differently, which counts against the document; a reader who grades 3.4 Yes has misread the
fixture. A reader who attributes the suppression to 3.3 rather than 3.4 has read the narrowing
passage of 3.3 as covering it, which is a fair reading and is not marked wrong.

## 4. Confusion

No keyed answer. Record every passage quoted. Two or more readers quoting the same passage is a
finding that blocks until the text is changed and a fresh cohort no longer quotes it. What to
change is the editor's decision; the reader is not asked and any suggestion it volunteers is
discarded unread.
