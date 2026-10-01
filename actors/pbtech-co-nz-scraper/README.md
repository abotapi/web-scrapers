# PB Tech Scraper

Scrape pbtech.co.nz products with full specifications, price, brand, condition, per-store stock, image gallery, customer reviews and rating stats. Search by keyword and department with brand, price, rating and sort filters, or paste product / category / search URLs.

**[Open PB Tech Scraper on Apify](https://apify.com/abotapi/pbtech-co-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~pbtech-co-nz-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["gaming laptop"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "NZ"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `specialsCategory` | string | Specials / offers category |
| `urls` | array | PB Tech URLs |
| `brand` | string | Brand |
| `sortBy` | string | Sort by |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `minRating` | integer | Minimum rating |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max result pages per product |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/pbtech-co-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `code` | string |
| `name` | string |
| `url` | string |
| `price` | integer |
| `originalPrice` | null |
| `currency` | string |
| `reviewCount` | integer |
| `specifications` | object |
| `promotion` | string |
| `imageUrl` | null |
| `discountPercent` | null |
| `searchMode` | string |
| `specialsCategory` | null |
| `source` | string |
| `sku` | string |
| `mpn` | string |
| `gtin` | string |
| `brand` | string |
| `description` | string |
| `images` | list |
| `rating` | float |
| `basePrice` | integer |
| `availability` | string |
| `condition` | string |
| `priceValidUntil` | string |
| `seller` | string |
| `categories` | list |
| `specificationsText` | string |
| `storeStock` | list |
| `totalStoreStock` | integer |
| `ratingBreakdown` | object |

---

[← All scrapers](../../README.md)
