#!/usr/bin/env python3
"""
Revert CSS paths for GitHub Pages compatibility
Changes all ../shared/styles/ references to shared/styles/
"""

import os
import re


def fix_css_paths_for_github_pages():
    """Fix CSS paths in all lab HTML files for GitHub Pages deployment"""

    # Base directory containing all labs
    web_components_dir = "."

    # Pattern to match CSS links with ../shared/styles/
    pattern = r'(href=["\']\.\./shared/styles/)'
    replacement = r'href="shared/styles/'

    files_updated = 0

    # Process each lab directory
    for i in range(1, 11):
        lab_dir = f"lab{i:02d}"
        html_file = os.path.join(web_components_dir, lab_dir, "index.html")

        if os.path.exists(html_file):
            print(f"Processing {html_file}...")

            try:
                # Read the file
                with open(html_file, "r", encoding="utf-8") as f:
                    content = f.read()

                # Count matches before replacement
                matches_before = len(re.findall(pattern, content))

                if matches_before > 0:
                    # Replace the paths
                    new_content = re.sub(pattern, replacement, content)

                    # Write back to file
                    with open(html_file, "w", encoding="utf-8") as f:
                        f.write(new_content)

                    # Count matches after replacement to verify
                    matches_after = len(re.findall(pattern, new_content))

                    print(f"  ✅ Updated {matches_before} CSS path(s) in {html_file}")
                    files_updated += 1
                else:
                    print(f"  ℹ️  No CSS paths to update in {html_file}")

            except Exception as e:
                print(f"  ❌ Error processing {html_file}: {e}")
        else:
            print(f"  ⚠️  File not found: {html_file}")

    print(f"\n🎉 Completed! Updated CSS paths in {files_updated} files.")
    print("✅ GitHub Pages deployment should now work correctly.")
    print("⚠️  Local development will show broken styles (this is expected).")


if __name__ == "__main__":
    fix_css_paths_for_github_pages()
