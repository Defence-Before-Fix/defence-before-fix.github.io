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

Accepted by a cold cohort of five Haiku readers in three runs; findings applied: 3.1 closes with
its record, 3.3 opens with the two-halves test as two bullets. Clause 3.1 remains the clause
readers name as read twice; every reader graded it as keyed, so it is recorded, not blocking.

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

Accepted by a cold cohort of five Haiku readers in three runs; findings applied: 6.3's family
rule as two listed alternatives with a worked example, a derived-versus-assigned example in 4.3,
a seven-term gloss in section 2. Clause 6.3 remains the clause readers name as read twice; every
reader graded it as keyed, so it is recorded, not blocking.

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

Not yet accepted. Three runs of a cold cohort of five Haiku readers: every load-bearing statement
and every fixture verdict correct in every run, and the findings applied (4.1 point 2 leads with
"wrapping can add a mechanism; it cannot excuse a gap" and a two-case example, 6.2's heading
carries the generic-justification rejection, an eleven-term gloss and a reading note in sections
1 and 2), but the clarity median held at 3 of 5 across all three runs, below the threshold of 4,
with the same cause named each time: the density of linked terms and cross-references to the two
companion documents. The decision on that cause is recorded in the repository's plan journal.

### 0.1.0, 2026-09-08

First published version, the draft label dropped on the same day as the method specification. States what a toolchain must offer so that a practitioner can follow the method:
custom rules, a single-rule harness, identifier resolution, a derived listing of active defences,
the project record, self-application, and the conformance definition in section 11.
