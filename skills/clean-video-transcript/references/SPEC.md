# Clean Video Transcript — Spec (single source of truth)

Use for any video-derived transcript: sermons, lectures, teaching series, panels, documentaries, and similar material.

## Goals

1. A readable full transcript that preserves the spoken message.
2. Careful spelling, punctuation, paragraphing, and restrained editorial headings.
3. A useful Scripture and source apparatus appropriate to the length and structure of the presentation.
4. A traceable record of verified, corroborating, and unresolved sources without altering transcript evidence.
5. Accessible output suitable for print, screens, screen readers, and machine parsing when those formats are requested.

## Inputs and outputs

| Input | Default output |
|---|---|
| Raw transcript with timestamps or subtitle line breaks | Cleaned Markdown next to the source |
| Clean transcript needing study aids | Updated Markdown with the selected reference apparatus |
| Follow-along download request | Markdown plus requested Word/PDF and semantic HTML editions |

Do not modify the raw transcript source unless the user explicitly asks. A file is already clean when it has a readable header, no timestamps, coherent paragraphs, approximately 90–100% of source-body words after allowed removals, and the required end matter.

## Header template

```markdown
# <Readable Title>
**<Speaker or channel>**
<Series / event line when known>
Video: <https://www.youtube.com/watch?v=...>
Video ID: <id>
Duration: <optional>

---
```

`Video ID:` is required when a YouTube URL is known. Use the bare identifier parsed from `v=` or `youtu.be/`.

## Body cleaning rules

1. **Preserve the full message.** No summaries in place of spoken content, no abridgment, and no invented teaching.
2. **Remove mechanical artifacts.** Delete timestamps, raw download headers, caption counters, and isolated subtitle artifacts such as `[Music]` when the requested clean style omits them. Retain meaningful stage direction only when useful.
3. **Join line-broken speech.** Restore sentences and readable paragraphs; use blank lines between paragraphs.
4. **Punctuation and case.** Repair obvious caption punctuation and capitalization without changing meaning.
5. **Filler.** Remove excessive `uh`, `um`, stutters, and accidental repeated words. Keep natural speech, rhetorical questions, and audience interaction when they carry voice or meaning.
6. **Repeated greetings.** In a stitched or multipart presentation, omit redundant restart greetings only when the user asks for a continuous clean edition or has said they are unnecessary. Do not remove substantive recaps that advance the argument.
7. **Headings.** Add short descriptive headings at genuine topic changes. Headings are editorial navigation, not a substitute for transcript text.
8. **Quotes.** Preserve quoted wording as supplied. Use quotation marks and italicized titles consistently, but do not silently modernize or harmonize a quotation.
9. **Speaker labels.** Use them only for genuine multi-speaker dialogue where labels aid comprehension.
10. **Spelling.** Follow `SPELLING.md` when relevant. Correct ASR only when the intended form is clear; preserve historically meaningful forms inside quotations.
11. **Fidelity check.** Target approximately 90–100% body retention after permitted removals. For high-trust work, compare normalized source and output tokens and document the result.

## Source preservation and research

### Absolute rule

A named source or claim in the transcript is evidence about what the speaker said. Never replace, silently correct, delete, or reattribute it—even if:

- the exact quotation cannot be located;
- a date or page appears wrong;
- a stronger primary source is available;
- a modern legal or historical source qualifies the statement; or
- secondary sources disagree.

Keep the spoken wording in the transcript. Add research after the relevant section.

### Verification tiers

Use the narrowest accurate tier in internal editorial/research records:

- **Verified — primary text:** exact wording or claim located in the original document or an authoritative official transcription.
- **Verified — facsimile/transcription:** exact material located in a scan, facsimile, or reliable transcription of the cited edition.
- **Verified — reliable edition:** the material is located in a reputable published edition, though not the original artifact.
- **Located — contemporary report:** a contemporary news report or recording documents the event or quotation.
- **Located — bibliographic trail:** the citation can be traced to a named secondary work, but the requested original has not been inspected.
- **Corroborating context:** a strong source supports the surrounding event, date, law, or historical setting without proving the transcript's exact words.
- **Source follow-up needed:** the named source, page, exact quotation, or original edition was not located.

Do not assign `verified` without an exact bibliographic or linked basis. These tiers are internal editorial metadata unless the user specifically requests a research audit; do not turn them into public-facing badges or prefixes in the transcript companion. A stronger source may be listed in addition to the transcript source; it may never replace it.

### Discrepancies

Keep date, wording, legal-status, and attribution discrepancies outside the transcript in a short source note. State what the located source says, what the transcript says, and what still needs confirmation. Avoid turning a source note into an argument with the speaker.

## Choose an end-matter pattern

### Pattern A — compact Quick Reference

Use for a short or single-topic transcript. Append one presentation-order `Quick Reference` after the body with Bible, EGW/SOP when applicable, and Other Sources. Omit empty categories.

```markdown
---

## Quick Reference

### Bible verses
| Ref | Key point from the passage |
|---|---|
| Revelation 13:11 | A second beast rises from the earth with two lamb-like horns and a dragon-like voice |

### Other sources

**<Source as named in transcript>**

<What the source contains and why it is relevant.> [View Source Material](<stable URL>)
```

### Pattern B — section-aware follow-along edition

Use for several major topics, long-form downloads, or an explicit request for a study companion.

At the end of each major topic, add in this order:

1. `<Topic> Scripture Guide`
2. Historical, church, constitutional, legal, or other documentary sources appropriate to that topic

After all topics, add:

3. `Master Scripture Index`
4. `Source Follow-up Needed`
5. Transcript information or production notes when useful

