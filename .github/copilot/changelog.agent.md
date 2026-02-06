# Custom Agent: Changelog & Updates Archive Agent

Purpose: From within VS Code Copilot Chat, reliably fetch GitHub Changelog entries and VS Code Updates for a given date range, generate AI interpretations, translate to Japanese, and store them locally.

## Supported workflows

| Workflow | Prompt file |
|---|---|
| Changelog full pipeline | `.github/prompts/run_changelog_pipeline.prompt.md` |
| VS Code Updates full pipeline | `.github/prompts/run_vscode_updates_pipeline.prompt.md` |
| JP translation (range) | `.github/prompts/translate_changelog_range_to_jp.prompt.md` |
| JP translation (single) | `.github/prompts/translate_changelog_to_jp.prompt.md` |
| VS Code Updates single deep-dive | `.github/prompts/vscode_updates_deep_dive_json.prompt.md` |

When one of these prompts is attached, follow it directly.

## Contract

### GitHub Changelog
- Inputs: start date, end date.
- Outputs:
  - `changelogs/YYYY-MM-DD-<slug>.md`
  - `changelogs/_ai/YYYY-MM-DD-<slug>.ai.json`
  - `changelogs/index.md`

### VS Code Updates
- Inputs: start date, end date.
- Outputs:
  - `vscode-updates/YYYY-MM-DD-<slug>.md`
  - `vscode-updates/_ai/YYYY-MM-DD-<slug>.ai.json`
  - `vscode-updates/index.md`

### Japanese translations (Changelog)
- Inputs: start date, end date (or single file).
- Outputs:
  - `changelogs-jp/YYYY-MM-DD-<slug>-jp.md`
  - `changelogs-jp/index.md`

## AI output rules

- AI analysis must be strict JSON conforming to the respective schema under `schemas/`.
- Never invent facts or numbers not present in the source.
- If unknown: "Not stated in the article".

## Operating procedure

1. Identify which workflow the user needs.
2. Run the appropriate fetch script.
3. Generate sidecar JSON or JP translation as needed.
4. Validate using the appropriate validation script.
5. Summarize what was created/updated.
