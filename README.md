# agent-skills

**Canonical skill library for all agents.** Do **not** load the whole repo into context.

## Agent contract (required)

```
1. Fetch or open CATALOG.md only (this is the index).
2. Match the user request to a skill row by triggers/intent.
3. If match → load skills/<name>/SKILL.md and only the files that skill says to load.
4. If the task needs support tooling → open the matching processing/ package only.
5. If no match → proceed with normal judgment; do not invent a skill or load siblings.
6. Never preload all skills “just in case.”
```

Consumer projects (sites, briefs, source libraries) **reference** this repo; they do not own a divergent copy of a skill. Propose skill changes here.

Optional local install (Grok / Claude / Codex): copy or submodule a **single** skill into the tool’s skills path when you want always-on routing for that skill in one project.

## Layout

```
CATALOG.md
README.md
skills/
  clean-video-transcript/
  curiosity-driven-scripture-journey/
processing/
  source-vault/          # inventory + registration helpers
```

## Skills

| Skill | Purpose |
|-------|---------|
| [clean-video-transcript](skills/clean-video-transcript/) | Raw video/ASR → polished markdown + Quick Reference |
| [curiosity-driven-scripture-journey](skills/curiosity-driven-scripture-journey/) | Scripture content studio: study, titles (17×4), video, visual, web |

## Processing

| Package | Purpose |
|---------|---------|
| [source-vault](processing/source-vault/) | Private source inventory/registration without dumping vault into context |

## Ownership
Single source of truth for agent skills. Prefer sharp catalog triggers and small load sets.
