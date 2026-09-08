import { render, screen, within } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";

import { phpQaCi, phpstan } from "../test/fixtures";
import { RegisterTable } from "./RegisterTable";

describe("RegisterTable", () => {
  it("renders one row per tool with a linked name and linked note clauses", () => {
    render(
      <RegisterTable
        tools={[phpQaCi, phpstan]}
        sort={{ key: "default", direction: "asc" }}
        onSort={vi.fn()}
      />,
    );
    const rows = screen.getAllByRole("row");
    expect(rows).toHaveLength(3);
    const phpstanRow = rows[2];
    if (phpstanRow === undefined) {
      throw new Error("expected a third row");
    }
    expect(
      within(phpstanRow).getByRole("link", { name: "PHPStan" }),
    ).toHaveAttribute("href", "/tools/phpstan.html");
    expect(
      within(phpstanRow).getByRole("link", { name: "6.2" }),
    ).toHaveAttribute("href", "/DETECTOR-SPEC.html#62-resolution");
  });

  it("reports a sort request when a column header is clicked and marks the active column", async () => {
    const onSort = vi.fn();
    render(
      <RegisterTable
        tools={[phpQaCi]}
        sort={{ key: "name", direction: "asc" }}
        onSort={onSort}
      />,
    );
    const name = screen.getByRole("columnheader", { name: "Tool" });
    expect(name).toHaveAttribute("aria-sort", "ascending");
    await userEvent.click(within(name).getByRole("button"));
    expect(onSort).toHaveBeenCalledWith("name");
  });

  it("says so when nothing matches", () => {
    render(
      <RegisterTable
        tools={[]}
        sort={{ key: "default", direction: "asc" }}
        onSort={vi.fn()}
      />,
    );
    expect(screen.getByText(/no tools match/i)).toBeInTheDocument();
  });
});
