---
name: video-library
description: Save every user-requested video for transcription, review, evaluation, or later viewing in Steve's local SQLite video library. Supports repeat counters, a closed ten-category list with one primary and up to two additional categories, collections, expert/preferred/core-knowledge marks, flat named transcript artifacts, an auto-saving detail page with separate AI takeaways and personal notes, and bulk dashboard editing.
---

# Video library

Canonical project: `G:/__ai-projects/__Personal.Projects/video-library`. Read its `AGENTS.md` before any change, `01-NOW.md` before substantial work, and `03-MEMORY.md` before changing decisions. CLI: `py G:/__ai-projects/__Personal.Projects/video-library/library.py`. Database: `video-library.sqlite` at that project root. Python 3.13 standard library; no cloud account required.

## Artifact layout — flat, one grammar, frozen names

All artifacts for a video sit **directly** in `transcripts/`. There are no subfolders, and no category value can ever create one.

```
transcripts/YYYY-MMDD--key--NNN--role--variant--slug.ext
2026-0929--dQw4w9WgXcQ--001--transcript--timecoded--never-gonna-give-you-up.srt
2026-0929--dQw4w9WgXcQ--002--transcript--clean--never-gonna-give-you-up.md
2026-0929--dQw4w9WgXcQ--003--transcript--clean--never-gonna-give-you-up.html
2026-0929--dQw4w9WgXcQ--004--metadata--compact--never-gonna-give-you-up.json
```

The date is `YYYY-MMDD` - the workspace date format, four-digit year with zero-padded two-digit month and day, the same one every filename, log and note uses. There is no exception. It is the **first acquisition date, frozen forever**; never re-stamp it on re-export. `key` is the 11-character YouTube video ID, or `no-id` for a non-YouTube source. It comes **before** the ordinal on purpose: an ordinal-first name scatters one video's four artifacts across four sort positions, so a plain directory listing never shows them together. `NNN` comes from a closed role table: `001` timed source, `002` clean Markdown, `003` clean HTML, `004` compact metadata. There is no `005`; a role outside the table is a bug, not a feature. `slug` is a kebab-case title capped at 68 characters.

`library.ARTIFACT_NAME` is the current contract and `library.LEGACY_ARTIFACT_NAME` is retained read-only for recognising pre-1.4.0 files. If the grammar ever changes again, add a new pattern rather than editing the old one, then run `py library.py resync-artifacts` to see the rename list and `--apply` to perform it. Resyncing renames files; it never touches a stored stem.

The per-video base `date--key--slug` is written once into `transcripts.artifact_stem` and reused verbatim. Read it; never recompute it from current data. That is what makes a corrected title, a metadata refresh, or a category change unable to rename or orphan a file. A re-import overwrites the same files in place. Superseded source bytes live in the `transcript_sources` table, not in per-video source folders. Exact `.srt`/`.vtt` streams stay byte-identical.

## Categories — closed list, single level

Choose from exactly these ten, by id or exact name. Free text is rejected with the valid list.

| Category | Videos | Absorbs |
|---|---|---|
| `Content Creation` | 41 | video editing, YouTube strategy, audio production, photography, cameras, graphic design |
| `Web Design & Conversion` | 25 | web design |
| `Marketing & Sales` | 22 | marketing and sales, business applications |
| `Storytelling & Communication` | 19 | storytelling, communication, presentation |
| `Science & Nature` | 15 | space, energy, science, nature, aviation, history |
| `Bible & Faith` | 11 | Bible study, prophecy, ministry |
| `Software & AI` | 5 | AI tools, software |
| `Technology` | 3 | robotics, consumer electronics, neurotechnology |
| `Personal Development` | 2 | personal development, psychology |
| `Other` | 0 | reserved |

Every video has **exactly one primary** category and at most **two additional** ones, from the same list. There is no second level; `subcategory` is deprecated and always empty. The Add dialog and `POST /api/add` take a single `category` from this list; the subcategory input no longer exists, and a script that still posts `subcategory` sends a field nothing reads. Never create a category or a folder from a phrase, a title fragment, or a guess. Intake and auto-classification fall back to `Other`; only an explicit `categorize` fails loudly. Changing a category moves zero files.

