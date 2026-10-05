# linkwarden/linkwarden — extension context menu saves the active tab instead of the clicked link/media

- Issue: https://github.com/linkwarden/linkwarden/issues/1851 (filed 2026-09-28, label bug, 0 comments, unassigned, no competing PR)
- PR: https://github.com/linkwarden/linkwarden/pull/1856 (base `dev`, per repo branch policy) — OPEN
- Venue: same repo as PR #1855 (run 50); no bounty, tips welcome.

## Bug
The extension registers "Add link to Linkwarden" context menus for page/selection/link/editable/image/video/audio contexts, but `genericOnClick` (`apps/extension/src/pages/Background/index.ts`) ignored `info.linkUrl` / `info.srcUrl` / `info.selectionText` and unconditionally saved `tab.url`/`tab.title`. Right-clicking any hyperlink or image bookmarked the page being read, not the clicked target. The API path also hardcoded collection `"Unorganized"`, ignoring `config.defaultCollection` (which "Save all tabs" respects).

## Fix
Default branch of `genericOnClick`: target = `info.linkUrl || info.srcUrl || tab.url`; title = `selectionText` if present, else tab title when the target is the tab, else the target URL; collection = `config.defaultCollection` (schema default is "Unorganized", so default behavior unchanged). Applied to both the API (`postLinkFetch`) and bookmark-sync (`bookmarks.create`) paths. 16 insertions / 7 deletions, one function.

## Verification (red → green, real code)
Harness bundles the real `index.ts` via Bun.build with the four imported modules stubbed (config/postLinkFetch/bookmarks record calls; `hasAPI` configurable) and drives the captured `contextMenus.onClicked` listener:
- Pristine: link click, image click, page click, selection, and sync path ALL save the tab URL/title with "Unorganized" — the reported bug, reproduced exactly.
- Patched: link → linkUrl, image → srcUrl, page → tab URL/title (control, unchanged), selection → tab URL with selection text as name, sync path → bookmark created for the clicked link; collection = configured default ("My Default" in harness) in every API-path scenario.
- Prettier: pristine file clean; patched file clean after `prettier --write` (one line-wrap), harness re-run green after formatting.
- Honest limitation (disclosed in PR): full extension workspace build not run locally (no pnpm workspace install in sandbox); change is confined to one function in one file. No test suite exists for the background page.

## Payment
None requested — no bounty on #1851; fix offered freely, tips welcome via PR footer. $0 received.
