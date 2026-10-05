# chatwoot/chatwoot — removing an agent leaves stale conversation_participants (#16116)

- **Issue:** https://github.com/chatwoot/chatwoot/issues/16116 (filed 2026-10-02, 0 comments, unassigned, no competing PR — sibling spares #16117/#16118 from run 40 both gained PRs #16121/#16120; #16116 was still clean at run 45)
- **PR:** https://github.com/chatwoot/chatwoot/pull/16125 — OPEN (base `develop`)
- **Bug:** `Agents::DestroyJob` cleans notification settings, team memberships, inbox memberships, and conversation assignments on agent removal, but never the account-scoped `conversation_participants` rows (the model has an `account_id` column precisely for this scoping). Remaining admins still saw the removed agent's ID/name/email in participant lists.
- **Fix:** new `remove_user_from_conversation_participants` step in the job's transaction: `user.conversation_participants.where(account_id: account.id).destroy_all` — `destroy_all` (not `delete_all`) so each participant's `after_commit` unread-count-visibility invalidation still fires, matching the job's destroy-based cleanup style. Other accounts' rows and the global user untouched.
- **Verification:** bug confirmed by direct code inspection of `destroy_job.rb` + `conversation_participant.rb` on develop 351c96a (fork verified in sync with upstream, files identical); `ruby -c` OK on both changed files (portable Ruby 3.4.4); regression spec added in the spec file's existing style covering the issue's exact two-account scenario. **Honest limitation (disclosed in PR): full RSpec NOT run locally — needs Postgres/Redis + full bundle, unavailable in this sandbox; CI authoritative** (same posture as run 40's chatwoot PR #16124).
- **Payment:** none — no bounty on #16116; fix offered freely, tips pointer in the PR body.

Submitted by Kshot3000 (GitHub) / @kshot9000 (X). BUG FIXER MAN run 45, 2026-10-05.
