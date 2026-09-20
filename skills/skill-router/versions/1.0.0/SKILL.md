---
name: skill-router
description: Load a managed skill from the library when the user names it or types /skill-name. Ordinary chat loads no other managed skill.
---

# Skill router

Load a managed skill only when the user names it, types `/skill-name`, or says `load <skill>`. Default for ordinary chat is no other managed skill.

## Where the library is

1. `C:/Users/noise/.agents/skill-library/current.json` — `library` is the payload root.
2. If that file is missing, use this repository checkout and `release-index.json`.

Do not copy `versions/`, grids, or design references into an agent skill folder.

## How to match a name

Exact catalog name wins. Slash form `/web-studio` and `load web-studio` are the same skill.

Do **not** guess. The word “video” is not Remotion. “Page” is not `web-studio` unless the user named it.

If the name is not in `CATALOG.md`, say so. Do not invent an alias (`html-page-standard`, `studio-web`, and the other retired names are not skills).

## How to load

1. If you need the name list, read `CATALOG.md` (short rows only). Do not paste the table into the reply.
2. Read `skills/<name>/CURRENT` (or `STABLE` if asked, or an explicit version).
3. Read `skills/<name>/versions/<ver>/SKILL.md` and `manifest.json` from the payload / checkout.
4. Follow **only** that release. Never mix releases.

## Companions

Load another skill only when **both** are true:

- the loaded skill says that companion is required for this kind of work
- the **current user request** actually needs it

Do not load a stack because a catalog line says “no cap.” After this slice of work, drop companions. Do not keep them warm across a mode change (code vs graphics).

## Retired names

Refuse and point to `web-studio`:

`html-page-standard`, `studio-web`, `interactive-components`, `modern-css-design`, `modern-html-aeo`, `optimized-deliverables`

## Voice

Replies go to a person. No inner-agent talk. No router/payload/token jargon unless the user asked how loading works.
