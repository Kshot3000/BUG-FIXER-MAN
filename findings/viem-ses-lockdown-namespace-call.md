# wevm/viem — `viem`/`viem/actions`/`viem/chains` throw under SES `lockdown()` (#5188)

- **Project:** wevm/viem (wallet/client library; Kyle already has merged PR #5176 there)
- **Issue:** https://github.com/wevm/viem/issues/5188 (filed 2026-10-05 by superKalo, 0 comments, no competing PR at submission)
- **PR:** https://github.com/wevm/viem/pull/5189 — OPEN
- **Payment:** none posted; fix offered freely, tips welcome in PR footer.

## Bug
Since 2.54.0, the token and tempo actions declare their contract-call builder as a namespace member (`export namespace approve { export function call() }`), which TypeScript emits as a plain `approve.call = call` assignment. SES `lockdown()` (LavaMoat, MetaMask Snaps, Ambire) tames `Function.prototype`, making `call` read-only — the assignment is an "override mistake" and throws `TypeError: Cannot assign to read only property 'call'` at module evaluation, so `viem`, `viem/actions`, and `viem/chains` cannot be imported at all in hardened realms.

## Proof (red)
Reporter's exact repro against the published `viem@2.57.3` + `ses@1.14.0`:
```
viem/actions THROWS: TypeError: Cannot assign to read only property 'call' of function 'async function approve…'
viem/chains  THROWS: TypeError: Cannot assign to read only property 'call' of function 'async function getConfigCommitment…'
viem         THROWS: (same)
```
A minimal two-file TypeScript experiment confirmed the mechanism and the fix shape before touching the repo (baseline emits `approve.call = call` and throws under lockdown; patched variant imports cleanly, descriptor identical, `.d.ts` byte-identical).

## Fix
At the top of each affected namespace — 116 namespaces across 21 files (5 token actions, 16 tempo action files), located with a TypeScript-AST codemod and re-audited with a second AST pass (no namespace missed, incl. overloads and the nested `simulate` namespace in propAmm) — pre-define `call` as a writable own property:
```ts
Object.defineProperty(approve, 'call', {
  configurable: true,
  enumerable: true,
  value: undefined,
  writable: true,
})
```
The statement emits before the namespace's member assignments, so `approve.call = call` lands on the own writable property. Patch changeset included.

## Verification (green)
- Built ESM + CJS (`pnpm build:esm` / `build:cjs` in an /opt copy — sandbox home fs rejects pnpm's chown for human-id, /var/tmp tmpfs too small): under `lockdown()`, importing `viem`, `viem/actions`, `viem/chains` (ESM) and requiring `viem/actions` (CJS) all succeed.
- `pnpm build:types` output (`.d.ts` tree) **byte-identical** before/after — public API unchanged.
- Property descriptor of patched members = plain-assignment semantics (writable/enumerable/configurable all true).
- Behavioral probe: every exported token/tempo `.call` (114 functions) invoked against the built package — output identical to the published 2.57.3 package.
- Biome clean on all changed files.
- Honest limitation (disclosed in PR): the repo vitest suites fork public RPCs via Anvil and stalled in this sandbox; CI is authoritative for the suite.

## Watch
Maintainer response on #5189; viem maintainers (jxom) merged Kyle's #5176 quickly. If they prefer a build-level rewrite of the emitted JS instead, the source-level pattern here is the fallback — do not argue, adapt if asked.
