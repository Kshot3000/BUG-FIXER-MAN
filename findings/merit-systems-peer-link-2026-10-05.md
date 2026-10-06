# Merit Systems — deep check after Kyle's sign-up (2026-10-05, evening)

Kyle created a Merit Systems account via the Merit Terminal (terminal.merit.systems), connected with GitHub as Kshot3000. This addendum re-checks Merit with the account live. **Headline: Merit IS a real, live paid channel — but its only funded-issue program is fully claimed, and acceptance is gated on real bank-account ownership. No submission was possible today; exact unlock steps for Kyle are at the bottom.** $0 requested, $0 received.

## How Merit actually pays (from Merit's own rollout docs)
- Projects fund pools in the Merit Terminal; the program page pattern is `terminal.merit.systems/<org>/<repo>`.
- Contributors are paid in USDC after a maintainer records acceptance; per Merit's rollout announcement, payouts are **claimed in the Terminal after filling out a W-9/W-8BEN form** — a Kyle-only tax step inside his account.
- Two models exist: per-issue funded bounties (zkp2p below) and attribution distributions for merged PRs (drizzle-orm, Unitary Foundation repos, seveibar's projects mention the Terminal — no per-issue amounts, nothing actionable as a funded issue).

## The one funded-issue program: zkp2p/peer-link ($1,000 pool, 20 × $50)
Real project (ZKP2P fiat↔crypto ramps). Each issue: integrate one bank's transfer adapter (`banks/<cc>/<bank>/`), labels `integration, Merit, $50`, submissions due **2026-11-15 23:59 UTC**. Claim/payment flow, verbatim from the issues:
1. Comment with the surface + transfer type you'll cover, and **confirm you or a collaborator own an account you are authorized to use** (never post credentials/records).
2. A maintainer assigns **one attempt for 14 days**; "unassigned competing work earns nothing extra."
3. Build per AGENTS.md + skills/contribute-bank/SKILL.md: pure deterministic adapter + manifest + acquisition notes, synthetic fixtures + negative tests, `npm run check` and `npm run privacy -- --staged` must pass, no real banking records in Git.
4. **Acceptance additionally requires one privacy-safe live report from the authorized account owner, bound to the exact adapter and harness commits, using an existing transaction.** @0xSachinK reviews and records acceptance on the issue, then pays through Merit. Merge alone never triggers payment.

## Why nothing was submittable today (all direct-verified)
- **All 20 funded banks already have claimants and/or open PRs** (40+ open PRs in the repo): Chase #73 → PRs #144/#152; Wells Fargo #75 → claimed by Simultech369, PR #98; Bank of America #74 → assigned (Primuez, label `bounty: assigned`) + PR #143; and likewise OPay, Vietcombank, Monobank, BBVA MX/ES, Itau (×2), BCP Peru, Kaspi, M-Pesa, MTN MoMo, bKash, BCA, GCash, Ziraat (×2), Uala (×2), Easypaisa, Bancolombia. A late unassigned entry earns $0 under the program's own rules.
- **The account-ownership gate is decisive for the other 17 banks:** Kyle (Wisconsin, US) cannot truthfully confirm owning an authorized Bancolombia/GCash/bKash/Kaspi/etc. account, and cannot produce the required live report from one. The only banks he could plausibly hold are the three US ones — all taken (above).
- Newer Singapore/HK issues (#158–#162, #183) are only "[$50 **pending funding**]" and already have PRs too (#163–#169, #184).

## Kyle-only unlocks (precise)
1. **Say which of Chase / Wells Fargo / Bank of America you actually have an account with** (if any). That's the only realistic target set. I then watch that bank's assigned attempt; if it fails review or the 14 days lapse, I post the claim comment the same day (surface + transfer type + your ownership confirmation, which only you can make true) and build the full adapter package on assignment.
2. **During acceptance you'd run the repo's local harness once against one existing transaction** in that account to produce the privacy-safe live report — raw captures stay on your machine; only the redacted report ships. I prep everything else (adapter, fixtures, tests, checks, PR).
3. **In your Merit Terminal: complete the W-9 form** Merit requires before any payout can be claimed. Needed only when a payout exists, but it's yours alone to do.

## Also updated
PAID-AVENUES.md Merit entry corrected (it previously said "not a live channel" — that was based on the marketing homepage; the Terminal is where the programs live). Pipeline + run log updated. Watch item: peer-link US-bank attempts (Chase/Wells Fargo/BofA) for failure/expiry openings until 2026-11-15.
