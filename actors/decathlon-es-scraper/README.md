# Decathlon.es Scraper

Scrape Decathlon Spain (decathlon.es) sporting goods: current price plus strike-through discount, brand, seller, technical specifications, colour/size availability, GTINs, and reviews. Search by keyword/category with brand and price filters, or paste product and listing links.

**[Open Decathlon.es Scraper on Apify](https://apify.com/abotapi/decathlon-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~decathlon-es-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "zapatillas running", "sortBy": "RELEVANCE", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword |
| `category` | string | Category path |
| `brand` | string | Brand |
| `specialsOnly` | boolean | On sale only |
| `minPrice` | number | Minimum price (EUR) |
| `maxPrice` | number | Maximum price (EUR) |
| `sortBy` | string | Sort order |
| `urls` | array | URLs to scrape |
| `fetchDetails` | boolean | Fetch full product detail |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/decathlon-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `supermodelId` | string |
| `sku` | string |
| `name` | string |
| `brand` | string |
| `url` | string |
| `image` | string |
| `images` | list |
| `price` | float |
| `currency` | string |
| `originalPrice` | float |
| `discountPercent` | integer |
| `isOnSpecial` | boolean |
| `saleEndsAt` | string |
| `availableSizes` | list |
| `onlineAvailable` | boolean |
| `seller` | object |
| `sports` | list |
| `nature` | string |
| `rating` | float |
| `reviewCount` | integer |
| `reviews` | object |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
