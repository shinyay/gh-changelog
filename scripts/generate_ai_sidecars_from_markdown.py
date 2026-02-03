#!/usr/bin/env python3
"""Generate strict-JSON AI sidecars from generated Markdown entries.

This is intended for the "Copilot Chat運用" workflow:
- Markdown entries are already generated under ./changelogs by scripts/fetch_changelog.py
- Copilot/LLM can be used to create sidecars, but this helper can also generate
  schema-conformant sidecars by extracting the structured sections from Markdown.

It never invents facts beyond what exists in the Markdown sections.

Output: changelogs/_ai/<same-stem>.ai.json
Schema: schemas/changelog_ai_analysis.schema.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from typing import Dict, List, Optional


_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
_BULLET_RE = re.compile(r"^\s*-\s+(.+?)\s*$")


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


def _extract_section_block(lines: List[str], heading: str) -> List[str]:
    """Return lines after '## {heading}' until next '## ' heading."""
    start = None
    for i, line in enumerate(lines):
        if line.strip() == f"## {heading}":
            start = i + 1
            break
    if start is None:
        return []

    out: List[str] = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        out.append(line.rstrip("\n"))
    return out


def _extract_overview(lines: List[str]) -> str:
    block = _extract_section_block(lines, "Overview")
    text = "\n".join([ln.strip() for ln in block]).strip()
    return text or "Not stated in the article."


def _extract_simple_bullets(lines: List[str], heading: str) -> List[str]:
    block = _extract_section_block(lines, heading)
    bullets: List[str] = []
    for ln in block:
        m = _BULLET_RE.match(ln)
        if m:
            bullets.append(m.group(1).strip())
    return bullets


def _extract_detailed_explanation(lines: List[str]) -> List[Dict[str, object]]:
    block = _extract_section_block(lines, "Detailed Explanation")
    if not block:
        return [{"title": "Detailed Explanation", "bullets": ["Not stated in the article."]}]

    sections: List[Dict[str, object]] = []
    current_title: Optional[str] = None
    current_bullets: List[str] = []

    def flush() -> None:
        nonlocal current_title, current_bullets
        if current_title and current_bullets:
            sections.append({"title": current_title, "bullets": current_bullets[:12]})
        current_title = None
        current_bullets = []

    for ln in block:
        # Subsection headings are rendered as ### ...
        if ln.startswith("### "):
            flush()
            current_title = ln.replace("### ", "", 1).strip()
            continue

        m = _BULLET_RE.match(ln)
        if m:
            current_bullets.append(m.group(1).strip())

    flush()

    if not sections:
        return [{"title": "Detailed Explanation", "bullets": ["Not stated in the article."]}]

    # Enforce schema maxItems
    return sections[:12]


def parse_markdown_entry(md_path: str) -> ParsedMarkdown:
    text = _read_text(md_path)
    lines = text.splitlines()

    overview = _extract_overview(lines)
    detailed = _extract_detailed_explanation(lines)
    key_changes = _extract_simple_bullets(lines, "Key Changes")
    impact = _extract_simple_bullets(lines, "Impact / Who’s Affected")
    caveats = _extract_simple_bullets(lines, "Caveats / Limitations")
    insights = _extract_simple_bullets(lines, "Insights (derived from article language)")

    return ParsedMarkdown(
        overview=overview,
        detailed=detailed,
        key_changes=key_changes,
        impact=impact,
        caveats=caveats,
        insights=insights,
    )


def compute_confidence(parsed: ParsedMarkdown) -> float:
    # A conservative, deterministic confidence score based on available structured content.
    score = 0.4
    if parsed.overview and parsed.overview != "Not stated in the article.":
        score += 0.2
    if parsed.detailed and parsed.detailed[0]["bullets"] != ["Not stated in the article."]:
        score += 0.2
    if parsed.key_changes:
        score += 0.1
    if parsed.impact:
        score += 0.05
    if parsed.caveats:
        score += 0.05
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
    parser = argparse.ArgumentParser(description="Generate AI sidecars from Markdown entries")
    parser.add_argument("--output-dir", default="changelogs", help="Directory containing Markdown entries")
    parser.add_argument("--ai-dir", default=os.path.join("changelogs", "_ai"), help="Directory for AI sidecars")
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
