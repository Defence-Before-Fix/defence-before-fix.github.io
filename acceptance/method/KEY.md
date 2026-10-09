# Answer key for SPEC.md

Marked against the document at the commit the readers read, with this key, its question set and
fixture at that same commit.
Quotations below are from the document; when a clause is reworded, update the quotation here in
the same commit.

## 1. Restatement

A bullet is correct when it names one of these obligations. Four or more correct bullets, and no
bullet asserting an obligation the document does not state, is a correct restatement.

- Attribute the defect to a class, bounded on both sides, with the hazard stated ([3.1](../../SPEC.md#31-attribute-the-defect-to-a-class)).
- Express the class as a rule in a detector that reads code, never a test ([3.2](../../SPEC.md#32-build-the-net)).
- Write the rule in the strongest kind of detector that can express it, semantic, else
  syntactic, else textual, name the detector and its kind on the rule's remediation docs, and
  record why where it is in a weaker kind ([3.2](../../SPEC.md#32-build-the-net)).
- Prove the rule fires, against the instance or a fixture, in a commit of its own ([3.3](../../SPEC.md#33-prove-the-net-by-making-the-rule-fire)).
- Sweep the whole codebase, record the count, then fix every instance ([3.4](../../SPEC.md#34-sweep-the-codebase-then-fix-every-instance)).
- Make the rule permanent and blocking in the project's checks ([3.5](../../SPEC.md#35-enforce-permanently-and-block)).
- Make the failure message terse, with a stable identifier resolving to documentation versioned
  with the rule ([3.6](../../SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation)).
- Record a defect whose fix is deferred where the project's other decisions are enumerable, rather
  than only mentioning it (section [2](../../SPEC.md#2-when-the-method-applies)).

Wrong if it asserts: the practitioner fixes the reported instance first and defends afterwards;
a test may serve as the detector; an agent may baseline the remaining instances; only a semantic
detector may host a rule. A bullet that names the semantic kind and does not mention the fallback
is correct; a bullet that says no weaker kind is ever allowed is wrong.

## 2. Load-bearing statements

- **2a.** Attribute the defect to a class, express it as a detector rule, prove the rule fires,
  then sweep and fix every instance, in that order. Key quotations, section [3](../../SPEC.md#3-the-method): "Six clauses, in
  order."; [3.4](../../SPEC.md#34-sweep-the-codebase-then-fix-every-instance): "The Practitioner MUST run the Rule across the entire codebase and record the
  total Instance count before fixing anything, and MUST then fix every Instance found rather
  than only the one". An answer that has the fix before the rule, or the sweep before the proof,
  is wrong.
- **2b.** The owner of the codebase, always a human; an agent may not. Key quotation, section [4](../../SPEC.md#4-authority-which-decisions-belong-to-whom):
  "An Agent MUST NOT Baseline, suppress or knowingly leave an Instance unfixed on its own
  authority, whatever the Instance count turns out to be." An answer that lets the practitioner
  decide because the count was small, or because the project recorded no rule, is wrong (the
  default owner paragraph in the terminology entry for Owner still requires a recorded decision).
- **2c.** All six clauses of section [3](../../SPEC.md#3-the-method) were followed for that defect, and the verdict rests on the
  reviewer reproducing the red and green runs, not on the report. Key quotations, section [7](../../SPEC.md#7-conformance): "A
  remediation Conforms if all six clauses of section [3](../../SPEC.md#3-the-method) were followed for that Defect, and the
  verdict that they were rests on reproduction"; "A verdict on a remediation or a Defence MUST
  rest on reproduction, not on the report". An answer that accepts the pull request description
  as the verdict is wrong, and so is one that states the six clauses and says nothing of
  reproduction.
- **2d.** The strongest kind that can express it: a semantic detector, else a syntactic one, else
  a textual one, judged by the configuration the rule runs in; a weaker kind only where the
  stronger cannot express the rule or the language has no detector of that kind that accepts
  bespoke rules, and then the practitioner records, for each step down from semantic, which
  reason holds and why, naming the stronger detectors considered, on the rule's remediation docs
  and in the description of the commit that adds the rule, moves it, or first records the
  reason. Key quotations, [3.2](../../SPEC.md#32-build-the-net): "A Rule the
  Practitioner writes MUST be written in the strongest kind of Detector that can express it: a
  Semantic one, else a Syntactic one, else a Textual one."; "Where that kind is weaker than
  Semantic, the Practitioner MUST also record, for each step down from Semantic, which of the
  two grounds holds and why, naming the Detectors of the stronger kind that were considered, on
  the Rule's Remediation docs and in the description of the commit that adds the Rule, moves it to
  another Detector, or first records the grounds." Supporting: "On the Remediation docs of a Rule
  they write, the Practitioner MUST name the Detector and its kind." A correct answer gives three
  elements, and may leave out everything else above: (i) the strongest kind that can express the
  rule, in the order semantic, syntactic, textual; (ii) a weaker kind only where the stronger
  cannot express the rule or the language has no detector of that kind that takes bespoke rules,
  both grounds; (iii) the reason recorded; naming one of the two places is enough, and an answer
  that presents them as alternatives is wrong. An answer that misses one
  of the three, that says any detector is as good as another, that the semantic kind is only
  preferred and may be passed over for another reason, that a weaker kind is never allowed, or
  that the owner must always approve a weaker kind (the practitioner judges it unless the
  project requires the owner's sign-off), is wrong.

## 3. Application: the ledger remediation

| Clause                                                                                    | Intended verdict   | Reasoning the fixture supports                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [3.1](../../SPEC.md#31-attribute-the-defect-to-a-class)                                   | Yes, Partial or No | Class, hazard and the next wider rule are named; Partial or No is accepted where the reader notes that no independent search technique is recorded, which step 2 and the record [3.1](../../SPEC.md#31-attribute-the-defect-to-a-class) requires both call for                                                                                                                                |
| [3.2](../../SPEC.md#32-build-the-net)                                                     | Partial or No      | A rule in the project's static analyser, reading code, not a test, but the wiki page of commit D names neither the detector nor its kind; [3.2](../../SPEC.md#32-build-the-net): "On the Remediation docs of a Rule they write, the Practitioner MUST name the Detector and its kind." The fixture does not say what the analyser can see, so no reason for a weaker kind is shown to be owed |
| [3.3](../../SPEC.md#33-prove-the-net-by-making-the-rule-fire)                             | Yes                | Commit B is red on the fixture and the originating instance and survives as its own commit                                                                                                                                                                                                                                                                                                    |
| [3.4](../../SPEC.md#34-sweep-the-codebase-then-fix-every-instance)                        | No or Partial      | Five findings recorded, but one instance was left unfixed behind an inline ignore on the agent's own authority; Partial accepted where the reasoning names that suppression                                                                                                                                                                                                                   |
| [3.5](../../SPEC.md#35-enforce-permanently-and-block)                                     | Partial or No      | The rule is permanent and blocking, but the suppression was not a recorded decision; [3.5](../../SPEC.md#35-enforce-permanently-and-block): "neither does a Rule whose green run depends on a Suppression that no recorded decision covers"                                                                                                                                                   |
| [3.6](../../SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation) | No or Partial      | The message is terse and carries an identifier, but the documentation lives on a wiki, not versioned with the rule; Partial accepted where the reasoning quotes the versioning sentence                                                                                                                                                                                                       |

Section [7](../../SPEC.md#7-conformance): the **remediation does not conform**, because [3.2](../../SPEC.md#32-build-the-net), [3.4](../../SPEC.md#34-sweep-the-codebase-then-fix-every-instance) and [3.6](../../SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation) were not followed. The
**defence does not conform** either, because [3.2](../../SPEC.md#32-build-the-net) and [3.6](../../SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation) fail; a reader who names either is correct.
A reader who says the defence conforms because the sweep is what failed has missed both.

Section [4](../../SPEC.md#4-authority-which-decisions-belong-to-whom): the **inline ignore on `Report::render()`** was the owner's decision, not the
practitioner's. An answer naming instead the decision not to build the wider rule is half right, which is a miss:
that is also listed in section [4](../../SPEC.md#4-authority-which-decisions-belong-to-whom) as the owner's to take, and an answer naming both is correct.
An answer naming neither is wrong.

A reader who grades [3.5](../../SPEC.md#35-enforce-permanently-and-block) Yes because the rule fails the build has not applied the clause's opening
sentence on unrecorded suppression, and that counts against the document. A reader who grades
[3.6](../../SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation) Yes because the URL resolves has read the versioning sentence of [3.6](../../SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation)
differently, which counts against the document. A reader who grades [3.2](../../SPEC.md#32-build-the-net) Partial or No only because no reason for a weaker kind is recorded has the verdict on a
ground the fixture does not show: the reason is owed only where the rule is in a weaker kind than
semantic. That is not marked wrong. A reader who grades [3.2](../../SPEC.md#32-build-the-net) Yes is marked
wrong, including one who assigns the wiki page's failure to [3.6](../../SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation) alone: a rule with no
conforming remediation docs has its detector and kind named on none, so [3.2](../../SPEC.md#32-build-the-net) fails either
way. A reader who attributes
the suppression to [3.3](../../SPEC.md#33-prove-the-net-by-making-the-rule-fire) rather than [3.4](../../SPEC.md#34-sweep-the-codebase-then-fix-every-instance) has read the narrowing passage of [3.3](../../SPEC.md#33-prove-the-net-by-making-the-rule-fire) as covering it, which is a fair reading and is not marked wrong.

## 4. Confusion

No keyed answer. Record every passage quoted. Two or more readers naming the same passage, as
`ACCEPTANCE.md` defines it, is a finding that blocks until the text is changed and a fresh
cohort no longer names it. What to change is the editor's decision; the reader is not asked
and any suggestion it volunteers is discarded unread.
