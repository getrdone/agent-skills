# Visual Learning and Design System

Use this file for visual direction, layouts, graphics, thumbnails, typography, color, imagery, composition, motion, or design review.

## Contents

- Visual DNA brief
- Order of operations
- Gestalt and teaching
- Composition (dynamic symmetry = soft standard)
- Typography
- Color
- Imagery and thumbnail-specific rules
- Motion and interaction
- Design fingerprint and anti-repetition
- Dynamic symmetry detail → `references/dynamic-symmetry.md`

## Visual DNA brief

Before detailed styling, define:

```yaml
brand_or_project_spine:
piece_personality:
tone_keywords:
emotional_arc:
known_visual_anchor:
new_visual_idea:
visual_metaphor:
focal_point:
eye_path:
grouping:
composition_system:
typography_direction:
palette_direction:
imagery_direction:
texture:
motion_character:
interaction_style:
references:
avoid:
```

Reason from the content. Do not pull a finished aesthetic from a token file, font list, palette list, trend, or example.

## Order of operations

1. Map the learning sequence: known anchor → scaffolding → new idea → payoff.
2. Map Gestalt structure: proximity/grouping, figure-ground/focal subject, and continuity/eye path. Use similarity, closure, and common region only where they clarify relationships.
3. **Choose a dynamic-symmetry rectangle + armature** for the real canvas (soft standard — see Composition). Load a matching PNG from the design-resources pack when available.
4. Build the hierarchy in grayscale/monochrome with type scale, value, spacing, and placement on that armature.
5. Run grayscale and squint/phone-size checks.
6. Select typography and palette together from tone keywords and actual content.
7. Add imagery, texture, interaction, and motion only when each supports meaning.
8. Re-run grayscale, squint, accessibility, and integrity checks.
9. Record which grid/ratio you used in the visual DNA / fingerprint.

## Gestalt and teaching

- **Proximity:** place related ideas together; let separation signal a new chunk.
- **Figure-ground:** make the subject unmistakable against the background, especially at thumbnail size.
- **Continuity:** guide the eye in the same order as the teaching path.
- **Similarity:** make repeated roles look related; avoid visual sameness between unrelated roles.
- **Closure:** simplify graphics when the eye can complete the form without losing clarity.
- **Common region/fate:** group only elements that behave or belong together.

Design is instruction. The viewer should see what matters, what belongs together, and where to go next before reading every word.

## Composition

- Start with the subject and intended eye path; choose a system that supports them.
- **Dynamic symmetry is the soft standard** for layout, spacing, visual hierarchy, thumbnails, section heroes, and crop decisions. Not a hard law—but there is rarely a good reason to skip it when anything is being *placed* on a canvas. Full method, vocabulary, ratios, pack paths, and safety rules: **`references/dynamic-symmetry.md`**.
- **What it is:** an armature (diagonals, reciprocals, eyes, optional MAD/themes) inside a chosen root/phi/1.5 rectangle so placement has unity, rhythm, and movement—stronger and more flexible than defaulting to rule of thirds.
- **How to use (short):**
  1. Lock the delivery crop (16:9, 9:16, 1:1, page, print…).
  2. Match a root/phi/1.5 rectangle (e.g. 16:9 ≈ root 3).
  3. Overlay a black-line PNG from `F:\__ai-projects\design-resources\dynamic-symmetry-grids\` (US or A4, horizontal or vertical) **or** construct the basic armature.
  4. Put the dominant subject and type on strong lines/eyes; let negative space be intentional.
  5. Use MAD/themes when the frame has multiple zones; vary themes across pieces so work does not clone itself.
- **Why:** hierarchy and spacing become *related* instead of arbitrary; thumbnails and web heroes stay calm under bold ideas; anti-repetition stays lawful.
- Compute for the **actual** canvas. Cropping to a different ratio after compose breaks the armature—match final delivery ratio when choosing the grid.
- **Never** use nude/sexually explicit study imagery from educational PDFs; only use line grids and pure method knowledge (see dynamic-symmetry.md safety table).
- Use negative space, editorial asymmetry, centered iconic composition, timelines, evidence trails, comparisons, diagrams, photographic journeys, and other archetypes **on top of** the armature as appropriate.
- Consider a broad journey bank before defaulting: evidence trail, visual investigation, comparison journey, timeline, progressive discovery, document/exhibit, story-led journey, question-and-answer path, layered diagram, text-to-text investigation, immersive photographic journey, editorial feature, or interactive explorer.
- Avoid repetitive “hero + card + card + three columns + CTA” layouts unless the content genuinely calls for them.
- Aim for bold, memorable “wow factor” that remains organized, legible, and calm enough for the subject; impact never excuses clutter or garishness.

## Typography

1. Extract 2–3 tone/brand adjectives.
2. Choose a personality direction before font names.
3. Default to one expressive display face plus one quiet, highly legible supporting face when the subject benefits from contrast.
4. Alternatives: one variable family with a broad weight range, or a coordinated superfamily.
5. Check weight contrast, x-height compatibility, and personality contrast without conflict.
6. Use a mathematical type scale and fluid `rem`/`clamp()` or container-responsive sizing for web work.
7. Keep body text effectively at least 1rem on mobile; use comfortable body line-height and tighter display line-height.
8. Give fonts a performance budget: favor WOFF2, variable fonts where useful, limited families/weights, good fallbacks, and selective preloading.
9. Test thumbnail display type at actual phone-preview size. Legibility outranks ornament.

Named font examples are sanity checks, not a menu. Reason first.

## Color

- Build meaning and hierarchy in grayscale first.
- Derive palette direction from the same tone keywords as type.
- Use a dominant neutral, one primary accent, and one secondary accent; add more only when each earns a role.
- Never use color as the only signal.
- Verify text and controls against accessibility contrast requirements in every state.
- Check the finished design in grayscale, on a dark surrounding surface, and in squint/phone view.
- Do not default unrelated work to beige, cream, brown, or muted green because an earlier token set used them.

## Imagery and thumbnail-specific rules

- Never use explicit, nude, or sexually suggestive content, poses, shapes, or object symbolism.
- Use expressive faces or recognizable human elements only when authentic to the content and emotion.
- Avoid misleading composites, invented evidence, sensational prophecy imagery, or expressions that overstate the actual delivery.
- Use one clear focal subject and purposeful supporting elements.
- For thumbnails, prefer concise overlay text of four words or fewer, high dynamic contrast, and dark-mode/feed visibility.
- Extract principles from references—attention, hierarchy, negative space, tone, type—not a composition to copy.

## Motion and interaction

- Use motion for feedback, orientation, progress, state change, discovery, emphasis, transition, explanation, or delight.
- Do not animate merely because an element can move.
- Normal motion is the default. Disable or simplify it inside `@media (prefers-reduced-motion: reduce)`.
- Match motion pacing to cognitive load: quieter during complex reading, more energetic during transitions or simple reveals.
- Keep interaction optional for core understanding and keyboard/touch accessible.

## Design fingerprint and anti-repetition

Record the completed piece’s composition, writing framework, type personality, palette family, hero treatment, interaction, motion, and imagery. Compare it with recent work.

Warn when several dimensions repeat without a content reason. Preserve the project spine while changing multiple personality dimensions to create coherent variety.
