---
name: transcript
description: Use when the spoken content of a YouTube video is needed — even if not explicitly requested. Supports structured format with section markers and master reference lists (default) and exact timestamps. Triggers on video links, transcribe, summarize, quote, or extract from video.
version: "1.8.0"
---

# Transcript

Fetch via TranscriptAPI.com. Default Mode 2 (structured, approximate sections, Bible / SOP / other source lists). Mode 1 only when the user asks for exact timestamps.

Setup: `references/auth-setup.md`. Examples: `references/curl-examples.md`. Template: `references/structured-format.md`.

Required headers: Authorization Bearer $TRANSCRIPT_API_KEY and a real User-Agent.
