#!/usr/bin/env python3
"""
Generate press data from CV CSV files for Jekyll.
Processes press articles and generates Jekyll-compatible YAML data.
"""

import os
import sys
import csv
import yaml
from pathlib import Path
from datetime import datetime

# Paths
SITE_ROOT = Path(__file__).parent.parent
CV_DATA_DIR = SITE_ROOT / "_data" / "cv_data" / "data"
OUTPUT_DIR = SITE_ROOT / "_data"

def load_csv_data(filename):
    """Load data from a CSV file."""
    filepath = CV_DATA_DIR / filename
    if not filepath.exists():
        print(f"⚠️  File not found: {filepath}")
        return []
    
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Clean up the data
            cleaned_row = {}
            for key, value in row.items():
                cleaned_row[key] = value.strip() if value else ""
            data.append(cleaned_row)
    
    return data

def generate_press_yaml():
    """Generate press.yml for Jekyll."""
    print("=" * 60)
    print("Press Data Generator")
    print("=" * 60)
    
    print(f"📂 Site root: {SITE_ROOT}")
    print(f"📂 CV data directory: {CV_DATA_DIR}")
    
    # Load press data
    print("\n📰 Loading press data...")
    press_articles = load_csv_data("press.csv")
    
    if not press_articles:
        print("❌ No press articles found")
        return []
    
    print(f"   Found {len(press_articles)} press articles")
    
    # Sort by year (newest first), then by title for same year
    press_articles.sort(key=lambda x: (x.get('Year', ''), x.get('Title', '')), reverse=True)
    
    # Write to YAML file
    output_file = OUTPUT_DIR / "press.yml"
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(press_articles, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=1000)
    
    print(f"✅ Generated: {output_file}")
    
    # Show some stats
    years = set(article.get('Year', '') for article in press_articles if article.get('Year'))
    sources = set(article.get('Source', '') for article in press_articles if article.get('Source'))
    
    print(f"   Articles span {len(years)} years: {sorted(years, reverse=True)}")
    print(f"   From {len(sources)} sources: {sorted(sources)}")
    
    print("\n" + "=" * 60)
    print("✨ Done! Press data has been generated.")
    print("=" * 60)
    print(f"\nGenerated {len(press_articles)} press articles in {output_file}")
    print("\nNext steps:")
    print("1. Create press.md page to display the data")
    print("2. Add navigation link to press page")
    print("3. Test the integration")
    print("=" * 60)
    
    return press_articles

if __name__ == "__main__":
    generate_press_yaml()
