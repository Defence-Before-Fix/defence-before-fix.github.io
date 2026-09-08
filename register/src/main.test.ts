import { afterEach, describe, expect, it, vi } from "vitest";

describe("main", () => {
  afterEach(() => {
    document.body.replaceChildren();
    vi.unstubAllGlobals();
  });

  it("mounts the application into the page on load", async () => {
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
    document.body.append(host);
    await import("./main");
    await vi.waitFor(() =>
      expect(host.querySelector("[role='status']")).not.toBeNull(),
    );
  });
});
