import { afterEach, describe, expect, it, vi } from "vitest";

import { mount } from "./mount";

describe("mount", () => {
  afterEach(() => {
    document.body.replaceChildren();
    vi.unstubAllGlobals();
  });

  it("renders the application into the mount point and hides the static fallback", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn(async () => ({
        ok: true,
        status: 200,
        json: async () => ({ languages: [], tools: [] }),
      })),
    );
    const host = document.createElement("div");
    host.id = "register-app";
    host.dataset["source"] = "/tools/register.json";
    const fallback = document.createElement("div");
    fallback.id = "register-static";
    document.body.append(host, fallback);
    expect(mount(document)).toBe(true);
    await vi.waitFor(() =>
      expect(host.querySelector("[role='status']")).not.toBeNull(),
    );
    expect(fallback.hidden).toBe(true);
  });

  it("keeps the static fallback visible when the register cannot be loaded", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn(async () => ({ ok: false, status: 404, json: async () => ({}) })),
    );
    const host = document.createElement("div");
    host.id = "register-app";
    const fallback = document.createElement("div");
    fallback.id = "register-static";
    document.body.append(host, fallback);
    expect(mount(document)).toBe(true);
    await vi.waitFor(() =>
      expect(host.querySelector("[role='alert']")).not.toBeNull(),
    );
    expect(fallback.hidden).toBe(false);
  });

  it("does nothing when there is no mount point", () => {
    expect(mount(document)).toBe(false);
  });
});
