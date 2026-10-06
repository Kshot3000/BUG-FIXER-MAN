# trezor/trezor-suite — composePsbt reports malformed PSBT as Failure_UnknownCode

- **Project:** trezor/trezor-suite (`@trezor/connect`, packages/connect-core)
- **Issue:** https://github.com/trezor/trezor-suite/issues/33224 (filed 2026-10-06 by Spittyy, 0 comments, unassigned, no competing PR at submission time)
- **Submission:** PR https://github.com/trezor/trezor-suite/pull/33231 — OPEN / MERGEABLE, commit `08577b9` (GitHub-verified signature), branch `Kshot3000/trezor-suite:fix/33224-psbt-invalid-parameter` against `develop`.

## Bug
`parsePsbt` (`packages/connect-core/src/api/bitcoin/parsePsbt.ts`) called `Psbt.fromHex` unwrapped. The parser throws plain `Error`s for malformed data, so `composePsbt` surfaced them as `Failure_UnknownCode`, while every other validation failure in the same function (`Utxo not found`, non-positive fee, invalid OP_RETURN, unknown output type) is a `TypedError('Method_InvalidParameter', ...)`. In Suite, any `composePsbt` error whose code is not `Method_InvalidParameter` triggers a `sign-tx-error` toast, so a malformed PSBT from a DEX swap provider toasted during fee estimation and twice when signing.

## Proof (red → green, executed)
Standalone tsx harness around the **real** repo sources (`parsePsbt.ts`, `@trezor/utxo-lib`, `@trezor/connect-common`, `@trezor/utils`; only type-only packages and one pure brand-cast stubbed), using the issue's own repro on the "Testnet (Bech32/P2WPKH)" e2e fixture:

| Case | Unpatched | Patched |
|---|---|---|
| valid fixture | OK — fee 150, totalSpent 150, 125 bytes (matches e2e expectations) | identical |
| magic bytes replaced | plain `Error`, no code — "Invalid PSBT magic bytes." | `TrezorError` code `Method_InvalidParameter` |
| truncated to 60 hex chars | plain `Error`, no code — "Cannot read slice out of bounds" | `Method_InvalidParameter` |
| trailing extra byte `aa` | plain `Error`, no code — "PSBT has unexpected data." | `Method_InvalidParameter` |

The new co-located test file `parsePsbt.test.ts` was itself executed in the harness (minimal jest shim): **1 pass / 3 fail unpatched → 4/4 pass patched**. Prettier (repo style options) clean on both files.

Honest limitation (disclosed in the PR): the full monorepo jest/workspace suite was not run locally — no Yarn workspace install in the sandbox; CI is authoritative. Note PR #32177 (maintainer, open) also touches `parsePsbt.ts` and adds a `parsePsbt.test.ts` but explicitly does not cover the `fromHex` wrap (per the issue); hunks do not overlap, a small test-file rebase may be needed if it lands first.

House rules followed: the repo's `AGENTS.md` requires agent-authored PR descriptions to carry an agent prefix — the PR description starts with it, per the project's explicit policy. No issue/PR comments posted, nothing approved or merged.

## Fix
Wrap `Psbt.fromHex` in `parsePsbt` and rethrow as `TypedError('Method_InvalidParameter', 'parsePsbt: Invalid PSBT data: <original parser message>')` — the exact shape the issue's "Possible Fix" section proposes. Success path untouched.

## Payment
No bounty posted on the issue; fix offered freely with tips welcome via the PR footer. $0 requested, $0 received.
