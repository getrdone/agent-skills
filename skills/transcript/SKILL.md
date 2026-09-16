---
name: transcript
description: Use when the spoken content of a YouTube video is needed — even if not explicitly requested. Supports two output modes: (1) structured format with approximate section markers, video header metadata, and ordered master reference lists for Bible verses, Spirit of Prophecy, and other sources (default) and (2) exact timestamps. Triggers on video links/IDs, requests to transcribe, summarize, quote, or extract from video. Not for uploads or account management.
version: "1.8.0"
user-invocable: true
compatibility: Requires internet access to reach transcriptapi.com. No additional runtimes or dependencies needed.
required_environment_variables:
  - name: TRANSCRIPT_API_KEY
    prompt: Your TranscriptAPI key (starts with sk_)
    help: Free account at https://transcriptapi.com — 100 credits, no card required. Or let the agent create one for you.
    required_for: all API requests
---

# Transcript

Fetch video transcripts via [TranscriptAPI.com](https://transcriptapi.com).

Two output modes are supported. Choose the mode based on user request. **Mode 2 (Structured / General Timecodes) is the default.**

## Setup

If `$TRANSCRIPT_API_KEY` is not set, read [references/auth-setup.md](references/auth-setup.md) and follow the instructions there to get and store the key.

## Required Headers

Every request needs two headers:

- **Authorization:** `Bearer $TRANSCRIPT_API_KEY`
- **User-Agent:** your agent's name and version if known (e.g. `HermesAgent/0.11.0`, `ClaudeCode/1.0`). Version is optional — agent name alone is fine. Do not omit this header or send a bare default — Cloudflare will return a 403 (error code 1010) and block the request.

## GET /api/v2/youtube/transcript

```http
GET https://transcriptapi.com/api/v2/youtube/transcript?video_url=VIDEO_URL&format=text&include_timestamp=true&send_metadata=true
Authorization: Bearer $TRANSCRIPT_API_KEY
User-Agent: YourAgent/1.0
```

| Param               | Required | Default | Values                          |
| ------------------- | -------- | ------- | ------------------------------- |
| `video_url`         | yes      | —       | YouTube URL or 11-char video ID |
| `format`            | no       | `json`  | `json`, `text`                  |
| `include_timestamp` | no       | `true`  | `true`, `false`                 |
| `send_metadata`     | no       | `false` | `true`, `false`                 |

Accepts: full URLs (`youtube.com/watch?v=ID`), short URLs (`youtu.be/ID`), shorts (`youtube.com/shorts/ID`), or bare video IDs.

**API Default:** Always use `format=text&include_timestamp=true&send_metadata=true` unless the chosen output mode requires otherwise.

## Output Modes

### Mode 2 — Structured / General Timecodes (default)

Use this by default, or when the user requests structured transcript, general timecodes, approximate sections, with reference list, or Spirit of Prophecy format.

Required document structure: header (Slug, Duration, Channel, Series); approximate blocks `[~0–7 min]` with **full spoken content** (do not summarize); Master Reference List in order Bible Verses, Spirit of Prophecy, Other Sources. Empty headings still say (none). Never emit exact second timestamps in Mode 2. Verify SOP/Bible quotes; if not found, say so in the list.

### Mode 1 — Exact Timestamps

Use only when the user explicitly asks for exact timestamps. Keep raw API timestamps. Do not force the structured header unless they also want source extraction.

## Errors

| Code     | Meaning          | Action                              |
| -------- | ---------------- | ----------------------------------- |
| 401      | Bad API key      | Check key or re-setup               |
| 402      | No credits       | Top up at transcriptapi.com/billing |
| 403/1010 | Cloudflare block | Add or fix User-Agent header        |
| 404      | No transcript    | Video may not have captions         |
| 408      | Timeout          | Retry once after 2s                 |
| 429      | Rate limited     | Wait and retry                      |

## Tips

- 1 credit per successful request. Errors don't cost credits.
- Free tier: 100 credits, 300 req/min.
- Default is Mode 2. Switch to Mode 1 only on explicit request.

Copy-paste examples: [references/curl-examples.md](references/curl-examples.md)
Mode 2 template: [references/structured-format.md](references/structured-format.md)
