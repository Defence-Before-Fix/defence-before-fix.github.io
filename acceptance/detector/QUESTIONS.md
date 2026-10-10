# Questions for a cold reader of DETECTOR-SPEC.md

You have been given `DETECTOR-SPEC.md` and the fixture `fixtures/lintomatic.md`, and nothing
else. Read the document once, then answer every question below in order. Quote the document
where a question asks for a quotation. Do not consult anything outside what you were given.

## 1. Restatement

In your own words and in at most six bullets, what does this document require of a detector?

## 2. Load-bearing statements

Answer each in one sentence, followed by the sentence of the document you are relying on, quoted.

- 2a. What does it mean for a detector to conform, and can a detector that was written before
  this document existed, and has never heard of it, conform?
- 2b. A detector ships an inline ignore comment. What must the detector do about that route for
  it to conform?
- 2c. Where must the documentation for a bundled rule's identifier live, and must it be
  reachable without network access?

## 3. Application

Grade Lintomatic 4.2, as described in the fixture, against every MUST clause in sections [4](../../DETECTOR-SPEC.md#4-authoring-rules) to [7](../../DETECTOR-SPEC.md#7-suppression):
[4.1](../../DETECTOR-SPEC.md#41-the-detector-must-support-bespoke-rules-written-by-the-project-that-runs-it), [4.2](../../DETECTOR-SPEC.md#42-the-detector-must-provide-a-harness-that-runs-a-single-rule-against-supplied-code), [4.3](../../DETECTOR-SPEC.md#43-the-detector-must-allow-a-rule-to-carry-a-stable-identifier-and-must-print-it-with-every-finding), [5.1](../../DETECTOR-SPEC.md#51-the-detector-must-be-invocable-by-the-practitioner-locally-with-no-infrastructure), [5.2](../../DETECTOR-SPEC.md#52-the-detector-must-support-invocation-over-a-subset-at-minimum-a-single-file), [5.3](../../DETECTOR-SPEC.md#53-the-result-must-reach-the-practitioner-in-the-output-of-the-command-they-ran), [5.4](../../DETECTOR-SPEC.md#54-a-finding-must-not-be-reportable-only-through-a-hosted-service-licence-tier-or-ci-only-mode-the-practitioner-cannot-invoke-locally), [6.1](../../DETECTOR-SPEC.md#61-the-detector-must-provide-a-mechanism-that-resolves-a-printed-identifier-to-its-documentation), [6.2](../../DETECTOR-SPEC.md#62-resolution-of-a-bundled-rules-identifier-must-work-from-the-installed-copy-without-network-access), [6.3](../../DETECTOR-SPEC.md#63-a-bundled-rules-documentation-must-ship-with-the-rule-at-a-version-tracked-together), [7.1](../../DETECTOR-SPEC.md#71-a-detector-may-offer-an-inline-suppression-route-but-must-make-it-detectable-or-disableable). For each give Yes, Partial or No and one
line of reasoning. Then state whether Lintomatic conforms under section [8](../../DETECTOR-SPEC.md#8-conformance), and why. Finally,
state whether clause [6.4](../../DETECTOR-SPEC.md#64-the-detector-should-fail-its-own-release-if-a-bundled-rule-lacks-resolvable-documentation) changes the verdict.

## 4. Confusion

Quote any passage you found confusing on your one reading, with its clause number. Do not say what
would make it clearer and do not propose any change. Write "none" if there was none.
