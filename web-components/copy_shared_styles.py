#!/usr/bin/env python3
"""
Copy shared styles to each lab directory for GitHub Pages deployment

Each lab is deployed as a separate repository (lab01-student, lab02-student, etc.)
so the shared styles need to be copied into each lab directory.
"""

import os
import shutil
from pathlib import Path

def copy_shared_styles():
    """Copy shared styles to each lab directory"""
    web_components_dir = Path(__file__).parent
    shared_dir = web_components_dir / "shared"
    
    if not shared_dir.exists():
        print(f"❌ Shared directory not found: {shared_dir}")
        return
    
    # Find all lab directories
    lab_dirs = [d for d in web_components_dir.iterdir() 
                if d.is_dir() and d.name.startswith('lab') and d.name != 'shared']
    
    print("📁 Copying shared styles to lab directories...")
    print("=" * 50)
    
    copied_count = 0
    
    for lab_dir in sorted(lab_dirs):
        lab_shared_dir = lab_dir / "shared"
        
        # Remove existing shared directory if it exists
        if lab_shared_dir.exists():
            shutil.rmtree(lab_shared_dir)
        
        # Copy the entire shared directory
        try:
            shutil.copytree(shared_dir, lab_shared_dir)
            print(f"✅ Copied shared styles to {lab_dir.name}/")
            copied_count += 1
        except Exception as e:
            print(f"❌ Failed to copy to {lab_dir.name}/: {e}")
    
    print("=" * 50)
    print(f"📊 Summary: Copied shared styles to {copied_count} lab directories")
    
    if copied_count > 0:
        print("\n✅ All labs now have local copies of shared styles!")
        print("   This enables proper styling when deployed as separate GitHub Pages.")
    else:
        print("\n⚠️  No shared styles were copied.")

if __name__ == "__main__":
    copy_shared_styles()