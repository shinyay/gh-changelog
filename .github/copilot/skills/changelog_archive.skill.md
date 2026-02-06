# Skill: Content archiving (fetch → interpret → validate)

This skill describes how to reliably archive GitHub Changelog entries and VS Code Updates into this repository.

## Tools in this repo

### GitHub Changelog
| Tool | Path |
|---|---|
| Fetcher | `scripts/fetch_changelog.py` |
| AI sidecar generator (no LLM) | `scripts/generate_ai_sidecars_from_markdown.py` |
| Missing sidecar checker | `scripts/list_missing_ai_sidecars.py` |
| Validator | `scripts/validate_ai_outputs.py` |
| Schema | `schemas/changelog_ai_analysis.schema.json` |

### VS Code Updates
| Tool | Path |
|---|---|
| Fetcher | `scripts/fetch_vscode_updates.py` |
| AI sidecar generator (no LLM) | `scripts/generate_vscode_updates_ai_sidecars_from_markdown.py` |
| Missing sidecar checker | `scripts/list_missing_vscode_updates_ai_sidecars.py` |
| Validator | `scripts/validate_vscode_updates_ai_outputs.py` |
| Schema | `schemas/vscode_updates_ai_analysis.schema.json` |

### Japanese translations (Changelog)
| Tool | Path |
|---|---|
| Missing translation checker | `scripts/list_missing_jp_translations.py` |
| Validator | `scripts/validate_jp_translations.py` |
| Index generator | `scripts/generate_jp_index.py` |

## Best practices

- Prefer completeness: use `--use-api` for changelog fetching.
- Keep AI outputs strict JSON and validate after every generation.
- Do not copy large verbatim excerpts; keep cleaned article content as the reference.
- If you regenerate, keep filenames stable and avoid duplicates.
- For JP translations, keep section headings in English; translate body text only.

## Failure handling

- If JSON validation fails, regenerate the JSON with stricter instructions and re-validate.
- If the article is missing key info, state "Not stated in the article" instead of guessing.
- If JP validation fails, check heading names match the EN source exactly.
