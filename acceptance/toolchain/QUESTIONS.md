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
sections 4 to 6: 4.1, 4.2, 4.3, 4.4, 4.5, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3. For each give Yes,
Partial or No and one line of reasoning. Then state whether the toolchain conforms under section
9, whether it conforms with agent support, and whether section 8 applies to it. Finally, state
whether the absence of a declaration affects the verdict.
