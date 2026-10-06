# go-gitea/gitea — Telegram webhook: line breaks lost in rich messages

- **Issue:** https://github.com/go-gitea/gitea/issues/39649 (filed 2026-10-06 by xsergos, 0 comments, unassigned, no competing PR)
- **PR:** https://github.com/go-gitea/gitea/pull/39650 — OPEN / MERGEABLE, commit `1cb955f` (GitHub-verified)
- **Sector:** (5) web / other OSS — run 165

## Bug
Since the Telegram webhook moved to Bot API 10.1 Rich Messages (upstream PR #38298, `sendRichMessage` with `rich_message.html`), line breaks in webhook messages are lost: Telegram treats a bare `\n` in rich-message HTML as insignificant whitespace, like HTML. Every convertor builds multi-line text with `\n` (PR/issue bodies, comments, push commit lists) and `createTelegramPayloadHTML` passed it through unchanged, so messages render as a single paragraph. Regression vs. the old `sendMessage` + `parse_mode=HTML`.

## Fix
In `createTelegramPayloadHTML` (the single funnel for all Telegram payloads): sanitize as before, then convert `\r\n` / `\r` / `\n` to `<br>`. `<br>` is in Gitea's sanitizer allowlist, and converting after sanitizing means only our own breaks are inserted — all user text is already escaped.

## Proof (red → green)
- New regression test `Line breaks are kept in rich messages` + updated Push/Issue/IssueComment/PullRequest/PullRequestComment/Review expectations: FAIL on pristine main (payload contains literal `\n`, e.g. expected `first line<br>second line<br>third line`, actual `first line\nsecond line\nthird line`) → PASS patched.
- Full `services/webhook` package test suite PASS; gofmt + `go vet` clean.
- Test-env note: the package TestMain refuses to run as root; the compiled test binary was run with the documented SNAP bypass (`SNAP=1 SNAP_NAME=gitea`), same code path, no test changes for it.

## Rejected this run (sector-5 sweep, all direct-verified singly)
- **go-vikunja/vikunja #4117** (Postgres password with `@` breaks connection, filed minutes before the sweep): real regression (2.7 switched pq→pgx, whose URI parser ends userinfo at the first `@`, and the DSN builder used `url.PathEscape`, which leaves `@` unescaped) — but **already fixed on main** by commit `d568a258` (2026-10-03, percent-encode credentials via `url.UserPassword`, with a pgconn round-trip test); v2.7.0 predates it. A PR would duplicate the merged fix.
- **chatwoot/chatwoot #16158** (SendReplyJob parallel delivery reorders messages): reporter-diagnosed, but the fix is an architectural per-conversation ordering/locking decision and is not locally verifiable (needs live channel providers).
- **payloadcms/payload #18565** (backport the multi-worker jobs fix #17441 to 3.x): the upstream fix is a breaking `feat!` on 4.0; what portion is backportable is a maintainer call, and the change is far beyond a one-run verified patch.
- listmonk #3259 vague support question (no repro); appwrite fresh burst = one-account team-surface reports (known pattern); audiobookshelf #5638 single-reporter UI symptom on an old version, no logs; supabase #51366 hosted-service 5xx report; outline #13977 Linear-tracked (known); memos #6434 / vikunja #4110 / #4107 = ours; cal #30302 reporter-offered (known); twenty/nocodb/uptime-kuma/Ghost/plausible/formbricks heads = features, vague, or ours.

## Payment
No bounty posted on the issue; fix offered freely with tips welcome via the PR footer. $0 requested, $0 received.
