# Lowe's Scraper

Scrape Lowe's (lowes.com) home improvement, tools, appliances and building supplies by keyword search. Extract product names, brands, prices, descriptions, specifications, stock availability, ratings and customer reviews. Ideal for price monitoring, competitor analysis and retail market research.

**[Open Lowe's Scraper on Apify](https://apify.com/abotapi/lowes-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~lowes-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "urls", "searchTerms": ["drill"], "urls": [{"url": "https://www.lowes.com/search?searchTerm=drill"}, {"url": "https://www.lowes.com/pd/CRAFTSMAN-20-volt-Max-1-2-in-Keyless-Brushless-Cordless-Drill-1-Batteries-Included-Soft-Bag-Included/5016412045"}], "maxReviews": 10, "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `searchTerms` | array | Search terms |
| `urls` | array | Storefront links |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviews` | integer | Max reviews per product |
| `zipCode` | string | ZIP code for pricing |
| `maxItems` | integer | Max items |
| `proxyConfiguration` | object | Proxy configuration |
| `changeScope` | string | Changes to watch (incremental mode onl |
| `compactUpdates` | boolean | Compact UPDATED rows (incremental mode |
| `watchStockQuantity` | boolean | Count stock unit changes (incremental  |
| `expireAfterMissedScans` | integer | Expire after missed scans (incremental |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/lowes-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `productId` | string |
| `lin` | string |
| `modelId` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `price` | integer |
| `priceUnavailableReason` | null |
| `wasPrice` | integer |
| `pricePerUnit` | null |
| `currency` | string |
| `stockQuantity` | integer |
| `itemNumber` | string |
| `inStock` | boolean |
| `pickupEligible` | boolean |
| `parcelEligible` | boolean |
| `freeShipping` | boolean |
| `storeNumber` | string |
| `marketingBullets` | list |
| `brandId` | string |
| `groups` | list |
| `collection` | object |
| `categories` | list |
| `merchandisingHierarchy` | object |
| `measurements` | object |
| `guides` | list |
| `images` | list |
| `videos` | list |
| `status` | string |
| `lowesExclusive` | boolean |
| `energyStar` | boolean |
| `priceInfo` | object |
| `savingsAmount` | integer |
| `savingsPercent` | integer |
| `saleEndsAt` | string |
| `promotions` | list |
| `inventory` | list |
| `storeInfo` | null |
| `barcode` | string |

---

[← All scrapers](../../README.md)
