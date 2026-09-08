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
    expect(fallback.hidden).toBe(true);
    await vi.waitFor(() =>
      expect(host.querySelector("[role='status']")).not.toBeNull(),
    );
  });

  it("does nothing when there is no mount point", () => {
    expect(mount(document)).toBe(false);
  });
});
