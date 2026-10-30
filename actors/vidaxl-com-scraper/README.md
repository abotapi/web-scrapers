# VidaXL Scraper

Scrape the vidaXL storefronts by keyword or URL across 6 European markets. Every row carries price, currency, brand, category path, EAN and stock state. Detail enrichment adds description, specifications and the full image gallery. Recurring change tracking is first-class.

**[Open VidaXL Scraper on Apify](https://apify.com/abotapi/vidaxl-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~vidaxl-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["garden chair"], "market": "de", "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `searchTerms` | array | Search terms |
| `urls` | array | Store URLs |
| `market` | string | Market |
| `sortBy` | string | Sort the store results by |
| `minPrice` | number | Minimum price |
| `maxPrice` | number | Maximum price |
| `onSaleOnly` | boolean | Discounted rows only |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/vidaxl-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `productId` | string |
| `ean` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `sku` | string |
| `masterProductId` | string |
| `categories` | list |
| `categoryPath` | string |
| `variants` | object |
| `price` | float |
| `oldPrice` | null |
| `onSale` | boolean |
| `currency` | string |
| `imageUrl` | string |
| `market` | string |
| `marketHost` | string |
| `description` | string |
| `specifications` | object |
| `imageUrls` | list |
| `imageCount` | integer |
| `availability` | string |
| `stockStatus` | string |
| `deliveryEstimate` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
