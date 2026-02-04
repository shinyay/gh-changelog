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
- Keep the Markdown section headings in ENGLISH exactly as-is:
  - `## Overview`
  - `## Detailed Explanation`
  - `## Key Changes`
  - `## Impact / Who’s Affected`
  - `## Caveats / Limitations`
  - `## Insights (derived from article language)`
  - `## Article Content (cleaned)`
- Translate:
  - YAML front matter `title:` value (Japanese)
  - The top-level heading `# ...` (Japanese)
  - All body text, including `## Article Content (cleaned)` content
- Do NOT add an “original link” or backlink to the EN file.
- Add `lang: "ja"` in YAML front matter.
- Preserve the rest of the YAML front matter keys and values (date/type/labels/author/source_url/fetched_at) unless translation requires only `title`.
- Keep links, URLs, code blocks, inline code, and product names accurate; do not invent facts.
- If the source is ambiguous or does not state something, say so plainly in Japanese (do not guess).

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

## Completion
When done, write the translated Markdown to the required output path.
