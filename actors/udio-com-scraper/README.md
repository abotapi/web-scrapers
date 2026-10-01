# Udio Scraper

Collect public Udio tracks with the complete generation prompt, full lyrics, style tags, like and play counts, duration, artwork and a direct audio link. Search the catalogue by keyword and ordering, read a list of track addresses, or pull a public playlist in its original order.

**[Open Udio Scraper on Apify](https://apify.com/abotapi/udio-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~udio-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "sortBy": "newest", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | What to collect |
| `searchTerm` | string | Keyword |
| `sortBy` | string | Order results by |
| `trackIds` | array | Track addresses |
| `playlistIds` | array | Playlist addresses |
| `maxItems` | integer | Maximum tracks |
| `proxyConfiguration` | object | Connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/udio-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `trackId` | string |
| `url` | string |
| `title` | string |
| `artist` | string |
| `artistImageUrl` | string |
| `creatorId` | string |
| `prompt` | string |
| `lyrics` | string |
| `description` | string |
| `tags` | list |
| `userTags` | list |
| `attribution` | null |
| `likeCount` | integer |
| `playCount` | integer |
| `durationSeconds` | float |
| `createdAt` | string |
| `publishedAt` | string |
| `audioUrl` | string |
| `videoUrl` | null |
| `artworkUrl` | string |
| `styleId` | null |
| `styleSourceType` | null |
| `styleSourceTrackId` | null |
| `parentTrackId` | string |
| `generationId` | string |
| `generationStatus` | string |
| `isFinished` | boolean |
| `isPublishable` | boolean |
| `sourceMode` | string |
| `collectionId` | null |
| `collectionName` | null |
| `positionInCollection` | null |
| `scrapedAt` | string |
| `raw` | object |

---

[← All scrapers](../../README.md)
