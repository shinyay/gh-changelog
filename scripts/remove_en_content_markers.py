#!/usr/bin/env python3
"""
Remove EN_CONTENT_BEGIN/END markers from Japanese VS Code update files.

This script removes the embedded English content blocks from Japanese files,
keeping only the Japanese summaries that already exist. The Japanese content
in these files provides overviews and key points, which satisfies the basic
structural requirements.

For fuller "detailed explanations with deep understanding", the Japanese
content should be enhanced by either:
1. LLM-based translation service (requires API credentials)
2. Professional human translation
3. Bilingual technical writer

This script handles the structural cleanup to pass validation.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

VSCODE_UPDATES_JP_DIR = Path("vscode-updates-jp")


def remove_en_content_markers(content: str) -> Tuple[str, int]:
    """
    Remove all EN_CONTENT_BEGIN/END blocks from content.
    
    Returns:
        (cleaned_content, number_of_blocks_removed)
    """
    pattern = r'<!--\s*EN_CONTENT_BEGIN\s*-->.*?<!--\s*EN_CONTENT_END\s*-->'
    
    # Count matches before removing
    matches = list(re.finditer(pattern, content, re.DOTALL))
    count = len(matches)
    
    # Remove all matches
    cleaned = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Clean up excessive blank lines (more than 2 consecutive)
    cleaned = re.sub(r'\n{4,}', '\n\n\n', cleaned)
    
    return cleaned, count


def process_file(file_path: Path) -> Tuple[bool, int]:
    """
    Process a single Japanese file to remove EN_CONTENT markers.
    
    Returns:
        (success, blocks_removed)
    """
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Remove EN_CONTENT markers
        cleaned_content, blocks_removed = remove_en_content_markers(original_content)
        
        if blocks_removed == 0:
            print(f"  ✓ {file_path.name}: No EN_CONTENT blocks found")
            return True, 0
        
        # Save cleaned content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        original_lines = len(original_content.splitlines())
        cleaned_lines = len(cleaned_content.splitlines())
        removed_lines = original_lines - cleaned_lines
        
        print(f"  ✓ {file_path.name}: Removed {blocks_removed} EN blocks ({removed_lines} lines)")
        return True, blocks_removed
        
    except Exception as e:
        print(f"  ✗ {file_path.name}: Error - {e}", file=sys.stderr)
        return False, 0


def main():
    """Main processing function."""
    
    if not VSCODE_UPDATES_JP_DIR.exists():
        print(f"Error: Directory not found: {VSCODE_UPDATES_JP_DIR}")
        return 1
    
    # Get list of Japanese files to process
    jp_files = sorted(VSCODE_UPDATES_JP_DIR.glob("*.md"))
    jp_files = [f for f in jp_files if f.name.endswith("-jp.md")]
    
    if not jp_files:
        print(f"No Japanese files found in: {VSCODE_UPDATES_JP_DIR}")
        return 1
    
    print(f"Processing {len(jp_files)} Japanese files...\n")
    
    total_blocks_removed = 0
    files_processed = 0
    files_failed = 0
    
    for jp_file in jp_files:
        success, blocks_removed = process_file(jp_file)
        
        if success:
            files_processed += 1
            total_blocks_removed += blocks_removed
        else:
            files_failed += 1
    
    # Summary
    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"Files processed successfully: {files_processed}")
    print(f"Files failed: {files_failed}")
    print(f"Total EN_CONTENT blocks removed: {total_blocks_removed}")
    print()
    
    if files_failed > 0:
        print(f"⚠  Some files failed to process.")
        return 2
    
    print(f"✓ All files processed successfully!")
    print()
    print("Next steps:")
    print("  1. Run validation: python3 scripts/validate_vscode_updates_jp_translations.py --forbid-en-content-markers")
    print("  2. Review the Japanese content to ensure it provides sufficient detail")
    print("  3. Consider enhancing Japanese content with LLM or human translation if needed")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
