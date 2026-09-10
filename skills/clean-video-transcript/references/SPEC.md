# Clean Video Transcript — Spec (single source of truth)

Use for **any video-derived transcript**: sermons, lectures, teaching series, panels, YouTube captures, Stephen Bohr / Anchor / Secrets Unsealed / SUMtv, and similar.

## Goals
1. Readable full transcript matching established clean style.
2. Faithful spoken content (no abridgment, no invented teaching).
3. Correct Bible/EGW/historicist spellings (see `SPELLING.md`).
4. End-of-file **Quick Reference** for verses, EGW, and other sources in **presentation order**.

## Inputs / outputs
| Input | Output |
|-------|--------|
| Raw `*.txt` (timestamps, Title/URL/Video ID header) | Cleaned `*.md` next to source (same basename) |
| Do **not** modify raw `.txt` unless user asks | Leave already-clean files alone |

**Already clean** if `.md` has: `#` title header, no `[MM:SS]` timestamps, proper paragraphs, word count ≥ ~90% of source body, and (when required) Quick Reference end-matter.

## Header template
```markdown
# <Readable Title>
**<Speaker or channel>**
<Series / event line when known>
Video: <https://www.youtube.com/watch?v=...>
Video ID: <id>

---

[Music]

<cleaned body>
```

- **Video ID** is required: the bare YouTube id (e.g. `fhMi9OLR-xQ`), taken from the raw `.txt` `Video ID:` line or parsed from the URL (`v=` / `youtu.be/`). Enables deep-links (`&t=`) and tooling without re-parsing the URL.
- Optional: `Duration: ~NN minutes` under the series line when known.

## Body cleaning rules
1. **Full transcript** — preserve essentially all spoken content. No `[...]` summaries, no abridgment.
2. **Remove** timestamps (`[00:04]`, `[1:02:33]`), raw `Title:`/`URL:`/`Video ID:`/`====` blocks.
3. **Join** line-broken speech into paragraphs; blank line between paragraphs; occasional double blank for major section shifts.
4. **Punctuation & case** — proper sentence starts/ends; no random mid-sentence Title Case.
5. **Filler** — drop excessive `uh`/`um`/stutters/repeated words; keep natural speech (`you know` when natural, rhetorical questions, “Are you with me?”).
6. **Keep** `[Music]` at start (and end if in source).
7. **Quotes** — Scripture in `"double quotes"`; book titles in `*italics*` when named.
8. **No speaker labels** unless the source is genuinely multi-speaker dialogue and labels aid clarity.
9. **Spelling** — follow `SPELLING.md` (Bible, EGW, standard historicist/SDA usage). Prefer KJV/NKJV forms when Bohr quotes KJV (e.g. keep “brake” **inside** a KJV quote; modern “broke” in prose).
10. **Word-count target** — cleaned body ≈ 90–100% of source body (minus fillers/timestamps only).

## End-matter: Quick Reference (required on every cleaned file)

Append after the body (and final `[Music]` if present). **Order of appearance in the talk**, not alphabetical. First mention only for repeated refs (note “reused” only if helpful).

```markdown
---

## Quick Reference

### Bible verses
| Ref | Highlight |
|-----|-----------|
| Dan 2:20–21 | God changes times/seasons; removes/raises kings; gives wisdom |
| Rev 13:1–2 | Sea beast; dragon gives power, seat, great authority |

### Ellen White / Spirit of Prophecy
| Source | Highlight |
|--------|-----------|
| GC 49 | Compromise restrained by pagan persecution; then church enters courts of kings |
| PK 535 | Rise/fall of Babylon, Medo-Persia, Greece, Rome under Watcher and Holy One |

### Other sources
| Source | Highlight |
|--------|-----------|
| Gibbon, *Decline and Fall* | Rome’s iron dominion / trampling imagery as cited |
| Cardinal Manning (as quoted) | Empire’s fall frees papal temporal power |
```

### What to include
- **Bible:** every distinct passage the speaker reads, cites, or clearly hinges an argument on (e.g. “Daniel 8:14”, “go to Revelation 13”). Omit vague “the Bible says” with no ref.
- **EGW/SOP:** every named book+page or clearly identified quotation (GC, DA, PK, 5T, etc.). Use standard abbreviations when the speaker does; expand once if helpful (`GC` = *The Great Controversy*).
- **Other:** historians, papal docs, scholars, creeds, non-EGW books, newsletters—anything cited as authority or illustration with a nameable source.

### Highlight line rules
- **One short clause** (≈8–20 words): the point **in this talk**, not a full verse dump or multi-paragraph quote.
- Prefer **why the speaker used it** over a generic Bible-dictionary gloss.
- Use en-dash ranges: `Dan 9:24–27`, `Rev 13:11–17`.
- If only a book/page was given with no quote body, still list it with the claim made from it.

### What not to do
- Do not invent references not in the transcript.
- Do not renumber or reorder by canonical Bible order.
- Do not paste long quotations into the tables (body already has them).
- If a category has zero entries, omit that subsection (or write `*(none cited)*` only if user prefers explicit empty sections).

## Quality checklist (before finish)
- [ ] No timestamps; raw header gone
- [ ] Header matches template; Video URL + Video ID correct
- [ ] Full content retained (~90%+ words)
- [ ] Spellings match `SPELLING.md`
- [ ] Quick Reference present, presentation order, three tables as applicable
- [ ] Source `.txt` untouched

## Style anchors
- End-matter sample: `../examples/end-matter-sample.md` in this skill.
- If the consumer project has already-cleaned transcripts, match their paragraph tone; **do not abridge**.

<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 2026-09-10 · Fixed a relative path that did not resolve. -->