Before finishing, run `py G:/__ai-projects/__Personal.Projects/video-library/_tools/verify-layout.py` (or `py library.py verify`). It is read-only, safe at any time, and must report CLEAN. It checks that every recorded path exists, every file on disk is recorded, every stem matches the contract, no directory exists under `transcripts/`, every category is on the list, and no video exceeds the additional-category cap.

## Save first

When Steve requests a specific video or a list for transcription, review, ideas, usefulness evaluation, or saving for later, record every requested video before fetching or analyzing it. This standing instruction applies across configured local agents and, when the skill or equivalent default is installed there, ChatGPT web and Work. It is a deliberate exception to named-only specialist loading. Do not record unrelated links, unsolicited suggestions, ambient browser tabs, or search results unless they fall within the user's requested collection.

Use `add URL --purpose "what Steve requested" --source "chat identifier or source"`. For batches use `add --file ABSOLUTE_URL_LIST --purpose ... --source ...`; one URL per line. Draft lists go in the active project's `_wip/`, never a new competing library. Intake does not fetch media.

**Repeated requests:** the canonical video stays one row; each distinct user request adds one request row and raises its displayed/database-query counter by exactly 1. Do not call `add` again when retrying retrieval, importing a transcript, updating notes, or continuing the same request. Use existing record IDs for follow-up processing. `import-history` uses source-event identity to avoid inflation when rerun. Multiple actual requests must never be deduplicated merely because their URL matches.

The user may explicitly exempt a video or disable capture. Respect that. For a web/cloud session without local file access, follow [handoff.md](handoff.md). A local skill alone cannot install a web default or provide a missing transfer tool; report coverage and delivery status accurately.

## Acquire, categorize, and preserve

1. Reuse a verified complete transcript already on disk. `import-transcript VIDEO_KEY ABSOLUTE_FILE` preserves the source and creates category exports. Read the source first; never import summaries, highlight lists, or failed-download stubs as full transcripts.
2. For full-transcript work, prefer quiet audio-only yt-dlp download and local Whisper as described in [whisper.md](whisper.md). Existing human-authored captions may be reused when reliable. The dashboard Fetch action creates a durable SQLite batch for the audio-first worker; it runs without an agent supervising it. Do not install models or start GPU work for a request that only asks to save a link.
3. Apply one primary category to every video. `categorize VIDEO_KEY "Content Creation"` sets the single-level category. The closed list above is the only set of valid names. Add up to two further applicable categories and any project collections through the local dashboard. Classify from the actual title, description, or transcript; do not infer a narrow subject without evidence. A category change is a single row update and moves no files.
4. For semantic transcript cleaning, resolve `clean-video-transcript/CURRENT` in the authoritative library and read that release's skill and required references. It remains the owner of spelling, faithful cleanup and source references. This wrapper's requested output takes precedence: complete readable speech, no per-cue timestamps by default, original source chapter names/timestamps when provided. Never invent chapter times or claim automated subtitle normalization is a full editorial review. Import the reviewed complete transcript back into this library.
5. Keep any content evaluation separate from the full transcript. Save notes through the dashboard or the local API. A transcript is not a summary. Preserve original sources and timing evidence.

Recommended taxonomy: the closed ten-item list above. Extend it only by editing `CATEGORIES` in `library.py` and the seed in `schema.sql` together, then re-run `py library.py collapse-categories` to remap existing videos. Never add a category ad hoc from a request.

## Organize and find videos

The SQLite `categories` table holds the closed single-level list; `videos.primary_category_id` holds exactly one primary category per video, including `Other` until reviewed. `video_categories` holds up to two additional category memberships. `collections` and `video_collections` group videos for projects across subject categories. The `videos.category` and `videos.subcategory` text fields are a deprecated mirror kept in step with the primary category; `subcategory` is always empty. Do not update those fields directly.

