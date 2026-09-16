# Visual Learning and Design System

Use this file for visual direction, layouts, graphics, thumbnails, typography, color, imagery, composition, motion, or design review.

**Core design constitution:** for a new or materially revised palette/theme, first load repository-root **`skills/color-palette-composition/SKILL.md`**. It owns visual weight, field/partner/spark allocation, Itten/Munsell theory, mixing, placement, naming handoff, and verification. Load repository-root **`DESIGN-DIRECTIVES.md`** when that theme becomes source locks, story names, semantic tokens, gradients, or an implementation handoff. Load **`COLOR-PSYCHOLOGY.md`** only when an intended/alternate reading, culture, Scripture context, or psychology claim materially changes the decision. This file adds Scripture-journey-specific composition, teaching, typography, imagery, and motion rules.

## Contents

- Visual DNA brief
- Order of operations
- Gestalt and teaching
- Composition (dynamic symmetry = soft standard)
- Typography
- Color
- Palette composition → repository-root `skills/color-palette-composition/SKILL.md`
- Contextual color interpretation → repository-root `COLOR-PSYCHOLOGY.md` when consequential
- Imagery and thumbnail-specific rules
- Motion and interaction
- Design fingerprint and anti-repetition
- Dynamic Symmetry → load skill `skills/dynamic-symmetry/SKILL.md` (glossary + method live there; local files are pointers only)

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
6. Select typography and palette together from tone keywords and actual content. For a new/materially revised theme, follow `color-palette-composition` first; use `DESIGN-DIRECTIVES.md` for source names/tokens/gradients, and add `COLOR-PSYCHOLOGY.md` only for consequential contextual interpretation.
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
- **Dynamic Symmetry is the soft standard** for layout, spacing, visual hierarchy, thumbnails, section heroes, and crop decisions. Not a hard law—but there is rarely a good reason to skip it when anything is being *placed* on a canvas. Full method: skill **`dynamic-symmetry`** (`skills/dynamic-symmetry/`).
- **What it is:** an armature (diagonals, reciprocals, eyes, optional MAD/themes) inside a chosen root/phi/1.5 rectangle so placement has unity, rhythm, and movement—stronger and more flexible than defaulting to rule of thirds.
- **How to use (short):**
  1. Lock the delivery crop (16:9, 9:16, 1:1, page, print…).
  2. Match a root/phi/1.5 rectangle (e.g. 16:9 ≈ root 3).
  3. Overlay a black-line PNG from `G:\__ai-projects\_resources\design-resources\dynamic-symmetry-grids\` (US or A4, horizontal or vertical) **or** construct the basic armature.
  4. Put the dominant subject and type on strong lines/eyes; let negative space be intentional.
  5. Use MAD/themes when the frame has multiple zones; vary themes across pieces so work does not clone itself.
- **Why:** hierarchy and spacing become *related* instead of arbitrary; thumbnails and web heroes stay calm under bold ideas; anti-repetition stays lawful.
- Compute for the **actual** canvas. Cropping to a different ratio after compose breaks the armature—match final delivery ratio when choosing the grid.
- **Never** use nude/sexually explicit study imagery from educational PDFs; only use line grids and pure method knowledge (see `skills/dynamic-symmetry/references/method.md` safety table).
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
8. **Web default = network or self-hosted webfonts** (Google Fonts, Bunny, Fontshare, Adobe, WOFF2). System stacks are fallbacks only. Do **not** constrain pages to “local/stock fonts only.”
9. Avoid the AI-slop pairing of Inter (or system UI) + generic serif on cream paper as a default Scripture look—choose faces from the content’s tone.
10. Performance: prefer WOFF2/variable fonts, limited weights, preconnect, and fallbacks after the designed faces.
11. Test thumbnail display type at actual phone-preview size. Legibility outranks ornament.

Named font examples are sanity checks, not a menu. Reason first.

## Color

**Apply repository-root `skills/color-palette-composition/SKILL.md` to create or materially revise the palette.** Apply `DESIGN-DIRECTIVES.md` to turn the approved palette into its source-specific naming, token, gradient, and implementation architecture. Add `COLOR-PSYCHOLOGY.md` only when contextual interpretation changes the choice. Keep detailed color references out of this lane file so ordinary visual work stays lean. In shorthand:

> **visual-weight composition (Itten + Munsell) → source-specific evocative naming → locked official colors → compact harmonized palette → semantic developer tokens → named signature gradients → contextual psychology when consequential → practical guidance → validated accessibility and readability**

Journey-specific additions:

- Build meaning and hierarchy in grayscale first; color strengthens hierarchy rather than creating it from nothing.
- Derive palette direction from the same tone keywords and content used for typography and imagery.
- For every created/revised theme, name field/partner/spark, allocation, Itten contrast/extension decision, Munsell HVC/value-chroma correction, and one- or two-sentence theory summary.
- Preserve official/user-locked brand colors exactly; never silently replace them with a sampled or aesthetically tidier alternative.
- Prefer memorable names that belong to the current source/story instead of generic color labels or names copied from another project.
- Keep the core palette learnable; add colors only when each earns a distinct role.
- Separate canonical/story tokens from semantic application aliases in web work.
- When `COLOR-PSYCHOLOGY.md` is consequential, use its workflow: define intended response; check audience, culture, faith context, medium, and viewing duration; record a plausible alternate reading; grade evidence; validate pairings; and add non-color cues.
- Treat psychological notes as contextual design intentions, not universal color laws. Never imply that a hue guarantees trust, calm, urgency, conversion, learning, health, or a physiological result.
- In Scripture/ministry work, verify symbolism from the actual passage and object. Color may support teaching but can never serve as doctrinal proof or fear pressure.
- **Readable text is a hard gate:** target 7:1 for body/sustained reading when practical and never fall below WCAG 2.2 AA. Test the exact final foreground/background at the final size, including the worst point over gradients, transparency, imagery, or video. An explicit artistic exception cannot hide the only copy of essential content.
- Never use color as the only signal.
- Independently calculate contrast for actual foreground/background values and every important interaction state; never inherit AA/AAA labels from a previous agent or reference without validation.
- Check the finished design in grayscale, on a dark surrounding surface, and in squint/phone view.
- Do not default unrelated work to beige, cream, brown, muted green, or any prior project palette because an earlier token set used them.

## Imagery and thumbnail-specific rules

- Never use explicit, nude, or sexually suggestive content, poses, shapes, or object symbolism.
- Use expressive faces or recognizable human elements only when authentic to the content and emotion.
- Avoid misleading composites, invented evidence, sensational prophecy imagery, or expressions that overstate the actual delivery.
- Use one clear focal subject and purposeful supporting elements.
- For thumbnails, prefer concise overlay text of four words or fewer, high dynamic contrast, and dark-mode/feed visibility.
- Extract principles from references—attention, hierarchy, negative space, tone, type—not a composition to copy.

### Artwork production route

Use the image-generation or design capability explicitly requested by the user when it is available. Load **`artwork-prompts-handoff`** only when the user asks for a manual prompt pack, says they will generate the images themselves, or the project explicitly requires a recorded human-generation handoff.

For a manual handoff, write the prompts pack with each paste-ready prompt, aspect ratio, Dynamic Symmetry note, target filename, and checkbox. Naming: repo root [`WORKSPACE.md`](../../../../WORKSPACE.md) §3.

## Motion and interaction

- Use motion for feedback, orientation, progress, state change, discovery, emphasis, transition, explanation, or delight.
- Do not animate merely because an element can move.
- **Full motion is the default design language.** Optional simplify only inside `@media (prefers-reduced-motion: reduce)`—never ship a static page “to be safe.”
- Match motion pacing to cognitive load: quieter during complex reading, more energetic during transitions or simple reveals.
- Journey interactions may require JavaScript; verify they work in a browser. Keyboard/touch access for real controls.

## Design fingerprint and anti-repetition

Record the completed piece’s composition, writing framework, type personality, palette family, hero treatment, interaction, motion, and imagery. Compare it with recent work.

Warn when several dimensions repeat without a content reason. Preserve the project spine while changing multiple personality dimensions to create coherent variety.

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-08 | Narrowed manual artwork handoff routing. -->

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-13 | Routed created/revised themes to canonical palette composition, retaining Psychology for consequential context. -->
