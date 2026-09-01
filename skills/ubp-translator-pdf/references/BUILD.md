# Build translator-review PDFs

<!-- Agent: Grok · Model: Grok 4.5 · Thinking: not exposed · Date: 2026-09-01 -->

Companion to `skills/ubp-translator-pdf/SKILL.md`. Update the **status** table when you ship or rebuild a PDF.

## Tools (names only)

Full rows: repo `tools/TOOLS.md` → **Unlocking Bible Prophecies translator PDFs**.

| Piece | What it does |
|-------|----------------|
| Windows PowerShell 5.1 | Hosts `build-translator-pdf.ps1` |
| `System.Windows.Forms.RichTextBox` | RTF speaker notes → plain text (STA) |
| `System.Drawing` | Resize + grayscale JPEG thumbs; optional invert of dark cards |
| Microsoft Edge headless | HTML → PDF (`--print-to-pdf --no-pdf-header-footer`) |
| Modular `_Sequence/*.pvs` | Edited slide order (`SlideName` + `SlideLocation`) |
| Xodo PDF (Pixel) | Markup of travel-review PDFs only |

Do not start from reportlab / the bundled Grok `pdf` skill unless Edge print is impossible.

## Pipeline

1. Close Plain Vision.
2. Read Modular `Modified Programs/Modular/_Sequence/pvUBP NNN.pvs`. Count `<SlideName>` — that is the deck.
3. For each `SlideName`: image from Malagasy originals (fallback English Original, then Modular); notes from Modular English `{jpg}.rtf` (fallback Original English).
4. Write grayscale thumbs under `thumbs/Malagasy/` (invert on) or `thumbs/Malagasy-plain/` (`-NoInvert`).
5. Write letter HTML: ordinal + notes + thumb + `ubp-NN-NNN` caption. CSS `@page` footer; Edge `--no-pdf-header-footer` so Chrome/Edge chrome does not double the footer.
6. Print via Edge with kit `_edge-profile` as `--user-data-dir`.
7. Open the PDF. Confirm first/last slides vs the `.pvs`. Page count is **not** equal to slide count (several slides per letter page).

## Builder flags

Script: `Documents/UBP-translator-pdf/build-translator-pdf.ps1`

| Flag | Default | Meaning |
|------|---------|---------|
| `-Sermon` | `3` | Sermon number (`pvUBP {0:d3}`) |
| `-SermonTitle` | `THE SIGNS` | Used in banner and output filename |
| `-Version` | empty | Suffix on HTML/PDF (`v2` → `…-translator-v2.pdf`) and copies notes to `notes-v2/pvUBP NNN/` |
| `-TargetPages` | `0` | `0` = full deck. `10` = sample; builder walks slide count until PDF page count matches |
| `-MaxSlides` | `0` | Cap how many sequence slides to include |
| `-NoInvert` | off | Grayscale only; thumbs look like the filmstrip |
| `-ForceThumbs` | off | Delete that sermon’s thumb folder and rebuild |

Print default (current v2 decks): invert dark-blue / near-black slides, lift photo shadows. Intermediate “plain” experiment: `UBP-03-THE-SIGNS-translator-v2-plain.pdf` (`-NoInvert`). Final call from the 2026-08-28 session was invert-on for toner.

### Commands

Sample (do this first on a new layout):

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Users\ion\Documents\UBP-translator-pdf\build-translator-pdf.ps1" -Sermon 3 -SermonTitle "THE SIGNS" -TargetPages 10
```

Full deck, inverted v2:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Users\ion\Documents\UBP-translator-pdf\build-translator-pdf.ps1" -Sermon 9 -SermonTitle "THE RESCUE" -Version v2
```

