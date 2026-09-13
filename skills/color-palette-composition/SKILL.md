---
name: color-palette-composition
description: Create, revise, critique, or document high-attention color themes for interiors, graphics, brands, web pages, interfaces, data displays, and print. Use whenever a request needs a coordinated palette, color scheme, proportions, placement, mixing, or visual hierarchy; not for one isolated color choice.
---

# Color Palette Composition

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-13 | Established this skill as the canonical palette-generation workflow; split the guide for selective loading and made source-specific naming a required handoff. -->

Build a controlled distribution of attention, not a pile of attractive swatches. Hue is secondary to visual weight: area, chroma, local contrast, temperature, and isolation decide whether a palette holds together.

This is the **canonical skill for generating or materially revising a palette/theme**. Other systems may supply source constraints, story, semantic roles, implementation tokens, or interpretation evidence; they do not replace this composition workflow.

## Load only what the task needs

Read [core composition](references/core-composition.md) for every substantive new or revised theme. Then load exactly the relevant module:

| Need | Read |
|---|---|
| Interior, graphic/editorial, UI, data display, or print placement | [medium application](references/medium-application.md) |
| Starting examples or a named harmony pattern | [starter kits](references/starter-kits.md) |
| Formal handoff, contrast/production verification, provenance, or design-token bridge | [validation and handoff](references/validation-and-handoff.md) |

Do not load starter kits for a routine critique, and do not load every module merely because the task is a palette task. The core remains mandatory; the additional module makes the skill precise without making routine requests expensive.

## Start with the brief

Identify the medium, intended mood and audience, source/story, fixed colors or materials, lighting/output conditions, accessibility requirement, and one attention target. Preserve a locked color exactly. Label serious values `official`, `extracted`, `harmonized`, or `semantic`; a derived swatch must not become a false brand standard.

Use **field / partner / spark** whenever “primary” could be ambiguous. In a room or editorial composition, the largest color is generally the field. In UI, `primary` often means a small, high-emphasis action color; use `canvas`, `surface`, and `on-*` for broad roles.

## Mandatory dual-lens method for themes

For every substantive proposed color scheme or theme, apply and report **both** lenses. A named harmony or recipe alone is insufficient.

1. **Itten:** name one or two of the seven contrasts doing the compositional work (hue, light-dark, cold-warm, complementary, simultaneous, saturation, or extension). When two chromatic areas coexist, make an extension decision rather than assuming equal area.
2. **Munsell:** name the HVC path building the family (vertical value, lateral hue, or inward through gray to the opposite), then make a value-chroma correction. A small intense color can balance a much larger muted field; percentage alone is not balance.
3. **Visual weight:** assess `weight ~= area x chroma x local contrast`. Temperature and isolation amplify or dampen it. This is a directional design heuristic, not a physical calculation.
4. **Human reading:** include a one- or two-sentence `theory_summary` naming the Itten and Munsell patterns used, what they changed, and why a human could research them.

## Required naming contract

Apply this before handoff. The Design Directives own the token architecture; this skill requires the palette behavior that feeds it.

- Give the completed theme and canonical/story swatches short, evocative, source-specific names (normally 1–3 words). Do not call a real design color `Orange 1` or `Dark Blue`.
- Preserve an official manufacturer or brand color name exactly; record it as `official` rather than replacing it with a poetic alias.
- Keep **canonical story names** separate from **semantic role aliases**: for example, `Flame` can map to `--flame`, while `--color-primary` or `action` describes its implementation job. A role may change without renaming the color story.
- Name signature gradients from the image/story they create (`Fire Core`, `Wing Sweep`), never `Gradient 1`. A generic construction label is only provisional.
- If a supplied source uses generic names, retain the source label in provenance and propose an evocative canonical name only when it is not locked/official.

## Fast workflow

1. Build the value structure first: readable field plus ink/on-color. A design that dies in grayscale has unresolved hierarchy.
2. Choose one attention target. Give it the strongest advantage in chroma, value contrast, warm/cool contrast, isolation, or scale—not all elements.
3. Consider `70/20/10` for attention-led editorial/campaign/room work or `80/15/5` for dense, refined, information-led work. These are favored first trials, not rules. Use another split with a visual-weight reason; use `60/30/10` only when its balanced interior bias fits.
4. Assign field, partner, spark, neutral/on-color, and semantic state roles; map them to surfaces or components.
5. Apply the Itten contrast and Munsell HVC/value-chroma decisions. Build a related family before importing an unrelated hue.
6. Run the two-second focal test, contrast/non-color-cue checks, and medium/output test.

## Non-negotiable safeguards

- 60/30/10 is a documented interior convention, not a global default or scientific law.
- A locked brand color that fails contrast changes **role**. An unlocked derived color may change value/chroma, role, or both.
- Color never conveys a status, category, action, or error alone; add words, icons, shapes, pattern, position, or underlining as appropriate.
- Do not treat a screen HEX as a paint formula or production CMYK specification. Proof print with its output profile; test paint samples under installed light and beside fixed materials.
- Starter recipes are directions, never default brands. Re-name and re-derive them from the present source.

## Required handoff

For a substantive palette response, include the following as applicable:

```yaml
palette:
  medium: interior | graphic | ui | data-viz | print | mixed
  concept:
  attention_target:
  naming:
    theme_name:
    canonical_story_names: []
    semantic_role_aliases: {}
    signature_gradient_names: []
    official_names_preserved: []
  theory_lens: "Itten + Munsell"
  itten_application: { contrasts: [], extension_decision: "" }
  munsell_application: { hvc_path: "", value_chroma_correction: "" }
  visual_weight: "field / partner / spark rationale"
  theory_summary: "One or two sentences: named pattern, decision, and why."
  harmony:
  allocation:
  provenance: {}
  field: { name, value_or_material, placement }
  partner: { name, value_or_material, placement }
  spark: { name, value_or_material, placement }
  neutrals_and_on_colors: []
  semantic_states: []
  contrast_status:
  non_color_cues:
  production_or_light_test:
  do_not_use_as: []
```

`theory_lens`, `itten_application`, `munsell_application`, and `theory_summary` are required for a created theme. In a casual explanation, state them compactly rather than emitting the full block.

## Done when

- Every surviving color has a canonical name or preserved official name, role, allocation, placement, and provenance.
- The field, partner, and spark are evident in two seconds.
- The strongest chroma/contrast earns its attention.
- Both Itten and Munsell decisions are named, applied, and explained.
- Text, controls, meaningful graphics, and states work in actual context and are not distinguished by color alone.
- The result is tested in its real light, display, stock, or output condition when applicable.