The dashboard at `http://127.0.0.1:8876/` supports individual category/collection edits, collection creation/rename, and bulk add/remove/set-primary actions. Creating or renaming a category is refused; the list is closed. Select visible videos or explicitly select every matching video across pages; changing filters clears that selection. Category filters include descendants and additional memberships. Search includes category names and aliases. Bulk add keeps prior assignments; primary changes are explicit. A primary category cannot be removed until a replacement is chosen. Each video can independently carry Subject matter expert, Preferred, and Core knowledge marks. The dashboard can filter by each mark, edit them per video, and add or remove them in bulk across filtered pages. These edits do not add request events or alter request counters.

## Video detail page

The dashboard is plain HTML, CSS and JavaScript with no build step, so the wiring between the three files is itself the contract. `web/app.js` is a base `App` object plus stacked `Object.assign` and bind-wrapping layers. The video detail dialog is four of those layers, and the upper ones find their insertion points by looking up the `organize-form` class and the `Source information` and `Transcript` headings. Renaming an anchor disables a layer silently instead of raising, so `tests/test_web_assets.py` asserts all three.

- **The organize form auto-saves and there is no Save button.** Primary category, additional categories, collections, and the three marks persist on `change`; the two textareas save 800 ms after typing stops and on blur. Each affected section carries its own `save-status` line with a timestamp.
- **Takeaways and Personal notes are different fields and must stay different.** `summary` is the AI-authored write-up; `notes` is Steve's own. Never fall back from one to the other. Takeaways render through a line-oriented reader that treats a short line above a dash list as a heading, because that is the shape AI summaries actually arrive in.
- **The two-additional-category cap is enforced twice, deliberately.** The page disables further tiles and explains why; `_apply_organization` raises and rolls the whole payload back, so a third extra arriving in one request leaves nothing partially written. The server side is the real gate.
- **Never use `innerHTML`.** Summaries are built with `textContent` so AI-authored text cannot inject markup.
- **An element removed from `index.html` must also be removed from `app.js`.** A dangling `this.el('…')` throws on the next use; the static test now checks every lookup against a real `id`.

All processing status, attempts, QA, and completion events belong in SQLite. Transcript Markdown/HTML and source timing files are outputs, not job logs or incomplete-video trackers.

## Artifacts and queries

The authoritative catalog and full-text index are SQLite. All transcript exports live flat in `transcripts/` under the naming contract above, with HTML and Markdown side by side. Raw source copies are preserved in the `transcript_sources` table and original imported files are never modified. Because the artifact stem is frozen, a category change or a title correction does not regenerate or relocate anything.

Every transcript header must include title, complete canonical URL, YouTube short ID (or not applicable), source channel, actual download/acquisition time or explicit unknown, and separate library import time. Do not replace unknown download times with today's import date. Preserve source chapter labels with timestamps and video jump links. Preserve source timing files even though the readable transcript omits per-cue timestamps.

`search "phrase"` searches titles, metadata, notes, and full transcripts. Agents can query SQLite read-only; use the CLI/API for writes so the full-text index and exported files stay consistent. `export` rebuilds the artifact set in place. `verify` audits the layout without writing. Start the dashboard with `Open Video Library.cmd` in the project root, or `serve --port 8876` from a detached process.

## Private backup

After each completed video batch or material catalog/transcript edit, run `py G:/__ai-projects/__Personal.Projects/video-library/_tools/private-github-backup.py`. It checks that `getrdone/video-library-private` is PRIVATE before uploading, VACUUMs the live database, makes and validates a compact SQLite snapshot, and verifies the pushed Git commit against the remote. The hourly and sign-in Windows task `VideoLibraryPrivateBackup` is a safety net for edits made outside an agent session. Backup attempts and results are tracked in local SQLite `_wip/private-github-sync/backup-state.sqlite`; check it if a run fails, then retry. Never claim a backup succeeded until the remote commit is verified.

