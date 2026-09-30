# Quality Gates

<!-- Agent: Buffy | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-24 | Added story-craft, source-integrity, delivery, and claim-discipline gates. -->

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-08-21 -->

Use only the gates relevant to the artifact. A gate may produce PASS, FAIL, or BLOCKED with a concise reason and next correction.

**Run the loop yourself first.** The agent owns the check → critique → fix cycle before the human sees anything: run the relevant gates, then critique/audit and iterate (see `design-critique-and-anti-slop.md` iteration verbs — evaluate, refine, harden) until the artifact is genuinely strong. Aim for **loop until amazing**, not until acceptable. Hand the human direction-level and taste decisions, not mechanical errors or gate failures they must catch — the agent does the checking, testing, and rechecking; the human feedback loop steers and signs off.

**Page builds:** the **Automatic page-build contract** in `web-experience.md` is mandatory on every “build a page / Scripture Journey page” request. Treat broken interactions, missing verification, and system-font shells as gate failures.

## 1. Integrity gate

- The promise is true and deliverable.
- Evidence, quotations, translations, analytics, outliers, testimonials, and citations are not invented.
- Emotion serves meaning rather than manipulation.
- No fear escalation, guilt, shame, coercion, false urgency, deceptive certainty, sensationalism, or manufactured suspense (empty reaction bait, stacked opaque teasers, unsupported insinuation, vague trailer language). Honest, concrete curiosity gaps in titles, thumbnails, and pre-click copy are not a fail — see `youtube-planning.md` → Honest curiosity vs manufactured suspense.
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

For substantial teaching, review the core plans in `motivation-and-curiosity.md` and `memory-and-learning.md`; use `learning-evidence.md` to check scientific claims.

- Motivation framing identifies a valued toward goal and any genuine away concern without assigning fixed types or manufacturing pressure.
- The concept names what should remain retrievable and the prerequisite/load decisions; a chunk-count estimate is not a rigid slide or page quota.
- Planned learner processing, voluntary recall/explanation, source-grounded feedback, and a later varied return or transfer are present where they serve the central targets.
- Every curiosity promise resolves at a useful point; progress means actual clarity and capability.
- Captions, visible evidence, readable holds, and accessible equivalents survive the multimedia/load pass.
- Behavioral evidence, design heuristics, and scientific claims are distinguished; no dopamine-spike promise, universal attention timer, or guaranteed memory outcome is used.
- Engagement, understanding, and delayed memory/transfer are evaluated separately if outcome data is collected.

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
- If a story or illustration carries teaching load, its source status, meaning handoff, limits, and access equivalent are explicit.
- PAST scene details are sourced or labeled; no invented biblical dialogue, historical detail, or inner states.
- Plain-language clarity is tested as writing quality, not as a claim about children, fixed learning styles, the subconscious, or guaranteed transformation.
- No hypnosis, hypnotherapy, theta/brainwave reprogramming, subliminal or covert influence, coercive emotional conditioning, NLP-style rewiring, affirmation-based mind reprogramming, or manifestation method appears as content, delivery, formation, or conversion guidance.
- Authorized internal learning practices proceed under the core guidance. Any learner-facing neuroscience assertion satisfies the scoped claim rule in `story-craft.md`, using existing authorization where applicable.
- Website copy follows a named writing-strategy mix (`learning-and-writing.md`); conversion copy is short punch, not YouTube 80–110.
- Candidate public sentences stand on their own for splicing (`youtube-planning.md`).

## 5. Visual gate

