# Core Design Directives

**Cross-skill design constitution.** Load this file for any design-bearing task: brand systems, palette work, visual systems, graphic design, thumbnails, artwork direction, UI theming, CSS color systems, visual review, or developer handoff of design tokens.

This file owns **design reasoning and color-system architecture**. Individual skills may add stricter rules for composition, CSS mechanics, HTML, accessibility, motion, or artwork production, but they should not contradict this foundation.

---

## Core design chain

For source-led or brand-led visual work, reason in this order:

> **source-specific evocative naming → locked official colors → harmonized families → compact core palette → semantic developer tokens → named signature gradients → psychological usage tied to imagery/content → practical designer/developer guidance → validated accessibility**

Do not treat this as a cosmetic naming exercise. Each step solves a different problem:

1. **Source-specific evocative naming** makes colors memorable and ties them to the actual work rather than a generic paint deck.
2. **Locked official colors** protect brand truth and user-provided source-of-truth values.
3. **Harmonized families** create usable relationships around those anchors instead of collecting unrelated samples.
4. **Compact core palette** keeps the system learnable and prevents near-duplicate color sprawl.
5. **Semantic developer tokens** separate brand/story names from application roles.
6. **Named signature gradients** preserve meaningful source transitions and make them reusable.
7. **Psychological usage tied to imagery/content** explains why a color works *here*, without pretending color psychology is universal law.
8. **Practical designer/developer guidance** turns a palette into a working system.
9. **Validated accessibility** verifies technical claims instead of trusting labels, examples, or visual intuition.

---

## 1. Establish the source of truth before sampling

Before deriving colors, identify what is authoritative.

Priority order:

1. **Official/user-locked brand values** — exact names and values supplied by the user or canonical brand source.
2. **Approved source artwork / visual references** — representative colors visibly present in the chosen source.
3. **Harmonized derived colors** — deliberately adjusted or created to bridge families, improve spacing, or provide usable states.
4. **Semantic aliases / generated states** — developer-facing roles and calculated variants; these are not new brand colors.

Never silently replace an official value because a sampled or mathematically tidy alternative looks better.

If an official color and the artwork differ, keep the official color locked and harmonize neighboring colors around it. Record the distinction.

### Provenance labels

When documenting a serious palette, classify values when useful:

- **OFFICIAL / LOCKED** — exact source-of-truth value; do not alter.
- **EXTRACTED** — representative sample chosen from source imagery.
- **HARMONIZED** — intentionally adjusted/derived to create a coherent family.
- **SEMANTIC** — alias such as `--color-primary`; points to another token.
- **STATE / RELATIVE** — hover, focus, muted, overlay, border, or other calculated variant.

This prevents an attractive derived color from accidentally becoming a false brand standard later.

---

## 2. Name from the source, not from a generic color dictionary

Prefer **short, evocative, source-specific names** that help a designer remember where the color belongs and why it exists.

Good naming usually has these traits:

- 1–3 words.
- Concrete or image-linked rather than abstract marketing language.
- Distinct from neighboring colors.
- Stable enough to become a long-term token name.
- Meaningful to a human designer even before reading the hex value.

Examples of the pattern — **not universal names to copy**:

- a fire-dominant source might naturally produce names such as `Flame`, `Ember`, `Deep Ember`;
- a wing or sky motif might suggest `Wing Azure`, `Celestial Violet`, `Night Violet`;
- a lion/gold motif might suggest `Lion Gold`, `Amber Glow`.

Do **not** carry those names into unrelated projects. Re-derive names from each project's own imagery, story, objects, atmosphere, or established brand language.

Avoid generic auto-palette naming such as `Orange 1`, `Dark Blue`, `Primary Red`, or arbitrary poetic names that have no visible connection to the source.

### Official names win

If a brand color already has an official name, preserve that name exactly unless the user explicitly asks to rename it.

---

## 3. Build harmonized families around anchors

Do not simply sort sampled hex values by hue. Build **families with visual and functional relationships**.

Typical family logic might include:

- warm/fire/action family;
- gold/light/glory family;
- cool/sky/heaven/secondary family;
- neutral/background/text family;
- project-specific families suggested by the source.

A family may contain an official anchor plus extracted or harmonized companions. Derived companions should feel like intentional steps, not arbitrary near-duplicates.

### Prefer a compact core

For most brand or project systems, target roughly **8–14 core colors** before states and semantic aliases. This is guidance, not a quota.

Add a color only when it earns a distinct role, for example:

- a necessary tonal step;
- a separate functional state;
- a recurring source motif;
- a contrast-safe text/surface pairing;
- a signature highlight that cannot be served by an existing token.

