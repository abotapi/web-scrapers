# Sam's Club Scraper

Scrape Sam's Club (samsclub.com) products by keyword, catalogue, category or URL. Extract prices, original prices, unit prices, ratings, stock availability, variants, images, specifications and customer reviews. Supports scheduled price change tracking.

**[Open Sam's Club Scraper on Apify](https://apify.com/abotapi/samsclub-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~samsclub-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["coffee"], "slugKeywords": ["paper towels"], "categoryKeywords": ["paper towels"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "reviewSort": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `slugKeywords` | array | Words in the product name |
| `categoryKeywords` | array | Words in the category name |
| `maxCategories` | integer | Max categories |
| `urls` | array | Sam's Club links |
| `sortBy` | string | Sort by |
| `minPrice` | number | Minimum price |
| `maxPrice` | number | Maximum price |
| `onSaleOnly` | boolean | Only discounted products |
| `minRating` | number | Minimum rating |
| `skipSponsored` | boolean | Skip sponsored products |
| `fetchDetails` | boolean | Read each product's page |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `reviewSort` | string | Review order |
| `includeReviewImages` | boolean | Include review photos |
| `fixedClub` | boolean | Read every page as one fixed club |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max result pages per keyword, category |
| `proxy` | object | Proxy configuration |
| `changeScope` | string | Changes to watch (incremental mode onl |
| `watchStock` | boolean | Count stock changes (incremental mode  |
| `compactUpdates` | boolean | Compact UPDATED rows (incremental mode |
| `expireAfterMissedScans` | integer | Expire after missed scans (incremental |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/samsclub-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `usItemId` | string |
| `productId` | string |
| `abstractProductId` | null |
| `name` | string |
| `url` | string |
| `brand` | null |
| `model` | null |
| `upc` | null |
| `productType` | string |
| `category` | null |
| `categoryPath` | list |
| `breadcrumbs` | list |
| `categoryPathId` | string |
| `departmentName` | string |
| `price` | float |
| `priceString` | string |
| `priceChannel` | null |
| `currency` | string |
| `wasPrice` | null |
| `wasPriceString` | null |
| `onSale` | boolean |
| `discountPercent` | null |
| `savingsAmount` | null |
| `savingsText` | null |
| `promotions` | list |
| `unitPrice` | null |
| `unitPriceText` | string |
| `priceRangeMin` | null |
| `priceRangeText` | null |
| `priceNote` | null |
| `isPriceByWeight` | boolean |
| `rating` | float |
| `reviewCount` | integer |
| `ratingHistogram` | null |
| `recommendedPercent` | null |
| `reviewsWithTextCount` | null |
| `reviewTopics` | list |
| `storeSummary` | null |
| `stockStatus` | string |

---

[← All scrapers](../../README.md)
