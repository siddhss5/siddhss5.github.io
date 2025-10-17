#!/usr/bin/env python3
"""
YouTube Videos Generator for Jekyll Site

This script fetches videos from YouTube channel and favorites playlist
and generates Jekyll-compatible YAML data files.

Usage:
    python3 scripts/generate_videos.py

Outputs:
    - _data/videos.yml

Copyright (c) 2024 Personal Robotics Laboratory, University of Washington
MIT License
"""

import os
import sys
import yaml
import requests
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

# Paths
SITE_ROOT = Path(__file__).parent.parent
CONFIG_FILE = SITE_ROOT / "_data" / "videos_config.yaml"
OUTPUT_DIR = SITE_ROOT / "_data"

# YouTube Data API v3 endpoints
YOUTUBE_API_BASE = "https://www.googleapis.com/youtube/v3"


def substitute_env_vars(text: str) -> str:
    """Substitute environment variables in text like ${VAR_NAME}."""
    def replace_var(match):
        var_name = match.group(1)
        return os.getenv(var_name, match.group(0))  # Return original if env var not found
    
    return re.sub(r'\$\{([^}]+)\}', replace_var, text)


def load_config() -> Dict[str, Any]:
    """Load videos configuration from YAML file."""
    if not CONFIG_FILE.exists():
        print(f"❌ Configuration file not found: {CONFIG_FILE}")
        print("   Please create videos_config.yaml with your YouTube API key")
        sys.exit(1)
    
    with open(CONFIG_FILE, 'r') as f:
        content = f.read()
    
    # Substitute environment variables
    content = substitute_env_vars(content)
    
    config = yaml.safe_load(content)
    
    # Check for required fields
    required_fields = ['api_key', 'channel_id', 'favorites_playlist_id']
    for field in required_fields:
        if field not in config:
            print(f"❌ Missing required field '{field}' in {CONFIG_FILE}")
            sys.exit(1)
    
    # Check if API key is still a placeholder
    if config['api_key'] == '${YOUTUBE_API_KEY}':
        print("⚠️  YouTube API key not found in environment variables")
        print("   Set YOUTUBE_API_KEY environment variable or update videos_config.yaml")
        return None
    
    return config


def get_youtube_videos(api_key: str, playlist_id: str, max_results: int = 50) -> List[Dict[str, Any]]:
    """Fetch videos from a YouTube playlist."""
    videos = []
    next_page_token = None
    
    while len(videos) < max_results:
        # Calculate how many videos to fetch in this batch
        remaining = max_results - len(videos)
        current_max = min(50, remaining)  # YouTube API max is 50 per request
        
        params = {
            'part': 'snippet',
            'playlistId': playlist_id,
            'maxResults': current_max,
            'key': api_key
        }
        
        if next_page_token:
            params['pageToken'] = next_page_token
        
        try:
            response = requests.get(f"{YOUTUBE_API_BASE}/playlistItems", params=params)
            response.raise_for_status()
            data = response.json()
            
            for item in data.get('items', []):
                snippet = item.get('snippet', {})
                video_id = snippet.get('resourceId', {}).get('videoId')
                title = snippet.get('title')
                
                # Skip private videos
                if not video_id or not title or title == 'Private video':
                    continue
                
                # Get thumbnail URL with fallback
                thumbnails = snippet.get('thumbnails', {})
                thumbnail_url = (
                    thumbnails.get('high', {}).get('url') or
                    thumbnails.get('medium', {}).get('url') or
                    thumbnails.get('default', {}).get('url') or
                    f'https://i.ytimg.com/vi/{video_id}/hqdefault.jpg'
                )
                
                video = {
                    'id': video_id,
                    'title': title,
                    'description': snippet.get('description', ''),
                    'published_at': snippet.get('publishedAt'),
                    'thumbnail_url': thumbnail_url,
                    'channel_title': snippet.get('channelTitle', ''),
                    'playlist_id': playlist_id
                }
                videos.append(video)
            
            next_page_token = data.get('nextPageToken')
            if not next_page_token:
                break
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching videos from playlist {playlist_id}: {e}")
            break
    
    return videos[:max_results]


def get_channel_uploads_playlist(api_key: str, channel_id: str) -> str:
    """Get the uploads playlist ID for a channel."""
    params = {
        'part': 'contentDetails',
        'id': channel_id,
        'key': api_key
    }
    
    try:
        response = requests.get(f"{YOUTUBE_API_BASE}/channels", params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'items' in data and len(data['items']) > 0:
            return data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        else:
            print(f"❌ Channel {channel_id} not found")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching channel info: {e}")
        return None


def generate_videos_yaml():
    """Generate videos.yml for Jekyll."""
    print("🎥 Generating videos data...")
    
    # Load configuration
    config = load_config()
    if config is None:
        print("⚠️  Skipping videos generation due to missing API key")
        return []
    
    api_key = config['api_key']
    channel_id = config['channel_id']
    favorites_playlist_id = config['favorites_playlist_id']
    max_videos = config.get('max_videos', 100)
    
    all_videos = []
    
    # Get channel uploads playlist
    print(f"📺 Fetching channel videos from {channel_id}...")
    uploads_playlist = get_channel_uploads_playlist(api_key, channel_id)
    if uploads_playlist:
        channel_videos = get_youtube_videos(api_key, uploads_playlist, max_videos // 2)
        all_videos.extend(channel_videos)
        print(f"   Found {len(channel_videos)} channel videos")
    
    # Get favorites playlist
    print(f"⭐ Fetching favorites from playlist {favorites_playlist_id}...")
    favorites_videos = get_youtube_videos(api_key, favorites_playlist_id, max_videos // 2)
    all_videos.extend(favorites_videos)
    print(f"   Found {len(favorites_videos)} favorite videos")
    
    # Remove duplicates (same video ID)
    seen_ids = set()
    unique_videos = []
    for video in all_videos:
        if video['id'] and video['id'] not in seen_ids:
            seen_ids.add(video['id'])
            unique_videos.append(video)
    
    # Sort by published date (newest first)
    unique_videos.sort(key=lambda x: x['published_at'], reverse=True)
    
    # Limit to max_videos
    unique_videos = unique_videos[:max_videos]
    
    # Write to Jekyll _data directory
    output_file = OUTPUT_DIR / "videos.yml"
    with open(output_file, 'w') as f:
        yaml.dump(unique_videos, f, default_flow_style=False, allow_unicode=True)
    
    print(f"✅ Generated: {output_file}")
    print(f"   Found {len(unique_videos)} unique videos")
    
    return unique_videos


def main():
    """Generate videos data file."""
    print("=" * 60)
    print("YouTube Videos Generator")
    print("=" * 60)
    
    print(f"\n📂 Site root: {SITE_ROOT}")
    print(f"📂 Config file: {CONFIG_FILE}")
    
    # Generate videos data
    generate_videos_yaml()
    
    print("\n" + "=" * 60)
    print("✨ Done! Your videos data has been updated.")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review generated file:")
    print(f"   {OUTPUT_DIR}/videos.yml")
    print("\n2. Test locally:")
    print("   bundle exec jekyll serve")
    print("\n3. Commit and push to deploy:")
    print("   git add _data/")
    print("   git commit -m 'Update videos data'")
    print("   git push")
    print("=" * 60)


if __name__ == "__main__":
    main()
