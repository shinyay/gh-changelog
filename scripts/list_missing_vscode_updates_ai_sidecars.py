#!/usr/bin/env python3
"""List VS Code Updates Markdown entries that are missing AI sidecar JSON files."""

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


def expected_sidecar_path(ai_dir: str, md_path: str) -> str:
    stem = os.path.splitext(os.path.basename(md_path))[0]
    return os.path.join(ai_dir, f"{stem}.ai.json")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="List VS Code Updates Markdown files missing AI sidecars"
    )
    parser.add_argument(
        "--output-dir", default="vscode-updates", help="Directory containing Markdown entries"
    )
    parser.add_argument(
        "--ai-dir",
        default=os.path.join("vscode-updates", "_ai"),
        help="Directory for AI JSON sidecars",
    )
    args = parser.parse_args()

    output_dir = os.path.abspath(args.output_dir)
    ai_dir = os.path.abspath(args.ai_dir)

    if not os.path.isdir(output_dir):
        raise SystemExit(f"Output dir not found: {output_dir}")

    md_entries = find_markdown_entries(output_dir)
    if not md_entries:
        print(f"No Markdown entries found under: {output_dir}")
        return 1

    missing: List[Tuple[str, str]] = []
    for md_path in md_entries:
        sidecar = expected_sidecar_path(ai_dir, md_path)
        if not os.path.exists(sidecar):
            missing.append((md_path, sidecar))

    if not missing:
        print(f"All {len(md_entries)} entries have AI sidecars in: {ai_dir}")
        return 0

    print(f"Missing AI sidecars: {len(missing)}/{len(md_entries)}")
    for md_path, sidecar in missing:
        print(f"- {os.path.basename(md_path)} -> {os.path.relpath(sidecar, os.getcwd())}")

    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        raise SystemExit(0)
