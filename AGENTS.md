# Agents

This repo generates a local Markdown archive of GitHub Changelog entries.

## What is generated

- Markdown entries: `./changelogs/YYYY-MM-DD-<slug>.md`
- Index: `./changelogs/index.md`
- AI sidecar JSON (validated): `./changelogs/_ai/YYYY-MM-DD-<slug>.ai.json`

## Required environment variables (for AI)

This project calls an OpenAI-compatible chat completions endpoint (default intended for GitHub Models).

- `GITHUB_TOKEN`: token used as the Bearer token for the AI endpoint.
- `AI_BASE_URL`: base URL of an OpenAI-compatible API (example: `https://models.inference.ai.azure.com/v1`).
- `AI_MODEL`: model name (example: `gpt-4.1-mini`).

See `.env.example`.

## Typical run

- Fetch and generate for a date range (API source recommended for completeness):
  - `python3 scripts/fetch_changelog.py --use-api --start-date 2025-10-27 --end-date 2026-01-30`

## VS Code Copilot usage

- Use the prompt file `.github/prompts/fetch_changelog_range.prompt.md` to standardize the workflow in chat.
- Optional: run the VS Code task "Changelog: fetch range (use API)" to fetch content.
- Then (in Copilot Chat) generate AI sidecar JSON files under `changelogs/_ai/` and validate them.

## Coverage helper

- List entries missing AI sidecars:
  - `python3 scripts/list_missing_ai_sidecars.py`
  - or run the VS Code task "Changelog: list missing AI sidecars"

## Validation

- Validate all AI sidecar files:
  - `python3 scripts/validate_ai_outputs.py`

## Notes

- By default, AI analysis is required. Use `--no-ai` to disable AI analysis (heuristic-only output).
