---
title: NullAway and Defence Before Fix
summary: One fixed nullness check fails 4.1 and its class-name identifier fails 4.3; it runs alone and locally, meeting 4.2 and section 5; one constant link for every finding resolves no identifier, failing 6.1 to 6.3; its own @SuppressWarnings handling ignores Error Prone's switch, failing 7.1
language: Java
kind: tool
readiness: 🔴
detector: 🔴
checked: 2026-10-10, version 0.14.2
---

# NullAway

{% include tool-grades.html %}

NullAway is Uber's nullness checker for Java, shipped as a single check that runs on the [Error Prone](error-prone.md) host inside `javac`. It treats code in the packages it is told about as non-null unless annotated `@Nullable`, follows values through each method with a data-flow analysis, and reports a dereference, return, assignment or field initialisation that could let a null through. In a Java project's checks it is part of the compile step, configured by `-XepOpt:NullAway:*` compiler arguments; this page grades what NullAway adds to the host, not the host itself.

## How it is conformant

The check runs wherever `javac` runs with Error Prone, with no service (5.1, 5.4). Ran at 0.14.2 on Error Prone 2.50.0 and JDK 21: `javac` on one source file with `-XepOpt:NullAway:AnnotatedPackages=p` printed `src/p/Base.java:7: warning: [NullAway] dereferenced expression 's' is @Nullable` in the compiler's own output (5.2, 5.3). The check is a warning by default, so the compile exits 0; raised with `-Xep:NullAway:ERROR` the same finding exits 1. One of `AnnotatedPackages` and `OnlyNullMarked` must be given, or the compiler stops with an exception and exits 4 ([configuration](https://github.com/uber/NullAway/wiki/Configuration)).

The check can be run alone against supplied code through the host: `-XepDisableAllChecks -Xep:NullAway:ERROR` on one file reported only `[NullAway]`, ran (4.2). NullAway has no rules of a project's own, so 4.2 is graded on its one bundled check, as the clause says.

## How it is not conformant

