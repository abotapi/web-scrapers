# ShortMax Scraper

Scrape the ShortMax short-drama catalog: titles, descriptions, creators, view and follow counters, two genre taxonomies, trending rails with rank and episode lists. Catalog, category, genre, trending or pasted links, in 19 site languages. Resume, incremental updates and MCP export.

**[Open ShortMax Scraper on Apify](https://apify.com/abotapi/shortmax-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~shortmax-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "catalog", "language": "en", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `categories` | array | Categories (category mode) |
| `genres` | array | Genres (genre mode) |
| `language` | string | Site language |
| `listingUrls` | array | Links (urls mode) |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per scope |
| `fetchDetails` | boolean | Fetch detail pages |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/shortmax-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `slug` | string |
| `title` | string |
| `cover` | string |
| `url` | string |
| `episodeUrl` | string |
| `viewsDisplay` | string |
| `followsDisplay` | string |
| `views` | integer |
| `follows` | integer |
| `recordType` | string |
| `language` | string |
| `mode` | string |
| `extractionPath` | string |
| `description` | string |
| `genres` | list |
| `category` | object |
| `creator` | string |
| `episodeList` | list |
| `episodes` | integer |
| `allEpisodesUrl` | string |
| `detailFetched` | boolean |
| `resultsReturned` | integer |
| `platform` | string |
| `scrapedAt` | string |
| `changeType` | string |

---

[← All scrapers](../../README.md)
