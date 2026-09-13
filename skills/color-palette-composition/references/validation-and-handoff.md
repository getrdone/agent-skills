# Validation and Handoff

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-13 | Split from the former monolithic field guide for formal system handoff and verification. -->

Read when a palette is being approved, implemented, documented, or connected to a design system. This does not replace the required core composition reference.

## Provenance and naming bridge

Record every serious swatch as one of:

- **official:** exact approved brand, manufacturer, or supplied source value; preserve its name and value.
- **extracted:** sampled from approved artwork, image, material, or existing environment; preserve source and date/asset when known.
- **harmonized:** deliberately derived to support a locked/extracted source color.
- **semantic:** chosen for a functional state or system role; it is not a source/brand color by implication.

The palette skill requires evocative canonical/story names and role aliases. The design-directive layer turns that contract into system tokens:

```text
Canonical story swatch: Flame             -> --flame
Semantic implementation alias: action      -> --color-primary: var(--flame)
Named image gradient: Fire Core            -> --gradient-fire-core
```

Never collapse story and role names. A color may move from action to accent or warning after testing without making the source story false. Preserve official names rather than overwriting them with a new story name.

## Verification checklist

- Does every color have a canonical/preserved official name, role, allocation, placement, and provenance?
- Are `theory_lens: Itten + Munsell`, the Itten contrast/extension decision, Munsell HVC/value-chroma correction, and one- or two-sentence theory summary present?
- Does the two-second focal test pass in color and grayscale?
- Do normal text pairs meet at least 4.5:1, large text 3:1, and meaningful controls/graphics 3:1 where WCAG applies?
- Is every status, category, action, and error backed by a visible non-color cue?
- Have image overlays, muted text, focus, dark mode, and real state combinations been checked?
- For interiors: fixed materials, sheen, LRV, room orientation, and installed light.
- For print: output profile, stock/press condition, and proof when color matters.

## Compact formal handoff

```yaml
palette:
  medium: graphic
  concept: "quiet, sun-warmed, editorial"
  attention_target: "the primary call to action"
  naming:
    theme_name: "Harbor Ledger"
    canonical_story_names: ["Warm Canvas", "Ink Structure", "Amber Action"]
    semantic_role_aliases: { canvas: "Warm Canvas", action: "Amber Action" }
    signature_gradient_names: []
    official_names_preserved: []
  theory_lens: "Itten + Munsell"
  itten_application:
    contrasts: ["saturation", "cold-warm", "extension"]
    extension_decision: "Amber receives 10% because it is warmer and more chromatic than navy."
  munsell_application:
    hvc_path: "Vertical warm-paper value family, then inward through gray toward amber."
    value_chroma_correction: "Keep amber small and navy muted so the spark does not outweigh the field."
  visual_weight: "Warm paper wins area; navy organizes with value; isolated amber wins through chroma and temperature."
  theory_summary: "Itten saturation/cold-warm contrast lets amber advance against navy, while extension limits its area. Munsell vertical and inward HVC paths keep the field coherent and preserve one focal spark with a value-chroma correction."
  harmony: neutral-plus-signal
  allocation: 70-20-10
  provenance: { field: harmonized, action: official }
  field: { name: "Warm Canvas", hex: "#F6F1E7", placement: "page canvas and cards" }
  partner: { name: "Ink Structure", hex: "#274C77", placement: "navigation and large type" }
  spark: { name: "Amber Action", hex: "#D97706", placement: "one CTA and key metric" }
  neutrals_and_on_colors:
    - { name: "Reading Ink", hex: "#182B3A", sits_on: "Warm Canvas" }
  semantic_states: []
  contrast_status: "Validate actual pairs before shipping"
  non_color_cues: "Icon and label accompany status"
  production_or_light_test: "Review at phone size and intended display"
  do_not_use_as: ["Amber is not body text or an error state"]
```

## Evidence and interpretation boundary

Use a color-psychology reference after composition only when Scripture symbolism, cultural/audience meaning, intended or alternate reading, or a material psychology claim changes the decision. Do not use generalized color meaning as a substitute for source evidence, visual hierarchy, contrast, or testing.

## Reference basis

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2*: text/non-text contrast and color-not-sole-cue requirements.
- International Color Consortium: profile-based color management improves consistency but cannot make screen, print, and paint identical.
- Design Directives: source-specific evocative naming, Layer A story names, Layer B role tokens, and story-named gradients.