There are no bespoke rules (4.1). NullAway is one check with options: annotation names, excluded classes, library models loaded through a `LibraryModels` service, and a `castToNonNull` method ([configuration](https://github.com/uber/NullAway/wiki/Configuration)). Each tunes the nullness analysis; none expresses a different pattern. A project's own class goes in an Error Prone check of its own beside NullAway, on the host. That is a structural failure, and it decides both grades.

Clause 4.3 fails as well. The `@BugPattern` on the check class sets no `name` ([`NullAway.java` at the tag](https://github.com/uber/NullAway/blob/v0.14.2/nullaway/src/main/java/com/uber/nullaway/NullAway.java)), so Error Prone uses the class name, `NullAway`, which is the derivation the clause rules out; with no rule of the project's own to carry any other, the row is No under reading 5. The token is printed unaltered in square brackets with every finding, and it is the same token for every kind of finding: a dereference and a missing initialisation both printed `[NullAway]`, ran. There is no rule over the rules (4.4).

Nothing resolves the identifier to documentation (6.1 to 6.3). Every finding ends with the same link, `(see http://t.uber.com/nullaway )`, the default of the `ErrorURL` option ([`ErrorProneCLIFlagsConfig.java` at the tag](https://github.com/uber/NullAway/blob/v0.14.2/nullaway/src/main/java/com/uber/nullaway/ErrorProneCLIFlagsConfig.java)), which redirected to the wiki's [Error Messages](https://github.com/uber/NullAway/wiki/Error-Messages) page, ran. That address is the same for every finding and is not keyed on the identifier as printed (reading 11), and the page is arranged by message text. The installed jar holds classes, a service file and `jspecify-jdk.astubx`, and no documentation (`unzip -l`, ran), and the wiki is online only. No release check over documentation was found (6.4).

Clause 7.1 fails. NullAway reads `@SuppressWarnings` itself rather than leaving it to the host: `symbolHasSuppressWarningsAnnotation` in [`ErrorBuilder.java` at the tag](https://github.com/uber/NullAway/blob/v0.14.2/nullaway/src/main/java/com/uber/nullaway/ErrorBuilder.java) honours `"NullAway"`, its alternative name `"CheckNullabilityTypes"`, the sub-keys `"NullAway.Init"` and `"NullAway.Optional"`, and any `SuppressionNameAliases`. Ran with Error Prone's `-XepIgnoreSuppressionAnnotations`, which on the [Error Prone page](error-prone.md) closes the host's own route: a method under `@SuppressWarnings("all")` was reported, but methods under `"NullAway"` and `"CheckNullabilityTypes"`, and a field under `"NullAway.Init"`, still were not. NullAway documents no option that switches its handling off ([suppressing warnings](https://github.com/uber/NullAway/wiki/Suppressing-Warnings)), and it reports nothing about what it suppressed. A second inline route behaves the same way: a class annotated with any annotation named `lombok.Generated` is not analysed, because the default `ExcludedClassAnnotations` entry is always kept when the option is set (`getFlagStringSet` adds to the defaults); ran with `ExcludedClassAnnotations=q.Other`, a hand-written `@lombok.Generated` class still reported nothing. A check of the project's own on the Error Prone host could see these annotations, but that is a rule in the host, not in NullAway. `@SuppressWarnings` takes no reason, and the optional `AutoFixSuppressionComment` only adds a fixed comment to suppressions NullAway itself suggests (7.2).

Readiness is 🔴 because no rule of the project's own can be written. The detector grade is 🔴 because 4.1 and 4.3 fail, both structural; 6.1, 6.2, 6.3 and 7.1 fail as well. A file that does not parse fails the compile with `javac`'s own errors and exits 1, ran. NullAway declares no version of this document.

## Clause by clause

| Document | Clause | Result       | Evidence                                                                                                                                                                                                                                                           |
| -------- | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Detector | 4.1    | No           | One check configured by options ([configuration](https://github.com/uber/NullAway/wiki/Configuration)); a new pattern needs a separate Error Prone check                                                                                                           |
| Detector | 4.2    | Yes          | `-XepDisableAllChecks -Xep:NullAway:ERROR` on one file, ran                                                                                                                                                                                                        |
| Detector | 4.3    | No           | No `name` in `@BugPattern`, so the class name `NullAway` ([`NullAway.java`](https://github.com/uber/NullAway/blob/v0.14.2/nullaway/src/main/java/com/uber/nullaway/NullAway.java)); reading 5                                                                      |
| Detector | 4.4    | No           | No rule over the rules                                                                                                                                                                                                                                             |
| Detector | 5.1    | Yes          | Runs inside a local `javac`, ran                                                                                                                                                                                                                                   |
| Detector | 5.2    | Yes          | One source file, ran                                                                                                                                                                                                                                               |
| Detector | 5.3    | Yes          | Findings in the compiler's output; exit 1 at `ERROR`, ran                                                                                                                                                                                                          |
| Detector | 5.4    | Yes          | Every finding is reported locally                                                                                                                                                                                                                                  |
| Detector | 6.1    | No           | One constant link for every finding, keyed on no identifier ([`ErrorProneCLIFlagsConfig.java`](https://github.com/uber/NullAway/blob/v0.14.2/nullaway/src/main/java/com/uber/nullaway/ErrorProneCLIFlagsConfig.java)); reading 11                                  |
| Detector | 6.2    | No           | No mechanism; no documentation in the jar, ran                                                                                                                                                                                                                     |
| Detector | 6.3    | No           | Documentation is the online wiki only                                                                                                                                                                                                                              |
| Detector | 6.4    | Not verified | No release check found                                                                                                                                                                                                                                             |
| Detector | 7.1    | No           | Its own `@SuppressWarnings` names survive `-XepIgnoreSuppressionAnnotations`, and `@lombok.Generated` cannot be un-excluded, ran ([`ErrorBuilder.java`](https://github.com/uber/NullAway/blob/v0.14.2/nullaway/src/main/java/com/uber/nullaway/ErrorBuilder.java)) |
| Detector | 7.2    | No           | `@SuppressWarnings` takes no reason                                                                                                                                                                                                                                |

## Notes for a practitioner

NullAway is worth running for the class it covers, but it cannot host a defence: write the project's own rule as an Error Prone check and run NullAway beside it. Raise it to `ERROR`, since a warning does not fail the compile. Because `-XepIgnoreSuppressionAnnotations` does not reach NullAway's own suppression names, a project that forbids them needs a check of its own on the host that reports `@SuppressWarnings("NullAway")`, `"NullAway.Init"`, `"NullAway.Optional"`, `"CheckNullabilityTypes"` and `@lombok.Generated` written by hand. `SuggestSuppressions` with Error Prone's patching adds a suppression at every existing finding in one pass; review what it writes rather than letting it stand as a baseline.

## Attributes

| Attribute      | Value                                                                                                              | Source                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| Kind           | Type checker (nullness), a check on the Error Prone host                                                           | [README](https://github.com/uber/NullAway/blob/v0.14.2/README.md)                  |
| Depth          | Semantic, with data flow within each method                                                                        | [how NullAway works](https://github.com/uber/NullAway/wiki/How-NullAway-Works)     |
| Output formats | `javac` diagnostics; fix serialisation writes error files for the NullAway annotator; no SARIF                     | ran, [configuration](https://github.com/uber/NullAway/wiki/Configuration)          |
| Exit codes     | 0 on a finding at the default `WARNING`, 1 at `ERROR`; 1 on a file that does not parse; 4 on missing configuration | ran                                                                                |
| Fix mode       | Suggested fixes through Error Prone patching, including `SuggestSuppressions`, which adds suppressions             | [suppressing warnings](https://github.com/uber/NullAway/wiki/Suppressing-Warnings) |
| Licence        | MIT                                                                                                                | [LICENSE.txt](https://github.com/uber/NullAway/blob/v0.14.2/LICENSE.txt)           |
