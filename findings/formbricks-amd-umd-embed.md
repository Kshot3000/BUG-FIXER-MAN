# formbricks/formbricks #9526 — HTML embed + SDK lazy load break on pages with an AMD loader

- **Issue:** https://github.com/formbricks/formbricks/issues/9526 (filed 2026-10-06T10:09Z, `bug`, unassigned; one comment — Vladokvl asking for assignment, not yet assigned)
- **Submission:** PR creation from the fork was denied by GitHub (GraphQL: "Kshot3000 does not have the correct permissions to execute CreatePullRequest"; REST create returned 404 — same venue pattern as MystenLabs/ts-sdks). Fix reported on the issue instead: https://github.com/formbricks/formbricks/issues/9526#issuecomment-6015767540
- **Ready branch:** https://github.com/Kshot3000/formbricks/tree/fix/9526-amd-safe-umd-loads — commit `b8cc846` (GitHub-verified SSH signature), based on upstream `708bd54`

## Bug

Both Formbricks browser bundles are UMD-only builds (`packages/js-core/vite.config.ts` lib name `formbricks`; `packages/surveys/vite.config.mts` lib name `formbricksSurveys`, `formats: ["umd"]`). A UMD wrapper prefers the AMD branch whenever the host page exposes `define` with `define.amd` (RequireJS and similar), and then never assigns its browser global. Two load paths depend on the global branch:

1. The default HTML embed loads `formbricks.umd.cjs` and calls `window.formbricks.setup(...)` — under AMD, `window.formbricks` is never set. The setup-page snippet also guessed timing with a 500 ms `setTimeout` (the docs copies already use `onload`).
2. The SDK itself: `loadFormbricksSurveysExternally` in `packages/js-core/src/lib/survey/widget.ts` injects `surveys.umd.cjs` and polls for `window.formbricksSurveys` — under AMD the global never appears, the poll times out after 10 s, and the survey silently never renders. This path cannot be fixed from the embed snippet.

## Fix (branch `fix/9526-amd-safe-umd-loads`, 4 files, +88/−2)

- `packages/js-core/src/lib/survey/widget.ts`: hide `window.define` while the injected surveys script executes; restore the host page's loader in `onload` and `onerror`.
- `packages/js-core/src/vite-env.d.ts`: declare `define?: unknown` on the `Window` interface.
- `apps/web/modules/workspaces/settings/(setup)/app-connection/page.tsx` (both snippet copies): same hide/restore around the entry bundle; `setup()` runs from the script's `onload` instead of the 500 ms timer, `onerror` restores the loader.

## Proof (red → green)

- Real upstream test file, standalone harness (js-core has no external runtime deps) with the repo's pinned Vitest 4.1.11: two new tests in `widget.test.ts` — "`define` hidden during load, restored on load" and "restored on error" — **fail on pristine `widget.ts`** and **pass patched; full file 40/40 patched**. Disclosure: on pristine code the first failure also leaves the load promise pending, so the following nonce test fails in that state too (knock-on of the aborted test, not a separate regression). An earlier harness run under Vitest 3 showed 14 failures including pre-existing tests — a version artifact, discarded.
- Embed snippet exercised in Node against a simulated UMD bundle on a page with `define.amd`: old snippet → bundle registers with AMD, `window.formbricks` never set; new snippet → global set, `define` restored after load, `setup()` called with the workspace id/app URL. Harnesses kept in the goal's hidden_files (`formbricks-harness/`, `snippet-test.mjs`, `snippet-test-old.mjs`).
- `tsc` check on the touched sources: no errors in the changed files (one pre-existing harness artifact in an untouched file from missing `@types/node` in the sandbox).

## Open gaps

- Full pnpm workspace install unavailable in the sandbox; js-core suite ran standalone against the package's real sources, disclosed on the issue.
- Snippet copies under `docs/` still use the older form.
- While a bundle loads, host-page code running in that window sees no AMD loader; restored on load/error (standard UMD-guard trade-off).

## Payment

None — no bounty posted on the issue; fix offered freely. $0 requested, $0 received.
