---
name: curiosity-driven-scripture-journey
description: Plan, package, design, write, build, or review a curiosity-driven Scripture content project from any entry point. Use for topic discovery, Bible-study questions and copy, source-library ingestion and alignment, source databases, YouTube ideas/titles/descriptions/thumbnails/scripts, graphic design, visual direction, learning architecture, interactive semantic HTML/CSS/JavaScript, SEO/AEO/GEO, project gates, or cross-channel consistency. Also use when continuing or changing one slice of an existing Scripture, ministry, educational, or high-trust project while preserving prior decisions.
---

## Version 3.2.0 workflow override

For substantial new Scripture Journey work, **develop the journey before building the experience**. Load `references/v3-workflow.md` before project planning, ideation, learning architecture, visual direction, or HTML production. Load `references/v3-quality.md` before reviewing or releasing a page.

Version 3.2.0 preserves the v3 workflow and consolidates the former web helper skills into the routed Scripture Journey web lane. It intentionally changes these legacy defaults:

- Broad ideation remains valuable, but the full 17×4 (68) matrix is no longer mandatory for every request. Use Quick, Standard, Full Matrix, or Deep mode as defined in v3-workflow; Standard is the default and remains deliberately broad, including some weak-fit territory.
- After the user selects favorites, synthesize why they work and generate hybrid/refined ideas rather than merely synonyms.
- Learning architecture starts with **learner jobs**; select the smallest effective set of learning patterns rather than satisfying a fixed pattern-family quota.
- A substantial new page normally requires an approved Journey Concept before production HTML. The user may explicitly bypass or compress this gate.
- The design pipeline must develop multiple credible experience concepts when the direction is unresolved, then iterate through independent critique/revision loops until mechanical defects are fixed and the experience reaches the requested quality class.
- Existing Hell Journey and Psalm 23 generations are regression/failure examples only, not positive benchmarks.
- Every color choice now follows the repository-root `COLOR-PSYCHOLOGY.md`: intended and alternate meanings, audience/cultural/Scripture context, lightness/chroma/area effects, evidence strength, non-color cues, and independently validated text pairings.
- WCAG AA/AAA accessibility and Experience Class A/AA/AAA craft are separate axes. Normal release minimum is WCAG 2.2 AA and Experience Class AA for substantial pages.
- Run the deterministic v3 HTML audit before candidate delivery. It is a mechanical floor, not a beauty score.
- Do not introduce SQLite project-state storage in 3.0.0. Keep the current file-based project system while minimizing Markdown note sprawl.


