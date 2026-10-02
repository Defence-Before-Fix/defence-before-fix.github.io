# Run 16: SPEC.md, deferral clause, first run

- **Document**: SPEC.md
- **Pull request**: 5, editor's branch `editor/pr-5` at e3cd120
- **Cohort**: five fresh Haiku readers, no shared context
- **Run within the pull request**: 1
- **Verdict**: FAIL on load-bearing statement 2c

## Marks

| Reader | Q1 restatement | 2a  | 2b  | 2c  | 3.1 | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 | Q4 confusion    |
| ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --------- | --------------- |
| 1      | correct        | ok  | ok  | no  | ok  | ok  | ok  | ok  | ok  | ok  | ok          | ok      | ok        | none            |
| 2      | correct        | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok          | ok      | ok        | 3.3 Part B, one |
| 3      | correct        | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok          | ok      | ok        | none            |
| 4      | correct        | ok  | ok  | no  | ok  | ok  | ok  | ok  | ok  | ok  | ok          | ok      | ok        | none            |
| 5      | correct        | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok          | ok      | ok        | 3.3 Part B, one |

## The failure

Readers 1 and 4 answered 2c with the six-clause condition and nothing about reproduction. The
reproduction requirement sits nine paragraphs below the conformance definition in section 7, and
both readers quoted the definition and stopped. Neither reasoning quotes the document wrongly;
the document let them stop early.

## Confusion

Two readers quoted different sentences of clause 3.3 Part B, the narrowing and suppression
distinction: one the "Narrowing that excludes code which does carry the Hazard is a Suppression"
sentence, one the "The decision comes first" paragraph. Not the same passage, so recorded as two
single-reader notes and not a blocking finding. No reader quoted the new deferral paragraph.

## Findings applied

The section 7 definition of a conforming remediation now names reproduction in the same
sentence, and the key's 2c quotation was updated to the new sentence with an answer that omits
reproduction marked wrong. Fresh cohort: run 17.
