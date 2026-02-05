# VS Code Update Japanese Translation Processing

## Overview

This directory contains scripts to process Japanese VS Code update files and replace embedded English content markers with detailed Japanese explanations using an LLM.

## Files

- `process_vscode_jp_en_markers.py` - Main processing script for all files
- `process_single_file.py` - Test/demonstration script for single file examination

## Requirements

### Python Dependencies

```bash
pip install requests
```

### Environment Variables

Create a `.env` file in the repository root with:

```bash
# Required: API authentication token
GITHUB_TOKEN=your_github_token_here
# OR
AI_API_KEY=your_api_key_here

# Required: OpenAI-compatible API endpoint
AI_BASE_URL=https://models.inference.ai.azure.com/v1

# Required: Model name
AI_MODEL=gpt-4o-mini
```

## Usage

### Process All Files

Process all 10 Japanese VS Code update files:

```bash
# Set environment variables
export GITHUB_TOKEN="your_token_here"
export AI_BASE_URL="https://models.inference.ai.azure.com/v1"
export AI_MODEL="gpt-4o-mini"

# Run the processing script
python3 scripts/process_vscode_jp_en_markers.py
```

### Dry Run Mode

Preview what would be processed without making API calls:

```bash
DRY_RUN=1 python3 scripts/process_vscode_jp_en_markers.py
```

### Validate Results

After processing, validate that all EN_CONTENT markers have been removed:

```bash
python3 scripts/validate_vscode_updates_jp_translations.py --forbid-en-content-markers
```

## What the Script Does

For each Japanese file (e.g., `2025-05-08-vscode-update-v1_100-jp.md`):

1. **Identifies EN_CONTENT blocks**: Finds all content between `<!-- EN_CONTENT_BEGIN -->` and `<!-- EN_CONTENT_END -->` markers

2. **Extracts context**: Gets 3 lines of surrounding Japanese content for context

3. **Calls LLM**: Sends the English content to an OpenAI-compatible API with instructions to:
   - Provide detailed technical explanation in Japanese
   - Go beyond literal translation to explain purpose, usage, and impact
   - Use bullet points and short paragraphs for readability
   - Preserve URLs, links, and code blocks
   - Avoid marketing language

4. **Replaces content**: Replaces the entire block (including markers) with the Japanese explanation

5. **Saves file**: Writes the updated content back to the file

## Expected Transformation

### Before (with EN_CONTENT markers):

```markdown
## Overview
このリリースは、Copilot Chat の機能強化に注力しています。

<!-- EN_CONTENT_BEGIN -->

_Release date: May 8, 2025_

<!-- EN_CONTENT_END -->

## Source Content (normalized)
```

### After (with Japanese explanation):

```markdown
## Overview
このリリースは、Copilot Chat の機能強化に注力しています。

リリース日: 2025年5月8日

## Source Content (normalized)
```

## Files to Process

Total: 10 files with 172 EN_CONTENT blocks

1. `2025-05-08-vscode-update-v1_100-jp.md` (16 blocks)
2. `2025-06-12-vscode-update-v1_101-jp.md` (17 blocks)
3. `2025-07-09-vscode-update-v1_102-jp.md` (15 blocks)
4. `2025-08-07-vscode-update-v1_103-jp.md` (16 blocks)
5. `2025-09-11-vscode-update-v1_104-jp.md` (17 blocks)
6. `2025-10-09-vscode-update-v1_105-jp.md` (18 blocks)
7. `2025-11-12-vscode-update-v1_106-jp.md` (21 blocks)
8. `2025-12-10-vscode-update-v1_107-jp.md` (20 blocks)
9. `2026-01-08-vscode-update-v1_108-jp.md` (16 blocks)
10. `2026-02-04-vscode-update-v1_109-jp.md` (16 blocks)

## Processing Time

With rate limiting delays (0.5s between calls), expect:
- ~86 seconds per file (average 17 blocks)
- ~15 minutes total for all 10 files

## Error Handling

The script includes:
- 3 retry attempts for failed API calls
- Exponential backoff for rate limiting
- Detailed error messages for debugging
- Progress tracking for each file and block

## Troubleshooting

### "No API token found"
- Ensure `GITHUB_TOKEN` or `AI_API_KEY` is set in environment or `.env` file

### "API call failed"
- Check your token has correct permissions
- Verify `AI_BASE_URL` is correct
- Ensure `AI_MODEL` is available in your API

### "Some files failed to process"
- Check error messages for specific failures
- Rerun the script (it will process remaining blocks)
- Consider processing files individually for debugging
