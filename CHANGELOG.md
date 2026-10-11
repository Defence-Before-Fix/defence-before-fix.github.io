# Changelog

Three documents, versioned independently. A detector or toolchain clause can be added without
reissuing the method.

Changes merged to `next` and not yet released sit under an `Unreleased` heading for their
document, one line per change naming the acceptance run under `acceptance/runs/` that accepted
it. At release the heading becomes the version and date, and the lines stay as its record. A
version entry with no cohort line has not been accepted and is not published.

## Method specification (SPEC.md)

### Unreleased

- Clarity, no obligation changed: remediation is a defined term in section [1](SPEC.md#1-terminology), the work done on
  one defect under the method, its fix included, whether or not every clause of section [3](SPEC.md#3-the-method) was
  followed, and every use links to it; section [8](SPEC.md#8-operating-a-defence-under-ai-assisted-development)'s "remediation loop", a different sense, reads
  "correction loop". Clauses [3.2](SPEC.md#32-build-the-net) and [3.3](SPEC.md#33-prove-the-net-by-making-the-rule-fire) name the detector specification's rule harness where
  they said "proving harness" and "rule-testing harnesses". Prompted by a review that found
  section [7](SPEC.md#7-conformance) defining when a remediation conforms without the word being defined, and "harness"
  read as the environment an agent runs in. [Run 31](acceptance/runs/031-defined-terms-method-run-1.md)
  failed on passages the change had kept, and the same change makes them clearer: section [2](SPEC.md#2-when-the-method-applies)
  gives section [3](SPEC.md#3-the-method)'s steps in order, after two readers left steps out quoting it; clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class) says what
  its two bounds compare and what the separate question of level is, and its lower bound no
  longer calls a rule drawn to the instance "the same Narrowing", after readers took both
  sentences two ways; clause [3.3](SPEC.md#33-prove-the-net-by-making-the-rule-fire)'s Part B says an ignore placed on one instance is a call-site
  suppression under clause [3.4](SPEC.md#34-sweep-the-codebase-then-fix-every-instance), not an exclusion from the rule's scope, after a reader failed the fixture
  under both clauses for the one ignore. [Run 35](acceptance/runs/035-defined-terms-method-run-2.md)
  failed on two of these passages: clause [3.3](SPEC.md#33-prove-the-net-by-making-the-rule-fire)'s Part B now opens by saying it judges the rule's own
  scope and not an ignore placed on one instance, after a reader still failed the ignore under
  both clauses; and section [4](SPEC.md#4-authority-which-decisions-belong-to-whom)'s item on the next wider rule says which rule and which rejection
  it reaches, after two readers could not tell what its last sentence limited.
  [Run 38](acceptance/runs/038-defined-terms-method-run-3.md) failed on two passages: section [2](SPEC.md#2-when-the-method-applies)
  names two independent attempts at writing the rule where it said "techniques tried at
  expressing the Rule, in the vocabulary clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class) uses for a search", after two readers took
  them for search techniques; and clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class)'s lower bound says what "tested as a Narrowing is"
  asks of the record and where a rejection without it goes, after two readers could not tell.
  Section [4](SPEC.md#4-authority-which-decisions-belong-to-whom)'s item on the next wider rule is restated as one test, the Hazard sentence, after three
  readers each named a different sentence of it; clause [3.1](SPEC.md#31-attribute-the-defect-to-a-class)'s level sentence, section [2](SPEC.md#2-when-the-method-applies)'s
  "the first from the second" and clause [3.6](SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation)'s "no Rule build of their own" are reworded after one
  reader each. [Run 41](acceptance/runs/041-defined-terms-method-run-4.md) failed on three
  passages: clause [3.3](SPEC.md#33-prove-the-net-by-making-the-rule-fire) says before its Parts that an ignore placed on one instance counts against none
  of them, and Part B no longer calls it a suppression, after a third reader failed the ignore
  under both clauses from that paragraph; the Owner entry says the default owner takes section [4](SPEC.md#4-authority-which-decisions-belong-to-whom)'s
  decisions, after two readers could not tell from "a decision they take" whether it may; and
  clause [3.4](SPEC.md#34-sweep-the-codebase-then-fix-every-instance)'s baseline MAY names the owner and says "a very large change" for "tremendous", after
  two readers could not tell what that measured. [Run 44](acceptance/runs/044-defined-terms-method-run-5.md)
  failed on two passages of clause [3.3](SPEC.md#33-prove-the-net-by-making-the-rule-fire): Part C no longer says the enforced run does not report a
  fixture, after a reader failed the fixture's red run for reporting it; and Part B's reporting
  MUST says "more code than it leaves the Rule covering", after two readers could not tell what
  "more code than the Rule still covers" compared. [Run 47](acceptance/runs/047-defined-terms-method-run-6.md)
  failed on section [4](SPEC.md#4-authority-which-decisions-belong-to-whom)'s "Decisions that MUST go to whoever owns the codebase": the Owner entry
  says that phrase means the Owner, after two readers could not tell whether it named the same
  person as the entry, the default owner included. Accepted by run NNN.

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

- Clarity, no obligation changed: the term Harness in section [2](DETECTOR-SPEC.md#2-terminology) is now Rule harness, used in
  that form in sections [3](DETECTOR-SPEC.md#3-the-division-of-responsibility), [4.2](DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code) and [8.1](DETECTOR-SPEC.md#81-a-maintainer-may-declare-the-version-of-this-document-the-detector-conforms-to-and-the-declaration-records-known-gaps), and its definition says it is not the environment an
  agent runs in. Prompted by readers taking "harness" in its AI-agent sense, the environment
  around a language model, rather than the route that runs one rule on supplied code.
  [Run 32](acceptance/runs/032-defined-terms-detector-run-1.md) failed on passages the change had
  kept, and the same change makes them clearer: the section [2](DETECTOR-SPEC.md#2-terminology) table glosses Message, after four
  readers could not read clause [6.1](DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)'s sentence on a documentation path in the message without it;
  clause [5.3](DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran) says the remainder is any finding the summary leaves out, after every reader took
  it for extra detail about findings already printed; clause [6.1](DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation) says it asks for the mechanism,
  and a bundled identifier with no page fails clause [6.3](DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together), with clause [6.4](DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation)'s Why naming [6.3](DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together) to
  match. [Run 36](acceptance/runs/036-defined-terms-detector-run-2.md) failed on three passages:
  clause [5.3](DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)'s remainder sentences are now two plain ones, after three readers found them hard to
  parse; clause [7.1](DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) says what a rule "in the Detector itself" is, after three readers set it against
  clause [4.1](DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it); and clause [8.1](DETECTOR-SPEC.md#81-a-maintainer-may-declare-the-version-of-this-document-the-detector-conforms-to-and-the-declaration-records-known-gaps) says the duty to record a gap falls on a detector that has a declaration,
  after two readers could not tell whether an undeclared detector is bound by it.
  [Run 39](acceptance/runs/039-defined-terms-detector-run-3.md) failed on clause [7.1](DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)'s new
  sentence, which all five readers could not square with "a Rule the project can write in the
  Detector itself": it now says the project writes that rule, in the detector's own rule
  language, and the detector runs it. Clause [8.1](DETECTOR-SPEC.md#81-a-maintainer-may-declare-the-version-of-this-document-the-detector-conforms-to-and-the-declaration-records-known-gaps)'s sentence on the gap duty is shorter, after one
  reader found it hard to square with the MUST before it.
  [Run 42](acceptance/runs/042-defined-terms-detector-run-4.md) failed on two passages: clause
  [8.1](DETECTOR-SPEC.md#81-a-maintainer-may-declare-the-version-of-this-document-the-detector-conforms-to-and-the-declaration-records-known-gaps)'s gap MUST names a detector that declares a version as its subject, in place of a
  sentence after it narrowing the duty, which two readers set against the MUST; and clause [7.1](DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)
  says that the rule or the mechanical check reports each use of the route and that the project
  writes the rule, after two readers could not tell who writes it or what the check is.
  [Run 45](acceptance/runs/045-defined-terms-detector-run-5.md) failed on clause [7.1](DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) again,
  after three readers could not tell whether the detector must ship the detecting rule or only
  let the project write one: the two sentences after the MUST are now one, saying the detector
  need not ship it, and "the Detector's own Rule language", which a reader could not place, is
  gone. Accepted by run NNN.

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

- Clarity, no obligation changed: the detector specification's Harness is Rule harness in the
  section [2](TOOLING-SPEC.md#2-terminology) gloss, the section [3](TOOLING-SPEC.md#3-the-division-of-responsibility) table and clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification), and the method specification's newly
  defined Remediation is linked in clause [4.5](TOOLING-SPEC.md#45-the-toolchains-entry-point-must-run-detectors-before-runners-and-must-stop-on-a-detector-failure); the section [3](TOOLING-SPEC.md#3-the-division-of-responsibility) table's "remediation text" reads
  "remediation docs content". Prompted by "harness" read in its AI-agent sense and by
  remediation being used undefined. [Run 33](acceptance/runs/033-defined-terms-toolchain-run-1.md)
  failed on passages the change had kept, and the same change makes them clearer: the section [2](TOOLING-SPEC.md#2-terminology)
  table glosses every term the document borrows, as section [1](TOOLING-SPEC.md#1-what-this-document-is-for) says it does, Remediation and
  Remediation docs among them, and says that a blocking rule with no documentation is still
  reached by clauses [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-it-routes-can-print-from-the-installed-copy-without-network-access), [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) and [8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation), after three readers set its Defence row against them; clause
  [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-it-routes-can-print-from-the-installed-copy-without-network-access) says one identifier that does not resolve fails it and names the acceptable forms of
  lookup, after two readers graded it as met in part; clause [4.3](TOOLING-SPEC.md#43-the-toolchain-must-forbid-every-suppression-route-that-bypasses-the-project-record-by-disabling-it-or-by-a-defence-of-its-own)'s heading names disabling as well as a defence,
  as its body does, after four readers set the two against each other; clause [9.1](TOOLING-SPEC.md#91-a-project-that-ships-a-detector-or-a-toolchain-has-two-levels-of-conformance-graded-separately) says what
  "nothing else built around it" counts; clause [9.2](TOOLING-SPEC.md#92-the-declaration-is-the-claim-and-the-known-gap-record-not-a-condition-of-conformance) says its gap record binds a project that
  declares, and that a gap method clause [3.2](SPEC.md#32-build-the-net) requires is recorded either way.
  [Run 37](acceptance/runs/037-defined-terms-toolchain-run-2.md) failed on three passages: clause [4.3](TOOLING-SPEC.md#43-the-toolchain-must-forbid-every-suppression-route-that-bypasses-the-project-record-by-disabling-it-or-by-a-defence-of-its-own)
  says the routes it covers are the ones each detector offers, after two readers graded it as met
  in part because the fixture did not rule out other routes; clause [9.2](TOOLING-SPEC.md#92-the-declaration-is-the-claim-and-the-known-gap-record-not-a-condition-of-conformance) says beside its gap MUST
  that the duty falls on a project that has a declaration, and drops "makes no claim for a gap
  record to qualify", which three readers could not parse; and section [2](TOOLING-SPEC.md#2-terminology)'s "These are
  additional." says which terms it introduces, after two readers could not tell.
  [Run 40](acceptance/runs/040-defined-terms-toolchain-run-3.md) failed on three passages:
  section [2](TOOLING-SPEC.md#2-terminology) says clauses [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-it-routes-can-print-from-the-installed-copy-without-network-access), [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) and [8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation) apply to an undocumented blocking rule as if it were a
  defence, listed under [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them), where "still reach it" left four readers unsure how [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) applies to
  a rule that is not a defence; clause [9.2](TOOLING-SPEC.md#92-the-declaration-is-the-claim-and-the-known-gap-record-not-a-condition-of-conformance) names the declaration's gap duty and method clause [3.2](SPEC.md#32-build-the-net)'s as two
  duties, after two readers took them for one; and clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) says every MUST of the detector
  specification's sections [4](DETECTOR-SPEC.md#4-authoring-rules) to [7](DETECTOR-SPEC.md#7-suppression) applies and the six are a summary, after two readers
  could not tell. [Run 43](acceptance/runs/043-defined-terms-toolchain-run-4.md) failed on
  three passages and one entry: section [2](TOOLING-SPEC.md#2-terminology)'s sentence on an undocumented blocking rule is cut
  to "where clauses [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-it-routes-can-print-from-the-installed-copy-without-network-access), [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) and [8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation) say Defence, they include it", and clause [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-it-routes-can-print-from-the-installed-copy-without-network-access)'s
  sentence on a third-party detector's native catalogue says an identifier it resolves meets the
  clause and one nothing resolves fails it, after three readers of the first and two of the
  second could not tell which governs a third-party detector's undocumented bundled rules; clause [9.1](TOOLING-SPEC.md#91-a-project-that-ships-a-detector-or-a-toolchain-has-two-levels-of-conformance-graded-separately)'s sentence on
  section [8](TOOLING-SPEC.md#8-self-audit) says it is the section [9](TOOLING-SPEC.md#9-conformance) addition for a shipped toolchain that bears on the
  artefact grade only, after three readers took the two as contradicting each other; and the
  Project record entry says it is one place for every kind of judgement, after two readers
  graded clause [6.1](TOOLING-SPEC.md#61-the-toolchain-must-define-a-location-for-the-project-record-and-must-read-it-itself) as met in part for want of a location for each kind.
  [Run 46](acceptance/runs/046-defined-terms-toolchain-run-5.md) failed on four of these
  passages: section [2](TOOLING-SPEC.md#2-terminology)'s sentence no longer says such a rule is not yet a defence, only that
  Defence in clauses [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-it-routes-can-print-from-the-installed-copy-without-network-access), [5.1](TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them) and [8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation) also covers it, after three readers read its two halves as
  contradicting each other; the Project record entry is as it was, ending "whichever it has made",
  after a reader again graded clause [6.1](TOOLING-SPEC.md#61-the-toolchain-must-define-a-location-for-the-project-record-and-must-read-it-itself) as met in part, this time for want of every kind in one
  place; clause [4.1](TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification) says every MUST applies "not only the six summarised here", after two
  readers still could not tell whether the six were the whole; and clause [9.1](TOOLING-SPEC.md#91-a-project-that-ships-a-detector-or-a-toolchain-has-two-levels-of-conformance-graded-separately)'s sentence on
  section [8](TOOLING-SPEC.md#8-self-audit) is as it was, since the rewording did not stop two readers setting it against
  section [9](TOOLING-SPEC.md#9-conformance). Accepted by run NNN.

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
widens the detector document's reach to the project's own rules; [4.3](TOOLING-SPEC.md#43-the-toolchain-must-forbid-every-suppression-route-that-bypasses-the-project-record-by-disabling-it-or-by-a-defence-of-its-own) loses its double negative;
[5.2](TOOLING-SPEC.md#52-the-listing-must-be-derived-from-the-active-configuration) gives the derived-listing test; [6.2](TOOLING-SPEC.md#62-every-exception-in-the-project-record-must-carry-a-written-justification-that-names-the-hazard-and-the-scope-and-the-toolchain-must-reject-a-generic-one)'s heading carries the generic-justification rejection;
[8.1](TOOLING-SPEC.md#81-a-shipped-toolchain-must-fail-its-own-release-if-a-bundled-defence-lacks-resolvable-documentation) is consistent with [4.2](TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-it-routes-can-print-from-the-installed-copy-without-network-access) on third-party catalogues. Runs 1 to 7 also asked readers what would
make a clause clearer and for a clarity rating; both questions were withdrawn before run 8, as
`ACCEPTANCE.md` records.

### 0.1.0, 2026-09-08

First published version, the draft label dropped on the same day as the method specification. States what a toolchain must offer so that a practitioner can follow the method:
custom rules, a single-rule harness, identifier resolution, a derived listing of active defences,
the project record, self-application, and the conformance definition in section 11. Published
before the acceptance test in `ACCEPTANCE.md` existed; 0.2.0 is the first version to pass it.
