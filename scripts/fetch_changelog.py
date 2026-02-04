#!/usr/bin/env python3
"""Fetch and analyze GitHub Changelog entries from the RSS feed."""

from __future__ import annotations

import argparse
import datetime as dt
import glob
import html
import os
import re
import sys
from email.utils import parsedate_to_datetime
from typing import Dict, Iterable, List, Optional, Tuple

import feedparser
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

DEFAULT_FEED_URL = "https://github.blog/changelog/feed/"
DEFAULT_ARCHIVE_URL_TEMPLATE = "https://github.blog/changelog/{year}/"
DEFAULT_API_URL = "https://github.blog/wp-json/wp/v2/changelogs"
DEFAULT_OUTPUT_DIR = "changelogs"


def parse_date(value: Optional[str]) -> Optional[dt.date]:
    if not value:
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"Invalid date format: {value}. Use YYYY-MM-DD.") from exc


def slugify(text: str, max_length: int = 80) -> str:
    cleaned = html.unescape(text).lower()
    cleaned = cleaned.replace("&", "and")
    cleaned = re.sub(r"[\'\"`]+", "", cleaned)
    cleaned = re.sub(r"[^a-z0-9]+", "-", cleaned).strip("-")
    cleaned = re.sub(r"-+", "-", cleaned)
    return cleaned[:max_length].strip("-") or "entry"


def safe_yaml_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f"\"{escaped}\""


def ensure_output_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def fetch_feed(url: str):
    return feedparser.parse(url)


def fetch_archive_links(url: str) -> List[str]:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    links: List[str] = []
    for anchor in soup.find_all("a", href=True):
        href = anchor["href"]
        if "/changelog/" not in href:
            continue
        if not re.search(r"/changelog/\d{4}-\d{2}-\d{2}-", href):
            continue
        links.append(requests.compat.urljoin(url, href))
    return sorted(set(links))


