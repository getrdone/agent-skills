# Workspace conventions (all agents, all skills)

**Always apply.** This file is part of the agent-skills contract, not a single skill.
Read with `CATALOG.md`. Every skill inherits these rules unless a skill explicitly tightens them.

Agents covered: **Grok, Claude, Codex, Freebuff, Cursor, Gemini**, and any other local agent.

> **This file is the ONLY statement of file naming, file I/O, and continuity in this repository.**
> Skills and references point here. They do not restate the rules. If you find a second copy of
> any rule below anywhere in the repo, that copy is a defect — delete it and link here instead.

---

## 1. Brain vs work

| Layer | Location | Role |
|-------|----------|------|
| **Brain (skills)** | `G:\__ai-projects\_agent-skills\skills\<name>\` | Procedures, SPECs, matrices — shared, synced. Archives in `packages\` only. |
| **Work (artifacts)** | The folder the user opened / named as the project | Transcripts, titles, pages, assets — **one shared root** |

Do **not** create a parallel per-agent project tree (`/grok`, `/claude`, …) for the same topic.
Do **not** fork skill bodies into the work folder.

---

## 2. One shared work folder

All agents write into the **same** user-chosen directory. When a topic outgrows a flat list
(~6+ artifact types), use **one topic/episode subfolder** — still shared by every agent, never one folder per agent.

```text
work-root/
  AGENTS.md                 # optional local pointer to this contract
  01-NOW.md                 # session pickup (Now / Blocked)
  02-TASKS.md               # the queue
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
  02-TASKS.md               # open work that outlives a session
  03-MEMORY.md              # durable locks and settled decisions
  project-brief.md          # one living brief (YAML) — durable + machine state
  planning/                 # optional long plans
  mood/                     # finished inspiration / generated art
  prompts/                  # artwork prompt packs
  references/               # project-specific refs
    dynamic-symmetry/       # optional: README pointing at design-resources pack
  sources/intake/           # user may dump files here — no forms required
  deliverables/             # shippable page, exports, finals
    assets/                 # finished art named to match the prompts file (p01-….png)
```

**Creative-friendly intake:** the user may drop files into `mood/` or `sources/intake/` with **zero paperwork**.
Formal `registry.yaml` is only for the shared source vault — not for every mood PNG.

**Dynamic Symmetry method (canonical skill):** `skills/dynamic-symmetry/`.  
**Shared grid pack (never duplicated into a project):** `G:\__ai-projects\_resources\design-resources\dynamic-symmetry-grids\` (legacy `F:\__ai-projects\design-resources\…`).  
Projects keep a short pointer under `references/dynamic-symmetry/README.md`.

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
- **Exception — competing proposals.** When two agents are deliberately asked for rival versions of the
  same deliverable (a design bake-off), those are deliberation artifacts for the duration:
  `index_<agent>.html`, promoted to `index.html` when the user picks one. This is the *only*
  surviving use of the agent suffix, and it requires the user to have asked for a bake-off.

### 3c. Run log entries (append-only)

A Run is appended to the bottom of a progressive stem file. Fixed grammar so humans scan it and
scripts can find it:

```markdown
## Run — 2026-09-10 09:15 PT — claude/claude-opus-5 — Thinking: not exposed
SUPERSEDES: 2026-09-09 16:40 PT        <!-- only when this run retracts an earlier one -->
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

### Lean chat

Brief status only — what / path / blocked. **No** code, diffs, patches, or full dumps in chat. Those live in files.

---

## 6. Continuity — five numbered files, created when that layer has content

Filenames are numbered in **order of need**. A directory listing tells you the reading order without
opening anything. Create a numbered file when that layer has something to say. Do **not** scaffold
empty `03-MEMORY.md` / `04-ACTIVITY.md` / `05-ARCHIVE.md` just to have all five. Never use the old
names (`NOW.md`, `MEMORY.md`, `AGENT-ACTIVITY.md`, `MEMORY-ARCHIVE.md`).

