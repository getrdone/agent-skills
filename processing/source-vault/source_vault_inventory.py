#!/usr/bin/env python3
# Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-08-21
"""Inventory a private source vault without copying or reading source content into AI context.

Lives in agent-skills under processing/source-vault/. The canonical private source repository owns registry, intake metadata, generated indexes, and SQLite.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_SOURCE_ROOT = Path(os.environ.get("SOURCE_VAULT_ROOT", ".")).expanduser()
IGNORED_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}
IGNORED_DIRS = {".git", ".svn", "__pycache__"}
DANGEROUS_EXTENSIONS = {
    ".apk", ".bat", ".cmd", ".com", ".dll", ".exe", ".jar", ".msi",
    ".ps1", ".scr", ".vbs",
}
ARCHIVE_EXTENSIONS = {".7z", ".gz", ".rar", ".tar", ".tgz", ".zip"}
TRANSCRIPT_EXTENSIONS = {".doc", ".docx", ".md", ".odt", ".pdf", ".rtf", ".txt"}
BOHR_MARKERS = {
    "bohr",
    "great prophecies of daniel and revelation",
    "prophecy's repeating sequence",
    "prophecys repeating sequence",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalized_relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def classify(relative_path: str, size: int, is_symlink: bool) -> tuple[str, list[str]]:
    lowered = relative_path.lower().replace("_", " ").replace("-", " ")
    extension = Path(relative_path).suffix.lower()
    reasons: list[str] = []

    if is_symlink:
        return "blocked", ["symlink-not-followed"]
    if size == 0:
        return "blocked", ["empty-file"]
    if extension in DANGEROUS_EXTENSIONS:
        return "blocked", ["executable-or-active-file"]
    if extension in ARCHIVE_EXTENSIONS:
        return "manual-review", ["archive-requires-inspection"]
    if extension in TRANSCRIPT_EXTENSIONS and any(marker in lowered for marker in BOHR_MARKERS):
        reasons.extend(["possible-stephen-bohr-transcript", "correction-and-rights-review-required"])
        return "needs-correction", reasons
    return "intake", ["metadata-and-rights-review-required"]


def load_previous(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def scan(source_root: Path) -> list[dict]:
    records: list[dict] = []
    for current_root, dir_names, file_names in os.walk(source_root, followlinks=False):
        dir_names[:] = sorted(
            name for name in dir_names
            if name not in IGNORED_DIRS and not (Path(current_root) / name).is_symlink()
        )
        for file_name in sorted(file_names):
            if file_name in IGNORED_NAMES:
                continue
            path = Path(current_root) / file_name
            relative_path = normalized_relative(path, source_root)
            is_symlink = path.is_symlink()
            modified_utc = None
            try:
                stat = path.lstat() if is_symlink else path.stat()
                size = stat.st_size
                modified_utc = datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat()
                status, reasons = classify(relative_path, size, is_symlink)
                checksum = None if is_symlink else sha256_file(path)
                error = None
            except OSError as exc:
                size = 0
                status = "blocked"
                reasons = ["read-error"]
                checksum = None
                error = str(exc)

            records.append({
                "path": relative_path,
                "extension": path.suffix.lower(),
                "mime_type": mimetypes.guess_type(file_name)[0] or "application/octet-stream",
                "size_bytes": size,
                "modified_utc": modified_utc,
                "sha256": checksum,
                "status": status,
                "reasons": reasons,
                "error": error,
            })
    return sorted(records, key=lambda item: item["path"].casefold())


def changes(previous: dict, current_files: list[dict]) -> dict:
    previous_by_path = {item["path"]: item for item in previous.get("files", [])}
    current_by_path = {item["path"]: item for item in current_files}
    added = sorted(set(current_by_path) - set(previous_by_path))
    removed = sorted(set(previous_by_path) - set(current_by_path))
    changed = sorted(
        path for path in set(previous_by_path) & set(current_by_path)
        if previous_by_path[path].get("sha256") != current_by_path[path].get("sha256")
    )
    return {"added": added, "changed": changed, "removed": removed}


def duplicate_groups(files: list[dict]) -> list[dict]:
    by_checksum: dict[str, list[str]] = defaultdict(list)
    for item in files:
        if item.get("sha256"):
            by_checksum[item["sha256"]].append(item["path"])
    return [
        {"sha256": checksum, "paths": sorted(paths)}
        for checksum, paths in sorted(by_checksum.items())
        if len(paths) > 1
    ]


def summary_markdown(manifest: dict) -> str:
    stats = manifest["statistics"]
    lines = [
        "# Private Source Vault Inventory",
        "",
        f"Generated: `{manifest['generated_utc']}`",
        "",
        "This report contains metadata only. It does not approve or upload source content.",
        "",
        "## Summary",
        "",
        f"- Files: {stats['total_files']}",
        f"- Intake: {stats.get('intake', 0)}",
        f"- Needs correction: {stats.get('needs-correction', 0)}",
        f"- Manual review: {stats.get('manual-review', 0)}",
        f"- Blocked: {stats.get('blocked', 0)}",
        f"- Duplicate groups: {len(manifest['duplicates'])}",
        "",
    ]
    for status, heading in (
        ("blocked", "Blocked files"),
        ("needs-correction", "Stephen Bohr transcript candidates"),
        ("manual-review", "Files requiring manual inspection"),
    ):
        selected = [item for item in manifest["files"] if item["status"] == status]
        if selected:
            lines.extend([f"## {heading}", ""])
            for item in selected:
                lines.append(f"- `{item['path']}` — {', '.join(item['reasons'])}")
            lines.append("")

    delta = manifest["changes"]
    lines.extend([
        "## Changes since the previous inventory",
        "",
        f"- Added: {len(delta['added'])}",
        f"- Changed: {len(delta['changed'])}",
        f"- Removed: {len(delta['removed'])}",
        "",
        "The complete file list and checksums are in `source-vault-inventory.json`.",
        "",
    ])
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--write", action="store_true", help="Write JSON and Markdown reports into sources/intake.")
    parser.add_argument("--fail-on-blocked", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_root = args.source_root.expanduser().resolve()
    repo_root = args.repo_root.expanduser().resolve()
    output_dir = repo_root / "intake" / "_inventory"
    json_path = output_dir / "source-vault-inventory.json"
    markdown_path = output_dir / "source-vault-inventory.md"

    if not source_root.is_dir():
        print(f"Source folder not found: {source_root}", file=sys.stderr)
        return 2
    if not (repo_root / "registry.yaml").is_file():
        print(f"Canonical source registry not found beneath: {repo_root}", file=sys.stderr)
        return 2

    previous = load_previous(json_path)
    files = scan(source_root)
    status_counts: dict[str, int] = defaultdict(int)
    for item in files:
        status_counts[item["status"]] += 1

    manifest = {
        "version": 1,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "source_root_label": "private-local-source-vault",
        "statistics": {"total_files": len(files), **dict(sorted(status_counts.items()))},
        "changes": changes(previous, files),
        "duplicates": duplicate_groups(files),
        "files": files,
    }

    if args.write:
        output_dir.mkdir(parents=True, exist_ok=True)
        json_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        markdown_path.write_text(summary_markdown(manifest), encoding="utf-8")
        print(json_path)
        print(markdown_path)
    else:
        print(summary_markdown(manifest))

    if args.fail_on_blocked and status_counts.get("blocked", 0):
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
