---
name: video-library
description: Save every user-requested video for transcription, review, evaluation, or later viewing in Steve's local SQLite video library. Supports repeat counters, primary and additional categories, collections, expert/preferred/core-knowledge marks, full transcripts, and bulk dashboard editing.
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
2. For full-transcript work, prefer quiet audio-only yt-dlp download and local Whisper as described in [whisper.md](whisper.md). Existing human-authored captions may be reused when reliable. The dashboard's current Fetch button still uses the older caption-only queue; do not describe it as the unattended audio-first pipeline. Do not install models or start GPU work for a request that only asks to save a link.
3. Apply one primary category to every video. `categorize VIDEO_KEY "Category" "Subcategory"` sets the primary path and relocates transcript exports. Add other applicable categories and project collections through the local dashboard. Classify from the actual title, description, or transcript; do not infer a narrow subject without evidence.
4. For semantic transcript cleaning, resolve `clean-video-transcript/CURRENT` in the authoritative library and read that release's skill and required references. It remains the owner of spelling, faithful cleanup and source references. This wrapper's requested output takes precedence: complete readable speech, no per-cue timestamps by default, original source chapter names/timestamps when provided. Never invent chapter times or claim automated subtitle normalization is a full editorial review. Import the reviewed complete transcript back into this library.
5. Keep any content evaluation separate from the full transcript. Save notes through the dashboard or the local API. A transcript is not a summary. Preserve original sources and timing evidence.

Recommended taxonomy (extend only when needed):

- Content creation / Storytelling; YouTube strategy; Thumbnails; Titles; Video editing; Presentation
- AI and technology / AI tools; Software; Automation; Business applications
- Faith and Bible / Bible study; Prophecy; Ministry
- Health and wellbeing / Nutrition; Health
- Learning and productivity / Learning; Productivity; Personal development
- Science and culture / Science; Aviation; Current events
- Science / Space; Technology / AI; Psychology
- Other / General

## Organize and find videos

The SQLite `categories` table holds a hierarchy; `videos.primary_category_id` holds exactly one primary category per video, including Uncategorized until reviewed. `video_categories` holds additional category memberships. `collections` and `video_collections` group videos for projects across subject categories. The original `videos.category` and `videos.subcategory` text fields mirror the primary path for existing exports and tools. Do not update those fields directly.

The dashboard at `http://127.0.0.1:8876/` supports individual category/collection edits, category creation/rename/nesting/merge, collection creation/rename, and bulk add/remove/set-primary actions. Select visible videos or explicitly select every matching video across pages; changing filters clears that selection. Category filters include descendants and additional memberships. Search includes category names and aliases. Bulk add keeps prior assignments; primary changes are explicit. A primary category cannot be removed until a replacement is chosen. Each video can independently carry Subject matter expert, Preferred, and Core knowledge marks. The dashboard can filter by each mark, edit them per video, and add or remove them in bulk across filtered pages. These edits do not add request events or alter request counters.

All processing status, attempts, QA, and completion events belong in SQLite. Transcript Markdown/HTML and source timing files are outputs, not job logs or incomplete-video trackers.

## Artifacts and queries

The authoritative catalog and full-text index are SQLite. All transcript exports live under `transcripts/<category>/<subcategory>/`, with HTML and Markdown together. Raw source copies remain in the library, and original imported files are not modified. Category changes regenerate exports in the appropriate folder.

Every transcript header must include title, complete canonical URL, YouTube short ID (or not applicable), source channel, actual download/acquisition time or explicit unknown, and separate library import time. Do not replace unknown download times with today's import date. Preserve source chapter labels with timestamps and video jump links. Preserve source timing files even though the readable transcript omits per-cue timestamps.

`search "phrase"` searches titles, metadata, notes, and full transcripts. Agents can query SQLite read-only; use the CLI/API for writes so the full-text index and exported files stay consistent. `export` rebuilds HTML/Markdown. Start the dashboard with `Open Video Library.cmd` in the project root, or `serve --port 8876` from a detached process.

## Private backup

After each completed video batch or material catalog/transcript edit, run `py G:/__ai-projects/__Personal.Projects/video-library/_tools/private-github-backup.py`. It checks that `getrdone/video-library-private` is PRIVATE before uploading, VACUUMs the live database, makes and validates a compact SQLite snapshot, and verifies the pushed Git commit against the remote. The hourly and sign-in Windows task `VideoLibraryPrivateBackup` is a safety net for edits made outside an agent session. Backup attempts and results are tracked in local SQLite `_wip/private-github-sync/backup-state.sqlite`; check it if a run fails, then retry. Never claim a backup succeeded until the remote commit is verified.

The private backup includes project files, the database, and only category folders with actual Markdown/HTML transcripts. Metadata archives and source-only evidence are packed into root-level ZIPs so a restore remains complete without creating empty category folders. Keep the private catalog and transcript contents out of the public `agent-skills` repository. The private backup repository contains restore instructions. Avoid backing up temporary audio or `_wip` working files.

For ad hoc offline backups, use SQLite's backup API or the project's backup tool while preserving `transcripts/`; do not copy a live WAL database file alone.

After work, report the number saved, transcripts available, retrieval failures, and whether a repeat counter changed. Keep source-history coverage honest.

## Cross-environment intake

Use this workflow by default in all configured agents for specific user video requests. Web sessions must save directly through available authorized local tools, or send the durable handoff described in [handoff.md](handoff.md) to local ChatGPT Work/Codex. Sending this scoped handoff is explicitly authorized by Steve. Never claim an unavailable communication path worked.
