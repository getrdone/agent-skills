---
name: ubp-translator-pdf
description: >
  Build toner-saving translator-review PDFs for Unlocking Bible Prophecies 2 /
  Plain Vision: English notes on the left, grayscale Malagasy slide on the right.
  Use when the user mentions translator PDF, UBP PDF, prophecy series PDF,
  printable notes for the translator, Plain Vision review PDF, or /ubp-translator-pdf.
---

<!-- Agent: Grok · Model: Grok 4.5 · Thinking: not exposed · Date: 2026-09-01 -->

# Unlocking Bible Prophecies translator PDFs

Canonical procedure for all agents. Load this skill only; then open `references/BUILD.md` before running a build. Tool names live in repo `tools/TOOLS.md` (section **Unlocking Bible Prophecies translator PDFs**).

Workspace rules in repo `WORKSPACE.md` still apply. PDFs are work artifacts on the machine that has the Plain Vision library — do not commit thumbs, Edge profiles, or generated PDFs into git.

## Always

- Close Plain Vision before copying or replacing library files.
- Find the library by folder fingerprint `Unlocking Bible Prophecies 2/Original Programs`, not by Windows/Mac username.
- Slide **order and count** come from Modular `_Sequence` `*.pvs` (`SlideName` list). Never invent order from a folder listing.
- Center filmstrip thumbnail in Plain Vision is the projected slide. Notes on the top pane match the same `SlideName`.
- Notes: customized Modular English `{jpg}.rtf` first; fall back to Original English `{jpg}.rtf`. Malagasy pack is slides only (no `.rtf`).
- Layout: ordinal left, English notes, grayscale thumb right, caption `slide N | ubp-NN-NNN`.
- Default print path **inverts** dark-blue verse/title cards and near-black slides (toner). `-NoInvert` keeps thumbs looking like the filmstrip.
- Prefer the existing builder over the bundled Grok `pdf` skill (reportlab). Established pipeline is HTML + Edge headless `--print-to-pdf`.
- Build a 10-page sample (`-TargetPages 10`) before a full deck when the user has not already approved the layout for that sermon.

## Kit (work machine)

Laptop (Steve / ion):

| Role | Path |
|------|------|
| Library | `Documents/Presentations for Plain Vision Software/Unlocking Bible Prophecies 2` |
| Builder kit | `Documents/UBP-translator-pdf/` |
| Standard builder | `build-translator-pdf.ps1` |
| UBP #11 travel-review (notes vs original diffs) | `build-ubp11-travel-review.ps1` |
| Related kits | `Documents/UBP-save-my-notes/`, `Documents/UBP-ending-slides-patch/` |

On another machine, locate the library by the fingerprint above, then copy the two `.ps1` files next to an output folder. Edit `$libRoot` / `$outDir` at the top of the script if the paths differ.

## Build (standard translator PDF)

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Users\ion\Documents\UBP-translator-pdf\build-translator-pdf.ps1" -Sermon 3 -SermonTitle "THE SIGNS" -Version v2
```

Flags: `-Sermon`, `-SermonTitle`, `-Version`, `-TargetPages`, `-MaxSlides`, `-NoInvert`, `-ForceThumbs`. Details in `references/BUILD.md`.

Campaign night order, titles, Modular slide counts, and which PDFs already exist: `references/BUILD.md`.

## Related local Grok skill

Notes backup/restore and ending-title image patch stay in the machine skill `ubp-plain-vision` (`~/.grok/skills/ubp-plain-vision/`). This skill is PDF-only.

## Done when

- [ ] Sequence slide count matches the Modular `.pvs` (not Original, unless Modular is missing)
- [ ] PDF opened; first and last thumbs match first and last `SlideName`
- [ ] Notes are the customized Modular text, not stock-only unless Modular `.rtf` is absent
- [ ] User has a path to the PDF; do not close a result window until they have seen it
