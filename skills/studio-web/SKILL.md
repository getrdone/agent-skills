---
name: studio-web
description: Master web craft for Grok, Codex, Claude, and Scripture Journey. Use for HTML CSS JS pages, landing pages, ministry sites, web.build, web.repair, section edits, AEO SEO GEO, Core Web Vitals, container queries, motion, interactivity, and polished studio-quality pages. Do not load modern-html-aeo, modern-css-design, interactive-components, or optimized-deliverables with this skill.
metadata:
  version: "1.1"
  type: workflow
  canonical: getrdone/agent-skills
---

# Studio Web — one craft, two lanes

This skill is the **only** web implementation skill. It merges the useful parts of the retired local helpers (`modern-html-aeo`, `modern-css-design`, `interactive-components`, `optimized-deliverables`) with Curiosity-Driven Scripture Journey 3.2.0 `web.build` / `web.repair`.

Canonical long-form Journey web rules live in `getrdone/agent-skills` → CDSJ `versions/3.2.0/references/web-experience.md` (and `visual-system.md` on build). This skill is the shared web craft face for Grok, Codex, and Claude. Local clone on the current machine is `G:\__AI-projects\agent-skills\` (older docs may still say `F:\__ai-projects\`).

Declare before loading extra files:

```text
LANE: web.build | web.repair
CHANGE: <section ids or "new page">
FROZEN: <ids or files not to touch>
```

## When to use which lane

| User ask | Lane | Load |
|---|---|---|
| New page, rebuild, restyle the whole thing | `web.build` | This file + `references/page-anatomy.md`. If a Journey project is open, also CDSJ `web-experience.md` + `visual-system.md`. |
| Fix one section, contrast, broken control, copy block, CSS slice | `web.repair` | This file + `references/repair-contract.md` only. Do not open the design tree. |
| Deploy to Cloudflare | this skill for the page, `cloudflare-platform` only for deploy | Never mix CF docs into design. |

Journey **content** (sources, titles, learning patterns, brief gates) stays in CDSJ other lanes. This skill owns HTML/CSS/JS craft only.

## Constitution (silent on every run)

1. **Works in a real browser** before it is called done. Dead primary controls = FAIL.
2. **Looks premium.** Class-A studio bar. Cream paper + Inter/system fonts as the whole personality = FAIL.
3. **Motion and JS are first-class.** Full purposeful motion is the default. `prefers-reduced-motion` is an optional query, not the design.
4. **Performance without flattening.** CWV constrains how assets load, not whether images, type, or motion exist. Fix the file or the script. Do not delete the picture.
5. **Readable text.** Target 7:1 for sustained reading. Floor is WCAG 2.2 AA. Test type over gradients and images.
6. **Container-query-first.** No `@media (min-width: …)` for component layout. Viewport media only for print, color-scheme, contrast, reduced-motion, root chrome. Human-tunable type, stack (vertical), inset (horizontal), gutter, measure, radius, and motion times live in labeled `/* TUNE */` blocks — see `references/page-anatomy.md`.
7. **One primary action per view.** Hierarchy by scale and position, not five equal cards.
8. **Surgical by default.** Prefer `web.repair` on an accepted page. Snapshot `index_vN.html` only before a destructive structural rewrite.

## Build lane (`web.build`)

1. Lock goal, audience, one promise, one primary action. If Journey work, require `approved-for-build` or an explicit user build order.
2. Lock visual DNA in the brief or `03-MEMORY.md` — type pairing, palette, motion character, imagery direction. Do not invent a second look.
3. Write `deliverables/index.html` (canonical name on first write). Bake-off only if the user asked two agents for rivals (`index_<agent>.html`).
4. Semantic HTML first. Truth and citations live in the document, not only in JS.
5. Network webfonts (display + body). System stacks are fallbacks only.
6. Section-stable markup — see `references/page-anatomy.md`. Every major region gets a stable `id`.
7. CSS in layers or clearly marked section blocks that match those ids.
8. JS config object at the top. Interactions verified in a browser.
9. Images — hero eager (`fetchpriority="high"`), width/height or aspect-ratio set, rest `loading="lazy"`. Missing pixels — CSS/SVG/gradient stand-ins + prompt pack. Layout must not collapse.
10. JSON-LD only when it matches visible content.
11. Stop when the page works and looks finished. Do not rewrite for taste unless asked.

## Repair lane (`web.repair`)

Follow `references/repair-contract.md`. Hard rules:

- Touch only named section ids / selectors.
- Do not restyle frozen regions.
- Do not retitle, re-outline, or swap the palette unless that is the repair.
- Edit in place (search-replace / ranged edit). Do not regenerate the whole file from memory.
- If the change forces a new document outline, say so and switch to `web.build` after snapshot.

## Token discipline (all agents)

- Chat stays lean — path, what changed, what is frozen, what is blocked. No full HTML dumps.
- Read by range. Append with the shell. Edit by pattern. See `getrdone/agent-skills` `WORKSPACE.md` §4.
- Never load the four retired local web skills in the same turn as this one.
- On Journey pages, do not load CDSJ `study` / `packaging` files just to change a footer.

## Cloudflare

Use `cloudflare-platform` after the page exists. Pages/Workers/headers/caching only. Design decisions stay here.

## Quality bar (release)

PASS / FAIL / BLOCKED only.

- Browser — interactions work, no console-breaking errors on the happy path, phone and desktop layout hold.
- Visual — distinct type pairing, real hierarchy, imagery or designed stand-ins, motion present.
- A11y floor — keyboard, focus, labels, contrast AA, alt text.
- Perf floor — LCP image not lazy, CLS reserved, INP-friendly handlers.
- Integrity — no invented verses, testimonials, or schema facts.

Journey pages still run CDSJ `scripts/audit_html.py` when that repo is the work root.
