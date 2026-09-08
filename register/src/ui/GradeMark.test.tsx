import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { GradeMark } from "./GradeMark";

describe("GradeMark", () => {
  it("shows the mark with the level as an accessible label", () => {
    render(
      <GradeMark grade={{ mark: "🟢", level: "green" }} column="readiness" />,
    );
    const cell = screen.getByLabelText("Readiness: green");
    expect(cell).toHaveAttribute("data-level", "green");
    expect(cell.querySelector(".register-dot")).not.toBeNull();
  });

  it("renders a middle dot for a grade that does not apply", () => {
    render(
      <GradeMark grade={{ mark: "·", level: "none" }} column="toolchain" />,
    );
    expect(
      screen.getByLabelText("Toolchain: not applicable"),
    ).toHaveTextContent("·");
  });
});
