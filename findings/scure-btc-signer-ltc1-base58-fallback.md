# scure-btc-signer — Litecoin P2PKH addresses starting with `LTC1`/`LTc1` cannot be decoded

- **Project:** paulmillr/scure-btc-signer (@scure/btc-signer) — https://github.com/paulmillr/scure-btc-signer
- **Issue:** #133 — "P2PKH Litecoin addresses starting with `LTc1` or `LTC1` cannot be decoded" https://github.com/paulmillr/scure-btc-signer/issues/133 (open, unassigned, filed 2025-10-10; follow-up to the partial GH-112 fix)
- **Submission:** **PR #144 OPEN (2026-10-04): https://github.com/paulmillr/scure-btc-signer/pull/144** (fork branch `Kshot3000/scure-btc-signer@fix/address-decode-base58-fallback`, commit 029595c)
- **Bounty:** none — OSS fix offered freely, tips welcome.
- **Status:** PR #144 OPEN, awaiting maintainer review.

## Bug

`Address(network).decode()` in `src/payment.ts` routes any string starting (case-insensitively) with `${network.bech32}1` into the bech32/bech32m branch and lets its error propagate — there is no fallback. Litecoin's version byte (48) makes some perfectly valid base58check P2PKH payloads start with `LTC1` / `LTc1`, which look like the `ltc1` bech32 prefix. Those addresses throw `mixed-case string not allowed` (bech32) and then fail bech32m the same way, instead of decoding as base58check.

## Proof (master 22770eb, v2.4.1)

Reporter's exact addresses on unpatched master:

```
FAIL LTC1zjVGsmn3xcSkog7Bo1uGyDxahZVQUb -> mixed-case string not allowed
FAIL LTc1ryp642TP8mPRfPch3ZM9wGo9zRF2oJ -> mixed-case string not allowed
FAIL LTC18PhC7QM3s39HUBevPHqtrMf2mNkzSj -> mixed-case string not allowed
FAIL LTc1589Ti1BerhYUzVW4dAs8AawDtnJmTD -> mixed-case string not allowed
```

Brute force (generate random LTC p2pkh addresses until `LTC1`/`LTc1`-prefixed ones appear): 5 found in 200k tries, all undecodable pre-fix.

## Fix

Wrap the segwit branch in try/catch and fall through to the existing base58check decode on failure — the try-bech32-then-base58 order bitcoinjs-lib uses (suggested by the issue reporter). Genuine bech32/bech32m addresses (lowercase and uppercase) decode exactly as before; a string valid in neither format still throws.

Note on the earlier attempt, PR #136 (open since 2025-11, currently CONFLICTING, no maintainer review): it gates the bech32 branch on a case-sensitive prefix, which stops routing *uppercase* bech32 addresses (`LTC1Q...`) to the bech32 decoder — those then fail base58check and throw. PR #144 keeps case-insensitive routing and adds the fallback instead, and says so openly in its description (maintainer can pick either direction).

## Verification

- Post-fix: all 4 reported addresses decode as `pkh` (exact hash asserted for the first; encode∘decode round-trips for the rest); brute-forced `LTC1`/`LTc1` addresses round-trip; genuine LTC bech32 lowercase + UPPERCASE still decode as `wpkh`; garbage `LTC1qqq...` still rejected.
- New `GH-133` regression test in `test/basic.test.ts` next to the existing GH-112 test.
- Full suite: **550 tests passed**; prettier clean on both changed files.
