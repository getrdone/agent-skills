# Web Experience Build Standard

Use this file to plan, build, repair, or review semantic HTML/CSS/JavaScript experiences and landing pages.

**Quality target:** The finished page must reach the level of a highly polished Class-A design and coding agency (Apple-website caliber). High-end, purposeful interactions are desired. All existing content-generation philosophy and rules still apply. If a conflict appears between the high-end design goal and any content rule, stop and highlight the conflict for the user instead of deciding unilaterally.

## Preconditions

- For a new build, require a content-approved brief, visual direction, interaction plan, and `status: approved-for-build`.
- For an existing page audit or narrow repair, preserve the current approved concept and fix the requested problem without inventing a new one.
- Reuse the project’s chosen title, promise, learning map, visual DNA, and design fingerprint.

## Build sequence

1. Confirm the page’s one primary question/action and visible payoff.
2. Write the complete semantic HTML content path.
3. Add metadata, discoverability, and structured data that accurately describe visible content.
4. Implement layout and design from the approved visual direction.
5. Add CSS/JS interactions as progressive enhancement.
6. Optimize assets, fonts, rendering, and interaction performance from the beginning.
7. Test without CSS, without JavaScript, by keyboard, at zoom, on phone widths, and with reduced motion requested.
8. Run the planning, technical, integrity, learning, visual, and experience gates.

## HTML foundation

- Put headings, passages, answers, evidence, links, forms, and core navigation in semantic HTML.
- Use landmarks, one coherent heading outline, lists/tables/figures where structurally correct, and meaningful link/control labels.
- Keep source order meaningful when styles fail.
- Do not hide primary content behind JavaScript, accordions that require scripting, canvas, or client-only rendering.
- For a Scripture Journey Page, place traceable inline citations beside the claims they support and include compact semantic end matter for passages/translations, references, further reading, and external links. Native `<details>`/`<summary>` disclosure may organize supporting detail but never hide the core answer or required evidence.
- During review, every cited verse or passage must expose an accessible comparison beginning with KJV, then NLT, CSB, WEB, and NASB at minimum. Preserve the reviewer’s per-passage choice; do not force one translation across the page unless explicitly approved for that scope.
- Use buttons for actions and links for navigation.
- Add form labels, instructions, validation messages, autocomplete, appropriate input types, and consent/compliance language.
- Prefer a self-contained HTML/CSS/JS deliverable when the project or hosting model calls for it; do not sacrifice maintainability or caching without reason.

## CSS and design implementation

- Use neutral design tokens derived from the approved visual DNA; never import a finished default aesthetic blindly.
- Keep a predictable class system such as BEM when the project standard requires it.
- Favor mobile-first fluid layout, logical properties, modern grid/flex, `clamp()`, and container queries when component behavior depends on its container.
- Preserve zoom, text reflow, touch size, visible focus, contrast, and readable measure.
- Reserve space for media and dynamic states to prevent layout shifts.
- Scope component styles and states clearly; avoid specificity escalation.

## JavaScript and motion

Use JavaScript when it improves exploration, explanation, feedback, state, visualization, or delight.

- The page’s truth, answer, and primary navigation must still work without it.
- Start from valid server/static HTML and enhance it.
- Keep state understandable and controls keyboard-operable.
- Avoid blocking rendering with unnecessary libraries or large hydration costs.
- Provide purposeful normal transitions/animations by default.
- Inside `@media (prefers-reduced-motion: reduce)`, remove or simplify nonessential motion. Do not assume reduced motion for everyone.

## Accessibility and performance

Plan both before implementation:

- keyboard order, focus visibility, skip navigation, labels, status announcements, contrast, zoom/reflow, error recovery, alt text, captions/transcripts, and non-color cues;
- critical content/render path, image dimensions and formats, lazy loading below the fold, font subsets/weights, caching, third-party cost, DOM size, long tasks, layout stability, and responsive media;
- fast-feeling feedback and no decorative effect that delays the answer or harms input responsiveness.

Measure with current accessibility and Core Web Vitals tooling when available. Treat automated checks as necessary but incomplete.

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
