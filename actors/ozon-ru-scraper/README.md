# Ozon.ru Scraper

Extract structured product data from Ozon.ru, Russia’s largest marketplace. Search by keyword or use product, category, and seller URLs. Get clean JSON with 40+ fields, including prices, discounts, ratings, specs, variants, images, current seller, buybox sellers, and reviews.

**[Open Ozon.ru Scraper on Apify](https://apify.com/abotapi/ozon-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~ozon-ru-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["iphone 15"], "sortBy": "score", "maxReviewsPerProduct": 10, "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Run mode |
| `queries` | array | Search queries |
| `sortBy` | string | Sort order |
| `urls` | array | URLs |
| `minPrice` | integer | Min price (RUB) |
| `maxPrice` | integer | Max price (RUB) |
| `minRating` | integer | Minimum average rating |
| `scrapeProductDetails` | boolean | Scrape full product details |
| `fetchBuybox` | boolean | Track competing sellers (buybox) |
| `fetchSellerDetails` | boolean | Enrich seller profile |
| `fetchReviews` | boolean | Attach reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per query / URL |
| `maxListings` | integer | Max products (total) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/ozon-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `sku` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `price` | integer |
| `originalPrice` | integer |
| `discountPercent` | integer |
| `currency` | string |
| `rating` | integer |
| `reviewCount` | integer |
| `questionCount` | integer |
| `availability` | string |
| `coverImage` | string |
| `images` | list |
| `description` | null |
| `specs` | list |
| `hashtags` | list |
| `ratingBreakdown` | null |
| `variants` | list |
| `categoryPath` | string |
| `sellerName` | string |
| `sellerId` | string |
| `seller` | object |
| `otherSellersCount` | integer |
| `otherSellersMinPrice` | integer |
| `buyboxSellers` | list |
| `reviews` | list |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
