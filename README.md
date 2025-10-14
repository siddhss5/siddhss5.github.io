# Siddhartha Srinivasa - Personal Website

Personal website built with Jekyll and the [Minimal Mistakes theme](https://github.com/mmistakes/minimal-mistakes).

## Features

- **Publications**: Automatically generated from BibTeX files using [prl_bib2html](https://github.com/siddhss5/prl_bib2html)
- **Projects**: Research projects with associated publications (collapsible view)
- **Blog Posts**: Technical blog posts and thoughts
- **CV, Teaching, Contact**: Standard academic pages

---

## Running Locally

### Prerequisites

You need Ruby 3.4+ installed via Homebrew (macOS):

```bash
brew install ruby
```

Add to your `~/.zshrc`:
```bash
# Ruby (Homebrew)
export PATH="/opt/homebrew/opt/ruby/bin:/opt/homebrew/lib/ruby/gems/3.4.0/bin:$PATH"
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

Then reload your shell or run `source ~/.zshrc`.

### Setup

1. **Install dependencies:**
   ```bash
   cd /Users/siddh/code/siddhss5.github.io
   bundle install
   ```

2. **Start the Jekyll server:**
   ```bash
   bundle exec jekyll serve
   ```

3. **View the site:**
   Open your browser to: http://localhost:4000

The server will automatically rebuild when you make changes to files (except `_config.yml`, which requires a restart).

---

## Updating Publications & Projects

### Quick Update

To fetch the latest publications from BibTeX files and regenerate the data:

```bash
python3 scripts/generate_publications.py
```

This will:
- Fetch BibTeX files from the [personalrobotics/pubs](https://github.com/personalrobotics/pubs) repo
- Cache them locally in `_data/bib/`
- Generate `_data/publications.yml` with all publications
- Generate `_data/projects.yml` with project-organized publications

The Jekyll server will automatically pick up the changes if it's running.

### Adding a New Project

1. **Edit `_data/projects-config.yaml`** and add your project:
   ```yaml
   myproject:
     title: "My Research Project"
     description: "Brief description of the project"
     website: "https://project-website.com"
     status: "active"  # or "archived"
   ```

2. **Tag publications in your BibTeX files** with the project name:
   ```bibtex
   @inproceedings{smith2024,
     title = {My Paper},
     author = {Smith, J.},
     year = {2024},
     project = {myproject}  # Add this field
   }
   ```

3. **Regenerate the data:**
   ```bash
   python3 scripts/generate_publications.py
   ```

### Configuration

Edit `_data/publications_config.yaml` to configure:
- BibTeX source URL
- Which BibTeX files to include
- PDF base URL
- Projects configuration file location

---

## Deployment

After making changes:

```bash
git add .
git commit -m "Update site"
git push origin minimal-mistakes
```

GitHub Pages will automatically rebuild and deploy your site to https://siddhss5.github.io

---

## Project Structure

```
├── _config.yml                  # Jekyll configuration
├── _data/
│   ├── navigation.yml          # Site navigation menu
│   ├── publications_config.yaml # Publications generation config
│   ├── projects-config.yaml    # Project definitions
│   ├── publications.yml        # Generated publications data
│   └── projects.yml            # Generated projects data
├── _pages/
│   ├── publications.md         # Publications page template
│   ├── projects.md             # Projects page template
│   ├── cv.md
│   ├── teaching.md
│   └── contact.md
├── _posts/                     # Blog posts
├── assets/                     # Images, PDFs, etc.
└── scripts/
    └── generate_publications.py # Publication generator script
```

---

## Credits

- Theme: [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) by Michael Rose
- Publications Generator: [prl_bib2html](https://github.com/siddhss5/prl_bib2html)
