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

# transcript

Resolve an explicitly requested release, `STABLE` when requested, otherwise `CURRENT`. Read that release's manifest.json and SKILL.md under `versions/<release>/`. All resources belong to that release; do not mix releases. The complete authoritative library is this repository, not legacy or upstream files.

Read [CURRENT](CURRENT) or [STABLE](STABLE) to select the release. Previous releases are available only on explicit selection.
