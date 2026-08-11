# Handoff — Private Scripture Source Vault

Use with skill `curiosity-driven-scripture-journey` and this processing package.

## Paths (set per machine)

| Role | Example |
|------|---------|
| Agent-skills checkout | clone of `https://github.com/getrdone/agent-skills` |
| Consumer project | e.g. `scripture-discovery-journey` (content site / brief / `sources/`) |
| Private source folder | local-only Bible study materials (never commit unapproved originals) |

## Goal

Inventory, verify, classify, and register a private source collection without uploading copyrighted or unapproved originals into the agent-skills repo or the public web.

## Required operating rules

1. Read agent-skills `CATALOG.md`, then `skills/curiosity-driven-scripture-journey/SKILL.md`. Load only required references.
2. Read this folder’s `sources-library-README.md` and `source-record.schema.yaml`. In the **consumer project**, read `sources/registry.yaml` before source-dependent work.
3. Authority order: Scripture compared with Scripture; original-language work; named Reformers; named Adventist pioneers; approved trusted sources; other contemporary material only for a defined supporting purpose.
4. A trusted source is a research starting point, not blanket approval of every claim. Cite the exact work, episode, page, or timestamp.
5. Never infer rights or approval. Unknown rights means link-only or local-only until verified.
6. Never commit source-folder credentials, absolute private paths, executables, duplicate binaries, or unapproved copyrighted originals into agent-skills.
7. Do not modify the master skill during an ordinary intake task. Propose skill changes as a separate PR to agent-skills.

## Phase 1 — Cheap deterministic inventory

```bash
python3 processing/source-vault/source_vault_inventory.py \
  --source-root '/path/to/private-source-materials' \
  --repo-root '/path/to/consumer-project' \
  --write
```

Review inventory outputs under the consumer project’s `sources/intake/` (or the path the script reports). Stop on unreadable files, executables, unexpected symlinks, empty files, or suspicious archives.

## Phase 2 — Selective review

1. Group exact duplicates by SHA-256. Do not delete from the private source folder.
2. Create candidate source records only for accurately identified files.
3. Verify title, author, edition, date, publisher, URL, provenance, rights, attribution. Leave unknowns unknown.
4. Keep candidates in consumer `sources/intake/`. Only approved records with applicable scope enter `sources/library/` and `sources/registry.yaml`.
5. Review only files needed for the current task. Do not load the whole vault into model context.

## Transcript correction

Physical ASR transcripts may require correction before publication. Work one episode at a time against the official video; preserve meaning; fix transcription, punctuation, names, and references only. Prefer the `clean-video-transcript` skill for final polished markdown + Quick Reference when applicable.
