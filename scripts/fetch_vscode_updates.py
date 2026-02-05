#!/usr/bin/env python3
"""Fetch and normalize VS Code monthly release notes and save locally.

Source of truth:
- Upstream Markdown in microsoft/vscode-docs:
  https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_XX.md

Output layout (mirrors changelogs/ style):
- Markdown entries: vscode-updates/YYYY-MM-DD-vscode-update-v1_XX.md
- Index: vscode-updates/index.md

Notes:
- This script intentionally avoids adding new dependencies (no YAML parser).
- It does not require authentication, but will use GITHUB_TOKEN if present
  to reduce GitHub API rate-limit issues when listing files.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import os
import re
from typing import Dict, List, Optional, Tuple

import requests


GITHUB_OWNER = "microsoft"
GITHUB_REPO = "vscode-docs"
GITHUB_REF = "main"
RELEASE_NOTES_DIR = "release-notes"
DEFAULT_OUTPUT_DIR = "vscode-updates"

_CONTENTS_API_URL = (
    f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{RELEASE_NOTES_DIR}"
)
_RAW_BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_OWNER}/{GITHUB_REPO}/{GITHUB_REF}/{RELEASE_NOTES_DIR}"


_V1_NOTE_RE = re.compile(r"^v1_(\d+)\.md$")
_H1_RE = re.compile(r"^#\s+(.+?)\s*$")


def parse_date(value: Optional[str]) -> Optional[dt.date]:
    if not value:
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"Invalid date format: {value}. Use YYYY-MM-DD.") from exc


def parse_flexible_ymd(value: str) -> Optional[dt.date]:
    """Parse YYYY-M-D or YYYY-MM-DD."""
    m = re.match(r"^(\d{4})-(\d{1,2})-(\d{1,2})$", value.strip())
    if not m:
        return None
    year, month, day = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    try:
        return dt.date(year, month, day)
    except ValueError:
        return None


def safe_yaml_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def ensure_output_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def write_file_if_changed(path: str, content: str) -> None:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as handle:
            if handle.read() == content:
                return
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def read_existing_title(path: str) -> Optional[str]:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            for index, line in enumerate(handle):
                if line.startswith("title:"):
                    return line.split(":", 1)[1].strip().strip("\"' ")
                if line.strip() == "---" and index > 0:
                    break
    except FileNotFoundError:
        return None
    return None


def resolve_path(output_dir: str, base_name: str, title: str) -> str:
    candidate = os.path.join(output_dir, base_name)
    if not os.path.exists(candidate):
        return candidate

    existing_title = read_existing_title(candidate)
    if existing_title and existing_title == title:
        return candidate

    stem, ext = os.path.splitext(base_name)
    counter = 2
    while True:
        next_name = f"{stem}-{counter}{ext}"
        candidate = os.path.join(output_dir, next_name)
        if not os.path.exists(candidate):
            return candidate
        existing_title = read_existing_title(candidate)
        if existing_title and existing_title == title:
            return candidate
        counter += 1


def should_include(date_value: dt.date, start_date: Optional[dt.date], end_date: Optional[dt.date]) -> bool:
    if start_date and date_value < start_date:
        return False
    if end_date and date_value > end_date:
        return False
    return True


def github_headers() -> Dict[str, str]:
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def list_release_notes_files() -> List[str]:
    """Return filenames like v1_109.md."""
    resp = requests.get(_CONTENTS_API_URL, headers=github_headers(), timeout=30)
    if resp.status_code != 200:
        raise RuntimeError(
            f"Failed to list release notes via GitHub API ({resp.status_code}): {resp.text[:200]}"
        )

    data = resp.json()
    if not isinstance(data, list):
        raise RuntimeError("Unexpected GitHub API response for directory listing")

    names: List[str] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        if item.get("type") != "file":
            continue
        name = item.get("name")
        if isinstance(name, str) and _V1_NOTE_RE.match(name):
            names.append(name)
    return sorted(names)


def fetch_raw_markdown(file_name: str) -> str:
    url = f"{_RAW_BASE_URL}/{file_name}"
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    return resp.text


def find_title(markdown_text: str) -> str:
    for line in markdown_text.splitlines():
        m = _H1_RE.match(line)
        if m:
            return html.unescape(m.group(1).strip()) or "Untitled"
    return "Untitled"


def extract_docfx_metadata(markdown_text: str) -> Dict[str, str]:
    """Extract a DocFX-style metadata block bounded by --- fences.

    Upstream release notes often include a metadata block with keys like:
    - Date
    - DownloadVersion

    The block may appear anywhere in the document.
    """
    lines = markdown_text.splitlines()
    fence_indexes: List[int] = [i for i, ln in enumerate(lines) if ln.strip() == "---"]
    for start, end in zip(fence_indexes, fence_indexes[1:]):
        # Only consider reasonably small blocks
        if end <= start + 1:
            continue
        block = lines[start + 1 : end]
        meta: Dict[str, str] = {}
        for ln in block:
            if ":" not in ln:
                continue
            key, val = ln.split(":", 1)
            key = key.strip()
            val = val.strip()
            if key and val:
                meta[key] = val
        if "Date" in meta:
            return meta
    return {}


def remove_toc_comments(markdown_text: str) -> str:
    # Drop large autogenerated TOC comment blocks.
    return re.sub(r"<!--\s*TOC[\s\S]*?-->", "", markdown_text, flags=re.IGNORECASE)


def normalize_download_placeholder(markdown_text: str, source_url: str) -> str:
    if "DOWNLOAD_LINKS_PLACEHOLDER" not in markdown_text:
        return markdown_text
    note = f"_(Download links are available on the official release page: {source_url})_"
    markdown_text = markdown_text.replace("<!-- DOWNLOAD_LINKS_PLACEHOLDER -->", note)
    markdown_text = markdown_text.replace("DOWNLOAD_LINKS_PLACEHOLDER", note)
    return markdown_text


def rewrite_assets_to_code_site(markdown_text: str, version_dir: str) -> str:
    """Rewrite images/{version_dir}/... to code.visualstudio.com assets URLs."""
    base = f"https://code.visualstudio.com/assets/updates/{version_dir}/"

    # Markdown link/image targets: (...)
    markdown_text = re.sub(
        rf"\((images/{re.escape(version_dir)}/[^)]+)\)",
        lambda m: f"({base}{m.group(1).split('/', 2)[-1]})",
        markdown_text,
    )

    # HTML attributes: src="images/..." poster='images/...'
    markdown_text = re.sub(
        rf"([\"'])(images/{re.escape(version_dir)}/[^\"']+)([\"'])",
        lambda m: f"{m.group(1)}{base}{m.group(2).split('/', 2)[-1]}{m.group(3)}",
        markdown_text,
    )

    return markdown_text


def extract_overview(markdown_text: str) -> str:
    """Extract the first paragraph after the H1, if available."""
    lines = markdown_text.splitlines()
    # Find H1 line index
    h1_index = None
    for i, ln in enumerate(lines):
        if _H1_RE.match(ln):
            h1_index = i
            break
    if h1_index is None:
        return "Not stated in the article."

    paragraph: List[str] = []
    for ln in lines[h1_index + 1 :]:
        if ln.strip() == "":
            if paragraph:
                break
            continue
        if ln.startswith("#"):
            if paragraph:
                break
            continue
        if ln.strip().startswith("<!--"):
            continue
        paragraph.append(ln.strip())

    text = " ".join(paragraph).strip()
    return text or "Not stated in the article."


def build_front_matter(
    *,
    title: str,
    date_str: str,
    version_ref: str,
    download_version: str,
    source_url: str,
    source_markdown_url: str,
) -> str:
    fetched_at = dt.datetime.now(dt.UTC).isoformat().replace("+00:00", "Z")
    return "\n".join(
        [
            "---",
            f"title: {safe_yaml_string(title)}",
            f"date: {safe_yaml_string(date_str)}",
            f"version_ref: {safe_yaml_string(version_ref)}",
            f"download_version: {safe_yaml_string(download_version)}",
            f"source_url: {safe_yaml_string(source_url)}",
            f"source_markdown_url: {safe_yaml_string(source_markdown_url)}",
            f"fetched_at: {safe_yaml_string(fetched_at)}",
            "---",
        ]
    )


def build_markdown(*, title: str, overview: str, normalized_source: str) -> str:
    lines: List[str] = []
    lines.append(f"# {title}")
    lines.append("")

    lines.append("## Overview")
    lines.append(overview)
    lines.append("")

    lines.append("## Source Content (normalized)")
    lines.append(normalized_source.strip())
    lines.append("")

    return "\n".join(lines).strip() + "\n"


def generate_index(output_dir: str) -> None:
    index_path = os.path.join(output_dir, "index.md")
    lines = ["# VS Code Updates Archive", "", "## Entries", ""]

    md_names = [
        name
        for name in os.listdir(output_dir)
        if name.endswith(".md") and name != "index.md" and os.path.isfile(os.path.join(output_dir, name))
    ]

    disk_entries: List[Tuple[str, str, str]] = []
    for name in md_names:
        date_str = name[:10]
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
            continue
        path = os.path.join(output_dir, name)
        title = read_existing_title(path) or name
        disk_entries.append((date_str, name, title))

    disk_entries.sort(key=lambda item: (item[0], item[1]), reverse=True)

    for date_str, filename, title in disk_entries:
        lines.append(f"- {date_str} — [{title}]({filename})")

    content = "\n".join(lines).strip() + "\n"
    write_file_if_changed(index_path, content)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch and normalize VS Code monthly release notes (v1_XX) and save locally."
    )
    parser.add_argument("--start-date", help="YYYY-MM-DD")
    parser.add_argument("--end-date", help="YYYY-MM-DD")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--no-index", action="store_true")

    args = parser.parse_args()
    start_date = parse_date(args.start_date)
    end_date = parse_date(args.end_date)

    ensure_output_dir(args.output_dir)

    files = list_release_notes_files()

    created_or_updated = 0
    processed = 0

    for name in files:
        m = _V1_NOTE_RE.match(name)
        if not m:
            continue
        version_ref = name[:-3]  # v1_109
        version_dir = version_ref[1:]  # 1_109

        source_url = f"https://code.visualstudio.com/updates/{version_ref}"
        source_markdown_url = f"{_RAW_BASE_URL}/{name}"

        raw_md = fetch_raw_markdown(name)
        meta = extract_docfx_metadata(raw_md)
        date_raw = meta.get("Date", "").strip()
        date_value = parse_flexible_ymd(date_raw) if date_raw else None
        if not date_value:
            # Skip if we can't date it (range filtering depends on date)
            continue
        if not should_include(date_value, start_date, end_date):
            continue

        title = find_title(raw_md)
        download_version = meta.get("DownloadVersion", "Not stated in the article.")

        normalized = raw_md
        normalized = remove_toc_comments(normalized)
        normalized = normalize_download_placeholder(normalized, source_url=source_url)
        normalized = rewrite_assets_to_code_site(normalized, version_dir=version_dir)

        overview = extract_overview(normalized)

        date_str = date_value.isoformat()
        base_name = f"{date_str}-vscode-update-{version_ref}.md"
        path = resolve_path(args.output_dir, base_name, title)

        front_matter = build_front_matter(
            title=title,
            date_str=date_str,
            version_ref=version_ref,
            download_version=download_version,
            source_url=source_url,
            source_markdown_url=source_markdown_url,
        )
        body = build_markdown(title=title, overview=overview, normalized_source=normalized)
        content = front_matter + "\n\n" + body

        # Count only if actual content differs
        before = None
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                before = f.read()

        write_file_if_changed(path, content)
        after = content

        processed += 1
        if before != after:
            created_or_updated += 1

    if not args.no_index:
        generate_index(args.output_dir)

    print(f"Processed in range: {processed}")
    print(f"Markdown entries created/updated: {created_or_updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
