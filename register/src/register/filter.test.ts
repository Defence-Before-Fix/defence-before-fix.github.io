import { describe, expect, it } from "vitest";

import { biome, phpQaCi, phpstan, register, ruff } from "../test/fixtures";
import {
  apply,
  decode,
  defaultFilters,
  encode,
  noteText,
  sortTools,
} from "./filter";

describe("defaultFilters", () => {
  it("selects everything and sorts in register order", () => {
    const f = defaultFilters();
    expect(f.query).toBe("");
    expect(f.languages).toEqual([]);
    expect(f.kinds).toEqual([]);
    expect(f.sort).toEqual({ key: "default", direction: "asc" });
  });
});

describe("apply", () => {
  it("matches the query against name, language and notes, case-insensitively", () => {
    expect(
      apply(register, { ...defaultFilters(), query: "phpstan" }).map(
        (t) => t.slug,
      ),
    ).toEqual(["phpstan"]);
    expect(
      apply(register, { ...defaultFilters(), query: "DOCUMENTATION" }).map(
        (t) => t.slug,
      ),
    ).toEqual(["phpstan"]);
    expect(
      apply(register, { ...defaultFilters(), query: "python" }).map(
        (t) => t.slug,
      ),
    ).toEqual(["ruff"]);
    expect(apply(register, { ...defaultFilters(), query: "tool" })).toEqual([]);
  });

  it("narrows by language, kind and grade level together", () => {
    const f = defaultFilters();
    expect(
      apply(register, { ...f, languages: ["PHP"] }).map((t) => t.slug),
    ).toEqual(["php-qa-ci", "phpstan"]);
    expect(
      apply(register, { ...f, kinds: ["toolchain"] }).map((t) => t.slug),
    ).toEqual(["php-qa-ci"]);
    expect(
      apply(register, {
        ...f,
        grades: { ...f.grades, readiness: ["green"] },
      }).map((t) => t.slug),
    ).toEqual(["php-qa-ci", "phpstan"]);
    expect(
      apply(register, {
        ...f,
        languages: ["PHP"],
        grades: { ...f.grades, detector: ["red"] },
      }).map((t) => t.slug),
    ).toEqual([]);
  });
});

describe("sortTools", () => {
  it("keeps register order by default: language order, toolchains first, then name", () => {
    expect(
      sortTools([ruff, biome, phpstan, phpQaCi], register.languages, {
        key: "default",
        direction: "asc",
      }),
    ).toEqual([phpQaCi, phpstan, biome, ruff]);
  });

  it("sorts by a grade with green first, and reverses on descending", () => {
    const asc = sortTools(register.tools, register.languages, {
      key: "readiness",
      direction: "asc",
    });
    expect(asc.map((t) => t.readiness.level)).toEqual([
      "green",
      "green",
      "amber",
      "red",
    ]);
    const desc = sortTools(register.tools, register.languages, {
      key: "readiness",
      direction: "desc",
    });
    expect(desc.map((t) => t.readiness.level)).toEqual([
      "red",
      "amber",
      "green",
      "green",
    ]);
  });

  it("sorts by name without regard to case", () => {
    expect(
      sortTools(register.tools, register.languages, {
        key: "name",
        direction: "asc",
      }).map((t) => t.name),
    ).toEqual(["Biome", "php-qa-ci", "PHPStan", "Ruff"]);
  });
});

describe("encode and decode", () => {
  it("round-trips through the URL hash and omits defaults", () => {
    expect(encode(defaultFilters())).toBe("");
    const f = {
      ...defaultFilters(),
      query: "php stan",
      languages: ["PHP", "Python"],
      kinds: ["tool" as const],
      grades: {
        ...defaultFilters().grades,
        detector: ["amber" as const, "red" as const],
      },
      sort: { key: "name" as const, direction: "desc" as const },
    };
    const hash = encode(f);
    expect(hash).toContain("q=php+stan");
    expect(decode(hash)).toEqual(f);
  });

  it("ignores values it does not know", () => {
    const f = decode(
      "kind=toolchain,rocket&sort=colour:up&detector=purple&lang=PHP",
    );
    expect(f.kinds).toEqual(["toolchain"]);
    expect(f.sort).toEqual({ key: "default", direction: "asc" });
    expect(f.grades.detector).toEqual([]);
    expect(f.languages).toEqual(["PHP"]);
  });
});

describe("noteText", () => {
  it("joins the segments", () => {
    expect(noteText(phpstan)).toBe(
      "Bundled documentation online only fails 6.2 and 6.3.",
    );
  });
});
