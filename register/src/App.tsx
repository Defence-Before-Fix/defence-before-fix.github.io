import { useEffect, useMemo, useRef, useState } from "react";

import { apply, decode, defaultFilters, encode } from "./register/filter";
import { parseRegister } from "./register/parse";
import type { Filters, Register, SortKey } from "./register/types";
import { FilterBar } from "./ui/FilterBar";
import { RegisterTable } from "./ui/RegisterTable";

export type LoadState = "ready" | "failed";

interface AppProps {
  source: string;
  onLoad?: (state: LoadState) => void;
}

// A hash the application did not write, such as #grades, is left alone; only a hash that
// round-trips through the filter codec belongs to the application.
function isFilterHash(hash: string): boolean {
  return hash === "" || encode(decode(hash)) === hash;
}

type Loaded =
  | { state: "loading" }
  | { state: "ready"; register: Register }
  | { state: "failed"; detail: string };

function nextSort(filters: Filters, key: SortKey): Filters {
  const flip = filters.sort.key === key && filters.sort.direction === "asc";
  return { ...filters, sort: { key, direction: flip ? "desc" : "asc" } };
}

export function App({ source, onLoad }: AppProps) {
  const [loaded, setLoaded] = useState<Loaded>({ state: "loading" });
  const [filters, setFilters] = useState<Filters>(defaultFilters);
  const fromHash = useRef(false);

  useEffect(() => {
    const read = () => {
      fromHash.current = true;
      setFilters(decode(window.location.hash));
    };
    read();
    window.addEventListener("hashchange", read);
    return () => window.removeEventListener("hashchange", read);
  }, []);

  useEffect(() => {
    if (loaded.state !== "loading") {
      onLoad?.(loaded.state);
    }
  }, [loaded, onLoad]);

  useEffect(() => {
    let cancelled = false;
    fetch(source)
      .then(async (response) => {
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }
        const body: unknown = await response.json();
        return parseRegister(body);
      })
      .then((register) => {
        if (!cancelled) {
          setLoaded({ state: "ready", register });
        }
      })
      .catch((error: unknown) => {
        if (!cancelled) {
          setLoaded({
            state: "failed",
            detail: error instanceof Error ? error.message : String(error),
          });
        }
      });
    return () => {
      cancelled = true;
    };
  }, [source]);

  useEffect(() => {
    if (fromHash.current) {
      fromHash.current = false;
      return;
    }
    const encoded = encode(filters);
    const current = window.location.hash.replace(/^#/, "");
    if (encoded !== current && (encoded !== "" || isFilterHash(current))) {
      window.history.replaceState(
        null,
        "",
        encoded === "" ? window.location.pathname : `#${encoded}`,
      );
    }
  }, [filters]);

  const shown = useMemo(
    () => (loaded.state === "ready" ? apply(loaded.register, filters) : []),
    [loaded, filters],
  );

  if (loaded.state === "loading") {
    return <p className="register-loading">Loading the register…</p>;
  }
  if (loaded.state === "failed") {
    return (
      <p className="register-error" role="alert">
        Could not load the register ({loaded.detail}). The static table below is
        the same data.
      </p>
    );
  }
  return (
    <div className="register-app">
      <FilterBar
        filters={filters}
        languages={loaded.register.languages}
        shown={shown.length}
        total={loaded.register.tools.length}
        onChange={setFilters}
      />
      <RegisterTable
        tools={shown}
        sort={filters.sort}
        onSort={(key) => setFilters((f) => nextSort(f, key))}
      />
    </div>
  );
}
