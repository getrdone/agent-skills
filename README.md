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
7. All agents share one work folder: canonical name.ext vs draft name_<agent>.ext; keep a BOARD.
```

Consumer projects **reference** this repo; they do not own a divergent copy of a skill. Propose skill changes here.

Optional local install: symlink skills into the tool’s skills path; procedures still come from this clone.

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

## Processing

| Package | Purpose |
|---------|---------|
| [source-vault](processing/source-vault/) | Private source inventory/registration without dumping vault into context |

## Ownership
Single source of truth for agent skills. Prefer sharp catalog triggers and small load sets.
