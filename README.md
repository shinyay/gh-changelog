# gh-changelog

Fetch GitHub Changelog entries for a date range and generate a local Markdown archive under `./changelogs/`.

This repo is designed to be driven from **VS Code GitHub Copilot Chat** with high reproducibility:

- Fetch entries via the Python fetcher script.
- Generate an AI deep dive as **strict JSON** (sidecar files) validated against a JSON schema.
- Keep the Markdown output consistent and scannable.

## What gets generated

- `changelogs/YYYY-MM-DD-<slug>.md`
- `changelogs/index.md`
- `changelogs/_ai/YYYY-MM-DD-<slug>.ai.json`

## Japanese translations (manual, Copilot Chat)

This repo can also store Japanese translations of each changelog entry under `./changelogs-jp/`.

- JP entries: `changelogs-jp/YYYY-MM-DD-<slug>-jp.md`
- JP index: `changelogs-jp/index.md`

Notes:

- Filenames must reuse the EN stem exactly (including any `-2`, `-3`, etc). Do not re-slugify.
- Section headings (`## Overview`, etc.) stay in English for structural consistency.
- The YAML front matter `title:` and the top-level `# ...` heading should be translated to Japanese.

Optional VS Code tasks:

- "Changelog JP: list missing translations"
- "Changelog JP: validate translations"
- "Changelog JP: generate index"

## How to use from Copilot Chat

- Repo-level instructions live in `.github/copilot-instructions.md`.
- Use the prompt `.github/prompts/fetch_changelog_range.prompt.md` and provide a date range (YYYY-MM-DD to YYYY-MM-DD).

After fetching, generate AI sidecar JSON for each entry using `.github/prompts/changelog_deep_dive_json.prompt.md` and save it under `changelogs/_ai/`.

You can check which entries still need AI sidecars by running the task "Changelog: list missing AI sidecars".

## Tasks (optional)

This repo includes VS Code tasks in `.vscode/tasks.json`:

- "Changelog: fetch range (use API)"
- "Changelog: validate AI outputs"
- "Changelog: list missing AI sidecars"
- "Changelog: generate AI sidecars from Markdown (no LLM)"

### Optional helper: generate AI sidecars from Markdown (no LLM)

If you already have Markdown entries under `./changelogs/`, you can optionally run `scripts/generate_ai_sidecars_from_markdown.py` (or the VS Code task "Changelog: generate AI sidecars from Markdown (no LLM)") to create/update AI sidecar files under `changelogs/_ai/`.

This helper:

- Extracts structured sections from the Markdown (for example: Overview, Key Changes, Caveats).
- Writes **schema-conformant** sidecar JSON (it does **not** call an LLM).

You should still run validation afterwards ("Changelog: validate AI outputs").

## Installation

Create/activate your venv, then install dependencies from `requirements.txt`.

On Linux, use `python3` (the `python` shim may not be installed by default).

## License

Released under the [MIT license](https://gist.githubusercontent.com/shinyay/56e54ee4c0e22db8211e05e70a63247e/raw/f3ac65a05ed8c8ea70b653875ccac0c6dbc10ba1/LICENSE)

## Author

- github: <https://github.com/shinyay>
- twitter: <https://twitter.com/yanashin18618>
- mastodon: <https://mastodon.social/@yanashin>
