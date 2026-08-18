---
name: cloudflare-platform
description: Comprehensive guidance for building sites and apps on Cloudflare Pages, Workers, storage, AI, and security. Use when deploying static or dynamic sites, edge functions, full-stack apps, or integrating Cloudflare with HTML/CSS skills. Prefer live docs over trained knowledge. Triggers on Cloudflare, Workers, Pages, edge, deploy site, wrangler.
---

# Cloudflare Platform for Sites

Use this skill for any Cloudflare development related to sites, static hosting, edge compute, storage, or AI-enhanced web apps. Always prefer retrieval from current Cloudflare docs over baked-in knowledge.

**Note:** This is an optional deployment/edge layer. Do **not** make it the automatic starting point for every site. Build with `modern-html-aeo` + `modern-css-design` + `interactive-components` + `optimized-deliverables` first. Reach for this skill when the user asks about Cloudflare, Pages, Workers, edge deployment, or when a site is ready to be hosted/deployed.

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

1. **Content and structure** — Use `modern-html-aeo` and `optimized-deliverables` first. Produce clean, semantic, AEO/GEO-optimized HTML with strong Core Web Vitals posture.
2. **Styling** — Apply `modern-css-design` (container queries, cqi units, no viewport breakpoints for components).
3. **Interactivity** — Use `interactive-components` for progressive-enhancement UI (accordions, tabs, forms, calculators). Prefer CSS-first + clean vanilla JS.
4. **Deploy and edge** — Layer this Cloudflare skill on top:
   - Put the finished HTML/CSS/JS into a Pages project.
   - Add Pages Functions or a Worker only where server-side logic is required.
   - Bind KV/D1/R2 as needed for dynamic data.
   - Use Wrangler for local dev and deploy.

## Recommended Workflow for a New Site

1. Clarify goal, audience, conversion action (from optimized-deliverables / modern-html-aeo).
2. Design information architecture + visual hierarchy + Core Web Vitals constraints.
3. Build the self-contained or multi-page HTML with modern-css-design and interactive-components.
4. Create a Cloudflare Pages project (or Workers site).
5. Add edge logic only if needed (auth, form handling, dynamic data).
6. Configure caching, images, security, and analytics via Cloudflare dashboard or IaC.
7. Deploy via Git integration or `wrangler pages deploy`.

## Retrieval Priority

Always fetch latest before citing limits, pricing, API shapes, or config options:
- https://developers.cloudflare.com/
- Product changelogs
- Wrangler config schema
- @cloudflare/workers-types

When references and live docs conflict, trust the live docs.

## Key References (load on demand)

- Pages overview and Git deploys
- Workers and bindings
- D1 / KV / R2 patterns for sites
- Turnstile for forms
- Images product for media
- Wrangler CLI best practices
- Agents SDK if the site needs AI agents or chat

## Anti-patterns

- Do not invent Cloudflare API signatures or limits from memory.
- Do not force Workers when pure Pages static is sufficient.
- Do not bloat the client with heavy frameworks when edge + static HTML can handle the job.
- Do not skip Core Web Vitals and security defaults that Cloudflare already provides for free.
- Do not treat this skill as the default starting point for every new page or site.
