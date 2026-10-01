# Vinted Multi-Country Scraper

Scrape Vinted across 27 country marketplaces: keyword search with brand, price and condition filters, item and seller URLs, or a seller's full feedback history. Returns price, currency, condition, size, view and favourite counts, seller rating and profile depth per listing.

**[Open Vinted Multi-Country Scraper on Apify](https://apify.com/abotapi/vinted-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~vinted-marketplace-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "country": "de", "queries": ["nike"], "sortBy": "relevance", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `country` | string | Country marketplace |
| `queries` | array | Search keywords |
| `categoryId` | string | Category ID (optional) |
| `brandId` | string | Brand ID (optional) |
| `conditions` | array | Condition (optional) |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `sortBy` | string | Sort order |
| `urls` | array | URLs to scrape |
| `sellers` | array | Sellers |
| `fetchDetails` | boolean | Fetch item detail |
| `fetchSellerProfiles` | boolean | Fetch seller profiles |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max items total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/vinted-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `itemId` | string |
| `title` | string |
| `url` | string |
| `path` | string |
| `brandTitle` | string |
| `priceAmount` | integer |
| `currency` | string |
| `size` | string |
| `condition` | string |
| `viewCount` | null |
| `favouriteCount` | integer |
| `promoted` | boolean |
| `photos` | list |
| `image` | string |
| `seller` | object |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