- Proximity/grouping, figure-ground, and continuity/eye path are intentional.
- Hierarchy survives grayscale.
- Focal point and grouping survive squint/phone-size view.
- Type, color, imagery, and composition arise from the content/visual DNA.
- **Web fonts are designed faces** (network or self-hosted WOFF2), not system-only stacks; avoid Inter/system-default as the whole personality unless the brief demands it.
- Page does not read as generic AI slop (see `design-critique-and-anti-slop.md`).
- For layout/placement work: skill `dynamic-symmetry` was loaded; rectangle/armature considered (soft standard); grid choice recorded when used; pack path preferred over inventing thirds-only habits.
- No nude/sexually explicit reference imagery used in deliverables.
- Color is not the only signal; persistent words, shape, icon, pattern, or position carry the same meaning.
- Every color in a new or materially revised theme has an earned composition role, allocation, placement, provenance, and field/partner/spark visual-weight rationale through repository-root `skills/color-palette-composition/SKILL.md`; it records Itten/Munsell application and a short theory summary.
- When a color's intended/alternate response, culture, Scripture context, or psychology claim materially affects the decision, that claim is grounded through repository-root `COLOR-PSYCHOLOGY.md` with evidence strength recorded.
- Scripture color symbolism is verified from the actual passage/context and is never used as doctrinal proof or fear pressure.
- Text remains easily readable at final size and viewing conditions: 7:1 body/sustained-reading target when practical; WCAG 2.2 AA is the floor; gradients, transparency, imagery, video, and states are tested at their worst point.
- Any approved artistic low-legibility exception is nonessential and has an accessible, easily readable equivalent.
- Thumbnail is legible in a feed and against dark surroundings.
- Motion is purposeful and present in the **default** experience; optional `prefers-reduced-motion` accommodation does not define the design.
- Design fingerprint does not repeat recent work without reason.

## 6. YouTube gate

- Idea and packaging are distinguished.
- Title opens one honest, concrete gap (recognizable topic, stakes, and kind of payoff) and the content closes it. A reaction is not the whole hook. The line would not paste unchanged onto an unrelated story.
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
- Retention tactics do not delay value or fake stakes. Scripts include load-aware evidence beats and useful recall/transfer opportunities; cuts follow meaning and reading time rather than a supposed attention-span law.
- Story-led scripts use the truthful story architecture and meaning handoff in `story-craft.md`; the hook is honest, the turn is evidenced, and the payoff is delivered.
- Delivery craft follows `presentation-craft.md`: consequential voice/pause, visual, transition, and reading-time choices connect to the learning target. A requested script includes a scaled rehearsal plan; never claim rehearsal or audience testing occurred without evidence.
- Cases and invitations follow `ethical-persuasion.md`: sources, reasoning, material limits, and voluntary next steps are inspectable. Confidence, emotion, repetition, popularity, and production polish do not replace evidence.
- Presentation/persuasion claims use `presentation-evidence.md`; no guarantee of attention, comprehension, memory, virality, sales, or audience response follows from a craft technique.
- Neuroscience, psychology, sales, and outcome claims are verified, qualified, or rejected; any learner-facing neuroscience assertion satisfies the scoped claim rule in `story-craft.md`; creator testimony is not Scripture authority.
- Banned influence and reprogramming methods are absent from the script, delivery, packaging, CTA, and learner exercise.

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
- File naming followed repo root [`WORKSPACE.md`](../../../../../WORKSPACE.md) §3 for the artifact's kind — progressive stem for deliberation artifacts, canonical-on-first-write for deterministic deliverables.
- The requested artifact is complete at its current scope; unresolved dependencies (missing art files, etc.) are named rather than hidden.

<!-- Agent: grok · Model: Grok 4.6 · Date: 2026-08-20 · website copy + splice-safe content gate -->

<!-- Agent: Codex · Model: GPT-5 · Thinking: not exposed · Date: 2026-09-09 · Added color-psychology and readable-text gates. -->
<!-- Agent: grok · Model: Grok 4.6 · Date: 2026-09-09 · Integrity/YouTube gates distinguish honest curiosity gaps from manufactured suspense. -->
<!-- Agent: Buffy | Model: GPT-5 · Thinking: not exposed · Date: 2026-09-24 | Added hard-ban and approval-gated neuroscience quality gates for release 3.4.1. -->

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed · Date: 2026-09-13 | Added canonical palette-composition verification and scoped contextual psychology. -->

<!-- Agent: Codex | Model: GPT-6 | Thinking: not exposed | Date: 2026-09-25 | Integrated evidence-calibrated motivation, curiosity, and memory design. -->



<!-- Agent: Codex | Model: GPT-6 | Thinking: not exposed | Date: 2026-09-25 | Expanded presentation craft and evidence-based ethical persuasion. -->
