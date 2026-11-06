# NetShort Scraper

Scrape the NetShort short-drama catalog: series with synopses, like and follow counters, categories, episode lists with lock flags, publish dates and reviews. Catalog, category, trending or pasted links, in 16 site languages. Resume, incremental updates and MCP export included.

**[Open NetShort Scraper on Apify](https://apify.com/abotapi/netshort-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~netshort-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "catalog", "language": "en", "maxItems": 10, "maxPages": 1, "maxReviews": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `categories` | array | Categories (category mode) |
| `language` | string | Site language |
| `listingUrls` | array | Links (urls mode) |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per scope |
| `fetchDetails` | boolean | Fetch detail pages |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviews` | integer | Max reviews per series |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/netshort-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `slug` | string |
| `title` | string |
| `titleRaw` | string |
| `isDubbed` | boolean |
| `url` | string |
| `fullEpisodesUrl` | string |
| `cover` | string |
| `description` | string |
| `genres` | list |
| `genreIds` | list |
| `episodes` | integer |
| `language` | string |
| `libraryId` | string |
| `isDelisted` | boolean |
| `releaseDate` | null |
| `mode` | string |
| `extractionPath` | string |
| `likesDisplay` | string |
| `followsDisplay` | string |
| `likes` | integer |
| `follows` | integer |
| `detailFetched` | boolean |
| `reviews` | list |
| `reviewsFetched` | boolean |
| `resultsReturned` | integer |
| `platform` | string |
| `scrapedAt` | string |
| `changeType` | string |

---

[← All scrapers](../../README.md)
