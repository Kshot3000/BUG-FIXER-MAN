# vyperlang/vyper — parser source spans desync on form feeds / non-ASCII, silently compiling wrong literal values

- **Project:** Vyper compiler (Ethereum smart-contract language) — https://github.com/vyperlang/vyper
- **Issue:** #5292 (filed 2026-10-04 by hyeon-Sec, 0 comments, unassigned, no competing PR; public follow-up to a closed private GHSA, filed at maintainer request — no released version affected) — https://github.com/vyperlang/vyper/issues/5292
- **Submission:** PR #5294 OPEN / MERGEABLE (2026-10-05) — https://github.com/vyperlang/vyper/pull/5294 — branch `Kshot3000/vyper@fix/parser-source-span-byte-offsets` (ca79f0e)
- **Bounty/payment:** none posted on the issue; fix offered freely, tips welcome via this hub's README. $0 requested, $0 received.

## Bug
`AnnotatingVisitor` (vyper/ast/parse.py) slices each node's source text with `line_index[lineno] + col_offset`, but (1) `line_index` was built from `str.splitlines()`, which also breaks on `\x0c`, `\x0b`, `\x85`, U+2028/U+2029 — none of which are line boundaries for CPython, so one form feed shifted every following line by one; and (2) CPython `col_offset`s are UTF-8 **byte** offsets within the line, applied directly as character indices, so any multi-byte character earlier on a line displaced every following span. `visit_Num` re-derives Hex/Bytes/Decimal values from the sliced text, so affected literals silently compiled to values the source does not contain; `src` source-map entries and error pointers were misaligned by the same spans.

## Proof (red → green, local, Python 3.12 venv, master 17e925d)
- Issue repro exact: control `A: constant(address) = 0x1111…1111` parses as Hex; the form-feed variant and the U+FB01 (NFKC) variant both sliced shifted text and became `Int` with value `97433442488726861213578988847752201310395502865` (the issue's number, character-for-character). A `1.5` decimal after a form feed became `Decimal('1')`; a `0b…` literal was re-typed Bytes→Int. Unpatched, compiling the form-feed variant raised a `TypeMismatch` whose own source pointer was garbled (`line 2:23` pointing at "line 3" text), as the issue described.
- Post-fix all variants slice exactly: Hex value/string, `Decimal('1.5')`, binary `Bytes`, plus U+2028-in-comment, CRLF, non-ASCII/astral previous-line, form-feed-at-EOL and form-feed-on-own-line cases.
- End-to-end: form-feed-prefixed contract compiles to runtime bytecode **identical** to the control (deployment bytecode differs only in the appended source hash, as expected).
- Tests: 9 new regression tests in tests/unit/ast/test_parser.py — 7 fail unpatched, all pass patched (the 2 always-passing ones guard previous-line non-ASCII). Full `tests/unit/`: **4769 passed, 5 skipped, 12 xfailed, 0 failures**. tests/functional/syntax/test_constants.py passes. black + flake8 clean on touched files.

## Fix
Root-cause fix at the span computation (not a visit_Num special-case, so source maps and error pointers are fixed too):
- `source_lines`: split only on `\n`, `\r`, `\r\n`, matching CPython's tokenizer.
- New `_char_index(lineno, byte_col_offset)`: converts byte columns to character offsets by decoding the line's UTF-8 prefix; the hand-set Module end column is now expressed in byte units to match.

## Sector-2 sweep rejects (same run)
cosmjs #1982 (reporter's fix PR #1983 still open), MystenLabs/ts-sdks #1303 (feature/design request — add a field saying which simulation mode ran; network-dependent), connext/monorepo #6394/#6395 (detailed audit-style reports, 0 comments, but repo dormant since 2026-03-04 and the monorepo is heavy — low merge likelihood; #6394 swaputil amount-unit bug noted as a future candidate if the repo revives), superfluid #2233 (duplicate sfId 5 — reporter themselves says only a maintainer can say which network's published id may move; decision-blocked), UniswapX #381 (team-tracked in Linear), smart-order-router #968 (complex routing internals), web3.py #3889 / balancer #2664 / superfluid #2240 (promo/"machine-proven" spam-pattern issues), anchor #3838/#5067 (Rust/IDL, heavy), aptos-core (Move compiler, heavy), near-api-js #1639 (standing reject — fix PRs already open), solana-web3.js / LI.FI / Safe-apps / CowSwap queues (stale or no fresh verifiable bugs).