| File | Scope | Read | Written by |
|------|-------|------|-----------|
| `01-NOW.md` | this session | **every session** | agent + human |
| `02-TASKS.md` | open work that outlives a session | **every session** | agent + human |
| `03-MEMORY.md` | the whole project | before changing settled work | mostly human |
| `04-ACTIVITY.md` | one dated entry per material change | rarely | agent, append-only |
| `05-ARCHIVE.md` | pruned locks and closed tasks | only when asked | nobody directly |

`AGENTS.md` and `CLAUDE.md` stay **unnumbered** — those exact names are what Codex and Claude Code look
for. Numbered files are this workspace's contract; unnumbered files are tool entry points.

`project-brief.md` is a sixth file belonging to **one deliverable**, not the project. See §6d.

There are no other state files. Not `NOW.md`, not `MEMORY.md`, not `TOPIC-BOARD.md`, `START-HERE.md`,
`PROJECT-STATUS.md`, `STATUS.md`, `CURRENT.md`, `ACTIVE-WORK.md`, or a per-agent board. If you find one, it is a leftover:
fold it into the numbered file that owns its content and delete it.

### 6a. What each one is for

**`01-NOW.md` — what is in flight.** Now and Blocked. Not a queue — the queue is `02-TASKS.md`, and
duplicating it here is the most likely way this drifts. Never a `## Next` heading. Never task
checkboxes. `workspace-doctor.ps1` fails if either returns. Read first, every session; update before
ending substantial work. Keep under ~3 KB.

**`02-TASKS.md` — the queue.** Open work that survives past this session. One task per line, fixed
shape (§6b). This is the only place tasks are authored, in any project.

**`03-MEMORY.md` — durable locks.** The only file in the system that can hold a **no**. Git records
what changed, not what is forbidden. The artifacts hold the locked copy but not the fact that it is
locked — an agent reading a page sees copy it could improve, and improving it is the failure. Agent
chat memory does not cross agents and never overrides repo files.

So this holds standing constraints and settled decisions: locked copy, locked visual direction,
closed choices, "do not reopen X", "Y is on hold". Read it before touching anything that looks already
decided. **A thing being improvable is not permission to change it.**

**`04-ACTIVITY.md` — the journal.** One dated entry when material work finishes, shaped by
`_agent-control\templates\AGENT-ACTIVITY-ENTRY.md`. Append only; never rewrite an earlier entry. It
answers "why is this odd thing here" months later, and grows freely because nobody reads it in bulk.

**`05-ARCHIVE.md` — a destination, not a source.** Its only job is letting `03-MEMORY.md` and
`02-TASKS.md` stay short. Content arrives **only** by being pruned out of one of them. Never write to
it directly, never read it unless asked.

### 6b. Task format (fixed — a regex has to parse it)

```markdown
## Open
- [ ] 2026-09-12 :: @grok :: Wire AF auto-send using the short URL
- [ ] :: :: Hide the theme switcher before ads

## Done (keep the last 10, prune the rest to 05-ARCHIVE.md)
- [x] 2026-09-09 :: @claude :: Local D1 smoke test
```

One task per line. `- [ ]` or `- [x]`, then due date (or empty), then owner (or empty), then the text.
Never wrap a task across lines. Never nest sub-tasks — split them into separate lines.

### 6c. Task lifecycle (the workflow — follow it exactly)

A task leaves `02-TASKS.md` by exactly one of four routes. It is never in two places at once.

| What happened | Where it goes | What is left behind in `02-TASKS.md` |
|---|---|---|
| **Picked up** — you are working it now | name it in `01-NOW.md` under Now | the line stays, unchecked |
| **Finished** | tick it `- [x]`, leave it under Done | nothing more; prune past 10 to `05-ARCHIVE.md` |
| **Became a decision** — it settled into a standing constraint, a lock, or a "we are not doing this" | write it in `03-MEMORY.md` | **delete the line.** It is a decision now, not work |
| **Abandoned** | one line of why in `04-ACTIVITY.md` | **delete the line** |

