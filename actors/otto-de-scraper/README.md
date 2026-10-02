# OTTO.de Scraper

Scrape OTTO.de products by search or URL. Extract prices, discounts, variants, availability, brand, seller, EAN/GTIN, specifications, categories, and customer reviews across fashion, furniture, electronics, and homeware.

**[Open OTTO.de Scraper on Apify](https://apify.com/abotapi/otto-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~otto-de-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "ecksofa", "sortBy": "RELEVANCE", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword or category name |
| `urls` | array | URLs to scrape |
| `specialsOnly` | boolean | Specials / offers only |
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

Full details on the [scraper page](https://apify.com/abotapi/otto-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `variationId` | string |
| `articleNumber` | string |
| `name` | string |
| `brand` | string |
| `url` | string |
| `image` | string |
| `images` | list |
| `price` | float |
| `currency` | string |
| `originalPrice` | integer |
| `discountPercent` | integer |
| `isOnSpecial` | boolean |
| `promoLabel` | string |
| `availability` | string |
| `availabilityText` | string |
| `rating` | integer |
| `reviewCount` | integer |
| `variants` | list |
| `category` | null |
| `seller` | null |
| `ean` | null |
| `gtin` | null |
| `sku` | null |
| `description` | null |
| `specs` | null |
| `breadcrumb` | null |
| `returnPolicy` | null |
| `reviews` | object |

---

[← All scrapers](../../README.md)
