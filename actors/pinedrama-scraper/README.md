# PineDrama Scraper

Scrape Pine Drama series by keyword, category or URL across 17 languages. Extract titles, watch counts, episode counts, genres, theme tags, covers, languages, hot/new/free labels, creator IDs and full episode lists. Supports incremental updates and MCP export.

**[Open PineDrama Scraper on Apify](https://apify.com/abotapi/pinedrama-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~pinedrama-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": ["CEO"], "language": "en", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `keywords` | array | Keywords |
| `categoryFilters` | array | Category filters |
| `language` | string | Language |
| `urls` | array | Links |
| `fetchDetails` | boolean | Fetch episode lists |
| `fetchVideoStats` | boolean | Fetch first-episode video stats |
| `maxPages` | integer | Max pages |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/pinedrama-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `collection_id` | string |
| `title` | string |
| `cover_url` | string |
| `cover_uri` | string |
| `cover_width` | integer |
| `cover_height` | integer |
| `episode_count` | integer |
| `watched_count` | integer |
| `categories` | list |
| `theme_tags` | list |
| `theme_tag_ids` | list |
| `category` | integer |
| `is_limited_free` | boolean |
| `is_safety_selected` | boolean |
| `label_hot` | boolean |
| `label_new` | boolean |
| `language_code` | string |
| `scene` | integer |
| `category_filters` | list |
| `keyword` | string |
| `video_id` | string |
| `creator_id` | string |
| `short_cut_num` | integer |
| `episodes` | list |
| `episodes_collected` | integer |
| `source_collection_id` | null |
| `language` | string |
| `page` | integer |
| `detailFetched` | boolean |
| `extractionPath` | string |
| `scrapedAt` | string |
| `resultsReturned` | integer |
| `changeType` | string |

---

[← All scrapers](../../README.md)
