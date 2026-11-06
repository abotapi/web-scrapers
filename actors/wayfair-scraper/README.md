# Wayfair Scraper

Scrape Wayfair.com furniture and home products by keyword or URL, including product, category, brand and sitemap links. Extract prices, discounts, ratings, variants, stock, images, specifications, dimensions and reviews. Supports scheduled price and stock change tracking.

**[Open Wayfair Scraper on Apify](https://apify.com/abotapi/wayfair-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~wayfair-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["standing desk"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "reviewSort": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `urls` | array | Wayfair links |
| `sortBy` | string | Sort by |
| `minPrice` | number | Minimum price |
| `maxPrice` | number | Maximum price |
| `onSaleOnly` | boolean | Only discounted products |
| `minRating` | number | Minimum rating |
| `brands` | array | Brands |
| `skipSponsored` | boolean | Skip sponsored products |
| `fetchDetails` | boolean | Read each product's page |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `reviewSort` | string | Review order |
| `includeReviewImages` | boolean | Include review photos |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max result pages per keyword or link |
| `proxy` | object | Proxy configuration |
| `changeScope` | string | Changes to watch (incremental mode onl |
| `compactUpdates` | boolean | Compact UPDATED rows (incremental mode |
| `expireAfterMissedScans` | integer | Expire after missed scans (incremental |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/wayfair-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `promoFlag` | string |
| `isBestValue` | boolean |
| `isSponsored` | boolean |
| `stockMessage` | string |
| `deliveryPromise` | string |
| `arrivalMessage` | string |
| `keySpecs` | object |
| `brandId` | null |
| `brandUrl` | null |
| `collection` | null |
| `ratingHistogram` | null |
| `reviewSummary` | null |
| `stockStatus` | null |
| `category` | null |
| `categoryId` | null |
| `breadcrumbs` | list |
| `description` | null |
| `highlights` | list |
| `specifications` | object |
| `dimensions` | object |
| `materials` | list |
| `selectedOptions` | object |
| `options` | list |
| `videos` | list |
| `sku` | string |
| `variantId` | string |
| `optionIds` | string |
| `name` | string |
| `url` | string |
| `brand` | string |
| `price` | float |
| `wasPrice` | float |
| `currency` | string |
| `discountPercent` | integer |
| `discountLabel` | string |
| `priceLabel` | null |
| `rating` | float |
| `reviewCount` | integer |
| `imageUrl` | string |

---

[← All scrapers](../../README.md)
