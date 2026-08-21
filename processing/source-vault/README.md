# Source vault processing

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-08-21 -->

Tooling and rules for inventorying private Scripture source material before it enters the canonical **getrdone/bible-study-source-materials** repository.

| File | Role |
|------|------|
| `source_vault_inventory.py` | Cheap metadata inventory, hashes, change detection, and duplicate groups without loading full texts into chat |
| `source-record.schema.yaml` | Portable source-record schema mirrored for intake tooling |
| `sources-library-README.md` | Canonical repository layout, approval rules, and SQLite contract |
| `source-vault-codex-handoff.md` | Operator handoff for inventory, intake, quarantine, and publication |

**Not stored here:** private originals, approved source-library binaries, project-specific registries, generated indexes, or `sources.sqlite3`. Those live in the private source-materials repository or remain local-only when rights require it.
