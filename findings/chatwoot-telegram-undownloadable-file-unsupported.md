# chatwoot/chatwoot — Telegram files over 20 MB silently dropped, leaving blank messages

- **Issue:** https://github.com/chatwoot/chatwoot/issues/16110 (filed 2026-10-02 by Timur2915; labels Bug + channel/telegram; 0 comments, unassigned, no competing PR at submission)
- **PR:** https://github.com/chatwoot/chatwoot/pull/16124 — OPEN / MERGEABLE (2026-10-05)
- **Payment:** none posted on the issue; fix offered freely, tips pointer in the PR footer.

## Bug

The Telegram Bot API only lets bots download files up to 20 MB (`getFile` returns
`400 Bad Request: file is too big`), while users can send files up to 2 GB.
`Channel::Telegram#get_telegram_file_path` returns `nil` for any non-success
`getFile` response, and `Telegram::IncomingMessageService#attach_files` treated a
blank path as a silent skip (one info-level log line, added by #8679 to replace an
earlier crash). The message was still saved:

- no caption → a completely empty message (no content, no attachments);
- with a caption → a plain text message indistinguishable from a normal one.

Nothing in `content_attributes` / `content_type` / attachments showed an
attachment was lost, so neither agents nor webhook/API consumers could detect it.
Other channels already flag this shape: WhatsApp
(`create_unsupported_message`), Instagram/Facebook and TikTok all set
`content_attributes.is_unsupported = true`, and the dashboard renders the
standard unsupported-message notice (`Message.vue` → `UnsupportedBubble` when
`contentAttributes.isUnsupported`).

## Fix

In `attach_files`' blank-path branch, merge `is_unsupported: true` into
`@message.content_attributes` before the message is saved — the verbatim
pattern from `Whatsapp::IncomingMessageBaseService#create_unsupported_message`
(`@message.content_attributes.merge(is_unsupported: true)`; `is_unsupported` is a
declared `Message` store accessor). The caption stays in `content`, so it
remains available to API/webhook consumers. 5-line production change + comment.

## Verification (honest scope)

- Code-level proof of the bug: the blank-path branch returned without touching
  the message; the flagged path is the only difference.
- End-to-end rendering path verified by inspection: store accessor exists
  (`app/models/message.rb`), the API camelizes to `isUnsupported`, and
  `Message.vue` renders `UnsupportedBubble` on it (generic
  `CONVERSATION.UNSUPPORTED_MESSAGE` locale fallback covers Telegram).
- Syntax: `ruby -c` OK on the repo's pinned Ruby 3.4.4 (portable ruby-builder
  binary) for both the service and the spec.
- Harness: the exact merge expression was run through the store's JSON coder
  round-trip — `is_unsupported: true` persists with string keys and does not
  clobber `in_reply_to_external_id`; the unpatched path has no flag.
- Two regression specs added to
  `spec/services/telegram/incoming_message_service_spec.rb` in the file's own
  stubbing style (`get_telegram_file_path` → `nil`): no-caption video →
  no attachments, blank content, `is_unsupported` true; captioned video →
  caption preserved, `is_unsupported` true.
- **Limitation (disclosed in the PR):** the full RSpec suite was NOT run
  locally — it needs Postgres/Redis plus Chatwoot's full bundle, unavailable in
  this sandbox (no Ruby/Postgres preinstalled; 2 cores). CI is authoritative.
  No Enterprise override of this service exists (checked `enterprise/`).

## Same-run sector-5 verdicts (run 40)

- Curated framework sweep (httpx/starlette/flask/fastapi/django/aiohttp/
  celery/DRF/requests/next/vue/angular/prisma/supabase/nocodb/appwrite/
  pocketbase/directus + textual/uvicorn/poetry/ruff/pydantic/sqlalchemy/
  werkzeug/jinja/click/scrapy/mitmproxy/locust…): no fresh unassigned
  bug-label issues since 2026-10-02 outside supabase support tickets.
- jellyfin #18274 (no-change scan re-saves items): already cross-referenced by
  PRs #18278/#18294 — skip.
- chatwoot #16116 / #16118 / #16117 (stale rows on agent/account deletion):
  clean, unclaimed spares in the same repo if #16124 lands well.
- linkwarden #1849 (tag-merge unique-constraint crash) / #1851 (extension
  context menu): unclaimed spares, weaker local verification story.
