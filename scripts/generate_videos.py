#!/usr/bin/env python3
"""
Generate YouTube videos data for Jekyll site.

Fetches videos from:
1. Channel uploads (your own videos)
2. Favorites playlist (curated videos)

Merges, deduplicates, and sorts by publication date (newest first).

Usage:
    export YOUTUBE_API_KEY=your_key_here
    python3 scripts/generate_videos.py

Output:
    site/_data/videos.yml
"""

import os
import sys
import yaml
import requests
from pathlib import Path
from typing import List, Dict, Optional

# Configuration
SITE_ROOT = Path(__file__).parent.parent
CONFIG_FILE = SITE_ROOT / "site/_data/videos_config.yaml"
OUTPUT_FILE = SITE_ROOT / "site/_data/videos.yml"
YOUTUBE_API = "https://www.googleapis.com/youtube/v3"


def load_config() -> Dict:
    """Load and validate configuration."""
    if not CONFIG_FILE.exists():
        sys.exit(f"❌ Config not found: {CONFIG_FILE}")

    with open(CONFIG_FILE) as f:
        config = yaml.safe_load(f)

    # Get API key from environment
    api_key = os.getenv('YOUTUBE_API_KEY')
    if not api_key:
        sys.exit("❌ YOUTUBE_API_KEY environment variable not set")

    config['api_key'] = api_key

    # Validate required fields
    required = ['channel_id', 'favorites_playlist_id']
    missing = [f for f in required if f not in config]
    if missing:
        sys.exit(f"❌ Missing required fields in config: {missing}")

    return config


def fetch_playlist_videos(api_key: str, playlist_id: str, max_results: int = 50) -> List[Dict]:
    """Fetch videos from a YouTube playlist."""
    videos = []
    next_page = None

    while len(videos) < max_results:
        params = {
            'part': 'snippet',
            'playlistId': playlist_id,
            'maxResults': min(50, max_results - len(videos)),
            'key': api_key
        }
        if next_page:
            params['pageToken'] = next_page

        try:
            resp = requests.get(f"{YOUTUBE_API}/playlistItems", params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
        except requests.RequestException as e:
            print(f"⚠️  Error fetching playlist {playlist_id}: {e}", file=sys.stderr)
            break

        for item in data.get('items', []):
            snippet = item['snippet']
            video_id = snippet.get('resourceId', {}).get('videoId')
            title = snippet.get('title')

            # Skip private/deleted videos
            if not video_id or not title or title == 'Private video':
                continue

            # Get best available thumbnail
            thumbnails = snippet.get('thumbnails', {})
            thumbnail = (
                thumbnails.get('high', {}).get('url') or
                thumbnails.get('medium', {}).get('url') or
                thumbnails.get('default', {}).get('url') or
                f'https://i.ytimg.com/vi/{video_id}/hqdefault.jpg'
            )

            videos.append({
                'id': video_id,
                'title': title,
                'description': snippet.get('description', ''),
                'published_at': snippet.get('publishedAt'),
                'thumbnail_url': thumbnail,
                'channel_title': snippet.get('channelTitle', ''),
            })

        next_page = data.get('nextPageToken')
        if not next_page:
            break

    return videos[:max_results]


def fetch_video_details(api_key: str, video_ids: List[str]) -> Dict[str, Dict]:
    """Fetch original publication dates and details for videos (in batches of 50)."""
    details = {}

    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        params = {
            'part': 'snippet',
            'id': ','.join(batch),
            'key': api_key
        }

        try:
            resp = requests.get(f"{YOUTUBE_API}/videos", params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
        except requests.RequestException as e:
            print(f"⚠️  Error fetching video details: {e}", file=sys.stderr)
            continue

        for item in data.get('items', []):
            video_id = item['id']
            snippet = item['snippet']
            details[video_id] = {
                'published_at': snippet.get('publishedAt'),
                'channel_title': snippet.get('channelTitle', ''),
                'description': snippet.get('description', ''),
            }

    return details


def get_channel_uploads_playlist(api_key: str, channel_id: str) -> Optional[str]:
    """Get the uploads playlist ID for a channel."""
    params = {
        'part': 'contentDetails',
        'id': channel_id,
        'key': api_key
    }

    try:
        resp = requests.get(f"{YOUTUBE_API}/channels", params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        print(f"⚠️  Error fetching channel info: {e}", file=sys.stderr)
        return None

    items = data.get('items', [])
    if not items:
        print(f"⚠️  Channel not found: {channel_id}", file=sys.stderr)
        return None

    return items[0]['contentDetails']['relatedPlaylists']['uploads']


def main():
    """Generate videos.yml from YouTube data."""
    print("🎥 Fetching YouTube videos...")

    # Load config
    config = load_config()
    api_key = config['api_key']
    channel_id = config['channel_id']
    favorites_id = config['favorites_playlist_id']
    max_videos = config.get('max_videos', 100)

    all_videos = []

    # Fetch channel uploads
    print(f"📺 Fetching channel uploads...")
    uploads_id = get_channel_uploads_playlist(api_key, channel_id)
    if uploads_id:
        channel_videos = fetch_playlist_videos(api_key, uploads_id, max_videos // 2)
        all_videos.extend(channel_videos)
        print(f"   Found {len(channel_videos)} channel videos")

    # Fetch favorites (need original publication dates, not when added to favorites)
    print(f"⭐ Fetching favorites...")
    favorites = fetch_playlist_videos(api_key, favorites_id, max_videos // 2)

    # Get original publication dates for favorites
    if favorites:
        video_ids = [v['id'] for v in favorites]
        print(f"   Fetching original dates for {len(video_ids)} favorites...")
        details = fetch_video_details(api_key, video_ids)

        # Update favorites with original publication dates
        for video in favorites:
            if video['id'] in details:
                video.update(details[video['id']])

        all_videos.extend(favorites)
        print(f"   Found {len(favorites)} favorite videos")

    # Deduplicate by video ID
    seen = set()
    unique = []
    for video in all_videos:
        if video['id'] not in seen:
            seen.add(video['id'])
            unique.append(video)

    # Sort by publication date (newest first)
    unique.sort(key=lambda v: v.get('published_at', ''), reverse=True)

    # Limit to max
    unique = unique[:max_videos]

    # Write output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w') as f:
        yaml.dump(unique, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"✅ Wrote {len(unique)} videos to {OUTPUT_FILE.relative_to(SITE_ROOT)}")


if __name__ == "__main__":
    main()
