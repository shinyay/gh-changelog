# Copilot instructions (gh-changelog)

This repository fetches GitHub Changelog posts and generates a local Markdown archive.

## Goals

- Generate one Markdown file per changelog entry in `./changelogs/`.
- Each Markdown file must include YAML front matter and the required heading sections.
- "Deep dive" content must be produced by an LLM as **structured JSON** that is validated against a schema.

## Chat-driven workflow (VS Code Copilot)

When the user asks for a date range (YYYY-MM-DD to YYYY-MM-DD), you should:

1. Fetch entries using `scripts/fetch_changelog.py` (prefer `--use-api` for completeness).
2. For each entry, produce an AI deep-dive that is strict JSON conforming to the schema.
3. Save the AI result as a sidecar file under `changelogs/_ai/`.
4. Validate outputs using `scripts/validate_ai_outputs.py`.

## Non-negotiable requirements

- LLM output MUST be strict JSON that conforms to `schemas/changelog_ai_analysis.schema.json`.
- Do not invent facts or numbers that are not supported by the source content.
- When information is not present in the source, say so explicitly (e.g., "Not stated in the article").
- Keep the output scannable: short paragraphs and bullet points.

## Output structure (Markdown)

Required sections:

- `# {title}`
- `## Overview`
- `## Detailed Explanation`
- `## Key Changes`
- `## Impact / Who’s Affected`
- `## Caveats / Limitations`
- `## Insights (derived from article language)`
- `## Article Content (cleaned)`

## Style

- Prefer actionable phrasing.
- Avoid marketing language.
- Avoid verbatim long excerpts of the article.

## Japanese translation workflow (optional)

When the user asks to translate changelog entries into Japanese:

- Source: `changelogs/YYYY-MM-DD-<slug>.md` (exclude `changelogs/index.md`).
- Output directory: `changelogs-jp/`
- Output filename MUST be: `changelogs-jp/YYYY-MM-DD-<same-stem>-jp.md`
	- Reuse the EN filename stem exactly (including any `-2`, `-3`, etc). Do not re-slugify.

### Non-negotiable requirements (JP)

- Preserve YAML front matter and add `lang: "ja"`.
- Translate `title:` value and the `# {title}` H1 to Japanese.
- Keep the section headings in English exactly as in the EN file:
	- `## Overview`
	- `## Detailed Explanation`
	- `## Key Changes`
	- `## Impact / Who’s Affected`
	- `## Caveats / Limitations`
	- `## Insights (derived from article language)`
	- `## Article Content (cleaned)`
- Translate all section bodies, including `## Article Content (cleaned)`.
- Preserve links/URLs/code and do not invent facts not present in the source.
