# agent-skills

Canonical skill library for coding/chat agents. **Do not load the whole repo into context.**

## Agent contract (required)

```
1. Fetch or open CATALOG.md only (this is the index).
2. Match the user request to a skill row by triggers/intent.
3. If match → load skills/<name>/SKILL.md and only the files that skill says to load.
4. If no match → proceed with normal judgment; do not invent a skill or load siblings.
5. Never preload all skills “just in case.”
```

Optional local install (Grok / similar): copy or submodule a **single** skill into  
`.grok/skills/<name>/` when you want always-on routing for that skill in one project.  
The GitHub catalog remains the source of truth for discovery.

## Layout

```
CATALOG.md                 # thin index — always start here
README.md                  # this contract
skills/
  clean-video-transcript/  # first skill
    SKILL.md
    README.md
    references/
    examples/
```

## Skills

| Skill | Purpose |
|-------|---------|
| [clean-video-transcript](skills/clean-video-transcript/) | Raw video/ASR transcript → polished markdown + source Quick Reference |

## Ownership
Repo: intended as the single place to gather skills over time. Prefer small, single-purpose skills with sharp catalog triggers.
