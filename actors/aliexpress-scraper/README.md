# AliExpress Scraper

Scrape AliExpress products: search by keyword or category, or process pasted search, category and product URLs page by page. Identity, price, availability, media and SKU fields come from the results page; optional detail and reviews steps add variant tables, specifications, seller data and reviews.

**[Open AliExpress Scraper on Apify](https://apify.com/abotapi/aliexpress-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~aliexpress-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "shippingCountry": "us", "queries": ["airpods"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Run mode |
| `shippingCountry` | string | Target market |
| `queries` | array | Search keywords |
| `categoryId` | string | Category ID (optional) |
| `freeShippingOnly` | boolean | Free shipping only |
| `sortBy` | string | Sort order |
| `urls` | array | URLs |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `minRating` | integer | Minimum average rating |
| `reviewsOnly` | boolean | Output reviews only (instead of produc |
| `fetchReviews` | boolean | Include reviews on each product (slowe |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `fetchDetails` | boolean | Fetch full product detail (slower, not |
| `maxPages` | integer | Max result pages per query/URL |
| `maxListings` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/aliexpress-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

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
| `shippingCountry` | string |
| `currency` | string |
| `title` | string |
| `price` | float |
| `imageUrl` | string |
| `additionalImages` | list |
| `scrapedAt` | string |
| `productType` | string |
| `currentPrice` | float |
| `isSponsored` | boolean |
| `primaryImage` | string |
| `imageGallery` | list |
| `categoryId` | string |
| `raw` | object |
| `fetchedAt` | string |

---

[← All scrapers](../../README.md)
