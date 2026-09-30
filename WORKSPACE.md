# Workspace conventions (all agents, all skills)

**Always apply.** This file is part of the agent-skills contract, not a single skill.
Read with `CATALOG.md`. Skills follow these conventions; specialist recommendations cannot override the user or accepted project requirements.

Agents covered: **Grok, Claude, Codex, Freebuff, Cursor, Gemini**, and any other local agent.

> **This file is the ONLY statement of file naming, file I/O, and continuity in this repository.**
> Skills and references point here. They do not restate the rules. If you find a second copy of
> any rule below anywhere in the repo, that copy is a defect — delete it and link here instead.

---

## 0. Authoritative workflow and working locations

This repository is the complete source of truth for managed skills. Installed copies are generated distributions. Never load a legacy skill, shim, alias, archive or upstream instruction file to fill a gap. Integrate required knowledge here first. References within the new library are direct ownership links.

For coding use `skills/coding-workflow/SKILL.md`. For web work use `skills/web-studio/SKILL.md`. Current user instructions and accepted project requirements take precedence over recommendations and reference examples. Modular source, dependencies, Motion/Framer Motion, GSAP, Remotion and Lottie are allowed when appropriate. Never produce a self-contained or offline build unless Steve asks for one in that run; modular source with dependencies is the default. Dates have one form everywhere: four-digit year, zero-padded two-digit month, zero-padded two-digit day, written 2026-0930.

Temporary plans, captures, diagnostics, experiments and drafts go in `_wip/<task>/`, never the project root or durable planning folders. Reusable project utilities go in `_tools/`; shared tools retain one shared home. Skill-bound scripts stay in their release. Read the master `_tools/TOOLS.md` in this library before creating a utility. Project `_tools/TOOLS.md` lists local tools and links directly to the master. Do not copy the master into each project. Accepted plans remain in established durable documentation.

Work in cohesive verifiable chunks: outcome, affected area, check, evidence, status, next action. No elapsed-time work quota, inactivity deadline or automatic kill. Continue authorized work without repeated approval gates; no automatic job retry or model switching. Explicit user stop requests and actual failures remain actionable.

## 0b. Source provenance for every new or materially updated skill

Every skill created, combined, or materially revised must record the substantive videos, research, articles, datasets, source skills, and other references that shaped it. Maintain the library-wide per-skill entry in [`_docs/skill-source-register.md`](_docs/skill-source-register.md) and keep `_docs/source-provenance.json` in sync where applicable.

For each video, capture its exact title, creator/channel, canonical URL, and the concepts it contributed. For research, capture the exact title, author/publisher, direct URL, and the claim or method supported. When a skill combines prior skills or source material, preserve the lineage and list inherited sources under the resulting skill too. Never invent missing citations: mark them `needs-identification` and retain useful identifying clues until verified. Before sealing a new release, check that its sources are represented in the register.

## 1. Brain vs work

| Layer | Location | Role |
|-------|----------|------|
| **Brain (skills)** | `G:\__ai-projects\_agent-skills\skills\<name>\` | Procedures, SPECs, matrices — shared, synced. Archives live in `G:\__ai-projects\_zzz-repo-archive\<YYYY-MMDD>\` only. |
| **Work (artifacts)** | The folder the user opened / named as the project | Transcripts, titles, pages, assets — **one shared root** |

Do **not** create a parallel per-agent project tree (`/grok`, `/claude`, …) for the same topic.
Do **not** fork skill bodies into the work folder.

---

## 2. One shared work folder

All agents share the user-chosen project. Put drafts, temporary plans, experiments and intermediate artifacts in `_wip/<task>/`. Put reusable project tools in `_tools/`. Keep actual source, tests, assets, accepted documentation and deliverables in their established locations.

```text
work-root/
  AGENTS.md                 # optional local pointer to this contract
  01-NOW.md                 # session pickup (Now / Blocked)
  03-MEMORY.md              # durable locks and settled decisions
  project-brief.md          # durable decisions + machine state
  <stem>.txt                # source
  <stem>.titles.md          # progressive stem (see §3)
  <stem>.archive.md         # retired run history
