# Siddhartha Srinivasa - Personal Website

Personal website built with Jekyll and the [Minimal Mistakes theme](https://github.com/mmistakes/minimal-mistakes).

## Features

- **Publications**: Automatically generated from BibTeX files using [prl_bib2html](https://github.com/siddhss5/prl_bib2html) (installed from git)
- **Projects**: Research projects with associated publications (collapsible view)
- **Awards**: Dynamic awards data with automatic publication linking from CSV sources
- **Videos**: YouTube videos from channel and favorites with embedded players and modal popups
- **Blog Posts**: Technical blog posts and thoughts
- **CV, Teaching, Contact**: Standard academic pages with integrated CV data

---

## Running Locally

### Prerequisites

You need Ruby 3.4+ and Python 3.8+ installed:

**Ruby (macOS with Homebrew):**
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

**Python (recommended with uv):**
```bash
# Install uv (fast Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with pip
pip install uv
```

Then reload your shell or run `source ~/.zshrc`.

### Setup

1. **Install dependencies:**
   ```bash
   cd /Users/siddh/code/siddhss5.github.io
   
   # Ruby dependencies
   bundle install
   
   # Python dependencies (includes prl_bib2html from git)
   uv pip install -r requirements.txt
   ```

2. **Start the Jekyll server:**
   ```bash
   bundle exec jekyll serve
   ```

3. **View the site:**
   Open your browser to: http://localhost:4000

The server will automatically rebuild when you make changes to files (except `_config.yml`, which requires a restart).

---

## Updating Publications, Projects, Awards & Videos

### Automatic Generation

Publications, projects, awards, and videos data are **automatically generated** before every Jekyll build via dedicated plugins. This means:

- When you run `bundle exec jekyll serve`, all data is regenerated automatically
- No manual step needed for local development
- All content is always fresh when viewing the site

### Manual Generation (Optional)

You can also manually regenerate publications, projects, awards, and videos data:

```bash
# Update CV from submodule to assets
uv run python scripts/update_cv.py

# Generate publications and projects (using prl_bib2html)
uv run python scripts/generate_publications.py

# Generate awards (from CV CSV data)
uv run python scripts/generate_awards.py

# Generate videos
uv run python scripts/generate_videos.py
```

This will:
- **CV**: Copy latest CV PDF from `_data/cv_data/sidd-cv.pdf` to `assets/SiddharthaSrinivasaCV.pdf`
- **Publications**: Use [prl_bib2html](https://github.com/siddhss5/prl_bib2html) to process BibTeX files from `_data/pubs/` (from [personalrobotics/pubs](https://github.com/personalrobotics/pubs))
- **Projects**: Generate `_data/projects.yml` with project-organized publications using prl_bib2html's advanced features
- **Awards**: Process CSV data from `_data/cv_data/data/awards.csv` and generate `_data/awards.yml` with publication links
- **Videos**: Fetch videos from YouTube channel and favorites playlist, generate `_data/videos.yml`

The Jekyll server will automatically pick up the changes if it's running.

### Updating BibTeX Files

The BibTeX files are managed as a Git submodule. To get the latest publications:

```bash
# Update the submodule to latest commits
git submodule update --remote _data/pubs

# Regenerate the data
uv run python scripts/generate_publications.py

# Commit the submodule update
git add _data/pubs
git commit -m "Update publications submodule"
```

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
   uv run python scripts/generate_publications.py
   ```

### Configuration

Edit `_data/publications_config.yaml` to configure:
- BibTeX directory (currently `_data/pubs/` from Git submodule)
- Which BibTeX files to include
- PDF base URL
- Projects configuration file location

---

## prl_bib2html Integration

### Overview

This site uses [prl_bib2html](https://github.com/siddhss5/prl_bib2html/) installed from git for advanced publication processing. The library provides:

- **Advanced BibTeX Processing**: Rich academic metadata formatting
- **LaTeX Support**: Automatic conversion of LaTeX formatting to HTML
- **Author Formatting**: Intelligent author name formatting and abbreviation
- **Project Organization**: Group publications by research projects
- **Framework Agnostic**: Clean separation between data processing and presentation

### Installation

The prl_bib2html library is automatically installed from git when you run:

```bash
# Install all dependencies (including prl_bib2html from git)
uv pip install -r requirements.txt
```

This installs the latest version directly from the git repository, ensuring you always have the most up-to-date features.

### Configuration

The publications generation uses the library's advanced configuration system via `_data/publications_config.yaml`. This provides:

- **BibTeX File Management**: Automatic processing of multiple BibTeX files
- **Project Metadata**: YAML-based project configuration
- **Output Formatting**: Customizable publication display options
- **PDF Integration**: Support for both local and remote PDF links

### Advanced Features

- **LaTeX Conversion**: Mathematical expressions, accents, and formatting
- **Smart Author Handling**: Proper author name formatting and affiliations
- **Year Grouping**: Automatic organization by publication year and type
- **URL Support**: Publication URLs, video links, and external resources
- **Project Tags**: BibTeX-based project association with YAML metadata

---

## YouTube Videos Integration

### Setup

The videos page automatically fetches videos from your YouTube channel and favorites playlist. To set this up:

1. **Get a YouTube Data API v3 key:**
   - Go to [Google Developer Console](https://console.developers.google.com/)
   - Create a new project or select existing one
   - Enable the YouTube Data API v3
   - Create credentials (API key)

2. **Configure the videos:**
   Edit `_data/videos_config.yaml`:
   ```yaml
   api_key: "YOUR_YOUTUBE_API_KEY_HERE"
   channel_id: "UCv0BqZMqV5xNa5JOkibxOpw"  # Your channel ID
   favorites_playlist_id: "FLv0BqZMqV5xNa5JOkibxOpw"  # Your favorites playlist
   max_videos: 100
   ```

3. **Test the integration:**
   ```bash
   uv run python scripts/generate_videos.py
   ```

### Features

- **Automatic fetching**: Videos are fetched from your YouTube channel and favorites playlist
- **Chronological sorting**: Videos are sorted by upload date (newest first)
- **Private video filtering**: Private videos are automatically excluded
- **Responsive grid**: Clean thumbnail grid layout with hover effects
- **Modal popups**: Click any video to open a modal with embedded YouTube player
- **Robust thumbnails**: Fallback system ensures all videos have thumbnails

### Video Data Structure

The script generates `_data/videos.yml` with:
- Video ID, title, description, upload date
- Thumbnail URLs with fallback system
- Channel information
- Automatic deduplication and sorting

---

## CV Data Integration

### Overview

This site integrates with the [sidd-cv repository](https://github.com/siddhss5/sidd-cv) as a git submodule to maintain a single source of truth for CV data. Awards are automatically generated from CSV files and linked to publications.

### Features

- **Single Source of Truth**: CV data managed in dedicated [sidd-cv repository](https://github.com/siddhss5/sidd-cv)
- **Automatic Awards Generation**: Awards data automatically generated from CSV files
- **Publication Linking**: Awards automatically linked to publications via citation keys
- **Dynamic CV Page**: CV page displays awards in table format with publication links
- **Git Submodule Integration**: CV data stays in sync via git submodule
- **Automatic Updates**: Website automatically updates when CV or Publications change
- **Dynamic CV File**: Latest CV PDF automatically copied from submodule to assets

### Setup

The CV data is automatically integrated via git submodule:

```bash
# Initialize submodule (run once)
git submodule update --init --recursive

# Update CV data to latest version
git submodule update --remote _data/cv_data
```

### Data Structure

The integration processes CSV files from `_data/cv_data/data/`:
- **awards.csv**: Award data with citation keys for publication linking
- **grants.csv**: Research grants and funding information
- **students-*.csv**: Student information (PhD, MS, postdocs, interns)
- **press.csv**: Press coverage and media mentions

### Automatic Generation

Awards data is automatically generated on every Jekyll build:
- **CSV Processing**: Awards data read from `_data/cv_data/data/awards.csv`
- **Publication Linking**: Citation keys matched to publications for automatic linking
- **YAML Generation**: Clean awards data generated in `_data/awards.yml`
- **Dynamic Display**: CV page automatically displays awards with publication links

### Manual Updates

To update CV data:

```bash
# Update submodule to latest
git submodule update --remote _data/cv_data

# Regenerate awards data
uv run python scripts/generate_awards.py

# Commit changes
git add _data/awards.yml
git commit -m "Update awards data"
```

### Configuration

The awards generator uses:
- **Input**: `_data/cv_data/data/awards.csv` (from git submodule)
- **Publications**: `_data/publications.yml` (for citation key lookup)
- **Output**: `_data/awards.yml` (clean awards data with publication links)

### Automatic Updates

The website automatically stays in sync with your data repositories:

#### **Scheduled Updates**
- **Frequency**: Every 6 hours via GitHub Actions
- **Monitors**: Both CV (`sidd-cv`) and Publications (`personalrobotics/pubs`) repositories
- **Automatic**: No manual intervention required
- **Smart**: Only rebuilds when changes are detected

#### **Update Process**
1. **Check for changes** in both submodules
2. **Update submodules** to latest commits
3. **Commit changes** with descriptive messages
4. **Trigger rebuild** of the website
5. **Deploy updated site** with latest data

#### **Manual Trigger**
You can manually trigger updates:
1. Go to **Actions** tab in your repository
2. Click **"Check for CV and Publications updates"** workflow
3. Click **"Run workflow"** button

#### **Local Development**
When running locally (`bundle exec jekyll serve`):
- ✅ Automatically updates CV from submodule
- ✅ Updates all submodules to latest
- ✅ Regenerates all data (publications, awards, etc.)
- ✅ Always shows latest content

---

## Automated Build & Deployment

This site uses **GitHub Actions** for automated builds and deployment:

### Features
- **Automatic builds** on every push to `main` or `minimal-mistakes` branches
- **Secure API key handling** using GitHub repository secrets
- **Fast dependency installation** with `uv` (10-100x faster than pip)
- **Automatic GitHub Pages deployment**

### Setup for Automated Builds

1. **Set up GitHub repository secrets:**
   - Go to your repository → Settings → Secrets and variables → Actions
   - Add `YOUTUBE_API_KEY` with your YouTube Data API v3 key

2. **Push changes:**
   ```bash
   git add .
   git commit -m "Update site"
   git push origin minimal-mistakes
   ```

3. **Monitor the build:**
   - Go to the "Actions" tab in your GitHub repository
   - Watch the automated build and deployment process

The site will be automatically deployed to https://siddhss5.github.io

### Manual Deployment

You can also build and deploy manually:

```bash
# Generate all data
uv run python scripts/update_cv.py
uv run python scripts/generate_publications.py
uv run python scripts/generate_awards.py
uv run python scripts/generate_videos.py

# Build the site
bundle exec jekyll build

# Deploy (if using manual deployment)
git add _data/ assets/
git commit -m "Update site data"
git push origin minimal-mistakes
```

---

## Project Structure

```
├── _config.yml                  # Jekyll configuration
├── _data/
│   ├── navigation.yml          # Site navigation menu
│   ├── publications_config.yaml # Publications generation config
│   ├── projects-config.yaml    # Project definitions
│   ├── videos_config.yaml      # YouTube videos configuration
│   ├── publications.yml        # Generated publications data
│   ├── projects.yml            # Generated projects data
│   ├── videos.yml              # Generated videos data
│   ├── awards.yml              # Generated awards data
│   ├── pubs/                   # Git submodule with BibTeX files
│   └── cv_data/                # Git submodule with CV CSV data
├── _pages/
│   ├── publications.md         # Publications page template
│   ├── projects.md             # Projects page template
│   ├── videos.md               # Videos page template
│   ├── cv.md
│   ├── teaching.md
│   └── contact.md
├── _posts/                     # Blog posts
├── _plugins/
│   ├── generate_publications.rb # Auto-generates publications and projects data
│   └── generate_videos.rb       # Auto-generates videos data
├── assets/                     # Images, PDFs, etc.
├── scripts/
│   ├── generate_publications.py # Publication generator script (uses prl_bib2html)
│   ├── generate_awards.py      # Awards generator script (processes CV CSV data)
│   ├── update_cv.py            # CV update script (copies latest CV from submodule)
│   └── generate_videos.py      # YouTube videos generator script
├── requirements.txt            # Python dependencies (includes prl_bib2html from git)
├── .github/workflows/          # GitHub Actions for automated builds
│   ├── build.yml              # Build and deploy workflow
│   └── check-cv-updates.yml   # Automatic CV and Publications update workflow
└── .gitmodules                 # Git submodule configuration (pubs and cv_data)
```

---

## Credits

- Theme: [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) by Michael Rose
- Publications Generator: [prl_bib2html](https://github.com/siddhss5/prl_bib2html) (installed from git)
- YouTube Integration: Custom Python scripts with YouTube Data API v3
