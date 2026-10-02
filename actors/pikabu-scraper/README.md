# Pikabu Scraper

Scrape Pikabu (Пикабу): keyword search, hot/new/best feeds, communities, tags, full story details with media, all comments, creator profiles. Monitoring (NEW, UPDATED, REAPPEARED, EXPIRED), incremental runs, resume, MCP export.

**[Open Pikabu Scraper on Apify](https://apify.com/abotapi/pikabu-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~pikabu-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQuery": "steam", "searchOrder": "relevance", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQuery` | string | Search query |
| `searchOrder` | string | Order |
| `feedLinks` | array | Feed, community, tag or user links |
| `storyUrls` | array | Story links or IDs |
| `profileUrls` | array | Profile links or names |
| `fetchDetails` | boolean | Open each story for full detail |
| `fetchComments` | boolean | Collect comments (story mode or with f |
| `maxCommentsPerStory` | integer | Max comments per story (0  all) |
| `maxItems` | integer | Max items |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/pikabu-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `id` | string |
| `title` | string |
| `url` | string |
| `author` | object |
| `community` | object |
| `tags` | list |
| `tagUrls` | list |
| `rating` | integer |
| `pluses` | null |
| `minuses` | null |
| `commentsCount` | integer |
| `publishedAt` | string |
| `timestamp` | integer |
| `seriesId` | null |
| `isLong` | boolean |
| `isPinned` | boolean |
| `blocks` | list |
| `text` | string |
| `images` | list |
| `videos` | list |
| `media` | object |

---

[← All scrapers](../../README.md)
