# Reown AppKit — SIWX sign view queues a duplicate wallet signature request per click

- **Project:** reown-com/appkit (@reown/appkit-scaffold-ui 1.8.24)
- **Issue:** #5811 — "[bug] SIWX sign prompt: 'Sign' button is not disabled while signing - repeated clicks queue multiple wallet signature requests" (filed 2026-10-02, 0 comments, unassigned, no competing PR)
  https://github.com/reown-com/appkit/issues/5811
- **PR:** #5813 OPEN / MERGEABLE — https://github.com/reown-com/appkit/pull/5813
- **Payment:** none posted on the issue; fix offered freely, tips welcome in the PR footer. $0 requested, $0 received.

## Bug
In `packages/scaffold-ui/src/views/w3m-siwx-sign-message-view/index.ts`, the Sign button bound only `?loading=${this.isSigning}`. `wui-button` derives the inner button's `disabled` solely from its own `disabled` prop — `loading` only renders a spinner. So the button stayed clickable while a signature request was in flight, and `onSign()` had no re-entry guard: every click called `SIWXUtil.requestSignMessage()` again, creating a fresh-nonce SIWE message and another wallet signature request per click (each passes server-side verification → duplicate sessions / concurrent verify side effects). `onCancel()` had the identical defect. Same class as legacy #2841, which the SIWX view never inherited the guard from. Confirmed verbatim on main (fork HEAD 7897b8d).

## Fix (fork branch `fix/siwx-sign-message-reentry`, commit 3544f72)
View-level, exactly the issue's suggested option A, following the codebase's own pattern (`w3m-swap-preview-view`, `w3m-connecting-farcaster-view` bind `?disabled=${loading}`):
- Sign button gains `?disabled=${this.isSigning}`; Cancel gains `?disabled=${this.isCancelling}`
- Re-entry guards at the top of `onSign()` / `onCancel()` (defense in depth — handlers are safe even for programmatic clicks)
- New regression test `test/views/w3m-siwx-sign-message-view.test.ts` + a changeset (repo PR requirements)

## Proof (red → green)
- Environment note: pnpm install fails on this sandbox's home filesystem (chown EPERM importing `human-id`'s tarball CLI file — same sandbox class as the classic-level node-gyp EPERM in earlier runs), so install/build/test ran in an identical clone under /var/tmp where chown works; sources are byte-identical.
- New tests: **2 failed unpatched** (3 clicks → 3 `requestSignMessage()` calls; button never disabled), **2 passed patched** (3 clicks → 1 call; disabled in flight; works again after settle; same for Cancel).
- Full scaffold-ui views suite: **41 files / 394 tests pass** with the fix.
- `@reown/appkit-scaffold-ui` `tsc --build` passes; Prettier reports no changes on the touched files; ESLint clean on the changed source file.

## Watch
Maintainer review + CI on #5813 (DangerJS checks import boundaries / changeset presence — changeset included).
