#!/usr/bin/env python3
"""
Update CV from sidd-cv submodule to assets directory.
This ensures the website always uses the latest CV from the submodule.
"""

import os
import sys
import shutil
from pathlib import Path

# Paths
SITE_ROOT = Path(__file__).parent.parent
CV_SOURCE = SITE_ROOT / "_data" / "cv_data" / "sidd-cv.pdf"
CV_DEST = SITE_ROOT / "assets" / "SiddharthaSrinivasaCV.pdf"

def update_cv():
    """Copy the latest CV from submodule to assets directory."""
    print("=" * 60)
    print("CV Update Script")
    print("=" * 60)
    
    print(f"📂 Site root: {SITE_ROOT}")
    print(f"📂 CV source: {CV_SOURCE}")
    print(f"📂 CV destination: {CV_DEST}")
    
    # Check if source CV exists
    if not CV_SOURCE.exists():
        print(f"❌ Source CV not found: {CV_SOURCE}")
        print("   Make sure the cv_data submodule is initialized")
        return False
    
    # Check if destination directory exists
    CV_DEST.parent.mkdir(parents=True, exist_ok=True)
    
    # Copy the CV
    try:
        shutil.copy2(CV_SOURCE, CV_DEST)
        print(f"✅ CV updated successfully!")
        print(f"   Source: {CV_SOURCE}")
        print(f"   Destination: {CV_DEST}")
        
        # Show file sizes for comparison
        source_size = CV_SOURCE.stat().st_size
        dest_size = CV_DEST.stat().st_size
        print(f"   Source size: {source_size:,} bytes")
        print(f"   Destination size: {dest_size:,} bytes")
        
        return True
        
    except Exception as e:
        print(f"❌ Error copying CV: {e}")
        return False

if __name__ == "__main__":
    success = update_cv()
    sys.exit(0 if success else 1)