> **Canonical location:** [getrdone/agent-skills](https://github.com/getrdone/agent-skills) → `skills/curiosity-driven-scripture-journey/`
> **Path resolution:** every relative path in this file resolves under `versions/3.2.0/`. Paths written `repo:` resolve from the repository root.
> **Workspace (all skills):** file naming, file I/O, and continuity are defined **only** in repo root [`WORKSPACE.md`](../../../../WORKSPACE.md). This skill does not restate them.

# Curiosity-Driven Scripture Journey

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-08-21 -->

Operate as one coherent content studio with a thin router. For Scripture, ministry, educational, or other high-trust journey work, this skill owns the page architecture, CSS, interaction, accessibility, performance, and SEO/AEO route; do not load retired generic web helper skills alongside it. Apply the shared spine below to every task, then load only the reference files required for the requested lane. Keep universal web rules, Scripture-specific rules, and YouTube-specific mechanics internally distinct so a small task never loads the whole system.

## Shared spine

Apply these invariants even when the user asks for only one title, one graphic, one section, or one code repair:

1. **Truth and dignity:** clarify and reward sincere curiosity. Never use fear escalation, guilt, shame, coercion, deceptive certainty, false urgency, or a promise the content cannot deliver. **Manufactured suspense** (generic reaction bait, stacked opaque teasers, unsupported insinuation, empty trailer language) is forbidden. **Honest curiosity gaps** are required packaging: titles, thumbnails, and pre-click copy may reserve the exact reveal when the topic, stakes, and kind of payoff are recognizable and the content fully delivers the answer. Teaching copy must still confirm the promise, give evidence early, and state the answer plainly. Full reject standard: `references/youtube-planning.md` → Honest curiosity vs manufactured suspense.
2. **One governing promise:** identify the audience, core question, why it matters, and exact payoff. Every artifact must inherit that same promise unless the user explicitly changes it.
3. **Experience sequence:** use Attention → Emotion → Clarity → Progress → Payoff → Reflection → Next Curiosity. Earn attention; make emotion serve meaning; add information throughout; deliver the promised answer. This sequence is a **buffet, not a hard order** — vary which beats appear, their order, and their emphasis per piece and per section so nothing feels formulaic; keep the variation deliberate and in-family so it never becomes a pattern interrupt.
4. **Learning map:** identify the familiar anchor, new idea, scaffolding path, chunks, visual evidence, low-pressure participation, payoff, and reflection. Manage cognitive load and use progressive disclosure without hiding the answer manipulatively. For a substantive Scripture Journey, identify learner jobs first, then select the smallest effective set of named learning patterns (normally 2–5) from `references/learning-patterns.md`; each pattern must perform a distinct learning job and preserve an accessible equivalent.
5. **Teaching clarity (scoped):** for Bible-study *explanations* and new-reader rewrites, use plain everyday language (~3rd–5th-grade), short sentences, spell out “verses 8–11” (never “vv.”), and define hard terms. **This does not limit** titles, hooks, story craft, packaging, or any specialized copywriting/creative skill the user or catalog loads—those stay free within high-trust ethics. See `references/resources-and-authority.md` (plain-language scope).
   For Scripture/ministry-facing teaching copy, avoid an unnamed teacher collective or institutional voice such as “we,” “us,” and “our” unless the user explicitly requests that voice or the words identify a real named organization.
6. **Project spine + piece personality:** keep integrity, semantics, accessibility, focus behavior, spacing logic, performance, and major interaction conventions consistent. Let typography, palette, imagery, composition, motion, and visual metaphor vary by subject.
7. **Structure before decoration:** establish grouping, hierarchy, eye path, and content sequence in grayscale before relying on fonts, color, imagery, effects, or motion.
8. **HTML + CSS + JS as one craft:** semantic HTML holds study truth and citations; CSS holds premium presentation (including **network webfonts**—not system-only); JavaScript is first-class for journey interaction, scroll storytelling, state, and delight. Do not strip fonts, motion, or JS to satisfy a no-JS purity test. Broken interactions are a fail.
9. **Motion policy:** full purposeful motion is the default design. Optional `@media (prefers-reduced-motion: reduce)` may simplify nonessential motion—never design the main experience as reduced-motion.
10. **Imagery boundary:** never create or select explicit, nude, or sexually suggestive imagery, poses, shapes, or object symbolism. This applies to references and generated or sourced media.
11. **Canonical source alignment:** use the private `getrdone/bible-study-source-materials` repository as the source of truth for approved source records. Pin the library snapshot used by a substantive study, preserve supplied sources, and block unresolved contradictions rather than silently harmonizing them.
12. **Readable text is non-negotiable:** whenever text carries meaning, easy reading outranks mood, palette, texture, imagery, and artistic flourish. Target 7:1 contrast for sustained reading when practical; never fall below WCAG 2.2 AA. Low-legibility text is allowed only for an explicitly approved artistic effect and can never be the only copy of essential teaching, Scripture, navigation, form, control, or safety content.

## Route the request

`load-map.yaml` beside this file is the machine-readable form of this table, with per-lane file
budgets and the conditional loads. Match the request, emit `LANES:` and `LOAD:` (see the router
`SKILL.md`), then read **only** what you declared, plus any file the user supplies.

| Requested work | Lane | Read |
| --- | --- | --- |
| Substantial new work — before planning, ideation, learning architecture, visual direction, or HTML | `develop` | `references/v3-workflow.md` |
| Start a project, resume from mixed artifacts, set status, or coordinate several deliverables | `project`  | `references/project-system.md` |
| Find or approve a topic, map a learning journey, write general teaching copy, or choose a writing framework | `study`  | `references/learning-and-writing.md` |
| Choose, combine, implement, or audit learning patterns or teaching strategies | `study`  | `references/learning-patterns.md`, then only the selected pattern-family file(s); read `references/learning-pattern-sources.md` only for provenance or catalog maintenance |
| Ingest, approve, classify, index, query, or audit Bible-study source material or its SQLite database | `sources`  | `references/source-governance.md` |
| Plan or write a Bible study, Scripture Journey Page, evidence path, source trail, translation review, interactions, or next-study choices | `study`  | `references/scripture-study.md`, `references/source-governance.md`, `references/learning-and-writing.md`, `references/learning-patterns.md`, and `references/branching-journey.md`; then load only the selected pattern-family file(s) |
| Generate or review YouTube ideas, titles, descriptions, packaging, video structure, scripts, or retention | `packaging`  | `references/youtube-planning.md`; also read `references/learning-and-writing.md` for content or scripts |
| Create or review a thumbnail, graphic, moodboard, visual direction, typography, palette, layout, or motion language | `visual` | `references/visual-system.md` (which requires repository-root `COLOR-PSYCHOLOGY.md` whenever a color decision is present) + skim `references/dynamic-symmetry-glossary.md` then `references/dynamic-symmetry.md`; for **actual image generation**, load skill **`artwork-prompts-handoff`** (prompts file for human tools—default; no paid Canva/Leonardo APIs unless user explicitly confirms credits); add `references/youtube-planning.md` for thumbnails |
| **Narrow repair** to an existing page — one component, a contrast fix, a broken control | `web.repair` | `references/web-experience.md` only. Do not open the design tree. |
| **Build or rebuild** HTML/CSS/JS, landing pages, interactions, SEO/AEO/GEO, performance, or accessibility | `web.build` | `references/web-experience.md`; also `references/visual-system.md`, `references/motion-and-premium-ui.md`, `references/design-critique-and-anti-slop.md`, `references/branching-journey.md`, and `references/learning-and-writing.md` for on-page copy |
| Validate a plan, artifact, experience, or release | `release` | `references/quality-gates.md`, `references/v3-quality.md`, and the artifact's lane. Run `scripts/audit_html.py` on every substantial HTML candidate. |
| Change the `modern-html-css-aeo` standard, validators, releases, syncing, or version compatibility | `governance`  | `references/standards-governance.md` |

## Continue from any stage

1. Inspect what is already known or supplied. Do not restart completed work.
2. Recover locked decisions from the project brief, selected artifact, or conversation. Ask only for a missing fact that materially changes the requested output.
3. Identify the current lane and nearest dependency. Use existing approved decisions instead of reopening them.
4. Produce the exact slice requested. Do not force a full report when the user asks for a few options or one revision.
5. State assumptions when no project record exists. Preserve approved wording and visual direction unless the user asks to change them.
6. Record newly selected decisions in the project's canonical brief when working in files. In chat-only work, end with a compact **Locked decisions** block only when it helps the next step.
7. Run the relevant gates in `references/quality-gates.md` before calling the slice complete.

## Dependency gates

- **Topic discovery:** when no topic exists, provide a topic menu and stop for selection unless the user explicitly asks for further development in the same turn.
- **Titles and idea generation:** require a real topic (or extract one from supplied content), audience, and deliverable payoff. Use the v3 ideation mode requested by the user, defaulting to **Standard (~36–48 ideas)**. Quick (~24–32), Full Matrix (17×4 = 68), and Deep (~80–120) remain available. Standard mode deliberately includes some unusual/weak-fit territory. When Full Matrix is selected, follow `references/youtube-planning.md` exactly. Apply **Honest curiosity vs manufactured suspense** (What not to do) before writing any title line. File order is mandatory: **Phase 1 Packaging Report → What the Episode Is Really About** (content primer from transcript, user idea, or from-scratch concept) **→ Title Options** (matrix + shortlist). Then stop for `~` selection unless the user already asked for the next step.
- **Title selection (`~` workflow):** user marks preferred title lines with a trailing `~`, saves the file, then asks for descriptions and/or more titles like the marked ones. Treat `~` lines (or titles named in chat) as the only selection set. Preserve marks when editing the file.
- **YouTube descriptions:** write only after titles are selected (`~` marks or explicit list)—**one description per selected title**. Ground copy in **What the Episode Is Really About** and that title’s promise. Main prose must be **80–110 words**, aiming for **95–105 words**. Candidate sentences follow **Splice-safe sentences + short punch** and **Honest curiosity vs manufactured suspense** (What not to do) in `references/youtube-planning.md`. The extra gap must be a named remaining beat, not a reaction or trailer closer.
- **Website / landing copy:** do **not** apply the YouTube 80–110 word rule. Conversion surfaces (H2 support, blurbs, form leads) use **short punch**. Follow a named mix from `references/learning-and-writing.md` Writing strategy router so the reader wants to keep learning or complete the page job. Every candidate sentence stands on its own (`references/youtube-planning.md` Splice-safe sentences + short punch).
- **More titles from selection:** when the user wants variations on `~`-marked titles, add a small set (default 4–8) under `## More titles from ~ selection`; do not rebuild the full 17×4 unless asked.
- **Thumbnails:** require a selected title, title family, or clearly locked promise. The title and thumbnail must complement rather than repeat each other.
- **Video script/structure:** require a greenlit idea and viable package unless restructuring content that already exists.
- **New production HTML / “build me a page” / Scripture Journey page:** require `status: approved-for-build` (or an explicit user build order that locks the same scope) plus content, visual, and interaction direction. Then apply the **Automatic page-build contract** in `references/web-experience.md` in full—write `deliverables/index.html`, network fonts, full motion, working JS, art prompts + complete CSS without waiting for pixels, browser verification with FAIL on dead interactions, mood/references, gate loop until strong. The user does not need to restate those rules. Audits and narrow repairs may proceed against an existing page without inventing a new concept.
- **Approval:** never infer an approval status from silence. Approval to draft is not approval of the draft. Agent-selected decisions remain candidates until the user accepts them. A user choice or explicit instruction to proceed counts as approval only for that named gate. Scripture translation approval is passage-specific unless the user explicitly approves one version for a defined larger scope.

## Output discipline

- Lead with the requested deliverable, not a lecture about the framework.
- Show reasoning only where it helps the user choose or verify.
- **Lean to the user (Steve).** Prefer high information density and short responses. Avoid long explanatory preambles, repeated framework summaries, or filler. When the CLI or any agent produces verbose output, compress to the essential result. Match the lean-output skill principles.
- **Expanded for the actual reader.** Scripture Journey pages, study text, and other teaching body copy must be expanded, interesting, and conversational — written like a thoughtful person composing for someone else. It must never feel like a dry “fact → quote → fact” sequence. Mix writing strategies from `references/learning-and-writing.md` so the reader wants to keep going. **Landing / conversion copy is the exception:** use **short punch** (a few tight sentences), not a YouTube-length explainer. All candidate sentences remain splice-safe. Still obey the core voice rule: do not use “we / us / our” as if the writer is sitting beside the reader.
- Label facts, interpretation, recommendations, and open decisions when blending them could mislead.
- Preserve source claims and citations. Do not invent evidence, testimonials, outliers, analytics, quotations, or Scripture support.
- Before source-dependent work, resolve the consumer project's source-library lock and read the pinned `getrdone/bible-study-source-materials` registry. Treat only records with an applicable `approval.status: approved` as authoritative starting or reference material. Intake files and the generated SQLite database are never independently authoritative.
- Gate results are only `PASS`, `FAIL`, or `BLOCKED`, with concise evidence. Completion alone cannot produce a pass.
- For a narrow task, apply the whole shared spine silently and return the narrow result.
- Descriptions, emails, and pre-click copy may keep the title’s gap plus **one additional, grounded reason to click** (a named remaining scene, stake, question, or kind of payoff — not “what he did next surprised him,” “then everything shifts,” or other reaction/trailer language). Support dual-audience design (early CTA for skimmers + continued tension for engaged readers). Vary structure deliberately so pieces do not feel formulaic. The gap must never **leak** the payoff the title/episode promises — apply the leak test and **Honest curiosity vs manufactured suspense** in `references/youtube-planning.md`. Website copy must follow the writing-strategy router; conversion copy uses short punch.
- **Proofread every pass.** After every change to public-facing copy — titles, descriptions, emails, page text — re-read and fix spelling, grammar, subject–verb agreement, punctuation, and typos. This includes the user's own final “approved” text: correct obvious mechanical errors rather than copying them through, and never finalize copy that still contains them.
- Every generated file carries an execution-identity stamp and, on later edits by a different agent/model/thinking level, an appended stamp line. Exact fields and format: repo root `WORKSPACE.md` §5.

<!-- Agent: grok · Model: Grok 4.6 · Date: 2026-08-20 · splice-safe + short punch + website writing-strategy mix -->

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-08 | Released 3.1.0 consolidated routing. -->

<!-- Agent: Codex · Model: GPT-5 · Thinking: not exposed · Date: 2026-09-09 · Released 3.2.0 color psychology and text-readability requirements. -->
<!-- Agent: grok · Model: Grok 4.6 · Date: 2026-09-09 · Honest curiosity vs manufactured suspense: packaging may keep a real gap; teaching may not delay the answer. -->
<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 2026-09-10 · Route table gains lane names, the develop and release rows, and a narrow web.repair door; naming and stamping rules point at WORKSPACE.md. -->
