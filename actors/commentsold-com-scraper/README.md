# CommentSold Scraper

Scrape CommentSold boutique shops by name or URL. Extract product catalogs, descriptions, variant prices, stock availability and product details. Collect live shopping status, show replays and shoppable videos. Supports scraping single or multiple shops.

**[Open CommentSold Scraper on Apify](https://apify.com/abotapi/commentsold-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~commentsold-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "shops": ["shopthemasonjar"], "collections": ["all-items"], "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `shops` | array | Shop names or shop links |
| `urls` | array | Shop links |
| `collections` | array | Collections |
| `searchQuery` | string | Keyword |
| `inStockOnly` | boolean | In-stock products only |
| `fetchDetails` | boolean | Read each product's full detail page |
| `includeLive` | boolean | Include the live surface |
| `minPrice` | number | Minimum price |
| `maxPrice` | number | Maximum price |
| `maxItems` | integer | Max results |
| `maxPages` | integer | Max pages per shop or link |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/commentsold-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `shopSlug` | string |
| `shopUrl` | string |
| `showId` | string |
| `title` | string |
| `status` | string |
| `isLiveNow` | boolean |
| `viewerCount` | integer |
| `startedAt` | null |
| `productCount` | integer |
| `thumbnailUrl` | null |
| `url` | string |
| `searchMode` | string |
| `searchQuery` | null |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
