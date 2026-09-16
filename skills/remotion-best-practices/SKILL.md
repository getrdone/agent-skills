---
name: remotion-best-practices
description: Router for all Remotion skills. Load only when the user asks for Remotion, compositions, captions, Player, Studio, or related video-code work.
version: 4.0.506
---

# Remotion best practices (router)

Load **only** the sibling skill named below. Do not load this router’s whole tree.

## Creating a video

If the user asks to make, create, or build a new video or composition, load [`../remotion-create/SKILL.md`](../remotion-create/SKILL.md), whether or not a Remotion project already exists.

## React markup

If writing Remotion React markup, load [`../remotion-markup/SKILL.md`](../remotion-markup/SKILL.md).

## Maps

For static maps, animated routes/markers, geographic explainers, Mapbox, MapLibre, MapTiler, GeoJSON, or 3D flyovers, load [`../remotion-maps/SKILL.md`](../remotion-maps/SKILL.md).

## Multimedia

For browser multimedia (trim, crop, metadata), load [`../remotion-multimedia/SKILL.md`](../remotion-multimedia/SKILL.md).

## Interactivity

For Studio interactivity write-back patterns, load [`../remotion-interactivity/SKILL.md`](../remotion-interactivity/SKILL.md).

## Rendering

For advanced rendering beyond `npx remotion render`, load [`../remotion-render/SKILL.md`](../remotion-render/SKILL.md).

## Remotion Studio

To launch Studio or configure Studio CLI flags, load [`../remotion-studio/SKILL.md`](../remotion-studio/SKILL.md).

## Captions

When working with captions, load [`../remotion-captions/SKILL.md`](../remotion-captions/SKILL.md).

## SaaS / Player / Lambda

For Remotion-powered apps (`<Player>`, Lambda/Vercel/Cloudflare rendering, templates), load [`../remotion-saas/SKILL.md`](../remotion-saas/SKILL.md).

## Docs lookup

To find current Remotion APIs/docs, load [`../remotion-docs/SKILL.md`](../remotion-docs/SKILL.md).

## Upgrading

To upgrade Remotion and related packages, load [`../remotion-upgrade/SKILL.md`](../remotion-upgrade/SKILL.md).
