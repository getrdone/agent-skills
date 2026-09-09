# Skill catalog (read this first — do not load every skill)

<!-- Agent: Grok · Model: Grok 4.5 · Thinking: not exposed · Date: 2026-09-01 -->
<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-08-21 -->
<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-08 -->

**Always also follow** [`WORKSPACE.md`](WORKSPACE.md): one shared work folder; **until final chosen**, all agent work products (HTML, packaging, **prompts**, pass notes) are `name_<agent>_vN`; promote bare `name.ext` only after the user chooses that deliverable; series/topic boards; **auto-scaffold** new topic folders. Workspace rules apply to **every** skill and to work with no matching skill.

**For any design-bearing task, also follow** [`DESIGN-DIRECTIVES.md`](DESIGN-DIRECTIVES.md): brand systems, palettes, visual systems, graphic design, thumbnails, artwork direction, UI theming, CSS color systems, visual review, and developer handoff of design tokens. Its core chain is: **source-specific evocative naming → locked official colors → harmonized families → compact core palette → semantic developer tokens → named signature gradients → evidence-calibrated psychological usage tied to imagery/content → practical designer/developer guidance → validated accessibility and readability**. Project/source truth always outranks examples.

**Whenever colors are chosen, recommended, generated, requested, compared, or reviewed, also load** [`COLOR-PSYCHOLOGY.md`](COLOR-PSYCHOLOGY.md). Keep ordinary tasks lean by loading the full reference only when a color decision is actually present.

**Shared design pack:** private repo [getrdone/design-resources](https://github.com/getrdone/design-resources) → local clone `F:\__ai-projects\design-resources\` (continuously synced). Glossary text lives in this skills repo; pack `GLOSSARY.md` is a symlink. See `F:\__ai-projects\SOURCES-OF-TRUTH.md`.

Agents: match the user request against **Triggers** below.

### Versioned skill resolution

When a skill directory contains `CURRENT`, `STABLE`, and `versions/`, resolve the requested release before loading its full specification:
- no version named → `CURRENT`;
- "stable" → `STABLE`;
- exact version → `versions/<version>/`.

Do not silently mix versioned reference files across releases. The selected release manifest controls compatibility.  
If one skill matches → load **only** `skills/<name>/SKILL.md` (and files it points to).  
If none match → use your own judgment; do not force a skill.

| Skill | Path | Triggers (keywords / intent) |
|-------|------|------------------------------|
| clean-video-transcript | `skills/clean-video-transcript/` | clean transcript, clean video transcript, remove timestamps, ASR cleanup, Quick Reference, verse list, EGW reference list, YouTube transcript polish |
| curiosity-driven-scripture-journey | `skills/curiosity-driven-scripture-journey/` | Scripture journey, Bible study page, discovery topic, source library, source ingestion, source SQLite, source alignment, learning patterns, teaching strategies, YouTube titles/ideas packaging, 17-category title matrix, thumbnail, ministry landing page, Scripture SEO/AEO, high-trust faith content, project brief gates |
| artwork-prompts-handoff | `skills/artwork-prompts-handoff/` | explicit manual prompt pack, art handoff, I'll generate the images myself, paste-ready prompts file |

## External maintained skills

| Source | Local clone | Routing |
|--------|-------------|---------|
| [Cloudflare Skills](https://github.com/cloudflare/skills) | `F:\\__ai-projects\\cloudflare-skills\\` | Official Cloudflare skills are installed by symlink from this separate clone. Pull updates through the workstation's canonical-repository sync, then repair symlinks. Never copy or fork their instructions into this repository. |

## Specialized repositories

| Repository | Purpose |
|------------|---------|
| [getrdone/ubp-tools](https://github.com/getrdone/ubp-tools) | Trip/project-specific Unlocking Bible Prophecies translator-PDF and Plain Vision tooling; not part of default routing. |

## Processing (load only when needed)

| Package | Path | Triggers |
|---------|------|----------|
| source-vault | `processing/source-vault/` | source vault inventory, register sources, intake records, private library, Bohr transcript quarantine, `registry.yaml` |
| tools registry | `tools/TOOLS.md` | tool list, Canva, Leonardo, OpenBible, EGW, UBP translator PDF tools |

## How to add a skill
1. Add `skills/<kebab-name>/SKILL.md` (+ optional `references/`, `examples/`).
2. Add one row to this table (name, path, short triggers).
3. Keep trigger text short so catalog scans stay cheap.
4. Put support scripts under `processing/<package>/` and add a CATALOG processing row.

## Folded external skills (provenance & sync)

When a community/external skill's knowledge is folded into a skill's references (instead of installing it), record a **provenance block** at the top of the affected reference file: source repo + URL, last-synced date, check cadence, and the re-sync command. List each fold here so the whole tree stays re-checkable:

- `curiosity-driven-scripture-journey/references/motion-and-premium-ui.md` <- `github/awesome-copilot` (`premium-frontend-ui`, `gsap-framer-scroll-animation`) - last synced 2026-08-13 - re-sync: diff against `skills/*/SKILL.md` in that repo.
- `curiosity-driven-scripture-journey/references/design-critique-and-anti-slop.md` <- `pbakaus/impeccable` (surface mode, anti-slop detectors, iteration verbs; Apache 2.0) - last synced 2026-08-13 - re-sync: diff against the impeccable repo skill + detector docs (or install as companion via `npx impeccable install`).

<!-- Agent: Codex · Model: GPT-5 · Thinking: not exposed · Date: 2026-09-09 · Routed color decisions to COLOR-PSYCHOLOGY.md. -->
