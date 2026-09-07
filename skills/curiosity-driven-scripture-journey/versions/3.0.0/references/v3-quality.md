# Scripture Journey v3 — quality and review contract

## 1. Two quality axes

Do not use AA/AAA ambiguously.

### Accessibility conformance

- WCAG 2.2 AA is the normal release minimum.
- Attempt AAA for text contrast/readability where practical without damaging the approved concept.
- Never claim AA or AAA without checks against the actual candidate.

### Experience craft

- **Class A:** coherent, functional, non-generic candidate.
- **Class AA:** polished professional work with strong subject-specific design, learning interaction, mobile execution, and detail.
- **Class AAA:** flagship work: memorable concept, exceptional composition, refined motion/interaction, strong learning payoff, and no obvious generic-template residue.

For substantial Scripture Journey pages, target **Experience Class AA or better** before presenting the page as finished. The user may request AAA/flagship iteration.

## 2. Required design loop

Rules alone do not create beauty. Run an iterative loop:

1. **Compose** — establish hierarchy, rhythm, focal moments, negative space, typography, imagery, and progression.
2. **Critique** — actively search for flatness, generic structure, repetitive cards, weak focal moments, poor proportion, subject-disconnected visuals, decorative interaction, and weak mobile collapse.
3. **Revise** — use focused passes such as bolder, layout, typeset, colorize, animate, delight, distill, or polish.
4. **Phone / squint / grayscale review.**
5. **Learning-experience review** — prove that interaction produces discovery rather than decoration.
6. **Re-run deterministic and accessibility checks.**
7. Continue until release-blocking problems are fixed and the target craft class is met.

The critic should assume the builder is too attached to its solution. The builder must respond with revisions, not merely record findings.

## 3. Independent review passes

A substantial page should receive separate passes for:

- design / visual craft;
- learning experience;
- accessibility / semantics;
- performance / code quality;
- security / error handling when forms, user input, persistence, or external services are present.

Each pass identifies blockers and the highest-leverage correction first. Re-run affected reviews after fixes.

## 4. Deterministic audit

Run `scripts/audit_html.py` on every substantial HTML candidate before human review. Release-blocking checks include, where deterministically detectable:

- missing language, charset, viewport, title, meta description, main landmark, or exactly one H1;
- unresolved production `href="#"` placeholders;
- duplicate IDs;
- images without `alt` attributes;
- viewport-width component breakpoints that violate the container-query-first standard;
- interactive pages without visible focus treatment;
- motion without `prefers-reduced-motion` accommodation;
- disclosure controls without accessible expanded state.

The deterministic audit is a **floor**, not a design scorer. Passing it does not make a page beautiful, educationally effective, secure, or performant.

## 5. Release rule

Do not hand the user mechanical defects that the design/code review loop could have corrected. Human review should focus on taste, direction, theological/content judgment, and final acceptance—not broken controls, obvious contrast failures, placeholder links, or generic first-pass design.
