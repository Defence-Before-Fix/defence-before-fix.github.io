# Changelog

Three documents, versioned independently. A detector or toolchain clause can be added without
reissuing the method.

Changes merged to `next` and not yet released sit under an `Unreleased` heading for their
document, one line per change naming the acceptance run under `acceptance/runs/` that accepted
it. At release the heading becomes the version and date, and the lines stay as its record. A
version entry with no cohort line has not been accepted and is not published.

## Method specification (SPEC.md)

### Unreleased

- New obligation, clause [3.2](SPEC.md#32-build-the-net): a rule the practitioner writes MUST be written in the strongest
  kind of detector that can express it, semantic, else syntactic, else textual, judged by the
  configuration it runs in; enabling an existing rule or tightening its thresholds is not writing
  one, and giving an existing rule a pattern of the project's own, or changing the pattern of one
  the project wrote, is. A weaker
  kind is allowed only where the stronger cannot express the rule or the language has no
  detector of that kind that accepts bespoke rules; a stronger configuration of a detector the
  project runs counts, and one only a hosted service or licence tier provides does not. A
  detector accepts bespoke rules when the project can add its own through a documented extension
  point, and a rule its extension points cannot reach is one it cannot express. The
  remediation docs of a rule the practitioner writes MUST name its detector and kind, and for
  each step down from semantic the reason, with the stronger detectors considered, MUST be
  recorded there and in the description of the commit that adds or moves the rule or first
  records the reason. The practitioner judges it; a project MAY require the owner's sign-off by
  recording that requirement where it records its calibrations, the sign-off then recorded with
  the reason, which section [4](SPEC.md#4-authority-which-decisions-belong-to-whom) and the section [3](SPEC.md#3-the-method) map note. Clause [3.6](SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation)'s list of what the
  remediation docs state defers to what clause [3.2](SPEC.md#32-build-the-net) adds. Section [1](SPEC.md#1-terminology)
  defines textual, syntactic and semantic by whether a rule can ask the type of any expression
  and what any name refers to across the whole program, naming mypy as semantic only with
  `check_untyped_defs`, since by default it does not check the bodies of unannotated functions.
  Section [2](SPEC.md#2-when-the-method-applies) and clause [3.2](SPEC.md#32-build-the-net) send a class that no extensible detector of a kind the language
  has can express within clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class)'s bounds to a bespoke detector or a toolchain gap, not to
  "no pattern exists". Section
  [7](SPEC.md#7-conformance)'s conforming defence carries the kind, and Appendix A carries the requirement. Prompted by
  project rules hosted in ast-grep, where the language already had a semantic host, that decided
  by names: they reported unrelated calls of the same name, and clause [3.2](SPEC.md#32-build-the-net) said any detector
  qualified whatever its category. The method question set gains load-bearing statement 2d, which
  `ACCEPTANCE.md` now lists, and `index.md`, `README.md`, `PRIMER.md` and two register pages
  defer to the clause. After run 19, clarity edits: clause [3.2](SPEC.md#32-build-the-net) sets out the two grounds
  for a weaker kind as a numbered pair, calls them grounds throughout, as Appendix A now does, and
  says the extension-points rule in two sentences; section [2](SPEC.md#2-when-the-method-applies) says what independent means instead
  of pointing at clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class)'s vocabulary; clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class) says what the level of a class is; clause [3.3](SPEC.md#33-prove-the-net-by-making-the-rule-fire)'s
  Part B says an instance left behind an inline ignore comment, an ignore entry or a baseline is
  not a narrowing, since the code still carries the hazard, but a suppression for clauses [3.4](SPEC.md#34-sweep-the-codebase-then-fix-every-instance) and
  [3.5](SPEC.md#35-enforce-permanently-and-block) and section [4](SPEC.md#4-authority-which-decisions-belong-to-whom); and clause [3.4](SPEC.md#34-sweep-the-codebase-then-fix-every-instance) says plainly that a baseline is rare. After run 21, clarity
  edits: section [2](SPEC.md#2-when-the-method-applies) names the order of the steps, since three readers stopped at its MUST
  sentence; clause [3.2](SPEC.md#32-build-the-net) states both grounds for a weaker kind in the sentence that allows one, since
  no reader named them, and says the extension-points rule in short sentences; clause [3.3](SPEC.md#33-prove-the-net-by-making-the-rule-fire)'s Part
  B says an inline ignore is not judged under it, and Part C says the red run may report a
  fixture and the green run does not; section [4](SPEC.md#4-authority-which-decisions-belong-to-whom)'s lead-in names the owner, and its bullet on the
  next wider rule, with the section [3](SPEC.md#3-the-method) map's row, says the owner decides unless the practitioner
  has written and confirmed why the hazard cannot arise there. After run 23, clarity edits: clause
  [3.2](SPEC.md#32-build-the-net)'s record sentence names the order of kinds, both grounds and the two places first, since
  no reader stated all three; clause [3.2](SPEC.md#32-build-the-net) asks the second ground as two questions of each
  stronger detector; clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class)'s lower bound says an exact-value rule matches one thing and
  states the test of the wider rule's rejection in short sentences, without calling it a
  narrowing; section [1](SPEC.md#1-terminology)'s Narrowing and Suppression entries say an exclusion of code that carries
  the hazard is a suppression, not a narrowing; and the Owner entry says the default owner is the
  human who instructed the practitioner, or, where an agent gave the instruction, the human who
  instructed that agent, and takes section [4](SPEC.md#4-authority-which-decisions-belong-to-whom)'s
  decisions. Each after readers of run 23 missed or named the passage. After run 25, clarity
  edits: clause [3.2](SPEC.md#32-build-the-net)'s record sentence states both grounds in its main clause, not in brackets,
  and its paragraph on the second ground says in fewer sentences when the language has a
  detector of the stronger kind and when it accepts bespoke rules; clause [3.5](SPEC.md#35-enforce-permanently-and-block) says what a
  bundled defence is and that a project installing somebody else's toolchain counts, without the
  undefined term consuming project; clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class)'s paragraph on independent techniques is shorter
  and says plainly that a run of the rule is never one; and clause [3.6](SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation)'s versioning sentence
  says a rule's documentation is versioned with the rule. Each after readers of run 25 missed or
  named the passage. After run 27, clarity edits: clause [3.2](SPEC.md#32-build-the-net) states both grounds for a weaker
  kind in the sentence straight after the strongest-kind sentence, and its record paragraph names
  the two places, both required, before what is recorded and which commit carries it; section
  [7](SPEC.md#7-conformance)'s conforming defence satisfies each clause in full, and its summary of clause [3.5](SPEC.md#35-enforce-permanently-and-block) includes
  permanence and the recorded decision behind every suppression; section [2](SPEC.md#2-when-the-method-applies) and clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class) each say
  what a technique is there, and clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class)'s paragraph on independent techniques is three short
  paragraphs, saying that a run of the rule belongs to the proof or the sweep. Each after readers
  of run 27 missed or named the passage. After run 29, clarity edits: section [2](SPEC.md#2-when-the-method-applies)'s sentence that
  no pattern exists names two independent ways of writing the rule that were tried, in place of
  "techniques", and says a way of writing the rule is not a technique, which clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class) defines;
  the MUST it carries is reworded, not changed. Clause [3.2](SPEC.md#32-build-the-net)'s paragraph on the two kinds of gap
  gives each kind a sentence of its own and names, for a missing mechanism, the substitutes
  clauses [3.3](SPEC.md#33-prove-the-net-by-making-the-rule-fire) and [3.6](SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation) already allow, each only under the condition its clause sets and only for
  what it stands in for: the smoke check for the fixture-based test clause [3.3](SPEC.md#33-prove-the-net-by-making-the-rule-fire)'s test-first
  paragraph asks for, so that Part A's red run and Part C's proof on fixture code are still owed,
  and the anchor for a resolver; it says every other obligation of those clauses still applies,
  so nothing is relaxed; and clause [3.5](SPEC.md#35-enforce-permanently-and-block)'s paragraph on a bundled
  defence says in shorter sentences that, where a mechanism gap stops the toolchain running its
  own entry point, the demonstration is made through another project's entry point and owed
  there in full, and that clause [3.2](SPEC.md#32-build-the-net)'s substitutes give no way round it. Each after two readers of
  run 29 named the passage. Clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class) says a technique is a way of searching for instances
  wherever the specification uses the word, after one reader of run 29 named run 25's open
  passage there, and section [4](SPEC.md#4-authority-which-decisions-belong-to-whom) calls suppressions and baselines practices, not techniques, to
  follow it. Section [4](SPEC.md#4-authority-which-decisions-belong-to-whom) says an exception exists only where the owner, not "a human", has
  discussed, agreed and documented it, as the owner's terminology entry and the section's own
  list already say, after a reader of run 29 answered 2b with "a human" and not the owner. Accepted by run
  NNN. Minor version when released.

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

### Unreleased

- New obligation, clause [8.2](DETECTOR-SPEC.md#82-a-verdict-on-a-detector-must-name-its-kind-in-each-configuration-it-grades): a verdict on a detector MUST name the kind, semantic, syntactic
  or textual, of each configuration it grades, as the detector has it without any hosted service
  or licence tier. It is not a level of conformance and does not change the verdict; it
  is stated because method clause [3.2](SPEC.md#32-build-the-net) now requires a rule to be written in the strongest kind of
  detector that can express it, and a verdict of conforming alone presents a textual detector as
  an equal host. Section [9](DETECTOR-SPEC.md#9-relationship-to-the-other-specifications) still adds no obligation to the method a practitioner
  follows and names this one as binding whoever gives a verdict on a detector, a practitioner
  included when they give one, and section [2](DETECTOR-SPEC.md#2-terminology)'s gloss carries the three terms. After run 20, changed obligation, clause [5.3](DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran): the
  usable summary gives each finding in it with its location and identifier, and the location of
  the rest is owed only where the summary leaves a finding out, so output that prints every
  finding conforms though extra detail goes to a file it does not name; the old text owed that
  location unconditionally, run 20's five readers graded the fixture's [5.3](DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran) Partial on it, and the
  key's intended Yes already assumed the new reading. Clarity edits: clause [6.1](DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation) says it asks
  for the mechanism and that missing documentation for a bundled rule fails clause [6.3](DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together), as
  clause [6.4](DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation)'s Why now says too, and says plainly why a path in the message is not enough;
  clause [7.1](DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) says the project writes the detecting rule in the detector, of the kind clause
  [4.1](DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it) requires, and that the detector need not remove or forbid the route; clause [8.1](DETECTOR-SPEC.md#81-a-maintainer-may-declare-the-version-of-this-document-the-detector-conforms-to-and-the-declaration-records-known-gaps) says
  what a gap is, that a detector declaring a version records it there, and that conformance is
  judged on evidence with or without a declaration. After run 22, clarity edits: section [8](DETECTOR-SPEC.md#8-conformance)
  says beside the definition of conformance that it is judged on evidence and a declaration is
  optional, and clause [8.1](DETECTOR-SPEC.md#81-a-maintainer-may-declare-the-version-of-this-document-the-detector-conforms-to-and-the-declaration-records-known-gaps) says plainly which declaration claims conformance; clause [7.1](DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) opens by
  saying the detector need not remove or forbid the route and says what detectable means in short
  sentences; clause [5.3](DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran) says the summary need not list every finding; clause [6.1](DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation) says
  plainly why a path in the message is not enough, and section [2](DETECTOR-SPEC.md#2-terminology)'s gloss defines the message.
  Each after readers of run 22 missed or named the passage. After run 24, clarity edits: clause
  [7.1](DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)'s sentence that either thing alone satisfies the clause adds that neither requires the
  detector to remove or forbid the route, and the clause is in shorter sentences; clause [8.1](DETECTOR-SPEC.md#81-a-maintainer-may-declare-the-version-of-this-document-the-detector-conforms-to-and-the-declaration-records-known-gaps)'s
  sentence that a detector may be graded conforming on evidence says a declaration is optional,
  and its paragraph is in short sentences; section [8](DETECTOR-SPEC.md#8-conformance)'s paragraph on the kind says one
  detector can be graded in more than one configuration and that one needing a hosted service or
  licence tier does not count. Each after readers of run 24 missed or named the passage. After
  run 26, clarity edits: clause [7.1](DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)'s obligation sentence itself says the detector need not
  remove or forbid the route, and its definition of detectable is one sentence; section [8](DETECTOR-SPEC.md#8-conformance)'s
  paragraph on the kind is shorter, says what the kind is, and says the duty is on whoever gives
  the verdict, not on the detector. Each after readers of run 26 missed or named the passage.
  After run 28, clarity edits: clause [7.1](DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) says after the two things that neither requires removing
  or forbidding the route, and says in a paragraph of its own what detectable means, that the
  project writes the detecting rule, which works only where the detector lets it see every use, and what a
  documented check is; clause [6.1](DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation) says that for a project's own rule printing the identifier
  unaltered is everything it asks of the detector and the resolving is the toolchain's, without
  needing the other specifications; section [8](DETECTOR-SPEC.md#8-conformance)'s paragraph on the kind says what a
  configuration is and, in a paragraph of its own, that the duty is not one of the MUSTs
  conformance is judged on and that a verdict leaving the kind out still stands on conformance.
  Each after readers of run 28 missed or named the passage. After run 30, the MUST to name the
  kind moves, unchanged, from the body of section [8](DETECTOR-SPEC.md#8-conformance), beside the conformance test, to a clause
  [8.2](DETECTOR-SPEC.md#82-a-verdict-on-a-detector-must-name-its-kind-in-each-configuration-it-grades) of its own, with a Why; the paragraph after it says, in new words, that it binds whoever
  gives the verdict, anyone grading under clause [8.1](DETECTOR-SPEC.md#81-a-maintainer-may-declare-the-version-of-this-document-the-detector-conforms-to-and-the-declaration-records-known-gaps) and a maintainer grading their own detector
  included, and asks nothing of the detector itself, nor of a declaration under clause [8.1](DETECTOR-SPEC.md#81-a-maintainer-may-declare-the-version-of-this-document-the-detector-conforms-to-and-the-declaration-records-known-gaps), which
  is the maintainer's claim and not a verdict; section [9](DETECTOR-SPEC.md#9-relationship-to-the-other-specifications) names the clause and says it
  binds a practitioner who gives a verdict. Clarity edits: clause [7.1](DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) says, route by route, what
  a project's own rule must be able to match for the route to be detectable that way: for an
  ignore comment or a per-line directive each place it is written, for a generated baseline each
  of its entries; clause [8.1](DETECTOR-SPEC.md#81-a-maintainer-may-declare-the-version-of-this-document-the-detector-conforms-to-and-the-declaration-records-known-gaps) says a gap is a MUST the detector does not satisfy, that a
  declaration is the maintainer's claim, and that a detector with no declaration claims nothing.
  Each after two or more readers of run 30 named the passage. Clause [6.2](DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access) gains a paragraph
  saying that resolution reads the documentation clause [6.3](DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together) requires to ship with the rule, at a
  version tracked together with it, in the installed copy, that clause [6.2](DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access) asks that the
  lookup reach it without network access, and that a missing page fails clause [6.3](DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together), not
  clause [6.2](DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access), after two readers of run 30 answered
  2c from clause [6.2](DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access) alone and left out the version. Accepted by run NNN. Minor version
  when released.

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
