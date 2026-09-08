import { describe, expect, it } from "vitest";

import { phpstan, register } from "../test/fixtures";
import { parseRegister } from "./parse";

describe("parseRegister", () => {
  it("accepts a well-formed register", () => {
    expect(parseRegister(JSON.parse(JSON.stringify(register)))).toEqual(
      register,
    );
  });

  it("rejects anything that is not a register", () => {
    expect(() => parseRegister(null)).toThrow(/not a register/);
    expect(() => parseRegister({ languages: [], tools: [{}] })).toThrow(
      /tool 0/,
    );
    expect(() =>
      parseRegister({
        languages: ["PHP"],
        tools: [{ ...phpstan, readiness: { mark: "🟢", level: "blue" } }],
      }),
    ).toThrow(/tool 0/);
  });
});
