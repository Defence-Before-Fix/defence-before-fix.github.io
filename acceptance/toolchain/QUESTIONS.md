# Questions for a cold reader of TOOLING-SPEC.md

You have been given `TOOLING-SPEC.md` and the fixture `fixtures/zigpipe.md`, and nothing else.
Read the document once, then answer every question below in order. Quote the document where a
question asks for a quotation. Do not consult anything outside what you were given.

## 1. Restatement

In your own words and in at most six bullets, what does this document require of a project's
toolchain?

## 2. Load-bearing statements

Answer each in one sentence, followed by the sentence of the document you are relying on, quoted.

- 2a. At what level is toolchain conformance measured, and what is the toolchain?
- 2b. A project's tooling is assembled from a third-party detector, a first-party package and
  the project's own rules. How many conformance grades does that assembly receive, and what is
  the role of the individual parts in reaching it?
- 2c. A company publishes a toolchain package and also uses it on the package's own repository.
  How many conformance grades does that project have, and does one imply the other?

## 3. Application

Grade the Zigpipe project's toolchain, as described in the fixture, against every MUST clause in
sections [4](../../TOOLING-SPEC.md#4-the-detectors-a-toolchain-routes-defences-through) to [6](../../TOOLING-SPEC.md#6-the-project-record): [4.1](../../TOOLING-SPEC.md#41-every-detector-the-toolchain-routes-a-defence-through-must-conform-to-the-detector-specification), [4.2](../../TOOLING-SPEC.md#42-the-toolchain-must-resolve-every-identifier-a-defence-it-routes-can-print-from-the-installed-copy-without-network-access), [4.3](../../TOOLING-SPEC.md#43-the-toolchain-must-forbid-through-a-defence-of-its-own-every-suppression-route-that-bypasses-the-project-record), [4.4](../../TOOLING-SPEC.md#44-the-toolchains-own-invocation-must-satisfy-the-detector-specifications-reporting-clauses-for-every-defence-it-routes), [4.5](../../TOOLING-SPEC.md#45-the-toolchains-entry-point-must-run-detectors-before-runners-and-must-stop-on-a-detector-failure), [5.1](../../TOOLING-SPEC.md#51-the-toolchain-must-be-able-to-list-the-defences-active-in-a-project-without-triggering-them), [5.2](../../TOOLING-SPEC.md#52-the-listing-must-be-derived-from-the-active-configuration), [5.3](../../TOOLING-SPEC.md#53-a-projects-own-defences-must-appear-in-the-listing-alongside-bundled-ones), [6.1](../../TOOLING-SPEC.md#61-the-toolchain-must-define-a-location-for-the-project-record-and-must-read-it-itself), [6.2](../../TOOLING-SPEC.md#62-every-exception-in-the-project-record-must-carry-a-written-justification-that-names-the-hazard-and-the-scope-and-the-toolchain-must-reject-a-generic-one), [6.3](../../TOOLING-SPEC.md#63-the-project-record-must-be-enumerable-by-the-same-means-as-the-defences). For each give Yes,
Partial or No and one line of reasoning. Then state whether the toolchain conforms under section
9, whether it conforms with agent support, and whether section [8](../../TOOLING-SPEC.md#8-self-audit) applies to it. Finally, state
whether the absence of a declaration affects the verdict.

## 4. Confusion

Quote any passage you found confusing on your one reading, with its clause number. Do not say what
would make it clearer and do not propose any change. Write "none" if there was none.
