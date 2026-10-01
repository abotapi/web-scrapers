# Idealo.de Scraper

Scrape Idealo.de products with identity details, GTIN, price ranges, specifications, images, rating breakdowns and customer reviews. Get the complete merchant offer list, including prices, seller details, and offer pros and cons. Search by keyword or paste product URLs.

**[Open Idealo.de Scraper on Apify](https://apify.com/abotapi/idealo-de-price-comparison-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~idealo-de-price-comparison-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "url", "searchQuery": "iphone 15", "urls": ["https://www.idealo.de/preisvergleich/ProductCategory/5292.html"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "DE"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `searchQuery` | string | Search keyword (search mode only) |
| `urls` | array | URLs (URL mode only) |
| `fetchDetails` | boolean | Fetch full product detail |
| `maxItems` | integer | Maximum items |
| `maxPages` | integer | Maximum pages per search |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/idealo-de-price-comparison-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `category` | null |
| `gtin` | null |
| `lowPrice` | float |
| `highPrice` | integer |
| `currency` | string |
| `priceFormatted` | string |
| `offerCount` | integer |
| `rating` | float |
| `reviewCount` | integer |
| `reviewBreakdown` | object |
| `previewImage` | string |
| `images` | list |
| `description` | string |
| `specs` | object |
| `offers` | list |
| `reviews` | list |

---

[← All scrapers](../../README.md)
