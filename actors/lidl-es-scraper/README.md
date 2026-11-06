# Lidl.es Products Scraper

Scrape Lidl.es grocery and non-food products across weekly offers, tools, home, garden, kitchen, fashion, kids, sport and more. Search by keyword, department or URL. Extract prices, was-prices, discounts, package formats, images, ratings and full shopper reviews.

**[Open Lidl.es Products Scraper on Apify](https://apify.com/abotapi/lidl-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~lidl-es-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "bateria", "sortBy": "RELEVANCE", "maxPages": 1, "maxItems": 10, "maxReviewsPerProduct": 10, "proxy": {"useApifyProxy": true}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword |
| `category` | string | Department |
| `brand` | string | Brand |
| `specialsOnly` | boolean | Weekly offers only |
| `inStockOnly` | boolean | In stock only |
| `strictMatch` | boolean | Strict keyword match |
| `minPrice` | number | Minimum price (EUR) |
| `maxPrice` | number | Maximum price (EUR) |
| `minRating` | number | Minimum rating (1-5) |
| `sortBy` | string | Sort order |
| `urls` | array | URLs to scrape |
| `maxPages` | integer | Max search pages |
| `maxItems` | integer | Max products total |
| `fetchDetails` | boolean | Fetch shopper reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `proxy` | object | Proxy configuration |
| `changeScope` | string | What counts as a change (incremental m |
| `compactUpdates` | boolean | Compact update rows (incremental mode  |
| `expireAfterMissedScans` | integer | Expire after N missed full scans (incr |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/lidl-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `title` | string |
| `brand` | string |
| `categoryPath` | list |
| `category` | string |
| `productUrl` | string |
| `price` | float |
| `currency` | string |
| `wasPrice` | null |
| `discountAmount` | null |
| `discountPercent` | null |
| `isOnSpecial` | boolean |
| `promoLabel` | null |
| `packageFormat` | null |
| `hasVat` | boolean |
| `unitPrice` | null |
| `unitOfMeasure` | null |
| `onlineAvailable` | boolean |
| `inStoreOnly` | boolean |
| `stockAvailability` | object |
| `images` | list |
| `internalArticleNumbers` | list |
| `description` | string |
| `badges` | list |
| `averageRating` | float |
| `reviewCount` | integer |
| `recommendedYes` | integer |
| `recommendedNo` | integer |
| `reviews` | object |
| `name` | string |
| `erpNumber` | string |
| `itemNumber` | string |
| `productKey` | string |
| `country` | string |
| `categoryLvl0` | string |
| `labels` | list |
| `priceEur` | float |
| `priceNormal` | float |
| `comparePrice` | null |
| `compareUnit` | null |

---

[← All scrapers](../../README.md)
