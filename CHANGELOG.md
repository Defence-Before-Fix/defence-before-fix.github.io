# Changelog

Three documents, versioned independently. A detector or toolchain clause can be added without
reissuing the method.

## Method specification (SPEC.md)

### 1.0.1, 2026-09-08

Clarity only; no obligation changed. Section [3](SPEC.md#3-the-method) opens with a map of the six clauses, with a column
naming what goes to the Owner at each; clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class) opens with its five steps and a worked example
and closes with the five things it leaves on the record; clause [3.3](SPEC.md#33-prove-the-net-by-making-the-rule-fire) is in three named parts and
its narrowing part opens with the decision and a two-row example before the proof; clause [3.5](SPEC.md#35-enforce-permanently-and-block)
says that a Suppression no recorded decision covers leaves the clause unmet; the Owner
definition's longest sentence is split. The header and the terminology entries for Detector,
Toolchain and Conform name the detector specification 1.0.0 and toolchain specification 0.2.0
as companions, and Conform now reads "every MUST of the relevant section [7](SPEC.md#7-conformance) level, or of the
companion specification being claimed", so that detector conformance is a use of the word.

Accepted by a cold cohort of five Haiku readers under the criteria in `ACCEPTANCE.md`: every
load-bearing statement keyed by all five, every fixture verdict within the key by at least four
of five, and no passage quoted as confusing by more than one reader. The accepting run is run
15, at commit 6bff4f0; run numbers are positions in one sequence shared by the three documents,
and this document was read in all of them but run 10. Single-reader misses in the accepting run:
one [3.5](SPEC.md#35-enforce-permanently-and-block) Yes and one [3.6](SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation) Yes, neither quoting the document. Findings applied across the runs are
the changes the first paragraph describes. One key correction during the runs, recorded here because the key
changed after a run: [3.1](SPEC.md#31-attribute-the-defect-to-a-class) accepts No as well as Partial where the reasoning names the missing
search record, since step 2 and the record the clause requires both call for it, and two readers
of run 9 graded it so from the text. One marking error, recorded because it passed a run that
should have failed: run 9 was marked as passing with four readers grading [3.5](SPEC.md#35-enforce-permanently-and-block) Yes against a key
of Partial or No; run 11 repeated that result and a clause [3.5](SPEC.md#35-enforce-permanently-and-block) sentence was added in response;
run 12 still had three readers, and run 14 two, grading Yes on the clause's opening MUSTs and
the green run alone, so the
opening now names its three conditions with the recorded decision the third, and the section [3](SPEC.md#3-the-method)
map's record column for [3.5](SPEC.md#35-enforce-permanently-and-block) names it too; run 15 had four readers grade it from the text. Runs 1
to 7 also asked readers what would make a clause clearer and for a clarity rating; both questions
were withdrawn before run 8, as `ACCEPTANCE.md` records.

### 1.0.0, 2026-09-08

First normative version, published the day the repository went public. Six clauses in section [3](SPEC.md#3-the-method),
decision rights in section [4](SPEC.md#4-authority-which-decisions-belong-to-whom), conformance in section [7](SPEC.md#7-conformance), operation under AI-assisted development
in section [8](SPEC.md#8-operating-a-defence-under-ai-assisted-development). Hardened by eleven cold reads,
five adversarial critique rounds and six execution tests on real defects in php-qa-ci and
ts-qa-ci before publication, each test judged by an independent reader against section [7](SPEC.md#7-conformance).
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
document was read in runs 1 to 11, run 10 passed at 6a7372a, and a review of the pull request
then changed the text. Findings applied across the runs: a seven-term gloss in section [2](DETECTOR-SPEC.md#2-terminology);
[4.3](DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding) as a five-row table of stable and derived identifiers; [6.1](DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation) opens with a two-case table of
who documents what, and its URL sentence, quoted as confusing by two readers of run 8, is
rewritten; [6.3](DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together) says one unresolved identifier fails it, and the family-page material is its own
clause [6.5](DETECTOR-SPEC.md#65-one-page-may-document-a-family-of-identifiers-and-should-name-its-members-so-a-check-can-confirm-them); [7.1](DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) says "at least one of two things". Runs 1 to 7 also asked readers what would
make a clause clearer and for a clarity rating; both questions were withdrawn before run 8, as
`ACCEPTANCE.md` records.

## Toolchain specification (TOOLING-SPEC.md)

### 0.2.0, 2026-09-08

Reissued the same day as 0.1.0 with sections [4](TOOLING-SPEC.md#4-the-detectors-a-toolchain-routes-defences-through) to [6](TOOLING-SPEC.md#6-the-project-record) moved to the detector specification and
replaced by one section on the detectors a toolchain routes defences through: each must conform
to the detector specification, the toolchain must resolve every identifier its defences print,
including the project's own, and the toolchain must forbid every suppression route that bypasses
the project record, which is where the old clause 8.3 ban now lives. The toolchain is defined as
whatever a project assembles from third-party, first-party and project-level parts, and
conformance is measured at the project level. A project that ships a detector or toolchain has two
levels, its own and its artefact's, graded and declared separately. The declaration under the old
clause 11.1 is no longer a condition of conformance; a claim with a non-empty gap record is not a
claim of conformance. Enumeration, project record, agent context and self-audit are unchanged in
substance and renumbered as sections [5](TOOLING-SPEC.md#5-enumeration) to [8](TOOLING-SPEC.md#8-self-audit), with conformance in section [9](TOOLING-SPEC.md#9-conformance).

Accepted by a cold cohort of five Haiku readers, every load-bearing statement and every fixture
verdict within the key by all five, [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) graded No by all five, and no passage quoted as confusing
by any reader: run 11, at commit fa31c4e. Run numbers are positions in one sequence shared by the
three documents; this document was read in runs 1 to 8 and 11, run 8 passed at 9aaf62d, and a
review of the pull request then changed the text. One key correction during the runs, recorded
here because the key changed after a run:
[5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) accepts Partial or No where the reasoning counts the two unresolved documentation routes,
since the clause says the listing MUST provide the route and [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) point 2 says a gap may be named
again by a later clause; three readers of run 8 graded it so from the text. Findings applied
across the runs: an eleven-term gloss and a reading note in sections [1](TOOLING-SPEC.md#1-what-this-document-is-for) and [2](TOOLING-SPEC.md#2-terminology); long sentences
split; [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) opens by listing the detector specification's MUSTs and its point 2
leads with a three-case table of wrapped pairs, then the one question behind it; [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-it-routes-can-print-from-the-installed-copy-without-network-access) says it
widens the detector document's reach to the project's own rules; [4.3](TOOLING-SPEC.md#43-the-toolchain-must-forbid-through-a-defence-of-its-own-every-suppression-route-that-bypasses-the-project-record) loses its double negative;
[5.2](TOOLING-SPEC.md#52-the-listing-must-be-derived-from-the-active-configuration) gives the derived-listing test; [6.2](TOOLING-SPEC.md#62-every-exception-in-the-project-record-must-carry-a-written-justification-that-names-the-hazard-and-the-scope-and-the-toolchain-must-reject-a-generic-one)'s heading carries the generic-justification rejection;
[8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation) is consistent with [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-it-routes-can-print-from-the-installed-copy-without-network-access) on third-party catalogues. Runs 1 to 7 also asked readers what would
make a clause clearer and for a clarity rating; both questions were withdrawn before run 8, as
`ACCEPTANCE.md` records.

### 0.1.0, 2026-09-08

First published version, the draft label dropped on the same day as the method specification. States what a toolchain must offer so that a practitioner can follow the method:
custom rules, a single-rule harness, identifier resolution, a derived listing of active defences,
the project record, self-application, and the conformance definition in section 11. Published
before the acceptance test in `ACCEPTANCE.md` existed; 0.2.0 is the first version to pass it.
