# Target AU Scraper

Scrape products and customer reviews from Target.com.au. Search by keyword or use product/category URLs with sorting and filters. Returns name, brand, price, OnePass price, ratings, review text and stats, colours, sizes, images, category, stock, and variations.

**[Open Target AU Scraper on Apify](https://apify.com/abotapi/target-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~target-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["shirt"], "sortBy": "relevance", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `urls` | array | URLs |
| `sortBy` | string | Sort by |
| `specialsCategory` | string | Specials / offers |
| `brand` | string | Brand |
| `colour` | string | Colour |
| `minPrice` | integer | Min price (AUD) |
| `maxPrice` | integer | Max price (AUD) |
| `fetchReviews` | boolean | Fetch ratings and reviews |
| `maxReviews` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/target-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `id` | string |
| `name` | string |
| `title` | string |
| `url` | string |
| `baseUrl` | string |
| `brand` | string |
| `price` | integer |
| `wasPrice` | null |
| `onePassPrice` | null |
| `currency` | string |
| `onSale` | boolean |
| `isOnSpecial` | boolean |
| `savingsAmount` | null |
| `savingsPercent` | null |
| `promoLabel` | null |
| `onlineOnlyPrice` | boolean |
| `clearance` | boolean |
| `description` | string |
| `features` | list |
| `careInstructions` | list |
| `category` | string |
| `breadcrumbs` | list |
| `topLevelCategory` | string |
| `merchDepartmentCode` | integer |
| `productType` | string |
| `availability` | string |
| `groupIds` | list |
| `colour` | string |
| `colourVariantCode` | integer |
| `sizeVariantCode` | integer |
| `inStock` | boolean |
| `availableOnlineQty` | integer |
| `availableStoreQty` | integer |
| `bulkyProduct` | boolean |
| `targetExclusive` | boolean |
| `onlineExclusive` | boolean |
| `newArrival` | boolean |
| `onePassExclusive` | boolean |
| `advFreeDeliveryEligible` | boolean |

---

[← All scrapers](../../README.md)
