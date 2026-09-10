# Project System and Gates

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-08-21 -->

Use this file for new projects, cross-channel work, handoffs, or continuation from partial artifacts.

## Contents

- One capability, modular responsibilities
- Canonical project record
- Status progression
- Cross-channel inheritance
- Piecemeal work
- Recommended project planning files

## Compact intake for a small prompt

For a small prompt such as `Psalm 23`, keep it creative-friendly—**no bureaucratic source forms**.

### 0) Scaffold first (if this is a new project)

If no topic folder exists yet, create the standard shell from **`WORKSPACE.md` §2b** (AGENTS.md, 01-NOW.md, 02-TASKS.md, project-brief.md, `planning/`, `mood/`, `prompts/`, `references/`, `sources/intake/`, `deliverables/assets/`).  
If the folder already exists, **do not rebuild**—only add missing folders/files and use what is already there. Point `references/dynamic-symmetry/` at `F:\__ai-projects\design-resources\dynamic-symmetry-grids\` (do not copy the whole pack).  
When artwork is needed, use skill **`artwork-prompts-handoff`** → `prompts/artwork-prompts.md` (human generates; no paid image APIs by default). Naming: repo [`WORKSPACE.md`](../../../../WORKSPACE.md) §3.

### 1) Then one compact decision round

1. Recommend or confirm the deliverable.
2. Offer several sincere curiosity angles.
3. Present a verse-by-verse translation review plan. Never prescribe a project-wide version unless the user asks for one.
4. State the proposed files and durable location (inside the scaffold).
5. State the truthful status and exact approval boundary.
6. Include a flexible choice such as “I’m not sure yet—develop some grounded ideas.”

That flexible choice permits creativity, not unsupported claims or unbiblical tangents. Approval to explore or draft does not approve the resulting content. Keep every agent-selected decision labeled `candidate` until the user accepts it.

User drops in mood images or sources anytime via `mood/` and `sources/intake/`—agents notice and use them without requiring registration.

## One capability, modular responsibilities

Present one user-facing ability while preserving three internal domains:

- **Universal web experience:** semantic HTML, CSS, progressive JavaScript, accessibility, performance, SEO/AEO/GEO, visual implementation, and technical validation.
- **Scripture journey:** question choice, source integrity, curiosity architecture, evidence, reading level, payoff ladders, low-pressure interaction, and next paths.
- **YouTube/video:** audience, ideation, filtration, packaging, titles, descriptions, thumbnails, structure, retention, production, and learning from results.

The shared spine travels across all three. Channel mechanics do not leak into unrelated work.

## Canonical project record

Maintain one `project-brief.md` when files are available. Reuse equivalent existing filenames instead of creating duplicates.

```yaml
project:
status: idea
# --- machine state (read first on resume; write before exiting) ---
stem:                     # artifact stem in this folder, e.g. dan8-cleansing
last_lanes: []            # lanes loaded on the last run, from load-map.yaml
open_gates: []            # gates currently FAIL or BLOCKED
last_agent:               # agent/model/thinking of the last material change
last_updated:             # ISO date
# ------------------------------------------------------------------
audience:
channel_role:
core_question:
why_care:
known_anchor:
new_idea:
promise:
primary_payoff:
evidence_plan: []
source_library:
  repository: getrdone/bible-study-source-materials
  snapshot:
  registry_version:
