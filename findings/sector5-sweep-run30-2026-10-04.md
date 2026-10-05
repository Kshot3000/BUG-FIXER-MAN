# Sector 5 (web / other OSS) sweep — run 30, 2026-10-04

**Result: NO submission.** Status watch: no changes (see below).

## Status watch (run 30)
- All 12 open PRs still OPEN, comment counts identical to run 29: dentalpin #599 (1c), ERCs #2045 (1c), cake #3671 (0c), electrum #11012 (0c), electrum #11013 (0c), ThreeDRadio #93 (0c), scure-btc-signer #144 (0c), GE #12289 (0c), gofactory #67 (1c), BlueWallet #8985 (0c), safe #1440 (6c — CLAAssistant check still stale FAILURE despite Kyle's signature), nicegui #6372 (0c, CLA+Test SUCCESS). `gh search prs --author Kshot3000 --state open` = 12, matches.
- Expensify ×4 unchanged: #102072 53 comments, #102226 35, #101684 33, #102044 28 — no C+ response / assignment / hire on any.
- ESLint #21155 still OPEN, labels `bug`/`repro:yes` only — no `accepted` label. stellar #1734 (6c, ours) / PyBNF #931 (1c, ours): no maintainer replies.
- HackerOne: no logged-in check this run; ledger-only.

## Hunt — sector 5, ~50 web/other-OSS repos swept via API
Fresh bug queues checked (NiceGUI, Textual, Sanic, Telegram-bot, discord.py, Flask, Werkzeug, FastAPI, httpx, Starlette, aiohttp, Celery, redis-py, Black, Requests, Gradio, Streamlit, Supabase, Directus, Mealie, Outline, Flet, Dash, Hono, Fastify, Express, Socket.io, NestJS, Nuxt, Svelte, Preact, Vite, Vue, Angular, Expo, Ionic, tRPC, Prisma, Drizzle, TypeORM, Sequelize, MikroORM, Apollo, graphql-js, Joomla, Payload, Medusa, Saleor, Vendure, Keystone, Adonis, Feathers, Loopback, Meteor, Redwood, Appsmith, Budibase, Windmill, Formbricks, PostHog, NocoDB, Cal.com, Documenso, Uvicorn, Quart, Tornado, Gunicorn, Strawberry, …).

Every verifiable candidate was already taken, usually within hours:
- **directus/directus #28318** (`getKeysByQuery` drops falsy PKs `0`/`''`, filed 2026-10-01) — maintainer Nitwel's fix PR **#28319** already open.
- **typeorm/typeorm #12923** (`@VersionColumn` not incremented on `upsert()`, Postgres, c=0) — reporter's fix PR **#12924** already open.
- **payloadcms/payload** — the fresh detailed reports are PR'd almost immediately: #18480→PR #18483, #18476→PR #18479, #18465→PR #18472, #18451→PR #18458, #18432→PR #18449.
- **mealie #8589** — already PR'd (noted in earlier runs).

## Rejected on scope/verifiability
- **payloadcms/payload #18462** (SQL adapters strand block rows in old numbered tables when placements are renumbered; duplicates on next save) — the only un-PR'd fresh Payload bug, but the fix is an architectural data-migration decision (moving rows across renumbered variant tables during schema push/migrate, incl. versions + child tables) for the core team, not a one-run verifiable patch. Not attempted.
- **flet-dev/flet #6895** (`Dropdown.expanded_insets` never read by the Flutter client) — fix is Dart/Flutter client code; no Flutter/Dart toolchain in this sandbox, cannot verify. Not attempted.
- Supabase fresh issues are hosted-service incidents (project restore/WAL/free-tier), not code bugs in the repo. Gradio #13939 is assigned. Budibase/Appsmith/PostHog fresh items are assigned, platform-specific, or need their full stacks.

## Payments
None requested, none received. $0 received all-time; 4 × $250 Expensify proposals still pending selection.

Next run: sector 1 (crypto wallets).
