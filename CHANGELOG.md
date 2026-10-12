# Changelog

Three documents, versioned independently. A detector or toolchain clause can be added without
reissuing the method.

Changes merged to `next` and not yet released sit under an `Unreleased` heading for their
document, one line per change naming the acceptance run under `acceptance/runs/` that accepted
it. At release the heading becomes the version and date, and the lines stay as its record. A
version entry with no cohort line has not been accepted and is not published.

## Method specification (SPEC.md)

### 1.1.0, 2026-10-02

- New obligation, section [2](SPEC.md#2-when-the-method-applies): a defect whose fix is deferred MUST be recorded where the project's
  other decisions are enumerable under clause [8.7](SPEC.md#87-recorded-project-decisions-must-be-discoverable-by-the-same-means), naming the class where apparent; whether it
  stays unfixed is the owner's decision under section [4](SPEC.md#4-authority-which-decisions-belong-to-whom), and a mention in conversation is not a
  record. Appendix A carries the agent-facing sentence. Proposed in pull request 5 by an outside
  contributor after three defects reported in chat went unrecorded; rewritten by the editor.
  Section [7](SPEC.md#7-conformance)'s definition of a conforming remediation now names reproduction in the same sentence,
  after run 16 had two readers stop at the six-clause condition. Accepted by a cold cohort of
  five Haiku readers in three runs: [run 16](acceptance/runs/016-deferral-clause-run-1.md) failed
  on load-bearing statement 2c, [run 17](acceptance/runs/017-deferral-clause-run-2.md) passed with
  one single-reader miss on the defence's conformance, and after two wording edits from review
  [run 18](acceptance/runs/018-deferral-clause-run-3.md) passed with every item five of five.
  Minor version: a new obligation.

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

### Unreleased

- Clarity, no obligation changed: four passages that cold readers of an unrelated change read as
  the document pulling against itself, each listed in `acceptance/ROUTED.md`. Section [9](TOOLING-SPEC.md#9-conformance)'s
  conformance sentence now says that section [8](TOOLING-SPEC.md#8-self-audit) bears on a shipping project's artefact grade
  under clause [9.1](TOOLING-SPEC.md#91-a-project-that-ships-a-detector-or-a-toolchain-has-two-levels-of-conformance-graded-separately), not on its project grade, which is what clause [9.1](TOOLING-SPEC.md#91-a-project-that-ships-a-detector-or-a-toolchain-has-two-levels-of-conformance-graded-separately) already said and the
  answer key assumed. Clause [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access) says that one identifier that does not resolve fails it and
  that a blocking rule whose documentation is missing is graded as a defence with a gap, and
  clause [8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation) says the same of a bundled defence, after readers took section [2](TOOLING-SPEC.md#2-terminology)'s Defence row to
  put such a rule outside both clauses. Clause [9.2](TOOLING-SPEC.md#92-the-declaration-is-the-claim-and-the-known-gap-record-not-a-condition-of-conformance)'s duty to record a known gap in the
  declaration falls only on a project or artefact that declares a version, and says so beside
  "The declaration is optional", with the method's clause [3.2](SPEC.md#32-build-the-net) record applying either way.
  Clause [4.3](TOOLING-SPEC.md#43-the-toolchain-must-forbid-every-suppression-route-that-bypasses-the-project-record-by-disabling-it-or-by-a-defence-of-its-own)'s heading names both ways its body allows, disabling the route or a defence of
  the toolchain's own. Clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) says every MUST of the detector specification's sections [4](DETECTOR-SPEC.md#4-authoring-rules) to [7](DETECTOR-SPEC.md#7-suppression)
  applies and the six it lists are a summary, and its point 2 says the wrapped pair is what the
  clause judges whilst the detector's own grade is a separate verdict. Prompted by runs 33 to 52
  and 55 on the defined-terms change, in which two or more readers quoted each passage.
  [Run 57](acceptance/runs/057-toolchain-contradictions-run-1.md) failed on the first wording: every reader set clause [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access)'s
  "a defence with a gap" against the Defence row, so the sentence now says Defence there
  reaches every blocking rule whether or not its documentation exists; clause [4.3](TOOLING-SPEC.md#43-the-toolchain-must-forbid-every-suppression-route-that-bypasses-the-project-record-by-disabling-it-or-by-a-defence-of-its-own) says the
  routes are the ones each detector offers, after two readers graded it Partial for routes the
  fixture does not describe; section [1](TOOLING-SPEC.md#1-what-this-document-is-for) says the document defers to the detector specification
  only in clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification); clause [9.1](TOOLING-SPEC.md#91-a-project-that-ships-a-detector-or-a-toolchain-has-two-levels-of-conformance-graded-separately) says what the artefact grade counts; and section [9](TOOLING-SPEC.md#9-conformance)'s agent-support
  sentence says section [7](TOOLING-SPEC.md#7-agent-context) recommends, after two readers set "additionally satisfies" against
  that section's SHOULDs. [Run 58](acceptance/runs/058-toolchain-contradictions-run-2.md) failed
  on four findings in the revised text, every keyed item five of five: four readers set clause
  [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access)'s "whether or not its documentation exists" against the Defence row again, so clauses
  [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access) and [8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation) now say that a blocking rule whose documentation is missing is not yet a
  defence and is the failure each names; clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) says its six sentences are a summary and
  not the test, and its Why names the method's clauses [3.1](SPEC.md#31-attribute-the-defect-to-a-class) to [3.6](SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation) rather than "six clauses";
  section [9](TOOLING-SPEC.md#9-conformance) says every project has one project grade and that section [8](TOOLING-SPEC.md#8-self-audit) bears on a shipping
  project's separate artefact grade, clause [9.1](TOOLING-SPEC.md#91-a-project-that-ships-a-detector-or-a-toolchain-has-two-levels-of-conformance-graded-separately) names the two levels, and the agent-support
  sentence says which document's section [7](TOOLING-SPEC.md#7-agent-context) it means.
  [Run 62](acceptance/runs/062-toolchain-contradictions-run-3.md) failed on the same clause
  [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access) sentence, every keyed item five of five: four readers could not settle whether the
  clause covers its defences or every blocking rule, so its heading and its obligation sentence
  now name both, a defence or a blocking rule it routes, and the body says why the blocking
  rules are named. [Run 65](acceptance/runs/065-toolchain-contradictions-run-4.md) failed on it
  a third time, three readers unable to square a clause on defences with rules that are not
  yet one, so the heading and the obligation now name blocking rules alone, with one sentence
  on why, and clause [8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation) drops its sentence on the same contrast; clause [9.1](TOOLING-SPEC.md#91-a-project-that-ships-a-detector-or-a-toolchain-has-two-levels-of-conformance-graded-separately) says which
  document grades what, after two readers asked which section [7](TOOLING-SPEC.md#7-agent-context) the project grade rests on.
  [Run 67](acceptance/runs/067-toolchain-contradictions-run-5.md) failed on clause [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access)'s first
  paragraph, three readers each stopping at a different sentence of it, and on section [1](TOOLING-SPEC.md#1-what-this-document-is-for)'s
  "How to read this document" set against clause [4.4](TOOLING-SPEC.md#44-the-toolchains-own-invocation-must-satisfy-the-detector-specifications-reporting-clauses-for-every-defence-it-routes): the paragraph is rewritten in three, the
  obligation first, then what is in scope, then the mechanism, with Remediation docs glossed in
  section [2](TOOLING-SPEC.md#2-terminology)'s table; and section [1](TOOLING-SPEC.md#1-what-this-document-is-for) says that a toolchain can be graded from this document
  alone because each clause that rests on the detector specification says in its own words what
  that document requires. [Run 68](acceptance/runs/068-toolchain-contradictions-run-6.md) failed
  on six findings in that text: readers set a URL scheme against "without network access", "MUST
  ship with the project or with the Toolchain" against a third-party catalogue "not re-shipped
  here", the sentence on why the clause names blocking rules against the Defence row and clause
  [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) yet again, and clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification)'s "a summary, not the test" against section [1](TOOLING-SPEC.md#1-what-this-document-is-for). Clause [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access) now
  says only what it requires, of the project's own rules and bundled rules alike, with no
  sentence on defences and no list of mechanisms, and its remediation docs may ship with the
  detector whose rule they document; clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) and section [1](TOOLING-SPEC.md#1-what-this-document-is-for) both say the clause restates
  the detector specification far enough to grade what a toolchain's evidence shows.
  [Run 72](acceptance/runs/072-toolchain-contradictions-run-7.md) failed on four findings: four
  readers set the Defence row and clause [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) against clause [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access) once more, asking whether an
  undocumented blocking rule is a defence and is listed, and two set section [1](TOOLING-SPEC.md#1-what-this-document-is-for)'s "graded
  from this document alone" against clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification)'s "restated here or not". Section [2](TOOLING-SPEC.md#2-terminology) now says,
  under its table, that a blocking rule whose documentation is missing is not yet a defence and
  is what clauses [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access), [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) and [8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation) exist to catch; clause [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) says the listing covers every
  blocking rule, documented or not, with a missing route showing; and section [1](TOOLING-SPEC.md#1-what-this-document-is-for) and clause
  [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) both say a verdict from this document alone rests on what is restated and a grader with
  the detector specification holds the detector to all of it. [Run
  76](acceptance/runs/076-toolchain-contradictions-run-8.md) failed on clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification)'s first
  paragraph, all five readers unable to tell which of its two tests governs a grader without the
  detector specification, and on section [2](TOOLING-SPEC.md#2-terminology)'s "These are additional.", which the new
  paragraph had parted from its table. Clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) and section [1](TOOLING-SPEC.md#1-what-this-document-is-for) now give one test: a
  grader checks the restated sentences and takes a verdict already given on the detector under
  the detector specification as settled; the new paragraph sits at the end of section [2](TOOLING-SPEC.md#2-terminology), after
  the Project record entry. [Run 81](acceptance/runs/081-toolchain-contradictions-run-9.md)
  failed on clause [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them), two readers setting "every Defence active" against the new sentence that the
  listing covers every blocking rule, documented or not: a listing of defences said to cover
  what is not one. Clause [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) now says such a rule is not yet a defence, that clause [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access) fails it,
  and that the listing can show it with the gap showing; section [2](TOOLING-SPEC.md#2-terminology)'s paragraph names
  clauses [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access) and [8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation) as the clauses that catch it. [Run 82](acceptance/runs/082-toolchain-contradictions-run-10.md)
  failed on that clause [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) sentence again, two readers asking whether an empty route meets the MUST
  and whether "can show" means such a rule need not appear, and on clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification)'s "a verdict
  already given", two readers unable to tell which verdict or what a grader does without one.
  Clause [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) says nothing of undocumented rules now, section [2](TOOLING-SPEC.md#2-terminology)'s closing paragraph being where
  that is said; clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) and section [1](TOOLING-SPEC.md#1-what-this-document-is-for) name the verdict as one given under the detector
  specification's conformance section and say that without one the restated sentences are the test.
  [Run 83](acceptance/runs/083-toolchain-contradictions-run-11.md) failed on section [2](TOOLING-SPEC.md#2-terminology)'s
  closing paragraph and on clause [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) set against it, three readers asking whether an
  undocumented blocking rule has to appear in the listing. The paragraph now answers: nothing
  the document asks of defences, the listing included, is asked of such a rule, and a toolchain
  that runs one has failed clause [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access) whether or not its listing shows it. [Run
  84](acceptance/runs/084-toolchain-contradictions-run-12.md) failed on clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification), three
  readers unable to tell whether "every one of them" or the restated sentences set the test, and
  on the paragraph again, one reader still asking whether such a rule is listed and one unable
  to place "they". Clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) now has one test, every MUST of the detector specification's authoring, reporting, resolving and suppression sections, with the
  restated sentences as where to look first and a grader without the detector specification
  checking only them and saying so; section [1](TOOLING-SPEC.md#1-what-this-document-is-for) says the same; the paragraph says in plain
  sentences that clause [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) does not require such a rule to be listed and that clauses [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access) and
  [8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation) reach it. [Run 85](acceptance/runs/085-toolchain-contradictions-run-13.md) failed on that
  paragraph's sentence naming both clauses as reaching every blocking rule, two readers setting it against
  clause [8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation)'s exclusion of a third-party detector's native catalogue; the paragraph names
  clause [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access) alone. Accepted by [run 86](acceptance/runs/086-toolchain-contradictions-run-14.md).

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
leads with a three-case table of wrapped pairs, then the one question behind it; [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access) says it
widens the detector document's reach to the project's own rules; [4.3](TOOLING-SPEC.md#43-the-toolchain-must-forbid-every-suppression-route-that-bypasses-the-project-record-by-disabling-it-or-by-a-defence-of-its-own) loses its double negative;
[5.2](TOOLING-SPEC.md#52-the-listing-must-be-derived-from-the-active-configuration) gives the derived-listing test; [6.2](TOOLING-SPEC.md#62-every-exception-in-the-project-record-must-carry-a-written-justification-that-names-the-hazard-and-the-scope-and-the-toolchain-must-reject-a-generic-one)'s heading carries the generic-justification rejection;
[8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation) is consistent with [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-blocking-rule-it-routes-can-print-from-the-installed-copy-without-network-access) on third-party catalogues. Runs 1 to 7 also asked readers what would
make a clause clearer and for a clarity rating; both questions were withdrawn before run 8, as
`ACCEPTANCE.md` records.

### 0.1.0, 2026-09-08

First published version, the draft label dropped on the same day as the method specification. States what a toolchain must offer so that a practitioner can follow the method:
custom rules, a single-rule harness, identifier resolution, a derived listing of active defences,
the project record, self-application, and the conformance definition in section 11. Published
before the acceptance test in `ACCEPTANCE.md` existed; 0.2.0 is the first version to pass it.