source_records: []
source_alignment_status: unstarted
source_alignment_manifest:
source_conflicts: []
source_expansions: []
truth_boundaries: []
tone_keywords: []
learning_path: []
learning_pattern_plan: []
visual_direction_status: unstarted
visual_dna: {}
interaction_plan: []
chosen_title:
youtube_description:
thumbnail_direction:
video_structure_status: unstarted
html_status: unstarted
next_curiosity:
featured_next_path:
alternate_paths: []
translation_status: per-passage-review-required
translation_review_minimum: [KJV, NLT, CSB, WEB, NASB]
passage_translation_selections: {}
translation_rights: []
references_status: unstarted
locked_decisions: []
open_decisions: []
```

Add lane-specific details only when that lane begins. Do not prefill invented decisions.

`status` is the single stage field — there is no separate stage file. Do not create `PROJECT-STATUS.md`,
`STATUS.md`, or any second machine-readable state store in a work folder.

### Scope: this brief covers ONE deliverable

`project-brief.md` is the production record for a single Scripture Journey deliverable. A project with
six episodes has one `03-MEMORY.md` and up to six briefs. Scope test: **would this still be true for the
next episode?** Yes → the project's `03-MEMORY.md`. Only for this one → this brief.

**Cite, never copy.** Project-wide locks — locked palette, locked copy, approved visual direction —
live in `03-MEMORY.md`. Write `locked_decisions: [see 03-MEMORY.md § Locked visual]`, not the values
themselves. A value in two files goes stale in one of them silently.

**A brief is not mandatory.** Create it when a deliverable starts moving through stages. An ops or
landing-page project runs on `01-NOW.md` + `02-TASKS.md` + `03-MEMORY.md` alone; do not scaffold an empty forty-field YAML.

Full five-file model and the task lifecycle: repo root `WORKSPACE.md` §6.

### Resume rule (required)

A new agent entering an existing work folder:

1. Read `01-NOW.md` and `02-TASKS.md`.
2. Read the project's `03-MEMORY.md` before touching anything that looks already decided.
3. Read `project-brief.md`. If `status` is set, **resume that stage** — do not restart earlier ones.
4. Load only the lanes for that stage (`load-map.yaml`), plus `spine`. Never reload the whole skill.
5. Clear or carry forward each entry in `open_gates`; do not silently drop one.
6. Before exiting, write `status`, `stem`, `last_lanes`, `open_gates`, `last_agent`, `last_updated`.

With no `project-brief.md`, treat the work as intake/discovery. Never assume a prior approval.

## Status progression

Use the smallest truthful status:

```text
idea → candidate → content-approved → visual-approved
→ approved-for-build → building → validation → released
```

- `content-approved`: the question, audience, payoff, evidence, pinned source-library snapshot, source alignment, learning path, selected learning patterns, and truth boundaries are stable.
- `visual-approved`: the visual DNA, hierarchy, composition, imagery direction, type direction, palette direction, interaction style, and avoid list are stable.
- `approved-for-build`: content, visual, and interaction plans are complete enough to implement without guessing.
- `validation`: the artifact is built and undergoing the relevant technical, integrity, learning, visual, and experience gates.

## Cross-channel inheritance

Every artifact derives from the same core brief:

| Shared decision | Title/description | Thumbnail/graphic | Video | Scripture study | HTML |
| --- | --- | --- | --- | --- | --- |
| Core question | One honest gap | One visual question | Single goal | Central question | Opening promise |
| Payoff | Accurate benefit | Preview, not answer | Nested payoffs | Evidence ladder | Progressive sections |
| Learning map | Plain phrasing | Minimal load | Scaffolding + pacing | Known→new sequence | Progressive disclosure |
| Tone | Word choice | Face/type/color | Delivery/music | Voice | Design/motion |
| Truth boundary | No overclaim | No false image | No fake stakes | Source integrity | Visible evidence/schema |

If a downstream artifact needs a different promise, update the core brief or treat it as a separate project/variant.

## Piecemeal work

- Start at the artifact the user brings.
- Backfill only dependencies that materially affect the requested slice.
- Do not force topic discovery when a transcript or finished study already defines the topic.
- Do not force thumbnail design when only titles are requested.
- Do not reopen an approved title merely because the next step is a description.
- After title generation, expect the user to mark preferred lines with trailing `~` in the packaging file, then request descriptions and/or a few more titles inspired by those marks—do not require a separate formal “approval” status for that selection step.
- Keep **What the Episode Is Really About** in the packaging file once written; update it only if the source idea or transcript understanding materially changes.
- When several options are still live, label them as candidates rather than silently locking one.

## Recommended project planning files

Prefer the **topic root scaffold** (WORKSPACE §2b). Inside it, for a substantial build, grow:

```text
<topic-slug>/
  project-brief.md
  planning/
    content-plan.md
    visual-direction.md      # name dynamic-symmetry ratio + grid file used
    interaction-plan.md
    design-fingerprint.json
  mood/                      # freeform inspiration drops
  references/
  deliverables/
```

Keep planning assets separate from production files. Do not turn the brief into duplicate long-form instructions already held by this skill.

## Multi-agent workspace

File naming, file I/O, and continuity are defined **only** in the agent-skills root
[`WORKSPACE.md`](../../../../WORKSPACE.md) §3–§6. Read it when creating or naming files. Do not restate its rules here or in a
project folder.

The two things this skill adds on top:

- Packaging artifacts are **deliberation artifacts** (progressive stems, append-only run log).
  A built page, a cleaned transcript, and a prompts pack are **deterministic deliverables** (canonical
  on first write).
- Preserve the user's `~` marks on title lines exactly. `~` is the marking gesture; the `SELECTED`
  block is generated from those marks and is the only thing a later stage reads.

<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 2026-09-10 · Added machine state fields + resume rule to the canonical brief; naming rules single-sourced to WORKSPACE.md. -->
<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 2026-09-10 · Brief is one deliverable, optional, and cites MEMORY.md rather than copying project-wide locks. -->
