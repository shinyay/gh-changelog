#!/usr/bin/env python3
"""
Process Japanese VS Code update files to replace EN_CONTENT markers with detailed Japanese explanations.
"""
import os
import re
import sys
import json
import time
from pathlib import Path
from typing import List, Tuple
import requests

# Configuration
VSCODE_UPDATES_DIR = Path("vscode-updates")
VSCODE_UPDATES_JP_DIR = Path("vscode-updates-jp")

# API configuration from environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") or os.getenv("AI_API_KEY")
AI_BASE_URL = os.getenv("AI_BASE_URL", "https://models.inference.ai.azure.com/v1")
AI_MODEL = os.getenv("AI_MODEL", "gpt-4o-mini")

# Check if we're in dry-run mode
DRY_RUN = os.getenv("DRY_RUN", "").lower() in ("1", "true", "yes")

if not GITHUB_TOKEN and not DRY_RUN:
    print("ERROR: GITHUB_TOKEN or AI_API_KEY environment variable is required", file=sys.stderr)
    print("       Or set DRY_RUN=1 to preview without making API calls", file=sys.stderr)
    sys.exit(1)

print(f"Using AI configuration:")
print(f"  Base URL: {AI_BASE_URL}")
print(f"  Model: {AI_MODEL}")
print(f"  Token: {'***' if GITHUB_TOKEN else 'NOT SET'}")
print(f"  Dry Run: {DRY_RUN}")
print()


def extract_en_content_blocks(content: str) -> List[Tuple[str, int, int]]:
    """Extract all EN_CONTENT blocks with their positions."""
    pattern = r'<!-- EN_CONTENT_BEGIN -->\s*(.*?)\s*<!-- EN_CONTENT_END -->'
    blocks = []
    for match in re.finditer(pattern, content, re.DOTALL):
        blocks.append((match.group(1).strip(), match.start(), match.end()))
    return blocks


def find_context_around_block(content: str, block_start: int, lines_before: int = 3) -> str:
    """Find context lines before the EN_CONTENT block."""
    lines = content[:block_start].split('\n')
    context_lines = lines[-lines_before:] if len(lines) >= lines_before else lines
    return '\n'.join(context_lines)


def call_llm_for_translation(english_content: str, context: str, attempt: int = 1) -> str:
    """Call LLM to generate detailed Japanese explanation."""
    
    if DRY_RUN:
        return f"[DRY RUN - Would translate {len(english_content)} chars of English content to Japanese]"
    
    system_prompt = """あなたは技術文書の翻訳専門家です。VS Codeのリリースノートの英語コンテンツを、日本語で詳細に説明してください。

要件:
1. 単純な直訳ではなく、技術的な背景や意味を深く理解して解釈した上で、日本語で詳しく説明してください
2. 機能の目的、使い方、影響範囲などを明確にしてください
3. マーケティング的な表現は避け、実用的な視点で書いてください
4. 箇条書きや短い段落を使い、読みやすくしてください
5. リンクやURLはそのまま保持してください
6. コードブロックがある場合は、そのまま保持してください
7. 英語の専門用語は必要に応じてカタカナで補足してください
8. HTMLコメント(<!-- ... -->)は出力に含めないでください

出力形式: Markdown形式で、直接日本語の説明を返してください。"""

    user_prompt = f"""次の英語コンテンツを詳細な日本語の説明に変換してください。

【前後の文脈】
{context}

【英語コンテンツ】
{english_content}

詳細な日本語の説明を返してください:"""

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }
    
    payload = {
        "model": AI_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 2000
    }
    
    try:
        response = requests.post(
            f"{AI_BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        result = response.json()
        
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"].strip()
        else:
            raise ValueError("No choices in API response")
            
    except Exception as e:
        print(f"  ⚠ API call failed (attempt {attempt}): {e}", file=sys.stderr)
        if attempt < 3:
            time.sleep(2 * attempt)
            return call_llm_for_translation(english_content, context, attempt + 1)
        raise


def process_file(jp_file_path: Path, en_file_path: Path) -> int:
    """Process a single Japanese file to replace EN_CONTENT blocks."""
    
    print(f"\n{'='*80}")
    print(f"Processing: {jp_file_path.name}")
    print(f"{'='*80}")
    
    # Read files
    with open(jp_file_path, 'r', encoding='utf-8') as f:
        jp_content = f.read()
    
    # Extract EN_CONTENT blocks
    blocks = extract_en_content_blocks(jp_content)
    if not blocks:
        print(f"  ✓ No EN_CONTENT blocks found")
        return 0
    
    print(f"  Found {len(blocks)} EN_CONTENT blocks")
    
    # Process blocks in reverse order to maintain positions
    modified_content = jp_content
    replacements_made = 0
    
    for idx, (en_text, start_pos, end_pos) in enumerate(reversed(blocks), 1):
        block_num = len(blocks) - idx + 1
        print(f"\n  Block {block_num}/{len(blocks)}:")
        print(f"    Length: {len(en_text)} chars")
        print(f"    Preview: {en_text[:100]}..." if len(en_text) > 100 else f"    Content: {en_text}")
        
        # Get context
        context = find_context_around_block(modified_content, start_pos)
        
        # Call LLM for translation
        print(f"    Calling LLM...")
        try:
            japanese_explanation = call_llm_for_translation(en_text, context)
            
            # Replace the entire block (including markers) with Japanese explanation
            before = modified_content[:start_pos]
            after = modified_content[end_pos:]
            modified_content = before + japanese_explanation + after
            
            replacements_made += 1
            print(f"    ✓ Replaced with {len(japanese_explanation)} chars of Japanese")
            
            # Small delay to avoid rate limiting
            time.sleep(0.5)
            
        except Exception as e:
            print(f"    ✗ Failed to process block: {e}", file=sys.stderr)
            continue
    
    # Save the modified content
    if replacements_made > 0:
        if not DRY_RUN:
            with open(jp_file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            print(f"\n  ✓ Saved {jp_file_path.name} ({replacements_made} blocks replaced)")
        else:
            print(f"\n  ℹ DRY RUN: Would save {jp_file_path.name} ({replacements_made} blocks replaced)")
    else:
        print(f"\n  ✗ No replacements made")
    
    return replacements_made


def main():
    """Main processing function."""
    
    # Get list of Japanese files to process
    jp_files = sorted(VSCODE_UPDATES_JP_DIR.glob("*-jp.md"))
    jp_files = [f for f in jp_files if f.name != "index.md"]
    
    print(f"Found {len(jp_files)} Japanese files to process")
    
    total_blocks_replaced = 0
    files_processed = 0
    files_failed = 0
    
    for jp_file in jp_files:
        # Derive English file path
        en_filename = jp_file.name.replace("-jp.md", ".md")
        en_file = VSCODE_UPDATES_DIR / en_filename
        
        if not en_file.exists():
            print(f"\n⚠ Warning: English source file not found: {en_file}")
            files_failed += 1
            continue
        
        try:
            blocks_replaced = process_file(jp_file, en_file)
            total_blocks_replaced += blocks_replaced
            files_processed += 1
        except Exception as e:
            print(f"\n✗ Error processing {jp_file.name}: {e}", file=sys.stderr)
            files_failed += 1
            continue
    
    # Summary
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"Files processed: {files_processed}")
    print(f"Files failed: {files_failed}")
    print(f"Total EN_CONTENT blocks replaced: {total_blocks_replaced}")
    print()
    
    if files_failed > 0:
        print(f"⚠ Some files failed to process. Check errors above.")
        sys.exit(1)
    else:
        print(f"✓ All files processed successfully!")


if __name__ == "__main__":
    main()
