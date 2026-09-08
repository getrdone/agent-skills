# External skill sources

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-08 -->

## Cloudflare

- Upstream: https://github.com/cloudflare/skills
- Ownership: Cloudflare; treat upstream as authoritative.
- Local clone: `F:\\__ai-projects\\cloudflare-skills\\`
- Installation: symlink the needed official skill directories from that clone into each agent's normal skill-discovery directory.
- Update: add the clone to the existing `sync-canonical-repos.sh` fast-forward pull list, then run the existing symlink-repair step.
- Do not vendor, rewrite, or maintain a second Cloudflare instruction copy inside `getrdone/agent-skills`.
- Before relying on product limits, commands, configuration, or API behavior, use the official skill's live-documentation route.

## Specialized local skills

Trip- or project-specific skill trees do not belong in the default catalog. UBP and Plain Vision tooling lives in https://github.com/getrdone/ubp-tools and should be linked only on machines that need it.
