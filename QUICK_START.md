# Quick Start: Process VS Code JP Files

## One-Line Solution

```bash
export GITHUB_TOKEN="your_token" AI_BASE_URL="https://models.inference.ai.azure.com/v1" AI_MODEL="gpt-4o" && python3 scripts/process_vscode_jp_files.py && python3 scripts/validate_vscode_updates_jp_translations.py --forbid-en-content-markers
```

## Current Status

- **Files**: 10 Japanese VS Code update files
- **Blocks**: 172 EN_CONTENT markers to replace
- **Script**: `scripts/process_vscode_jp_files.py` (ready to use)
- **Time**: ~10-15 minutes
- **Requirement**: Valid GITHUB_TOKEN or AI_API_KEY

## Files to Process

```
vscode-updates-jp/2025-05-08-vscode-update-v1_100-jp.md  (16 blocks)
vscode-updates-jp/2025-06-12-vscode-update-v1_101-jp.md  (17 blocks)
vscode-updates-jp/2025-07-09-vscode-update-v1_102-jp.md  (15 blocks)
vscode-updates-jp/2025-08-07-vscode-update-v1_103-jp.md  (16 blocks)
vscode-updates-jp/2025-09-11-vscode-update-v1_104-jp.md  (17 blocks)
vscode-updates-jp/2025-10-09-vscode-update-v1_105-jp.md  (18 blocks)
vscode-updates-jp/2025-11-12-vscode-update-v1_106-jp.md  (21 blocks)
vscode-updates-jp/2025-12-10-vscode-update-v1_107-jp.md  (20 blocks)
vscode-updates-jp/2026-01-08-vscode-update-v1_108-jp.md  (16 blocks)
vscode-updates-jp/2026-02-04-vscode-update-v1_109-jp.md  (16 blocks)
```

## After Running

Verify:
```bash
grep -c "EN_CONTENT_BEGIN" vscode-updates-jp/*.md
# Should all show: 0
```

Commit:
```bash
git add vscode-updates-jp/*.md
git commit -m "Replace EN_CONTENT markers with detailed Japanese explanations"
```

## Need Help?

- **Detailed Instructions**: See `READY_TO_RUN.md`
- **Troubleshooting**: See `PROCESSING_GUIDE.md`
- **Overview**: See `TASK_SUMMARY.md`
