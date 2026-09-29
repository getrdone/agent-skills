---
name: video-library
description: Save every user-requested video for transcription, content or idea review, usefulness evaluation, or later viewing in Steve's local SQLite video library. Supports bulk lists, repeat-request counters, categorized full transcripts, chapter times, and a local dashboard.
---

# Video library

Canonical project: `G:/__ai-projects/__Personal.Projects/video-library`. Read its `01-NOW.md` before substantial work and `03-MEMORY.md` before changing decisions. CLI: `py G:/__ai-projects/__Personal.Projects/video-library/library.py`. Database: `video-library.sqlite` at that project root. Python 3.13 standard library; no cloud account required.

## Save first

When Steve requests a specific video or a list for transcription, review, ideas, usefulness evaluation, or saving for later, record every requested video before fetching or analyzing it. This standing instruction applies across configured local agents and, when the skill or equivalent default is installed there, ChatGPT web and Work. It is a deliberate exception to named-only specialist loading. Do not record unrelated links, unsolicited suggestions, ambient browser tabs, or search results unless they fall within the user's requested collection.

Use `add URL --purpose "what Steve requested" --source "chat identifier or source"`. For batches use `add --file ABSOLUTE_URL_LIST --purpose ... --source ...`; one URL per line. Draft lists go in the active project's `_wip/`, never a new competing library. Intake does not fetch media.

**Repeated requests:** the canonical video stays one row; each distinct user request adds one request row and raises its displayed/database-query counter by exactly 1. Do not call `add` again when retrying retrieval, importing a transcript, updating notes, or continuing the same request. Use existing record IDs for follow-up processing. `import-history` uses source-event identity to avoid inflation when rerun. Multiple actual requests must never be deduplicated merely because their URL matches.

The user may explicitly exempt a video or disable capture. Respect that. For a web/cloud session without local file access, follow [handoff.md](handoff.md). A local skill alone cannot install a web default or provide a missing transfer tool; report coverage and delivery status accurately.

## Acquire, categorize, and preserve

1. Reuse a verified complete transcript already on disk. `import-transcript VIDEO_KEY ABSOLUTE_FILE` preserves the source and creates category exports. Read the source first; never import summaries, highlight lists, or failed-download stubs as full transcripts.
2. `fetch --id VIDEO_KEY` obtains metadata and existing English captions through `G:/-- appStore/ytdlp/dlp.exe`. The caption workflow skips video downloads, prefers human captions, and falls back to automatic captions. `fetch` without an ID processes pending records; it may take time, so run large lists detached with a log and check progress responsively. Failed videos stay saved and retryable.
3. When captions are unavailable and a full transcript is requested, use the existing local Whisper sidecar, described in [whisper.md](whisper.md). This does not require a new Whisper service or paid API. Do not install models, download large media, or start GPU work for a request that only asks to save a link.
4. Apply a meaningful top-level category and subcategory using `categorize VIDEO_KEY "Category" "Subcategory"`. Reuse the taxonomy below; classify from the actual title, description, or transcript. Automatic keyword categories are provisional. Other is better than an invented classification.
5. For semantic transcript cleaning, resolve `clean-video-transcript/CURRENT` in the authoritative library and read that release's skill and required references. It remains the owner of spelling, faithful cleanup and source references. This wrapper's requested output takes precedence: complete readable speech, no per-cue timestamps by default, original source chapter names/timestamps when provided. Never invent chapter times or claim automated subtitle normalization is a full editorial review. Import the reviewed complete transcript back into this library.
6. Keep any content evaluation separate from the full transcript. Save notes through the dashboard or the local API. A transcript is not a summary. Preserve original sources and timing evidence.

Recommended taxonomy (extend only when needed):

- Content creation / Storytelling; YouTube strategy; Thumbnails; Titles; Video editing; Presentation
- AI and technology / AI tools; Software; Automation; Business applications
- Faith and Bible / Bible study; Prophecy; Ministry
- Health and wellbeing / Nutrition; Health
- Learning and productivity / Learning; Productivity; Personal development
- Science and culture / Science; Aviation; Current events
- Other / General

## Artifacts and queries

The authoritative catalog and full-text index are SQLite. All transcript exports live under `transcripts/<category>/<subcategory>/`, with HTML and Markdown together. Raw source copies remain in the library, and original imported files are not modified. Category changes regenerate exports in the appropriate folder.

Every transcript header must include title, complete canonical URL, YouTube short ID (or not applicable), source channel, actual download/acquisition time or explicit unknown, and separate library import time. Do not replace unknown download times with today's import date. Preserve source chapter labels with timestamps and video jump links. Preserve source timing files even though the readable transcript omits per-cue timestamps.

`search "phrase"` searches titles, metadata, notes, and full transcripts. Agents can query SQLite read-only; use the CLI/API for writes so the full-text index and exported files stay consistent. `export` rebuilds HTML/Markdown. Start the dashboard with `Open Video Library.cmd` in the project root, or `serve --port 8876` from a detached process.

For backup, use SQLite's backup API or the project's backup tool while preserving `transcripts/`; do not copy a live WAL database file alone.

After work, report the number saved, transcripts available, retrieval failures, and whether a repeat counter changed. Keep source-history coverage honest.

## Cross-environment intake

Use this workflow by default in all configured agents for specific user video requests. Web sessions must save directly through available authorized local tools, or send the durable handoff described in [handoff.md](handoff.md) to local ChatGPT Work/Codex. Sending this scoped handoff is explicitly authorized by Steve. Never claim an unavailable communication path worked.
