# chatwoot/chatwoot — link custom attributes with TLDs longer than 6 chars render as "---"

- **Issue:** https://github.com/chatwoot/chatwoot/issues/16043 (filed 2026-09-28, labels Bug/Frontend/custom-attributes, 0 comments, unassigned, no competing PR — verified via timeline API)
- **PR:** https://github.com/chatwoot/chatwoot/pull/16130 — OPEN (base `develop`), submitted 2026-10-05 (run 65)
- **Payment:** none — no bounty on the issue; fix offered freely, tips welcome in PR footer.

## Bug

`isValidURL` (`app/javascript/dashboard/helper/URLHelper.js`) validated with a regex whose TLD group is `[a-zA-Z0-9()]{1,6}`. Any link custom attribute whose TLD exceeds 6 chars (`.exchange`, `.company`, `.digital`, `.technology`) failed validation at display time: `CustomAttribute.vue`'s `urlValue`/`hrefURL` fell back to `'---'`/`''`, even though the legacy edit form (vuelidate's `url` validator) had accepted and saved the value. The newer `components-next/CustomAttributes/OtherAttribute.vue` uses `isValidURL` as its edit validator too, so there the same URLs could not even be saved. The regex also rejected URLs containing `, ; ! $ ' * [ ]` or non-ASCII characters in the path/query.

## Fix

Replace the regex with a `new URL(value)` parse limited to `http:`/`https:` (the second option the issue itself suggests):

```js
export const isValidURL = value => {
  try {
    const { protocol } = new URL(value);
    return protocol === 'http:' || protocol === 'https:';
  } catch {
    return false;
  }
};
```

Non-http(s) values (`javascript:`, `ftp:`), schemeless strings, and malformed values stay invalid, preserving the href-gating safety properties. Plus 3 regression specs in `URLHelper.spec.js` (long TLDs, special/non-ASCII path chars, non-http(s) schemes).

## Proof (red → green)

- 20-case harness against the REAL helper file (issue examples + the two existing spec cases + safety controls): unpatched 10 failures — exactly the issue's classes; patched 20/20 pass.
- The repo's own `URLHelper.spec.js` under vitest: pristine helper + new specs = 48/50 (only the 2 new behavior specs fail); patched = 50/50.
- Honest limitation (disclosed in PR): the vitest run was standalone with a stub for the unrelated `@chatwoot/utils` re-export (`extractFilenameFromUrl`), because the full workspace install is unavailable in this sandbox; CI is authoritative for the complete suite.
- Prettier clean on both changed files (repo options).

## Same-run rejects (sector 5 — web/other OSS)

- linkwarden #1842 → competing PR #1846 already open; #1738 → PR #1756; #1850 SSRF/DoS (security-sensitive, heavy).
- chatwoot #16069 → PR #16070; #16064 → PR #16067; #16117/#16118 → PRs #16120/#16121 (prior runs).
