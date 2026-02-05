#!/usr/bin/env python3
"""Validate Japanese translation Markdown files under vscode-updates-jp/.

This validator is intentionally lightweight (no external YAML parser).

Rules enforced:
- JP file exists for each EN entry (unless --allow-missing)
- YAML front matter fences exist
- Front matter contains required keys: title, date, source_url, lang
- lang is "ja"
- JP front matter preserves all EN keys; non-title values match EN values
- H1 title matches the JP front matter title
- JP file has the same set/order of '##' section headings as its EN source

EN -> JP mapping:
- EN: vscode-updates/<stem>.md
- JP: vscode-updates-jp/<stem>-jp.md

Notes:
- Section headings are expected to remain in English.
"""

from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


_FRONT_MATTER_FENCE = "---"
_H1_RE = re.compile(r"^#\s+(.+?)\s*$")
_H2_RE = re.compile(r"^##\s+(.+?)\s*$")


@dataclass
class ParsedDoc:
    front_matter: Dict[str, str]
    h1: str
    h2_headings: List[str]


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


def _read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _parse_front_matter(lines: List[str]) -> Tuple[Dict[str, str], int]:
    """Return (front_matter_dict, end_index_exclusive).

    end_index_exclusive is the line index after the closing fence.
    """
    if not lines or lines[0].strip() != _FRONT_MATTER_FENCE:
        raise ValueError("Missing starting front matter fence '---'")

    fm: Dict[str, str] = {}
    for i in range(1, len(lines)):
        if lines[i].strip() == _FRONT_MATTER_FENCE:
            return fm, i + 1

        raw = lines[i].rstrip("\n")
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        fm[key.strip()] = value.strip()

    raise ValueError("Missing closing front matter fence '---'")


def _strip_yaml_quotes(value: str) -> str:
    v = value.strip()
    if len(v) >= 2 and ((v[0] == v[-1] == '"') or (v[0] == v[-1] == "'")):
        return v[1:-1]
    return v


def parse_doc(path: str) -> ParsedDoc:
    text = _read_text(path)
    lines = text.splitlines()

    fm, body_start = _parse_front_matter(lines)

    # Find first H1 after front matter.
    h1: Optional[str] = None
    h2s: List[str] = []
    for ln in lines[body_start:]:
        m1 = _H1_RE.match(ln)
        if m1 and h1 is None:
            h1 = m1.group(1).strip()
            continue
        m2 = _H2_RE.match(ln)
        if m2:
            h2s.append(m2.group(1).strip())

    if not h1:
        raise ValueError("Missing H1 ('# ...') heading")

    return ParsedDoc(front_matter=fm, h1=h1, h2_headings=h2s)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate JP VS Code Updates translation Markdown files"
    )
    parser.add_argument(
        "--en-dir",
        default="vscode-updates",
        help="Directory containing English Markdown entries",
    )
    parser.add_argument(
        "--jp-dir",
        default="vscode-updates-jp",
        help="Directory containing Japanese Markdown entries",
    )
    parser.add_argument(
        "--allow-missing",
        action="store_true",
        help="Do not fail if JP translations are missing",
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

    errors: List[str] = []
    missing_count = 0

    for en_md in en_entries:
        jp_md = expected_jp_path(jp_dir, en_md)
        en_name = os.path.basename(en_md)
        jp_name = os.path.basename(jp_md)

        if not os.path.exists(jp_md):
            missing_count += 1
            if not args.allow_missing:
                errors.append(
                    f"Missing JP file for {en_name}: {os.path.relpath(jp_md, os.getcwd())}"
                )
            continue

        try:
            en_doc = parse_doc(en_md)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Failed to parse EN {en_name}: {exc}")
            continue

        try:
            jp_doc = parse_doc(jp_md)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Failed to parse JP {jp_name}: {exc}")
            continue

        # Required front matter keys.
        for key in ("title", "date", "source_url", "lang"):
            if key not in jp_doc.front_matter:
                errors.append(f"{jp_name}: missing front matter key '{key}:'")

        lang_val = _strip_yaml_quotes(jp_doc.front_matter.get("lang", ""))
        if lang_val and lang_val.lower() != "ja":
            errors.append(f"{jp_name}: lang must be 'ja' (got {lang_val!r})")

        # JP front matter should preserve EN keys and values (except title).
        for key, en_val_raw in en_doc.front_matter.items():
            if key == "title":
                continue
            if key not in jp_doc.front_matter:
                errors.append(f"{jp_name}: missing front matter key '{key}:' (from EN)")
                continue
            en_val = _strip_yaml_quotes(en_val_raw)
            jp_val = _strip_yaml_quotes(jp_doc.front_matter.get(key, ""))
            if en_val and jp_val and en_val != jp_val:
                errors.append(
                    f"{jp_name}: front matter value mismatch for '{key}:' (EN={en_val!r}, JP={jp_val!r})"
                )

        # H1 must match JP front matter title (normalized).
        jp_title = _strip_yaml_quotes(jp_doc.front_matter.get("title", "")).strip()
        if jp_title and jp_doc.h1.strip() != jp_title:
            errors.append(
                f"{jp_name}: H1 title must match front matter title (fm={jp_title!r}, h1={jp_doc.h1!r})"
            )

        # Section headings must match EN exactly (order + presence).
        if en_doc.h2_headings != jp_doc.h2_headings:
            errors.append(
                f"{jp_name}: '##' section headings differ from EN ({en_name}).\n"
                f"  EN: {en_doc.h2_headings}\n"
                f"  JP: {jp_doc.h2_headings}"
            )

    if errors:
        print(f"VS Code Updates JP validation failed. Missing: {missing_count}/{len(en_entries)}")
        for msg in errors:
            print(f"- {msg}")
        return 2

    print(f"VS Code Updates JP validation OK. Missing: {missing_count}/{len(en_entries)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        raise SystemExit(0)
