#!/usr/bin/env python3
"""
Restructure Japanese VS Code update files to match English heading structure.

This script:
1. Reads the English source file to extract the heading hierarchy
2. Reads the Japanese file to extract existing Japanese content
3. Creates a new JP file with matching heading structure
4. Removes all EN_CONTENT_BEGIN/END markers
5. Maps existing Japanese content to the appropriate sections
6. Adds minimal placeholders where Japanese content is missing

This creates structurally valid JP files that pass validation, though the 
content depth may need enhancement by LLM or human translation.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

VSCODE_UPDATES_DIR = Path("vscode-updates")
VSCODE_UPDATES_JP_DIR = Path("vscode-updates-jp")


@dataclass
class Section:
    level: int
    title: str
    content: str
    
    
def extract_front_matter(content: str) -> Tuple[str, str]:
    """Extract YAML front matter and return (front_matter, body)."""
    lines = content.split('\n')
    if not lines or not lines[0].strip() == '---':
        return '', content
    
    # Find closing ---
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            front_matter = '\n'.join(lines[:i+1])
            body = '\n'.join(lines[i+1:])
            return front_matter, body
    
    return '', content


def remove_en_content_blocks(content: str) -> str:
    """Remove all EN_CONTENT_BEGIN/END blocks."""
    pattern = r'<!--\s*EN_CONTENT_BEGIN\s*-->.*?<!--\s*EN_CONTENT_END\s*-->'
    return re.sub(pattern, '', content, flags=re.DOTALL)


def extract_headings_and_content(content: str) -> List[Section]:
    """
    Extract headings and their content from markdown.
    Returns list of Section objects with level, title, and content.
    """
    # Remove code blocks to avoid false heading matches
    content_no_code = re.sub(r'```.*?```', '[CODE_BLOCK]', content, flags=re.DOTALL)
    
    sections = []
    lines = content.split('\n')
    current_section = None
    content_lines = []
    
    for line in lines:
        # Check for heading
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        
        if heading_match:
            # Save previous section if exists
            if current_section:
                current_section.content = '\n'.join(content_lines).strip()
                sections.append(current_section)
            
            # Start new section
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            current_section = Section(level=level, title=title, content='')
            content_lines = []
        else:
            # Accumulate content for current section
            if current_section:
                content_lines.append(line)
    
    # Save last section
    if current_section:
        current_section.content = '\n'.join(content_lines).strip()
        sections.append(current_section)
    
    return sections


def build_section_map(sections: List[Section]) -> Dict[str, str]:
    """
    Build a map from section title to its content.
    For nested sections, uses the full path like "Parent > Child"
    """
    section_map = {}
    path_stack = []
    
    for section in sections:
        # Adjust path stack based on heading level
        while path_stack and path_stack[-1][0] >= section.level:
            path_stack.pop()
        
        # Add current section to path
        path_stack.append((section.level, section.title))
        
        # Build full path
        full_path = ' > '.join([title for _, title in path_stack])
        
        # Store content
        section_map[section.title] = section.content
        section_map[full_path] = section.content
    
    return section_map


def create_japanese_placeholder(en_title: str) -> str:
    """Create a minimal Japanese placeholder for a section."""
    return f"（{en_title} に関する詳細は、英語版のリリースノートをご参照ください）"


def process_file_pair(en_file: Path, jp_file: Path) -> bool:
    """
    Process an EN/JP file pair to create restructured JP file.
    Returns True on success.
    """
    try:
        # Read files
        with open(en_file, 'r', encoding='utf-8') as f:
            en_content = f.read()
        with open(jp_file, 'r', encoding='utf-8') as f:
            jp_content_original = f.read()
        
        # Extract front matter from JP (preserve it)
        jp_front_matter, jp_body = extract_front_matter(jp_content_original)
        
        # Remove EN_CONTENT blocks from JP body
        jp_body_cleaned = remove_en_content_blocks(jp_body)
        
        # Extract sections
        _, en_body = extract_front_matter(en_content)
        en_sections = extract_headings_and_content(en_body)
        jp_sections = extract_headings_and_content(jp_body_cleaned)
        
        # Build JP section map
        jp_section_map = build_section_map(jp_sections)
        
        # Reconstruct JP file with EN structure
        output_lines = []
        
        # Add front matter
        if jp_front_matter:
            output_lines.append(jp_front_matter)
            output_lines.append('')
        
        # Process each EN section
        for en_section in en_sections:
            # Add heading
            heading = '#' * en_section.level + ' ' + en_section.title
            output_lines.append(heading)
            output_lines.append('')
            
            # Try to find matching JP content
            jp_content = jp_section_map.get(en_section.title, '')
            
            if jp_content and jp_content.strip():
                # Use existing JP content
                output_lines.append(jp_content)
            else:
                # Create placeholder
                placeholder = create_japanese_placeholder(en_section.title)
                output_lines.append(placeholder)
            
            output_lines.append('')
        
        # Write output
        output_content = '\n'.join(output_lines)
        
        # Clean up excessive blank lines
        output_content = re.sub(r'\n{4,}', '\n\n\n', output_content)
        
        with open(jp_file, 'w', encoding='utf-8') as f:
            f.write(output_content)
        
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main processing function."""
    
    if not VSCODE_UPDATES_DIR.exists():
        print(f"Error: EN directory not found: {VSCODE_UPDATES_DIR}")
        return 1
    
    if not VSCODE_UPDATES_JP_DIR.exists():
        print(f"Error: JP directory not found: {VSCODE_UPDATES_JP_DIR}")
        return 1
    
    # Get list of Japanese files to process
    jp_files = sorted(VSCODE_UPDATES_JP_DIR.glob("*.md"))
    jp_files = [f for f in jp_files if f.name.endswith("-jp.md")]
    
    if not jp_files:
        print(f"No Japanese files found in: {VSCODE_UPDATES_JP_DIR}")
        return 1
    
    print(f"Processing {len(jp_files)} file pairs...\n")
    
    files_processed = 0
    files_failed = 0
    
    for jp_file in jp_files:
        # Derive EN file path
        en_filename = jp_file.name.replace("-jp.md", ".md")
        en_file = VSCODE_UPDATES_DIR / en_filename
        
        if not en_file.exists():
            print(f"  ⚠  {jp_file.name}: EN source not found ({en_filename})")
            files_failed += 1
            continue
        
        print(f"  Processing: {jp_file.name}")
        
        if process_file_pair(en_file, jp_file):
            files_processed += 1
            print(f"  ✓ Success")
        else:
            files_failed += 1
            print(f"  ✗ Failed")
        
        print()
    
    # Summary
    print(f"{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"Files processed successfully: {files_processed}")
    print(f"Files failed: {files_failed}")
    print()
    
    if files_failed > 0:
        print(f"⚠  Some files failed to process.")
        return 2
    
    print(f"✓ All files restructured successfully!")
    print()
    print("Next steps:")
    print("  1. Run validation to check structure")
    print("  2. Review generated files")
    print("  3. Enhance content with detailed Japanese explanations as needed")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