```

### 2b. New topic project — agent creates the shell

When the user starts a **new** named topic and no project folder exists:

1. Create **one** kebab-case folder where they asked (or under the current work root).
2. **If a path already exists, do not wipe or rebuild it** — create only what is missing.
3. Seed this **same** structure every time:

```text
<topic-slug>/
  AGENTS.md                 # short pointer to agent-skills + this file
  01-NOW.md                 # Now / Blocked
  03-MEMORY.md              # durable locks and settled decisions
  project-brief.md          # one living brief (YAML) — durable + machine state
  _wip/                    # temporary plans and task intermediates
  _tools/                  # reusable project utilities and local index
  mood/                     # finished inspiration / generated art
  prompts/                  # artwork prompt packs
  references/               # project-specific refs
    dynamic-symmetry/       # project composition notes, if needed
  sources/intake/           # user may dump files here — no forms required
  deliverables/             # shippable page, exports, finals
    assets/                 # finished art named to match the prompts file (e.g. topic_p01.webp)
```

**Creative-friendly intake:** the user may drop files into `mood/` or `sources/intake/` with **zero paperwork**.
Formal `registry.yaml` is only for the shared source vault — not for every mood PNG.

**Dynamic Symmetry method (canonical skill):** `skills/dynamic-symmetry/`.  
**Shared grid pack (never duplicated into a project):** `repo:resources/dynamic-symmetry-grids/`. Project composition notes may cite selected grids directly within this library.

---

## 3. File naming (required — single source of truth)

Two kinds of artifact. Pick the kind first; the naming follows.

| Kind | Test | Naming |
|------|------|--------|
| **Deliberation artifact** | The user will *choose between* things in it — titles, descriptions, visual directions, idea passes | **Progressive stem**, one file, append-only (§3a) |
| **Deterministic deliverable** | Running the same spec twice gives the same file — cleaned transcript, built page, prompts pack, export | **Canonical on first write** (§3b) |

### 3a. Deliberation artifacts — progressive stems

One file per stage. The stage's name grows; the stem never changes.

```text
<stem>.titles.md
<stem>.titles+descriptions.md
<stem>.titles+descriptions+visuals.md
<stem>.archive.md              # retired runs, all stages
```

- **The longest compound stem present is authoritative.** When the next compound file is created, the
  earlier one becomes read-only and gets a `SUPERSEDED BY:` line under its title.
- A compound file's `SELECTED` block opens by quoting the upstream `SELECTED` verbatim under
  `INHERITED FROM: <file>`, so drift between stages is visible without opening both.
- Agents **do not** create `<stem>.titles_grok_v3.md` for normal work. They append a Run (§3c).
- `_vN` is for **rare full snapshots only** — the user asked to freeze a moment, or a destructive
  rewrite is unavoidable. It is never the everyday path.
- `+` is safe in NTFS filenames and PowerShell globs. Never link these files by raw URL.

#### Required file shape

Every progressive stem file starts with this block, written by the agent that creates the file:

```markdown
# <stem> — <stage>

<!-- HOW THIS FILE WORKS
  1. SELECTED below is yours. Mark winners with a trailing ~ inside a Run, then say "promote" —
     an agent copies the marked lines into SELECTED.
  2. Agents never edit inside the SELECTED fence. They only append a new Run at the bottom.
  3. The newest Run is the newest, not the best. SELECTED is what later stages read.
  4. A Run that corrects an earlier one carries SUPERSEDES: <that run's timestamp>.
     The agent writes that line, never you.
  5. Answer is at the top. Latest attempt is at the bottom. Nothing important is in the middle.
-->

<!-- SELECTED:BEGIN -->
## SELECTED (user-owned)
- (none yet)
<!-- SELECTED:END -->

