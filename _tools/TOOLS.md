# Master tool catalog

**Rule for agents: read this FIRST. If a tool for your task is already listed, USE IT — do not create a duplicate.** After adding any tool (downloaded, extracted, or agent-created), add one row here. Project-specific reusable tools live in project `_tools/`; shared tools stay at their actual shared locations.

Root: `G:\__ai-projects\_agent-tools\` · Put `bin\` on PATH · Approve-only tools need explicit human sign-off.

## Before you run anything: how to start it without a window

**Read this before invoking any tool on this list.** This is Steve's active desktop, and a console window
that flashes is a window on his screen — for reads and status checks exactly as for long jobs.

There is exactly one permitted spawn, and it has two hops: `pythonw.exe`, created through WMI/CIM,
running `G:\__ai-projects\_agent-control\bin\silent-run.py`, which creates the real command with
`CREATE_NO_WINDOW` and writes the exit code, duration, stdout and stderr into a JSON file.

    powershell -NoProfile -NonInteractive -WindowStyle Hidden -Command "Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine='\"C:\Users\noise\AppData\Local\Programs\Python\Python313\pythonw.exe\" \"G:\__ai-projects\_agent-control\bin\silent-run.py\" \"<result.json>\" -- <command> [args]'}"

- **`Invoke-CimMethod` may only ever create `pythonw.exe`.** `cmd.exe`, `powershell.exe`, `pwsh.exe`,
  `python.exe`, `node.exe` and `bash.exe` are console programs; `Win32_Process::Create` cannot pass
  `CREATE_NO_WINDOW`, so creating one raises a window. This has already happened from an agent that had
  read the rule.
- **Never `cmd /c <anything>`** — not to redirect output into a file, not to chain commands, not to reach
  a PowerShell script. `-- powershell -NoProfile -NonInteractive -File <script.ps1>` goes through the same
  launcher instead. The launcher already captures both streams.
- **Read the JSON result.** Do not re-run a command to see its output.
- **One exception:** a local web server surfaced in the browser, so Steve can see the result.

## Daily shims — `bin\` (on PATH)

| Shim | Tool | Typical agent use |
|------|------|-------------------|
| `es.exe` + `es-agent.cmd` + `Search-Everything.ps1` | Everything CLI 1.5.0.1423b (instance `AgentTools`) | Instant file/folder find across all disks |
| `pslist.exe` | PsList | List processes / detect orphans |
| `pskill.exe` | PsKill | Kill stuck worker by PID/name (careful) |
| `pssuspend.exe` | PsSuspend | Pause runaway CLI without killing |
| `psservice.exe` | PsService | Query/control services |
| `psinfo.exe`, `psloglist.exe`, `psping.exe` | PsTools extras | System info, event logs, network probes |
| `procmon.exe` | Process Monitor | Deep file/reg/network trace (GUI; filter PML) |
| `procexp.exe` | Process Explorer | Process/handle inspection (GUI) |
| `handle.exe` | Handle | Who has a file locked |
| `procdump.exe` | ProcDump | Hang dumps |
| `du.exe` | Disk Usage | Folder size inventory |
| `sigcheck.exe` | Sigcheck | Hash/signature verify downloads |
| `strings.exe` | Strings | Peek binaries |
| `junction.exe` | Junction | Reparse points |
| `tcpview.exe` / `tcpvcon.exe` | TCPView | Connectivity / sockets |
| `listdlls.exe`, `autoruns.exe`, `autorunsc.exe` | Sysinternals extras | DLLs, autostart inventory |
| `openedfilesview.exe` | OpenedFilesView (NirSoft) | Open handles (GUI/export) |
| `nircmdc.exe` | NirCmd | Scriptable Windows chores |

## Tool suites

| Folder | Tool | Notes |
|--------|------|-------|
| `sysinternals\` | Full Microsoft Sysinternals Suite | Complete set; `bin\` holds the daily subset |
| `everything\` | Voidtools Everything | `everything\app\` = 1.5.0.1423b (instance `AgentTools`); CLI at `everything\cli\es.exe`; start via `everything\Start-AgentEverything.ps1`. The Steve GUI install in Program Files is separate |
| `exiftool-13.59_64\` | ExifTool 13.59 | Image/video metadata |
| `nirsoft\` | Curated NirSoft utilities | From official nirsoft.net |
| `mailbox-mcp-server\` | Mailbox MCP server | Email access for agents; run via `_agent-control\bin\run-mailbox-mcp.ps1` |
| `qpdf\` | qpdf 12.3.2 (MSVC64) | PDF manipulation (was in old `__claude\tools\`) |
| `media-organizer\` | MediaOrganizer.ps1 suite | Media file organization tool (own README/config). Scan root `G:\media`; library zones are now `images`, `inbox`, `library`, `photos`, `reference` (`# by-device` and `_for-mom` keep their names) |
| `reference-image-library\` | Palette cards, colour extraction, named signature gradients, library intake | Python 3.13 + own `.venv` (Pillow). `bin\reference-image-library.ps1 inventory\|palette\|intake\|verify\|hashes`. Every path is an explicit argument, dry-run by default, `--apply` to execute; manifests carry relative asset paths so they work across drives. Library: `G:\media\images\reference-images\`. |
| `markdown-app\` | Markdown editor app | Browser markdown editor, current milestone v03.5.0 (was `tools\markdown-app`) |
| `ga4-blocker\` | GA4 Blocker Chrome extension v1.2 | Manifest V3 declarativeNetRequest blocker (was `tools\ga4-blocker`) |
| `auto-sized-timeline\` | AutoSizedTimeline v02.7.0 (DaVinci Resolve Lua) | Builds timeline sized to selected clips (was `tools\auto-sized-timeline`) |
| `resolve-project-health-scan\` | Project Health Scan v1.0.0 (DaVinci Resolve Python) | Missing Fusion fonts, Color/Fusion OFX, log plugin IDs, offline media. `install.ps1` then Workspace > Scripts > Project Health Scan. CLI: `py scan.py` with Resolve open. |
| `whisper-local\` | Isolated faster-whisper YouTube transcription runner | `prepare --detach`; CUDA/model `doctor` + `smoke-test`; detached `start --request`, durable `status --job`, resumable checkpoints, TXT/SRT/VTT/JSON/MD exports. Uses bundled yt-dlp/FFmpeg; local model and caches stay under the tool. |
| `approve-only\` | PsExec, NirCmdC | **Never run unsupervised** — also no PsShutdown/SDelete/PsPasswd/raw Sysmon without Steve |
| `_review-tools\` | Tool-review working files | 2026-09 review packet, logs, pids — not for daily use |
| Skill library lifecycle | `_tools/library.py` in this repository | Verified snapshots, releases, validation, managed content-hash sync, and safe Git updates. |
| Codex model advisor settings reader | `G:/__ai-projects/_agent-control/_tools/model-advisor/current-setting.ps1` | Read-only current-chat model/effort metadata plus last execution; used by the personal global Codex advisor instructions. No polling, model calls, switching, or conversation output. |

| Durable local Codex orchestration | `G:/__ai-projects/_agent-control/_tools/task-orchestrator/orchestrator.ps1` | Serial local jobs, explicit settings, observed execution, idempotency, cancellation/recovery and coordinator acceptance. Read sibling README; native chat remains default. |
| Video Library database maintenance | `G:/__ai-projects/__Personal.Projects/video-library/library.py optimize-db` | Python 3.13 stdlib. During idle maintenance: verified gzip SQLite backup, exact metadata gzip archives, compact metadata/export migration, integrity checks and VACUUM. Does not fetch videos or alter transcript/request history. See project README. |
| Video Library private GitHub backup | `G:/__ai-projects/__Personal.Projects/video-library/_tools/private-github-backup.py` | VACUUM, verified SQLite snapshot, transcript-bearing folders, private-visibility check, GitHub push and remote-head verification. Hourly/sign-in Windows task; run state in local SQLite. |
| Workspace database backup | `G:/__ai-projects/_agent-control/_tools/backup-databases.py` | Python 3.13 stdlib. Snapshots both workspace databases with `VACUUM INTO` (never a file copy) plus AGENTS.md and the launcher batch files to `G:/__ai-projects/_backups/databases/YYYY-MMDD--HHMM/`. Gzip, sha256, `PRAGMA quick_check` and row counts per run; 12 days kept; unrecognised folders reported, never deleted. Prints nothing. Register the schedule with `G:/__ai-projects/_agent-control/bin/register-database-backup.ps1` (three daily triggers, action is pythonw.exe so there is no console to flash); run state in `_backups/backup-state.sqlite`. |

## Scripts — `scripts\`

| Script | Use |
|--------|-----|
| `normalize_versions.py` | Audit/fix version-filename padding; dry-run then `--apply` (from old `__claude\scripts\`) |
| `srt_export.py` | Rebuild timing-accurate `.srt` from finished translation sheet (with the Translation Sheet project) |
| `audit_image_veils.js` | Static audit of image-veil/mask patterns in HTML/CSS (seams, mask-composite, // CSS comments, non-zero mask fades, bottom-anchor traps). Companion to `_agent-skills\skills\web-studio\references\image-veils.md`. Exit 1 on fail. |
| `audit_page.js` | One-command full-page static audit: CSS brace balance, // CSS comments, mask-composite (comment-aware), inline `<script>` parse (vm, no execution), div balance, video play contract (CONFIG.videoUrl / data-open-video / VideoStage.init / .is-playing), fd-page identity metas, document structure (DOCTYPE position incl. comment-before-doctype quirks trap, charset, title), plus delegation to audit_image_veils.js. `--json` output; folder = recursive. Exit 1 on fail. Validated: 10.11.2 index PASS (1 intentional warn: version-stamp comment above DOCTYPE = quirks mode); transcript page flags 3 warns (no DOCTYPE/charset/title — pre-existing since 10.9.3); negative tests fire. |
| `analyze_screenshot_rows.js` | Zero-dep Node PNG analyzer — measures ink bands (text rows) + vertical gaps in screenshots, to verify spacing claims from user captures (20260917) |
| `analyze_video_choppiness.js` | Zero-dep Node per-frame RMS delta analyzer — pair with ffmpeg frame extraction (`ffmpeg -i clip.mp4 /tmp/f/%04d.png`) to measure animation smoothness/choppiness from screen recordings (20260917) |
| `cdp_shot.js` | Zero-dep headless-Chrome screenshot + DOM metrics via CDP: `node cdp_shot.js <url> <out.png> [eval-js] [--width N] [--height N]`. Evaluates JS in the live page, dumps console errors, captures full-page PNG. Emulation is set BEFORE navigation (mobile:false + dpr 1) so media queries/cqi resolve at the emulated width. Requires Node >= 22. (20260917) |
| `clean_thumbnail.js` | ffmpeg-backed thumbnail artifact analyzer + cleaner: `analyze <image>` reports dark edge bands / vertical seam columns (luminance + per-channel steps, bottom-third zones); `clean <in> <out.jpg>` crops detected margins and rescales. Used in the Final Days thumbnail investigation (20260918); root cause there turned out to be CSS, not the image. Requires ffmpeg on PATH. |
| `shrink-video.sh` | Detached-safe video shrinker + quality check: `shrink-video.sh <in> <out> [crf=20] [preset=slow]` encodes libx264 CRF (High profile, yuv420p, `+faststart`), **copies the audio stream untouched**, and writes `<out>.status` / `.progress` / `.log` so it can run in the background while the agent polls with short reads (workspace §8). `--compare <original> <shrunk>` prints SSIM and PSNR — the quality it actually cost. Run it detached via `Start-Process`, never in the foreground. |

## EULA & PATH notes

- First run of Sysinternals tools may show a EULA GUI — accept once, or pass `-accepteula`.
- User PATH should include: `G:\__ai-projects\_agent-tools\bin` (update pending in Windows PATH).
- Everything 1.5 instance `AgentTools` must be running for `es.exe` shims; start it with `everything\Start-AgentEverything.ps1`.

## AI web-services registry

Browser-driven AI accounts (Claude, SuperGrok, Leonardo via Canva, Gemini, Meta AI, NightCafe, Labs FX, Flow, ChatGPT, DeepSeek), login identities, verified status, and routing guidance: see `_docs\AI-Tools-Registry.md` (archived 20260915 from the old `__claude\memory\` copy; browser-tool registry, not disk tools).

<!-- Agent: Codex | Model: GPT-6 | Thinking: not exposed | Date: 20260917 | Updated sync tool entry. -->


## Shared historical memory
<!-- Agent: Codex | Model: GPT-6 | Thinking: not exposed | Date: 20260917 -->
| Tool | Location | Use |
|------|----------|-----|
| Agent Memory | `G:\__ai-projects\agent-memory\bin\memory.cmd` | SQLite archive: search, native sync, project events, source-backed decisions, artifacts, localhost UI, verified backups, recent replica. User-authorized self-contained exception to the usual `_agent-tools` location. Read `G:\__ai-projects\agent-memory\AGENT-MEMORY.md`. |


## Design, research and specialist services



## Design / images
| Tool | URL | Status |
|------|-----|--------|
| Canva | https://www.canva.com | active |
| Leonardo.ai | https://leonardo.ai | active |
| NightCafe Creator | https://creator.nightcafe.studio/ | active |

## Research
| Tool | URL | Status |
|------|-----|--------|
| OpenBible cross-references | https://www.openbible.info/labs/cross-references/ | active |
| OpenBible topics | https://www.openbible.info/topics/ | active |
| EGW Writings | https://text.egwwritings.org/allCollection/en | active |
| White Estate | https://whiteestate.org/ | active |
| Amazing Facts guides | https://www.amazingfacts.org/study/bible-study-guides/ | active |

## Channels
| Tool | URL | Status |
|------|-----|--------|
| MOPT Ministry | https://www.youtube.com/@mopt_ministry | active |
| Heritage & Hope | https://www.youtube.com/@heritageandhope | active |
| H&H Sunday Law Updates | https://www.youtube.com/playlist?list=PLnymF_jIY3hnME1omB4ds2l3rx6xAAS4R | active |

## Unlocking Bible Prophecies translator PDFs

Procedure: private repo [getrdone/ubp-tools](https://github.com/getrdone/ubp-tools) — moved out of this repo in 3.1.0 and not part of default routing. Kit on the work laptop: `Documents/UBP-translator-pdf/`.

| Tool | Role | Status |
|------|------|--------|
| Windows PowerShell 5.1 | Host `build-translator-pdf.ps1` | active |
| System.Windows.Forms.RichTextBox | RTF notes → plain text | active |
| System.Drawing | Grayscale JPEG thumbs; invert dark cards | active |
| Microsoft Edge (headless `--print-to-pdf`) | HTML → letter PDF | active |
| Plain Vision | Library: Modular `_Sequence` + slides + notes | active |
| Xodo PDF | Pixel markup of travel-review PDFs | active |

<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 20260910 · Fixed dead pointer to the retired ubp-translator-pdf skill. -->

<!-- Agent: Codex | Model: GPT-6 | Thinking: not exposed | Date: 20260920 -->


## Registered project utility indexes

- Video Library: `G:/__ai-projects/__Personal.Projects/video-library/_tools/TOOLS.md` — local video intake, backup, handoff, and dashboard launcher.

- Personal Bible Studies: `G:/__ai-projects/__Personal.Projects/bible-studies--personal/_tools/TOOLS.md` — source-study workspace; no standalone utilities identified.

- ai-agent-control: `G:/__ai-projects/_agent-control/_tools/TOOLS.md` — local tools, invocation and reusable components.
- final-days-international: `G:/__ai-projects/__Final.Days.International/_tools/TOOLS.md` — local tools, invocation and reusable components.
- design-resources: `G:/__ai-projects/_resources/design-resources/_tools/TOOLS.md` — local tools, invocation and reusable components.
- transcript-skill-demo: `G:/__ai-projects/__Personal.Projects/transcript-skill-demo/_tools/TOOLS.md` — local tools, invocation and reusable components.
- scripture-journeys: `G:/__ai-projects/__Ministry.Projects/scripture-journeys/_tools/TOOLS.md` — local tools, invocation and reusable components.
- scripture-discovery-journey: `G:/__ai-projects/__Ministry.Projects/scripture-discovery-journey/_tools/TOOLS.md` — local tools, invocation and reusable components.
- agent-memory: `G:/__ai-projects/agent-memory/_tools/TOOLS.md` — local tools, invocation and reusable components.

## Authoritative lifecycle tools

- `_tools/library.py`: Python 3.11+, standard library. `backup`, `restore`, `seal`, `validate`, `sync`, `git-update`.
- `_agent-control/_tools/todos.py`: Python 3.13 stdlib. The single workspace database, `G:/__ai-projects/projects-and-todos.sqlite` — tasks (`global_todo`, `project_todo`, `subtask`, `archive`) and project memory (`project`, `project_lock`, `project_file`, `project_note`). Replaces the per-project `02-TASKS.md` files. Schema in `todos_schema.sql` plus numbered `NNNN_*.sql` migrations; `migrate_tasks.py` for the one-time import. `_agent-control/bin/open-tasks.ps1` reads it. Every database file in this workspace uses the `.sqlite` extension.
- `_tools/install.py`: Python 3.11+, installs current native startup instructions and the Grok hook with verified before-images.
- `_tools/sync.ps1` and `_tools/sync-hidden.vbs`: native silent Windows scheduler entrypoints.
- `_tools/test_library.py`: lifecycle regression checks; isolated fixtures.

- Bible Study Source Materials: `G:/__ai-projects/_resources/bible-studies--source-materials/_tools/TOOLS.md` — source registry/database tooling.

## Project utility inventory

The complete machine-readable inventory is [project-tools.json](project-tools.json). These are direct final locations; no legacy command aliases. Arguments vary by tool: consult the named command and local index before invoking.

| Project / purpose | Canonical path | Runtime / dependencies |
|---|---|---|
| ai-agent-control / Run GrokMemoryAudit | `G:/__ai-projects/_agent-control/_tools/Run-GrokMemoryAudit.ps1` | PowerShell |
| ai-agent-control / register project | `G:/__ai-projects/_agent-control/scripts/register-project.ps1` | PowerShell |
| ai-agent-control / sync project | `G:/__ai-projects/_agent-control/scripts/sync-project.ps1` | PowerShell |
| ai-agent-control / workspace status | `G:/__ai-projects/_agent-control/scripts/workspace-status.ps1` | PowerShell |
| ai-agent-control / install mcp servers | `G:/__ai-projects/_agent-control/bin/install-mcp-servers.sh` | Bash |
| ai-agent-control / migrate project files | `G:/__ai-projects/_agent-control/bin/migrate-project-files.ps1` | PowerShell |
| ai-agent-control / open tasks | `G:/__ai-projects/_agent-control/bin/open-tasks.ps1` | PowerShell |
| ai-agent-control / prune to archive | `G:/__ai-projects/_agent-control/bin/prune-to-archive.ps1` | PowerShell |
| ai-agent-control / run mailbox mcp | `G:/__ai-projects/_agent-control/bin/run-mailbox-mcp.ps1` | PowerShell |
| ai-agent-control / start browser use cdp | `G:/__ai-projects/_agent-control/bin/start-browser-use-cdp.ps1` | PowerShell |
| ai-agent-control / workspace doctor | `G:/__ai-projects/_agent-control/bin/workspace-doctor.ps1` | PowerShell |
| final-days-international / build transcript body | `G:/__ai-projects/__Final.Days.International/final-days-video-landing-page/_tools/build-transcript-body.js` | Node.js |
| final-days-international / srt to transcript | `G:/__ai-projects/__Final.Days.International/final-days-video-landing-page/_tools/srt_to_transcript.js` | Node.js |
| final-days-international / init local d1 | `G:/__ai-projects/__Final.Days.International/final-days-video-landing-page/scripts/init-local-d1.ps1` | PowerShell |
| final-days-international / refresh local sqlite | `G:/__ai-projects/__Final.Days.International/final-days-video-landing-page/scripts/refresh-local-sqlite.ps1` | PowerShell |
| final-days-international / refresh local sqlite | `G:/__ai-projects/__Final.Days.International/final-days-video-landing-page/scripts/refresh_local_sqlite.py` | Python 3 |
| bible-study-source-materials / build source db | `G:/__ai-projects/_resources/bible-studies--source-materials/scripts/build_source_db.py` | Python 3; requirements.txt |
| bible-study-source-materials / query sources | `G:/__ai-projects/_resources/bible-studies--source-materials/scripts/query_sources.py` | Python 3; requirements.txt |
| bible-study-source-materials / validate sources | `G:/__ai-projects/_resources/bible-studies--source-materials/scripts/validate_sources.py` | Python 3; requirements.txt |
| scripture-discovery-journey / source vault inventory | `G:/__ai-projects/__Ministry.Projects/scripture-discovery-journey/scripts/source_vault_inventory.py` | Python 3 |
| agent-memory / install schedule | `G:/__ai-projects/agent-memory/bin/install-schedule.ps1` | PowerShell |
| agent-memory / memory | `G:/__ai-projects/agent-memory/bin/memory.cmd` | Windows cmd |
| agent-memory / memory | `G:/__ai-projects/agent-memory/bin/memory.ps1` | PowerShell |
| agent-memory / memory | `G:/__ai-projects/agent-memory/bin/memory.py` | Python 3 |
| agent-memory / nightly | `G:/__ai-projects/agent-memory/bin/nightly.ps1` | PowerShell |
| agent-memory / open memory | `G:/__ai-projects/agent-memory/bin/open-memory.ps1` | PowerShell |

- `_tools/check_links.py`: Python 3, standard library (optional PyYAML elsewhere); checks current local references, `--all-versions` for explicit history, `--load-map` for orphaned CDSJ references. Preserves the original link-audit capability with per-skill release resolution.
- `_tools/install-schedule.ps1 -BackupDirectory PATH`: PowerShell ScheduledTasks; backs up and repoints the existing Windows task, preserving triggers and removing its execution timeout.

## Shared job queue utilities

The existing queue remains at `G:/__ai-projects/_agent-control/jobs`; runtime job state is not a skill release or legacy fallback.

- Complete Job: `pwsh -File G:/__ai-projects/_agent-control/jobs/bin/Complete-Job.ps1` — PowerShell 7; Git/Grok/Codex for selected lane. Shared job queue lifecycle; inspect parameters and jobs/README.md.
- Invoke CodexJob: `pwsh -File G:/__ai-projects/_agent-control/jobs/bin/Invoke-CodexJob.ps1` — PowerShell 7; Git/Grok/Codex for selected lane. Shared job queue lifecycle; inspect parameters and jobs/README.md.
- Invoke GrokJob: `pwsh -File G:/__ai-projects/_agent-control/jobs/bin/Invoke-GrokJob.ps1` — PowerShell 7; Git/Grok/Codex for selected lane. Shared job queue lifecycle; inspect parameters and jobs/README.md.
- New Job: `pwsh -File G:/__ai-projects/_agent-control/jobs/bin/New-Job.ps1` — PowerShell 7; Git/Grok/Codex for selected lane. Shared job queue lifecycle; inspect parameters and jobs/README.md.
- Start JobLane: `pwsh -File G:/__ai-projects/_agent-control/jobs/bin/Start-JobLane.ps1` — PowerShell 7; Git/Grok/Codex for selected lane. Shared job queue lifecycle; inspect parameters and jobs/README.md.
- Start JobWatcher: `pwsh -File G:/__ai-projects/_agent-control/jobs/bin/Start-JobWatcher.ps1` — PowerShell 7; Git/Grok/Codex for selected lane. Shared job queue lifecycle; inspect parameters and jobs/README.md.
- Test ApproveDelete: `pwsh -File G:/__ai-projects/_agent-control/jobs/bin/Test-ApproveDelete.ps1` — PowerShell 7; Git/Grok/Codex for selected lane. Shared job queue lifecycle; inspect parameters and jobs/README.md.
- Watch Jobs: `pwsh -File G:/__ai-projects/_agent-control/jobs/bin/Watch-Jobs.ps1` — PowerShell 7; Git/Grok/Codex for selected lane. Shared job queue lifecycle; inspect parameters and jobs/README.md.
