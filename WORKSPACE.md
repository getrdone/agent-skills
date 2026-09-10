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
| **Brain (skills)** | `F:\__ai-projects\agent-skills\` | Procedures, SPECs, matrices — shared, synced |
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
  NOW.md                    # session pickup (Now / Next / Blocked)
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
  NOW.md                    # Now / Next / Blocked
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

**Shared design pack (never duplicated into a project):** `F:\__ai-projects\design-resources\dynamic-symmetry-grids\`.
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

### 3d. What stays unsuffixed and unversioned

- Navigation and state: `NOW.md`, `project-brief.md`, `AGENTS.md`
- User drops: anything the human puts in `mood/` or `sources/intake/` under their own names
- Generated binary assets once saved to the agreed filenames under `deliverables/assets/`

### 3e. Forbidden

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

## 6. Continuity — two files, no others

| File | Audience | Contents |
|------|----------|----------|
| `NOW.md` | human | Now / Next / Blocked. Prose. Never parsed by an agent. |
| `project-brief.md` | both | Durable decisions **and** machine state (`stage`, `stem`, `last_lanes`, `open_gates`, `last_agent`). The only machine-readable state in a work folder. |

**Session pickup is `NOW.md`.** Read `project-brief.md` when the task needs stage, locked decisions, or
source pins — which is most substantial work.

- **Legacy `MEMORY.md`:** some existing projects use it as pickup. If a project has `MEMORY.md` and no
  `NOW.md`, read `MEMORY.md` and leave it alone. Do not create new `MEMORY.md` files.
- **Retired:** `TOPIC-BOARD.md` (do not create, do not restore). `START-HERE.md` is not a workspace file.
- **Optional:** `SERIES-BOARD.md` — an inventory for a folder with several episodes. Never mandatory,
  never session context, never per-agent. Update it when you promote a material artifact, if one exists.

Resume rule: read `NOW.md`, then `project-brief.md`. If `stage` is set, resume that stage and load only
its lanes. If there is no brief, treat the work as intake/discovery — do not assume prior approvals.

---

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
<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 2026-09-10 · Single-sourced the naming contract; progressive stems + run-log journal; added §4 file I/O rules; resolved NOW.md/MEMORY.md pickup conflict. -->
