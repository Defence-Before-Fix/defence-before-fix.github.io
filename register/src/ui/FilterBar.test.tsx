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

  it("narrows by language, kind and a grade through labelled selects", async () => {
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
    await userEvent.selectOptions(
      screen.getByRole("combobox", { name: "Language" }),
      "PHP",
    );
    expect(onChange).toHaveBeenLastCalledWith({
      ...defaultFilters(),
      languages: ["PHP"],
    });
    await userEvent.selectOptions(
      screen.getByRole("combobox", { name: "Kind" }),
      "toolchain",
    );
    expect(onChange).toHaveBeenLastCalledWith({
      ...defaultFilters(),
      kinds: ["toolchain"],
    });
    await userEvent.selectOptions(
      screen.getByRole("combobox", { name: "Detector conformance" }),
      "green",
    );
    expect(onChange).toHaveBeenLastCalledWith({
      ...defaultFilters(),
      grades: { ...defaultFilters().grades, detector: ["green"] },
    });
  });

  it("returns a select to any and reflects a chosen value", async () => {
    const onChange = vi.fn();
    render(
      <FilterBar
        filters={{ ...defaultFilters(), languages: ["PHP"] }}
        languages={languages}
        shown={2}
        total={4}
        onChange={onChange}
      />,
    );
    const language = screen.getByRole("combobox", { name: "Language" });
    expect(language).toHaveValue("PHP");
    await userEvent.selectOptions(language, "");
    expect(onChange).toHaveBeenLastCalledWith(defaultFilters());
  });

  it("names the grade levels in words, not marks alone", () => {
    render(
      <FilterBar
        filters={defaultFilters()}
        languages={languages}
        shown={4}
        total={4}
        onChange={vi.fn()}
      />,
    );
    expect(
      screen.getAllByRole("option", { name: /green/i }).length,
    ).toBeGreaterThan(0);
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