Filmstrip-look (no invert):

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Users\ion\Documents\UBP-translator-pdf\build-translator-pdf.ps1" -Sermon 3 -SermonTitle "THE SIGNS" -Version v2 -NoInvert
```

### Output names

- Full: `UBP-{nn}-{TITLE}-translator{-Version}.pdf`
- Sample: `UBP-{nn}-{TITLE}-translator-sample-{N}pp{-Version}.pdf`
- HTML sibling: `ubp-{nn}{-Version}.html`

Hardcoded in the script: `$libRoot` and `$outDir` under `C:\Users\ion\Documents\…`. Change those two lines if the library is not on this laptop.

## UBP #11 travel-review (different job)

`build-ubp11-travel-review.ps1` is **not** the standard translator PDF.

- Part 1: customized Modular notes, small inverted Malagasy thumbs, yellow **CHANGED** vs original.
- Part 2: only slides that differ; green = added, red strike = dropped.
- Phone markup: `UBP-11-HOW-TO-REVIEW-ON-PIXEL.txt` (Xodo on a Pixel). Copies also went to `Desktop/-- travel/`.

If the user asks for a translator PDF of #11, run `build-translator-pdf.ps1 -Sermon 11 -SermonTitle "THE NEW LIFE" -Version v2` unless they want the diff review again.

## Madagascar campaign order

From `Documents/# AWR Sermon Order  wNotes.md`. Modular counts are `<SlideName>` in `Modified Programs/Modular/_Sequence` as of 2026-09-01. Original `_Sequence` is the untrimmed stock deck — do not use it when Modular exists.

| Night | # | Title | Modular slides | Original slides | Translator PDF |
|-------|---|-------|----------------|-----------------|----------------|
| Fri | 01 | THE PREDICTION | 62 | 62 | **not built** |
| Sat AM | 03 | THE SIGNS | 50 | 72 | `UBP-03-THE-SIGNS-translator-v2.pdf` (also sample, v3, v2-plain) |
| Sat PM | 04 | THE WARNING | 53 | 72 | `UBP-04-THE-WARNING-translator-v2.pdf` |
| Sun | 05 | THE WAY | 43 | 74 | `UBP-05-THE-WAY-translator-v2.pdf` — built when deck was 74; **rebuild** if sharing current Modular 43 |
| Mon | 06 | THE AUTHENTIC SEAL | 42 | 79 | `UBP-06-THE-AUTHENTIC-SEAL-translator-v2.pdf` — built as 46 slides / 9 pages; **rebuild** if sharing current Modular 42 |
| Tue | 11 | THE NEW LIFE | 68 | 71 | travel-review only (`UBP-11-THE-NEW-LIFE-travel-review.pdf`); standard translator PDF **not built** |
| Wed | 09 | THE RESCUE | 59 | 59 | **not built** |
| Thu | 08 | THE GRAVE | 67 | 67 | **not built** |
| Fri | 10 | THE DESOLATION | 59 | 60 | **not built** |
| Sat AM | 15 | THE REMNANT | 61 | 61 | **not built** |

Stock sermons not in this campaign (skip unless asked): 02 THE FALL, 07 THE COUNTERFEIT, 12 THE BEAST, 13 THE MARK, 14 THE HARLOT, 16 THE GREAT CONTROVERSY, 17 THE WORTH OF A SOUL.

Next likely builds: 01, 09, 08, 10, 15, then standard #11, then rebuild 05/06 if Modular trim should be what the translator sees.

## Library map (do not dump)

```
Unlocking Bible Prophecies 2/
  Original Programs/          downloaded repo
    _Sequence/pvUBP NNN.pvs
    English/pvUBP NNN/*.jpg + *.jpg.rtf + *.jpg.hsh
    Malagasy/pvUBP NNN/*.jpg + *.hsh     (no notes)
  Modified Programs/          user overlays
    Modular/_Sequence/pvUBP NNN.pvs      ← PDF order
    Modular/English/pvUBP NNN/*.jpg.rtf  ← customized notes
    My Campaign/                         (ending-title patch kit, not PDFs)
```

English `.hsh` is SHA-384 of the JPEG only, Base64. Malagasy `.hsh` is SHA-256 hex of the JPEG. Irrelevant to PDF build; needed if replacing slide images.

## What not to do

- Do not git-add `thumbs/`, `_edge-profile/`, `_pdfcheck*/`, `video-frames/`, or the PDF binaries.
- Do not invert *and* claim the thumb still matches the filmstrip.
- Do not restore notes from Original English when a Modular `.rtf` exists.
- Do not change ending-title JPEGs from this skill (that is `UBP-ending-slides-patch`).
- Do not download a language pack without `UBP-save-my-notes` backup/restore.
