# Answer key for DETECTOR-SPEC.md

Marked against the document at the commit the readers read, with this key, its question set and
fixture at that same commit.
Quotations below are from the document; when a clause is reworded, update the quotation here in
the same commit.

## 1. Restatement

A bullet is correct when it names one of these obligations. Four or more correct bullets, and no
bullet asserting an obligation the document does not state, is a correct restatement.

- Support bespoke rules written by the project ([4.1](../../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)).
- Provide a harness that runs a single rule against supplied code ([4.2](../../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)).
- Allow a stable identifier per rule and print it, unaltered, with every finding ([4.3](../../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)).
- Be invocable locally by the practitioner, over a subset down to one file, with the result in
  the command's own output and never only through a hosted service or CI-only mode ([5.1](../../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure) to [5.4](../../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally)).
- Resolve a printed identifier to documentation; for bundled rules from the installed copy,
  offline, with the documentation shipped and versioned with the rule ([6.1](../../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation) to [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)).
- Make any inline suppression route detectable or disableable ([7.1](../../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)).

A bullet saying that a verdict on a detector names the kind, semantic, syntactic or textual, of
each configuration it grades (section [8](../../DETECTOR-SPEC.md#8-conformance)) is correct too, though it is an obligation on whoever
gives the verdict, as section [9](../../DETECTOR-SPEC.md#9-relationship-to-the-other-specifications) says. A bullet saying that the detector, or a verdict on it, must state
its kind is marked correct as this obligation, although the document puts it on the verdict.

Wrong if it asserts: the detector must be semantic to conform; the detector must enforce a
project's suppression policy; the detector must
declare a version to conform; the detector must list a project's active defences or produce an
agent summary (those belong to the toolchain specification).

## 2. Load-bearing statements

- **2a.** Conformance is satisfying every MUST in sections [4](../../DETECTOR-SPEC.md#4-authoring-rules) to [7](../../DETECTOR-SPEC.md#7-suppression), judged on evidence; a detector
  that predates the document can conform, and the declaration is optional. Key quotation, section
  8: "A Detector Conforms if it satisfies every MUST in sections [4](../../DETECTOR-SPEC.md#4-authoring-rules) to [7](../../DETECTOR-SPEC.md#7-suppression)." Supporting, [8.1](../../DETECTOR-SPEC.md#81-a-maintainer-may-declare-the-version-of-this-document-the-detector-conforms-to-and-the-declaration-records-known-gaps): "A
  maintainer MAY declare the version of this document the detector conforms to". An answer that
  says a declaration is required, or that partial satisfaction is conformance, is wrong.
- **2b.** It must make the route either disableable by configuration or detectable by a rule the
  project can write or a mechanical check it documents; it is not required to remove or forbid
  it. Key quotation, [7.1](../../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable): "For each route it ships, it need not remove or forbid the route,
  but it MUST do at least one of two things: let the project switch the route off in the Detector's
  configuration, or make the route detectable. Either alone satisfies this clause; neither requires
  the Detector to remove or forbid the route."; "A route is detectable when the project can find
  every use of it, in one of two ways. The first is a Rule the project writes for itself, under
  clause [4.1](../../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it), and the Detector runs. That way works only where the Detector lets such a Rule see
  every use of the route, and the Detector need not ship the Rule itself. The second is a
  mechanical check the Detector documents". An answer that says the detector must forbid the route, or must require a
  reason ([7.2](../../DETECTOR-SPEC.md#72-an-inline-suppression-route-should-require-a-written-reason) is SHOULD), is wrong.
- **2c.** With the rule, in the installed copy, at a version tracked together, and yes, offline.
  Key quotations, [6.2](../../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access): "Resolution of a bundled rule's identifier MUST work from the installed
  copy, without network access"; [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together): "A bundled rule's documentation MUST ship with the rule, at
  a version tracked together". An answer naming the detector's website as an acceptable location
  is wrong.

## 3. Application: Lintomatic 4.2

| Clause                                                                                                                                                              | Intended verdict | Reasoning the fixture supports                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| [4.1](../../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it)                                                        | Yes              | Project rules via the `Rule` interface, first class in every report                                                  |
| [4.2](../../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code)                                                  | Yes              | `check --only <identifier> <path>` runs one rule, bundled or project, with a distinguishing exit code                |
| [4.3](../../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding)                                   | Yes              | `LM-NNNN` fixed at first release; project names taken as given, not rewritten; printed on every finding line         |
| [5.1](../../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure)                                                  | Yes              | Local, no account, no server, no network                                                                             |
| [5.2](../../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file)                                                        | Yes              | `check <path>` accepts a single file                                                                                 |
| [5.3](../../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran)                                                       | Yes              | One line per finding on standard output whether or not the HTML report is enabled                                    |
| [5.4](../../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally) | Yes              | The hosted dashboard shows nothing the command line does not print                                                   |
| [6.1](../../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation)                                      | Yes              | `explain <identifier>` resolves a printed identifier; project rules resolve to their declared `doc` string           |
| [6.2](../../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access)                                  | Yes              | `explain` reads the installed package; there is no website                                                           |
| [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together)                                                | No               | Two of forty bundled rules print `No documentation declared`; every identifier a bundled rule can print MUST resolve |
| [7.1](../../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable)                                        | Yes              | The ignore comment is disableable with `ignore_comments = false`                                                     |

Section [8](../../DETECTOR-SPEC.md#8-conformance) verdict: **does not conform**, because [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together) fails and partial conformance MUST NOT be
described as conformance. A reader who grades [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together) Partial on the grounds that thirty-eight resolve
has read the clause differently and that counts against the document.

The fixture does not say what Lintomatic can see. A reader who names its kind as unknown, or names
none, is not marked on it; a reader who makes the verdict turn on its kind has read section [8](../../DETECTOR-SPEC.md#8-conformance)
differently, which counts against the document: "the kind is not a level of Conformance and does
not change the verdict".

Clause [6.4](../../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation): **does not change the verdict**. It is a SHOULD, and Lintomatic's failure to check its
own identifiers in CI is a missed SHOULD, not a further MUST failure; the MUST that fails is [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together).

## 4. Confusion

No keyed answer. Record every passage quoted. Two or more readers naming the same passage, as
`ACCEPTANCE.md` defines it, is a finding that blocks until the text is changed and a fresh
cohort no longer names it. What to change is the editor's decision; the reader is not asked
and any suggestion it volunteers is discarded unread.
