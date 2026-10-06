# Chatwoot — Assignment V2 job enqueued before the creating transaction commits

- **Project:** chatwoot/chatwoot
- **Issue:** https://github.com/chatwoot/chatwoot/issues/16134 (filed 2026-10-05 by varunhooja, 0 comments, unassigned, no competing PR)
- **Fix PR:** https://github.com/chatwoot/chatwoot/pull/16154 — OPEN / MERGEABLE, commit c8fdfc1 GitHub-verified

## Bug

`AutoAssignmentHandler` enqueues `AutoAssignment::AssignmentJob` from `after_save`. `after_save` runs *inside* the transaction that creates (or re-opens) the conversation, and the enqueue is a Redis `SET NX` + an immediate Sidekiq push — neither is transactional. A fast worker starts within ~2 ms (the reporter's logs), scans `inbox.conversations.unassigned.open` through its own connection before the creating transaction commits, sees nothing, logs "Assigned 0 conversations", releases the in-flight marker, and exits. Nothing retries for inboxes without an assignment policy (`PeriodicAssignmentJob` only covers policy inboxes), so the conversation stays unassigned until an unrelated status change in the same inbox triggers a new job. The reporter's self-hosted instance saw this on 11 of 11 unassigned-at-creation conversations in one day.

The old code comment even anticipated the rollback case ("harmless") but not the job running *before commit*.

## Fix

In the V2 branch of `run_auto_assignment`, defer the enqueue until every open transaction has committed, using the Rails 7.2 API built for exactly this (Chatwoot pins Rails 7.2.3.1):

```ruby
inbox_id = inbox.id
ActiveRecord.after_all_transactions_commit do
  AutoAssignment::AssignmentJob.enqueue_for_inbox(inbox_id)
end
```

Legacy V1 paths untouched (inline `before_save` assignment; post-save service call for new conversations), per-inbox coalescing untouched. On rollback nothing is enqueued. No enterprise overlay touches this concern (code search: only `app/models/concerns/auto_assignment_handler.rb` + its inclusion in `conversation.rb`).

## Proof (red → green, real code)

Standalone harness (portable Ruby 3.4.4 + real `activerecord` 7.2.3.1 + sqlite3 gems) that `load`s the **actual concern file** into a minimal model, with the job's scan running through a **separate connection** (a worker can only see committed rows):

| Scenario | Pristine | Patched |
|---|---|---|
| Create inside an outer transaction | enqueue fires inside the tx; worker scan sees **0** unassigned (the reported symptom) | no enqueue inside the tx; after commit the scan sees **1** |
| Plain create (save's own transaction) | enqueue fires inside the tx; scan sees **0** | enqueue after commit; scan sees **1** |
| Rolled-back create | job still enqueued (sees 0) | nothing enqueued |

`ruby -c` clean. Honest limitation, disclosed in the PR: full RSpec not run locally (needs Postgres/Redis + the full bundle) — CI is authoritative. The in-flight coalesce-drop variant the reporter mentioned but did not observe is not addressed; this fix removes the observed pre-commit race.

Harness kept at `~/workspace/goals/bug-fixer-man-global-bug-hunt/hidden_files/work-chatwoot16134/harness.rb`.

## Payment

No bounty posted on the issue; fix offered freely, tips welcome via the PR footer. $0 requested, $0 received.
