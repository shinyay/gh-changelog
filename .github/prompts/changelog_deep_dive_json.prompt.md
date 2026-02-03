# Prompt: Deep dive a single changelog entry (strict JSON)

You are given metadata and the cleaned article content of a single GitHub Changelog entry.

## Your output

Return **ONLY** a single JSON object that conforms to `schemas/changelog_ai_analysis.schema.json`.

## Rules

- Strict JSON only. No Markdown. No code fences.
- No extra keys.
- Do not invent facts; do not guess.
- Keep it scannable: short bullets.

## Hints for content

- `overview`: 1–3 sentences.
- `detailed_explanation`: 3–8 sections, each 2–6 bullets.
- `key_changes`: concrete deltas.
- `impact`: who is affected + what action.
- `caveats`: limitations/prereqs/rollout notes.
- `insights`: practical takeaways derived from wording.
- `confidence`: 0..1 (lower if the article is vague).
