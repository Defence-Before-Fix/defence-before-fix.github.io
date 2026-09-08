import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import { App } from "./App";
import { register } from "./test/fixtures";

function stubFetch(body: unknown, ok = true): void {
  vi.stubGlobal(
    "fetch",
    vi.fn(async () => ({ ok, status: ok ? 200 : 500, json: async () => body })),
  );
}

describe("App", () => {
  beforeEach(() => {
    window.location.hash = "";
  });

  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it("loads the register, filters it, and mirrors the filters into the hash", async () => {
    stubFetch(register);
    render(<App source="/tools/register.json" />);
    expect(
      await screen.findByRole("link", { name: "PHPStan" }),
    ).toBeInTheDocument();
    expect(screen.getByRole("status")).toHaveTextContent("4 of 4 tools");
    await userEvent.type(
      screen.getByRole("searchbox", { name: /search/i }),
      "ruff",
    );
    await waitFor(() =>
      expect(screen.getByRole("status")).toHaveTextContent("1 of 4 tools"),
    );
    expect(window.location.hash).toBe("#q=ruff");
    expect(screen.queryByRole("link", { name: "PHPStan" })).toBeNull();
  });

  it("starts from the filters in the hash", async () => {
    window.location.hash = "#kind=toolchain";
    stubFetch(register);
    render(<App source="/tools/register.json" />);
    expect(
      await screen.findByRole("link", { name: "php-qa-ci" }),
    ).toBeInTheDocument();
    expect(screen.getByRole("status")).toHaveTextContent("1 of 4 tools");
  });

  it("reports a failed load and tells the host", async () => {
    stubFetch({}, false);
    const onLoad = vi.fn();
    render(<App source="/tools/register.json" onLoad={onLoad} />);
    expect(await screen.findByRole("alert")).toHaveTextContent(
      /could not load/i,
    );
    expect(onLoad).toHaveBeenCalledWith("failed");
  });

  it("tells the host when the register is ready", async () => {
    stubFetch(register);
    const onLoad = vi.fn();
    render(<App source="/tools/register.json" onLoad={onLoad} />);
    await screen.findByRole("link", { name: "PHPStan" });
    expect(onLoad).toHaveBeenCalledWith("ready");
  });

  it("leaves a hash that is not a filter alone", async () => {
    window.location.hash = "#grades";
    stubFetch(register);
    render(<App source="/tools/register.json" />);
    await screen.findByRole("link", { name: "PHPStan" });
    expect(window.location.hash).toBe("#grades");
  });
});
