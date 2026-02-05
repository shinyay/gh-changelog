#!/usr/bin/env python3
"""Enrich existing VS Code Updates JP files with the full EN content.

This repo originally generated JP files that were structurally valid but sometimes
highly abbreviated. To make JP entries "as rich as" the EN originals without
LLM truncation, this script merges:

- JP: front matter + H1 (Japanese title) + existing JP section summaries
- EN: full section bodies (verbatim) appended under each `## ...` section

The output is a bilingual JP Markdown file:
- All headings except the H1 remain in English (anchor/link stability)
- JP summary/translation appears first
- EN original section content is included verbatim between markers

Markers:
- <!-- EN_CONTENT_BEGIN -->
- <!-- EN_CONTENT_END -->

Idempotent: re-running will not duplicate EN content; existing marked EN blocks
are removed before re-inserting.
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
_FENCE_RE = re.compile(r"^(`{3,})(.*)$")

_EN_BEGIN = "<!-- EN_CONTENT_BEGIN -->"
_EN_END = "<!-- EN_CONTENT_END -->"


@dataclass
class SectionsDoc:
    front_matter_block: str
    front_matter: Dict[str, str]
    h1: str
    sections: List[Tuple[str, str]]  # (h2 heading text, body)


def _read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _write_text(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def _parse_front_matter(lines: List[str]) -> Tuple[str, Dict[str, str], int]:
    """Return (front_matter_block_raw, dict, end_index_exclusive)."""
    if not lines or lines[0].strip() != _FRONT_MATTER_FENCE:
        raise ValueError("Missing starting front matter fence '---'")

    fm: Dict[str, str] = {}
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == _FRONT_MATTER_FENCE:
            end = i + 1
            break

        raw = lines[i].rstrip("\n")
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        fm[key.strip()] = value.strip()

    if end is None:
        raise ValueError("Missing closing front matter fence '---'")

    block = "".join(lines[:end])
    return block, fm, end


def _strip_marked_en_content(section_body: str) -> str:
    """Remove any existing marked EN block from a section body."""
    if _EN_BEGIN not in section_body:
        return section_body
    before = section_body.split(_EN_BEGIN, 1)[0]
    return before.rstrip() + "\n"


def _extract_h1_and_h2_sections(lines: List[str], start: int) -> Tuple[str, List[Tuple[str, str]]]:
    """Extract first H1 and all H2 sections from lines[start:].

    Headings are detected only outside fenced code blocks.
    """
    h1: Optional[str] = None

    # Gather H2 indices outside fences
    in_fence = False
    fence_ticks: Optional[str] = None

    h2_indices: List[Tuple[int, str]] = []  # (line_index, heading_text)

    for idx in range(start, len(lines)):
        ln = lines[idx].rstrip("\n")

        fence_m = _FENCE_RE.match(ln)
        if fence_m:
            ticks = fence_m.group(1)
            if not in_fence:
                in_fence = True
                fence_ticks = ticks
            else:
                if fence_ticks is not None and ticks.startswith(fence_ticks):
                    in_fence = False
                    fence_ticks = None
            continue

        if in_fence:
            continue

        if h1 is None:
            m1 = _H1_RE.match(ln)
            if m1:
                h1 = m1.group(1).strip()
                continue

        m2 = _H2_RE.match(ln)
        if m2:
            h2_indices.append((idx, m2.group(1).strip()))

    if h1 is None:
        raise ValueError("Missing H1 ('# ...') heading")

    sections: List[Tuple[str, str]] = []
    for i, (h2_idx, h2_text) in enumerate(h2_indices):
        body_start = h2_idx + 1
        body_end = h2_indices[i + 1][0] if i + 1 < len(h2_indices) else len(lines)
        body = "".join(lines[body_start:body_end]).strip("\n")
        sections.append((h2_text, body.strip()))

    return h1, sections


def parse_sections_doc(path: str) -> SectionsDoc:
    text = _read_text(path)
    lines = text.splitlines(True)  # keep newlines

    fm_block, fm, body_start = _parse_front_matter(lines)
    h1, sections = _extract_h1_and_h2_sections(lines, body_start)
    return SectionsDoc(front_matter_block=fm_block, front_matter=fm, h1=h1, sections=sections)


def expected_jp_path(jp_dir: str, en_md_path: str) -> str:
    stem = os.path.splitext(os.path.basename(en_md_path))[0]
    return os.path.join(jp_dir, f"{stem}-jp.md")


def find_markdown_entries(dir_path: str) -> List[str]:
    entries: List[str] = []
    for name in os.listdir(dir_path):
        if not name.endswith(".md"):
            continue
        if name == "index.md":
            continue
        entries.append(os.path.join(dir_path, name))
    return sorted(entries)


def build_enriched_jp(en_doc: SectionsDoc, jp_doc: SectionsDoc) -> str:
    jp_sections_map = {h2: body for (h2, body) in jp_doc.sections}

    out: List[str] = []

    # Preserve JP front matter exactly.
    out.append(jp_doc.front_matter_block.rstrip("\n"))
    out.append("\n\n")

    # Use JP H1.
    out.append(f"# {jp_doc.h1}\n\n")

    for (h2, en_body) in en_doc.sections:
        out.append(f"## {h2}\n")

        jp_body = jp_sections_map.get(h2, "")
        jp_body = _strip_marked_en_content(jp_body).strip()
        if jp_body:
            out.append(jp_body)
            out.append("\n\n")

        out.append(f"{_EN_BEGIN}\n\n")
        out.append(en_body.strip())
        out.append("\n\n")
        out.append(f"{_EN_END}\n\n")

    return "".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enrich VS Code Updates JP entries by embedding full EN content per section"
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
        "--dry-run",
        action="store_true",
        help="Compute changes but do not write files",
    )
    args = parser.parse_args()

    en_dir = os.path.abspath(args.en_dir)
    jp_dir = os.path.abspath(args.jp_dir)

    if not os.path.isdir(en_dir):
        raise SystemExit(f"EN dir not found: {en_dir}")
    if not os.path.isdir(jp_dir):
        raise SystemExit(f"JP dir not found: {jp_dir}")

    en_entries = find_markdown_entries(en_dir)
    changed = 0
    skipped_missing = 0

    for en_md in en_entries:
        jp_md = expected_jp_path(jp_dir, en_md)
        if not os.path.exists(jp_md):
            skipped_missing += 1
            continue

        en_doc = parse_sections_doc(en_md)
        jp_doc = parse_sections_doc(jp_md)

        enriched = build_enriched_jp(en_doc, jp_doc)
        current = _read_text(jp_md)
        if current != enriched:
            changed += 1
            if not args.dry_run:
                _write_text(jp_md, enriched)

    print(
        f"Enrichment complete. Changed: {changed}, skipped missing JP: {skipped_missing}, total EN: {len(en_entries)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
