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

## Output: agent-named prompts draft (until promote)

Create or update a **draft** prompts file — **always agent-named** until the user promotes a final pack (see repo `WORKSPACE.md` §3):

```text
prompts/artwork-prompts_<agent>.md           # first pass (preferred)
prompts/artwork-prompts_<agent>_v2.md        # re-run
# flat series folders:
<stem>.artwork-prompts_<agent>.md
```

**Do not** write bare `prompts/artwork-prompts.md` as the working file while the final pack is unchosen.  
**Promote** → copy the accepted draft to `prompts/artwork-prompts.md` (or `<stem>.artwork-prompts.md`) only when the user chooses that pack as final.

If `prompts/` does not exist, create it. Do not wipe existing prompt packs—keep prior `_<agent>_vN` files; write the next versioned draft.

## File structure (required)

```markdown
# Artwork prompts — <project / episode / topic>

**Status:** awaiting human generation  
**Created:** <date>  
**Agent:** <exact agent name that produced this file>  
**Model:** <exact model the agent ran on>  
**Agent vision summary:** <2–4 sentences: what the set must achieve together + the shared visual language that will tie every image>

## How to use (human)

1. Open your tool (Canva, Leonardo, Midjourney, Photoshop gen, etc.).
2. Work **top to bottom**; one prompt = one asset.
3. Save each file using the exact **Target filename**.
4. Tick the checkbox when done.

## Shared visual language (mandatory – apply to every prompt)

This is the single most important rule. All images in the set must feel like they belong to the same family.

- **Shared style / medium:** (e.g. painterly impressionistic with visible brushwork, or soft cinematic realism, etc.)
- **Shared color grade / palette:** list the core colors that must appear across the set
- **Shared lighting approach:** (e.g. soft golden first light, cool overcast, etc.)
- **Shared mood adjectives:** 4–7 words that every image must carry
- **Composition standard:** Dynamic Symmetry (never abbreviate as “DS”)
- **Global avoid list:** fear-porn, nude/sexual imagery, fake evidence, clutter, text-on-image unless explicitly required, modern objects, logos, watermarks, signatures, neon/candy colors, stock-photo look, cartoon/anime, children’s Bible illustration, glossy 3D, plastic textures

## Prompt list

### P01 — <short title>
- [ ] **Done**
- **Agent:** <name of agent writing this prompt> · **Model:** <model>
- **Role:** hero | section background | thumbnail | etc.
- **Target filename:** `deliverables/assets/p01-short-name.jpg`
- **Dimensions:** 16:9 — 1920×1080 (or exact required size)
- **Dynamic Symmetry armature:** Root 3 / Phi / etc. + short placement note
- **Alt text:** …
- **Notes:** (any special instructions)

**Prompt (copy everything inside the block):**

```text
<full self-contained prompt that includes:
- subject, setting, time of day, lighting
- the shared style + color grade + mood from the Shared visual language section above
- Dynamic Symmetry composition instructions written out
- exact dimensions if the tool needs them
- everything that must appear and everything that must be avoided
- no external references such as “same as above”>
```

### P02 — …
```

**Critical rules for every prompt**

1. One prompt = one image. Never combine assets.
2. The prompt itself must be fully self-contained and copy-paste ready. All style, color, lighting, composition, and negative instructions live inside the prompt text.
3. Always expand “DS” to the full words **Dynamic Symmetry**.
4. Dimensions must appear both in the notes above the prompt and inside the prompt when the tool benefits from it.
5. Begin the notes section with the agent name and model.
6. Creative concepts are required, but every image must share the same visual language defined at the top of the file so the set feels cohesive rather than like disconnected islands.
7. After assets exist, do not regenerate the whole prompts file unless asked.

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

- [ ] Agent-named draft exists (`prompts/artwork-prompts_<agent>.md` or `_vN`) with shared style lock + numbered prompts  
- [ ] Every needed asset has role, filename, aspect, paste-ready prompt  
- [ ] User knows where to save files and how to call the agent back  
- [ ] Canonical bare `artwork-prompts.md` was **not** used unless user already promoted that pack
