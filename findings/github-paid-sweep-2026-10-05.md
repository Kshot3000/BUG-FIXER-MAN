# GitHub-wide paid sweep — 2026-10-05 (parent-requested, sector-3 adjacent)

Full GitHub sweep for PAID work not already proposed/submitted. Result: **no new submission** — one genuinely new platform found (BountyHub) and its live bounties assessed; everything else is the known dry landscape. $0 requested, $0 received.

## Checks run (all direct-verified)
- **Expensify/App Help Wanted, created >2026-10-01:** zero new issues. Newest remains #102742 (Oct 1). Kyle's 3 live $250 proposals (#102072, #102044, #101684) unchanged; #102226 lost (known).
- **Opire** (api.opire.dev/rewards): exactly the same 5 dead rewards as every prior check — rodrigompy/bugb #1 ($100, junk repo), radumarias/rencfs #3 ($42, 2024), trovu/trovu #329 ($30, 23 claimers/38 trying), flowese/UdioWrapper #7 ($20, 16/28), buape/kiai-bounties #1 ($20). No escrow; none viable.
- **`Paid Bounty` label, GitHub-wide:** only crhy/OpenAirShips #8 (stale, known).
- **`💎 Bounty` label, GitHub-wide:** SecureBananaLabs/bug-bounty (synthetic auto-generated vuln-issue farm, no payout evidence), a personal qdrant fork (stale since June), a test repo. Nothing credible.
- **`$`/`USDC` in titles, created >2026-08-15:** spam farms (bounty-plaza, MisakaNet lessons, relayhop radar), SS13 game bounties (Goob-Station, SPLURT — BYOND/Windows tooling, in-game scope), rustchain-bounties (pays in its own RTC token), microG (below). Nothing else credible.
- **BasedHardware/omi:** no open `bounty`-label issues and no `$`-title issues right now — the standing program from PAID-AVENUES has no live targets.

## Merit Systems — checked directly, no live funded-issue surface
- merit.systems now presents as an "Agentic Commerce Product House"; the OSS attribution product has no publicly discoverable funded GitHub issues (GitHub search for `merit.systems` in issue bodies/comments returns only Merit-Systems' own product repos: echo #457, agentcash-router #5 — internal items, no contributor payment mechanism stated).
- Verdict: not a live channel for us today. Re-check only if they relaunch a public program.

## NEW PLATFORM: BountyHub (bountyhub.dev, bot `bountyhub-bot`)
Individuals fund GitHub issues; a merged PR claims; payouts run through Stripe (a funder comment on microG #2851 references retracting/refunding via Stripe). Receiving likely requires a BountyHub account — a Kyle sign-up step, flagged not done. Added to PAID-AVENUES.md. Live funded issues found, all assessed **not completable by us**:

1. **microg/GmsCore #2851 — $85** (D3SOX $35 + fm-knopfler $65, fm-knopfler later retracted; D3SOX re-added $50 → $85 current). Task: Play Integrity over remote (multi-step) DroidGuard + server/guide. Real project, real money — but the acceptance bar is a video of a real app working on real devices; the thread is a graveyard of failed attempts (maintainer on the latest: "like all the other AI things it doesn't work at all"), heavily swarmed, and verification is hardware-in-the-loop — impossible to verify red→green locally. **Skipped: not verifiable in our environment.**
2. **microg/GmsCore #2843 — $2,340 WearOS support.** Mega-feature, device-dependent, same swarm dynamics. Skipped.
3. **microg/GmsCore #2994 — $14,999 RCS support.** Multi-month protocol implementation. Skipped.
4. **moorcheh-ai/memanto #1852 — $100 Security Challenge** (2,315★ Python memory layer; challenge hosted on BountyHub, claim = public PR with fix + PoC; scope = core package + their live backend). Real and active: PRs being merged (#1980), organizer responsive. BUT the stated deadline (Oct 5, 23:59 UTC) has just passed with only an unconfirmed "probably extend by a week," the field is farmed, and the repo **restricts interactions to prior contributors** — my deadline-clarifying comment was rejected by GitHub, so the extension cannot be confirmed without opening a PR first. **Held, not chased:** worth a dedicated local audit of the core package ONLY if the extension is confirmed; do not probe their live backend (local code review only, per hard rules).

## Bottom line
21st consecutive paid-sector check with no completable new paid item. The near-term money still sits where it was: the 3 live Expensify $250 proposals (reviewer queues), Superteam Swap.io (Kyle's session, Oct 14), and the HackenProof Flow report (ready, Kyle's signed-in submission + $1 fee OK). New watch item added: BountyHub-funded issues in tractable repos.
