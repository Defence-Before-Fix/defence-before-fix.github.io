# Changelog

Three documents, versioned independently. A detector or toolchain clause can be added without
reissuing the method.

## Method specification (SPEC.md)

### 1.0.1, 2026-09-08

Clarity only; no obligation changed. Clause 3.1 now closes with the four things it leaves on the
record before clause 3.2 begins, and clause 3.3 opens its narrowing passage with the two-halves
test the passage then checks. Both were named independently by two or more readers of the first
acceptance cohort under [ACCEPTANCE.md](ACCEPTANCE.md). The header names the detector
specification 1.0.0 and toolchain specification 0.2.0 as companions.

Accepted by a cold cohort of five Haiku readers in nine runs, the last at spec repository commit
6c851b7: every load-bearing statement and every fixture verdict within the key, and no passage
quoted as confusing by more than one reader. Findings applied across the runs: 3.1 opens with
its five steps and a worked example and says what makes two search techniques independent; the
section 3 map gains a column naming what goes to the Owner at each clause; 3.3 is in three
named parts, and its narrowing part opens with the decision and a two-row example before the
proof; the Owner definition's longest sentence is split. Runs 1 to 7 also asked readers what
would make a clause clearer and for a clarity rating; both questions were withdrawn before run
8, as `ACCEPTANCE.md` records.

### 1.0.0, 2026-09-08

First normative version, published the day the repository went public. Six clauses in section 3, decision rights in section 4, conformance in
section 7, operation under AI-assisted development in section 8. Hardened by eleven cold reads,
five adversarial critique rounds and six execution tests on real defects in php-qa-ci and
ts-qa-ci before publication, each test judged by an independent reader against section 7.

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

Accepted by a cold cohort of five Haiku readers in ten runs, the last at spec repository commit
6a7372a: every load-bearing statement and every fixture verdict as keyed, and no passage quoted
as confusing by any reader. Findings applied across the runs: a seven-term gloss in section 2;
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

Accepted by a cold cohort of five Haiku readers in eight runs, the last at spec repository commit
9aaf62d: every load-bearing statement and every fixture verdict as keyed, 4.1 graded No by all
five for the first time, and no passage quoted as confusing by any reader. Findings applied
across the runs: an eleven-term gloss and a reading note in sections 1 and 2; every sentence over
forty words split; 4.1 opens by listing the detector specification's MUSTs and its point 2
leads with a three-case table of wrapped pairs, then the one question behind it; 4.2 says it
widens the detector document's reach to the project's own rules; 4.3 loses its double negative;
5.2 gives the derived-listing test; 6.2's heading carries the generic-justification rejection;
8.1 is consistent with 4.2 on third-party catalogues. Runs 1 to 7 also asked readers what would
make a clause clearer and for a clarity rating; both questions were withdrawn before run 8, as
`ACCEPTANCE.md` records.

### 0.1.0, 2026-09-08

First published version, the draft label dropped on the same day as the method specification. States what a toolchain must offer so that a practitioner can follow the method:
custom rules, a single-rule harness, identifier resolution, a derived listing of active defences,
the project record, self-application, and the conformance definition in section 11.
