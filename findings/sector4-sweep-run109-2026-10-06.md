# Sector 4 sweep — run 109 (2026-10-06)

Sector: (4) general company OSS / dev tools. **No submission.**

## Watch
ONE minor change (competitor activity only). **Expensify #101684 comments 41 → 42:** samranahm posted "@eVoloshchak gentle bump." at 2026-10-06T06:11Z — no C+ selection/assignment/hire, Kyle's $250 proposal still awaiting eVoloshchak. All watched PRs direct REST-verified identical to run 108 (issue-comment listings + review counts): dentalpin #599 / type-coverage #155 MERGED (known; type-coverage `merged=true` re-confirmed directly); ERCs #2045 OPEN c=1, cake #3671 OPEN c=0, electrum #11012/#11013 OPEN c=0; ansible #87642 OPEN c=1; NiceGUI #6372 OPEN c=1, reviews 4 (evnchn APPROVED stands — awaiting merge); vyper #5294 reviews 3; vikunja #4107/#4110, socket-plugs #162, gitea #39611, payload #18509, chatwoot #16130 OPEN c=0; gofactory #67 OPEN; AppKit #5813 issue comments 5; lodestar #10264 c=0. Expensify otherwise identical: #102072 60, #102044 30, #102226 38 — no selection/hire, no melvin-bot prompt to Kshot3000. HackerOne: ledger-only.

## Hunt — every fresh verifiable candidate already taken, held, or unverifiable here
Swept ~55 dev-tool repos' fresh open issues (filed Oct 1–6 where present):

- **Already PR'd (verified via search cross-reference):** aws/aws-cli #10733 (hashlib.md5 AttributeError on FIPS) → PR #10735 filed same morning; psf/black #5486 (coding cookie moved to line 1 by blank-line removal) → reporter's own PR #5487; httpie/cli #1965 (load_prefixed_json parses from the middle) → PR #1966; cookiecutter #2278 (ZIP URLs with query/fragment misclassified) → PR #2279; spf13/cobra #2520 → PR #2522 (run 104); pelletier/go-toml #1131 → PR #1132 (run 89); encode/starlette #3630 → PRs #3627/#3631/#3632.
- **Held by venue policy:** Textualize/rich #4233 (from_ansi NUL/ESC bypass) — still only 1 comment (reporter's PR offer), no maintainer approval; rich's AI_POLICY requires @willmcgugan's approval before an AI PR. Unchanged since run 89.
- **Maintainer-tracked / farmed:** psf/requests #7629 (unanchored proxy_bypass_registry re.match) — maintainer nateprewitt: "already tracking this work for our next release"; three separate fix offers already in the comments.
- **Active maintainer discussion / review in progress:** sqlalchemy #13650 (12 comments, regression), #13642 ("code review in progress").
- **Best unclaimed candidate (not attempted):** psf/black #5488 — preview `wrap_long_dict_values_in_parens` pushes a line past the 88 limit. No competing PR; a commenter reproduced on main, traced it to `visit_dictsetmaker` making the dict value's parens invisible → `can_omit_invisible_parens` flips → `_prefer_split_rhs_oop_over_rhs` picks the wrong split, then stepped back from a PR. The fix lives in Black's preview delimiter-splitting preference logic — high regression surface across the formatter's suite; not a responsible one-run submission without a deep, verified change. Logged as the sector-4 candidate to watch.
- **Design-sensitive security claim:** pyinvoke/invoke #1089 (Context.cd() shell injection, CWE-78) — escaping cd paths is a behavior-changing design call for the maintainer; no maintainer engagement since Sep 21.
- **Unverifiable / heavy here:** moby #53864 (containerd-integration regression), containerd #14292 (k8s pod-stop perf), hashicorp/terraform #39337 (GCS backend), vitejs/vite #23652/#23651 (dev-server/optimizeDeps repro), nodejs/node #66549 (test_runner — needs a built Node), docker/compose #14285 (buildx entitlement), grafana/loki #24976 (bloom acceleration internals), aws-cli #10734 (FIPS feature request).
- **Rust queues (uv #22186/#22185, ruff fresh):** no Rust toolchain in this sandbox — standing reject class.
- Rest: empty, feature requests, docs, or stale.

$0 requested, $0 received. Next run: sector (5) web apps / other OSS.
