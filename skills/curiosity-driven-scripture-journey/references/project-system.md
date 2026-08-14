# Project System and Gates

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

If no topic folder exists yet, create the standard shell from **`WORKSPACE.md` §2b** (AGENTS.md, TOPIC-BOARD.md, project-brief.md, `planning/`, `mood/`, `prompts/`, `references/`, `sources/intake/`, `deliverables/assets/`).  
If the folder already exists, **do not rebuild**—only add missing folders/files and use what is already there. Point `references/dynamic-symmetry/` at `F:\__ai-projects\design-resources\dynamic-symmetry-grids\` (do not copy the whole pack).  
When artwork is needed, use skill **`artwork-prompts-handoff`** → `prompts/artwork-prompts.md` (human generates; no paid image APIs by default).

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
audience:
channel_role:
core_question:
why_care:
known_anchor:
new_idea:
promise:
primary_payoff:
evidence_plan: []
truth_boundaries: []
tone_keywords: []
learning_path: []
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

## Status progression

Use the smallest truthful status:

```text
idea → candidate → content-approved → visual-approved
→ approved-for-build → building → validation → released
```

- `content-approved`: the question, audience, payoff, evidence, learning path, and truth boundaries are stable.
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

## Multi-agent workspace (inherits repo WORKSPACE.md)

Follow the agent-skills root **`WORKSPACE.md`** for every packaging or production folder:

- All agents share **one** work directory (series or topic root). No per-agent folder trees.
- **Progress / iteration drafts:** `stem.titles_grok.md`, `index_freebuff_v2.html`, etc. Keep version history when the user wants to see progress.
- **Canonical** (promoted polished only): `stem.titles.md`, `stem.descriptions.md`, `index.html` — no agent suffix, no bare `index_v2.html`.
- Maintain **`SERIES-BOARD.md`** or **`TOPIC-BOARD.md`** at the work root; optional `stem.STATUS.md` per episode/topic.
- Promote accepted polished drafts into canonical; preserve `~` title marks.
- Local `AGENTS.md` in the work folder should point at agent-skills + WORKSPACE.md.
