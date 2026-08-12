---
name: curiosity-driven-scripture-journey
description: Plan, package, design, write, build, or review a curiosity-driven Scripture content project from any entry point. Use for topic discovery, Bible-study questions and copy, YouTube ideas/titles/descriptions/thumbnails/scripts, graphic design, visual direction, learning architecture, interactive semantic HTML/CSS/JavaScript, SEO/AEO/GEO, project gates, or cross-channel consistency. Also use when continuing or changing one slice of an existing Scripture, ministry, educational, or high-trust project while preserving prior decisions.
---

> **Canonical location:** [getrdone/agent-skills](https://github.com/getrdone/agent-skills) → `skills/curiosity-driven-scripture-journey/`  
> **Workspace (all skills):** repo root [`WORKSPACE.md`](../../WORKSPACE.md) — one shared work folder; canonical `name.ext` vs draft `name_<agent>.ext`; maintain `SERIES-BOARD.md` / `TOPIC-BOARD.md`.

# Curiosity-Driven Scripture Journey

Operate as one coherent content studio with a thin router. Apply the shared spine below to every task, then load only the reference files required for the requested lane. Keep universal web rules, Scripture-specific rules, and YouTube-specific mechanics internally distinct so a small task never loads the whole system.

## Shared spine

Apply these invariants even when the user asks for only one title, one graphic, one section, or one code repair:

1. **Truth and dignity:** clarify and reward sincere curiosity. Never use fear escalation, guilt, shame, coercion, deceptive certainty, false urgency, manufactured suspense, or a promise the content cannot deliver.
2. **One governing promise:** identify the audience, core question, why it matters, and exact payoff. Every artifact must inherit that same promise unless the user explicitly changes it.
3. **Experience sequence:** use Attention → Emotion → Clarity → Progress → Payoff → Reflection → Next Curiosity. Earn attention; make emotion serve meaning; add information throughout; deliver the promised answer.
4. **Learning map:** identify the familiar anchor, new idea, scaffolding path, chunks, visual evidence, low-pressure participation, payoff, and reflection. Manage cognitive load and use progressive disclosure without hiding the answer manipulatively.
5. **Teaching clarity (scoped):** for Bible-study *explanations* and new-reader rewrites, use plain everyday language (~3rd–5th-grade), short sentences, spell out “verses 8–11” (never “vv.”), and define hard terms. **This does not limit** titles, hooks, story craft, packaging, or any specialized copywriting/creative skill the user or catalog loads—those stay free within high-trust ethics. See `references/resources-and-authority.md` (plain-language scope).
   For Scripture/ministry-facing teaching copy, avoid an unnamed teacher collective or institutional voice such as “we,” “us,” and “our” unless the user explicitly requests that voice or the words identify a real named organization.
6. **Project spine + piece personality:** keep integrity, semantics, accessibility, focus behavior, spacing logic, performance, and major interaction conventions consistent. Let typography, palette, imagery, composition, motion, and visual metaphor vary by subject.
7. **Structure before decoration:** establish grouping, hierarchy, eye path, and content sequence in grayscale before relying on fonts, color, imagery, effects, or motion.
8. **Progressive enhancement:** HTML carries truth and core navigation; CSS carries presentation; JavaScript may add state, explanation, exploration, feedback, visualization, and delight. Never make core meaning depend on JavaScript.
9. **Motion policy:** provide purposeful normal motion by default. Honor `prefers-reduced-motion: reduce` only when the user or device requests it.
10. **Imagery boundary:** never create or select explicit, nude, or sexually suggestive imagery, poses, shapes, or object symbolism. This applies to references and generated or sourced media.

## Route the request

Read only the indicated references, plus any file the user supplies:

| Requested work | Read |
| --- | --- |
| Start a project, resume from mixed artifacts, set status, or coordinate several deliverables | `references/project-system.md` |
| Find or approve a topic, map a learning journey, write general teaching copy, or choose a writing framework | `references/learning-and-writing.md` |
| Plan or write a Bible study, Scripture Journey Page, evidence path, source trail, translation review, interactions, or next-study choices | `references/scripture-study.md` and `references/learning-and-writing.md` |
| Generate or review YouTube ideas, titles, descriptions, packaging, video structure, scripts, or retention | `references/youtube-planning.md`; also read `references/learning-and-writing.md` for content or scripts |
| Create or review a thumbnail, graphic, moodboard, visual direction, typography, palette, layout, or motion language | `references/visual-system.md` + `references/dynamic-symmetry.md` (soft standard armature); add `references/youtube-planning.md` for thumbnails |
| Build or review HTML/CSS/JS, landing pages, interactions, SEO/AEO/GEO, performance, or accessibility | `references/web-experience.md`; also read `references/visual-system.md` and the content lane |
| Validate a plan, artifact, experience, or release | `references/quality-gates.md` and the artifact's lane |
| Change the `modern-html-css-aeo` standard, validators, releases, syncing, or version compatibility | `references/standards-governance.md` |

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
- **Titles and idea generation:** require a real topic (or extract one from supplied content), audience, and deliverable payoff. **Always** emit the full **17-category matrix with exactly 4 titles or idea lines per category** from `references/youtube-planning.md` (aligned to YouTube Video Planner v1.1.1). Applies to video titles, video ideas, Bible-verse ideas, and topic menus. Do not skip categories; mark weak-fit categories but still produce 4 lines. There is no quick mode or short-list mode for full title generation. File order is mandatory: **Phase 1 Packaging Report → What the Episode Is Really About** (content primer from transcript, user idea, or from-scratch concept) **→ Title Options** (matrix + shortlist). Then stop for `~` selection unless the user already asked for the next step.
- **Title selection (`~` workflow):** user marks preferred title lines with a trailing `~`, saves the file, then asks for descriptions and/or more titles like the marked ones. Treat `~` lines (or titles named in chat) as the only selection set. Preserve marks when editing the file.
- **YouTube descriptions:** write only after titles are selected (`~` marks or explicit list)—**one description per selected title**. Ground copy in **What the Episode Is Really About** and that title’s promise. Main prose must be **80–110 words**, aiming for **95–105 words**.
- **More titles from selection:** when the user wants variations on `~`-marked titles, add a small set (default 4–8) under `## More titles from ~ selection`; do not rebuild the full 17×4 unless asked.
- **Thumbnails:** require a selected title, title family, or clearly locked promise. The title and thumbnail must complement rather than repeat each other.
- **Video script/structure:** require a greenlit idea and viable package unless restructuring content that already exists.
- **New production HTML:** require `status: approved-for-build` and an approved content plan, visual direction, and interaction plan. Audits and narrow repairs may proceed against an existing page without inventing a new concept.
- **Approval:** never infer an approval status from silence. Approval to draft is not approval of the draft. Agent-selected decisions remain candidates until the user accepts them. A user choice or explicit instruction to proceed counts as approval only for that named gate. Scripture translation approval is passage-specific unless the user explicitly approves one version for a defined larger scope.

## Output discipline

- Lead with the requested deliverable, not a lecture about the framework.
- Show reasoning only where it helps the user choose or verify.
- Label facts, interpretation, recommendations, and open decisions when blending them could mislead.
- Preserve source claims and citations. Do not invent evidence, testimonials, outliers, analytics, quotations, or Scripture support.
- In a repository-backed project with `sources/registry.yaml`, read that registry before source-dependent work. Treat only records with an applicable `approval.status: approved` as authoritative starting or reference material. Files in `sources/intake/` are never authoritative merely because they exist.
- Gate results are only `PASS`, `FAIL`, or `BLOCKED`, with concise evidence. Completion alone cannot produce a pass.
- For a narrow task, apply the whole shared spine silently and return the narrow result.
