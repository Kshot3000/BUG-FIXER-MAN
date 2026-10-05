# zauberzeug/nicegui — `ui.timer` cancels `@await_on_shutdown` callbacks on shutdown

- **Project:** NiceGUI (zauberzeug/nicegui)
- **Issue:** https://github.com/zauberzeug/nicegui/issues/6331 (filed 2026-09-10, 0 comments, unassigned, no competing PR for the Timer path)
- **PR:** https://github.com/zauberzeug/nicegui/pull/6372 — OPEN / MERGEABLE (2026-10-04, run 25)
- **Payment:** none posted on the issue; fix offered freely, tips welcome. **$0 requested, $0 received.**
- **Branch:** `Kshot3000/nicegui@fix/6331-timer-await-on-shutdown` (096b0ec)

## Bug

`@background_tasks.await_on_shutdown` tags a function so tasks created from it are awaited, not cancelled, during shutdown: `background_tasks.create()` recognises the `_AwaitOnShutdown` marker on the awaitable it is handed and registers the task in `_await_tasks_on_shutdown`, which `teardown()` skips and waits for.

Issue #6331 listed three dispatch paths that hid the marker behind a fresh wrapper coroutine. Re-verified empirically on current `main` (19cc869) with the repo's `User` test fixture — protected callback in flight, then `background_tasks.teardown()`:

- `app.on_connect(save)` shorthand (`Client.safe_invoke`) — **now completes**. Since #6363 these paths hand the original awaitable to `create(..., context=...)`, and `create()` checks the original.
- `ui.button(on_click=save)` shorthand (`events.handle_event`) — **now completes**, same reason (`create_or_defer(..., context=...)`).
- `ui.timer(0.05, save, once=True)` — **still cancelled** (`['started', 'cancelled']`). The Timer path never reaches `background_tasks` with the callback at all: the callback runs as a child `asyncio` task in `Timer._invoke_callback`, awaited by the timer's loop task, so teardown's cancellation of the timer task propagates straight into the protected invocation.

## Fix

`nicegui/timer.py`, `Timer._invoke_callback`: when the callback's result is an `_AwaitOnShutdown`, hand it to `background_tasks.create(...)` (registered + marked, so `teardown()` awaits it) and await it via `asyncio.shield(...)`, so cancelling the timer or its invocation task does not propagate into the protected work. `handle_exceptions=False` because exceptions are handled by `_invoke_callback`'s existing in-context handler, exactly like unprotected callbacks. Repeating timers keep their pacing — the invocation is still awaited before the next tick.

## Proof (red → green, current `main`)

Harness: `tests/test_background_tasks.py`-style `User` fixture tests (no browser needed):

- New regression test `test_timer_invocation_is_awaited_on_shutdown`: **fails unpatched** (`events == ['cancelled']`), **passes patched** (`events == ['done']`).
- Scratch verification (not committed): all four strategies (`direct`, `connect`, `click`, `timer`) complete through teardown post-fix; a **repeating** timer's in-flight protected invocation also completes; a plain unprotected timer callback is **still cancelled** by teardown (no behavior change); a raising protected timer callback is reported to `ui.on_exception` **exactly once**, identical to the unprotected baseline.
- Suites: `tests/test_background_tasks.py` 8/8 user-fixture tests pass; `tests/test_timer.py` user-fixture tests pass; `ruff check` clean. Selenium `Screen` tests cannot run in this sandbox (no Chrome — they fail at fixture setup on the clean tree too); CI is authoritative for those. At submission, GitHub reported no checks yet on the branch (first-time-contributor gating is the maintainer's).

## Notes

- NiceGUI is an AI-welcoming venue (repo `AGENTS.md` pair-programming guidelines; maintainer PRs are regularly AI-coauthored). The PR follows the repo template with Motivation / Implementation / Progress, and discloses AI assistance.
- Related, disclosed in the PR but left out of scope: `Client.handle_exception` still wraps results in `helpers.await_with_context(...)` before `create()`, hiding the marker the same way for exception handlers.
- Sector-5 rejects this run (all verified via API before use): Textual #6726 (reporter's ready branch + a fresh claim today), #6723 (maintainer-acknowledged, likely-fixed), #6712 / #6708 / #6715 (already fixed or PR'd), Sanic #3200 (reporter's PR #3201 opened today), Sanic #3196 (PR #3198), NiceGUI #6343 (PR #6369) and #6348 (reporter's PR #6349, assigned to reporter), Black #5468 (PR #5469), Gradio/Streamlit/Discord.py queues (maintainer-worked, reporter-PR'd, or migration/meta issues).
