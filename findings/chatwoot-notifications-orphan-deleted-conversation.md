# chatwoot/chatwoot — notifications index 500s forever on a notification whose conversation was deleted (#16149)

- **Issue:** https://github.com/chatwoot/chatwoot/issues/16149 (filed 2026-10-06, 0 comments, unassigned, no competing PR — verified via timeline API; cross-reference to PR #16152 is ours)
- **PR:** https://github.com/chatwoot/chatwoot/pull/16152 — OPEN / MERGEABLE (base `develop`; mergeable_state "blocked" = checks/review pending, standard for external forks)
- **Payment:** none — no bounty posted on the issue; fix offered freely, tips pointer in the PR footer. Not a bounty request.

## Bug

Notifications are built from asynchronously dispatched events (`EventDispatcherJob` → `NotificationListener` → `NotificationBuilder`), and the builder held a conversation object without ever checking that the conversation still exists in the database. When the conversation is deleted before the queued work runs (the issue's case: a widget contact merge removes it), the builder still writes a notification whose polymorphic `primary_actor` points at a conversation row that is gone — there is no foreign key on a polymorphic association to stop it.

That orphan row is permanent poison for the agent's feed: `notifications/index.json.jbuilder` calls `notification.primary_actor.push_event_data` (and `push_message_title`/`push_message_body` dereference `primary_actor.inbox` / `conversation.display_id`) with no nil guard, so every `GET /api/v1/accounts/:id/notifications` request for that user returns 500, forever, because the row stays.

## Fix (commit 2f9a1e5, GitHub-verified)

- `app/builders/notification_builder.rb`: `build_notification` returns early when the conversation behind the notification no longer exists (`primary_actor_missing?` — resolves the conversation the same way the existing access check does, then `Conversation.exists?`). Runs before the blocked-contact and policy checks, which dereference the stale object.
- `app/finders/notification_finder.rb`: the feed query now excludes rows whose `primary_actor_type = 'Conversation'` and whose conversation no longer exists (`NOT EXISTS` subquery against `conversations`). This un-poisons feeds that already hold an orphan row and keeps `count`/`unread_count` consistent with the feed (both derive from the same relation).
- Regression specs: builder creates nothing after `primary_actor.destroy!`; finder excludes an orphan row (`primary_actor_id` pointed at a nonexistent conversation) from the feed and both counts (expected 3 → 2 in the existing fixture setup).

## Verification

- Code-level trace of the full chain on upstream `develop` f1c9e48: dispatcher/job → listener → builder (no existence check), polymorphic association (no FK), index jbuilder + model title/body methods (unguarded dereferences).
- `ruby -c` (portable Ruby 3.4.4) OK on all 4 changed files; all lines within the repo's 150-char RuboCop limit.
- The finder's exact SQL fragment was executed against a standalone SQLite harness with 2 live-conversation rows + 2 orphan rows (missing id, id 0): kept exactly the 2 live rows, excluded both orphans.
- **Honest limitation (disclosed in the PR):** the full RSpec suite was NOT run locally — it needs Postgres/Redis + the full bundle, unavailable in this sandbox; CI is authoritative (same posture as prior Chatwoot PRs #16124/#16125/#16130).

## Same-run rejects (sector 5 — web/other OSS)

- chatwoot #16145 → reporter's PR #16146 already open; listmonk #3258 = feature request (archive sort order); nocodb #14765 too vague (no repro detail beyond "URL fields not exported"); outline #13977 Linear-tracked (OLN-2203) editor round-trip, prior attempt #11818 closed stale; gitea #39634 reporter-owned ("I have a PR ready" + cross-referenced); gitea #39637/#39632/#39636 already commented/engaged; payload #18531 = our own PR #18534; vikunja #4109 = our own PR #4110; memos #6434 = our own PR #6435.

Submitted by Kshot3000 (GitHub) / @kshot9000 (X). BUG FIXER MAN run 140, 2026-10-06.
