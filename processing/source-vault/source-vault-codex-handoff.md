# Handoff — Private Scripture Source Vault

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-08-21 -->

Use with skill `curiosity-driven-scripture-journey`, this processing package, and private repository `getrdone/bible-study-source-materials`.

## Paths

| Role | Example |
|------|---------|
| Agent skills | clone of `https://github.com/getrdone/agent-skills` |
| Canonical source library | clone of `https://github.com/getrdone/bible-study-source-materials` |
| Consumer project | e.g. `scripture-discovery-journey` with `source-library.lock.yaml` |
| Private source folder | local Bible-study material; never commit unapproved or restricted originals |

## Goal

Inventory, verify, classify, register, index, and query a private source collection without replacing supplied sources or uploading material whose rights are unknown.

## Required rules

1. Read `CATALOG.md`, the Scripture Journey skill, and `skills/curiosity-driven-scripture-journey/versions/<CURRENT>/references/source-governance.md`.
2. Read the source repository's registry and policy.
3. Use only approved records within scope. Scripture remains the final authority.
4. Preserve named sources and transcript wording; add stronger evidence alongside.
5. Store one item and cross-list through metadata.
6. Never infer rights, approval, page numbers, quotations, or agreement.
7. Keep unknown-rights material local-only or link-only.
8. Do not modify the master skill during ordinary intake work.

## Phase 1 — deterministic inventory

```bash
python3 processing/source-vault/source_vault_inventory.py \
  --source-root '/path/to/private-source-materials' \
  --repo-root '/path/to/bible-study-source-materials' \
  --write
```

Review `intake/_inventory/`. Stop on unreadable files, executables, unexpected symlinks, empty files, or suspicious archives.

## Phase 2 — selective ingestion

1. Group exact duplicates by SHA-256 without deleting originals.
2. Verify one needed source at a time.
3. Create its record under intake.
4. When permitted, normalize searchable text to `content.md` while preserving headings, page markers, timestamps, locators, and source wording.
5. Correct transcripts against the official recording; preserve meaning and named sources.
6. Obtain explicit approval before moving the item into the library and registry.

## Phase 3 — publish searchable state

```bash
python3 scripts/validate_sources.py
python3 scripts/build_source_db.py
python3 scripts/validate_sources.py --database database/sources.sqlite3
```

Commit canonical inputs, generated indexes, and the validated SQLite database together. Update each consumer project's pinned snapshot. The planned HTML query surface remains a future read-only view of the same database.

<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 2026-09-10 · Fixed a relative path that did not resolve. -->
