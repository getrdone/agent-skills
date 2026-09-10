# Web Experience Build Standard

Use this file to plan, build, repair, or review semantic HTML/CSS/JavaScript experiences and landing pages.

**Quality target (wins):** The finished page must reach the level of a highly polished Class-A design and coding agency (Apple-website caliber)—visually stunning, fully working, and interactive. High-end purposeful motion and JS are **desired**, not optional extras. Content integrity rules still apply. If a content rule would force a flat, broken, or system-font page, **do not silently degrade beauty**—note the tension and still ship a premium working experience unless the user ordered a constrained build.

**Priority order when agents over-constrain themselves:** (1) works in a real browser, (2) looks premium, (3) interactions and motion land, (4) semantic structure + keyboard, (5) optional accommodations. Never optimize for (5) at the cost of (1)–(3).

## Automatic page-build contract (REQUIRED — no special user wording)

When the user asks to **build a Scripture Journey page**, **build a page**, **build the HTML**, **rebuild the page**, or any equivalent production HTML request, apply **all** of the following automatically. The user does **not** need to restate fonts, motion, JS, verification, naming, art order, or promote rules.

1. **Naming.** A built page is a deterministic deliverable: write the canonical name on the first pass — `deliverables/index.html`, `prompts/artwork-prompts.md`, `planning/gate-results.md`. Iterate in place. Full rules, including the bake-off exception when the user asks two agents for rival designs: repo [`WORKSPACE.md`](../../../../WORKSPACE.md) §3.
2. **Art path is automatic.** If the design needs pixel art and assets are missing: write or update the prompts pack via skill **artwork-prompts-handoff**; wire expected filenames under `deliverables/assets/`; **still ship a complete, beautiful page** using CSS/SVG/gradients so missing JPGs do not leave a broken or empty layout. When `mood/` or existing assets exist, use them. Stage/hero backgrounds must use `background-size: cover` + `background-repeat: no-repeat` (never the `background:` shorthand for fallbacks — it reintroduces tiling).
3. **Working bar is a hard FAIL.** Console-breaking errors, dead primary controls, non-functional map/trail/game/scroll interactions, or collapsed phone/desktop layout = FAIL. Loop: build → open in browser → exercise every interaction → fix → re-check until the designed experience works.
4. **Craft level is automatic.** Treat interactive HTML as premium agency work (network fonts, full motion, first-class JS, anti-slop). Do not ship cream-paper + Inter/system defaults or static shells with half-wired scripts.
5. **References and mood.** Read `mood/`, visual direction, brief, and any human reference images before inventing a new look. Match craft level of strong references when present.
6. **Protect an accepted page before a destructive rewrite.** Iterating on the working file is normal and expected. But if the page has already been accepted or deployed and the next pass would replace its structure, snapshot it first as `index_v2.html` (WORKSPACE §3b `_vN` snapshot), then rewrite the canonical file.
7. **Gates + self-loop.** Run the visual, technical, integrity, learning, and experience gates; iterate (critique → fix) until the page is genuinely strong—not merely “acceptable.” Hand the human taste/direction decisions, not broken mechanics.
8. **Handoff.** Update `NOW.md` (Now / Next / Blocked) and `planning/gate-results.md` with the page path, what was verified, and what still needs human art. If a `SERIES-BOARD.md` already exists in the folder, add a row; do not create one.

## Preconditions

- For a new build, require a content-approved brief, visual direction, interaction plan, and `status: approved-for-build`.
- For an existing page audit or narrow repair, preserve the current approved concept and fix the requested problem without inventing a new one.
- Reuse the project’s chosen title, promise, learning map, visual DNA, and design fingerprint.
- **File naming:** repo [`WORKSPACE.md`](../../../../WORKSPACE.md) §3. Do not restate naming rules in a project folder.

## Build sequence

1. Confirm the page’s one primary question/action and visible payoff.
2. Lock visual DNA (type pairing, palette, composition, motion character)—not a beige default.
3. Write complete semantic HTML for the content path (truth stays in the document).
4. Add metadata/discoverability that match visible content.
5. Implement **full** layout, web fonts, imagery slots, CSS, and JavaScript for the designed experience.
6. Open the page in a real browser; exercise every interaction; fix until it works.
7. Only then: keyboard pass, phone width, and optional `prefers-reduced-motion` media-query check.
8. Run integrity, learning, visual, technical, and experience gates—**working beauty first**.

## HTML foundation

