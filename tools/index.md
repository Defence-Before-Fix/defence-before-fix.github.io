---
title: Tools and Defence Before Fix
permalink: /tools/
---

# Tools and Defence Before Fix

A register of QA tools graded against the method. Each tool has a page saying how it is and is
not conformant, clause by clause against [the toolchain specification](../TOOLING-SPEC.md).

**Readiness** asks whether a practitioner can follow the six clauses of
[the method specification](../SPEC.md) with this tool alone: bespoke rules written by the project,
a single rule runnable against a single file, and a stable identifier printed with every finding.
**Conformance** is the toolchain specification's word, and it is strict: a tool is conforming only
when every MUST holds and the tool declares the version it conforms to with an empty gap record.
Most good tools are amber on conformance whilst being green on readiness, and that is a normal
and respectable condition rather than a criticism.

| Grade | Readiness                                                       | Conformance                                                    |
| ----- | --------------------------------------------------------------- | -------------------------------------------------------------- |
| 🟢    | All three of bespoke rules, single-rule run, printed identifier | Every MUST holds and the version is declared, gap record empty |
| 🟡    | Possible with a workaround, a plugin ecosystem, or two of three | Most MUSTs hold, undeclared, or declared with a gap record     |
| 🔴    | No bespoke rules, or no stable identifier on findings           | A structural MUST fails                                        |

The register is being compiled and will appear here.
