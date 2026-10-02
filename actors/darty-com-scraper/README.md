# Darty Scraper

Scrape Darty (darty.com) products: current price plus strike-through reference price and discount, brand, category breadcrumb, full spec sheet, and the site's own customer reviews with rating breakdown. Search by keyword or paste product/listing links.

**[Open Darty Scraper on Apify](https://apify.com/abotapi/darty-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~darty-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "television", "sortBy": "RELEVANCE", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "FR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword |
| `minRating` | integer | Minimum rating |
| `freeDeliveryOnly` | boolean | Free delivery only |
| `sortBy` | string | Sort order |
| `urls` | array | URLs to scrape |
| `brands` | array | Brands |
| `minPrice` | number | Minimum price (EUR) |
| `maxPrice` | number | Maximum price (EUR) |
| `specialsOnly` | boolean | Discounted items only |
| `fetchDetails` | boolean | Fetch full product detail |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/darty-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `ean` | null |
| `url` | string |
| `image` | string |
| `name` | string |
| `brand` | string |
| `category` | string |
| `price` | float |
| `currency` | string |
| `originalPrice` | integer |
| `discountAmount` | float |
| `discountPercent` | integer |
| `isOnSpecial` | boolean |
| `promoLabel` | string |
| `rating` | integer |
| `reviewCount` | integer |
| `inStock` | boolean |
| `condition` | string |
| `seller` | string |
| `reviews` | object |

---

[← All scrapers](../../README.md)