def fetch_api_entries(start_date: Optional[dt.date], end_date: Optional[dt.date]) -> List[dict]:
    params = {"per_page": 100, "page": 1}
    if start_date:
        params["after"] = dt.datetime.combine(start_date, dt.time.min).isoformat() + "Z"
    if end_date:
        params["before"] = dt.datetime.combine(end_date, dt.time.max).isoformat() + "Z"

    entries: List[dict] = []
    while True:
        response = requests.get(DEFAULT_API_URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        entries.extend(data)
        total_pages = int(response.headers.get("X-WP-TotalPages", "1"))
        if params["page"] >= total_pages:
            break
        params["page"] += 1
    return entries


def fetch_article_html(url: str) -> str:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.text


def extract_article_body(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article")
    return str(article or soup)


def clean_html(html: str) -> BeautifulSoup:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    for paragraph in soup.find_all("p"):
        text = paragraph.get_text(" ", strip=True).lower()
        if "appeared first on" in text:
            paragraph.decompose()
    return soup


def html_to_markdown(soup: BeautifulSoup) -> str:
    return md(str(soup), heading_style="ATX")


def split_sentences(text: str) -> List[str]:
    normalized = re.sub(r"\s+", " ", text).strip()
    if not normalized:
        return []
    return re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", normalized)


def extract_sections(soup: BeautifulSoup) -> List[Dict[str, List[Dict[str, str]]]]:
    sections: List[Dict[str, List[Dict[str, str]]]] = []
    current = {"title": "Overview", "items": []}

    for element in soup.find_all(["h1", "h2", "h3", "p", "ul", "ol"]):
        if element.name in {"h1", "h2", "h3"}:
            if current["items"]:
                sections.append(current)
            current = {"title": element.get_text(" ", strip=True), "items": []}
        elif element.name == "p":
            text = element.get_text(" ", strip=True)
            if text:
                current["items"].append({"text": text, "kind": "paragraph"})
        elif element.name in {"ul", "ol"}:
            for li in element.find_all("li", recursive=False):
                text = li.get_text(" ", strip=True)
                if text:
                    current["items"].append({"text": text, "kind": "list"})

    if current["items"]:
        sections.append(current)

    return sections


def extract_overview(soup: BeautifulSoup) -> str:
    paragraph = soup.find("p")
    if not paragraph:
        return ""
    text = paragraph.get_text(" ", strip=True)
    return text


def extract_key_changes(sections: List[Dict[str, List[Dict[str, str]]]]) -> List[str]:
    key_changes: List[str] = []
    matcher = re.compile(
        r"(what'?s new|what'?s included|changes|improvements|features|release notes)",
        re.IGNORECASE,
    )
    for section in sections:
        if matcher.search(section["title"]):
            for item in section["items"]:
                if item["kind"] == "list" or item["text"] not in key_changes:
                    key_changes.append(item["text"])
    return key_changes


def extract_sentences_by_keywords(sentences: List[str], keywords: Iterable[str]) -> List[str]:
    results: List[str] = []
    for sentence in sentences:
        lowered = sentence.lower()
        if any(keyword in lowered for keyword in keywords):
            if sentence not in results:
                results.append(sentence)
    return results


def extract_insights(sentences: List[str]) -> List[str]:
    insight_keywords = [
        "we recommend",
        "you should",
        "consider",
        "to start",
        "to begin",
        "learn more",
        "for more details",
        "note that",
        "requires",
    ]
    return extract_sentences_by_keywords(sentences, insight_keywords)


def parse_entry_metadata(entry) -> Tuple[str, str, dt.date, str, List[str], str]:
    title = html.unescape(entry.get("title", "Untitled"))
    link = entry.get("link", "")
    author = entry.get("author") or entry.get("dc_creator") or ""
    published = entry.get("published") or entry.get("updated") or ""
    published_dt = parsedate_to_datetime(published)
    published_date = published_dt.date()

    changelog_type = "Update"
    labels: List[str] = []
    for tag in entry.get("tags", []):
        term = tag.get("term")
        domain = (tag.get("domain") or tag.get("scheme") or "").lower()
        if "changelog-type" in domain and term:
            changelog_type = term
        elif "changelog-label" in domain and term:
            labels.append(term)

    return title, link, published_date, author, labels, changelog_type


def extract_html_content(entry, fallback_url: str) -> str:
    if entry.get("content"):
        return entry["content"][0].get("value", "")
    if entry.get("summary"):
        return entry.get("summary")
    if entry.get("description"):
        return entry.get("description")

    raw_html = fetch_article_html(fallback_url)
    return extract_article_body(raw_html)


def parse_date_from_url(url: str) -> Optional[dt.date]:
    match = re.search(r"/changelog/(\d{4})-(\d{2})-(\d{2})-", url)
    if not match:
        return None
    year, month, day = map(int, match.groups())
    return dt.date(year, month, day)


def parse_published_date_from_html(soup: BeautifulSoup, fallback_url: str) -> Optional[dt.date]:
    meta = soup.find("meta", property="article:published_time")
    if meta and meta.get("content"):
        try:
            return dt.datetime.fromisoformat(meta["content"].replace("Z", "+00:00")).date()
        except ValueError:
            pass
    time_tag = soup.find("time")
    if time_tag and time_tag.get("datetime"):
        try:
            return dt.datetime.fromisoformat(time_tag["datetime"].replace("Z", "+00:00")).date()
        except ValueError:
            pass
    return parse_date_from_url(fallback_url)


def parse_article_metadata_from_html(html: str, url: str) -> Tuple[str, dt.date, str, List[str], str]:
    soup = BeautifulSoup(html, "html.parser")
    title = ""
    h1 = soup.find("h1")
    if h1:
        title = h1.get_text(" ", strip=True)
    if not title:
        meta_title = soup.find("meta", property="og:title")
        if meta_title and meta_title.get("content"):
            title = meta_title["content"]
    if not title:
        title = "Untitled"
    title = html.unescape(title)

    published_date = parse_published_date_from_html(soup, url)
    if not published_date:
        raise ValueError(f"Unable to determine publish date for {url}")

    author = ""
    meta_author = soup.find("meta", attrs={"name": "author"})
    if meta_author and meta_author.get("content"):
        author = meta_author["content"]

    changelog_type = "Update"
    labels: List[str] = []
    section_meta = soup.find("meta", property="article:section")
    if section_meta and section_meta.get("content"):
        changelog_type = section_meta["content"]
    for tag in soup.find_all("meta", property="article:tag"):
        if tag.get("content"):
            labels.append(tag["content"])

    return title, published_date, author, labels, changelog_type


def parse_taxonomies_from_class_list(class_list: List[str]) -> Tuple[str, List[str]]:
    changelog_type = "Update"
    labels: List[str] = []
    for entry in class_list:
        if entry.startswith("changelog-type-"):
            changelog_type = entry.replace("changelog-type-", "").replace("-", " ")
        if entry.startswith("changelog-label-"):
            labels.append(entry.replace("changelog-label-", "").replace("-", " "))
    return changelog_type, labels


def parse_author_from_yoast(yoast_head_json: Optional[dict]) -> str:
    if not yoast_head_json:
        return ""
    misc = yoast_head_json.get("twitter_misc") or {}
    return misc.get("Written by", "")


def build_front_matter(
    title: str,
    date_str: str,
    changelog_type: str,
    labels: List[str],
    author: str,
    source_url: str,
) -> str:
    labels_yaml = "[" + ", ".join(safe_yaml_string(label) for label in labels) + "]"
    fetched_at = dt.datetime.now(dt.UTC).isoformat().replace("+00:00", "Z")
    return "\n".join(
        [
            "---",
            f"title: {safe_yaml_string(title)}",
            f"date: {safe_yaml_string(date_str)}",
            f"type: {safe_yaml_string(changelog_type)}",
            f"labels: {labels_yaml}",
            f"author: {safe_yaml_string(author)}",
            f"source_url: {safe_yaml_string(source_url)}",
            f"fetched_at: {safe_yaml_string(fetched_at)}",
            "---",
        ]
    )


def build_markdown(
    title: str,
    overview: str,
    sections: List[Dict[str, List[Dict[str, str]]]],
    key_changes: List[str],
    impacts: List[str],
    caveats: List[str],
    insights: List[str],
    cleaned_markdown: str,
) -> str:
    lines: List[str] = []
    lines.append(f"# {title}")
    lines.append("")

    if overview:
        lines.append("## Overview")
        lines.append(overview)
        lines.append("")

    lines.append("## Detailed Explanation")
    for section in sections:
        lines.append(f"### {section['title']}")
        for item in section["items"]:
            lines.append(f"- {item['text']}")
        lines.append("")

    if key_changes:
        lines.append("## Key Changes")
        for change in key_changes:
            lines.append(f"- {change}")
        lines.append("")

    if impacts:
        lines.append("## Impact / Who’s Affected")
        for impact in impacts:
            lines.append(f"- {impact}")
        lines.append("")

    if caveats:
        lines.append("## Caveats / Limitations")
        for caveat in caveats:
            lines.append(f"- {caveat}")
        lines.append("")

    if insights:
        lines.append("## Insights (derived from article language)")
        for insight in insights:
            lines.append(f"- {insight}")
        lines.append("")

    if cleaned_markdown.strip():
        lines.append("## Article Content (cleaned)")
        lines.append(cleaned_markdown.strip())
        lines.append("")

    return "\n".join(lines).strip() + "\n"


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


def read_existing_title(path: str) -> Optional[str]:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            for index, line in enumerate(handle):
                if line.startswith("title:"):
                    return line.split(":", 1)[1].strip().strip("\"\'")
                if line.strip() == "---" and index > 0:
                    break
    except FileNotFoundError:
        return None
    return None


def write_file_if_changed(path: str, content: str) -> None:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as handle:
            if handle.read() == content:
                return
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def generate_index(output_dir: str, entries: List[Dict[str, str]]) -> None:
    index_path = os.path.join(output_dir, "index.md")
    lines = ["# GitHub Changelog Archive", "", "## Entries", ""]
    # Build the index from all existing Markdown entries on disk.
    # When fetching a narrow date range, `entries` only contains that subset;
    # we still want `changelogs/index.md` to represent the full local archive.
    md_paths = glob.glob(os.path.join(output_dir, "*.md"))
    disk_entries: List[Dict[str, str]] = []
    for path in md_paths:
        filename = os.path.basename(path)
        if filename == "index.md":
            continue

        # Most files are named as YYYY-MM-DD-<slug>.md
        date_str = filename[:10]
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
            continue

        title = read_existing_title(path) or filename[len(date_str) + 1 : -3]
        disk_entries.append({"date": date_str, "title": title, "filename": filename})

    # Sort newest-first; keep ordering stable when dates are equal.
    disk_entries.sort(key=lambda item: (item["date"], item["filename"]), reverse=True)

    for entry in disk_entries:
        lines.append(f"- {entry['date']} — [{entry['title']}]({entry['filename']})")
    content = "\n".join(lines).strip() + "\n"
    write_file_if_changed(index_path, content)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch and analyze GitHub Changelog entries from RSS feed."
    )
    parser.add_argument("--feed-url", default=DEFAULT_FEED_URL)
    parser.add_argument("--archive-year", action="append", type=int, default=[])
    parser.add_argument("--use-api", action="store_true")
    parser.add_argument("--start-date", help="YYYY-MM-DD")
    parser.add_argument("--end-date", help="YYYY-MM-DD")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--no-index", action="store_true")

    args = parser.parse_args()
    start_date = parse_date(args.start_date)
    end_date = parse_date(args.end_date)

    ensure_output_dir(args.output_dir)

    index_entries: List[Dict[str, str]] = []
    processed_links: set[str] = set()

    def should_include(date_value: dt.date) -> bool:
        if start_date and date_value < start_date:
            return False
        if end_date and date_value > end_date:
            return False
        return True

    def process_entry(
        title: str,
        link: str,
        published_date: dt.date,
        author: str,
        labels: List[str],
        changelog_type: str,
        html: str,
    ) -> None:
        if link in processed_links:
            return
        if not should_include(published_date):
            return

        processed_links.add(link)
        soup = clean_html(html)

        overview = extract_overview(soup)
        sections = extract_sections(soup)
        full_text = soup.get_text(" ", strip=True)
        sentences = split_sentences(full_text)
        key_changes = extract_key_changes(sections)
        impacts = extract_sentences_by_keywords(
            sentences,
            [
                "now available",
                "now supported",
                "public preview",
                "generally available",
                "deprecated",
                "sunset",
                "retired",
                "not supported",
                "limited",
                "requires",
                "only",
            ],
        )
        caveats = extract_sentences_by_keywords(
            sentences,
            [
                "note",
                "important",
                "requires",
                "not supported",
                "only",
                "limited",
                "except",
            ],
        )
        insights = extract_insights(sentences)
        cleaned_markdown = html_to_markdown(soup)

        date_str = published_date.isoformat()
        slug = slugify(title)
        filename = f"{date_str}-{slug}.md"
        path = resolve_path(args.output_dir, filename, title)

        front_matter = build_front_matter(
            title=title,
            date_str=date_str,
            changelog_type=changelog_type,
            labels=labels,
            author=author,
            source_url=link,
        )

        body = build_markdown(
            title=title,
            overview=overview,
            sections=sections,
            key_changes=key_changes,
            impacts=impacts,
            caveats=caveats,
            insights=insights,
            cleaned_markdown=cleaned_markdown,
        )

        content = front_matter + "\n\n" + body
        write_file_if_changed(path, content)

        index_entries.append(
            {"date": date_str, "title": title, "filename": os.path.basename(path)}
        )

    feed = fetch_feed(args.feed_url)
    for entry in feed.entries:
        title, link, published_date, author, labels, changelog_type = parse_entry_metadata(entry)
        entry_html = extract_html_content(entry, link)
        process_entry(title, link, published_date, author, labels, changelog_type, entry_html)

    if args.use_api:
        for entry in fetch_api_entries(start_date, end_date):
            title = html.unescape(entry.get("title", {}).get("rendered", "Untitled"))
            link = entry.get("link", "")
            date_value = entry.get("date_gmt") or entry.get("date")
            published_date = dt.datetime.fromisoformat(date_value.replace("Z", "+00:00")).date()
            author = parse_author_from_yoast(entry.get("yoast_head_json"))
            changelog_type, labels = parse_taxonomies_from_class_list(entry.get("class_list", []))
            content_html = entry.get("content", {}).get("rendered", "")
            process_entry(title, link, published_date, author, labels, changelog_type, content_html)

    for year in args.archive_year:
        archive_url = DEFAULT_ARCHIVE_URL_TEMPLATE.format(year=year)
        for link in fetch_archive_links(archive_url):
            date_from_url = parse_date_from_url(link)
            if date_from_url and not should_include(date_from_url):
                continue
            article_html = fetch_article_html(link)
            title, published_date, author, labels, changelog_type = parse_article_metadata_from_html(
                article_html, link
            )
            article_body = extract_article_body(article_html)
            process_entry(title, link, published_date, author, labels, changelog_type, article_body)

    index_entries.sort(key=lambda item: item["date"], reverse=True)

    if not args.no_index:
        generate_index(args.output_dir, index_entries)

    return 0


if __name__ == "__main__":
    sys.exit(main())
