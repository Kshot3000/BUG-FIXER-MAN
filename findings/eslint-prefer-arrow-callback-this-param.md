# ESLint — `prefer-arrow-callback` reports callbacks that declare a TypeScript `this` parameter

- **Project:** eslint/eslint (sector: general company OSS / dev tools)
- **Issue:** https://github.com/eslint/eslint/issues/21155 (labels: bug, repro:yes, Stale)
- **Date:** 2026-10-02 (run 4)
- **Payment:** none — ESLint is a foundational OSS project with no bounty program; reputation/portfolio value only. No payment requested or expected.

## Bug
`prefer-arrow-callback` reports function expressions that declare a TypeScript `this: T` parameter:

```ts
acceptsCb(function (this: Foo) {})
```

Arrow functions cannot declare a `this` parameter, so the conversion the rule demands is impossible — the declaration *is* the function's `this`-binding contract. The report and the rule's own autofixer disagree: since #19678 the fixer already refuses to touch this exact shape (`node.params[0].name === "this"`), yet the report still fires.

Root cause: the rule discovers `this` usage only via `ThisExpression` scope tracking, so a declared `this` parameter is invisible to the report logic.

## Proof (verified locally, upstream main a438ec39 / v10.12.0)
Repro script (Linter API + `@typescript-eslint/parser`): `fixes/eslint-prefer-arrow-callback-this-param-repro.js`
- Pre-fix: `function (this: Foo) {}` → reported; `function (this: Foo, x) { return x; }` → reported; plain-param control `function (x) { return x; }` → reported **with** autofix (correct).
- Post-fix: both `this`-param callbacks no longer reported; control unchanged.
- Rule test suite: **122/122 passing** (existing `test('foo', function (this: any) {});` case moved invalid → valid, 2 valid cases added, docs TS example moved incorrect → correct).
- Repo self-lint (ESLint on changed files): clean. Prettier: clean. Docs rule-examples check: exit 0.

## Fix
`fixes/eslint-prefer-arrow-callback-this-param.patch` — skip reporting in the `FunctionExpression:exit` handler when the first parameter is named `this`, mirroring the existing fixer bail-out; tests + docs updated. Local branch `fix/prefer-arrow-callback-this-param` (commit d7868f0) in the working clone, ready to push to a fork the moment submission unblocks.

## Submission status — GATED, by the project's own AI policy
ESLint's AI Usage Policy (repo AGENTS.md / docs/src/contribute/ai-policy.md): AI-assisted PRs are **only considered for issues labeled `accepted`**, AI content must be disclosed, and maintainer feedback must be answered by a human. Issue #21155 is **not** labeled `accepted`, so no PR was opened — submitting one anyway would violate the project's CONTRIBUTING policy.

Instead, one disclosed comment was posted with the verified repro, root cause, and test results, asking maintainers to accept the issue:
https://github.com/eslint/eslint/issues/21155#issuecomment-5964511355

**Next step if maintainers label it `accepted`:** fork + push the prepared branch + open the PR with the required bold AI disclosure at the top of the description. **Maintainer follow-up questions on this one are Kyle's to answer** (ESLint policy expects a human respondent). Also note: ESLint PRs require EasyCLA signing — Kyle's alone if the PR proceeds.
