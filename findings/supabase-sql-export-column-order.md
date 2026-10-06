# supabase/supabase — Studio SQL export silently swaps values for numeric column names

- **Issue:** https://github.com/supabase/supabase/issues/51330 (filed 2026-10-06, unassigned, 0 comments at claim time; no competing PR — the open PRs the reporter referenced address identifier quoting / JSON escaping, a different behavior)
- **PR:** https://github.com/supabase/supabase/pull/51340 — OPEN, MERGEABLE, commit `76494db` GitHub-verified (SSH-signed)
- **Sector:** (4) general company OSS / dev tools — run 129. This was the top held candidate from the run-125 late scan.

## Bug

`formatTableRowsToSQL` in `apps/studio/components/interfaces/TableGridEditor/TableEntity.utils.ts` (used by Table Editor "Copy as SQL" and "Export as SQL") built the INSERT column list from table metadata but built each VALUES tuple from `Object.entries(row)`. JavaScript enumerates integer-like keys before all other string keys (ascending numeric order), so for a table with columns `id`, `"2024"`, `"2023"` and a row `(7, 99, 42)` the export produced:

```sql
INSERT INTO public.yearly_totals (id, "2024", "2023") VALUES (42, 99, 7);
```

PostgreSQL accepts that statement (all-integer columns), so a restore silently lands values in the wrong columns. The same code also deleted `idx` from every row unconditionally: a table with a real column named `idx` exported one value too few for its column list.

## Proof (red → green)

- Standalone reproduction of the exact enumeration logic: `Object.entries` on the JSON-parsed row `{"id":7,"2024":99,"2023":42}` yields `2023=42, 2024=99, id=7` → VALUES `(42, 99, 7)`; deleting `idx` from `{"idx":5,"name":"x"}` leaves one value for two columns.
- Added two regression tests to the existing `TableEntity.utils.test.ts` suite (integer-like column names keep column order; a real `idx` column keeps its value). Against the unpatched formatter: **2 failed / 12 passed**. Against the patched formatter: **14/14 passed**. Tests were run with vitest 3 in a minimal harness around the real source/test files (the `@supabase/pg-meta` `ident` import stubbed faithfully — bare for safe identifiers, double-quoted otherwise — because the full pnpm workspace install is not available in this sandbox; repo CI runs the real suite). Prettier check with the repo's core options passes.

## Fix

Map each row's values through `table.columns` — the same list the INSERT column list is built from — instead of enumerating the row object. Synthetic row keys such as the grid's `idx` are excluded by construction (they are not table columns), preserving the existing grid-`idx` removal behavior while keeping a real `idx` column's value. The per-value formatting logic (null / array / JSON / string escaping) is unchanged. Diff: +50/−5 across the source and test files.

## Submission status

PR #51340 open upstream; checks at submission: MERGEABLE, bot comments only (Vercel / welcome bot), Vercel preview deploys show "Authorization required" (standard for external fork PRs, not a code failure), CodeRabbit review pending. Added to the status watch.

## Payment

None — no bounty was posted on #51330; the fix is offered freely. $0 requested, $0 received.
