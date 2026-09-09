# Source Governance and Search

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-08-21 -->

Use this file for source ingestion, approval, classification, querying, source-aligned study work, and the generated SQLite database.

## Canonical source library

Use private repository `getrdone/bible-study-source-materials` as the source of truth. Consumer projects keep only a small `source-library.lock.yaml` containing the repository, exact commit snapshot, registry version, and database schema version used by that project.

Do not treat a consumer copy, cached extract, generated index, or SQLite row as a competing authority. If the canonical repository or pinned snapshot cannot be read, return `BLOCKED` for source-dependent work instead of silently substituting stale files.

## Authority classes

Use Scripture in context and compared with Scripture as the final authority. Keep these source classes distinct and allow a work or person to carry multiple classes or expertise tags without duplicating the source:

1. Scripture;
2. Hebrew, Aramaic, Greek, textual, translation, and historical tools;
3. Spirit of Prophecy;
4. named Reformers and Reformation primary works;
5. named Adventist founders and pioneers;
6. approved respected materials and subject-matter experts;
7. other historical or contemporary research for a defined supporting purpose;
8. creative inspiration, never doctrinal authority.

Approval is record-specific and scope-specific. Approval of one work does not approve every claim, work, channel, ministry, or author.

## Search workflow

1. Read the consumer's lock file and canonical `registry.yaml` at the pinned snapshot.
2. Identify the core passages, topics, people, expertise areas, and source classes.
3. Query the generated database with `scripts/query_sources.py` for routing and discovery.
4. Open the canonical `record.yaml` and relevant `content.md` section for exact wording, page, paragraph, heading, or timestamp verification.
5. Use only approved records whose scope covers the claim.
6. Record the exact source IDs, passages, and locators in the study alignment manifest.

SQLite defaults to approved-only results. Include unapproved material only during an explicit intake or review task.

## SQLite rule

`database/sources.sqlite3` is a deterministic view built from reviewed YAML records, permitted Markdown extracts, people records, and alignment manifests. It indexes source metadata, headings, heading paths, page labels, paragraph or timestamp locators, Scripture routes, topics, people, expertise, authority, approval, and full text.

Never edit SQLite by hand. After any approved record or extracted-text change:

```text
python3 scripts/validate_sources.py
python3 scripts/build_source_db.py
python3 scripts/validate_sources.py --database database/sources.sqlite3
```

Verify consequential quotations and locators against canonical records even when SQLite found them. A future read-only HTML query surface may use this database; it must not create another source store or write theological approvals.

## Ingestion workflow

1. Inventory without deleting, moving, or loading the entire private vault into context.
2. Hash files and group exact duplicates; never delete originals automatically.
3. Verify identity, provenance, edition, rights, and storage permission.
4. Create one canonical item record and cross-list it through metadata.
5. When permitted, extract to `content.md` while preserving wording, headings, page markers, timestamps, and paragraph locators.
6. Label transcript corrections; preserve the spoken message and named sources.
7. Keep restricted or unknown-rights originals local-only or link-only.
8. Leave the record in intake until the project owner explicitly approves its use and scope.
9. Rebuild indexes and SQLite only after validation.

Never replace a source supplied or named by the project owner. Add verified originals, corroboration, context, or stronger evidence beside it. If a reference cannot be found, record the unresolved item and request a screenshot, scan, edition detail, or physical-source check.

## Study alignment manifest

For a substantive study, record:

```yaml
study_id:
source_library:
  repository: getrdone/bible-study-source-materials
  snapshot:
source_records: []
scripture_passages: []
claims:
  - id:
    statement:
    type: scripture | quotation | historical | interpretation | application | inference | reconstruction | deduction | creative-explanation | expansion
    support:
      - source_id:
        locator:
        passage:
    status: supported | qualified | conflict | blocked
    notes:
```

Do not require a public page to expose this internal schema. Public citations remain readable; the manifest preserves reproducibility and agent handoff.

## Conflict and expansion rules

Do not silently contradict or harmonize applicable approved sources. Recheck Scripture, exact quotations, editions, locators, and approval scope. Record unresolved disagreement and return `BLOCKED` for the affected claim.

Allow new ideas, analogies, applications, and deductions only when rooted in Scripture, Spirit of Prophecy, or traceable scripturally aligned reasoning. Label the claim type and never present an expansion as a quotation or as the source author's own statement.
