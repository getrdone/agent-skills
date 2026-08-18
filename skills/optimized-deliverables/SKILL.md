---
name: optimized-deliverables
description: Use when creating or refining any digital deliverable including web pages, articles, landing pages, docs, emails, product pages, or interactive content. Enforces lean generation process, high quality, SEO plus AI findability, usability, speed, beauty, delight, and purposeful interactivity.
---

# Optimized Deliverables

Apply these rules to every deliverable. Challenge every element against the six goals. Prefer fewer, stronger choices over exhaustive lists.

## Core Goals and Trade-offs

1. **Token efficiency** — Keep reasoning and output lean. Prefer direct answers, tables, and structured lists over prose walls. Omit fluff, hedging, and restated instructions.
2. **Quality** — Accurate, original insight, evidence-backed, people-first. Never commodity content. Add unique angle, data, or experience when possible.
3. **SEO + AI findability (GEO)** — Answer-first structure, extractable facts, semantic clarity, entity consistency. Content that both ranks and gets cited by generative engines.
4. **Usability** — Clear hierarchy, scannable, accessible, mobile-first, low cognitive load.
5. **Speed** — Minimal payload, critical content in HTML. Progressive enhancement for resilience, not as a reason to start bland.
6. **Interaction + Delight** — Purposeful motion and interactivity are first-class when they improve clarity, feedback, or pleasure of use. Design the full experience; keep Core Web Vitals intact.

## Process Rules

- Start with the primary user question or job-to-be-done. Lead with the answer.
- Structure every major section answer-first (direct answer in first 40–80 words), then support with evidence, then optional depth.
- Prefer tables, numbered steps, definition lists, and short bullet groups over long paragraphs.
- Include specific, sourced statistics or concrete examples every 150–250 words where claims are made.
- Use question-form H2/H3 headings when they match real search/AI queries.
- End major pages or long content with a tight FAQ section (5–8 high-intent questions).
- For web content, recommend or implement semantic HTML, clear heading outline, and appropriate schema (Article, FAQPage, HowTo, Organization, Person) only when it adds clear value.
- Keep total length proportional to value. Cut any section that does not serve the primary intent.
- When generating code or markup, default to performance-friendly patterns (no heavy JS frameworks unless required, lazy loading, minimal CSS).

## Content Structure Template (adapt as needed)

- Opening: direct answer or key takeaway in 1–3 sentences.
- Body: 4–8 focused sections. Each starts with the answer, uses lists/tables for key facts, includes at least one concrete data point or example.
- Visuals / interactive: only if they clarify or enable action. Prefer lightweight (CSS/HTML first).
- Close: next action + FAQ if the format supports it.

## SEO + AI Findability Checklist

- Primary entity and key facts stated clearly and consistently.
- Answer-first + extractable formats (lists, tables, steps, Q&A).
- Fact density with numbers, dates, names, sources.
- Semantic structure and descriptive headings.
- Freshness signals (update dates) when relevant.
- Unique value that cannot be generated from generic training data alone.
- For sites: ensure AI crawlers are not blocked; recommend llms.txt only if low-effort and useful.

## Usability + Speed + Interaction

- Mobile-first hierarchy and touch targets.
- High contrast, readable type, logical tab order.
- Critical content server-rendered or in initial HTML.
- Interactivity via progressive enhancement (works without JS where possible).
- Avoid auto-playing media, heavy third-party scripts, or multi-step flows that add friction without clear payoff.
- Measure against Core Web Vitals intent even if not running Lighthouse: keep LCP, CLS, INP in mind.

## Token Discipline for the Agent

- Do not restate the skill rules in the output.
- Prefer concise bullet or table responses when listing optimizations or audits.
- When revising existing content, show only the changed sections or a precise diff-style summary unless full rewrite is requested.
- Stop when the deliverable meets the six goals. Do not pad.

## References

Load only as needed:

- `references/geo-checklist.md` — detailed GEO/SEO tactics and citation formats
- `references/performance-patterns.md` — common speed and progressive-enhancement patterns