Keep sources with the section where the audience encounters them. The master index is retained because it provides a single follow-along trail without forcing readers to hunt through three topic lists.

## Scripture Guide rules

- Include every distinct passage the speaker reads, names, or clearly builds an argument upon.
- Add genuinely useful cross-references generously when the user requests an expanded guide.
- References from the presentation receive no public usage label; their presence in the guide is sufficient.
- Put the exact label **Additional related source** immediately after the Bible reference only when a passage was added during study development. Never imply that an added verse was spoken.
- Describe the principal point of the passage itself in one clear sentence. Favor the text's subjects, actions, contrasts, promises, warnings, and stated interpretation over a personal application or generic devotional summary.
- Preserve the passage's immediate context; do not use the description to overstate a disputed conclusion.
- Use consistent full book names and en-dash verse ranges.

Example:

```markdown
### USA in Prophecy Scripture Guide

- **Daniel 7:24** The interpreting angel identifies horns as kings, kingdoms, or governing/ruling powers arising from a kingdom.
- **Revelation 13:11** The earth beast has two lamb-like horns, yet its voice becomes dragon-like.
- **Acts 5:29** *Additional related source* The apostles state that obedience to God takes precedence when human commands conflict with His command.
```

## Documentary source rules

- Repeat the transcript's named source in the source list even when unverified.
- Give author/institution, title, edition/date/page when known, a stable link, and a concise relevance note. Keep the verification tier in internal editorial metadata rather than displaying it as a public badge or prefix.
- References from the presentation receive no public usage label.
- Put **Additional related source** immediately after the source title only for supporting material added during research.
- In every public format, place the source title on its own line. Put the plain-language description on the next line, with `View Source Material` at the end of that description.
- Prefer primary and official sources; add facsimiles and reliable editions when originals are unavailable.
- Historical, constitutional, and legal sources belong under the section whose claim they illuminate.
- Avoid raw URL labels in Word/PDF. Use `View Source Material` by default; use a more specific equivalent such as `View Facsimile` only when it materially helps.
- Never claim a current law, official text, institutional position, or modern statistic without current verification.

## Source Follow-up Needed

This section is required whenever any source remains incomplete. Each item should say exactly what to obtain:

- original publication or edition;
- page number or archival shelf mark;
- scan, screenshot, book, or pamphlet;
- exact wording and surrounding context;
- unresolved date, attribution, or legal-status question.

Retain these notes in future revisions until the evidence is added. New evidence is appended or used to upgrade the verification tier; the transcript wording remains untouched.

## Master Scripture Index

For a section-aware edition, retain a final master list even though each topic has its own guide. Arrange it in approximate Bible order unless the user requests presentation order. For each entry include:

- reference;
- `Additional related source` immediately after the reference only when the passage was added; otherwise no usage label;
- text-centered description; and
- topic name(s) where it appears.

Deduplicate identical references while preserving all topic tags.

## Semantic HTML companion

When HTML is requested:

- Put the full transcript, Scripture Guides, source notes, and follow-up list in the DOM; do not hide essential content behind JavaScript.
- Use semantic landmarks (`header`, `nav`, `main`, `section`, `footer`), a skip link, logical headings, visible focus states, and meaningful link text.
- Use CSS custom properties for design tokens and a root `data-theme` attribute.
- Maintain one centralized theme registry/token source as the system of record. Generate or derive the CSS theme blocks, selector options, and JavaScript allowlist from that registry whenever the build environment permits.
- Components consume semantic aliases such as background, surface, text, muted text, accent, rule, focus, texture, and texture scale; do not scatter literal per-theme colors or texture data through component CSS.
- Support named themes through a selector and/or a stable query parameter such as `?theme=mark`; unknown values must fall back safely.
- Use clear public-facing names. A calm neutral-light option may be called `mild`; avoid internal placeholder names such as `bland` in the visible selector.
- The no-JavaScript state must remain complete and readable.
- Respect reduced motion and provide clean print styles.
- Keep metadata and JSON-LD accurate and avoid filler schema.
- Treat theme names as an extensible allowlist. Adding a future theme should require one registry entry/token block, including any self-contained texture and its scale, not a structural rewrite.
- Do not default every light theme to pastel washes or generic gradients. When the approved visual direction calls for texture, keep it subtle, self-contained, performance-light, contrast-safe, and removed in print.

## Quality checklist

- [ ] Raw source remains untouched
- [ ] No timestamps or caption counters remain
- [ ] Full spoken content retained after allowed removals
- [ ] Editorial headings do not replace transcript text
- [ ] Video URL and bare Video ID are correct when known
- [ ] Spelling and quotations are handled conservatively
- [ ] Every transcript source remains present
- [ ] Verification tiers match the evidence located and remain internal unless a research audit is requested
- [ ] Public references from the presentation have no usage label
- [ ] Only added Bible passages and supporting sources are labeled `Additional related source`, immediately after the reference/title
- [ ] Public documentary sources use title line, description line, and `View Source Material` at the description's end
- [ ] Scripture descriptions state key points from the passage itself
- [ ] Section sources follow each section in a multi-topic edition
- [ ] Master Scripture Index is included and deduplicated when using Pattern B
- [ ] Every unresolved source appears under `Source Follow-up Needed`
- [ ] No temporary landing-page URL or brittle deployment reference was inserted unless requested
- [ ] Word/PDF files were rendered and visually inspected; accessibility issues were fixed
- [ ] HTML works without JavaScript and passes ID/link/theme checks when supplied

<!-- Agent: Codex · Model: GPT-5 · Date: 2026-08-21 · Change: authoritative section-aware, source-preserving follow-along transcript specification. -->
