# Myer Scraper

Scrape Myer (myer.com.au) department-store products: name, brand, price, was-price, saving, availability, category, images, attributes, colour & size variants, plus ratings and customer reviews. Search by keyword with brand, price and rating filters, or paste product, search or category URLs.

**[Open Myer Scraper on Apify](https://apify.com/abotapi/myer-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~myer-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["perfume"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `specialsCategory` | string | Specials / sale category |
| `urls` | array | Myer URLs |
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

Full details on the [scraper page](https://apify.com/abotapi/myer-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `name` | string |
| `brand` | string |
| `url` | string |
| `seoToken` | string |
| `price` | integer |
| `priceTo` | integer |
| `listPrice` | integer |
| `wasPrice` | null |
| `savedAmount` | null |
| `savingsPercent` | null |
| `promoLabel` | null |
| `promoLabels` | null |
| `isOnSale` | null |
| `currency` | string |
| `isAvailable` | boolean |
| `isBuyable` | boolean |
| `supplierColour` | null |
| `hasMoreColours` | boolean |
| `colourVariants` | list |
| `mfPartNumber` | string |
| `productExclusive` | null |
| `merchCategory` | string |
| `category` | string |
| `categories` | list |
| `imageUrl` | string |
| `images` | list |
| `searchMode` | string |
| `source` | string |
| `internalId` | integer |
| `title` | string |
| `brandUrl` | string |
| `shortDescription` | null |
| `longDescription` | string |
| `metaDescription` | string |
| `isClearance` | null |
| `afterPayEligible` | boolean |
| `hummEligible` | boolean |
| `categoryUri` | string |
| `specifications` | object |

---

[← All scrapers](../../README.md)
