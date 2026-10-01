# Douglas Germany Scraper

Scrape Douglas.de beauty and fragrance products by keyword, category, brand, or URL. Extract brands, current and original prices, discounts, unit prices, size variants, stock, images, ratings, reviews, ingredients, and specifications.

**[Open Douglas Germany Scraper on Apify](https://apify.com/abotapi/douglas-de?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~douglas-de/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["parfum"], "category": "01", "gender": "any", "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "DE"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Input mode |
| `queries` | array | Search keywords |
| `category` | string | Category |
| `brand` | string | Brand |
| `gender` | string | Gender filter |
| `sortBy` | string | Sort order |
| `promoFlags` | array | Promotion flags |
| `urls` | array | Douglas URLs |
| `priceMin` | number | Minimum price (EUR) |
| `priceMax` | number | Maximum price (EUR) |
| `specialsOnly` | boolean | Discounted products only |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search/URL |
| `maxItems` | integer | Max products total |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/douglas-de?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `sku` | string |
| `title` | string |
| `variantLabel` | string |
| `url` | string |
| `brand` | object |
| `brandLine` | string |
| `productFamily` | string |
| `productType` | string |
| `isMarketplace` | boolean |
| `breadcrumbs` | list |
| `price` | object |
| `unitPrice` | object |
| `isOnSpecial` | boolean |
| `wasPrice` | float |
| `savingsAmount` | float |
| `savingsPercent` | float |
| `promoLabel` | string |
| `availability` | object |
| `variants` | list |
| `images` | list |
| `description` | string |
| `characteristics` | list |
| `rating` | float |
| `ratingStars` | null |
| `reviewCount` | null |
| `ean` | string |
| `ratingBreakdown` | list |
| `reviews` | list |
| `ingredients` | string |
| `howToUse` | string |
| `specifications` | object |
| `reviewSummary` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
