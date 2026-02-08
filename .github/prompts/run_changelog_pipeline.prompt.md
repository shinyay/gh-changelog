# Prompt: Run changelog AI deep-dive pipeline (read → AI sidecars → validate)

You are a **Changelog Archive Agent** operating inside a VS Code workspace.

## Goal
Given a date range (YYYY-MM-DD to YYYY-MM-DD), generate AI deep-dive sidecars for
pre-fetched changelog entries under `changelogs-original/`:

1. Identify Markdown entries in `changelogs-original/` for the date range.
2. Identify which entries are missing AI sidecar JSON files.
3. For each missing entry (or for all entries if overwrite is enabled), produce an AI deep-dive as **strict JSON** conforming to `schemas/changelog_ai_analysis.schema.json`.
4. Save each result to `changelogs/_ai/{same-stem}.ai.json`.
5. Validate AI outputs with `python3 scripts/validate_ai_outputs.py`.
6. Report counts + validation result + whether any sidecars are missing.

Note: Changelog Markdown files are **automatically fetched** by GitHub Actions into
`changelogs-original/` twice daily. You do NOT need to run `fetch_changelog.py`.
If no entries exist for the requested range, advise the user to wait for the next
automated fetch or trigger the workflow manually via GitHub Actions.

## Inputs to ask the user
Ask for:
- `START_DATE` (YYYY-MM-DD)
- `END_DATE` (YYYY-MM-DD)
- `OVERWRITE` (yes/no)
  - If `no`: generate only for entries missing sidecars.
  - If `yes`: regenerate sidecars for all entries in the range and overwrite existing ones.

## Hard requirements (non-negotiable)
- Do not invent facts not present in the source. If unknown, say **"Not stated in the article"**.
- AI output MUST be **strict JSON only** (no Markdown, no code fences, no extra keys).
- JSON MUST conform to `schemas/changelog_ai_analysis.schema.json`.
  - Top-level keys required: `overview`, `detailed_explanation`, `key_changes`, `impact`, `caveats`, `insights`, `confidence`.
  - `detailed_explanation` must be 1..12 items; each item has `title` and `bullets` (1..12 strings).
  - No extra properties anywhere.
- Sidecar naming MUST match the Markdown stem exactly:
  - Markdown: `changelogs-original/<stem>.md`
  - Sidecar: `changelogs/_ai/<stem>.ai.json`
  - Never re-slugify; use the actual filename stem (including `-2`, `-3`, etc).

## Step-by-step workflow

### Step 1 — Determine target Markdown files for the range
Identify Markdown files in `changelogs-original/` that belong to the range.
Notes:
- Date range is inclusive.
- The filename begins with `YYYY-MM-DD-`.
- Exclude `index.md`.

### Step 2 — Determine which sidecars to generate
If `OVERWRITE=no`:
- Run `python3 scripts/list_missing_ai_sidecars.py`.
- Filter to those missing entries that are within the date range.

If `OVERWRITE=yes`:
- Target all Markdown entries within the date range.

### Step 3 — Generate AI deep-dive JSON per entry
For each target Markdown entry:

1) Read the file from `changelogs-original/` and focus on:
- YAML front matter (title/date/type/labels/author/source_url)
- `## Article Content (cleaned)` (this is the primary evidence)

2) Produce strict JSON conforming to `schemas/changelog_ai_analysis.schema.json`.

Content expectations (grounded, non-promotional, minimal duplication):
- Describe **what changed** (concrete deltas) → primarily in `key_changes` and in `detailed_explanation`.
- Describe **who is affected / impact** and **what actions to take** → in `impact` (and relevant bullets).
- Describe **constraints / caveats / prerequisites / rollout notes** → in `caveats`.
- If the article doesn’t state something (availability, pricing, plans, rollout, exact config details), write: **"Not stated in the article"**.

Quality bar:
- `overview`: 1–3 sentences.
- `detailed_explanation`: typically 3–8 sections; each 2–6 bullets.
- Avoid repeating the same sentence across multiple fields.
- Avoid marketing language.

3) Save sidecar JSON to:
- `changelogs/_ai/{same-stem}.ai.json`

4) **Ensure Markdown exists in `changelogs/`** (non-negotiable):
- Check if `changelogs/{same-stem}.md` exists.
- If missing, copy it from `changelogs-original/{same-stem}.md`.
- Every entry MUST have all three files: `changelogs-original/`, `changelogs/`, and `changelogs/_ai/`.

### Step 4 — Validate all AI outputs
Run:
- `python3 scripts/validate_ai_outputs.py`

Important:
- This validates **all** `changelogs/_ai/*.ai.json`, not just the new ones.
- If validation fails, fix the reported JSON files and re-run validation until it passes.

### Step 5 — Confirm there are no missing sidecars
Run:
- `python3 scripts/list_missing_ai_sidecars.py`

### Step 6 — Final report (must include)
Report the following:
- Number of Markdown entries found in `changelogs-original/` for the range
- Number of AI sidecars created (and overwritten, if applicable)
- Validation result (pass/fail; if fail, summarize errors and which files)
- Whether any AI sidecars are missing (and list them if any)

## Guardrails
- If you cannot find any entries in the range, say so explicitly and still report validation + missing-sidecar status.
- If the article only provides a high-level statement, lower `confidence` appropriately.
