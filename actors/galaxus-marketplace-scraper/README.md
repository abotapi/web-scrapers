# Digitec Galaxus Scraper

Scrape Digitec Galaxus, Switzerland's largest online retailer: products with local prices, discounts, ratings, stock state and full specification tables across the galaxus.ch, galaxus.de and digitec.ch storefronts. Search keywords or paste links, and monitor price changes with recurring updates.

**[Open Digitec Galaxus Scraper on Apify](https://apify.com/abotapi/galaxus-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~galaxus-marketplace-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "market": "galaxus-ch", "searchTerms": ["laptop"], "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `market` | string | Storefront |
| `searchTerms` | array | Search terms |
| `sortBy` | string | Ordering |
| `minPrice` | integer | Min price (optional) |
| `maxPrice` | integer | Max price (optional) |
| `urls` | array | Product or category links |
| `fetchDetails` | boolean | Read product detail pages |
| `maxItems` | integer | Max records |
| `maxPages` | integer | Max pages per source |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/galaxus-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `productId` | integer |
| `name` | string |
| `brand` | string |
| `productTypeName` | string |
| `productTypeId` | integer |
| `url` | string |
| `imageUrl` | string |
| `price` | integer |
| `priceExclVat` | float |
| `currency` | string |
| `oldPrice` | null |
| `discountPercent` | null |
| `ratingAverage` | float |
| `ratingCount` | integer |
| `availability` | string |
| `stock` | object |
| `soldCount` | null |
| `promotionType` | null |
| `promotionRemainingDays` | null |
| `labels` | list |
| `canAddToCart` | boolean |
| `market` | string |
| `marketHost` | string |
| `sourceType` | string |
| `sourceId` | string |
| `sourceUrl` | string |
| `position` | integer |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
