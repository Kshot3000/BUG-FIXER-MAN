# go-vikunja/vikunja — v2 bulk task update clears assignees that weren't named in `fields`

- **Project:** go-vikunja/vikunja (Vikunja, self-hosted to-do app; Go API)
- **Issue:** [#4109](https://github.com/go-vikunja/vikunja/issues/4109) — filed 2026-10-06, 0 comments, unassigned, no competing PR
- **PR:** [#4110](https://github.com/go-vikunja/vikunja/pull/4110) — OPEN / MERGEABLE, commit 3ca4ea8 (GitHub-verified signature)
- **Payment:** no bounty posted on the issue; fix offered freely, tips welcome via the PR footer. $0 requested, $0 received.

## Bug

`Task.updateSingleTask` replaced a task's assignees unconditionally via
`ot.updateTaskAssignees(s, t.Assignees, a)`. Single-task updates pass no field
list, so that is the documented behaviour there (the #3222 v1 semantics). But
bulk updates — v2 `PUT /api/v2/tasks/bulk`, also exposed through the built-in
MCP server as `tasks_bulk_update` — clone the request's `values` task and run
it through the same path for every task ID. `values` carries no assignees, so a
bulk update naming only `priority` in `fields` deleted **every assignee from
every task in the request**, returning HTTP 200 — despite the `fields` schema
contract: *"only these fields are written, the rest of each task is left
untouched."* For an MCP assistant following that contract, a routine "set
priority on these 20 tasks" silently unassigns everyone.

## Proof (red → green)

New regression tests in `TestBulkTask_Update` (`pkg/models/bulk_task_test.go`),
using fixture task 30 ("task #30 with assignees", users 1 and 2 assigned):

- *bulk update without assignees field keeps assignees* — **fails unpatched**
  (both `task_assignees` rows for task 30 are gone after a priority-only bulk
  update), passes patched; the priority itself is applied.
- *bulk update with assignees field replaces assignees* — **errors unpatched**
  (`assignees` was rejected with `ErrInvalidTaskColumn`), passes patched
  (assignees replaced with exactly the named set).

Full suite: `go test ./pkg/models/ -count=1` passes; gofmt/vet clean.

## Fix (the issue's suggested option 1)

- Assignees are only replaced when no field list is given (single-task
  updates — unchanged) or when `assignees` is named in `fields`.
- `assignees` is accepted as a pseudo-field in the bulk field list (not a task
  column), so callers can still replace or explicitly clear assignees in bulk.
- Field validation now runs before the assignee update, so an invalid field
  no longer mutates assignees before the request errors.

## Related observation (disclosed in the PR, not fixed there)

The same pattern one step further down also wipes **reminders**: a bulk update
that doesn't name reminders deletes them (`updateReminders` runs
unconditionally with the cloned values task, whose `Reminders` is empty —
fixture task 27 loses both reminders after a priority-only bulk update,
verified with the same test setup). Left out of the PR because reminders
interact with the repeating-task rescheduling in `updateDone`; flagged in the
PR body for a maintainer-directed follow-up.

## Same-run sector-5 rejects

- payload #18521 (join "Add new" ignores create permission) — reporter's fix
  already landed as open PR #18526 within hours.
- chatwoot #16139 — Help Portal i18n metadata is a feature request, not a bug;
  #16133/#16122 already cross-referenced by PR #16123.
- navidrome #6276 (smart playlist import) — no repro steps, external file
  share, config-dependent; #6275 (listenbrainz agent) — reporter's own log
  shows a 0.49.3 binary against a claimed v0.64.2, config/version issue.
- jellyfin fresh queue — no dotnet toolchain in this sandbox (standing).
- actual #9104 (API transaction race) — needs-triage, non-deterministic race,
  not locally verifiable to the bar.
