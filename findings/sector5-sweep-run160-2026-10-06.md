# Sector 5 sweep — run 160 (2026-10-06)

**Result: NO submission.** Fresh web/other-OSS queues direct-verified singly; every tractable candidate was already PR'd, reporter-owned, or not cleanly verifiable in one run.

## Candidates checked
- **calcom/cal.com #30300** (event-type update toast shows previous title; reporter diagnosed the stale-prop cause across web + platform wrappers) — already fixed by the reporter's own open PR **#30301**. #30302 remains reporter-offered from run 155.
- **knadh/listmonk #3253** (GET /api/lists/{id} returns subscriber_count at exactly 2×; reporter root-caused the double-add in `Core.GetList` over the SQL aggregate) — already fixed by open PR **#3255** (biofool).
- **actualbudget/actual #9111** ("Post Transaction Today" leaves the upcoming scheduled transaction, which then posts again) — ambiguous semantics: reporter says behavior changed "for the last few months," no root cause, deep schedule logic; not verifiable as a bug vs. intended change in one run. **#9116** — mobile search term cleared after each edit; UX-state scope, vague.
- **mealie-recipes/mealie #8635** — AI import with "Translate recipe" zeroes servings/yield; requires an AI provider path, not locally verifiable here.
- **documenso/documenso #3425** — "[Security]" report in triage; not a public fix target.
- **appwrite/appwrite #14173–#14178** — burst of same-day database bug reports from one external account; team-product surface, consistent with run 155's "appwrite fresh = team items" finding.
- **usememos/memos #6434** is ours (PR #6435); #6431 is a feed-default preference, not a bug. **go-vikunja/vikunja #4115** is editor-toolbar UX/a11y wrapping. **outline/outline #13977** still Linear-tracked (known). **nocodb #14765/#14761** known vague/infra items. chatwoot/payload/directus/twenty fresh heads = features, ours, or empty.

## Watch
NO changes (direct single calls): open-PR count 81; dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045, cake #3671 OPEN; electrum #11012 CLOSED unmerged (known, org block-listed); lodestar #10284 / gitea #39646 / nats.go #2163 OPEN; NiceGUI #6372 APPROVED stands (evnchn); ansible #87642 comments=2 (known pkingstonxyz item); Expensify identical 60/43/33/38 — no selection/hire, no melvin-bot prompt. Held identical: lighthouse #10226 (1 comment, 0 assignees), bullbitcoin/SatoshiPortal #2902 (labels=["bug"] only — HELD stands), formbricks #9526 (3 comments). HackerOne: ledger-only.

$0 requested, $0 received. Next run: sector (1) crypto wallets.
