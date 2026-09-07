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


## 6. Public-write abuse protection standard (3.0.1)

Any public form or endpoint that writes data, creates a lead/account, increments a durable counter, triggers email/SMS, or causes another external side effect must include layered abuse protection appropriate to the risk.

Default to the **least intrusive controls that materially work**:

1. server-side validation and strict size/type bounds;
2. same-origin / expected-origin enforcement where the workflow is same-origin;
3. a honeypot or equivalent bot-only field when a browser form is involved;
4. a minimum plausible completion-time check for lead/contact forms;
5. rate limits at both network/IP and durable visitor/account scopes when available;
6. no wildcard CORS on same-origin write endpoints;
7. operational logging for blocked or failed writes;
8. a challenge such as Turnstile only when traffic risk, abuse history, or endpoint value justifies it, preferably as an escalation rather than friction for every visitor.

For phone/SMS workflows, **capture and send-readiness are separate states**. Preserve plausible user-entered international numbers even when they cannot be confidently normalized. Store the raw value and a status such as `e164_ready` / `needs_review` / `missing`. Only numbers classified as send-ready may enter automated SMS. Do not guess a country calling code for an ambiguous national-format international number.

This is a release requirement for substantial public interactive pages, not an optional polish item.