## RUN LOG — newest at the bottom
```

### 3b. Deterministic deliverables — canonical on first write

Write the plain name immediately: `<stem>.md`, `index.html`, `prompts/artwork-prompts.md`.
There is nothing to choose between, so there is nothing to promote.

- Re-running the same spec **overwrites** the canonical file.
- Keeping a prior copy for comparison uses `_vN`: `index_v2.html`. Nothing else.
- Source inputs the user supplied (`<stem>.txt`, files in `mood/` and `sources/intake/`) are **never** modified.
- Artwork prompt IDs and generated asset filenames use the same topic-prefixed sequence: `<topic>_p01`, `<topic>_p02`, etc. Use one lowercase topic stem per pack (kebab-case for multiple words), retain the number across revisions, and use the chosen image extension. Example: `antichrist_p01.webp`.
- **Exception — competing proposals.** When two agents are deliberately asked for rival versions of the
  same deliverable (a design bake-off), those are deliberation artifacts for the duration:
  `index_<agent>.html`, promoted to `index.html` when the user picks one. This is the *only*
  surviving use of the agent suffix, and it requires the user to have asked for a bake-off.

### 3c. Run log entries (append-only)

A Run is appended to the bottom of a progressive stem file. Fixed grammar so humans scan it and
scripts can find it:

```markdown
## Run — 20260910 09:15 PT — claude/claude-opus-5 — Thinking: not exposed
SUPERSEDES: 20260909 16:40 PT        <!-- only when this run retracts an earlier one -->
### Reasoning
### Candidates
1. …
```

- Header line must match: `^## Run — \d{4}-\d{2}-\d{2} \d{2}:\d{2} PT — [^—]+ — Thinking: .+$`
- `SUPERSEDES:` is written by the **agent** when its run corrects, retracts, or replaces an earlier
  run — a bad citation, a misspelling, a withdrawn set. The user never types it. A superseded run stays
  in the file; it is marked, not deleted.
- Never edit inside another agent's Run. Append after it.
- **Retention:** keep the newest 5 runs. Older runs move to `<stem>.archive.md` in one file operation
  (§4 rule 3) — one archive per stem, never one file per run. Soft cap 120 KB per stem file.

### 3d. Human-readable instruction folders

Prefer **`_docs/`** (leading underscore, kebab-case inside) for instruction PDFs, usage notes, and organization-only material. Do not use `docs/`. The underscore sorts the folder first and keeps it out of asset-pack names.

### 3e. What stays unsuffixed and unversioned

- Navigation and state: `NOW.md`, `project-brief.md`, `AGENTS.md`
- User drops: anything the human puts in `mood/` or `sources/intake/` under their own names
- Generated binary assets once saved to the agreed filenames under `deliverables/assets/`

### 3f. Forbidden

- Per-agent folder trees for the same topic
- Bare version piles: `final.html`, `latest.html`, `index_v2.html` as a working file
- Agent suffixes on normal work (they survive only for an explicitly requested bake-off, §3b)
- A second canonical name for the same artifact
- Copying a whole `versions/<n>/` tree for a small CSS, JS, or copy fix

### 3g. Project version folders (Steve, 20260920)

