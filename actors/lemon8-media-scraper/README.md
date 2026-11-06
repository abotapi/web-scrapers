# Lemon8 Media Scraper

Lightweight Lemon8 scraper for extracting image and video URLs from posts, with optional media downloads. Built for fast, clean media collection without comments, captions, or other post details.

**[Open Lemon8 Media Scraper on Apify](https://apify.com/abotapi/lemon8-media-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~lemon8-media-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "auto", "searchTerm": "fashion", "feedCategories": ["foryou"], "keywords": ["fashion"], "region": "us", "limit": 10, "proxy": {"useApifyProxy": true, "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `postUrls` | array | Post URLs |
| `searchTerm` | string | Search Term |
| `feedCategories` | array | Feed categories (feed mode) |
| `keywords` | array | Keywords (discover mode) |
| `profileUrls` | array | Profile URLs (profile mode) |
| `region` | string | Region |
| `limit` | integer | Limit |
| `saveImages` | boolean | Save Images |
| `saveVideos` | boolean | Save Videos |
| `downloadMedia` | boolean | Download Media |
| `highQuality` | boolean | High Quality URLs |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/lemon8-media-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `postId` | string |
| `postUrl` | string |
| `images` | list |
| `videos` | list |
| `imageCount` | integer |
| `videoCount` | integer |
| `groupId` | string |
| `url` | string |
| `title` | string |
| `content` | string |
| `articleClass` | string |
| `likes` | integer |
| `saves` | integer |
| `commentCount` | integer |
| `authorUserId` | string |
| `authorUsername` | string |
| `authorNickname` | string |
| `authorAvatar` | string |
| `authorFollowers` | integer |
| `videoUrl` | null |
| `thumbnailUrl` | string |
| `hashtags` | list |
| `topComments` | list |
| `keyword` | string |
| `category` | null |
| `region` | string |
| `sourceMode` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
