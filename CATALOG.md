# Skill catalog (read this first — do not load every skill)

<!-- Agent: Grok · Model: Grok 4.5 · Date: 2026-09-16 · Flatten reset: origin/main + local extras; images phase; Remotion on-request. -->

**Always also follow** [`WORKSPACE.md`](WORKSPACE.md).

**Whenever any image is generated or any visual layout places subjects/type on a canvas, load** [`skills/dynamic-symmetry/SKILL.md`](skills/dynamic-symmetry/SKILL.md). Soft standard: rectangle + armature + crop integrity. Write “Dynamic Symmetry” in full (never “DS”). Scripture Journey, web-studio, artwork prompts, and image-direction skills all route here — do not keep a second method copy.

## Layout standard (lock)

1. Live skills live only under `skills/<kebab-name>/` with a root `SKILL.md`.
2. **No nested skill packs** inside `skills/` (`agent-skills/`, `claude-skills/`, zip dumps).
3. Archives / retired skills go in `packages/` — never auto-loaded, never synced as discoverable skills.
4. Versioned skills (CDSJ) use `CURRENT` / `STABLE` + `versions/<ver>/` only when cross-release mixing is a real risk.
5. **This catalog is the allowlist.** If a folder is not listed here, do not treat it as a default skill.
6. **web-studio owns HTML.** Other skills call it; they do not invent parallel web pipelines.
7. Sync mirrors `skills/` into agent homes (`~/.grok/skills`, etc.). It does not `git pull`.

If one skill matches → load **only** `skills/<name>/SKILL.md` (and files it points to).

### Core (Grok main pack + GitHub HEAD)

| Skill | Path | Triggers |
|-------|------|----------|
| clean-video-transcript | `skills/clean-video-transcript/` | clean transcript, ASR cleanup, verse list, EGW list |
| curiosity-driven-scripture-journey | `skills/curiosity-driven-scripture-journey/` | titles, descriptions, Scripture journey, learning paths, ministry copy |
| artwork-prompts-handoff | `skills/artwork-prompts-handoff/` | art handoff, paste-ready prompts |
| color-palette-composition | `skills/color-palette-composition/` | palette, color scheme, 60-30-10 |
| dynamic-symmetry | `skills/dynamic-symmetry/` | Dynamic Symmetry, armature, root rectangle, phi, crop integrity, composition grid, placement |
| web-studio | `skills/web-studio/` | screenshot to page, clone, images, theme tokens, TUNE, polish, one-off HTML edit |
| lean-output | `skills/lean-output/` | lean, brief, tldr, no fluff |
| youtube-idea-generation | `skills/youtube-idea-generation/` | idea generation, video concepts |
| youtube-title-writing | `skills/youtube-title-writing/` | YouTube titles, curiosity gap, RO formula |
| youtube-thumbnail-design | `skills/youtube-thumbnail-design/` | YouTube thumbnails, three Cs |
| youtube-content-packaging | `skills/youtube-content-packaging/` | packaging, click triggers, story cycles |
| youtube-video-planner | `skills/youtube-video-planner/` | video brief, package my video, hook |
| transcript | `skills/transcript/` | transcribe, YouTube transcript, captions |
| character-turnaround-sheet | `skills/character-turnaround-sheet/` | character sheet, turnaround, FACE CLOSE UP |
| cloudflare-platform | `skills/cloudflare-platform/` | Cloudflare, Workers, Pages, wrangler |

### Local ops extras

| Skill | Path | Triggers |
|-------|------|----------|
| ai-image-generation | `skills/ai-image-generation/` | explicit only: belt / inference.sh image gen, or this skill by name |
| multi-cli-dispatch | `skills/multi-cli-dispatch/` | dispatch goBot / Grok CLI / Codex jobs, job cards, background watcher |

### Image-direction (on-request; web-studio images / polish companions)

| Skill | Path | Triggers |
|-------|------|----------|
| imagegen-frontend-web | `skills/imagegen-frontend-web/` | section art comps, landing image direction, one image per section |
| imagegen-frontend-mobile | `skills/imagegen-frontend-mobile/` | mobile app screen comps (images only) |
| brandkit | `skills/brandkit/` | brand boards, logo systems, identity decks |
| design-taste-frontend | `skills/design-taste-frontend/` | anti-slop frontend taste, redesign audit |
| high-end-visual-design | `skills/high-end-visual-design/` | premium agency spacing/type/shadow critique |
| redesign-existing-projects | `skills/redesign-existing-projects/` | upgrade existing site quality without breaking behavior |

**web-studio phase order:** `clone` → `images` → `theme` → `polish` (one phase per turn unless chained by name).

### Remotion (on-request only)

| Skill | Path | Triggers |
|-------|------|----------|
| remotion-best-practices | `skills/remotion-best-practices/` | Remotion router — load first when Remotion is requested |
| remotion-create | `skills/remotion-create/` | new Remotion video / project |
| remotion-markup | `skills/remotion-markup/` | Remotion React markup |
| remotion-maps | `skills/remotion-maps/` | Remotion maps / geo |
| remotion-multimedia | `skills/remotion-multimedia/` | Mediabunny / browser media |
| remotion-interactivity | `skills/remotion-interactivity/` | Studio interactivity |
| remotion-render | `skills/remotion-render/` | advanced render |
| remotion-studio | `skills/remotion-studio/` | Remotion Studio |
| remotion-captions | `skills/remotion-captions/` | captions |
| remotion-saas | `skills/remotion-saas/` | Player / Lambda / SaaS |
| remotion-docs | `skills/remotion-docs/` | Remotion docs lookup |
| remotion-upgrade | `skills/remotion-upgrade/` | upgrade Remotion |

## Banned / retired (do not load)

`html-page-standard`, `studio-web`, `modern-web-development`, `modern-web-development-v2`, `modern-html-aeo`, `modern-css-design`, `interactive-components`, `optimized-deliverables`, any `claude-skills` nest, any nested `skills/agent-skills` dump.

Retired copies may exist under `packages/retired/` or `packages/archive/` for history only.

## External

| Source | Routing |
|--------|---------|
| [Cloudflare Skills](https://github.com/cloudflare/skills) | Grok marketplace plugin `cloudflare`. Do not keep a second clone under this workspace. |
| [getrdone/ubp-tools](https://github.com/getrdone/ubp-tools) | Trip-specific UBP tooling; not default routing. |

## Sync

Tool: `G:\__ai-projects\_agent-tools\sync-agent-skills\`  
Source: `G:\__ai-projects\_agent-skills\skills`  
Task: `AgentSkillsRobocopy` (15m). Pull this git repo when GitHub changes, then sync.
