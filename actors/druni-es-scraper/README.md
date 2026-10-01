# druni.es Scraper

Scrape Druni beauty, cosmetics and perfume products. Search by keyword, category, Ofertas Flash deals or paste product and listing URLs. Extract prices, original prices, discounts, images, product details, and format or colour variants with individual prices and availability.

**[Open druni.es Scraper on Apify](https://apify.com/abotapi/druni-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~druni-es-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "perfume mujer", "sortBy": "RELEVANCE", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword |
| `category` | string | Category |
| `sortBy` | string | Sort order |
| `urls` | array | URLs to scrape |
| `specialsOnly` | boolean | Ofertas Flash only |
| `brands` | array | Brands |
| `minPrice` | number | Minimum price (EUR) |
| `maxPrice` | number | Maximum price (EUR) |
| `fetchDetails` | boolean | Fetch full product detail |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/druni-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `sku` | string |
| `name` | string |
| `brand` | string |
| `category` | string |
| `url` | string |
| `price` | float |
| `currency` | string |
| `originalPrice` | null |
| `discountAmount` | null |
| `discountPercent` | null |
| `isOnSpecial` | boolean |
| `promoLabel` | null |
| `packSizes` | null |
| `onlineAvailable` | boolean |
| `image` | string |
| `features` | list |
| `reviews` | object |

---

[← All scrapers](../../README.md)
