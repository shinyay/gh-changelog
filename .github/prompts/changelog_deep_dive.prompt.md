# Prompt: GitHub Changelog deep dive (JSON)

You are analyzing a single GitHub Changelog entry.

## Inputs you will receive

- Metadata: title, publish date, type/labels (if known), author (if known), source URL.
- Article content: cleaned Markdown converted from the HTML.

## Your task

Create a deep-dive interpretation of the entry that is helpful to engineers.

## Rules

- Output MUST be a single JSON object and MUST conform to this schema conceptually:
  - `overview` (string)
  - `detailed_explanation` (array of sections: each has `title` and `bullets`)
  - `key_changes` (array of strings)
  - `impact` (array of strings)
  - `caveats` (array of strings)
  - `insights` (array of strings)
  - `confidence` (number 0..1)
- Do NOT output Markdown.
- Do NOT include code fences.
- Do NOT include extra keys beyond the schema.
- If the source does not mention something, do not guess. Use neutral language.
- Prefer concise bullet points; avoid repeating the same sentence.

## Guidance

- `overview`: 1–3 sentences explaining what changed.
- `detailed_explanation`: 3–8 sections maximum; each section 2–6 bullets.
- `key_changes`: the concrete changes (features, fixes, deprecations).
- `impact`: who should care and what action (if any) they should take.
- `caveats`: limitations, prerequisites, rollout notes, exclusions.
- `insights`: practical tips inferred from the article wording.

Return ONLY the JSON.
