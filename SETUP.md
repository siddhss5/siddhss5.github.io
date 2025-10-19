# Setup Instructions

This Jekyll site uses automated GitHub Actions to build and deploy, with secure API key handling.

## Local Development

### 1. Install Dependencies

```bash
# Ruby dependencies
bundle install

# Python dependencies (includes prl_bib2html from git)
# Option 1: Using uv (recommended - faster)
uv pip install -r requirements.txt

# Option 2: Using pip
pip install -r requirements.txt
```

### 2. Configure API Keys

**For YouTube Videos:**

1. Copy the template:
   ```bash
   cp _data/videos_config.yaml.template _data/videos_config.yaml
   ```

2. Get a YouTube Data API v3 key from [Google Cloud Console](https://console.developers.google.com/)

3. Set your API key as an environment variable:
   ```bash
   export YOUTUBE_API_KEY="your_api_key_here"
   ```

   Or add it to your shell profile (`.bashrc`, `.zshrc`, etc.):
   ```bash
   echo 'export YOUTUBE_API_KEY="your_api_key_here"' >> ~/.zshrc
   ```

### 3. Generate Site Data

```bash
# Generate publications and projects
uv run python scripts/generate_publications.py

# Generate videos (requires API key)
uv run python scripts/generate_videos.py
```

### 4. Run Jekyll Locally

```bash
bundle exec jekyll serve
```

## GitHub Actions Deployment

### 1. Set Repository Secrets

Go to your GitHub repository → Settings → Secrets and variables → Actions, and add:

- `YOUTUBE_API_KEY`: Your YouTube Data API v3 key

### 2. Enable GitHub Pages

1. Go to repository Settings → Pages
2. Set Source to "GitHub Actions"
3. The workflow will automatically build and deploy on pushes to `main` or `minimal-mistakes` branches

## Security Notes

- API keys are never committed to the repository
- The `_data/videos_config.yaml` file is gitignored to prevent accidental commits
- GitHub Actions uses repository secrets for secure API key access
- The site will build successfully even without API keys (videos will be skipped)

## Troubleshooting

### Videos not showing up?

1. Check that `YOUTUBE_API_KEY` is set in your environment
2. Verify the API key has YouTube Data API v3 enabled
3. Check the channel ID and playlist ID in the config file
4. Run the script manually to see error messages:
   ```bash
   python scripts/generate_videos.py
   ```

### GitHub Actions failing?

1. Check that the `YOUTUBE_API_KEY` secret is set in repository settings
2. Look at the Actions tab for detailed error logs
3. The workflow will continue even if videos generation fails

## CV Data Integration

This Jekyll site integrates with the [sidd-cv repository](https://github.com/siddhss5/sidd-cv) as a git submodule to maintain a single source of truth for CV data.

### Git Submodule Setup

The sidd-cv repository is included as a submodule in `_data/cv_data/`. To initialize it:

```bash
# Initialize and update submodule (run once)
git submodule update --init --recursive

# Update submodule to latest version
git submodule update --remote _data/cv_data
```

### Data Synchronization

CSV files from the sidd-cv repository are automatically processed by Jekyll:

- **Awards**: `_data/awards.csv` → `_data/awards.yml` (with publication links)
- **Publications**: Linked to awards via citation keys
- **Automatic Updates**: Jekyll plugins regenerate data on every build

### Updating CV Data

1. **Update submodule to latest**:
   ```bash
   git submodule update --remote _cv_data
   ```

2. **Move updated CSV files to _data**:
   ```bash
   mv _cv_data/data/*.csv _data/
   ```

3. **Regenerate site data**:
   ```bash
   bundle exec jekyll serve
   ```

The Jekyll plugins will automatically:
- Generate `_data/awards.yml` from `_data/awards.csv`
- Link awards to publications using citation keys
- Add anchor IDs to publications for direct linking
