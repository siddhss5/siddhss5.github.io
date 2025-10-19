#!/usr/bin/env python3
"""
Generate mentoring data from CV CSV files for Jekyll.
Organizes students and postdocs by current/alumni status and degree level.
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

def is_current(start_year, finish_year):
    """Determine if someone is currently active based on start/finish years."""
    # If there's a finish year, they've graduated and are alumni
    if finish_year and finish_year.strip() != "":
        return False
    
    # If no finish year, they're still active
    return True

def categorize_students(students, start_key, finish_key):
    """Categorize students into current and alumni."""
    current = []
    alumni = []
    
    for student in students:
        if is_current(student.get(start_key, ""), student.get(finish_key, "")):
            current.append(student)
        else:
            alumni.append(student)
    
    return current, alumni

def generate_mentoring_yaml():
    """Generate mentoring.yml for Jekyll."""
    print("=" * 60)
    print("Mentoring Data Generator")
    print("=" * 60)
    
    print(f"📂 Site root: {SITE_ROOT}")
    print(f"📂 CV data directory: {CV_DATA_DIR}")
    
    # Load all the data
    print("\n📚 Loading student and postdoc data...")
    
    postdocs = load_csv_data("postdocs.csv")
    phd_students = load_csv_data("students-phd.csv")
    ms_students = load_csv_data("students-ms.csv")
    
    print(f"   Found {len(postdocs)} postdocs")
    print(f"   Found {len(phd_students)} PhD students")
    print(f"   Found {len(ms_students)} MS students")
    
    # Categorize by current/alumni status
    current_postdocs, alumni_postdocs = categorize_students(postdocs, "Start", "Finish")
    current_phd, alumni_phd = categorize_students(phd_students, "Start", "Finish")
    current_ms, alumni_ms = categorize_students(ms_students, "Start", "Finish")
    
    print(f"\n📊 Current vs Alumni breakdown:")
    print(f"   Current postdocs: {len(current_postdocs)}")
    print(f"   Alumni postdocs: {len(alumni_postdocs)}")
    print(f"   Current PhD students: {len(current_phd)}")
    print(f"   Alumni PhD students: {len(alumni_phd)}")
    print(f"   Current MS students: {len(current_ms)}")
    print(f"   Alumni MS students: {len(alumni_ms)}")
    
    # Organize the data
    mentoring_data = {
        "current": {
            "postdocs": current_postdocs,
            "phd_students": current_phd,
            "ms_students": current_ms
        },
        "alumni": {
            "postdocs": alumni_postdocs,
            "phd_students": alumni_phd,
            "ms_students": alumni_ms
        }
    }
    
    # Write to YAML file
    output_file = OUTPUT_DIR / "mentoring.yml"
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(mentoring_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=1000)
    
    print(f"\n✅ Generated: {output_file}")
    
    # Show some stats
    total_current = len(current_postdocs) + len(current_phd) + len(current_ms)
    total_alumni = len(alumni_postdocs) + len(alumni_phd) + len(alumni_ms)
    print(f"   Total current: {total_current}")
    print(f"   Total alumni: {total_alumni}")
    print(f"   Grand total: {total_current + total_alumni}")
    
    print("\n" + "=" * 60)
    print("✨ Done! Mentoring data has been generated.")
    print("=" * 60)
    print(f"\nGenerated mentoring data in {output_file}")
    print("\nNext steps:")
    print("1. Create mentoring.md page to display the data")
    print("2. Add navigation link to mentoring page")
    print("3. Test the integration")
    print("=" * 60)
    
    return mentoring_data

if __name__ == "__main__":
    generate_mentoring_yaml()
