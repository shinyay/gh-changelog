# Copilot instructions (gh-changelog)

This repository archives two content sources as local Markdown with AI analysis sidecars:

1. **GitHub Changelog** — product announcements
2. **VS Code Updates** — monthly release notes

It also supports **Japanese translations** of GitHub Changelog entries.

## Prompt files

Use the dedicated prompt files under `.github/prompts/` for each workflow:

- **Changelog pipeline**: `run_changelog_pipeline.prompt.md`
- **VS Code Updates pipeline**: `run_vscode_updates_pipeline.prompt.md`
- **JP translation (range)**: `translate_changelog_range_to_jp.prompt.md`
- **JP translation (single)**: `translate_changelog_to_jp.prompt.md`
- **VS Code Updates single deep-dive**: `vscode_updates_deep_dive_json.prompt.md`

When one of these prompts is attached or the user request clearly maps to a workflow above, follow the prompt instructions directly.

---

## GitHub Changelog workflow

When the user asks for a changelog date range (YYYY-MM-DD to YYYY-MM-DD):

1. Read pre-fetched entries from `changelogs-original/` (auto-fetched by GitHub Actions).
2. For each entry, produce an AI deep-dive as strict JSON conforming to `schemas/changelog_ai_analysis.schema.json`.
3. Save the AI result as a sidecar file under `changelogs/_ai/`.
4. Validate outputs using `scripts/validate_ai_outputs.py`.

## VS Code Updates workflow

When the user asks for a VS Code Updates date range:

1. Fetch entries using `scripts/fetch_vscode_updates.py`.
2. For each entry, produce an AI deep-dive as strict JSON conforming to `schemas/vscode_updates_ai_analysis.schema.json`.
3. Save the AI result as a sidecar file under `vscode-updates/_ai/`.
4. Validate outputs using `scripts/validate_vscode_updates_ai_outputs.py`.

## Non-negotiable requirements

- LLM output MUST be strict JSON that conforms to the respective schema.
- Do not invent facts or numbers that are not supported by the source content.
- When information is not present in the source, say so explicitly (e.g., "Not stated in the article").
- Keep the output scannable: short paragraphs and bullet points.

## Output structure (Changelog Markdown)

Required sections:

- `# {title}`
- `## Overview`
- `## Detailed Explanation`
- `## Key Changes`
- `## Impact / Who's Affected`
- `## Caveats / Limitations`
- `## Insights (derived from article language)`
- `## Article Content (cleaned)`

## Style

- Prefer actionable phrasing.
- Avoid marketing language.
- Avoid verbatim long excerpts of the article.

## Japanese translation workflow

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
  - `## Impact / Who's Affected`
  - `## Caveats / Limitations`
  - `## Insights (derived from article language)`
  - `## Article Content (cleaned)`
- Translate all section bodies, including `## Article Content (cleaned)`.
- Preserve links/URLs/code and do not invent facts not present in the source.
