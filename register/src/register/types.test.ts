import { describe, expect, it } from "vitest";

import { GRADE_COLUMNS } from "./types";

describe("GRADE_COLUMNS", () => {
  it("names the four graded columns in register order", () => {
    expect(GRADE_COLUMNS).toEqual([
      "readiness",
      "detector",
      "toolchain",
      "project",
    ]);
  });
});
