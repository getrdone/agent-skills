# Skill catalog (read this first — do not load every skill)

<!-- Agent: Grok · Model: Grok 4.6 · Date: 2026-09-15T21:08:00-07:00 · html-page-standard row replaced by web-studio. -->
<!-- Agent: Grok · Model: Grok 4.6 · Date: 2026-09-15 · Added html-page-standard for screenshot-to-HTML pipeline. -->
<!-- Agent: Grok · Model: Grok 4.5 · Thinking: not exposed · Date: 2026-09-01 -->
<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-08-21 -->
<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-08 -->

**Always also follow** [`WORKSPACE.md`](WORKSPACE.md). It is the single source of truth for file naming,
file I/O, and continuity — progressive stems for deliberation artifacts, canonical-on-first-write for
deterministic deliverables, O(1) appends, `NOW.md` pickup, `project-brief.md` machine state, and
auto-scaffolding new topic folders. It applies to **every** skill and to work with no matching skill.
No skill or reference restates its rules.

**For source-led/brand-led visual systems, design-token or gradient architecture, CSS implementation, or developer handoff, also follow** [`DESIGN-DIRECTIVES.md`](DESIGN-DIRECTIVES.md). A stand-alone new or revised palette starts with `color-palette-composition`; add Design Directives only when it needs source locks, canonical names, semantic roles, gradients, or implementation guidance. Its core chain is: **source-specific evocative naming → locked official colors → harmonized families → compact core palette → semantic developer tokens → named signature gradients → evidence-calibrated psychological usage tied to imagery/content → practical designer/developer guidance → validated accessibility and readability**. Project/source truth always outranks examples.

**Whenever a color theme, palette, scheme, allocation, accent plan, mixing, placement, or material palette is created or materially revised, load** [`skills/color-palette-composition/SKILL.md`](skills/color-palette-composition/SKILL.md). It is the sole canonical palette-generation workflow: visual weight, Itten and Munsell application, ratios, mixing, placement, naming handoff, and verification.

**Load** [`COLOR-PSYCHOLOGY.md`](COLOR-PSYCHOLOGY.md) **after composition only when an intended/alternate audience reading, cultural or Scripture context, or a color-psychology claim materially affects the decision.** It supplies contextual evidence and interpretation; it does not replace palette composition. [`DESIGN-DIRECTIVES.md`](DESIGN-DIRECTIVES.md) supplies source locks, canonical names, semantic tokens, gradients, and implementation guidance.

**Shared design pack:** private repo [getrdone/design-resources](https://github.com/getrdone/design-resources) → local clone `F:\\__ai-projects\\design-resources\\` (continuously synced). Glossary text lives in this skills repo; pack `GLOSSARY.md` is a current-release pointer, not a symlink. See `F:\\__ai-projects\\SOURCES-OF-TRUTH.md`.

**Canonical Bible-study source library:** private repo [getrdone/bible-study-source-materials](https://github.com/getrdone/bible-study-source-materials) → local clone `F:\\__ai-projects\\bible-study-source-materials\\` (continuously synced). Path aliases are junctions into that clone — never a second copy. Read `registry.yaml` and approval policy before treating any file as authoritative.

Agents: match the user request against **Triggers** below.

### Versioned skill resolution

When a skill directory contains `CURRENT`, `STABLE`, and `versions/`, resolve the requested release before loading its full specification:
- no version named → `CURRENT`;
- "stable" → `STABLE`;
- exact version → `versions/<version>/`.

Do not silently mix versioned reference files across releases. The selected release manifest controls compatibility.

**Every relative path inside a versioned skill resolves under `versions/<resolved-version>/`.** A skill
directory that carries `versions/` must not also keep a second copy of its references at the skill root.

If one skill matches → load **only** `skills/<name>/SKILL.md` (and files it points to).  
If none match → use your own judgment; do not force a skill.

| Skill | Path | Triggers (keywords / intent) |
|-------|------|------------------------------|
| clean-video-transcript | `skills/clean-video-transcript/` | clean transcript, clean video transcript, remove timestamps, ASR cleanup, Quick Reference, verse list, EGW reference list, YouTube transcript polish |
| curiosity-driven-scripture-journey | `skills/curiosity-driven-scripture-journey/` | titles, descriptions, packaging, `.titles.md`, `.descriptions.md`, Scripture journey, Bible study page, discovery topic, source library, source ingestion, source SQLite, source alignment, learning patterns, teaching strategies, YouTube titles/ideas packaging, 17-category title matrix, thumbnail, ministry landing page copy, Scripture SEO/AEO, high-trust faith content, project brief gates |
| artwork-prompts-handoff | `skills/artwork-prompts-handoff/` | explicit manual prompt pack, art handoff, I'll generate the images myself, paste-ready prompts file |
| color-palette-composition | `skills/color-palette-composition/` | color theme, palette, color combination, color scheme, 60-30-10, primary/secondary/accent, interior palette, graphic color pairing, web-page theme, undertones, tint/tone/shade, how much color, where to put color, palette critique or revision |
| web-studio | `skills/web-studio/` | screenshot to page, mockup to HTML, landing page files, clone page, theme tokens, TUNE, one-off HTML edit, deliverable-clone, deliverable-theme, deliverable-polish |

**Page files:** Scripture Journey and YouTube skills own copy, titles, and learning path. Living HTML uses **web-studio** only (`deliverable-clone` / `deliverable-theme` / `deliverable-polish`). Do not load html-page-standard, studio-web, or modern-web-development.

## External maintained skills

| Source | Install / path | Routing |
|--------|----------------|---------|
| [Cloudflare Skills](https://github.com/cloudflare/skills) | Grok plugin `cloudflare` at `~/.grok/installed-plugins/skills-39968d19/` (marketplace). Do **not** maintain a second `F:\\__ai-projects\\cloudflare-skills\\` clone or fold CF instructions into this repo. | On Workers / Pages / D1 / Wrangler / Agents SDK / Durable Objects match, load the matching skill from that plugin (`cloudflare`, `wrangler`, `agents-sdk`, `durable-objects`, `web-perf`, …). Account MCPs (`cloudflare-api`, bindings, builds, observability) need separate auth; `cloudflare-docs` works without it. |

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

- `skills/curiosity-driven-scripture-journey/versions/3.2.0/references/motion-and-premium-ui.md` <- `github/awesome-copilot` (`premium-frontend-ui`, `gsap-framer-scroll-animation`) - last synced 2026-08-13 - re-sync: diff against `skills/*/SKILL.md` in that repo.
- `skills/curiosity-driven-scripture-journey/versions/3.2.0/references/design-critique-and-anti-slop.md` <- `pbakaus/impeccable` (surface mode, detectors, iteration verbs; Apache 2.0) + `anthropics/skills` `frontend-design` (AI-design cluster list) + spot-check `ravidsrk/slop-detect` emerging fingerprints - last synced 2026-09-10 - next check ~2026-12-10 - re-sync: diff impeccable; re-fetch Anthropic `frontend-design/SKILL.md` clusters; skim slop-detect/essays for new durable tells only (optional `npx impeccable install`).