The private backup includes project files, the database, and only artifact groups that have a Markdown or HTML transcript. Metadata archives and source-only evidence are packed into root-level ZIPs so a restore remains complete without extra folders. Keep the private catalog and transcript contents out of the public `agent-skills` repository. The private backup repository contains restore instructions. Avoid backing up temporary audio or `_wip` working files.

For ad hoc offline backups, use SQLite's backup API or the project's backup tool while preserving `transcripts/`; do not copy a live WAL database file alone.

After work, report the number saved, transcripts available, retrieval failures, and whether a repeat counter changed. Keep source-history coverage honest.

## Cross-environment intake

Use this workflow by default in all configured agents for specific user video requests. Web sessions must save directly through available authorized local tools, or send the durable handoff described in [handoff.md](handoff.md) to local ChatGPT Work/Codex. Sending this scoped handoff is explicitly authorized by Steve. Never claim an unavailable communication path worked.

# Hard Windows foreground rule

Never launch a visible Command Prompt, PowerShell, Windows Terminal, Python console, or any child process that can create or steal focus from a window. This applies to every Video Library action, including inspection, tests, status checks, database maintenance, backups, dashboard restarts, and transcription. Do not use foreground shell execution as a convenience for a read or verification.

Use a silent launcher only: `pythonw.exe` or a hidden Windows process created through WMI/CIM, with stdin/stdout/stderr redirected to noninteractive files or SQLite state. There is exactly one permitted spawn on this machine and it has two hops: `pythonw.exe` created through WMI/CIM, running `G:/__ai-projects/_agent-control/bin/silent-run.py`, which creates the real command with `CREATE_NO_WINDOW` and writes the result to JSON. `Invoke-CimMethod` may only ever create `pythonw.exe` - `cmd.exe`, `powershell.exe` and `python.exe` are console programs, and `Win32_Process::Create` cannot pass `CREATE_NO_WINDOW`, so creating one raises a window. Never `cmd /c` for output redirection or command chaining; the launcher already captures both streams. Use `CREATE_NO_WINDOW` alone for background workers, never `DETACHED_PROCESS` - it also suppresses the console but detaches the child from it, so a child whose output you capture silently produces nothing. Record progress and completion in SQLite, then have the dashboard read SQLite directly. If the available environment cannot perform an action silently, leave it queued with a SQLite explanation rather than launching it visibly.

# Local thumbnail cache

For YouTube videos, display the dashboard thumbnail from the local `_thumbnails/` cache, not a remote image URL. Capture the standard JPEG silently on first use and preserve it as `_thumbnails/YYYY-MM-DD--YOUTUBE_ID.jpg`; do not store thumbnail binary data in SQLite and do not replace an existing first-captured file. The cache is rebuildable and is not a transcript folder for backup mirroring.


## Unattended parallel worker

Use `_tools/run-parallel-batch.py BATCH_ID`, launched invisibly through pythonw with redirected standard handles and Windows no-window flags. Use existing SQLite batch IDs on continuation; retries never call intake again. Reconcile complete transcripts before acquisition. Serial audio downloads feed a bounded queue of three prepared files. The worker benchmarks one, two, and three large-v3 model processes, preserves a 2 GB desktop GPU reserve, measures scheduler lag and selects higher concurrency only for a material throughput improvement. CPU priority is reduced. These checks do not certify the user experience or word-perfect ASR. Failed parallel jobs receive one single-worker retry; failed outputs retain audio. Delete audio only after timed source, Markdown, HTML and searchable SQLite verification.

SQLite tables `processing_workers` and `transcription_benchmarks` record worker heartbeats, concurrency and measurements. `/api/processing` verifies PID and heartbeat, so waiting work is distinguishable from a stopped worker. Dashboard Fetch queues survive server restarts; link intake alone does not fetch media. Batch completion triggers the private backup task. Automated transcription is local machine inference; intake, scheduling, QA, export, search and backup do not require a chat agent. Content judgments and semantic categorization still need review.
