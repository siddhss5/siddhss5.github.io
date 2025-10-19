#!/usr/bin/env python3
"""
Awards Data Generator for Jekyll Site

This script generates Jekyll-compatible YAML data files from awards.csv
and links them to publications using citation keys.

Usage:
    python3 scripts/generate_awards.py

Outputs:
    - _data/awards.yml

Copyright (c) 2024 Personal Robotics Laboratory, University of Washington
MIT License
"""

import os
import sys
import csv
import yaml
from pathlib import Path

# Paths
SITE_ROOT = Path(__file__).parent.parent
AWARDS_CSV = SITE_ROOT / "_data" / "cv_data" / "data" / "awards.csv"
OUTPUT_DIR = SITE_ROOT / "_data"


def load_publications():
    """Load existing publications data to build citation key lookup."""
    publications_file = OUTPUT_DIR / "publications.yml"
    
    if not publications_file.exists():
        print("⚠️  Publications file not found. Run generate_publications.py first.")
        return {}
    
    with open(publications_file, 'r') as f:
        publications_data = yaml.safe_load(f)
    
    # Build citation key lookup from publications
    citation_lookup = {}
    
    for year, categories in publications_data.items():
        for category, pubs in categories.items():
            for pub in pubs:
                # Extract citation key from PDF URL if available
                if pub.get('pdf_url'):
                    # Extract filename from URL (e.g., "gordonjenamaninanavati2024demo.pdf")
                    filename = pub['pdf_url'].split('/')[-1]
                    if filename.endswith('.pdf'):
                        citation_key = filename[:-4]  # Remove .pdf extension
                        citation_lookup[citation_key] = {
                            'title': pub['title'],
                            'year': pub['year'],
                            'venue': pub['venue'],
                            'pdf_url': pub['pdf_url']
                        }
    
    return citation_lookup


def generate_awards_yaml():
    """Generate awards.yml for Jekyll."""
    print("🏆 Generating awards data...")
    
    if not AWARDS_CSV.exists():
        print(f"❌ Awards CSV file not found: {AWARDS_CSV}")
        return []
    
    # Load publications for citation lookup
    citation_lookup = load_publications()
    
    awards_data = []
    
    with open(AWARDS_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            award = row['Award'].strip()
            year = row['Year'].strip()
            citation = row['Citation'].strip()
            
            # Skip empty rows
            if not award:
                continue
            
            award_entry = {
                'award': award,
                'year': year
            }
            
            # If we have a citation key, add publication link and title
            if citation and citation in citation_lookup:
                pub_info = citation_lookup[citation]
                award_entry['pub_link'] = f"/publications/#{citation}"
                award_entry['pub_title'] = pub_info['title'].replace('\n', ' ').strip()
            elif citation:
                # Citation key exists but publication not found
                print(f"⚠️  Citation key '{citation}' not found in publications")
                award_entry['pub_link'] = f"/publications/#{citation}"
            
            awards_data.append(award_entry)
    
    # Sort awards by year (newest first)
    awards_data.sort(key=lambda x: x['year'], reverse=True)
    
    # Write to Jekyll _data directory
    output_file = OUTPUT_DIR / "awards.yml"
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(awards_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=1000)
    
    print(f"✅ Generated: {output_file}")
    print(f"   Found {len(awards_data)} awards")
    
    # Show some stats
    with_citations = sum(1 for award in awards_data if award.get('citation'))
    print(f"   {with_citations} awards with citation links")
    
    return awards_data


def main():
    """Generate awards data file."""
    print("=" * 60)
    print("Awards Data Generator")
    print("=" * 60)
    
    print(f"\n📂 Site root: {SITE_ROOT}")
    print(f"📂 Awards CSV: {AWARDS_CSV}")
    
    # Generate awards data
    awards_data = generate_awards_yaml()
    
    print("\n" + "=" * 60)
    print("✨ Done! Awards data has been generated.")
    print("=" * 60)
    print(f"\nGenerated {len(awards_data)} awards in _data/awards.yml")
    print("\nNext steps:")
    print("1. Update cv.md to use dynamic awards data")
    print("2. Add anchors to publications page for linking")
    print("3. Test the integration")
    print("=" * 60)


if __name__ == "__main__":
    main()
