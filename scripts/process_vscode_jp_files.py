#!/usr/bin/env python3
"""
Process VS Code JP files to remove EN_CONTENT markers and replace with Japanese explanations.
"""

import os
import re
import sys
from pathlib import Path
import json

try:
    from openai import OpenAI
except ImportError:
    print("Error: OpenAI library not installed. Run: pip install openai")
    sys.exit(1)


def get_openai_client():
    """Create and return an OpenAI client configured for the AI endpoint."""
    api_key = os.environ.get("AI_API_KEY") or os.environ.get("GITHUB_TOKEN")
    base_url = os.environ.get("AI_BASE_URL")
    
    if not api_key:
        raise ValueError("GITHUB_TOKEN or AI_API_KEY environment variable is required")
    if not base_url:
        raise ValueError("AI_BASE_URL environment variable is required")
    
    return OpenAI(api_key=api_key, base_url=base_url)


def extract_en_blocks(content: str) -> list[tuple[int, int, str]]:
    """
    Extract all EN_CONTENT blocks with their positions.
    Returns list of (start_pos, end_pos, english_content).
    """
    pattern = r'<!-- EN_CONTENT_BEGIN -->\s*(.*?)\s*<!-- EN_CONTENT_END -->'
    blocks = []
    for match in re.finditer(pattern, content, re.DOTALL):
        blocks.append((match.start(), match.end(), match.group(1).strip()))
    return blocks


def translate_to_japanese(english_content: str, context: str = "") -> str:
    """
    Use LLM to translate/explain English content in detailed Japanese.
    """
    client = get_openai_client()
    
    system_prompt = """あなたは VS Code のリリースノートを日本語で詳しく解説する技術翻訳の専門家です。

要件:
- 英語の内容を詳細な日本語の解説に変換してください
- 単なる直訳ではなく、深い理解と解釈を提供してください（深く詳細に理解と解釈）
- 技術的な正確性を保ちながら、読者に分かりやすく説明してください
- マークダウン形式を保持してください
- コードブロック、リンク、画像参照などはそのまま保持してください
- 箇条書きや段落構造も適切に保ってください
- 専門用語は適切な日本語訳を使い、必要に応じて原語を併記してください
"""

    user_prompt = f"""以下の英語コンテンツを、詳細で分かりやすい日本語の解説に変換してください。

コンテキスト情報:
{context}

英語コンテンツ:
{english_content}

詳細な日本語解説を提供してください。"""

    try:
        response = client.chat.completions.create(
            model=os.environ.get("AI_MODEL", "gpt-4o"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error calling LLM: {e}")
        raise


def process_file(jp_file_path: Path, en_file_path: Path) -> bool:
    """
    Process a single JP file to remove EN_CONTENT markers and replace with Japanese.
    """
    print(f"\nProcessing: {jp_file_path.name}")
    
    # Read both files
    jp_content = jp_file_path.read_text(encoding='utf-8')
    en_content = en_file_path.read_text(encoding='utf-8') if en_file_path.exists() else ""
    
    # Extract EN blocks
    en_blocks = extract_en_blocks(jp_content)
    
    if not en_blocks:
        print(f"  No EN_CONTENT markers found")
        return True
    
    print(f"  Found {len(en_blocks)} EN_CONTENT blocks")
    
    # Process blocks in reverse order to maintain positions
    new_content = jp_content
    for i, (start_pos, end_pos, english_text) in enumerate(reversed(en_blocks)):
        block_num = len(en_blocks) - i
        print(f"  Processing block {block_num}/{len(en_blocks)}...")
        
        # Get context (section heading before this block if available)
        context_start = max(0, start_pos - 500)
        context = jp_content[context_start:start_pos]
        
        # Find the most recent heading
        heading_match = re.search(r'(#{1,6}\s+.+)$', context, re.MULTILINE)
        context_info = heading_match.group(1) if heading_match else "VS Code update content"
        
        # Translate to Japanese
        try:
            japanese_text = translate_to_japanese(english_text, context_info)
            
            # Replace the entire block (including markers) with Japanese content
            new_content = new_content[:start_pos] + japanese_text + new_content[end_pos:]
            
            print(f"    ✓ Block {block_num} translated")
        except Exception as e:
            print(f"    ✗ Error translating block {block_num}: {e}")
            return False
    
    # Write the updated content
    jp_file_path.write_text(new_content, encoding='utf-8')
    print(f"  ✓ File updated successfully")
    
    return True


def main():
    # Check for required environment variables
    if not (os.environ.get("GITHUB_TOKEN") or os.environ.get("AI_API_KEY")):
        print("Error: GITHUB_TOKEN or AI_API_KEY environment variable is required")
        sys.exit(1)
    
    if not os.environ.get("AI_BASE_URL"):
        print("Error: AI_BASE_URL environment variable is required")
        sys.exit(1)
    
    # Define paths
    repo_root = Path(__file__).parent.parent
    jp_dir = repo_root / "vscode-updates-jp"
    en_dir = repo_root / "vscode-updates"
    
    # Get all JP files (excluding index.md)
    jp_files = sorted([f for f in jp_dir.glob("2025-*.md") if f.name != "index.md"])
    jp_files.extend(sorted([f for f in jp_dir.glob("2026-*.md") if f.name != "index.md"]))
    
    print(f"Found {len(jp_files)} Japanese files to process")
    
    success_count = 0
    fail_count = 0
    
    for jp_file in jp_files:
        # Construct corresponding EN file path
        en_filename = jp_file.name.replace("-jp.md", ".md")
        en_file = en_dir / en_filename
        
        try:
            if process_file(jp_file, en_file):
                success_count += 1
            else:
                fail_count += 1
        except Exception as e:
            print(f"  ✗ Failed: {e}")
            fail_count += 1
    
    print(f"\n{'='*60}")
    print(f"Processing complete:")
    print(f"  Success: {success_count}")
    print(f"  Failed: {fail_count}")
    print(f"{'='*60}")
    
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
