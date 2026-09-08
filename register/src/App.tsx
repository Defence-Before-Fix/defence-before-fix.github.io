import { useEffect, useMemo, useState } from "react";

import { apply, decode, defaultFilters, encode } from "./register/filter";
import { parseRegister } from "./register/parse";
import type { Filters, Register, SortKey } from "./register/types";
import { FilterBar } from "./ui/FilterBar";
import { RegisterTable } from "./ui/RegisterTable";

interface AppProps {
  source: string;
}

type Loaded =
  | { state: "loading" }
  | { state: "ready"; register: Register }
  | { state: "failed"; detail: string };

function nextSort(filters: Filters, key: SortKey): Filters {
  const flip = filters.sort.key === key && filters.sort.direction === "asc";
  return { ...filters, sort: { key, direction: flip ? "desc" : "asc" } };
}

export function App({ source }: AppProps) {
  const [loaded, setLoaded] = useState<Loaded>({ state: "loading" });
  const [filters, setFilters] = useState<Filters>(defaultFilters);

  useEffect(() => {
    setFilters(decode(window.location.hash));
    const onHashChange = () => setFilters(decode(window.location.hash));
    window.addEventListener("hashchange", onHashChange);
    return () => window.removeEventListener("hashchange", onHashChange);
  }, []);

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
    const encoded = encode(filters);
    const current = window.location.hash.replace(/^#/, "");
    if (encoded !== current) {
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
