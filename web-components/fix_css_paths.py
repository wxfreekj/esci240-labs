#!/usr/bin/env python3
"""
Fix CSS paths in all lab HTML files
Changes ./shared/styles/ to ../shared/styles/
"""

import os
import re
from pathlib import Path


def fix_css_paths(file_path):
    """Fix CSS paths in an HTML file"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace ./shared/styles/ with ../shared/styles/
    updated_content = re.sub(
        r'href="\.\/shared\/styles\/', 'href="../shared/styles/', content
    )

    # Also handle the different attribute order (href= vs rel=)
    updated_content = re.sub(
        r'href="\.\/shared\/styles\/', 'href="../shared/styles/', updated_content
    )

    if content != updated_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"✅ Fixed: {file_path}")
        return True
    else:
        print(f"⏭️  No changes needed: {file_path}")
        return False


def main():
    """Fix CSS paths in all lab HTML files"""
    web_components_dir = Path(__file__).parent
    lab_dirs = [
        d
        for d in web_components_dir.iterdir()
        if d.is_dir() and d.name.startswith("lab")
    ]

    fixed_count = 0
    total_count = 0

    print("🔧 Fixing CSS paths in lab HTML files...")
    print("=" * 50)

    for lab_dir in sorted(lab_dirs):
        html_file = lab_dir / "index.html"
        if html_file.exists():
            total_count += 1
            if fix_css_paths(html_file):
                fixed_count += 1

    print("=" * 50)
    print(f"📊 Summary: Fixed {fixed_count} out of {total_count} files")

    if fixed_count > 0:
        print("\n✅ All CSS paths have been corrected!")
        print("   Labs should now display properly with styling.")
    else:
        print("\n⚠️  No files needed fixing.")


if __name__ == "__main__":
    main()
