# Source vault processing

Tooling and rules for private Scripture source libraries used with **curiosity-driven-scripture-journey**.

| File | Role |
|------|------|
| `source_vault_inventory.py` | Cheap inventory (hashes, types) without loading full texts into chat |
| `source-record.schema.yaml` | Schema for per-source `record.yaml` |
| `sources-library-README.md` | How consumer `sources/` trees work (registry, intake, library) |
| `source-vault-codex-handoff.md` | Operator handoff for intake / quarantine work |

**Not stored here:** private originals, approved library binaries, or project-specific `registry.yaml`. Those stay in each consumer project (or offline vault).
