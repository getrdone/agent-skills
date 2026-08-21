# Workspace conventions (all agents, all skills)

**Always apply.** This file is part of the agent-skills contract, not a single skill.  
Read with `CATALOG.md`. Every skill inherits these rules unless a skill explicitly tightens them.

Agents covered: **Grok, Claude, Codex, Freebuff, Cursor, Gemini**, and any other local agent.

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
  prompts/                  # agent writes artwork-prompts_<agent>.md (promote bare name only when final chosen)
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

**Until the user chooses the final for that deliverable, every agent-written work file is agent-named and versioned.**  
That includes HTML pages, packaging (titles/descriptions/thumbnails), **artwork prompts**, visual/content plans written for a pass, and gate-result notes for a build pass.  
Canonical `name.ext` (no agent token) exists **only after promote** — never as the working file while options are still open.

| Kind | Pattern | Meaning |
|------|---------|---------|
| **Canonical** | `name.ext` — **no** agent suffix | **Promoted final only** — user chose this as the ship/source of truth |
| **Draft / progress** | `name_<agent>.ext` | One agent’s working pass; human can inspect progress |
| **Draft re-run** | `name_<agent>_v2.ext` (then `_v3`, …) | Later pass by the same agent; keep history |

### Agent suffix tokens (use exactly these when known)

`grok` · `claude` · `codex` · `freebuff` · `cursor` · `gemini` · `other`

Examples:

```text
index_freebuff.html                              ← Freebuff HTML pass
index_grok.html                                  ← Grok HTML pass
index_grok_v2.html                               ← Grok re-run
index.html                                       ← CANONICAL only after user chooses/promotes
prompts/artwork-prompts_freebuff.md              ← Freebuff art prompts (not bare artwork-prompts.md)
prompts/artwork-prompts_grok_v2.md               ← Grok prompts re-run
prompts/artwork-prompts.md                       ← CANONICAL only after promote
stem.titles_claude.md                            ← Claude titles draft
stem.titles.md                                   ← canonical titles after promote
planning/gate-results_grok.md                    ← gate notes for a grok pass
```

**Forbidden while final is unchosen:** writing or updating bare `index.html`, `artwork-prompts.md`, `stem.titles.md`, etc. as the working file.  
**Forbidden always:** bare version piles (`index_v2.html`, `final.html`, `latest.html`). Version only as `_<agent>_vN`.

### What stays unsuffixed (not “final deliverables”)

- Shared navigation: `TOPIC-BOARD.md` / `SERIES-BOARD.md` / `START-HERE.md` / `AGENTS.md` / `project-brief.md` (living project spine — still get in-file agent stamps when edited)
- User drops: anything the human puts in `mood/` or `sources/intake/` under their own names
- Generated binary assets once the human saves them to the agreed target filenames under `deliverables/assets/`

### Agent rules

1. **Default for all agent work products:** write `name_<agent>.ext` or `name_<agent>_vN.ext`. Keep prior passes; do not overwrite earlier `_vN` files. **Do not** put unchosen work on the canonical name.
2. **Promote** = copy the accepted draft into unsuffixed `name.ext` when the user says promote / final / ship / “this is the one,” or otherwise chooses that pass as the final for that deliverable. Leave drafts in place unless asked to delete them. Promote **each deliverable type separately** (e.g. HTML can stay draft while prompts are promoted, or vice versa).
3. **In-place canonical edits** only after that deliverable was already promoted (typo, small fix), or when the user explicitly wants a single living file with no version history.
4. Never invent a second **canonical** name (`final`, `v2`, `latest`) — version only via `_<agent>_vN`.
5. Preserve user marks such as trailing `~` on title lines when editing.
6. Prefer a stable stem (`index`, `artwork-prompts`, `stem.titles`, …) over inventing new stems for the same artifact.
7. Re-running a draft: append `_v2` then `_v3` **after the agent token**, before the extension — e.g. `index_grok_v2.html`, `artwork-prompts_freebuff_v2.md`. Never `_vN` on the bare canonical stem.

---

## 3b. Agent identification (NON-NEGOTIABLE — all agents, all tasks)

