# Thalia.de Scraper

Scrape Thalia.de books, eBooks, audiobooks, toys and stationery. Search by keyword or category, browse Schnäppchen deals, or paste product and listing URLs. Get prices, original prices, discounts, ISBN/EAN, author, publisher, format, ratings and full reviews.

**[Open Thalia.de Scraper on Apify](https://apify.com/abotapi/thalia-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~thalia-de-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "krimi", "sortBy": "sfmd", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword |
| `category` | string | Category ID (optional) |
| `urls` | array | URLs to scrape |
| `specialsOnly` | boolean | Specials only (Schnäppchen) |
| `einband` | array | Format / binding |
| `minPrice` | integer | Minimum price (EUR) |
| `maxPrice` | integer | Maximum price (EUR) |
| `availability` | string | Availability filter |
| `sortBy` | string | Sort order |
| `fetchDetails` | boolean | Fetch full product detail |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/thalia-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `title` | string |
| `authors` | list |
| `url` | string |
| `image` | string |
| `price` | float |
| `currency` | string |
| `originalPrice` | float |
| `discountAmount` | integer |
| `discountPercent` | float |
| `isOnSpecial` | boolean |
| `badges` | list |
| `promoLabel` | null |
| `format` | string |
| `hasMoreFormats` | boolean |
| `categoryPath` | list |
| `availabilityText` | string |
| `availabilityStatus` | null |
| `rating` | integer |
| `reviewCount` | integer |
| `reviews` | object |

---

[← All scrapers](../../README.md)
