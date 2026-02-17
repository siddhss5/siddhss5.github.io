#!/usr/bin/env python3
"""Sync site/_config.yml and data files from source (single source of truth)."""

import yaml
import shutil
from pathlib import Path

ROOT = Path(__file__).parent.parent
LAB_CONFIG = ROOT / "lab.yaml"
JEKYLL_CONFIG = ROOT / "site/_config.yml"
DATA_DIR = ROOT / "data"
SITE_DATA_DIR = ROOT / "site/_data"


def sync_config():
    """Update _config.yml author section from lab.yaml."""

    # Load lab.yaml
    with open(LAB_CONFIG) as f:
        lab_data = yaml.safe_load(f)

    lab = lab_data['lab']

    # Load _config.yml
    with open(JEKYLL_CONFIG) as f:
        config = yaml.safe_load(f)

    # Update from lab.yaml
    config['title'] = lab['name']
    config['email'] = lab.get('email', '')
    config['description'] = lab['description']

    # Update author section
    if 'author' not in config:
        config['author'] = {}

    config['author']['name'] = lab['name']
    config['author']['bio'] = lab['description']

    # Update author links
    config['author']['links'] = [
        {
            'label': 'Lab Website',
            'icon': 'fa fa-users',
            'url': lab.get('lab_website', '')
        },
        {
            'label': 'Google Scholar',
            'icon': 'fas fa-graduation-cap',
            'url': lab.get('google_scholar', '')
        },
        {
            'label': 'Twitter',
            'icon': 'fab fa-fw fa-twitter-square',
            'url': lab.get('twitter', '')
        },
        {
            'label': 'GitHub',
            'icon': 'fab fa-fw fa-github',
            'url': lab.get('github', '')
        },
        {
            'label': 'Contact',
            'icon': 'far fa-envelope',
            'url': '/contact/'
        }
    ]

    # Write updated config
    with open(JEKYLL_CONFIG, 'w') as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"✅ Synced {JEKYLL_CONFIG.name} from {LAB_CONFIG.name}")


def sync_data_files():
    """Copy static data files from data/ to site/_data/ for Jekyll."""

    files_to_sync = ['awards.yaml', 'press.yaml']

    for filename in files_to_sync:
        src = DATA_DIR / filename
        # Keep .yaml extension in source, but Jekyll expects .yml
        dest_name = filename.replace('.yaml', '.yml')
        dest = SITE_DATA_DIR / dest_name

        if src.exists():
            shutil.copy2(src, dest)
            print(f"✅ Copied {filename} → site/_data/{dest_name}")
        else:
            print(f"⚠️  Warning: {src} not found")


if __name__ == "__main__":
    sync_config()
    sync_data_files()
