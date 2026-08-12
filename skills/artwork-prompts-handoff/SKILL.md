---
name: artwork-prompts-handoff
description: >
  When thumbnails, graphics, mood art, hero images, or other artwork are needed, write a complete
  prompts file for the human to generate assets manually (Canva, Leonardo, Midjourney, Photoshop, etc.).
  Do not call paid image APIs or Canva/Leonardo MCP unless the user explicitly asks and confirms credits.
  Use when the user needs image prompts, art brief, thumbnail concepts, visual assets handoff, or
  "I'll make the images myself".
---

# Artwork prompts handoff

**Default for artwork:** produce a **prompts file** the human runs one-by-one in their own tools.  
**Do not** use Canva MCP, Leonardo MCP, or other paid image APIs unless the user **explicitly** asks and confirms they have credits/budget.

Optional paid connectors stay documented under `_agent-control/mcp/` for later; they are **not** part of this skill’s default path.

## Load with visual work

If the task is ministry/Scripture/video packaging, also load curiosity skill `references/visual-system.md` and skim `dynamic-symmetry-glossary.md` when composition matters.

## When this skill fires

- Thumbnails, YouTube art, channel banners  
- Hero / section images for web pages  
- Mood boards, style frames, illustration directions  
- Any “generate image / make art / design this graphic” without confirmed API credits  

## Output: one prompts file (canonical)

Create or update **one** canonical file in the project work root (or topic folder):

```text
prompts/artwork-prompts.md          # preferred (folder of prompt packs)
# or
<stem>.artwork-prompts.md           # flat series folders
```

Use **no agent suffix** on the handoff file unless the user asked for a multi-agent draft (`artwork-prompts_grok.md`).

If `prompts/` does not exist, create it. Do not wipe existing prompt packs—add a dated section or a new file `prompts/artwork-prompts-<slug>.md`.

## File structure (required)

```markdown
# Artwork prompts — <project / episode / topic>

**Status:** awaiting human generation  
**Created:** <date>  
**Agent vision summary:** <2–4 sentences: what the set must achieve together>

## How to use (human)

1. Open your tool (Canva, Leonardo, Midjourney, Photoshop gen, etc.).
2. Work **top to bottom**; one prompt = one asset unless noted.
3. Save each file using the **Target filename** into `mood/` or `deliverables/assets/` (create folders if missing).
4. Tick the checkbox when done. Tell the agent when a batch is ready for layout.

## Shared style lock (apply to every prompt unless overridden)

- **Tone / adjectives:** …
- **Palette direction:** … (grayscale hierarchy first in final layout)
- **Typography note (if text in image):** … (prefer ≤4 words on thumbs)
- **Composition:** dynamic symmetry soft standard — ratio + grid note below per asset
- **Must avoid:** fear-porn, nude/sexual imagery, fake evidence, clutter, unreadable type
- **Negative prompt (global):** blurry, low quality, watermark, stock-photo look, extra fingers, … 

## Prompt list

### P01 — <short title>
- [ ] **Done**
- **Role:** thumbnail | hero | section | icon | mood | other
- **Target filename:** `deliverables/assets/p01-….png` (or .jpg)
- **Aspect / size:** 16:9 (1280×720) | 1:1 | 9:16 | …
- **DS / armature:** root 3 / phi / … · grid hint: `Phi-Black.png` or “basic diagonals+eyes”
- **Primary subject:** …
- **Text on image (if any):** `"…"` — max ~4 words for thumbs
- **Prompt (paste this):**

```text
…
```

- **Alt / accessibility text:** …
- **Notes:** complements title “…”; do not resolve the curiosity gap in the image

### P02 — …
```

Include **every** asset the vision needs in this first pass when possible (batch handoff). If the user only asked for one image, still use this format with a single `P01`.

## Prompt quality rules

1. **Self-contained** — each prompt pastes alone; no “same as above” without repeating locks.  
2. **Specific** — subject, setting, lighting, camera/angle, mood, color notes, what *not* to show.  
3. **Honest** — no invented real people, fake documents, or sensational prophecy gore.  
4. **Complements copy** — for YouTube, image + title share one promise; image doesn’t answer the whole question.  
5. **Filename targets** — stable, kebab-case, numbered so sort order matches the list.  
6. **Checkboxes** — so the human can track one-by-one progress.  
7. After assets exist, **do not regenerate the whole prompts file** unless asked; update statuses or add `P0n` only.

## Agent behavior after handoff

1. Stop generative-art work at the prompts file (plus any layout wireframes that don’t need pixels).  
2. Tell the user clearly: *“Credits/API not used — prompts are in `…`. Generate in order and drop files in `…`.”*  
3. When the user says assets are ready, read `mood/` / `deliverables/assets/`, match filenames, continue layout/HTML/thumbnail pairing.  
4. If an asset is missing, point to the exact `P0n` still unchecked—don’t invent a new full set.

## Optional later: paid MCP

Only if the user says to use Canva/Leonardo **and** confirms credits:

- Follow machine MCP docs in `F:\__ai-projects\_agent-control\mcp\README.md`  
- Still keep or update the prompts file as the creative record  

## Relationship to other skills

| Skill / doc | Role |
|-------------|------|
| `curiosity-driven-scripture-journey` + `visual-system.md` | Vision, DS, type, palette |
| `dynamic-symmetry-glossary.md` | Armature vocabulary for each prompt’s DS line |
| `youtube-planning.md` | Title selected before final thumb art when packaging video |
| This skill | **Human generation handoff** |

## Done when

- [ ] `prompts/…` file exists with shared style lock + numbered prompts  
- [ ] Every needed asset has role, filename, aspect, paste-ready prompt  
- [ ] User knows where to save files and how to call the agent back  
