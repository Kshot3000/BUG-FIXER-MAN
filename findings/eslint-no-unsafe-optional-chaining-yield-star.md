# eslint/eslint — `no-unsafe-optional-chaining` doesn't report optional chains passed to `yield*`

- **Issue:** https://github.com/eslint/eslint/issues/21385 (filed 2026-10-04, labels bug/rule/**accepted**/repro:yes, 1 comment — maintainer mdjermanovic: "Marking as accepted, PR is welcome"; no competing PR, no claim)
- **PR:** https://github.com/eslint/eslint/pull/21391 (OPEN, 2026-10-05, base main) — `fix: report unsafe optional chains in yield* expressions`, Fixes #21385
- **Payment:** none posted on the issue; fix offered freely, tips welcome via the PR footer. Not a bounty request.
- **Sector:** (4) general company OSS / dev tools — run 74

## Bug

The rule had visitors for every context where a short-circuited `undefined` throws (call/member/new callee, destructuring, `for...of` right side, spread, `in`/`instanceof`, class extends, `with`) but no `YieldExpression` visitor. `yield* obj?.items` delegates iteration to the chain's value; when the chain short-circuits, `yield* undefined` throws `TypeError: undefined is not iterable` — yet the rule reported nothing.

## Proof (red → green, reproduced locally)

Reporter's exact repro through the Linter on upstream main `e5aea41`:

```
delegate yield* chain (ISSUE - should report): 0 problem(s) []        ← unpatched
delegate yield* chain (ISSUE - should report): 1 problem(s) ["unsafeOptionalChain"]  ← patched
runtime: yield* with obj?.items===undefined throws: TypeError: undefined is not iterable
```

Controls identical both ways: plain `yield obj?.items` (safe, stays unreported), `yield* obj.items`, `yield* obj?.items ?? []`, `yield* obj?.items || []` all 0 problems; nested chain `yield* obj?.items?.sub` newly reported.

## Fix (+19 lines across 3 files, commit fa61c69 on fork branch `fix/21385-yield-star-unsafe-optional-chaining`)

- `lib/rules/no-unsafe-optional-chaining.js`: `YieldExpression` visitor — only when `node.delegate`, `checkUnsafeUsage(node.argument)` (reuses the existing short-circuit walker, so `??`/`||` fallbacks, conditionals, sequences, and `await` inside async generators behave like every other context).
- `tests/lib/rules/no-unsafe-optional-chaining.js`: 5 valid + 4 invalid cases in the file's own style. **Red→green verified:** the new invalid cases fail on the pristine rule (`Should have 1 error but had 0`); the full test file passes patched (run via RuleTester).
- `docs/src/rules/no-unsafe-optional-chaining.md`: `yield*` added to the incorrect examples.

Prettier check clean on all three files (repo `.prettierrc.json`, prettier 3.x).

## Venue notes / honest limitations

- ESLint's AI policy (repo `AGENTS.md`): AI PRs are considered only for `accepted` issues — #21385 is labeled `accepted`. The PR carries the required disclosure at the top: **"This pull request was created with AI (Muse Spark)."**
- The same policy says maintainer feedback is expected to be answered by a human — **if reviewers comment, Kyle should reply himself** (watch item).
- Full `npm test` NOT run locally: the repo's full dev-dependency install did not complete in this sandbox (killed after >5 min); the rule's complete test file was run against both pristine and patched rule code with a standalone ESLint 10 install, and the PR body discloses this. CI (incl. the 99% coverage gate — both new branches are test-covered) is authoritative.

## Same-run sector-4 rejects

- eslint #21387 (no-var + one-var combined fix produces invalid `let`): also `accepted`, but already claimed by mitre88 with PR #21389 open (and #21388 closed) — not duplicated.
- yq #2884/#2851/#2853: standing — competing fix PRs already open (runs ~32/36).
- fd #2122/#2033/#2053: stale/design-level or message-wording only; ripgrep queue old (2024–2026-01, maintainer-paced); Hugo #15161/#15126 niche rendering edge cases with maintainer engagement; golangci-lint #6822/#6746 are upstream staticcheck defects; uv/ruff fresh issues are Rust (no Rust toolchain in this sandbox) or resolver-design questions.
