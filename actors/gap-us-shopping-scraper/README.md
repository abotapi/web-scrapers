# Gap US Scraper

Scrape Gap US (gap.com) clothing and fashion products by category. Extract product names, prices, discounts, ratings, stock availability, colors, color-specific details and full descriptions. Ideal for price monitoring, competitor analysis and retail research.

**[Open Gap US Scraper on Apify](https://apify.com/abotapi/gap-us-shopping-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~gap-us-shopping-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "brands": ["gap"], "queries": ["denim jacket"], "categoryKeywords": ["women dresses"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "reviewSort": "newest", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `brands` | array | Storefronts |
| `queries` | array | Search keywords |
| `categoryKeywords` | array | Category name words |
| `maxCategories` | integer | Max categories per storefront |
| `urls` | array | Links |
| `sortBy` | string | Sort by |
| `minPrice` | number | Min price (USD) |
| `maxPrice` | number | Max price (USD) |
| `onSaleOnly` | boolean | On sale or clearance only |
| `minRating` | number | Min rating |
| `fetchDetails` | boolean | Read each product's page |
| `fetchReviews` | boolean | Collect customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `reviewSort` | string | Review order |
| `includeReviewPhotos` | boolean | Include review photo links |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max result pages per keyword or catego |
| `proxy` | object | Proxy configuration |
| `changeScope` | string | Changes to watch (incremental mode onl |
| `watchStock` | boolean | Count stock changes (incremental mode  |
| `compactUpdates` | boolean | Compact UPDATED rows (incremental mode |
| `expireAfterMissedScans` | integer | Expire after missed scans (incremental |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/gap-us-shopping-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `productKey` | string |
| `productId` | string |
| `name` | string |
| `brand` | string |
| `brandCode` | string |
| `url` | string |
| `currency` | string |
| `price` | integer |
| `priceMax` | integer |
| `regularPrice` | float |
| `discountPercent` | integer |
| `discountAmount` | float |
| `onSale` | boolean |
| `priceType` | string |
| `rating` | float |
| `reviewCount` | integer |
| `colorCount` | integer |
| `colors` | list |
| `inStock` | boolean |
| `totalInventory` | integer |
| `freeShipping` | boolean |
| `excludedFromPromotion` | boolean |
| `productType` | string |
| `promoFlags` | list |
| `badges` | list |
| `imageUrl` | string |
| `sourceLabel` | string |
| `position` | integer |
| `page` | integer |
| `scrapedAt` | string |
| `reviewsRequested` | boolean |
| `reviews` | list |
| `reviewsDelivered` | integer |

---

[← All scrapers](../../README.md)
