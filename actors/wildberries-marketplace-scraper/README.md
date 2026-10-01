# Wildberries Scraper

Scrape Wildberries marketplace: product search with prices (wallet vs retail), discounts, stock, ratings and seller data. Paste product or seller links for review analytics and seller registration info. Incremental monitoring with NEW, UPDATED, REAPPEARED, EXPIRED, resume and MCP export.

**[Open Wildberries Scraper on Apify](https://apify.com/abotapi/wildberries-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~wildberries-marketplace-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "query": "iphone", "sortBy": "popular", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `query` | string | Search query |
| `urls` | array | Wildberries links |
| `sortBy` | string | Sort by |
| `priceMin` | integer | Min price (RUB) |
| `priceMax` | integer | Max price (RUB) |
| `minRating` | integer | Min rating (1-5) |
| `minFeedbacks` | integer | Min review count |
| `onlyWithDiscount` | boolean | Only discounted products |
| `fetchDetails` | boolean | Fetch full product details |
| `maxFeedbacksPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per scope |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/wildberries-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `nmId` | integer |
| `rootId` | integer |
| `url` | string |
| `name` | string |
| `brand` | string |
| `brandId` | integer |
| `subjectId` | integer |
| `price` | integer |
| `priceRetail` | integer |
| `priceLogistics` | integer |
| `discountPercent` | integer |
| `hasDiscount` | boolean |
| `currency` | string |
| `rating` | integer |
| `reviewRating` | integer |
| `feedbacksCount` | integer |
| `stock` | integer |
| `volume` | integer |
| `weight` | float |
| `warehouseIds` | list |
| `deliveryDaysMin` | integer |
| `deliveryDaysMax` | integer |
| `colors` | list |
| `imageUrl` | string |
| `imageUrlsCount` | integer |
| `supplierId` | integer |
| `supplierName` | string |
| `supplierRating` | float |
| `description` | null |
| `characteristics` | null |
| `feedbacks` | list |
| `feedbackSummary` | object |

---

[← All scrapers](../../README.md)
