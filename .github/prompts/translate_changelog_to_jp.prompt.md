# Prompt: Translate one changelog entry to Japanese (save to changelogs-jp)

You are working in the `gh-changelog` repository.

## Task
Translate exactly one existing changelog Markdown entry from `changelogs/` into Japanese and save it under `changelogs-jp/`.

## Input
- Source file: `changelogs/YYYY-MM-DD-<slug>.md`

## Output
- Output file path MUST be: `changelogs-jp/YYYY-MM-DD-<slug>-jp.md`
  - IMPORTANT: reuse the source filename stem exactly (including any `-2`, `-3`, etc). Do NOT re-slugify.

## Hard requirements (do not violate)

### Heading and section rules
- Keep **all** `## ...` section headings exactly as in the EN file (same text, same order).
  - This includes any linked H2 headings that appear inside `## Article Content (cleaned)` (for example: `## [What's new](...)`).
  - Do not translate these `##` headings; the JP validator requires an exact match to the EN headings list.
- The following are common required headings in this repo (but the authoritative source is the EN file itself):
  - `## Overview`
  - `## Detailed Explanation`
  - `## Key Changes`
  - `## Impact / Who's Affected`
  - `## Caveats / Limitations`
  - `## Insights (derived from article language)`
  - `## Article Content (cleaned)`
- Translate the H1 `# {title}` into Japanese and ensure it matches the translated `title:`.
- Translate all section bodies into Japanese (including the cleaned article content).
- If a section exists in the source, it must exist in the JP output.
- If a section is absent in the source, do not add it.
- If a source EN file is missing expected headings/sections, translate what exists and do not fabricate missing sections.

### Front matter rules
- Translate **only**:
  - `title:` value (to Japanese)
- Add:
  - `lang: "ja"`
- Preserve **as-is** (do not translate, do not reformat):
  - `date`, `type`, `labels`, `author`, `source_url`, `fetched_at` and any other existing keys
- Keep `labels` unchanged (even if English), to avoid taxonomy drift and keep cross-language aggregation consistent.

### Content guardrails
- Preserve links/URLs/code blocks/inline code exactly as-is.
- Keep product names accurate; do not invent facts not present in the source.
- If the source is ambiguous or does not state something, say so plainly in Japanese (do not guess).
- Do NOT add an "original link" or backlink to the EN file.
- Avoid overly marketing phrasing; keep it scannable and faithful.

## Structure rules
- Keep the same overall structure as the source:
  - YAML front matter fenced by `---`
  - Blank line after front matter
  - `# {Japanese title}`
  - Same `##` section ordering as the source file
- If a section exists in the source, it must exist in the JP output.
- If a section is absent in the source, do not add it.

## Quality guidelines
- Prefer concise Japanese. Use bullet lists where the source uses bullet lists.
- Avoid marketing language.
- Avoid long verbatim quotes from the article; summarize when the source already summarizes.

## Post-translation (recommended)
After writing the JP file, run the following to verify structure:
- `python3 scripts/validate_jp_translations.py --allow-missing`

If translating multiple files, also regenerate the JP index:
- `python3 scripts/generate_jp_index.py`

## Completion
When done, write the translated Markdown to the required output path.