If two colors will always be used interchangeably, one probably does not belong in the core palette.

---

## 4. Keep story tokens and semantic tokens separate

Use **two layers**.

### Layer A — canonical brand/story tokens

These preserve the evocative names and remain stable across design tools and code:

```css
:root {
  --flame: ...;
  --deep-ember: ...;
  --lion-gold: ...;
  --wing-azure: ...;
  --warm-white: ...;
  --void: ...;
}
```

The names above are examples of structure only. Use names derived from the current project.

### Layer B — semantic application aliases

Map the canonical palette to roles:

```css
:root {
  --color-primary: var(--flame);
  --color-accent: var(--lion-gold);
  --color-secondary: var(--wing-azure);
  --color-bg: var(--void);
  --color-surface: var(--charcoal);
  --color-text: var(--pure-white);
}
```

Semantic aliases may change when a theme or component role changes. Canonical brand/story names should not be renamed merely because their current UI role changed.

Prefer semantic tokens over raw hex inside components.

### Theme registry rule

For multi-theme HTML or UI work, maintain one centralized theme registry or token source as the system of record.

- Each theme is one additive entry containing the complete semantic token set required by the experience.
- Generate or derive CSS theme blocks, selector options, query-parameter allowlists, and JavaScript allowlists from that registry whenever the build environment permits.
- Components consume semantic aliases such as background, surface, text, muted text, accent, rule, focus, texture, and texture scale. Do not scatter literal theme colors or texture assets through component CSS.
- Adding or adjusting a theme must not require structural page rewrites or edits across unrelated components.
- Give themes clear public-facing names tied to their visual character. A calm neutral-light theme may be called `mild`; avoid exposing temporary working names such as `bland`.
- Light themes may have distinct, evocative color personalities while remaining restrained enough for sustained reading. Do not automatically equate light with pastel or wash every theme in pale gradients; strong accents on quiet neutral surfaces may carry more character.
- When texture fits the visual DNA, store the self-contained texture asset or inline SVG plus its scale/opacity controls in the same theme entry. Texture should add material character without reducing legibility, delaying rendering, or requiring component rewrites.
- Validate contrast for every shipped theme and every text-bearing surface; a safe default does not excuse an inaccessible alternate theme.
- Document legacy aliases only when needed for old links or saved preferences, and keep them out of the visible selector.

A minimal maintainable pattern is:

```js
const themes = {
  mild: { paper: "…", surface: "…", text: "…", muted: "…", accent: "…", focus: "…", texture: "…", textureSize: "…" },
  mark: { paper: "…", surface: "…", text: "…", muted: "…", accent: "…", focus: "…", texture: "…", textureSize: "…" }
};
```

The exact implementation language may differ, but the single-source-of-truth rule does not.

---

## 5. Signature gradients must have meaning

When the source contains important transitions — fire into shadow, blue into violet, gold into ember, light into darkness — capture them as **named signature gradients**.

A reusable gradient definition should include:

- evocative source-specific name;
- angle/direction;
- exact stops and positions;
- intended usage;
- whether text may safely sit over it;
- light/dark context if relevant.

Name gradients from the image/story rather than `Gradient 1`, `Warm Gradient`, or `Blue Gradient`.

Examples of the naming pattern, not names to reuse automatically: `Fire Core`, `Wing Sweep`, `Lion Glory`, `Apocalyptic Blend`.

Do not invent a gradient merely to increase the number of deliverables. It should represent a real relationship in the visual language.

---

## 6. Psychological notes must be contextual, not pseudoscientific

Explain color roles in relation to the **actual source, audience, hierarchy, and subject**.

Good:

> In this composition, the blue-violet wing family counterbalances the dominant fire palette, creating a cooler visual release and a distinct spiritual/secondary zone.

Weak:

> Blue universally means trust.

Use psychological/perceptual notes to explain intended effects such as:

- energy vs rest;
- visual dominance vs counterpoint;
- gravity vs release;
- warning vs hope;
- sacred/premium emphasis;
- depth, mystery, clarity, or separation;
- where the eye is expected to move.

Treat these as **design intentions and contextual readings**, not universal human laws.

---

## 7. Turn the palette into practical guidance

A useful color system should tell both designers and developers what to do with it.

When the task warrants a full palette/style guide, include as appropriate:

- core swatches with name + HEX;
- RGB and HSL/OKLCH where useful;
- provenance/lock status for official values;
- family groupings;
- primary and muted text colors;
- background and elevated surface colors;
- primary/secondary actions;
- links, focus, hover, selected, disabled, success/error states when relevant;
- borders, shadows, glows, overlays;
- signature gradient names + stops;
- semantic CSS variables;
- recommended usage and anti-usage;
- accessibility results for important pairs;
- designer-friendly copyable values when HTML is the deliverable.

For interactive palette HTML, prefer useful behaviors such as click/keyboard-to-copy swatches, copyable token blocks, visible focus states, responsive intrinsic layout, and restrained motion.

Use full motion normally when it serves the experience. Simplify motion only inside `@media (prefers-reduced-motion: reduce)` when the user's environment requests it.

---

## 8. Validate accessibility; never inherit contrast labels blindly

Every contrast claim is a calculation, not a style opinion.

Before labeling a pair AA/AAA, calculate the contrast ratio from the actual foreground/background values being shipped.

WCAG contrast thresholds commonly used for validation:

- **AA normal text:** 4.5:1
- **AA large text:** 3:1
- **AAA normal text:** 7:1
- **AAA large text:** 4.5:1
- **Non-text UI / graphical objects where required:** 3:1 against adjacent colors

Also check:

- hover/focus/active/disabled states;
- text over gradients or imagery at the actual placement;
- muted text, not only headings;
- controls and focus indicators;
- color is never the only way information is communicated.

Do not copy an accessibility label from a reference file, previous agent, palette generator, or screenshot without re-validating it.

When a vibrant brand color fails as normal body text, keep the brand color if it is legitimate and change the **role**: large display text, icon, border, background, or decorative accent may still be appropriate.

---

## 9. Color-space and implementation guidance

### Web

- Preserve canonical source values exactly when they are locked.
- Use CSS custom properties for both canonical and semantic layers.
- Use modern color tools (`oklch`, relative color syntax, `color-mix(in oklab, ...)`) for derived states when browser support/project constraints allow.
- Do not convert an official hex to OKLCH and then round-trip it back to a visibly different hex while still calling it the official value.
- Prefer generated state colors over bloating the core palette with many one-off variants.
- Pair with container-query-first layout and the `modern-css-design` skill for CSS mechanics.

### Graphic design

- Keep official values and palette names consistent across Affinity, Canva, Figma, Illustrator, Photoshop, and export notes.
- Record gradient stop positions and direction so a signature gradient can be rebuilt faithfully.
- Check the work in grayscale/squint view as well as full color; color should strengthen hierarchy, not create it from nothing.

### Print

RGB artwork does not have one universally correct CMYK conversion.

- Generic RGB→CMYK percentages are approximations only.
- Do not label them "production-ready" without knowing the output condition.
- Final print conversion should use the printer/paper/process ICC profile or printer specification.
- Preserve the canonical RGB/HEX source alongside any print conversion so the brand master remains unambiguous.

---

## 10. Anti-slop checks for palette and visual-system work

Before finishing, ask:

- Did I preserve every official/user-locked color exactly?
- Did I distinguish official, extracted, harmonized, semantic, and state values where confusion is possible?
- Are the names specific to this source, or could they have come from any random palette generator?
- Do family names and color names help a human remember the visual source?
- Is the core palette compact, or did I keep near-duplicates just because they were sampled?
- Does every extra color have an earned role?
- Are semantic tokens separate from canonical/story names?
- Are signature gradients based on real visual relationships and named accordingly?
- Are psychological notes tied to this content rather than generic color-psychology claims?
- Have all important contrast labels been independently calculated?
- Did I check muted text and interaction states, not only hero headings?
- Did I avoid claiming generic CMYK conversions are press-ready?
- Can both a graphic designer and a web developer use the system without guessing?

If the answer to any of these is no, the color system is not finished.

---

## Relationship to skill-specific rules

- **`curiosity-driven-scripture-journey/references/visual-system.md`** — composition, Gestalt, typography, imagery, motion, design fingerprint; this file supplies the deeper cross-project color-system reasoning.
- **`modern-css-design`** — CSS architecture and implementation mechanics; this file decides how source/brand color systems are structured conceptually.
- **`modern-html-aeo`** — page structure, conversion, performance, semantics, AEO/GEO/SEO; use these directives before encoding the visual system into the page.
- **`artwork-prompts-handoff`** — artwork generation brief/handoff; use these directives to establish the shared palette and color-grade language before writing per-image prompts.

Specific project truth always beats examples in this file. Re-derive the visual language from the current source rather than cloning a previous project's aesthetic.

<!-- Agent: Codex · Model: GPT-5 · Date: 2026-08-21 · Change: centralized, additive, contrast-validated theme-registry directive. -->
