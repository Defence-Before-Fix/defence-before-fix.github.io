# Changelog

Three documents, versioned independently. A detector or toolchain clause can be added without
reissuing the method.

## Method specification (SPEC.md)

### 1.0.1, 2026-09-08

Clarity only; no obligation changed. Section 3 opens with a map of the six clauses, with a column
naming what goes to the Owner at each; clause 3.1 opens with its five steps and a worked example
and closes with the five things it leaves on the record; clause 3.3 is in three named parts and
its narrowing part opens with the decision and a two-row example before the proof; clause 3.5
says that a Suppression no recorded decision covers leaves the clause unmet; the Owner
definition's longest sentence is split. The header and the terminology entries for Detector,
Toolchain and Conform name the detector specification 1.0.0 and toolchain specification 0.2.0
as companions, and Conform now reads "every MUST of the relevant section 7 level, or of the
companion specification being claimed", so that detector conformance is a use of the word.

Accepted by a cold cohort of five Haiku readers under the criteria in `ACCEPTANCE.md`: every
load-bearing statement keyed by all five, every fixture verdict within the key by at least four
of five, and no passage quoted as confusing by more than one reader. The accepting run is run
15, at commit 6bff4f0; run numbers are positions in one sequence shared by the three documents,
and this document was read in all of them but run 10. Single-reader misses in the accepting run:
one 3.5 Yes and one 3.6 Yes, neither quoting the document. Findings applied across the runs are
the changes the first paragraph describes. One key correction during the runs, recorded here because the key
changed after a run: 3.1 accepts No as well as Partial where the reasoning names the missing
search record, since step 2 and the record the clause requires both call for it, and two readers
of run 9 graded it so from the text. One marking error, recorded because it passed a run that
should have failed: run 9 was marked as passing with four readers grading 3.5 Yes against a key
of Partial or No; run 11 repeated that result and a clause 3.5 sentence was added in response;
runs 12 and 14 still had three readers each grading Yes on the clause's opening MUSTs, so the
opening now names its three conditions with the recorded decision the third, and the section 3
map's record column for 3.5 names it too; run 15 had four readers grade it from the text. Runs 1
to 7 also asked readers what would make a clause clearer and for a clarity rating; both questions
were withdrawn before run 8, as `ACCEPTANCE.md` records.

### 1.0.0, 2026-09-08

First normative version, published the day the repository went public. Six clauses in section 3,
decision rights in section 4, conformance in section 7, operation under AI-assisted development
in section 8. Hardened by eleven cold reads,
five adversarial critique rounds and six execution tests on real defects in php-qa-ci and
ts-qa-ci before publication, each test judged by an independent reader against section 7.
Published before the acceptance test in `ACCEPTANCE.md` existed; 1.0.1 is the first version to
pass it.

## Detector specification (DETECTOR-SPEC.md)

### 1.0.0, 2026-09-08

First version, split out of toolchain specification 0.1.0 on the same day. States what a detector,
a tool that reads code without executing it, must offer so that a practitioner can write, prove,
run and resolve a rule in it: bespoke rules as first-class, a single-rule harness, a stable
identifier printed with every finding, local invocation down to one file, results in the
practitioner's own output, on-disk resolution and shipped documentation for bundled rules, and an
inline suppression route that a project can detect or disable. The split was prompted by grading
real detectors against 0.1.0: PHPStan, the best host for the method in PHP, graded as failing
because 0.1.0 asked it to enforce a project's suppression governance and to declare a version
before it could conform, and neither is a detector's to do. Conformance is on evidence; the
declaration is the claim and the known-gap record.

Accepted by a cold cohort of five Haiku readers, every load-bearing statement and every fixture
verdict within the key by all five and no passage quoted as confusing by any reader: run 11, at
commit fa31c4e. Run numbers are positions in one sequence shared by the three documents; this
document was read in every run, run 10 passed at 6a7372a, and a review of the pull request then
changed the text. Findings applied across the runs: a seven-term gloss in section 2;
4.3 as a five-row table of stable and derived identifiers; 6.1 opens with a two-case table of
who documents what, and its URL sentence, quoted as confusing by two readers of run 8, is
rewritten; 6.3 says one unresolved identifier fails it, and the family-page material is its own
clause 6.5; 7.1 says "at least one of two things". Runs 1 to 7 also asked readers what would
make a clause clearer and for a clarity rating; both questions were withdrawn before run 8, as
`ACCEPTANCE.md` records.

## Toolchain specification (TOOLING-SPEC.md)

### 0.2.0, 2026-09-08

Reissued the same day as 0.1.0 with sections 4 to 6 moved to the detector specification and
replaced by one section on the detectors a toolchain routes defences through: each must conform
to the detector specification, the toolchain must resolve every identifier its defences print,
including the project's own, and the toolchain must forbid every suppression route that bypasses
the project record, which is where the old clause 8.3 ban now lives. The toolchain is defined as
whatever a project assembles from third-party, first-party and project-level parts, and
conformance is measured at the project level. A project that ships a detector or toolchain has two
levels, its own and its artefact's, graded and declared separately. The declaration under the old
clause 11.1 is no longer a condition of conformance; a claim with a non-empty gap record is not a
claim of conformance. Enumeration, project record, agent context and self-audit are unchanged in
substance and renumbered as sections 5 to 8, with conformance in section 9.

Accepted by a cold cohort of five Haiku readers, every load-bearing statement and every fixture
verdict within the key by all five, 4.1 graded No by all five, and no passage quoted as confusing
by any reader: run 11, at commit fa31c4e. Run numbers are positions in one sequence shared by the
three documents; this document was read in runs 1 to 8 and 11, run 8 passed at 9aaf62d, and a
review of the pull request then changed the text. One key correction during the runs, recorded
here because the key changed after a run:
5.1 accepts Partial or No where the reasoning counts the two unresolved documentation routes,
since the clause says the listing MUST provide the route and 4.1 point 2 says a gap may be named
again by a later clause; three readers of run 8 graded it so from the text. Findings applied
across the runs: an eleven-term gloss and a reading note in sections 1 and 2; long sentences
split; 4.1 opens by listing the detector specification's MUSTs and its point 2
leads with a three-case table of wrapped pairs, then the one question behind it; 4.2 says it
widens the detector document's reach to the project's own rules; 4.3 loses its double negative;
5.2 gives the derived-listing test; 6.2's heading carries the generic-justification rejection;
8.1 is consistent with 4.2 on third-party catalogues. Runs 1 to 7 also asked readers what would
make a clause clearer and for a clarity rating; both questions were withdrawn before run 8, as
`ACCEPTANCE.md` records.

### 0.1.0, 2026-09-08

First published version, the draft label dropped on the same day as the method specification. States what a toolchain must offer so that a practitioner can follow the method:
custom rules, a single-rule harness, identifier resolution, a derived listing of active defences,
the project record, self-application, and the conformance definition in section 11. Published
before the acceptance test in `ACCEPTANCE.md` existed; 0.2.0 is the first version to pass it.
