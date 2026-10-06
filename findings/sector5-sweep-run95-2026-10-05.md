# Sector 5 (web / other OSS) sweep — run 95, 2026-10-05

**Result: NO submission.** Fresh bug queues (filed ≥ 2026-10-03, verified individually via the GitHub REST/search APIs) were empty, already fixed by open PRs, known rejects, or not locally verifiable. No verified bug → no PR, per the quality gate.

## Status watch (run 95)
**NO changes.** All body-listed + spot PRs direct REST-verified identical to run 94:
- dentalpin/dentalpin #599 and plantain-00/type-coverage #155: MERGED (known).
- ethereum/ERCs #2045 OPEN (1 issue comment), cake-tech/cake_wallet #3671 OPEN (0), spesmilo/electrum #11012 / #11013 OPEN (0).
- Spot: NiceGUI #6372 OPEN (1 comment, 3 reviews — awaiting re-review); vyper #5294 OPEN (0 issue comments, 3 reviews: Sporarum COMMENTED + Kshot3000 ×2, all known); AppKit #5813 OPEN (5 comments); gitea #39611, payload #18509, socket-plugs #162, chatwoot #16130, vikunja #4107, gofactory #67 all OPEN (0 comments).
- **Artifact caught + discarded:** a batched `--jq length` count briefly read vyper/gitea/payload/chatwoot review counts higher (4/2/2/1); direct per-PR review listings show the historical values (3/0/0/0). The listing is authoritative.
- Expensify counts identical (per_page=100): #102072 55, #101684 41, #102044 30, #102226 38 — no C+ selection/assignment/hire, no melvin-bot prompt to Kshot3000.
- HackerOne: ledger-only (no browser check this run).

## Hunt detail (sector 5)
Swept fresh `bug`-label queues (≥ Oct 3) for outline, Ghost, listmonk, directus, linkwarden, jellyfin, umami, nocodb, chatwoot, payload, formbricks, mastodon, discourse, plausible, appwrite, strapi, pocketbase, twenty, medusa, supabase, AFFiNE, filebrowser, mealie, joplin.

- **Already PR'd:** listmonk #3250 → PR #3256; payload #18521 → PR #18526, #18480 → PR #18483, #18476 → PRs #18487/#18479; chatwoot #16122 → PR #16123, #16117/#16118 → PRs #16120/#16121, #16116 → our PR #16125.
- **Known rejects / ours:** chatwoot #16133 (instance schema quirk), payload #18498 (our PR #18509), #18494 → PR #18496, #18489 → PR #18488.
- **payload #18490 (plugin-mcp revalidations dropped during MCP tool calls)** — no competing PR, but the fix is a transport-semantics change (buffering the streaming MCP response so Next.js applies hook revalidations) with session/SSE implications, and verification needs the full Payload+Next integration stack that is unavailable in this sandbox. Maintainer design territory — not a clean verified submission.
- **chatwoot #16114 (Captain gpt-6 models missing from `config/llm_models.json`)** — the catalog fix needs gpt-6 family specs (ids, context windows, pricing/capabilities) that cannot be verified from any source available here; inventing catalog metadata is exactly the fabrication the quality gate forbids. The alternative (OpenAI passthrough with `assume_model_exists`) is a maintainer design choice.
- **linkwarden #1854 (zombie chrome-headless processes in Docker)** — PID-1 reaping / process-lifetime issue that manifests over weeks of runtime; no local reproduction possible.
- **jellyfin fresh (#18312/#18307/#18302/#18301)** — C#/.NET, no dotnet toolchain in this sandbox (standing reject class).
- **supabase fresh** — all hosted-platform support tickets (stuck projects), not code bugs. **joplin fresh** — mostly open PRs and Joplin Cloud sync behaviour needing a cloud account.
- outline / Ghost / directus / umami / nocodb / formbricks / mastodon / discourse / plausible / appwrite / strapi / pocketbase / twenty / medusa / AFFiNE / filebrowser / mealie fresh bug queues: empty.

## Payments
None requested, none received. All-time received remains $0.
