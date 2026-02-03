# Skill: Changelog archiving (fetch → interpret → validate)

This skill describes how to reliably archive GitHub Changelog entries into this repository.

## Tools in this repo

- Fetcher: `scripts/fetch_changelog.py`
- Validator: `scripts/validate_ai_outputs.py`
- Schema: `schemas/changelog_ai_analysis.schema.json`

## Best practices

- Prefer completeness: use `--use-api`.
- Keep AI outputs strict JSON and validate.
- Do not copy large verbatim excerpts; keep cleaned article content as the reference.
- If you regenerate, keep filenames stable and avoid duplicates.

## Failure handling

- If JSON validation fails, regenerate the JSON with stricter instructions.
- If the article is missing key info, state "Not stated in the article" instead of guessing.
