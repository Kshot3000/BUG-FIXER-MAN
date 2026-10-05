# payloadcms/payload — plugin-ecommerce variant joins silently capped at 10 (PR #18509)

- **Issue:** https://github.com/payloadcms/payload/issues/18498 (filed 2026-10-05 by klaatu-code, label Bug, 0 comments, unassigned, no competing PR — timeline-verified)
- **PR:** https://github.com/payloadcms/payload/pull/18509 — OPEN / MERGEABLE (2026-10-05, base main), branch `Kshot3000/payload@fix/18498-plugin-ecommerce-join-limit` (cf03368)
- **Payment:** none — no bounty posted on the issue; fix offered freely, tips welcome via the PR footer.

## Bug
`plugin-ecommerce` read two join fields without passing a `limit`, so both fell back to the drizzle adapter's join default (`field.defaultLimit ?? 10`, verified in `packages/drizzle/src/find/traverseFields.ts:398`):

1. `VariantOptionsSelector` loaded each variant type's `options` join with only `sort: 'value'` → only the first 10 options of a type were ever offered; options 11+ were unselectable with no warning.
2. `validateOptions` loaded the product's `variants` join with no limit and duplicate-checked against `product.variants.docs` → a combination already used by an 11th or later variant passed validation and could be saved twice (data integrity). The selector's `ErrorBox` duplicate warning, fed by a product read with no joins argument, had the same blind spot.

Related (flagged as "minor" in the issue, verified broader): `validateOptions` looked up all four of its messages under `ecommerce:`, but the plugin registers translations only under `plugin-ecommerce:` (merge in `src/index.ts`) — it was the only file in the plugin using the wrong prefix, so none of its messages resolved (`key not found: ecommerce:variantOptionsAlreadyExists` in the server log; callers get only the generic field error).

## Fix (the issue's own suggested approach)
Explicit `limit: 0` (unbounded, adapter-supported) at all three call sites — selector options join, selector product read (`joins: { variants: { limit: 0 } }`), and the validator's sibling-variants join — plus the `ecommerce:` → `plugin-ecommerce:` namespace correction for all four keys in `validateOptions.ts` (existing `@ts-expect-error` comments kept; other plugin files use the same pattern for `plugin-ecommerce:` keys). New integration test in `test/plugin-ecommerce/int.spec.ts`: product with 11 variants, duplicate of every existing combination must be rejected; cleans up after itself (suite uses `resetBetweenTests: false`).

## Proof (red → green, reporter's own repro)
Cloned https://github.com/klaatu-code/payload-ecommerce-variant-limit-repro (SQLite, published `@payloadcms/plugin-ecommerce` 3.90.2) and ran it in this sandbox (Node 24.20):

- **Unpatched:** output character-for-character the issue's — 12 options in DB, 10 offered (`white`, `yellow` missing); 11 variants on product, validator compares against 10; control duplicate rejected; **duplicate of the oldest variant SAVED**; `key not found: ecommerce:variantOptionsAlreadyExists` logged. `Result: bug1=REPRODUCED bug2=REPRODUCED`.
- **Patched** (published package's compiled dist patched with exactly the PR's changes): selector query returns 12/12 options, validator sees 11/11 siblings, no duplicate saved (`bug1=not reproduced bug2=not reproduced`).
- **Isolation run** (original repro script, only the plugin patched): the duplicate of the out-of-window variant is now "rejected as expected" by the real `validateOptions` hook, and the `key not found` log is gone — proving the validator + i18n fixes end-to-end, independent of the script's own hardcoded queries.

Honest limitation (disclosed in the PR): the monorepo integration suite was not run locally (needs full pnpm install + core build); the new test follows the suite's fixture/seed patterns — CI authoritative. Changed files Prettier-clean under the repo's `.prettierrc.json`; TS transpile syntax check 0 errors. Venue note: Payload's CONTRIBUTING explicitly lists AI tooling (Claude Code) as supported; no CLA found.

## Same-run sector-5 rejects
- directus #28318 (falsy-PK getKeysByQuery) → maintainer Nitwel's own PR #28319 already open; #28235 → PRs #28236/#28239; #28288 → PR #28291; #28295 claimed in-thread + needs live Postgres/WS; #28322 no repro steps, root cause speculative.
- outline #13528 (diagrams.net embed key mismatch) → maintainer tommoor's PR #13556 already open.
- payload #18491 → cross-ref PR #18495; #18489 → cross-ref #18488.
