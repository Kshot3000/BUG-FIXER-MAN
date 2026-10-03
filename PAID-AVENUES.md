# Where bug work actually pays — verified 2026-10-02

> **The core truth:** legitimate venues pay only for work that is **in-scope, pre-authorized, and reported first through their channel**. An unsolicited fix followed by a payment request pays $0 everywhere — and can read as spam. So we hunt *inside* these programs and open-issue systems, verify with a working proof-of-concept, and submit there first. This repo is the public log, not the submission channel.

Quality is existential in 2026: programs are actively cracking down on AI-generated report volume (MetaMask narrowed scope and cut Low/Medium bounties; GitHub's program added signal requirements; curl ended its paid bounty entirely in Jan 2026). Verified PoC or don't submit.

## Crypto / Web3 — highest upside, pays to ETH/SOL wallets

| Platform | Site | How it pays | Notes |
|---|---|---|---|
| Immunefi | immunefi.com/explore | Per-bug, crypto, after triage; code PoC required | 171 live programs at verification; many require KYC + OFAC screening. Also absorbing Code4rena's customers and wardens (see Dead, below) — this is where the contest crowd moved |
| Sherlock | sherlock.xyz · audits.sherlock.xyz | Contests + bounties, USDC | Payout gate: USDC withheld until 2 valid lifetime issues submitted; only High/Medium pay |
| Cantina | cantina.xyz/competitions | Competitions + bounties, USDC | Best work is curated/invite + KYC; build reputation elsewhere first |
| CodeHawks | codehawks.cyfrin.io | Real contests pay USDC; **First Flights pay XP only ($0)** | Best beginner on-ramp: learn the report format on First Flights, then paid contests |
| HackenProof | hackenproof.com/programs | Managed Web3 bounties, per program terms | Mid-tier, less crowded than Immunefi |
| Hats Finance | hats.finance | On-chain vaults, encrypted report, committee-approved payout | No KYC for researchers; EVM-only |
| Ethereum Foundation | ethereum.org bug bounty | Direct program, ETH or DAI | Elite difficulty; websites/DNS/ENS/ERC-20s out of scope |

## General platforms — PayPal fits here

| Platform | Site | How it pays | Notes |
|---|---|---|---|
| HackerOne | hackerone.com/bug-bounty-programs | **PayPal, Bitcoin via Coinbase, or bank**; W-9 for US hunters | Public crypto programs include Coinbase and MetaMask |
| Bugcrowd | bugcrowd.com | Cash via platform, **first reporter only** — duplicates pay nothing | Anyone can sign up for public programs |
| YesWeHack / Intigriti | — | Per-program cash | Verify each listing actually pays — some are VDP-only ($0) |
| Internet Bug Bounty | hackerone.com/ibb | Pooled fund for **CVEs in core open source**, split 80% finder / 20% project | Bug must be a real, fixed CVE in a covered project |

## Paid GitHub issues — smallest dollars, fastest start

- **Opire** — opire.dev. Anyone can attach a bounty to a public GitHub issue; hunters claim via the issue and a PR. Developer keeps 100%, but there is **no escrow** — the funder arranges payment after approval, so verify the funder first. Typical live bounties are small.
- **"Paid Bounty" label repos** — e.g. BasedHardware/Omi. Rules vary; typically the PR must be **merged**, eligibility is at maintainer discretion, and claims go to the team with a PayPal account. Always confirm the issue is open, unassigned, and the funder has paid before.
- **Superteam Earn** (Solana) — earn.superteam.fun. Open listings paid in USDC/USDG to a Solana wallet; mostly dev/content work, useful filler income.

## ☠️ Dead — do not chase

- **Code4rena** — announced its wind-down on 2026-05-13; active contests/bounties run to completion but **no new accounts can be created** (confirmed 2026-10-02). Immunefi is absorbing its customers and wardens — hunt there instead
- **Algora** — pivoted to recruiting; bounty pages 404
- **Polar.sh** — now a billing platform; issue funding gone
- **OnlyDust** — shut down
- **Bountysource / IssueHunt** — no live, functioning bounty marketplace found; treat any bounty referencing them as unpaid until proven otherwise

## Realistic ranking

1. **No barriers, start today:** CodeHawks First Flights (learn, $0) → Sherlock + Cantina public contests (USDC) + Opire / Paid-Bounty issues (small, PayPal — verify funder first)
2. **Best PayPal fit:** HackerOne and Bugcrowd public programs
3. **Highest ceiling, hardest:** Immunefi (now also home to Code4rena's migrated programs and wardens) + HackenProof — requires working Foundry PoCs and, on Immunefi, KYC (a sign-up step Kyle does himself)
