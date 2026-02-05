#!/usr/bin/env python3
"""
Process a single Japanese VS Code update file - for testing/demonstration.
"""
import os
import re
import sys
from pathlib import Path

def extract_first_en_block(content: str):
    """Extract the first EN_CONTENT block."""
    pattern = r'<!-- EN_CONTENT_BEGIN -->\s*(.*?)\s*<!-- EN_CONTENT_END -->'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return {
            'content': match.group(1).strip(),
            'start': match.start(),
            'end': match.end(),
            'full_match': match.group(0)
        }
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 process_single_file.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    filepath = Path("vscode-updates-jp") / filename
    
    if not filepath.exists():
        print(f"File not found: {filepath}")
        sys.exit(1)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count all blocks
    all_blocks = re.findall(r'<!-- EN_CONTENT_BEGIN -->.*?<!-- EN_CONTENT_END -->', content, re.DOTALL)
    print(f"File: {filename}")
    print(f"Total EN_CONTENT blocks: {len(all_blocks)}")
    print()
    
    # Show first block
    first_block = extract_first_en_block(content)
    if first_block:
        print("First EN_CONTENT block:")
        print("=" * 80)
        print(first_block['content'][:500])
        if len(first_block['content']) > 500:
            print(f"... (truncated, total {len(first_block['content'])} chars)")
        print("=" * 80)
    else:
        print("No EN_CONTENT blocks found")

if __name__ == "__main__":
    main()
