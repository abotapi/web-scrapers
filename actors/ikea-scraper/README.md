# IKEA Products & Reviews Scraper

Scrape IKEA products across 50+ markets. Extract names, prices, currencies, ratings, full reviews, colours, dimensions, images, categories, variants, badges and store availability. Supports search, category, item-number and URL inputs with filters and sorting.

**[Open IKEA Products & Reviews Scraper on Apify](https://apify.com/abotapi/ikea-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~ikea-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "market": "us/en", "searchTerms": ["bookcase"], "sortBy": "RELEVANCE", "specialsCategory": "none", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `market` | string | Market and language |
| `searchTerms` | array | Search terms |
| `sortBy` | string | Sort by |
| `categories` | array | Category links or ids |
| `productIds` | array | Item numbers |
| `urls` | array | URLs |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `minRating` | integer | Min rating |
| `inStockOnly` | boolean | In stock only |
| `containsKeyword` | string | Contains keyword |
| `specialsCategory` | string | Specials |
| `fetchDetails` | boolean | Fetch full details and reviews |
| `maxReviews` | integer | Max reviews per product |
| `includeAvailability` | boolean | Include store availability |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per input |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/ikea-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `id` | string |
| `itemNo` | string |
| `itemNoGlobal` | string |
| `itemType` | string |
| `name` | string |
| `typeName` | string |
| `description` | string |
| `url` | string |
| `price` | integer |
| `currency` | string |
| `priceFormatted` | string |
| `priceDiscount` | null |
| `priceTag` | null |
| `onSale` | boolean |
| `isOnSpecial` | boolean |
| `wasPrice` | null |
| `wasPriceFormatted` | null |
| `savingsAmount` | null |
| `discountPercent` | null |
| `specialsLabel` | null |
| `isBreathTaking` | boolean |
| `priceValidFrom` | null |
| `priceValidTo` | null |
| `ratingValue` | float |
| `ratingCount` | integer |
| `color` | string |
| `colors` | list |
| `measurementText` | string |
| `width` | float |
| `depth` | integer |
| `height` | float |
| `measurementUnit` | string |
| `categoryPath` | list |
| `categoryClass` | string |
| `businessStructure` | object |
| `badge` | string |
| `badgeType` | string |
| `isBestseller` | boolean |
| `isNewArrival` | boolean |

---

[← All scrapers](../../README.md)
