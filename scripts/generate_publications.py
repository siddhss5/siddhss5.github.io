#!/usr/bin/env python3
"""
Publications and Projects Generator for Jekyll Site

This script generates Jekyll-compatible YAML data files from BibTeX sources
for use with the Minimal Mistakes theme.

Usage:
    python3 scripts/generate_publications.py

Outputs:
    - _data/publications.yml
    - _data/projects.yml

Copyright (c) 2024 Personal Robotics Laboratory, University of Washington
MIT License
"""

import os
import sys
from pathlib import Path

# Add prl_bib2html to the path
prl_bib2html_path = Path(__file__).parent.parent / "prl_bib2html"
sys.path.insert(0, str(prl_bib2html_path))

from prl_bib2html import (
    LibraryConfig,
    list_publications,
    load_projects_config,
    list_publications_by_project,
    publications_to_dict,
    projects_to_dict,
    export_to_yaml
)

# Paths
SITE_ROOT = Path(__file__).parent.parent
CONFIG_FILE = SITE_ROOT / "_data" / "publications_config.yaml"
OUTPUT_DIR = SITE_ROOT / "_data"


def generate_publications_yaml():
    """Generate publications.yml for Jekyll."""
    print("📚 Generating publications data...")
    
    # Load configuration
    lib_config = LibraryConfig.from_yaml(str(CONFIG_FILE))
    config = lib_config.to_publications_config()
    
    # Get publications organized by year and category
    pubs = list_publications(config)
    
    # Convert to dict using library function
    yaml_data = publications_to_dict(pubs)
    
    # Write to Jekyll _data directory
    output_file = OUTPUT_DIR / "publications.yml"
    export_to_yaml(yaml_data, str(output_file))
    
    total_pubs = sum(len(pubs) for year in yaml_data.values() for pubs in year.values())
    print(f"✅ Generated: {output_file}")
    print(f"   Found {total_pubs} publications across {len(yaml_data)} years")
    
    return yaml_data


def generate_projects_yaml():
    """Generate projects.yml for Jekyll."""
    print("\n📁 Generating projects data...")
    
    # Load configuration
    lib_config = LibraryConfig.from_yaml(str(CONFIG_FILE))
    config = lib_config.to_publications_config()
    
    # Load projects configuration
    projects_config = load_projects_config(config.projects_yaml_path) if config.projects_yaml_path else {}
    
    if not projects_config:
        print("⚠️  No projects configured in projects-config.yaml")
        print("   Skipping projects.yml generation")
        return {}
    
    # Get publications grouped by project
    project_pubs = list_publications_by_project(config, projects_config)
    
    # Sort projects (active first, then by newest pub, then alphabetical)
    def project_sort_key(item):
        project_name, project_info = item
        status = project_info.get('status', '').lower()
        status_priority = {'active': 0, 'archived': 1}.get(status, 2)
        
        newest_year = 0
        if project_name in project_pubs and project_pubs[project_name]:
            newest_year = max(pub.year for pub in project_pubs[project_name])
        
        return (status_priority, -newest_year, project_name)
    
    sorted_projects = dict(sorted(projects_config.items(), key=project_sort_key))
    
    # Create simplified structure with only publications
    yaml_data = {}
    for project_name, project_info in sorted_projects.items():
        publications = []
        if project_name in project_pubs and project_pubs[project_name]:
            # Convert publications to dict format
            for pub in project_pubs[project_name]:
                pub_dict = {
                    'title': pub.title,
                    'authors': pub.authors,
                    'venue': pub.venue,
                    'year': pub.year,
                    'pdf_url': pub.pdf_url,
                    'note': pub.note,
                    'projects': pub.projects,
                    'entry_type': pub.entry_type
                }
                publications.append(pub_dict)
        
        yaml_data[project_name] = {
            'publications': publications
        }
    
    # Write to Jekyll _data directory
    output_file = OUTPUT_DIR / "projects.yml"
    export_to_yaml(yaml_data, str(output_file))
    
    total_project_pubs = sum(len(p['publications']) for p in yaml_data.values())
    print(f"✅ Generated: {output_file}")
    print(f"   Found {len(yaml_data)} projects with {total_project_pubs} publications")
    
    return yaml_data


def main():
    """Generate all Jekyll data files."""
    print("=" * 60)
    print("Publications & Projects Generator")
    print("=" * 60)
    
    # Check if config file exists
    if not CONFIG_FILE.exists():
        print(f"❌ Configuration file not found: {CONFIG_FILE}")
        print(f"   Please create it before running this script")
        sys.exit(1)
    
    print(f"\n📂 Site root: {SITE_ROOT}")
    print(f"📂 Config file: {CONFIG_FILE}")
    
    # Generate data files
    generate_publications_yaml()
    generate_projects_yaml()
    
    print("\n" + "=" * 60)
    print("✨ Done! Your Jekyll site data has been updated.")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review generated files:")
    print(f"   {OUTPUT_DIR}/publications.yml")
    print(f"   {OUTPUT_DIR}/projects.yml")
    print("\n2. Test locally:")
    print("   bundle exec jekyll serve")
    print("\n3. Commit and push to deploy:")
    print("   git add _data/")
    print("   git commit -m 'Update publications and projects'")
    print("   git push")
    print("=" * 60)


if __name__ == "__main__":
    main()