- Put headings, passages, answers, evidence, links, forms, and core navigation in semantic HTML.
- Use landmarks, one coherent heading outline, lists/tables/figures where structurally correct, and meaningful link/control labels.
- Keep source order coherent.
- Primary study text and citations should exist in the HTML document (not only injected by JS). Interactive chrome (maps, trails, games, scroll storytelling, ordering exercises) **may require JavaScript**—that is correct for a journey page. Design the full interactive experience; do not gut it to pass a no-JS purity test.
- For a Scripture Journey Page, place traceable inline citations beside the claims they support and include compact semantic end matter for passages/translations, references, further reading, and external links. Native `<details>`/`<summary>` may organize supporting detail but never hide the core answer or required evidence.
- During review, every cited verse or passage must expose an accessible comparison beginning with KJV, then NLT, CSB, WEB, and NASB at minimum. Preserve the reviewer’s per-passage choice; do not force one translation across the page unless explicitly approved for that scope.
- Use buttons for actions and links for navigation.
- Single-file or multi-file is fine. **“Self-contained” does not mean local-only fonts or no network CSS/JS.** Web fonts and small CDNs (fonts, GSAP, etc.) are allowed and preferred when they raise quality.

## Typography and fonts (not system-only)

- **Default: network webfonts.** Use Google Fonts, Bunny Fonts, Fontshare, Adobe Fonts, or self-hosted WOFF2. Pair one distinctive display face with one highly legible body face.
- **Forbidden as the design default:** system UI stacks only, “stock local fonts only,” or Inter/Roboto/Arial as the whole personality. Those are fallbacks in `font-family` stacks, not the face the page is designed in.
- Load fonts with `preconnect` + stylesheet (or `@font-face` WOFF2); include sensible fallbacks after the designed faces.
- Extreme scale contrast, fluid `clamp()`, and real hierarchy beat safe generic type.

## CSS and design implementation

### Container-query-first architecture

- Components respond to their owning container. Do not use viewport `@media (min-width: …)` rules for component layout.
- Reserve viewport media queries for genuine viewport or user-preference concerns such as print, color scheme, contrast, reduced motion, and root-level application chrome.
- Establish `container-type: inline-size` where component behavior needs it. Start from a narrow, usable base; enhance with `@container`, `cqi`, `clamp()`, logical properties, wrapping, and intrinsic Grid/Flex patterns.
- Prefer resilient tracks such as `repeat(auto-fit, minmax(min(<measure>, 100%), 1fr))` so components do not overflow when moved between page regions.
- Use container queries when behavior depends on available component space; do not add them mechanically when intrinsic layout already solves the problem.

- Tokens come from the approved visual DNA; never paste a finished default aesthetic (especially repeated cream paper + muted sage “ministry template”).
- Favor mobile-first fluid layout, modern grid/flex, `clamp()`, container queries when useful.
- Preserve zoom, text reflow, touch size, visible focus, contrast, and readable measure.
- Reserve space for media and dynamic states to prevent layout shifts.
- Scope component styles clearly; avoid specificity wars.

## JavaScript and motion (first-class)

### Interactive-component implementation order

1. Prefer native HTML and modern CSS primitives such as `details`, `dialog`, popovers, native validation, `:has()`, and container queries when they fully express the interaction.
2. Add focused vanilla JavaScript with event delegation and explicit state when native behavior is insufficient.
3. Use a small specialist library only when its value outweighs its payload and maintenance cost.
4. Use framework components only when the host project already depends on that framework.

Keep ordinary interactions within the Core Web Vitals INP “good” threshold (200 ms), reserve space for dynamic states, and use `aria-live` only for changes that genuinely require announcement.

JavaScript is a **primary tool** for Scripture Journey pages when the brief calls for maps, scroll progress, ordering games, branching state, sticky journey UI, or delight.

- Build and verify the **with-JS** experience first. Broken or half-wired JS is a FAIL.
- Prefer small, reliable patterns (vanilla or GSAP/ScrollTrigger per `motion-and-premium-ui.md`) over cargo-cult progressive-enhancement that ships nonfunctional controls.
- Keep controls keyboard-operable where they are buttons/links/inputs.
- Avoid huge unused libraries; paid APIs still need explicit user OK.
- **Motion default = full purposeful motion** (scroll reveals, trail lighting, transitions, micro-interactions). Design for users who allow motion.
- `prefers-reduced-motion: reduce` is an **optional media-query accommodation only**—shorten or simplify nonessential motion inside that query. **Never** design the main page as if reduced-motion were on. Never remove hero motion globally “to be safe.”

## Accessibility and performance

Floor, not ceiling—do not use these to justify bland pages:

