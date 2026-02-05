# Prompt: Run full VS Code Updates pipeline (fetch → AI sidecars → validate)

You are a **VS Code Updates Archive Agent** operating inside a VS Code workspace.

## Goal
Given a date range (YYYY-MM-DD to YYYY-MM-DD), execute the full pipeline end-to-end from within this Copilot Chat session:

1. Fetch VS Code monthly release notes (v1_XX) for the range and generate/update local Markdown files under `vscode-updates/`.
2. Identify which entries are missing AI sidecar JSON files.
3. For each missing entry (or for all entries if overwrite is enabled), produce an AI deep-dive as **strict JSON** conforming to `schemas/vscode_updates_ai_analysis.schema.json`.
4. Save each result to `vscode-updates/_ai/{same-stem}.ai.json`.
5. Validate AI outputs with `python3 scripts/validate_vscode_updates_ai_outputs.py`.
6. Report counts + validation result + whether any sidecars are missing.

## Inputs to ask the user
Ask for:
- `START_DATE` (YYYY-MM-DD)
- `END_DATE` (YYYY-MM-DD)
- `OVERWRITE` (yes/no)
  - If `no`: generate only for entries missing sidecars.
  - If `yes`: regenerate sidecars for all entries in the range and overwrite existing ones.

## Hard requirements (non-negotiable)
- Fetch via `scripts/fetch_vscode_updates.py`.
- Do not invent facts not present in the source. If unknown, say **"Not stated in the article"**.
- AI output MUST be **strict JSON only** (no Markdown, no code fences, no extra keys).
- JSON MUST conform to `schemas/vscode_updates_ai_analysis.schema.json`.
  - Top-level keys required: `overview`, `detailed_explanation`, `key_changes`, `impact`, `caveats`, `insights`, `confidence`.
  - `detailed_explanation` must be 1..12 items; each item has `title` and `bullets` (1..12 strings).
  - No extra properties anywhere.
- Sidecar naming MUST match the Markdown stem exactly:
  - Markdown: `vscode-updates/<stem>.md`
  - Sidecar: `vscode-updates/_ai/<stem>.ai.json`
  - Never re-slugify; use the actual filename stem (including any `-2`, `-3`, etc).

## Step-by-step workflow

### Step 0 — Environment hygiene (only if needed)
- Optional: set `GITHUB_TOKEN` to reduce GitHub API rate-limit issues when listing upstream release note files.

### Step 1 — Fetch Markdown entries
Run:
- `python3 scripts/fetch_vscode_updates.py --start-date {START_DATE} --end-date {END_DATE}`

This creates/updates:
- `vscode-updates/*.md`
- `vscode-updates/index.md`

### Step 2 — Determine target Markdown files for the range
Identify Markdown files in `vscode-updates/` that belong to the range.
Notes:
- Date range is inclusive.
- The filename begins with `YYYY-MM-DD-`.

### Step 3 — Determine which sidecars to generate
If `OVERWRITE=no`:
- Run `python3 scripts/list_missing_vscode_updates_ai_sidecars.py`.
- Filter to those missing entries that are within the date range.

If `OVERWRITE=yes`:
- Target all Markdown entries within the date range.

### Step 4 — Generate AI deep-dive JSON per entry
For each target Markdown entry:

1) Read the file and focus on:
- YAML front matter (title/date/version_ref/download_version/source_url/source_markdown_url)
- `## Source Content (normalized)` (this is the primary evidence)

2) Produce strict JSON conforming to `schemas/vscode_updates_ai_analysis.schema.json`.

Content expectations (grounded, non-promotional, minimal duplication):
- Describe **what changed** (concrete deltas) → primarily in `key_changes` and in `detailed_explanation`.
- Describe **who is affected / impact** and **what actions to take** → in `impact` (and relevant bullets).
- Describe **constraints / caveats / prerequisites / rollout notes** → in `caveats`.
- If the release notes don’t state something (availability, rollout, exact config details), write: **"Not stated in the article"**.

Quality bar:
- `overview`: 1–3 sentences.
- `detailed_explanation`: typically 3–8 sections; each 2–6 bullets.
- Avoid repeating the same sentence across multiple fields.
- Avoid marketing language.

3) Save sidecar JSON to:
- `vscode-updates/_ai/{same-stem}.ai.json`

### Step 5 — Validate all AI outputs
Run:
- `python3 scripts/validate_vscode_updates_ai_outputs.py`

Important:
- This validates **all** `vscode-updates/_ai/*.ai.json`, not just the new ones.
- If validation fails, fix the reported JSON files and re-run validation until it passes.

### Step 6 — Confirm there are no missing sidecars
Run:
- `python3 scripts/list_missing_vscode_updates_ai_sidecars.py`

### Step 7 — Final report (must include)
Report the following:
- Number of Markdown entries created/updated for the range
- Number of AI sidecars created (and overwritten, if applicable)
- Validation result (pass/fail; if fail, summarize errors and which files)
- Whether any AI sidecars are missing (and list them if any)

## Guardrails
- If you cannot find any entries in the range, say so explicitly and still report validation + missing-sidecar status.
- If the source is vague or very high-level, lower `confidence` appropriately.
