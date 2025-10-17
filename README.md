# Siddhartha Srinivasa - Personal Website

Personal website built with Jekyll and the [Minimal Mistakes theme](https://github.com/mmistakes/minimal-mistakes).

## Features

- **Publications**: Automatically generated from BibTeX files using [prl_bib2html](https://github.com/siddhss5/prl_bib2html) (integrated as Git submodule)
- **Projects**: Research projects with associated publications (collapsible view)
- **Videos**: YouTube videos from channel and favorites with embedded players and modal popups
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

## Updating Publications, Projects & Videos

### Automatic Generation

Publications, projects, and videos data are **automatically generated** before every Jekyll build via dedicated plugins. This means:

- When you run `bundle exec jekyll serve`, all data is regenerated automatically
- No manual step needed for local development
- All content is always fresh when viewing the site

### Manual Generation (Optional)

You can also manually regenerate publications, projects, and videos data:

```bash
# Generate publications and projects (using prl_bib2html)
python3 scripts/generate_publications.py

# Generate videos
python3 scripts/generate_videos.py
```

This will:
- **Publications**: Use [prl_bib2html](https://github.com/siddhss5/prl_bib2html) to process BibTeX files from the Git submodule at `_data/pubs/` (from [personalrobotics/pubs](https://github.com/personalrobotics/pubs))
- **Projects**: Generate `_data/projects.yml` with project-organized publications using prl_bib2html's advanced features
- **Videos**: Fetch videos from YouTube channel and favorites playlist, generate `_data/videos.yml`

The Jekyll server will automatically pick up the changes if it's running.

### Updating BibTeX Files

The BibTeX files are managed as a Git submodule. To get the latest publications:

```bash
# Update the submodule to latest commits
git submodule update --remote _data/pubs

# Regenerate the data
python3 scripts/generate_publications.py

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
   python3 scripts/generate_publications.py
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

This site uses [prl_bib2html](https://github.com/siddhss5/prl_bib2html/) as a Git submodule for advanced publication processing. The library provides:

- **Advanced BibTeX Processing**: Rich academic metadata formatting
- **LaTeX Support**: Automatic conversion of LaTeX formatting to HTML
- **Author Formatting**: Intelligent author name formatting and abbreviation
- **Project Organization**: Group publications by research projects
- **Framework Agnostic**: Clean separation between data processing and presentation

### Submodule Management

The prl_bib2html library is integrated as a Git submodule:

```bash
# Update to latest version of prl_bib2html
git submodule update --remote prl_bib2html

# Initialize submodule (for new clones)
git submodule update --init --recursive
```

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
   python3 scripts/generate_videos.py
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
│   ├── videos_config.yaml      # YouTube videos configuration
│   ├── publications.yml        # Generated publications data
│   ├── projects.yml            # Generated projects data
│   ├── videos.yml              # Generated videos data
│   └── pubs/                   # Git submodule with BibTeX files
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
├── prl_bib2html/               # Git submodule - prl_bib2html library
│   ├── prl_bib2html/           # Core library code
│   ├── demos/                  # Example applications
│   └── ...
├── scripts/
│   ├── generate_publications.py # Publication generator script (uses prl_bib2html)
│   └── generate_videos.py      # YouTube videos generator script
└── .gitmodules                 # Git submodule configuration
```

---

## Credits

- Theme: [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) by Michael Rose
- Publications Generator: [prl_bib2html](https://github.com/siddhss5/prl_bib2html) (integrated as Git submodule)
- YouTube Integration: Custom Python scripts with YouTube Data API v3
