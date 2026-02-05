#!/usr/bin/env python3
"""Generate strict-JSON AI sidecars for VS Code Updates from local Markdown entries.

This mirrors scripts/generate_ai_sidecars_from_markdown.py for changelogs, but targets:
- Markdown: ./vscode-updates/*.md
- Sidecars: ./vscode-updates/_ai/<same-stem>.ai.json
- Schema: schemas/vscode_updates_ai_analysis.schema.json

This helper does NOT call an LLM. It only extracts small, structured snippets that
already exist in the Markdown file.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


_BULLET_RE = re.compile(r"^\s*[-*]\s+(.+?)\s*$")
_H2_RE = re.compile(r"^##\s+(.+?)\s*$")


@dataclass
class ParsedMarkdown:
    overview: str
    detailed: List[Dict[str, object]]
    key_changes: List[str]
    impact: List[str]
    caveats: List[str]
    insights: List[str]


def _read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _find_section_indices(lines: List[str], heading: str) -> Optional[int]:
    target = f"## {heading}"
    for i, ln in enumerate(lines):
        if ln.strip() == target:
            return i
    return None


def _extract_overview(lines: List[str]) -> str:
    idx = _find_section_indices(lines, "Overview")
    if idx is None:
        return "Not stated in the article."

    out: List[str] = []
    for ln in lines[idx + 1 :]:
        if ln.startswith("## "):
            break
        if ln.strip() == "":
            if out:
                break
            continue
        out.append(ln.strip())

    text = " ".join(out).strip()
    return text or "Not stated in the article."


def _extract_source_content(lines: List[str]) -> List[str]:
    idx = _find_section_indices(lines, "Source Content (normalized)")
    if idx is None:
        return []
    # Source content is the remainder of the file; it can contain many '##' headings.
    return [ln.rstrip("\n") for ln in lines[idx + 1 :]]


def _split_h2_sections(source_lines: List[str]) -> List[Tuple[str, List[str]]]:
    sections: List[Tuple[str, List[str]]] = []
    current_title: Optional[str] = None
    current_lines: List[str] = []

    def flush() -> None:
        nonlocal current_title, current_lines
        if current_title is not None:
            sections.append((current_title, current_lines))
        current_title = None
        current_lines = []

    for ln in source_lines:
        m = _H2_RE.match(ln)
        if m:
            flush()
            current_title = m.group(1).strip()
            continue
        if current_title is not None:
            current_lines.append(ln)

    flush()
    return sections


def _extract_bullets_or_paragraph(lines: List[str], max_items: int) -> List[str]:
    bullets: List[str] = []
    for ln in lines:
        m = _BULLET_RE.match(ln)
        if m:
            bullets.append(m.group(1).strip())
        if len(bullets) >= max_items:
            return bullets

    # Fallback: grab the first non-empty paragraph-ish line.
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        if s.startswith("#"):
            continue
        if s.startswith("!["):
            continue
        if s.startswith("<!--"):
            continue
        return [s]

    return ["Not stated in the article."]


def parse_markdown_entry(md_path: str) -> ParsedMarkdown:
    text = _read_text(md_path)
    lines = text.splitlines()

    overview = _extract_overview(lines)
    source_lines = _extract_source_content(lines)

    detailed: List[Dict[str, object]] = []
    if source_lines:
        for title, body in _split_h2_sections(source_lines)[:8]:
            bullets = _extract_bullets_or_paragraph(body, max_items=6)
            detailed.append({"title": title, "bullets": bullets[:12]})

    if not detailed:
        detailed = [{"title": "Release notes", "bullets": ["Not stated in the article."]}]

    return ParsedMarkdown(
        overview=overview,
        detailed=detailed[:12],
        key_changes=[],
        impact=[],
        caveats=[],
        insights=[],
    )


def compute_confidence(parsed: ParsedMarkdown) -> float:
    score = 0.4
    if parsed.overview and parsed.overview != "Not stated in the article.":
        score += 0.2
    if parsed.detailed and parsed.detailed[0]["bullets"] != ["Not stated in the article."]:
        score += 0.2
    return max(0.0, min(1.0, score))


def write_if_changed(path: str, data: dict) -> bool:
    content = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=False) + "\n"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            if f.read() == content:
                return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate VS Code Updates AI sidecars from Markdown entries")
    parser.add_argument(
        "--output-dir", default="vscode-updates", help="Directory containing Markdown entries"
    )
    parser.add_argument(
        "--ai-dir",
        default=os.path.join("vscode-updates", "_ai"),
        help="Directory for AI sidecars",
    )
    args = parser.parse_args()

    output_dir = os.path.abspath(args.output_dir)
    ai_dir = os.path.abspath(args.ai_dir)
    os.makedirs(ai_dir, exist_ok=True)

    md_files = sorted(
        f
        for f in os.listdir(output_dir)
        if f.endswith(".md") and f != "index.md" and os.path.isfile(os.path.join(output_dir, f))
    )
    if not md_files:
        print(f"No Markdown entries found under: {output_dir}")
        return 1

    created_or_updated = 0
    for name in md_files:
        md_path = os.path.join(output_dir, name)
        stem = os.path.splitext(name)[0]
        sidecar_path = os.path.join(ai_dir, f"{stem}.ai.json")

        parsed = parse_markdown_entry(md_path)
        payload = {
            "overview": parsed.overview,
            "detailed_explanation": parsed.detailed,
            "key_changes": parsed.key_changes,
            "impact": parsed.impact,
            "caveats": parsed.caveats,
            "insights": parsed.insights,
            "confidence": compute_confidence(parsed),
        }

        if write_if_changed(sidecar_path, payload):
            created_or_updated += 1

    print(f"AI sidecars created/updated: {created_or_updated}/{len(md_files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
