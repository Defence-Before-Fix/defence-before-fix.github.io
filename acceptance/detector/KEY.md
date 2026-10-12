# Answer key for DETECTOR-SPEC.md

Marked against the document at the commit the readers read, with this key, its question set and
fixture at that same commit. Quotations below are from the document; when a clause is reworded,
update the quotation here in the same commit. `ACCEPTANCE.md` says how each item is marked;
`acceptance/README.md` says what each part of this key is for.

## 1. Restatement

A bullet is correct when it names one of these obligations. Four or more correct bullets, with
no bullet making an assertion listed below as wrong, is a correct restatement.

- Support bespoke rules written by the project ([4.1](../../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)).
- Provide a harness that runs a single rule against supplied code ([4.2](../../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)).
- Allow a stable identifier per rule and print it, unaltered, with every finding ([4.3](../../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)); a
  bullet that says each rule carries a stable identifier names this obligation.
- Be invocable locally by the practitioner, over a subset down to one file, with the result in
  the command's own output and never only through a hosted service or CI-only mode ([5.1](../../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure) to [5.4](../../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally));
  a bullet that says every finding, or each finding, must appear in that output names [5.3](../../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran),
  whose summary may leave findings out, and is not marked wrong for the plural.
- Resolve a printed identifier to documentation; for bundled rules from the installed copy,
  offline, with the documentation shipped and versioned with the rule ([6.1](../../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation) to [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)).
- Make any inline suppression route detectable or disableable ([7.1](../../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)).

Wrong if it asserts: the detector must enforce a project's suppression policy; the detector must
declare a version to conform; the detector must list a project's active defences or produce an
agent summary (those belong to the toolchain specification). A bullet that states what
conformance means, or restates a SHOULD as advice, asserts no obligation and is neither correct
nor wrong.

Wrong readings the text invites, which count against the document on one reader: none named.

## 2. Load-bearing statements

- **2a.** Required: (1) a detector conforms when it satisfies every MUST in sections [4](../../DETECTOR-SPEC.md#4-authoring-rules) to [7](../../DETECTOR-SPEC.md#7-suppression);
  (2) yes, a detector that predates the document can conform. Wrong if it says a declaration is
  required, or that partial satisfaction is conformance. Key quotation, section [8](../../DETECTOR-SPEC.md#8-conformance): "A Detector
  Conforms if it satisfies every MUST in sections [4](../../DETECTOR-SPEC.md#4-authoring-rules) to [7](../../DETECTOR-SPEC.md#7-suppression)." Supporting, [8.1](../../DETECTOR-SPEC.md#81-a-maintainer-may-declare-the-version-of-this-document-the-detector-conforms-to-and-the-declaration-records-known-gaps): "A maintainer
  MAY declare the version of this document the detector conforms to". The reason, that
  conformance is judged on evidence and a declaration is optional, is explanation: an answer
  that gives it, or gives it instead of a plain yes, states element (2).
- **2b.** Required: (1) the two things, both named: let the project switch the route off in its
  configuration, or make the route detectable (by a bespoke rule the project writes for the
  detector, or by a mechanical check the detector documents; naming either means of detection,
  or just "detectable", states that alternative); an answer naming only one of the two things
  misses this element; (2) yes, either one alone is enough. Wrong if it says the detector must
  remove or forbid the route, or must require a reason ([7.2](../../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason) is SHOULD). Key quotation,
  [7.1](../../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable): "For each one it MUST do at least one of two things, and either alone satisfies this
  clause: make the route disableable by configuration; or make the route detectable, by a
  bespoke Rule the project writes for the Detector under clause [4.1](../../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it) or by a mechanical check the
  Detector documents". An answer need not say
  that the detector is not required to remove or forbid the route; that follows from element (2)
  and the question does not ask it.
- **2c.** Required: (1) with the rule, in the installed copy; (2) at a version tracked together
  with the rule; (3) yes, it must be reachable without network access. Wrong if it names the
  detector's website, or any location reached over the network, as acceptable. Key quotations,
  [6.2](../../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access): "Resolution of a bundled rule's identifier MUST work from the installed copy, without
  network access"; [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together): "A bundled rule's documentation MUST ship with the rule, at a version
  tracked together". "Shipped with the rule", "in the installed package" or "on disk with the
  detector" each state element (1); "versioned with the rule" or "at the same version" states
  element (2).

## 3. Application: Lintomatic 4.2

| Clause                                                                                                                                                              | Accepted grade | What the fixture supports (no row carries a condition on the reasoning)                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [4.1](../../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)                                                        | Yes            | Project rules via the `Rule` interface, first class in every report                                                                                                                                                                                                               |
| [4.2](../../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)                                                  | Yes            | `check --only <identifier> <path>` runs one rule, bundled or project, with a distinguishing exit code                                                                                                                                                                             |
| [4.3](../../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)                                   | Yes            | `LM-NNNN` fixed at first release; project names taken as given, not rewritten; printed on every finding line                                                                                                                                                                      |
| [5.1](../../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure)                                                  | Yes            | Local, no account, no server, no network                                                                                                                                                                                                                                          |
| [5.2](../../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file)                                                        | Yes            | `check <path>` accepts a single file                                                                                                                                                                                                                                              |
| [5.3](../../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)                                                       | Yes            | One line per finding on standard output whether or not the HTML report is enabled; a reader who notes that the HTML report need not be named for that reason is right                                                                                                             |
| [5.4](../../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally) | Yes            | The hosted dashboard shows nothing the command line does not print                                                                                                                                                                                                                |
| [6.1](../../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)                                      | Yes            | `explain <identifier>` resolves a printed identifier; project rules resolve to their declared `doc` string; the two undocumented bundled rules are [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)'s failure |
| [6.2](../../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)                                  | Yes            | `explain` reads the installed package; there is no website                                                                                                                                                                                                                        |
| [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)                                                | No             | Two of forty bundled rules print `No documentation declared`; every identifier a bundled rule can print MUST resolve                                                                                                                                                              |
| [7.1](../../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)                                        | Yes            | The ignore comment is disableable with `ignore_comments = false`                                                                                                                                                                                                                  |

No grade above carries a condition on the reasoning: the accepted grade is correct whatever the
reasoning, and a reader who adds a caveat about what the fixture does not say and still gives
the accepted grade is correct.

The two answers the question then asks for, each with the condition its reason must meet:

- **Conformance under section [8](../../DETECTOR-SPEC.md#8-conformance).** Accepted answer: does not conform. Condition: the reason
  names [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together), the two undocumented bundled rules, or partial conformance not counting.
- **Whether clause [6.4](../../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation) changes the verdict.** Accepted answer: it does not. Condition: the reason
  says that it is a SHOULD, or that the MUST which fails is [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together).

Wrong readings the text invites, which count against the document on one reader:

- [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together) graded Partial with reasoning that says most, or thirty-eight of forty, bundled rules
  resolve, which has read the clause as admitting a proportion.
- [7.1](../../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) graded No with reasoning that says the comment takes no reason and quotes [7.1](../../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable) or [7.2](../../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason),
  which has read [7.2](../../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason)'s SHOULD into [7.1](../../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable).

A reader who grades [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together) Yes because they missed the last paragraph of the fixture has misread the
fixture, which is the reader's miss.

## 4. Confusion

No keyed answer. Record every passage named, as `ACCEPTANCE.md` defines naming and the same
passage. A passage named by two or more readers of the run is a finding: it blocks the change
where it lies in text the change wrote or altered, and is routed to `acceptance/ROUTED.md`
otherwise. What to change is the editor's decision; the reader is not asked and any suggestion
it volunteers is discarded unread.
