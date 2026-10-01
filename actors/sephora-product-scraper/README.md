# Sephora Scraper

Scrape Sephora products across 21+ storefronts (US, AU, NZ, SG, MY, ID, TH, PH, MX, DE, RO, SE, GR, DK) with a unified schema. Extract brand, title, ingredients, claims, full SKU and shade variants, ratings histogram, top reviews, Q&A, and rich media.

**[Open Sephora Scraper on Apify](https://apify.com/abotapi/sephora-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~sephora-product-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "storefront": "us", "queries": ["foundation"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxPages": 1, "maxProducts": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Input mode |
| `storefront` | string | Storefront |
| `queries` | array | Search queries |
| `categories` | array | Category slugs |
| `sortBy` | string | Sort order |
| `specialsOnly` | boolean | Specials (Sale) only |
| `urls` | array | Sephora URLs |
| `brands` | array | Filter by brand (optional) |
| `priceMin` | integer | Minimum price |
| `priceMax` | integer | Maximum price |
| `ratingMin` | integer | Minimum rating |
| `newOnly` | boolean | New arrivals only |
| `exclusiveOnly` | boolean | Sephora exclusives only |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch top reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `fetchQna` | boolean | Fetch top Q&A |
| `maxQnaPerProduct` | integer | Max Q&A per product |
| `maxPages` | integer | Max pages per query |
| `maxProducts` | integer | Max products total |
| `proxyConfiguration` | object | Proxy configuration |
| `resumeFromCheckpoint` | boolean | Resume from checkpoint |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/sephora-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `market` | string |
| `source` | object |
| `brand` | string |
| `title` | string |
| `isNewArrival` | boolean |
| `frontend` | string |
| `priceText` | null |
| `thumbnail` | string |
| `rating` | float |
| `reviewCount` | integer |
| `highlights` | list |
| `categories` | list |
| `medias` | list |
| `variants` | list |
| `options` | list |
| `isOnSpecial` | boolean |
| `wasPrice` | null |
| `savingsAmount` | null |
| `savingsPercent` | null |
| `soldOut` | null |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
