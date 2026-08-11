# Authoritative Source Library

This area holds source documents, links, and records used as starting places and reference material for Scripture Journey work.

## Authority rule

A file is not authoritative merely because it is present. Agents must read `sources/registry.yaml` first and may treat a source as an authoritative project input only when its record has:

- `approval.status: approved`;
- an approval scope that covers the current task;
- traceable provenance;
- a checksum for any stored original;
- usable rights and attribution information.

`sources/intake/` is a holding area only. Intake files are never authoritative until reviewed and registered.

## Structure

```text
sources/
  registry.yaml
  schema/source-record.schema.yaml
  intake/
  library/
    scripture/
    textual-tools/
    reformation/
    adventist-pioneers/
    trusted/
    historical/
    contemporary/
    creative/
```

Store each approved item under:

```text
sources/library/<category>/<source-id>/
  record.yaml
  original.<ext>   # only when storage/redistribution is permitted
  notes.md         # optional, derivative, and clearly labeled
```

## Source classes

1. Scripture and approved translation records
2. Hebrew, Aramaic, and Greek textual tools
3. Named Reformation witnesses
4. Named early Adventist pioneer witnesses
5. Project-approved trusted sources
6. Other historical material
7. Contemporary material used for documented positions or research
8. Creative inspiration, never doctrinal authority

## Intake workflow

1. Place or link the new source in `sources/intake/`.
2. Create and verify its `record.yaml`.
3. Check authorship, title, edition, date, locator, and checksum.
4. Record copyright, license, allowed uses, required attribution, and whether the original may be committed.
5. Review the source and set the truthful approval status and scope.
6. Move approved, legally storable material into the matching library category and add it to `registry.yaml`.
7. Keep restricted material link-only unless permission allows storage.

Inclusion records provenance; it does not make any human source equal to Scripture. Every commentary, Reformer, pioneer, teacher, lexicon, grammar, and trusted source remains subordinate to Scripture.