- keyboard order, focus visibility, skip link, labels, contrast, zoom/reflow, alt text, non-color cues;
- image dimensions, lazy-load below the fold, font subset/weight discipline, layout stability;
- fast feedback; no effect that blocks reading the answer.

## Mandatory browser verification

Before calling any HTML pass complete:

1. Open the file (or local server) in a browser.
2. Click/scroll/type every designed interaction.
3. Confirm no console-breaking errors on the happy path; layout holds at desktop and phone widths.
4. If verification is impossible in the environment, say so explicitly—do not claim “works.”

## SEO, AEO, and GEO

- Provide a unique descriptive title, meta description, canonical URL when known, index directives, language, social metadata, and meaningful headings.
- Make the question, answer, evidence, entities, definitions, and relationships explicit in visible prose.
- Add appropriate JSON-LD only when it matches the page type and visible content. Never fabricate reviews, authorship, dates, FAQ entries, or organizational facts.
- Use concise answer-first passages where they improve comprehension; preserve nuance and source context.
- Add citations/links to authoritative sources and identify exact Scripture translations/editions and historical documents as needed.
- Keep essential answers crawlable in initial HTML.

## Interaction and conversion

- Let interaction teach, orient, compare, or invite reflection; do not use dark patterns.
- Keep a primary action clear without hiding the study behind a form.
- Ask for contact information only with a truthful, concrete value exchange and clear consent.
- Preserve the learner’s ability to finish or continue without pressure.
- **Copy:** follow `learning-and-writing.md` **Writing strategy router**. Pick one pattern or mix them in body copy so the reader wants to keep learning or complete the page job (form, watch, continue). Conversion blurbs and form leads are **short punch**, not YouTube 80–110. Sentences stand on their own for splicing — `youtube-planning.md` **Splice-safe sentences + short punch**.
- When offering the next path, use the approved featured-direct-plus-four-alternates architecture: two more direct continuations, one moderately related question, and one wildcard.

### The next path — presentation (apply always)

The next path is a **continuation**, not a catalog. It reads as one obvious next step pulling the reader forward, plus a few quieter alternative threads — never as five interchangeable options. These rules govern structure and reading order; the visual foundation (light or dark, cinematic or editorial) is chosen per project and per section in the visual DNA, not here.

**Do:**

- **Let one primary path dominate.** The featured continuation is the hero — the largest, clearest element. The reader lands on it first and reads it as a door to step through, not as option #1 of 5.
- **Rank by scale, placement, and whitespace — not by boxes.** Express hierarchy through type scale, size, and position. Avoid five near-identical bordered cards or tiles.
- **Lead with the question or statement; trail with the verse reference.** The reader's first read must be the curiosity gap ("When Shepherds Fail"), then the Bible reference at the end as a quiet receipt ("— Ezekiel 34") — never the other way around.
- **Keep the loop open.** State the question; do not explain or pre-answer it. No clause that reveals the answer's shape before the click.
- **Signal continuation, not termination.** This block says "keep going," so avoid hard section terminators (a heavy rule or dash that reads as "this section ended").

**Don't:**

- **Don't expose the internal taxonomy.** Never label paths FEATURED / DIRECT CONTINUATION / MODERATELY RELATED / WILDCARD for the reader. Those are agent-side categories; the reader should feel the ranking through hierarchy, not read the filing system — and naming the wildcard deflates its surprise.
- **Don't lay the paths out as an equal grid.** A 3-across grid implies interchangeable tiles and kills forward motion; a journey is vertical and sequential.
- **Don't lead with the reference.** "Ezekiel 34 — When Shepherds Fail" puts the anchor before the hook; reverse it.
- **Don't pre-close the gap.** Copy that reveals the answer's shape ("the answer echoes across the entire biblical story") answers the question before the reader can click.
- **Don't default to a generic card-wall.** Whatever the chosen foundation, the section must still produce a dominant focal point and real hierarchy — a beige/white card grid is not a design decision, it is the absence of one.

## Release check

The page is not complete merely because it validates. Confirm that the opening matches the promise, each section adds value, design reflects the subject, motion and interaction help, the primary payoff is explicit, and the next curiosity feels natural.

<!-- Agent: grok · Model: Grok 4.6 · Date: 2026-08-20 · website copy: writing-strategy mix + short punch -->

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-08 | Consolidated useful CSS/component rules and removed competing skill routes. -->

<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 2026-09-10 · Page build writes canonical on first pass; naming rules single-sourced to WORKSPACE.md §3. -->