Multiple agents routinely read and write the **same** series/topic folders. The human must always be able to tell **who** produced a file, **which model produced it, and at what thinking/reasoning level**, without opening chat history.

### Identity fields

Use these four execution-identity fields wherever this standard requires agent identity:

- **Agent** — product/agent name, e.g. `ChatGPT`, `grok`, `claude`, `codex`, `freebuff`.
- **Model** — exact model identifier visible to the agent/runtime, e.g. `GPT-5.6 Sol`, `Grok 4.5`, `Claude Opus 4.1`.
- **Thinking** — exact thinking/reasoning-effort level selected or exposed by the runtime, e.g. `low`, `medium`, `high`, `max`, `extended`, or the vendor's exact label.
- **Date / What changed** — files use the date written; commits use a concise description of the change.

**Never guess a thinking/reasoning level.** If the runtime does not expose one, write `Thinking: not exposed`. If the runtime exposes a default but no named level, write the exact exposed label (for example `default`). Do not silently omit the field.

### Shared work root (default)

- **In-file stamp required** on every file you create or materially edit. The stamp must state the **agent**, **model**, **thinking/reasoning level**, and **date written** — e.g. `**Agent:** grok · **Model:** Grok 4.5 · **Thinking:** high · **Date:** 2026-08-12`, or HTML `<!-- Agent: grok · Model: Grok 4.5 · Thinking: high · Date: 2026-08-12 -->`, code header comment, YAML `agent:` / `model:` / `thinking:` / `date:` fields, or equivalent. **Never write only the agent name.**
- **Append, don't overwrite.** When a file is later written or materially edited by a different agent, model, or thinking level, **add a new stamp line** (date, agent, model, thinking) instead of replacing the original, so the file keeps a running history of who wrote it, with which model, and at which reasoning setting. If the same agent, model, and thinking level touch the file again, just update that line's date.
- **Filename suffix** `name_<agent>.ext` is **required** for bake-off drafts and for any parallel proposal that is not the promoted canonical.
- Canonical `name.ext` has **no** agent suffix, but **still** carries the in-file stamp (author or last material updater).
- When updating boards or `*.STATUS.md`, note the agent, model, and thinking level in the change line.
- **Git commit messages are required to carry execution identity.** For every commit to a skills repo, design repo, source repo, project repo, or any other repo touched by an agent, use this one-line subject format:

  `Agent: <agent> | Model: <model> | Thinking: <level-or-not-exposed> | What changed: <concise description>`

  Examples:

  `Agent: Grok | Model: Grok 4.5 | Thinking: high | What changed: harmonize Final Days palette around locked Deep Ember and add semantic tokens.`

  `Agent: ChatGPT | Model: GPT-5.6 Sol | Thinking: not exposed | What changed: add cross-skill design directives and route design work through them.`

  This applies to **all agents and sub-agents**, including automated or delegated passes. If one agent commits work substantially authored by another agent, the commit should identify the agent/model/thinking level that performed the committing change and mention material co-author/provenance in `What changed` when relevant.

### Agent-private root (only if user assigned one or an existing worktree)

Examples: `…/scripture-discovery-journey-worktrees/grok/`, a user-made `…/claude/` sandbox.

1. **Top-level identity:** the root folder name **or** an `AGENT.md` / `AGENT.txt` at that root must state the agent.
2. **In-file stamp** on every output (same as shared, including model + thinking level + date).
3. Do **not** invent a private tree for a topic that already has a shared root unless the user asks.

### Not sufficient

- Chat-only “— Grok” signatures with no disk stamp  
- A commit that names the agent but omits model or thinking/reasoning level  
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
- Bare version piles without agent tokens (`index_v2.html`, `final.html`)  
- Putting unfinished HTML on the canonical name while still iterating  
- Copying whole skill trees into the work root  
- Scattering the same episode across unrelated directories without a board link  

---

## 7. Skills still route via CATALOG

Workspace rules do **not** replace skill routing:

1. `CATALOG.md` → matching skill  
2. Skill procedure for *how* to write titles/pages/transcripts  
3. **This file** for *where* and *how files are named* in the work folder  
