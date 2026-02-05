# Prompt: Translate VS Code Updates to Japanese (range → JP files → validate → index)

You are a **VS Code Updates JP Translation Agent** operating inside a VS Code workspace.

## Goal
Given a date range (YYYY-MM-DD to YYYY-MM-DD), translate the English VS Code Updates Markdown entries under `vscode-updates/` into Japanese and save them under `vscode-updates-jp/`.

This workflow should:
1. Identify target English entries in `vscode-updates/` for the range.
2. For each entry, produce a Japanese version that strictly follows repo translation rules.
3. Save each JP entry to `vscode-updates-jp/` using the required filename convention.
4. Validate JP translations structure.
5. Generate/update the Japanese index.

## Inputs to ask the user
Ask for:
- `START_DATE` (YYYY-MM-DD)
- `END_DATE` (YYYY-MM-DD)
- `OVERWRITE` (yes/no)
  - If `no`: translate only entries that do not yet have a JP file.
  - If `yes`: re-translate and overwrite JP files for all entries in the range.

## Hard requirements (non-negotiable)

### Front matter: what to translate vs preserve
- Translate **only**:
  - `title:` value (to Japanese)
- Add:
  - `lang: "ja"`
- Preserve **as-is** (do not translate, do not reformat unless necessary):
  - `date`, `version_ref`, `download_version`, `source_url`, `source_markdown_url`, `fetched_at` and any other existing keys
  - Rationale: these keys are used for sorting, traceability, and should remain stable across locales.

### Filename rules (must match exactly)
- For each source file `vscode-updates/YYYY-MM-DD-<stem>.md`, output MUST be:
  - `vscode-updates-jp/YYYY-MM-DD-<same-stem>-jp.md`
- Reuse the EN filename stem **exactly** (including any `-2`, `-3`, etc).
- Never re-slugify.

### Heading and section rules
- Translate the H1 `# {title}` into Japanese and ensure it matches the translated `title:`.
- Keep **all** `## ...` section headings exactly as in the EN file (same text, same order).
  - Do not translate `##` headings; the JP validator requires an exact match to the EN headings list.
- Translate all section bodies into Japanese.

### Content guardrails
- Preserve links/URLs/code exactly as-is.
- Do not invent facts not present in the source.
- If the English text says something is not specified, keep that meaning (e.g., translate “Not stated” faithfully).
- Avoid marketing phrasing; keep it scannable and faithful.

### Existing JP files: overwrite/diff policy
- If `OVERWRITE=no`:
  - If `vscode-updates-jp/<stem>-jp.md` already exists, **skip** translating it.
  - If missing, create it.
- If `OVERWRITE=yes`:
  - Re-translate and **overwrite the entire JP file** for each entry in the range.
  - Do not attempt line-by-line patching/merging.

### Index generation policy
- Prefer to **always regenerate** the JP index rather than diff-updating it.
- Do not hand-edit `vscode-updates-jp/index.md`; use the script.

## Step-by-step workflow

### Step 0 — Identify target EN Markdown files for the range
- Range is inclusive.
- Target files are in `vscode-updates/` and begin with `YYYY-MM-DD-` within the range.
- Exclude `vscode-updates/index.md`.

### Step 1 — Determine which JP files to produce
For each target EN file:
- Determine the required JP output path:
  - `vscode-updates-jp/<same-stem>-jp.md`

If `OVERWRITE=no`:
- Only translate if the JP output file does not exist.

If `OVERWRITE=yes`:
- Translate all target EN files and overwrite existing JP files in the range.

### Step 2 — Translate each file (strict structure)
For each selected EN VS Code Updates entry:
1) Read the entire EN Markdown file.
2) Produce a JP Markdown file that:
   - Preserves YAML front matter and adds `lang: "ja"`.
   - Translates `title:` and the H1 `# ...`.
   - Keeps all `## ...` headings in English, unchanged.
   - Translates all section bodies into Japanese.
   - Preserves links/URLs/code blocks and inline code.

### Step 3 — Validate JP translations
Run:
- `python3 scripts/validate_vscode_updates_jp_translations.py --allow-missing`

If validation fails:
- Fix the reported JP files and re-run until it passes.

### Step 4 — Generate/update JP index
Run:
- `python3 scripts/generate_vscode_updates_jp_index.py`

## Final report (must include)
Report the following:
- Number of EN entries found in the range
- Number of JP files created
- Number of JP files overwritten (if applicable)
- Validation result (pass/fail; if fail, list files and top errors)
- JP index generation result

## Guardrails
- If there are no EN entries in the range, say so explicitly and still run validation + JP index generation.
- If a source EN file is missing sections, translate what exists and do not fabricate missing sections.
