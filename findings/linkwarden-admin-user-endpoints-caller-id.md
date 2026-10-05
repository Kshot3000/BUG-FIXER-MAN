# linkwarden/linkwarden — admin user endpoints act on the caller instead of the requested user

- **Issue:** https://github.com/linkwarden/linkwarden/issues/1848 (filed 2026-09-28, label bug batch, 0 comments, unassigned, no competing PR — open/closed PR search for "1848" empty at submission)
- **PR:** https://github.com/linkwarden/linkwarden/pull/1857 — OPEN, MERGEABLE, base `dev` (repo branch policy, per #1855/#1856)
- **Run:** 60 (2026-10-05, sector 5 — web/other OSS)

## Bug
In `apps/web/pages/api/v1/users/[id]/index.ts` (verified verbatim on upstream/dev cd0e918f), the GET and PUT handlers permission-check the requested user (`queryId`) but pass the caller's token ID (`userId`) to the controllers:

- Admin `GET /api/v1/users/2` → `getUserById(1)` — returns the admin's own profile.
- Admin `PUT /api/v1/users/2` → `updateUserById(1, body)` — silently overwrites the admin's own account (self-lockout risk), target untouched.

The DELETE handler in the same file already passes `queryId` correctly, and both controllers take the target user's ID as their first argument.

## Fix (2 lines)
Pass `queryId` to `getUserById` and `updateUserById`. Permission checks unchanged. Branch: `Kshot3000/linkwarden@fix/1848-admin-user-target-id` (7e007cb7).

## Proof (red → green)
Harness (Bun.build) bundling the REAL handler with stubbed imports (verifyToken / prisma / the three user controllers record calls), driven with fake requests:

| Scenario | Before | After |
|---|---|---|
| Admin GET user 2 | `getUserById(1)` | `getUserById(2)` |
| Admin PUT user 2 | `updateUserById(1, …)` | `updateUserById(2, …)` |
| Self GET user 1 | `getUserById(1)` | unchanged |
| Agent GET user 1 | 401, no controller call | unchanged |
| Agent PUT self (2) | `updateUserById(2, …)` | unchanged |
| Admin DELETE user 2 | `deleteUserById(1, {}, true, 2, false)` | unchanged |

Prettier check passes on the changed file. Honest limitation (disclosed in PR): full workspace build not run locally — workspace install unavailable in the sandbox; change is two lines in one file.

## Same-run rejects
- mealie-recipes/mealie #8544 (invalid DB_ENGINE silently falls back to SQLite) — already has PR #8605.
- chatwoot/chatwoot #16106 (Shopify Brazil phone normalization) — vague locus ("does not appear"), sprawling matching path, not cleanly verifiable here.
- chatwoot/chatwoot #16107 (inbox cache key not invalidated on role change) — full-stack IndexedDB/Redis repro not feasible in sandbox; left as a spare.
- linkwarden #1850 (remote-browser SSRF/DoS) — security-sensitive, heavy worker surface; #1842 (import description trimmed at 254 chars) — left as spares.
- Global `label:bug` stream — AI-farm noise, as in prior runs.

## Payment
No bounty posted on #1848; fix offered freely with tips welcome via the PR footer. $0 requested, $0 received.