When a project keeps working copies under `versions/<current>/` (named in that project's `01-NOW.md`):

- Small CSS, JS, and copy fixes **edit that folder in place**. Do not copy the tree to `versions/<n+1>/`.
- A new `versions/<n>/` folder is only for a schema or function change, a visual pass the user asked to keep separate, or a freeze they asked for.
- Do not create files or folders just to create them.

---

## 4. File I/O (required — applies to every request, every file, every agent)

Cost comes from **method**, not file size. Appending to a 2 MB file costs the same as appending to an
empty one — unless you read it first. These four rules are not optimisations; treat them as the contract.

| # | Rule | Do this | Not this |
|---|------|---------|----------|
| 1 | **Append with the shell** | `Add-Content -Path f.md -Value $block` · `cat >> f.md <<'EOF'` | Read whole file → edit in context → write whole file back |
| 2 | **Read by range** | `Select-String -Pattern 'SELECTED:BEGIN' -Context 0,40` · `sed -n '1,40p'` · locate with `rg -n`, then slice | Loading 120 KB to read a 40-line block |
| 3 | **Move data with the OS** | `Get-Content -Tail`/`Select-Object` piped to append, then truncate | Re-typing moved content through the model |
| 4 | **Edit in place by pattern** | `sed -i`, or a short script that reads and rewrites the file itself | Reproducing file contents from earlier tool output — that output may be truncated, which is a correctness bug, not just a cost one |

**Reading a progressive stem file:** `head` for the SELECTED fence, `tail` for the newest Run. Never
the middle unless searching for something specific.

**Harness note:** some agent harnesses require a file read before their edit tool will write (Claude
Code's `Edit` is one). Inside those, rule 1 means *use the shell for appends*, not the edit tool.

---

## 5. Agent identification (NON-NEGOTIABLE — all agents, all tasks)

Multiple agents read and write the **same** folders. The human must always be able to tell **who**
produced a file, **which model**, and **at what thinking level**, without opening chat history.

### Identity fields

- **Agent** — product/agent name: `grok`, `claude`, `codex`, `freebuff`, `ChatGPT`.
- **Model** — exact model identifier the runtime exposes: `Grok 4.6`, `GPT-5`, `claude-opus-5`.
- **Thinking** — exact reasoning-effort label the runtime exposes.
- **Date / What changed** — files use the date written; commits use a concise description.

**Never guess a thinking level.** If the runtime does not expose one, write `Thinking: not exposed`.
If it exposes a default with no name, write the exact exposed label. Never omit the field.

### Stamps

- **In-file stamp required** on every file you create or materially edit — agent, model, thinking, date.
  Markdown `**Agent:** … · **Model:** … · **Thinking:** … · **Date:** …`, HTML comment, code header,
  or YAML fields. **Never write only the agent name.**
- **Append, don't overwrite.** A different agent/model/thinking level adds a new stamp line. The same
  agent/model/thinking touching the file again just updates that line's date.
- Canonical files carry the stamp too — author or last material updater.

### Commits

Every commit to any repo touched by an agent uses this subject:

`Agent: <agent> | Model: <model> | Thinking: <level-or-not-exposed> | What changed: <concise description>`

Applies to all agents and sub-agents, including delegated passes. If one agent commits work authored
by another, identify the committing agent and note co-authorship in `What changed`.

### Not sufficient

- Chat-only signatures with no disk stamp
- A commit naming the agent but omitting model or thinking level

### Lean chat — always on

**`lean-output` is the default chat voice for every agent, every session, and it does not need to be invoked.** It is not an opt-in style. Treat its rules as the baseline unless the user asks for something else explicitly.

Brief status only — what / path / blocked. **No** code, diffs, patches, or full dumps in chat. Those live in files. No preamble, no closer, no restating the question, no summary of what you are about to do.

Length is a budget, not a courtesy. Deliverables stay whole — pages, documents, slides, and code files are never trimmed to make the chat shorter. Only the chat is compressed.

The one thing that overrides this: if the user asks a direct question, answer it in the fewest lines that fully answer it, and stop.

---

## 6. Continuity - the numbered files that exist, plus one database

There is one queue and it is not a markdown file. Open work lives in
`todos.db` at the workspace root, read with `_agent-control\_tools\todos.py`
or `_agent-control\bin\open-tasks.ps1`. Everything else is a numbered file,
created when that layer has something to say. Do **not** scaffold empty
`03-MEMORY.md` / `04-ACTIVITY.md` / `05-ARCHIVE.md` just to have the set. Never
use the old names (`NOW.md`, `MEMORY.md`, `AGENT-ACTIVITY.md`,
`MEMORY-ARCHIVE.md`, `02-TASKS.md`).

| File | Scope | Read | Written by |
|------|-------|------|-----------|
| `01-NOW.md` | this session | **every session** | agent + human |
| `03-MEMORY.md` | the whole project | before changing settled work | mostly human |
| `04-ACTIVITY.md` | opt-in journal | when a run asks for history | that run only |
| `05-ARCHIVE.md` | pruned locks and closed tasks | only when asked | nobody directly |
| `todos.db` | every open task, every project | before planning anything | `todos.py` |

`AGENTS.md` stays **unnumbered** - that exact name is what the tools look for.
Numbered files are this workspace's contract; unnumbered files are tool entry
points.

`project-brief.md` is a sixth file belonging to **one deliverable**, not the
project. See §6d.

There are no other state files. Not `NOW.md`, not `MEMORY.md`, not
`02-TASKS.md`, not `TOPIC-BOARD.md`, `START-HERE.md`, `PROJECT-STATUS.md`,
`STATUS.md`, `CURRENT.md`, `ACTIVE-WORK.md`, or a per-agent board. If you find
one, it is a leftover: fold it into the file that owns its content and delete
it.

### 6a. What each one is for

**`01-NOW.md` - what is in flight.** Now and Blocked. Not a queue - the queue
is `todos.db`, and duplicating it here is the most likely way this drifts.
Never a `## Next` heading. Never task checkboxes. `workspace-doctor.ps1` fails
if either returns. Read first, every session; update before ending substantial
work. Keep under ~3 KB.

**`todos.db` - the queue.** Open work that survives past this session, for
every project, in one database. Add, check, hold, search and close it with
`_agent-control\_tools\todos.py`; never hand-write SQL and never write a
markdown task list. A closed todo is archived automatically with its subtask
rollup.

**`03-MEMORY.md` - durable locks.** The only file in the system that can hold
a **no**. Git records what changed, not what is forbidden. The artifacts hold
the locked copy but not the fact that it is locked - an agent reading a page
sees copy it could improve, and improving it is the failure. Agent chat memory
does not cross agents and never overrides repo files.

So this holds standing constraints and settled decisions: locked copy, locked
visual direction, closed choices, "do not reopen X", "Y is on hold". Read it
before touching anything that looks already decided. **A thing being improvable
is not permission to change it.**

**`04-ACTIVITY.md` - opt-in, not a default.** Written only when the current
request asks for history, shaped by
`_agent-control\templates\AGENT-ACTIVITY-ENTRY.md`. Append only; never
rewrite an earlier entry. Provenance does **not** go here by default - it goes
in the commit trailer as `Agent`, `Model`, `Thinking`, `Date`, so `git log`
answers who did what and at what depth without any working file growing. A
later agent may offer a higher-thinking-level re-evaluation of shallow work in
one line; that is an offer, never a requirement, and never a reason to pause.

**`05-ARCHIVE.md` - a destination, not a source.** Its only job is letting
`03-MEMORY.md` stay short. Content arrives **only** by being pruned out of
`03-MEMORY.md`, and only when a run asks. Never write to it directly, never
read it unless asked.

### 6b. The task commands (there is no line format to hand-write)

```powershell
G:\__ai-projects\_agent-control\_tools\todos.py add global "Retitle the queue filter pills"
G:\__ai-projects\_agent-control\_tools\todos.py add project video-library "Add transcript resync"
G:\__ai-projects\_agent-control\_tools\todos.py list
G:\__ai-projects\_agent-control\_tools\todos.py search "dashboard"
G:\__ai-projects\_agent-control\_tools\todos.py show 42
G:\__ai-projects\_agent-control\_tools\todos.py check 42
G:\__ai-projects\_agent-control\_tools\todos.py hold 42 "waiting on Steve"
G:\__ai-projects\_agent-control\_tools\todos.py resume 42
G:\__ai-projects\_agent-control\_tools\todos.py supersede 42 "merged into 17"
G:\__ai-projects\_agent-control\_tools\todos.py archive
```

Titles are written for people in ordinary language, not agent shorthand. A
task is recorded only when Steve asked for one, or when the change is a major
addition to shipped code or a deliberate change of direction. A bug found and
fixed in the same change is not a task.

### 6c. Task lifecycle (the workflow - follow it exactly)

A task leaves the queue by exactly one of four routes. It is never in two
places at once.

| What happened | Where it goes | What is left in the queue |
|---|---|---|
| **Picked up** - you are working it now | name it in `01-NOW.md` under Now | the todo stays open |
| **Finished** | `todos.py check <id>` | archived with its subtask rollup |
| **Became a decision** - it settled into a standing constraint, a lock, or a "we are not doing this" | write it in `03-MEMORY.md`, then close the todo | nothing |
| **Abandoned** | `todos.py supersede <id> "<reason>"` | nothing |

The third route is the one that keeps the queue honest. "Decide whether to
gate the theme switcher" is a task; once decided, "theme switcher stays hidden
until ads are wired" is a lock. If the decision stays in the queue, agents keep
re-opening a settled question - the exact failure `03-MEMORY.md` exists to
prevent.
### 6d. `project-brief.md` — one deliverable, not the project

The structured production record for a **single** Scripture Journey deliverable: status, audience, core
question, chosen title, source pins, stage, open gates. YAML, agent-maintained, changes as the work
moves through stages. A project with six episodes has one `03-MEMORY.md` and up to six briefs.

**Scope test:** would this still be true for the next episode? Yes → `03-MEMORY.md`. Only this one →
the brief.

**The brief cites; it never copies.** Project-wide locks stay in `03-MEMORY.md` and the brief points at
them — `locked_decisions: [see 03-MEMORY.md § Locked visual]`, not the palette pasted in. A value in two
files goes stale in one of them silently.

**Not every project needs a brief.** It appears when a Scripture Journey deliverable starts moving
through stages. An ops or landing-page project runs on `01-NOW` + `02-TASKS` + `03-MEMORY` alone. Do not
scaffold an empty forty-field YAML nobody will fill in.

### 6e. The test that keeps `03-MEMORY.md` lean

**Could an agent discover this by reading the code?** If yes, it does not belong there — it belongs in
the project README, or nowhere. `03-MEMORY.md` earns its length only with what cannot be inferred.

Target under ~8 KB. Past that, prune the derivable material to `05-ARCHIVE.md` in one file operation, when a run asks for it,
(§4 rule 3) — never by re-typing it through the model.

Cross-project preferences — how the user likes to be worked with in general — are **not** project
memory. They belong in the machine-wide agent rules. A working-style section copied into several project
files drifts the first time it is refined in one of them.

### 6f. Finding open work across every project

There is **no** aggregated task file. A roll-up would be a second copy of every task and would be wrong
the moment a project file changed. Aggregate on demand instead — the answer is always live:

```powershell
G:\__ai-projects\_agent-control\bin\open-tasks.ps1              # every project
G:\__ai-projects\_agent-control\bin\open-tasks.ps1 -Project final-days
G:\__ai-projects\_agent-control\bin\open-tasks.ps1 -Owner @grok
```

It reads `todos.db` and prints every open item with its project and id. When the user asks *"what is open"*, *"show me all my
to-dos"*, or anything of that shape across projects — **run that, do not guess and do not hand-collect.**

Without the script, the same thing with the CLI:

```powershell
G:\__ai-projects\_agent-control\_tools\todos.py list
```

### 6g. Resume rule

Read `01-NOW.md`. Read the `todos.db` queue. Read `03-MEMORY.md` before changing anything already settled. For a
staged Scripture Journey deliverable, read its `project-brief.md`: if `status` is set, resume that stage
and load only its lanes. With no brief, treat the work as intake/discovery — never assume a prior
approval.

### 6h. Drift detection

```powershell
G:\__ai-projects\_agent-control\bin\workspace-doctor.ps1
```

Run after changing any numbered file. Exit 1 means the contract is broken — fix it before you stop.
It fails if `## Next` or task checkboxes appear in `01-NOW.md`, if both old and new names exist, if a
retired name returns, or if the machine-wide template regresses. Conventions hold because this notices.

## 7. Local `AGENTS.md` in a work folder

A consumer folder may keep a short `AGENTS.md` that points at `G:\__ai-projects\_agent-skills` and this
file, and states that all agents share the folder. It must **not** restate the rules above.

---

## 8. Skills still route via CATALOG

1. `CATALOG.md` → matching skill
2. The skill's procedure for *how*
3. **This file** for *where* files go, *how* they are named, and *how* they are read and written

<!-- Agent: goBot · Date: 20260909 · TOPIC-BOARD retired; NOW.md is session pickup. -->
<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 20260910 · Single-sourced the naming contract; progressive stems + run-log journal; added §4 file I/O rules. -->
<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 20260910 · §6 restored MEMORY.md as a first-class file; numbered five-file model in order of need, task queue + lifecycle, the derivability test, brief-cites-never-copies, and on-demand cross-project task discovery. -->
<!-- Agent: grok · Model: Grok 4.6 · Thinking: not exposed · Date: 20260910 · ACTIVE-WORK.md is a leftover state file; doctor FAILs pickup pointers at NOW.md/MEMORY.md. -->
<!-- Agent: grok · Model: Grok 4.5 · Date: 20260913 · §3d: human-readable instruction folders are _docs/, not docs/. -->

<!-- Agent: Codex | Model: GPT-6 | Thinking: not exposed | Date: 20260920 -->
<!-- Agent: grok · Model: Grok 4.6 · Date: 20260920 · §3g: do not copy a versions tree for a small CSS/JS/copy fix. -->

