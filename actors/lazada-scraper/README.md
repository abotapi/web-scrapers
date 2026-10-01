# Lazada Scraper

Scrape Lazada products and reviews across SEA markets, including Malaysia, Singapore, Indonesia, Philippines, Thailand, and Vietnam. Extract structured data on pricing, inventory, ratings, sellers, media, and reviews. Ideal for cross-region analysis with consistent, analytics-ready output.

**[Open Lazada Scraper on Apify](https://apify.com/abotapi/lazada-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~lazada-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "country": "sg", "queries": ["laptop"], "sortBy": "popularity", "maxReviewsPerProduct": 10, "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "SG"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Run mode |
| `country` | string | Country site |
| `queries` | array | Search queries |
| `categoryId` | string | Category ID (deprecated, no verified e |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `specialsOnly` | boolean | Flash Sale only |
| `sortBy` | string | Sort order |
| `urls` | array | URLs |
| `minRating` | integer | Minimum average rating |
| `freeShippingOnly` | boolean | Free shipping only |
| `reviewsOnly` | boolean | Output reviews only (instead of produc |
| `fetchReviews` | boolean | Include reviews on each product |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `fetchDetails` | boolean | Enrich each product with detail page d |
| `maxPages` | integer | Max SERP pages per query/URL |
| `maxListings` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/lazada-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `id` | string |
| `url` | string |
| `productName` | string |
| `productId` | string |
| `productUrl` | string |
| `sourceUrl` | string |
| `seedType` | string |
| `seedValue` | string |
| `country` | string |
| `currency` | string |
| `currentPrice` | integer |
| `originalPrice` | integer |
| `discountText` | string |
| `discountPct` | integer |
| `isOnSpecial` | boolean |
| `discountAmount` | integer |
| `promoLabel` | string |
| `specialsCategory` | string |
| `ratingScore` | float |
| `reviewCount` | integer |
| `itemSold` | string |
| `inStock` | boolean |
| `isSponsored` | boolean |
| `freeShipping` | boolean |
| `sellerName` | string |
| `sellerId` | string |
| `primaryImage` | string |
| `raw` | object |
| `fetchedAt` | string |

---

[← All scrapers](../../README.md)
