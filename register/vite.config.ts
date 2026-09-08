import react from "@vitejs/plugin-react";
import { defineConfig } from "vitest/config";

// The application is served from /tools/app/ on the site and mounted by tools/index.md, so
// the output file names are fixed rather than hashed: the page links them by name.
export default defineConfig({
  plugins: [react()],
  base: "/tools/app/",
  build: {
    outDir: "dist",
    emptyOutDir: true,
    rollupOptions: {
      input: "src/main.ts",
      output: {
        entryFileNames: "register.js",
        chunkFileNames: "register-[name].js",
        assetFileNames: "register.[ext]",
      },
    },
  },
  test: {
    environment: "jsdom",
    globals: true,
    setupFiles: ["src/test/setup.ts"],
    css: false,
  },
});
