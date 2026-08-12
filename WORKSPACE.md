# Workspace conventions (all agents, all skills)

**Always apply.** This file is part of the agent-skills contract, not a single skill.  
Read with `CATALOG.md`. Every skill inherits these rules unless a skill explicitly tightens them.

Agents covered: **Grok, Claude, Codex, Freebuff, Cursor**, and any other local agent.

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

Default: all agents write into the **same** user-chosen directory (example: a series folder or a topic folder).

When a topic outgrows a flat list (~6+ artifact types), use **one topic/episode subfolder** — still shared by every agent — never one folder per agent.

```text
work-root/
  AGENTS.md                 # optional local pointer to this contract
  SERIES-BOARD.md           # or TOPIC-BOARD.md — human map of everything
  <stem>.txt                # source
  <stem>.titles.md          # CANONICAL
  <stem>.titles_grok.md     # draft only
  <stem>.descriptions.md    # CANONICAL
  <stem>.STATUS.md          # optional per-item dashboard
```

---

## 2b. New topic project — agent creates the shell (stupid-simple)

When the user starts a **new** named topic (e.g. “Psalm 23”, “Mark of the Beast study”) and no project folder exists yet:

1. Create **one** kebab-case folder in the place they asked (or under the current work root).
2. **If a path already exists, do not wipe or rebuild it** — only create missing pieces; reference what is already there.
3. Seed this **same** structure every time so projects stay consistent:

```text
<topic-slug>/
  AGENTS.md                 # short pointer to agent-skills + WORKSPACE
  TOPIC-BOARD.md            # human map (update as you go)
  project-brief.md          # one living brief (YAML or markdown)
  planning/                 # optional long plans live here
  mood/                     # drop finished inspiration / generated art here
  prompts/                  # agent writes artwork-prompts.md for human image tools
  references/               # project-specific refs; link/copy only what you need
    dynamic-symmetry/       # optional: README pointing at design-resources pack
  sources/                  # project-local sources only (optional)
    intake/                 # user can dump files here — no forms required
  deliverables/             # shippable page, exports, finals
    assets/                 # finished art named to match prompts file (p01-….png)
```

**Creative-friendly intake:** the user may drop files into `mood/` or `sources/intake/` with **zero paperwork**. Agents use what is there. Formal `registry.yaml` is only for shared vault / doctrinal source libraries—not for every mood PNG.

**Shared design pack (do not duplicate 500MB into every project):**  
`F:\__ai-projects\design-resources\dynamic-symmetry-grids\`  
Projects only need a short pointer under `references/dynamic-symmetry/README.md`.

---

## 3. Canonical vs draft filenames (required)

| Kind | Pattern | Meaning |
|------|---------|---------|
| **Canonical** | `name.ext` — **no** agent suffix | Source of truth; user picks, ships, and continues from here |
| **Draft** | `name_<agent>.ext` | One agent’s proposal; never treated as final unless user promotes it |

### Agent suffix tokens (use exactly these when known)

`grok` · `claude` · `codex` · `freebuff` · `cursor` · `other`

Examples:

```text
FDI--3ABN--s02--ep19.titles.md              ← canonical
FDI--3ABN--s02--ep19.titles_grok.md         ← Grok draft
FDI--3ABN--s02--ep19.titles_freebuff.md     ← Freebuff draft
FDI--3ABN--s02--ep19.descriptions.md        ← canonical descriptions
ep19.STATUS.md                              ← status for humans + agents
```

### Agent rules

1. If the user did **not** ask for a multi-agent bake-off, write/update the **canonical** file.
2. If comparing agents, or the user says “your version,” write `_<agent>` **drafts** and leave canonical alone until told to promote.
3. **Promote** = merge/copy accepted content into the unsuffixed file; keep or delete drafts as the user prefers.
4. Never invent a second canonical name (`final`, `v2`, `latest`) when a suffix or STATUS note will do.
5. Preserve user marks such as trailing `~` on title lines when editing.
6. Prefer updating an existing canonical path over creating a sibling with a new stem.

---

## 3b. Agent identification (NON-NEGOTIABLE — all agents, all tasks)

Multiple agents routinely read and write the **same** series/topic folders. The human must always be able to tell **who** produced a file without opening chat history.

### Shared work root (default)

- **In-file stamp required** on every file you create or materially edit:  
  `**Agent:** Grok` / `**Agent:** Freebuff` / HTML `<!-- Agent: Grok -->` / code header comment / YAML `agent:` field / equivalent.
- **Filename suffix** `name_<agent>.ext` is **required** for bake-off drafts and for any parallel proposal that is not the promoted canonical.
- Canonical `name.ext` has **no** agent suffix, but **still** carries the in-file stamp (author or last material updater).
- When updating boards or `*.STATUS.md`, note the agent in the change line.

### Agent-private root (only if user assigned one or an existing worktree)

Examples: `…/scripture-discovery-journey-worktrees/grok/`, a user-made `…/claude/` sandbox.

1. **Top-level identity:** the root folder name **or** an `AGENT.md` / `AGENT.txt` at that root must state the agent.
2. **In-file stamp** on every output (same as shared).
3. Do **not** invent a private tree for a topic that already has a shared root unless the user asks.

### Not sufficient

- Chat-only “— Grok” signatures with no disk stamp  
- Editing shared files with no agent field and no `_<agent>` draft when the work is a competing proposal  

### Lean chat (NON-NEGOTIABLE — pairs with machine `AGENTS.md`)

- Brief status only in chat (what / path / blocked).  
- **No** code, diffs, patches, or full dumps in chat — those live in files only.

### Artifact stem order (video / packaging work)

Use a stable stem and grow extensions:

```text
<stem>.txt                 # transcript / source
<stem>.titles.md
<stem>.descriptions.md
<stem>.thumbnails.md
<stem>.page.md             # or page/ subfolder when HTML grows
<stem>.STATUS.md
```

---

## 4. Boards (so no one hunts folders)

### Series / folder board

At the work root, maintain **`SERIES-BOARD.md`** (or `TOPIC-BOARD.md` / `BOARD.md`):

- One row (or section) per episode/topic.
- Columns or bullets for: source, titles, descriptions, thumbs, page, notes, next action.
- Update the board when you create or promote a material artifact.

### Item status (optional but preferred once an item is busy)

`<stem>.STATUS.md` or `epNN.STATUS.md`:

- Paths to canonical + known drafts  
- User selections (`~` titles, chosen description)  
- Next step  

Agents: if a board exists, **read it before inventing new file names**; **update it** when finishing a slice.

---

## 5. Local `AGENTS.md` in a work folder

Consumer folders should keep a short `AGENTS.md` that:

1. Points at `F:\__ai-projects\agent-skills` + this `WORKSPACE.md`  
2. States “all agents share this folder”  
3. Repeats canonical vs `_<agent>` draft rules  
4. Names the board file (`SERIES-BOARD.md`, etc.)

`CLAUDE.md` may be `@AGENTS.md` only.

---

## 6. What not to do

- Per-agent folder trees for the same series/topic  
- Only draft files with no canonical  
- Copying whole skill trees into the work root  
- Scattering the same episode across unrelated directories without a board link  

---

## 7. Skills still route via CATALOG

Workspace rules do **not** replace skill routing:

1. `CATALOG.md` → matching skill  
2. Skill procedure for *how* to write titles/pages/transcripts  
3. **This file** for *where* and *how files are named* in the work folder  
