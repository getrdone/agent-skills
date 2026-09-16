# Mode 2 — Structured Transcript Format

Use this template whenever the user requests the structured / general-timecode / reference-list output.

## Full Template

```markdown
# Video Transcript

**Slug:** dOMHEm2No20
**Duration:** 42 min
**Channel:** Amazing Facts
**Series:** Standalone (series of one)

---

[~0–7 min]
Opening remarks and introduction of the topic. The speaker begins by reading from Scripture and sets the context for the study.

[~7–15 min]
Main exposition begins. Key points are developed around the theme of…  
(Here a Bible verse is cited: John 14:6)

[~15–22 min]
Further development. A quotation from the Spirit of Prophecy is introduced:  
“The greatest want of the world is the want of men…” (Education, p. 57)

[~22–30 min]
Practical application section…

[~30–42 min]
Closing appeal and final summary.

---

## Master Reference List

### Bible Verses
- John 14:6

### Spirit of Prophecy
- Education, p. 57 – “The greatest want of the world is the want of men…”

### Other Sources
- (none)
```

## Guidelines

- **Slug**: Prefer the 11-character YouTube video ID.
- **Duration**: Round to the nearest minute (e.g. “42 min”).
- **Channel**: Use the exact channel name returned by the API metadata.
- **Series**: Named series, or exactly `Standalone (series of one)`.
- **Section markers**: 5-, 7-, or 10-minute blocks as `[~start–end min]`. Never exact second timestamps in Mode 2.
- **Master list order is mandatory**: Bible Verses, Spirit of Prophecy, Other Sources.
- Empty categories still receive a heading followed by `(none)`.
- Keep body text as clean readable paragraphs. The body is the full spoken content, not a summary.