The third row is the one that keeps `02-TASKS.md` honest. "Decide whether to gate the theme switcher"
is a task; once decided, "theme switcher stays hidden until ads are wired" is a lock. If the decision
stays in the task file, agents keep re-opening a settled question — which is the exact failure
`03-MEMORY.md` exists to prevent.

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

Target under ~8 KB. Past that, prune the derivable material to `05-ARCHIVE.md` in one file operation
(§4 rule 3) — never by re-typing it through the model.

Cross-project preferences — how the user likes to be worked with in general — are **not** project
memory. They belong in the machine-wide agent rules. A working-style section copied into several project
files drifts the first time it is refined in one of them.

### 6f. Finding open work across every project

There is **no** aggregated task file. A roll-up would be a second copy of every task and would be wrong
the moment a project file changed. Aggregate on demand instead — the answer is always live:

```powershell
F:\__ai-projects\_agent-control\bin\open-tasks.ps1              # every project
F:\__ai-projects\_agent-control\bin\open-tasks.ps1 -Project final-days
F:\__ai-projects\_agent-control\bin\open-tasks.ps1 -Owner @grok
```

It reads `_agent-control\PROJECTS.yaml` for the project list, scans each `02-TASKS.md`, and prints every
open line with its source path and line number. When the user asks *"what is open"*, *"show me all my
to-dos"*, or anything of that shape across projects — **run that, do not guess and do not hand-collect.**

Without the script, the same thing by hand:

```powershell
Get-ChildItem F:\__ai-projects -Recurse -Filter 02-TASKS.md -Depth 3 |
  Select-String -Pattern '^- \[ \]'
```

### 6g. Resume rule

Read `01-NOW.md`. Read `02-TASKS.md`. Read `03-MEMORY.md` before changing anything already settled. For a
staged Scripture Journey deliverable, read its `project-brief.md`: if `status` is set, resume that stage
and load only its lanes. With no brief, treat the work as intake/discovery — never assume a prior
approval.

### 6h. Drift detection

```powershell
F:\__ai-projects\_agent-control\bin\workspace-doctor.ps1
```

Run after changing any numbered file. Exit 1 means the contract is broken — fix it before you stop.
It fails if `## Next` or task checkboxes appear in `01-NOW.md`, if both old and new names exist, if a
retired name returns, or if the machine-wide template regresses. Conventions hold because this notices.

## 7. Local `AGENTS.md` in a work folder

A consumer folder may keep a short `AGENTS.md` that points at `F:\__ai-projects\agent-skills` and this
file, and states that all agents share the folder. It must **not** restate the rules above.
`CLAUDE.md` may be `@AGENTS.md` only.

---

## 8. Skills still route via CATALOG

1. `CATALOG.md` → matching skill
2. The skill's procedure for *how*
3. **This file** for *where* files go, *how* they are named, and *how* they are read and written

<!-- Agent: goBot · Date: 2026-09-09 · TOPIC-BOARD retired; NOW.md is session pickup. -->
<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 2026-09-10 · Single-sourced the naming contract; progressive stems + run-log journal; added §4 file I/O rules. -->
<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 2026-09-10 · §6 restored MEMORY.md as a first-class file; numbered five-file model in order of need, task queue + lifecycle, the derivability test, brief-cites-never-copies, and on-demand cross-project task discovery. -->
<!-- Agent: grok · Model: Grok 4.6 · Thinking: not exposed · Date: 2026-09-10 · ACTIVE-WORK.md is a leftover state file; doctor FAILs pickup pointers at NOW.md/MEMORY.md. -->
<!-- Agent: grok · Model: Grok 4.5 · Date: 2026-09-13 · §3d: human-readable instruction folders are _docs/, not docs/. -->
