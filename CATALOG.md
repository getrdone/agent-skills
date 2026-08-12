# Skill catalog (read this first — do not load every skill)

**Always also follow** [`WORKSPACE.md`](WORKSPACE.md): one shared work folder, canonical files vs `_<agent>` drafts, series/topic boards, and **auto-scaffold** new topic folders (`mood/`, `references/`, etc.). Workspace rules apply to **every** skill and to work with no matching skill.

**Shared design pack:** private repo [getrdone/design-resources](https://github.com/getrdone/design-resources) → local clone `F:\__ai-projects\design-resources\` (continuously synced). Glossary text lives in this skills repo; pack `GLOSSARY.md` is a symlink. See `F:\__ai-projects\SOURCES-OF-TRUTH.md`.

Agents: match the user request against **Triggers** below.  
If one skill matches → load **only** `skills/<name>/SKILL.md` (and files it points to).  
If none match → use your own judgment; do not force a skill.

| Skill | Path | Triggers (keywords / intent) |
|-------|------|------------------------------|
| clean-video-transcript | `skills/clean-video-transcript/` | clean transcript, clean video transcript, remove timestamps, ASR cleanup, Quick Reference, verse list, EGW reference list, YouTube transcript polish |
| curiosity-driven-scripture-journey | `skills/curiosity-driven-scripture-journey/` | Scripture journey, Bible study page, discovery topic, YouTube titles/ideas packaging, 17-category title matrix, thumbnail, ministry landing page, Scripture SEO/AEO, high-trust faith content, project brief gates |

## Processing (load only when needed)

| Package | Path | Triggers |
|---------|------|----------|
| source-vault | `processing/source-vault/` |
| tools registry | `tools/TOOLS.md` | source vault inventory, register sources, intake records, private library, Bohr transcript quarantine, `registry.yaml` |

## How to add a skill
1. Add `skills/<kebab-name>/SKILL.md` (+ optional `references/`, `examples/`).
2. Add one row to this table (name, path, short triggers).
3. Keep trigger text short so catalog scans stay cheap.
4. Put support scripts under `processing/<package>/` and add a CATALOG processing row.
