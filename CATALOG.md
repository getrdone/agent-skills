# Skill catalog (read this first — do not load every skill)

<!-- Agent: Grok · Model: Grok 4.5 · Thinking: not exposed · Date: 2026-09-01 -->
<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-08-21 -->

**Always also follow** [`WORKSPACE.md`](WORKSPACE.md): one shared work folder; **until final chosen**, all agent work products (HTML, packaging, **prompts**, pass notes) are `name_<agent>_vN`; promote bare `name.ext` only after the user chooses that deliverable; series/topic boards; **auto-scaffold** new topic folders. Workspace rules apply to **every** skill and to work with no matching skill.

**For any design-bearing task, also follow** [`DESIGN-DIRECTIVES.md`](DESIGN-DIRECTIVES.md): brand systems, palettes, visual systems, graphic design, thumbnails, artwork direction, UI theming, CSS color systems, visual review, and developer handoff of design tokens. Its core chain is: **source-specific evocative naming → locked official colors → harmonized families → compact core palette → semantic developer tokens → named signature gradients → psychological usage tied to imagery/content → practical designer/developer guidance → validated accessibility**. Project/source truth always outranks examples.

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
| artwork-prompts-handoff | `skills/artwork-prompts-handoff/` | image prompts, artwork prompts, thumbnail prompts, generate art, make graphics, mood board images, I'll create images manually, Leonardo/Canva without credits, art handoff, prompts file |
| modern-html-aeo | `skills/modern-html-aeo/` | HTML page, landing page, self-contained HTML, AEO, GEO, SEO page, conversion page, Core Web Vitals, modern HTML |
| interactive-components | `skills/interactive-components/` | accordion, tabs, filter, calculator, modal, carousel, form interaction, progressive disclosure, UI components |
| modern-css-design | `skills/modern-css-design/` | CSS, container queries, layout, theming, design system, motion, effects, fluid type |
| optimized-deliverables | `skills/optimized-deliverables/` | web page, article, landing page, deliverable, SEO content, GEO, scannable content |
| cloudflare-platform | `skills/cloudflare-platform/` | Cloudflare, Pages, Workers, edge deploy, wrangler, KV, D1, R2, Turnstile, deploy site |
| ubp-translator-pdf | `skills/ubp-translator-pdf/` | translator PDF, UBP PDF, prophecy series PDF, Plain Vision printable notes, Unlocking Bible Prophecies review PDF, Malagasy translator review |

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
