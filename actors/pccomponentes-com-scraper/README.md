# PcComponentes Scraper

Scrape PcComponentes (pccomponentes.com) products: current price plus strike-through reference-price discount, configuration variants with price and availability, brand, category, and reviews with rating. Search by keyword/category or paste product and listing links.

**[Open PcComponentes Scraper on Apify](https://apify.com/abotapi/pccomponentes-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~pccomponentes-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "portatil", "sortBy": "RELEVANCE", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword |
| `category` | string | Category (used only when Search keywor |
| `brands` | array | Brands |
| `minPrice` | number | Minimum price (EUR) |
| `maxPrice` | number | Maximum price (EUR) |
| `specialsOnly` | boolean | Discounted items only |
| `sortBy` | string | Sort order (category browsing only) |
| `urls` | array | URLs to scrape |
| `fetchDetails` | boolean | Fetch full product detail |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/pccomponentes-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

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
| `price` | integer |
| `currency` | string |
| `originalPrice` | null |
| `discountAmount` | null |
| `discountPercent` | null |
| `isOnSpecial` | boolean |
| `image` | string |
| `rating` | float |
| `reviewCount` | integer |
| `onlineAvailable` | boolean |
| `freeShipping` | boolean |
| `reviews` | object |

---

[← All scrapers](../../README.md)
