# Quality Gates

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-08-21 -->

Use only the gates relevant to the artifact. A gate may produce PASS, FAIL, or BLOCKED with a concise reason and next correction.

**Run the loop yourself first.** The agent owns the check → critique → fix cycle before the human sees anything: run the relevant gates, then critique/audit and iterate (see `design-critique-and-anti-slop.md` iteration verbs — evaluate, refine, harden) until the artifact is genuinely strong. Aim for **loop until amazing**, not until acceptable. Hand the human direction-level and taste decisions, not mechanical errors or gate failures they must catch — the agent does the checking, testing, and rechecking; the human feedback loop steers and signs off.

**Page builds:** the **Automatic page-build contract** in `web-experience.md` is mandatory on every “build a page / Scripture Journey page” request. Treat broken interactions, missing verification, system-font shells, and premature canonical writes as gate failures.

## 1. Integrity gate

- The promise is true and deliverable.
- Evidence, quotations, translations, analytics, outliers, testimonials, and citations are not invented.
- Emotion serves meaning rather than manipulation.
- No fear escalation, guilt, shame, coercion, false urgency, deceptive certainty, sensationalism, or manufactured suspense.
- Facts, interpretation, application, and speculation are distinguished where needed.
- Scripture-first reasoning is preserved; modern consensus, popularity, or institutional acceptance is not used as proof.
- Every material lexical, historical, cultural, translation, doctrinal, quotation, or external factual claim has a traceable source, with inline support and complete end references.
- Imagery respects the absolute content boundary.

## 2. Source alignment gate

- The canonical source repository and exact snapshot are recorded.
- The pinned registry was read before source-dependent work.
- Every referenced human source is approved for the applicable scope; intake and under-review material is not treated as authority.
- Material claims are mapped to Scripture passages and exact source records/locators in an alignment manifest.
- Supplied sources and transcript claims are preserved; added corroboration does not replace them.
- Expansions are rooted in Scripture, Spirit of Prophecy, or traceable scripturally aligned reasoning and labeled by claim type.
- Apparent contradictions among applicable approved sources are recorded and the affected claim is `BLOCKED` until resolved or honestly qualified.
- SQLite results are treated as a searchable generated view and verified against canonical records when wording or locators matter.

## 3. Planning gate

For substantial production:

- canonical brief exists;
- audience, core question, why-care, promise, payoff, and truth boundaries exist;
- evidence and learning plans exist;
- a substantive journey identifies learner jobs first, then selects the smallest effective pattern set (normally 2–5), with placement, learner action, feedback/payoff, and accessible fallback;
- visual direction and interaction plan exist;
- new HTML build status is `approved-for-build`;
- downstream artifact inherits locked decisions.
- approval to draft has not been misreported as approval of the draft; unaccepted agent choices remain candidates.

## 4. Learning/content gate

- A useful known anchor leads toward one new idea.
- Scaffolding has no unexplained leap.
- Chunks have distinct purposes and manageable load.
- Signals make the path visible.
- Progressive disclosure does not conceal core content.
- Each major segment adds evidence, clarity, or a payoff.
- The promised primary payoff is explicit.
- Reading level is simple without talking down to adults.
- Every selected learning pattern performs a real and non-duplicative learning job; the mix fits this question instead of repeating a house template.
- At least one selected pattern supports access or learner agency, and active participation is present when the evidence can be inspected honestly.
- Feedback explains from evidence rather than relying on color, correctness labels, points, streaks, or celebration.
- Equivalent modalities carry the same claims, citations, and interpretive boundaries; learners are not assigned fixed learning-style labels.
- Website copy follows a named writing-strategy mix (`learning-and-writing.md`); conversion copy is short punch, not YouTube 80–110.
- Candidate public sentences stand on their own for splicing (`youtube-planning.md`).

## 5. Visual gate

