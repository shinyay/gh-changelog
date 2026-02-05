# Ready-to-Run Instructions for Processing VS Code JP Files

## Current Situation

- **10 Japanese files** need processing
- **172 EN_CONTENT blocks** need to be replaced with Japanese
- **Script is ready**: `scripts/process_vscode_jp_files.py`
- **Missing**: Valid API credentials

## Quick Start (When You Have Credentials)

```bash
# 1. Set environment variables with YOUR credentials
export GITHUB_TOKEN="paste_your_actual_github_token_here"
export AI_BASE_URL="https://models.inference.ai.azure.com/v1"
export AI_MODEL="gpt-4o"

# 2. Run the processing script
python3 scripts/process_vscode_jp_files.py

# 3. Validate results
python3 scripts/validate_vscode_updates_jp_translations.py --forbid-en-content-markers

# 4. Check what changed
git diff --stat vscode-updates-jp/

# 5. Commit if satisfied
git add vscode-updates-jp/*.md
git commit -m "Replace EN_CONTENT markers with detailed Japanese explanations"
```

## What The Script Will Do

When you run `python3 scripts/process_vscode_jp_files.py`:

1. Processes each of these 10 files:
   - 2025-05-08-vscode-update-v1_100-jp.md
   - 2025-06-12-vscode-update-v1_101-jp.md
   - 2025-07-09-vscode-update-v1_102-jp.md
   - 2025-08-07-vscode-update-v1_103-jp.md
   - 2025-09-11-vscode-update-v1_104-jp.md
   - 2025-10-09-vscode-update-v1_105-jp.md
   - 2025-11-12-vscode-update-v1_106-jp.md
   - 2025-12-10-vscode-update-v1_107-jp.md
   - 2026-01-08-vscode-update-v1_108-jp.md
   - 2026-02-04-vscode-update-v1_109-jp.md

2. For each file:
   - Finds all `<!-- EN_CONTENT_BEGIN -->` ... `<!-- EN_CONTENT_END -->` blocks
   - Extracts context (surrounding Japanese text)
   - Calls LLM API to generate detailed Japanese explanation
   - Replaces the entire block (including markers) with Japanese text
   - Saves the updated file

3. Output example:
```
Found 10 Japanese files to process

Processing: 2025-05-08-vscode-update-v1_100-jp.md
  Found 16 EN_CONTENT blocks
  Processing block 1/16...
    ✓ Block 1 translated
  Processing block 2/16...
    ✓ Block 2 translated
  ...
  ✓ File updated successfully

Processing: 2025-06-12-vscode-update-v1_101-jp.md
  Found 17 EN_CONTENT blocks
  ...

============================================================
Processing complete:
  Success: 10
  Failed: 0
============================================================
```

## Getting a GitHub Token

If you need to create a GitHub token:

1. Go to https://github.com/settings/tokens
2. Click "Generate new token" (classic)
3. Give it a name like "VS Code JP Processing"
4. Select scopes (for GitHub Models API):
   - No specific scopes needed if using GitHub Models
5. Click "Generate token"
6. Copy the token immediately (you won't see it again)

## Alternative: Using AI_API_KEY

If you're using a different OpenAI-compatible API:

```bash
export AI_API_KEY="your_api_key"
export AI_BASE_URL="https://your-api-endpoint.com/v1"
export AI_MODEL="gpt-4o"

python3 scripts/process_vscode_jp_files.py
```

## Estimated Cost & Time

- **API Calls**: 172 calls (one per EN_CONTENT block)
- **Time**: ~10-15 minutes (depending on API response time)
- **Cost**: Depends on your API pricing
  - For GitHub Models: Free tier may apply
  - For OpenAI: ~$0.01-0.05 per block (estimate)

## Files Modified

The script will modify these files in-place:
```
vscode-updates-jp/2025-05-08-vscode-update-v1_100-jp.md
vscode-updates-jp/2025-06-12-vscode-update-v1_101-jp.md
vscode-updates-jp/2025-07-09-vscode-update-v1_102-jp.md
vscode-updates-jp/2025-08-07-vscode-update-v1_103-jp.md
vscode-updates-jp/2025-09-11-vscode-update-v1_104-jp.md
vscode-updates-jp/2025-10-09-vscode-update-v1_105-jp.md
vscode-updates-jp/2025-11-12-vscode-update-v1_106-jp.md
vscode-updates-jp/2025-12-10-vscode-update-v1_107-jp.md
vscode-updates-jp/2026-01-08-vscode-update-v1_108-jp.md
vscode-updates-jp/2026-02-04-vscode-update-v1_109-jp.md
```

## Verification After Processing

```bash
# 1. Check that no EN_CONTENT markers remain
grep -l "EN_CONTENT_BEGIN" vscode-updates-jp/*.md
# Should return: no output (or just index.md)

# 2. Run official validation
python3 scripts/validate_vscode_updates_jp_translations.py --forbid-en-content-markers
# Should show: All files passed

# 3. Spot-check a file
head -100 vscode-updates-jp/2025-05-08-vscode-update-v1_100-jp.md
# Should show Japanese content without EN_CONTENT markers
```

## If Something Goes Wrong

The script processes blocks in reverse order, so if it fails partway through:
- Already-processed content is saved
- Re-running the script will continue from where it left off
- No duplicate processing occurs

To see current status:
```bash
python3 scripts/process_single_file.py 2025-05-08-vscode-update-v1_100-jp.md
```

## Ready to Go!

Once you have valid credentials, simply run:

```bash
export GITHUB_TOKEN="your_token_here"
export AI_BASE_URL="https://models.inference.ai.azure.com/v1"
export AI_MODEL="gpt-4o"

python3 scripts/process_vscode_jp_files.py
```

That's it! The script handles everything else automatically.
