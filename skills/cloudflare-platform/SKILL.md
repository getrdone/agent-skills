---
name: cloudflare-platform
description: Comprehensive guidance for building sites and apps on Cloudflare Pages, Workers, storage, AI, and security. Use when deploying static or dynamic sites, edge functions, full-stack apps, or integrating Cloudflare with HTML/CSS skills. Prefer live docs over trained knowledge. Triggers on Cloudflare, Workers, Pages, edge, deploy site, wrangler.
---

# Cloudflare Platform for Sites

Use this skill for any Cloudflare development related to sites, static hosting, edge compute, storage, or AI-enhanced web apps. Always prefer retrieval from current Cloudflare docs over baked-in knowledge.

## Core Decision Trees for Sites

### Hosting and compute choice
- Pure static site (HTML/CSS/JS) → Cloudflare Pages (Git-connected or direct upload)
- Static + light dynamic (forms, auth, API routes) → Pages + Pages Functions or Workers
- Full dynamic / API-heavy / stateful → Workers + Durable Objects or D1
- Real-time / multiplayer / coordination → Durable Objects
- Scheduled background work → Cron Triggers or Workflows

### Storage for sites
- Config, sessions, feature flags, cache → KV
- Relational data (users, content, orders) → D1
- Images, videos, downloads, large assets → R2
- Vector search / RAG over site content → Vectorize + Workers AI
- Secrets / API keys → Secrets Store or Wrangler secrets

### Performance and security defaults for sites
- Enable Cloudflare CDN + Auto Minify + Brotli
- Use Images product for on-the-fly resizing/optimization
- Turnstile for forms instead of traditional CAPTCHA
- WAF + Bot Management for protection
- Web Analytics for RUM Core Web Vitals

## Integration with Existing Site Skills

When building sites:

1. **Page craft** — Use `web-studio` (`deliverable-clone` / `deliverable-theme` / `deliverable-polish`). Do not load retired HTML helpers.
2. **Deploy and edge** — Layer this Cloudflare skill on top:
   - Put the finished HTML/CSS/JS into a Pages project.
   - Add Pages Functions or a Worker only where server-side logic is required.
   - Bind KV/D1/R2 as needed for dynamic data.
   - Use Wrangler for local dev and deploy.

## User-facing errors (required pattern)

- Show the user only what helps them fix the problem (what to check, what to try next).
- Never surface HTTP status codes, stack traces, binding names, or internal IDs in the UI.
- Log full technical detail to `console.error` and/or an ops table (D1) for troubleshooting.
- Prefer short, actionable copy.

## Recommended Workflow for a New Site

1. Clarify goal, audience, conversion action (`web-studio`).
2. Build or repair the page with `web-studio` before opening this skill.
4. Create a Cloudflare Pages project (or Workers site).
5. Add edge logic only if needed.
6. Configure caching, images, security, and analytics.
7. Deploy via Git integration or `wrangler pages deploy`.

## Retrieval Priority

Always fetch latest from https://developers.cloudflare.com/ before citing limits, pricing, or API shapes. When references and live docs conflict, trust the live docs.

## Anti-patterns

- Do not invent Cloudflare API signatures or limits from memory.
- Do not force Workers when pure Pages static is sufficient.
- Do not skip Core Web Vitals and security defaults Cloudflare already provides.