- Proximity/grouping, figure-ground, and continuity/eye path are intentional.
- Hierarchy survives grayscale.
- Focal point and grouping survive squint/phone-size view.
- Type, color, imagery, and composition arise from the content/visual DNA.
- **Web fonts are designed faces** (network or self-hosted WOFF2), not system-only stacks; avoid Inter/system-default as the whole personality unless the brief demands it.
- Page does not read as generic AI slop (see `design-critique-and-anti-slop.md`).
- For layout/placement work: a dynamic-symmetry ratio/armature was considered (soft standard); grid choice recorded when used; pack path preferred over inventing thirds-only habits.
- No nude/sexually explicit reference imagery used in deliverables.
- Color is not the only signal; persistent words, shape, icon, pattern, or position carry the same meaning.
- Every chosen color has a content role, intended viewer response, plausible alternate reading, and evidence strength grounded through repository-root `COLOR-PSYCHOLOGY.md`.
- Scripture color symbolism is verified from the actual passage/context and is never used as doctrinal proof or fear pressure.
- Text remains easily readable at final size and viewing conditions: 7:1 body/sustained-reading target when practical; WCAG 2.2 AA is the floor; gradients, transparency, imagery, video, and states are tested at their worst point.
- Any approved artistic low-legibility exception is nonessential and has an accessible, easily readable equivalent.
- Thumbnail is legible in a feed and against dark surroundings.
- Motion is purposeful and present in the **default** experience; optional `prefers-reduced-motion` accommodation does not define the design.
- Design fingerprint does not repeat recent work without reason.

## 6. YouTube gate

- Idea and packaging are distinguished.
- Title opens one honest gap and the content closes it.
- The requested v3 ideation mode was honored: Quick (~24–32), Standard (~36–48 default), Full Matrix (17×4 = 68), or Deep (~80–120).
- Standard mode includes broad strong-fit coverage plus a deliberate minority of unusual/weak-fit categories rather than pruning them automatically.
- Full Matrix mode still follows the YouTube Video Planner v1.1.1 17-category set exactly.
- Phase 1 packaging file order is: Packaging Report → **What the Episode Is Really About** (content primer first) → Title Options (summary present and above titles; grounded in transcript, user idea, or honest from-scratch synopsis).
- Descriptions run only for **selected** titles (`~` at end of line or explicit list), one description each, grounded in the episode summary + that title.
- `~` marks are preserved when the agent edits the packaging file.
- “More titles like my picks” produces a small add-on set (not a silent full re-matrix) unless the user asked to regenerate everything.
- Thumbnail complements rather than repeats the title.
- Description follows the chosen package and is 80–110 words, aiming at 95–105.
- Opening confirms the package immediately.
- One goal, visible progress, nested payoffs, and a real ending exist.
- Retention tactics do not delay value or fake stakes.

## 7. Technical web gate

**Primary (must pass — beauty and function):**

- Page **opens and works** in a real browser: no broken layout, no dead primary controls, no console-breaking errors on the designed path.
- Designed interactions (scroll journey, map/trail, order game, branching, sticky UI, etc.) function as specified.
- Heading outline, landmarks, links, buttons, forms, media alternatives, focus, keyboard use, zoom/reflow, and contrast are sound.
- CSS is responsive and derived from the visual direction; web fonts load (network fonts allowed).
- Metadata and JSON-LD (if present) match visible content.
- Every cited passage received a review opportunity beginning with KJV, NLT, CSB, WEB, and NASB at minimum; the approved version is recorded per passage or for an explicitly approved larger scope.
- Scripture translation labels, inline citations, and end references are present and traceable.
- Agent opened the page and exercised interactions before claiming complete (or stated that browser verification was impossible).

**Secondary (do not gut the design to chase these):**

- Study text and citations remain in the HTML source where practical.
- Optional `@media (prefers-reduced-motion: reduce)` simplifies nonessential motion—never the main design language.
- No-JS / no-CSS smoke checks are optional diagnostics, **not** release blockers and **not** reasons to strip fonts, motion, or interactive journey features.

## 8. Experience/release gate

- The first screen/seconds confirm the promise and feel **premium**, not template-generic.
- There is one obvious primary question or goal.
- Progress feels real rather than decorative.
- Typography, palette, composition, imagery, interaction, and motion fit the subject and hit Class-A agency quality.
- The experience avoids repetitive templates (including cream-paper + Inter/Fraunces defaults) and unnecessary friction.
- The ending resolves the promise and opens a sincere next curiosity.
- Iterative drafts for **all** agent work products (HTML, prompts, packaging, pass notes) used `name_<agent>_vN`; bare canonical names only after the user chose that deliverable (or small fix to an already-promoted file).
- The requested artifact is complete at its current scope; unresolved dependencies (missing art files, etc.) are named rather than hidden.

<!-- Agent: grok · Model: Grok 4.6 · Date: 2026-08-20 · website copy + splice-safe content gate -->

<!-- Agent: Codex · Model: GPT-5 · Thinking: not exposed · Date: 2026-09-09 · Added color-psychology and readable-text gates. -->
