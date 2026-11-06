# Kmart Australia Scraper Lite

Scrape kmart.com.au products and reviews: names, brand, prices, promotions, ratings, reviews, colours, sizes, images, seller, categories, stock, variations and specifications. Search or paste product and category URLs, with sorting and filters.

**[Open Kmart Australia Scraper Lite on Apify](https://apify.com/abotapi/kmart-au-scraper-lite?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~kmart-au-scraper-lite/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["towel"], "sortBy": "relevance", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `specialsCategory` | string | Specials / offers collection |
| `urls` | array | URLs |
| `basketItems` | array | Basket lines |
| `sortBy` | string | Sort by |
| `brand` | string | Brand |
| `colour` | string | Colour |
| `category` | string | Category |
| `includeMarketplace` | boolean | Include marketplace products |
| `sellers` | array | Sellers |
| `minPrice` | integer | Min price (AUD) |
| `maxPrice` | integer | Max price (AUD) |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviews` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per search |
| `storePostcodes` | array | Store postcodes |
| `storeNames` | array | Store names |
| `includeClickAndCollect` | boolean | Include Click & Collect and exact unit |
| `trackStates` | array | Tracked states |
| `verifyOnlineDelivery` | boolean | Check online delivery live (Tracked st |
| `deliveryPostcode` | string | Delivery postcode (optional, one Track |
| `returnDeliveryAnswers` | boolean | Return verified delivery answers once  |
| `proxy` | object | Proxy |
| `baselineDatasetId` | string | Start from an existing dataset (option |
| `earlierHistoryStoreId` | string | Continue from the Kmart Australia Scra |
| `changeScope` | string | What counts as a change (incremental m |
| `compactUpdates` | boolean | Compact update rows (incremental mode  |
| `expireAfterMissedScans` | integer | Expire after N missed full scans (incr |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/kmart-au-scraper-lite?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `id` | string |
| `productId` | string |
| `name` | string |
| `title` | string |
| `url` | string |
| `brand` | string |
| `apn` | integer |
| `description` | string |
| `descriptionText` | string |
| `descriptionSummary` | string |
| `features` | null |
| `specifications` | object |
| `careInstructions` | list |
| `additionalInfo` | list |
| `warnings` | null |
| `manuals` | null |
| `detailSections` | list |
| `price` | float |
| `currentPrice` | float |
| `listPrice` | float |
| `promoPrice` | float |
| `wasPrice` | null |
| `savingsAmount` | null |
| `savingsPercent` | null |
| `isOnSpecial` | boolean |
| `promoLabel` | null |
| `variantBadges` | null |
| `currency` | string |
| `onSale` | boolean |
| `clearance` | boolean |
| `averageRating` | float |
| `reviewCount` | integer |
| `colour` | string |
| `secondaryColour` | string |
| `size` | string |
| `seller` | string |
| `isMarketplace` | boolean |
| `merchDepartment` | integer |
| `merchClass` | string |

---

[← All scrapers](../../README.md)
