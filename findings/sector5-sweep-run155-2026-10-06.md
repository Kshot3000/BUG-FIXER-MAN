# Sector 5 sweep — run 155 (2026-10-06)

Sector: (5) web apps / other OSS. **No submission.**

## Methodology note
Every candidate below was verified by a single direct `gh api` call
(issue body, comments, timeline cross-references), per the standing lesson
from runs 127/134/154 — no batched-scan data was used for any decision.

## Candidates direct-verified and rejected
- **twentyhq/twenty #27400** (filed today, prio: high) — `eq`/`is`/`like`/`ilike`
  can emit an un-parenthesized `OR` (null-equivalent widening) that escapes
  past an AND-ed sibling filter. Real and well-analysed, but the reporter
  (Atharva0222) already has the fix open as PR **#27401**. Reporter-owned.
- **twentyhq/twenty #27398** (filed today, prio: high) — `neq` (and `not`+`eq`)
  excludes NULL rows against real values (three-valued logic; plain `!=`).
  Same reporter, fix already open as PR **#27399**, and the issue is
  assigned to maintainer charlesBochet. Reporter-owned + assigned.
- **twentyhq/twenty #27402** — table re-render perf freeze; same reporter's
  coordinated batch, frontend-perf shaped, not verifiable to a quality fix
  in one run.
- **calcom/cal.com #30302** — booking page crashes `RangeError: Invalid time
  value` on invalid `?month=`/`?date=` params. Detailed report, 0 comments,
  no competing PR — but the reporter spells out the exact suggested fix and
  states "I'm happy to open a PR for this." Reporter-offered; not raced.
- **directus/directus #28297** — `weekday()` numbering differs per DB vendor.
  The reporter explicitly asks maintainers to choose the canonical numbering
  before any code is written ("I would rather not pick unilaterally… just
  say which one and I will open the PR"), and the issue is Linear-tracked
  (CMS-3135). Maintainer-decision gate + reporter-owned.
- **directus/directus #28325** — public-policy warning/confirmation only
  covers the seeded Public policy ID. Real exposure gap, but the remedy is a
  broad product/security-UX decision across API, roles UI, drawers, flows
  and import — not a bounded verified fix.
- **mealie-recipes/mealie #8628** — concurrent recipe writes duplicate
  ingredient rows. Full root-cause in the report: the write path rebuilds
  the whole ingredient collection via `auto_init`/`handle_one_to_many_list`
  with no `id` on the write schema, so overlapping saves insert fresh rows.
  The fix is architectural (transaction/locking/reconciliation semantics in
  shared ORM model utils used by every model) — not tractable to a safe,
  verified fix in one run.
- **documenso/documenso #3403** — signature pad draws a stray stroke from
  the click that opens the dialog. Claimed within an hour of filing by
  contributor ius-sharma, with the fix approach spelled out. Claimed.
- **nocodb/nocodb #14765** — "url-fields not exported": three-line body, no
  export format/view/repro detail. Vague (standing reject from run 150).
- **nocodb/nocodb #14761** — Excel download URL served over http behind an
  HTTPS deployment (mixed-content block). Reporter-infra specific, tied to
  closed #14617 the reporter cannot reopen; no code path pinned in the
  report. Not verifiable locally in one run.
- **outline/outline #13977** — lists inside table cells lost on Markdown
  round-trip. Linear-tracked (standing reject from run 150).
- **chatwoot / payload / memos / vikunja fresh heads** — our own open PRs,
  reporter PRs, or feature requests only.
- **appwrite/appwrite fresh heads** — team-posted feature tasks.
- **supabase / formbricks fresh heads** — nothing new; formbricks' only
  fresh item is our held #9526.

## Watch
No changes (see hidden status-watch ledger for run 155 detail).
$0 requested, $0 received.
