# usememos/memos — new memos all get the same createTime while a date filter is active

- **Project:** usememos/memos (self-hosted note-taking app)
- **Issue:** [#6434](https://github.com/usememos/memos/issues/6434) — filed 2026-10-06, 0 comments, unassigned, no competing PR
- **PR:** [#6435](https://github.com/usememos/memos/pull/6435) — OPEN / MERGEABLE, commit 4b4f464 GitHub-verified (SSH signature valid)
- **Bounty:** none posted on the issue; fix offered freely, tips welcome via the PR footer. $0 requested, $0 received.

## Bug

With a `displayTime` date filter active on Home (e.g. after clicking a day in the sidebar calendar), every memo created from the composer was stored with the **same** `createTime`: the moment the filter was applied, not the moment of saving. The reporter's table: memos saved at 13:17:40 / 13:17:55 / 13:18:10 all stored as **13:17:23** — within-day order lost. The same applied to the calendar day panel composer.

Cause (traced by the reporter, confirmed in source at main f7a6186): the default is computed once and memoized (`Home.tsx` `useMemo(..., [filters])`; `CalendarView.tsx` the same with `[activeDate]`), seeded into the editor state as that exact `Date` object (`useMemoInit` + the live-sync effect in `MemoEditor/index.tsx`), and restored verbatim after every save (`useMemoSave`: "restore calendar-derived values for the next memo"). This contradicts the helper's own doc comment: the filtered date "combined with `now`'s wall-clock hh:mm:ss, so a memo composed for a past day still orders naturally within it."

## Fix (the issue's suggested small fix, adapted to the real save path)

- `web/src/components/MemoEditor/utils/deriveDefaultCreateTime.ts`: adds `withTimeOfDay(date, now)` (same calendar date, `now`'s hh:mm:ss, input not mutated) and `restampUntouchedDefault(time, defaultCreateTime, now)` — re-stamps only when `time` is still the untouched default (same `Date` reference). A timestamp picked in the TimestampPopover is a new `Date` object and passes through unchanged, so manual back-dating is preserved.
- `web/src/components/MemoEditor/hooks/useMemoSave.ts`: before creating a memo (`!memoName`), builds the save state with re-stamped `createTime`/`updateTime`. Edit mode owns its timestamps and is untouched; the post-save restore still re-seeds the default, so each subsequent save re-stamps again.

Deliberately out of scope (stated in the PR): the issue's design question — whether Home's browsing filter should derive a write default at all — is left for maintainers; this PR only makes the existing #5925 feature behave as documented. The composer's displayed timestamp still shows the filter time while composing (also noted in the issue).

## Proof (red → green)

- New tests in `web/tests/derive-default-create-time.test.ts` (6 added): on the unpatched tree, 6 fail / 6 existing pass; patched, **12/12 pass** — including consecutive saves from one composer getting distinct times (13:17:40 vs 13:17:55 against a 13:17:23 default), a past filtered date keeping its date while re-stamping the time of day, and a manually picked timestamp passing through by reference.
- `pnpm lint` clean (tsc --noEmit + Biome, 694 files; one formatter fix applied to the new function signature).
- Full frontend suite `pnpm test`: **194 files / 1,778 tests, all passing** (run locally, ~9.5 min in this sandbox).
- Repo's AGENTS.md explicitly documents AI-agent working rules; diff kept scoped (3 files, +111/−2), local patterns followed, no generated files touched.

## Same-run sector-5 rejects

- payload #18521 → PR #18526 already open (timeline-verified); chatwoot fresh = known rejects (#16139 feature, #16133 instance schema); gitea #39618 → maintainer fix PR #39619 already posted; gitea #39623 Windows/Bleve file-locking, env-bound; navidrome #6276 no repro steps / external files / config-specific, #6266 maintainer (deluan) actively diagnosing an environment-bound artwork crash; vikunja fresh = only our own #4109/#4104 plus a DB-specific migration failure #4102; immich #32146 iOS-widget mTLS (platform-bound); outline fresh = ChatGPT-plugin feature specs; supabase fresh = hosted-service tickets; global fresh-`bug` search = tiny farm repos only.

## Watch (run 110)

NO changes: all PR states direct-verified identical to run 109 (dentalpin #599 / type-coverage #155 MERGED known; ERCs #2045, cake #3671, electrum #11012/#11013, ansible #87642, NiceGUI #6372 with evnchn APPROVED standing, vyper #5294, vikunja #4107/#4110, socket-plugs #162, gitea #39611, payload #18509, chatwoot #16130, gofactory #67 all OPEN, counts unchanged). Expensify identical: #102072 60, #101684 42, #102044 30, #102226 38 — no selection/hire, no melvin-bot prompt to Kshot3000. HackerOne: ledger-only. **NEW watch item: memos PR #6435.**

## Follow-up (run 112, 2026-10-06)

CodeRabbit reviewed PR #6435 (COMMENTED, 07:01Z) with one valid minor
catch: `setHours` was called without the milliseconds argument, so a
re-stamped time kept the default date's milliseconds and two saves
within the same second could still share one timestamp. Fixed in
commit 26e8253 (pushed to the PR branch, PR head verified): both
`withTimeOfDay` and `deriveDefaultCreateTimeFromDate` now pass
`now.getMilliseconds()`, plus a regression test for two saves in the
same second — file suite 13/13. Noted on the PR
(comment 6011403793).
