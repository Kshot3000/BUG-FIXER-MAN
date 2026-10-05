# js-stellar-sdk — ContractSpec mishandles struct fields and function args named `__proto__`

- **Project:** stellar/js-stellar-sdk — the official Stellar JS SDK (Soroban contract spec handling) — https://github.com/stellar/js-stellar-sdk
- **Issue:** #1734 — "ContractSpec mishandles struct fields and function args named `__proto__`" https://github.com/stellar/js-stellar-sdk/issues/1734 (filed 2026-09-14 by Ryang-21 from a Copilot review on merged #1733; label `bug`, unassigned, 0 comments, no competing PR)
- **Submission route — NO PR opened, deliberately:** the repo's CONTRIBUTING.md accepts PRs **only on maintainer invitation** ("Unsolicited pull requests will be closed without explanation and may be reported as spam") and #1734 carries no `help wanted` label and no invitation. Following the PyBNF/GE precedent: a verified evidence report was posted on the issue and a tested fix branch was offered for a maintainer to invite/cherry-pick.
- **Report:** https://github.com/stellar/js-stellar-sdk/issues/1734#issuecomment-5986124677 (2026-10-04)
- **Ready branch:** `Kshot3000/js-stellar-sdk@fix/1734-proto-struct-fields` — commits 5325f77 (fix + tests + CHANGELOG) + generated-docs refresh commit. Push passed the repo's husky pre-push docs check.
- **Bounty:** none — OSS fix offered freely, tips welcome.
- **Status:** WATCH — maintainer reply on #1734 (may invite the PR; open it from the ready branch immediately if so).

## Bug

`Spec.structToNative` decoded structs into a plain `{}` and assigned each field by its raw spec name. A field literally named `__proto__` is a legal Soroban symbol, so an on-chain contract spec can carry one:

- **Primitive value** (e.g. u32): the assignment is a silent no-op — the field is dropped from the decoded object entirely.
- **Object value** (a nested struct): the assignment invokes the `__proto__` setter and replaces the decoded object's prototype; undeclared names then resolve through the attacker-supplied prototype (impact bounded to that one decoded object — `Object.prototype` itself is not polluted).
- **Round trip broken:** re-encoding the decoded struct reads the missing field back as `Object.prototype` and throws `TypeError: Received object [object Object] did not match the provided type …`.

The event decoder in the same package already guards against exactly this (`src/contract/event_spec.ts`, #1565) by building its output with `Object.create(null)`; the struct path was never made consistent. The same plain-object pattern in `jsonSchema()`'s `argsAndRequired` properties map (and the definitions accumulator) drops a `__proto__` field/argument/type name from the generated schema identically.

Encode side, measured: `readObj`/`nativeToStruct` already work when the caller supplies the value as an **own property** (`Object.defineProperty` / `JSON.parse`); an object literal `{ __proto__: 1 }` creates no own property for any code to find, so that direction is a documentation matter, not a code fix.

## Proof (main ddae19b / v17.2.1, red first)

Vitest repro with a spec built in code — structs `Evil { __proto__: u32, other: u32 }`, `EvilObj { __proto__: Inner, other: u32 }`, functions `take(__proto__: u32)`, `take_evil(x: Evil)`. Unpatched: **4 of 6 checks fail** — primitive decode (no own property, value lost), object decode (no own property; `out.a` resolves to 99 through the installed prototype), round trip (TypeError above), jsonSchema (`properties` has no own `__proto__`, `JSON.stringify` omits it while `required` still lists it). The 2 encode-as-own-property checks pass unpatched, confirming the encode direction already works that way.

## Fix

- `structToNative`: build the result with `Object.create(null)` (comment mirrors the event decoder's rationale).
- `argsAndRequired`: properties map on `Object.create(null)`; `jsonSchema()`: definitions accumulator on `Object.create(null)` (the spread into the result copies own properties safely).
- `funcArgsToScVals` TSDoc: documents that an argument/field named `__proto__` must be passed as an own property, and that decoded values already carry it as one.
- CHANGELOG entry under `## Unreleased`; generated reference docs regenerated (the repo's pre-push hook requires it).

## Verification

- Red→green: all 6 new regression tests in `test/unit/spec/contract_spec.test.ts` pass post-fix; the 4 decode/schema/round-trip tests fail on the unpatched tree.
- Spec suites: **123 passed / 1 skipped**. Full unit suite: **6904 passed**; the only failures are timeouts in `test/unit/server/soroban/request_airdrop.test.ts`, which fail identically on the unmodified tree in this sandbox (network-dependent friendbot tests; no direct egress here) — pre-existing, unrelated.
- `tsc -p tsconfig.json` clean; ESLint clean on changed files; Prettier applied to the test file (CHANGELOG.md fails Prettier at HEAD too — left in the file's existing style).
- Same-run sector-2 rejects: bitcoinjs-lib #2293/#2249 (fix PRs #2338/#2326 already open — repo is heavily farmed), cosmjs #1982 (fix PR #1983 already open by the reporter), near-api-js #1639 (fix PRs #2000/#1999 already open), stellar #1750/#1763 (fix PRs #1772/#1774 already open), noble/scure queues (feature requests only), avalanchejs #979 (feature question, not a bug).
