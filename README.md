# agent-skills

**Canonical skill library for all agents.** Do **not** load the whole repo into context.

## Agent contract (required)

```
1. Open CATALOG.md (skill index) and WORKSPACE.md (file layout — always).
2. Match the user request to a skill row by triggers/intent.
3. If match → load skills/<name>/SKILL.md and only the files that skill says to load.
4. If the task needs support tooling → open the matching processing/ package only.
5. If no match → proceed with normal judgment; do not invent a skill or load siblings.
6. Never preload all skills “just in case.”
7. All agents share one work folder: until final chosen, drafts are `name_<agent>_vN.ext` (including prompts); promote bare `name.ext` only when the user chooses that deliverable; keep a BOARD.
8. Every agent/sub-agent repo commit must identify execution identity: `Agent: <agent> | Model: <model> | Thinking: <level-or-not-exposed> | What changed: <summary>`; never guess a thinking level. Full rule: WORKSPACE.md §3b.
```

Consumer projects **reference** this repo; they do not own a divergent copy of a skill. Propose skill changes here.

**Local install must be symlinks** into this clone (see `F:\__ai-projects\SOURCES-OF-TRUTH.md` and `_agent-control/bin/repair-symlinks.sh`). Continuous sync: `sync-canonical-repos.sh`.

Sibling private pack repo: [getrdone/design-resources](https://github.com/getrdone/design-resources) → `F:\__ai-projects\design-resources\`.

## Layout

```
CATALOG.md
WORKSPACE.md             # multi-agent file/folder standard (all skills)
README.md
skills/
  clean-video-transcript/
  curiosity-driven-scripture-journey/
processing/
  source-vault/
```

## Skills

| Skill | Purpose |
|-------|---------|
| [clean-video-transcript](skills/clean-video-transcript/) | Raw video/ASR → polished markdown + Quick Reference |
| [curiosity-driven-scripture-journey](skills/curiosity-driven-scripture-journey/) | Scripture content studio: study, titles (17×4), video, visual, web |
| [artwork-prompts-handoff](skills/artwork-prompts-handoff/) | Artwork via human tools: numbered paste-ready prompts file (no paid API default) |

## Processing

| Package | Purpose |
|---------|---------|
| [source-vault](processing/source-vault/) | Private source inventory/registration without dumping vault into context |

## Ownership
Single source of truth for agent skills. Prefer sharp catalog triggers and small load sets.
