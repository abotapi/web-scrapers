# Officeworks Scraper

Scrape Officeworks products by keyword, category, or URL. Extract names, brands, prices, GST, stock by state, images, specifications, identifiers, ratings, reviews, and star distributions. Supports brand, price, and rating filters.

**[Open Officeworks Scraper on Apify](https://apify.com/abotapi/officeworks-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~officeworks-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["laptop"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `specialsCategory` | string | Specials / offers collection |
| `urls` | array | Officeworks URLs |
| `brand` | string | Brand |
| `sortBy` | string | Sort by |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `minRating` | integer | Minimum rating |
| `includeOutOfStock` | boolean | Include unavailable products |
| `detailEnrichment` | boolean | Fetch full product detail  reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/officeworks-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `sku` | string |
| `name` | string |
| `title` | string |
| `brand` | string |
| `url` | string |
| `seoPath` | string |
| `price` | integer |
| `currency` | string |
| `gtin` | string |
| `manufacturerPartNumber` | string |
| `productType` | string |
| `colour` | string |
| `multipackSize` | null |
| `unitsPerPack` | integer |
| `category` | string |
| `categoryPath` | string |
| `availableStates` | list |
| `isAvailableInStore` | boolean |
| `availableOnline` | boolean |
| `isClearance` | boolean |
| `isOnSpecial` | boolean |
| `isNew` | boolean |
| `promoLabel` | string |
| `wasPrice` | null |
| `savingsAmount` | null |
| `savingsPercent` | null |
| `rating` | integer |
| `reviewCount` | integer |
| `imageUrl` | string |
| `images` | list |
| `searchMode` | string |
| `source` | string |
| `variants` | list |
| `variantAxes` | object |
| `variantCount` | integer |
| `categoryHierarchy` | list |
| `itemsPerUnit` | null |
| `totalUnits` | null |
| `brandUrl` | string |
| `edlpPrice` | integer |

---

[← All scrapers](../../README.md)
