# Processing Guide: Remove EN_CONTENT Markers from VS Code JP Files

## Current Status

All 10 Japanese VS Code update files contain EN_CONTENT markers that need to be replaced with detailed Japanese explanations.

### Files to Process

```
1. vscode-updates-jp/2025-05-08-vscode-update-v1_100-jp.md (16 blocks)
2. vscode-updates-jp/2025-06-12-vscode-update-v1_101-jp.md (17 blocks)
3. vscode-updates-jp/2025-07-09-vscode-update-v1_102-jp.md (15 blocks)
4. vscode-updates-jp/2025-08-07-vscode-update-v1_103-jp.md (16 blocks)
5. vscode-updates-jp/2025-09-11-vscode-update-v1_104-jp.md (17 blocks)
6. vscode-updates-jp/2025-10-09-vscode-update-v1_105-jp.md (18 blocks)
7. vscode-updates-jp/2025-11-12-vscode-update-v1_106-jp.md (21 blocks)
8. vscode-updates-jp/2025-12-10-vscode-update-v1_107-jp.md (20 blocks)
9. vscode-updates-jp/2026-01-08-vscode-update-v1_108-jp.md (16 blocks)
10. vscode-updates-jp/2026-02-04-vscode-update-v1_109-jp.md (16 blocks)
```

**Total: 172 EN_CONTENT blocks across 10 files**

## Prerequisites

### 1. Python Dependencies

The OpenAI library is already installed in this repository (`requirements.txt` doesn't list it but it's available).

### 2. Environment Variables

You need to set three environment variables:

```bash
# Required: Authentication token for the AI API
export GITHUB_TOKEN="your_github_token_here"
# OR
export AI_API_KEY="your_api_key_here"

# Required: OpenAI-compatible API endpoint
export AI_BASE_URL="https://models.inference.ai.azure.com/v1"

# Required: Model name
export AI_MODEL="gpt-4o"  # or gpt-4o-mini for faster/cheaper processing
```

## Processing Methods

### Method 1: Automated Script (Recommended)

The repository includes `scripts/process_vscode_jp_files.py` which automatically processes all files:

```bash
# Set environment variables
export GITHUB_TOKEN="your_token"
export AI_BASE_URL="https://models.inference.ai.azure.com/v1"
export AI_MODEL="gpt-4o"

# Run processing
python3 scripts/process_vscode_jp_files.py

# Validate results
python3 scripts/validate_vscode_updates_jp_translations.py --forbid-en-content-markers
```

### Method 2: Interactive Script with Confirmation

Use the provided shell script for an interactive experience:

```bash
export GITHUB_TOKEN="your_token"
export AI_BASE_URL="https://models.inference.ai.azure.com/v1"
export AI_MODEL="gpt-4o"

./scripts/RUN_PROCESSING.sh
```

This script will:
1. Show current status (count of EN_CONTENT blocks)
2. Ask for confirmation
3. Process all files
4. Validate results

### Method 3: Manual File-by-File Processing

For debugging or selective processing, you can modify `process_vscode_jp_files.py` to process specific files.

## What Happens During Processing

For each file:

1. **Detection**: Script finds all `<!-- EN_CONTENT_BEGIN -->` ... `<!-- EN_CONTENT_END -->` blocks
2. **Context Extraction**: Gets surrounding content for context
3. **LLM Translation**: Calls OpenAI-compatible API with:
   - System prompt: Instructs to provide detailed Japanese technical explanations
   - User prompt: English content + context
   - Temperature: 0.3 (for consistency)
4. **Replacement**: Replaces entire block (including markers) with Japanese text
5. **Save**: Writes updated content back to file

## Expected Transformation

### Before:
```markdown
## Overview
このリリースは、Copilot Chat の機能強化に注力しています。

<!-- EN_CONTENT_BEGIN -->

_Release date: May 8, 2025_

**Update**: Enable Next Edit Suggestions (NES) by default...

<!-- EN_CONTENT_END -->

## Source Content
```

### After:
```markdown
## Overview
このリリースは、Copilot Chat の機能強化に注力しています。

リリース日: 2025年5月8日

このリリースでは、Next Edit Suggestions (NES) 機能がデフォルトで有効になりました。これは...

## Source Content
```

## Processing Time Estimate

- **Per API call**: ~2-3 seconds
- **Total blocks**: 172
- **Estimated time**: 8-15 minutes (depending on API response times)

## Validation

After processing, run validation to ensure no EN_CONTENT markers remain:

```bash
python3 scripts/validate_vscode_updates_jp_translations.py --forbid-en-content-markers
```

Expected output:
```
✓ All files passed validation
✓ No EN_CONTENT markers found
```

## Troubleshooting

### Error: "GITHUB_TOKEN environment variable is required"

**Solution**: Export the token before running:
```bash
export GITHUB_TOKEN="your_token_here"
```

### Error: "AI_BASE_URL environment variable is required"

**Solution**: Set the API endpoint:
```bash
export AI_BASE_URL="https://models.inference.ai.azure.com/v1"
```

### Error: "Error calling LLM: ..."

**Possible causes**:
1. Invalid API token
2. API rate limiting
3. Network connectivity issues
4. Model name not available

**Solution**: 
- Verify your token has correct permissions
- Check API endpoint is accessible
- Try a different model name
- Wait a moment and retry

### Files partially processed

The script processes blocks in reverse order, so if it fails mid-file, you can safely re-run it. Already-processed blocks won't have markers and will be skipped.

## Verification Steps

After processing:

1. **Check marker count**: Should be 0
   ```bash
   grep -c "EN_CONTENT_BEGIN" vscode-updates-jp/*.md
   ```

2. **Spot-check content**: Open a few files and verify:
   - Markers are gone
   - Japanese content looks detailed and meaningful
   - Structure/formatting preserved
   - Links and code blocks intact

3. **Run validation**:
   ```bash
   python3 scripts/validate_vscode_updates_jp_translations.py --forbid-en-content-markers
   ```

## Next Steps After Processing

1. Review changes with `git diff`
2. Commit the changes:
   ```bash
   git add vscode-updates-jp/*.md
   git commit -m "Replace EN_CONTENT markers with detailed Japanese explanations"
   ```
3. Push to repository
