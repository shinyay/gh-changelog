#!/usr/bin/env python3
"""List English Markdown entries that are missing Japanese translation files.

Mapping:
- EN: changelogs/<stem>.md (excluding index.md)
- JP: changelogs-jp/<stem>-jp.md

This supports a Copilot Chat human-in-the-loop translation workflow.
"""

from __future__ import annotations

import argparse
import os
from typing import List, Tuple


def find_markdown_entries(output_dir: str) -> List[str]:
    entries: List[str] = []
    for name in os.listdir(output_dir):
        if not name.endswith(".md"):
            continue
        if name == "index.md":
            continue
        entries.append(os.path.join(output_dir, name))
    return sorted(entries)


def expected_jp_path(jp_dir: str, en_md_path: str) -> str:
    stem = os.path.splitext(os.path.basename(en_md_path))[0]
    return os.path.join(jp_dir, f"{stem}-jp.md")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="List EN changelog Markdown files missing JP translations"
    )
    parser.add_argument(
        "--en-dir",
        default="changelogs",
        help="Directory containing English Markdown entries",
    )
    parser.add_argument(
        "--jp-dir",
        default="changelogs-jp",
        help="Directory containing Japanese Markdown entries",
    )
    args = parser.parse_args()

    en_dir = os.path.abspath(args.en_dir)
    jp_dir = os.path.abspath(args.jp_dir)

    if not os.path.isdir(en_dir):
        raise SystemExit(f"EN dir not found: {en_dir}")
    if not os.path.isdir(jp_dir):
        raise SystemExit(f"JP dir not found: {jp_dir}")

    en_entries = find_markdown_entries(en_dir)
    if not en_entries:
        print(f"No EN Markdown entries found under: {en_dir}")
        return 1

    missing: List[Tuple[str, str]] = []
    for en_md in en_entries:
        jp_md = expected_jp_path(jp_dir, en_md)
        if not os.path.exists(jp_md):
            missing.append((en_md, jp_md))

    if not missing:
        print(f"All {len(en_entries)} entries have JP translations in: {jp_dir}")
        return 0

    print(f"Missing JP translations: {len(missing)}/{len(en_entries)}")
    for en_md, jp_md in missing:
        print(
            f"- {os.path.basename(en_md)} -> {os.path.relpath(jp_md, os.getcwd())}"
        )

    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        raise SystemExit(0)
