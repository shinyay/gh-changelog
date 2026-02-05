# Prompt: Deep dive a single VS Code Updates entry (strict JSON)

You are given metadata and normalized source content for a single Visual Studio Code monthly release notes entry.

## Your output

Return **ONLY** a single JSON object that conforms to `schemas/vscode_updates_ai_analysis.schema.json`.

## Rules

- Strict JSON only. No Markdown. No code fences.
- No extra keys.
- Do not invent facts; do not guess.
- Keep it scannable: short bullets.
- If the source does not mention something, use: **"Not stated in the article"**.

## Evidence focus

Treat `## Source Content (normalized)` as the primary evidence.

## Hints for content

- `overview`: 1–3 sentences.
- `detailed_explanation`: 3–8 sections, each 2–6 bullets.
- `key_changes`: concrete deltas.
- `impact`: who is affected + what action.
- `caveats`: limitations/prereqs/rollout notes.
- `insights`: practical takeaways derived from wording.
- `confidence`: 0..1 (lower if vague).
