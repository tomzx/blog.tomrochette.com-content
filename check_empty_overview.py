#!/usr/bin/env python3
import os
import re
import glob

def check_empty_overview(file_path):
    """
    Check if a file has an empty Overview section.
    Returns True if Overview section exists and is empty.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for "# Overview" section
        overview_match = re.search(r'^# Overview\s*$', content, re.MULTILINE)
        if not overview_match:
            return False, "No Overview section found"
        
        # Get everything after "# Overview"
        after_overview = content[overview_match.end():]
        
        # Find the next header (any line starting with #)
        next_header_match = re.search(r'^\s*#[^#]', after_overview, re.MULTILINE)
        
        if next_header_match:
            # Content between Overview and next header
            between_content = after_overview[:next_header_match.start()].strip()
        else:
            # Content from Overview to end of file
            between_content = after_overview.strip()
        
        # Check if the content is empty (only whitespace)
        if not between_content:
            return True, "Empty Overview section"
        else:
            return False, f"Overview has content: {repr(between_content[:100])}"
            
    except Exception as e:
        return False, f"Error reading file: {e}"

def main():
    # Find all markdown files with "# Overview"
    md_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                md_files.append(file_path)
    
    empty_overview_files = []
    non_empty_overview_files = []
    
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                if '# Overview' in f.read():
                    is_empty, reason = check_empty_overview(file_path)
                    if is_empty:
                        empty_overview_files.append(file_path)
                    else:
                        non_empty_overview_files.append((file_path, reason))
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    print(f"Files with empty Overview sections ({len(empty_overview_files)}):")
    for file_path in sorted(empty_overview_files):
        print(f"  {file_path}")
    
    print(f"\nFiles with non-empty Overview sections ({len(non_empty_overview_files)}):")
    for file_path, reason in sorted(non_empty_overview_files):
        print(f"  {file_path}: {reason}")

if __name__ == "__main__":
    main()