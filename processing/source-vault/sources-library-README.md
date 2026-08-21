# Canonical Bible Study Source Library

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-08-21 -->

The private `getrdone/bible-study-source-materials` repository is the source of truth for approved Bible-study sources. Consumer projects pin a commit snapshot; they do not maintain competing source libraries.

## Canonical structure

```text
registry.yaml
policy/
schema/
library/
  items/<source-id>/
    record.yaml
    original.<ext>   # only when permitted
    content.md       # only when permitted
    notes.md
  people/<person-id>.yaml
intake/
indexes/
database/
  schema.sql
  sources.sqlite3
scripts/
alignments/
```

Store each item once. Route one person or source into multiple authority classes, topics, passages, and expertise domains through metadata and generated indexes.

## Approval rule

A file is not authoritative merely because it exists. Use it as an authoritative input only when its record has applicable `approval.status: approved`, traceable provenance, usable rights, and any required checksum. Intake and under-review records remain non-authoritative.

Scripture in context and compared with Scripture is the final authority. Spirit of Prophecy, Reformers, Adventist pioneers, respected materials, and subject-matter experts remain distinct source classes and subordinate to Scripture.

## SQLite contract

Reviewed YAML and permitted Markdown are canonical. `database/sources.sqlite3` is rebuilt deterministically and provides searchable source metadata, headings, heading paths, page and paragraph/timestamp locators, Scripture routes, people, topics, expertise, authority, approval, alignments, and FTS5 content.

Never edit the database or generated indexes by hand. Validate canonical records, build SQLite, then validate the database. Verify consequential wording and locators against canonical records.

A future read-only HTML query surface may use the same database. It must not create another source store or write approval decisions.

## Intake

1. Inventory without deleting or moving originals.
2. Hash files and identify exact duplicates.
3. Verify identity, edition, provenance, rights, and permitted storage.
4. Create one source record and preserve headings, pages, timestamps, and locators during permitted extraction.
5. Keep restricted material local-only or link-only.
6. Obtain explicit approval and scope.
7. Add the record to the registry, rebuild indexes and SQLite, and pin the new snapshot in consumer projects.

Never replace a supplied source. Add corroboration, context, verified originals, and stronger evidence beside it.
