#!/bin/bash
# Script to process all VS Code JP files and remove EN_CONTENT markers

set -e

echo "================================"
echo "VS Code JP Files Processing"
echo "================================"
echo ""

# Check for required environment variables
if [ -z "$GITHUB_TOKEN" ] && [ -z "$AI_API_KEY" ]; then
    echo "ERROR: GITHUB_TOKEN or AI_API_KEY environment variable is required"
    echo ""
    echo "Please set one of these environment variables:"
    echo "  export GITHUB_TOKEN='your_token'"
    echo "  export AI_API_KEY='your_api_key'"
    exit 1
fi

if [ -z "$AI_BASE_URL" ]; then
    echo "ERROR: AI_BASE_URL environment variable is required"
    echo ""
    echo "Example:"
    echo "  export AI_BASE_URL='https://models.inference.ai.azure.com/v1'"
    exit 1
fi

if [ -z "$AI_MODEL" ]; then
    echo "WARNING: AI_MODEL not set, using default 'gpt-4o'"
    export AI_MODEL="gpt-4o"
fi

echo "Configuration:"
echo "  AI_BASE_URL: $AI_BASE_URL"
echo "  AI_MODEL: $AI_MODEL"
echo "  Token: [SET]"
echo ""

# Count current EN_CONTENT markers
echo "Current state:"
echo "---"
python3 scripts/process_single_file.py 2025-05-08-vscode-update-v1_100-jp.md | grep "Total EN_CONTENT blocks"
python3 scripts/process_single_file.py 2025-06-12-vscode-update-v1_101-jp.md | grep "Total EN_CONTENT blocks"
python3 scripts/process_single_file.py 2025-07-09-vscode-update-v1_102-jp.md | grep "Total EN_CONTENT blocks"
python3 scripts/process_single_file.py 2025-08-07-vscode-update-v1_103-jp.md | grep "Total EN_CONTENT blocks"
python3 scripts/process_single_file.py 2025-09-11-vscode-update-v1_104-jp.md | grep "Total EN_CONTENT blocks"
python3 scripts/process_single_file.py 2025-10-09-vscode-update-v1_105-jp.md | grep "Total EN_CONTENT blocks"
python3 scripts/process_single_file.py 2025-11-12-vscode-update-v1_106-jp.md | grep "Total EN_CONTENT blocks"
python3 scripts/process_single_file.py 2025-12-10-vscode-update-v1_107-jp.md | grep "Total EN_CONTENT blocks"
python3 scripts/process_single_file.py 2026-01-08-vscode-update-v1_108-jp.md | grep "Total EN_CONTENT blocks"
python3 scripts/process_single_file.py 2026-02-04-vscode-update-v1_109-jp.md | grep "Total EN_CONTENT blocks"
echo "---"
echo ""

# Confirm before proceeding
read -p "Process all files? This will make API calls. (y/N) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

# Run the processing script
echo ""
echo "Starting processing..."
python3 scripts/process_vscode_jp_files.py

# Validate results
echo ""
echo "Validating results..."
python3 scripts/validate_vscode_updates_jp_translations.py --forbid-en-content-markers

echo ""
echo "================================"
echo "Processing Complete!"
echo "================================"
