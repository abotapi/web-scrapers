# dm.de Scraper

Scrape dm-drogerie markt (dm.de) products: current + strike-through Ausverkauf price with discount, per-unit pricing (per 100ml/kg/piece), brand incl. dm own-brands, EAN, ingredients, pack-size variants, and full reviews with rating breakdown. Search or paste links.

**[Open dm.de Scraper on Apify](https://apify.com/abotapi/dm-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~dm-de-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "shampoo", "sortBy": "RELEVANCE", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword or category |
| `urls` | array | URLs to scrape |
| `specialsOnly` | boolean | Ausverkauf / clearance only |
| `brands` | array | Brands |
| `minRating` | integer | Minimum rating |
| `minPrice` | number | Minimum price (EUR) |
| `maxPrice` | number | Maximum price (EUR) |
| `sortBy` | string | Sort order |
| `fetchDetails` | boolean | Fetch full product detail |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/dm-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `sku` | string |
| `ean` | string |
| `name` | string |
| `brand` | string |
| `category` | string |
| `url` | string |
| `price` | float |
| `currency` | string |
| `priceExclVat` | float |
| `originalPrice` | null |
| `discountAmount` | null |
| `discountPercent` | null |
| `isOnSpecial` | boolean |
| `promoLabel` | null |
| `unitPrice` | float |
| `unitPriceBasis` | string |
| `packSize` | string |
| `rating` | float |
| `reviewCount` | integer |
| `isPharmacy` | boolean |
| `image` | string |
| `images` | list |
| `reviews` | object |

---

[← All scrapers](../../README.md)
