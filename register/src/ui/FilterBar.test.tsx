import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";

import { defaultFilters } from "../register/filter";
import { FilterBar } from "./FilterBar";

const languages = ["PHP", "Python"];

describe("FilterBar", () => {
  it("emits an updated query as the user types", async () => {
    const onChange = vi.fn();
    render(
      <FilterBar
        filters={defaultFilters()}
        languages={languages}
        shown={4}
        total={4}
        onChange={onChange}
      />,
    );
    await userEvent.type(
      screen.getByRole("searchbox", { name: /search/i }),
      "p",
    );
    expect(onChange).toHaveBeenLastCalledWith({
      ...defaultFilters(),
      query: "p",
    });
  });

  it("toggles a language, a kind and a grade level", async () => {
    const onChange = vi.fn();
    render(
      <FilterBar
        filters={defaultFilters()}
        languages={languages}
        shown={4}
        total={4}
        onChange={onChange}
      />,
    );
    await userEvent.click(screen.getByRole("checkbox", { name: "PHP" }));
    expect(onChange).toHaveBeenLastCalledWith({
      ...defaultFilters(),
      languages: ["PHP"],
    });
    await userEvent.click(screen.getByRole("checkbox", { name: "Toolchain" }));
    expect(onChange).toHaveBeenLastCalledWith({
      ...defaultFilters(),
      kinds: ["toolchain"],
    });
    await userEvent.click(
      screen.getByRole("checkbox", { name: "Detector: green" }),
    );
    expect(onChange).toHaveBeenLastCalledWith({
      ...defaultFilters(),
      grades: { ...defaultFilters().grades, detector: ["green"] },
    });
  });

  it("shows the count and offers a reset only when something is filtered", async () => {
    const onChange = vi.fn();
    const { rerender } = render(
      <FilterBar
        filters={defaultFilters()}
        languages={languages}
        shown={4}
        total={4}
        onChange={onChange}
      />,
    );
    expect(screen.getByRole("status")).toHaveTextContent("4 of 4 tools");
    expect(screen.queryByRole("button", { name: /reset/i })).toBeNull();
    rerender(
      <FilterBar
        filters={{ ...defaultFilters(), query: "x" }}
        languages={languages}
        shown={1}
        total={4}
        onChange={onChange}
      />,
    );
    await userEvent.click(screen.getByRole("button", { name: /reset/i }));
    expect(onChange).toHaveBeenLastCalledWith(defaultFilters());
  });
});
