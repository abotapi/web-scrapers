# Universal Media Extractor Scraper

Extract videos, audio, and metadata from 1000+ websites including YouTube, TikTok, Twitter/X, Instagram, Vimeo, Facebook, Twitch, and many more. Stream directly to your cloud storage or get direct download URLs for your pipelines.

**[Open Universal Media Extractor Scraper on Apify](https://apify.com/abotapi/universal-media-extractor?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~universal-media-extractor/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "mode": "extract", "format": "best", "storage_type": "apify", "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `url` * | string | Video URL |
| `mode` | string | Mode |
| `format` | string | Format |
| `storage_type` | string | Storage Type |
| `storage_config` | object | Storage Configuration |
| `proxy` | object | Proxy configuration |
| `extract_flat` | boolean | Extract Flat (Playlists) |
| `playlist_items` | string | Playlist Items |
| `write_subtitles` | boolean | Write Subtitles |
| `subtitle_langs` | array | Subtitle Languages |
| `geo_bypass` | boolean | Geo Bypass |
| `ignore_errors` | boolean | Ignore Errors |
| `username` | string | Username |
| `password` | string | Password |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/universal-media-extractor?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `title` | string |
| `formats` | list |
| `thumbnails` | list |
| `thumbnail` | string |
| `description` | string |
| `channel_id` | string |
| `channel_url` | string |
| `duration` | integer |
| `view_count` | integer |
| `average_rating` | null |
| `age_limit` | integer |
| `webpage_url` | string |
| `categories` | list |
| `tags` | list |
| `playable_in_embed` | boolean |
| `live_status` | string |
| `media_type` | string |
| `release_timestamp` | null |
| `_format_sort_fields` | list |
| `automatic_captions` | object |
| `subtitles` | object |
| `comment_count` | integer |
| `chapters` | null |
| `heatmap` | list |
| `like_count` | integer |
| `channel` | string |
| `channel_follower_count` | integer |
| `creators` | null |
| `channel_is_verified` | boolean |
| `uploader` | string |
| `uploader_id` | string |
| `uploader_url` | string |
| `upload_date` | string |
| `timestamp` | integer |
| `availability` | string |
| `original_url` | string |
| `webpage_url_basename` | string |
| `webpage_url_domain` | string |
| `extractor` | string |

---

[← All scrapers](../../README.md)
