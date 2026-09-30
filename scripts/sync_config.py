#!/usr/bin/env python3
"""Sync site/_config.yml and data files from source (single source of truth)."""

import re
import shutil

import yaml
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


def assemble_awards():
    """Build site/_data/awards.yml from the two places an award can come from.

    A paper's awards live in its BibTeX `award` field and reach us through
    sslabdata, in site/_data/lab.yml. An award a person holds - a fellowship, a
    chair - is not a property of any paper and lives in data/awards.yaml. The
    site shows one table, so they are merged here, newest first, with the
    conference taken from the work's own venue rather than repeated in the
    award's name.
    """

    honours_file = DATA_DIR / "awards.yaml"
    lab_file = SITE_DATA_DIR / "lab.yml"

    if not lab_file.exists():
        raise SystemExit(
            f"{lab_file} is missing: run sslabdata before this script "
            "(paper awards are read from it)"
        )

    with open(honours_file) as f:
        honours = yaml.safe_load(f) or []
    with open(lab_file) as f:
        lab = yaml.safe_load(f)

    rows = []
    for honour in honours:
        if honour.get("pub_link"):
            raise SystemExit(
                f"{honours_file}: '{honour['award']}' has a pub_link, so it is a "
                "paper award - put it in that entry's BibTeX award field instead"
            )
        rows.append({
            "year": str(honour["year"]),
            "award": honour["award"],
            "conference": "",
            "pub_title": "",
            "pub_link": "",
        })

    paper_awards = 0
    for work in lab["works"]:
        for award in work.get("awards") or []:
            rows.append({
                "year": str(award["year"]) if award["year"] else "",
                "award": award["name"],
                "conference": (work.get("venue") or {}).get("name") or "",
                "pub_title": work["title"],
                "pub_link": f"/publications/#{work['bib_id']}",
            })
            paper_awards += 1

    def newest_first(row):
        match = re.match(r"(\d{4})", row["year"])
        return int(match.group(1)) if match else 0

    rows.sort(key=newest_first, reverse=True)

    dest = SITE_DATA_DIR / "awards.yml"
    with open(dest, "w") as f:
        yaml.dump(rows, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"✅ Assembled site/_data/awards.yml: {len(honours)} honours + "
          f"{paper_awards} paper awards")


def sync_data_files():
    """Copy static data files from data/ to site/_data/ for Jekyll."""

    files_to_sync = ['press.yaml']

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
    assemble_awards()
