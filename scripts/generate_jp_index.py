#!/usr/bin/env python3
"""Generate an index for Japanese translations under changelogs-jp/.

Creates/updates:
- changelogs-jp/index.md

It reads title/date from YAML front matter.
"""

from __future__ import annotations

import argparse
import os
from typing import Dict, List, Optional, Tuple


def find_markdown_entries(output_dir: str) -> List[str]:
    entries: List[str] = []
    for name in os.listdir(output_dir):
        if not name.endswith(".md"):
            continue
        if name == "index.md":
            continue
        entries.append(os.path.join(output_dir, name))
    return sorted(entries)


def _strip_yaml_quotes(value: str) -> str:
    v = value.strip()
    if len(v) >= 2 and ((v[0] == v[-1] == '"') or (v[0] == v[-1] == "'")):
        return v[1:-1]
    return v


def read_front_matter(path: str) -> Dict[str, str]:
    fm: Dict[str, str] = {}
    try:
        with open(path, "r", encoding="utf-8") as handle:
            first = handle.readline()
            if first.strip() != "---":
                return fm
            for line in handle:
                if line.strip() == "---":
                    break
                if ":" not in line:
                    continue
                key, value = line.split(":", 1)
                fm[key.strip()] = value.strip()
    except FileNotFoundError:
        return fm
    return fm


def write_file_if_changed(path: str, content: str) -> None:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as handle:
            if handle.read() == content:
                return
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate index for JP changelog translations")
    parser.add_argument(
        "--jp-dir",
        default="changelogs-jp",
        help="Directory containing Japanese Markdown entries",
    )
    args = parser.parse_args()

    jp_dir = os.path.abspath(args.jp_dir)
    if not os.path.isdir(jp_dir):
        raise SystemExit(f"JP dir not found: {jp_dir}")

    md_entries = find_markdown_entries(jp_dir)
    # It is OK for JP dir to be empty; still write an index.

    items: List[Tuple[str, str, str]] = []
    for md_path in md_entries:
        fm = read_front_matter(md_path)
        title = _strip_yaml_quotes(fm.get("title", "")).strip()
        date = _strip_yaml_quotes(fm.get("date", "")).strip()
        filename = os.path.basename(md_path)
        if not title:
            title = filename
        if not date:
            date = "????-??-??"
        items.append((date, title, filename))

    # Sort by date descending when possible.
    items.sort(key=lambda x: x[0], reverse=True)

    index_path = os.path.join(jp_dir, "index.md")
    lines = ["# GitHub Changelog Archive (JP)", "", "## Entries", ""]
    for date, title, filename in items:
        lines.append(f"- {date} — [{title}]({filename})")

    content = "\n".join(lines).strip() + "\n"
    write_file_if_changed(index_path, content)

    print(f"JP index updated: {os.path.relpath(index_path, os.getcwd())} (entries: {len(items)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
