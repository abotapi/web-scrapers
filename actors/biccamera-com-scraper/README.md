# Bic Camera Scraper

Scrape Bic Camera (biccamera.com) products: JPY price, list price and discount, Bic Point amount and rate, stock and delivery, spec table, image gallery, colour and capacity variants, plus review text with author, date, star rating and variant reviewed. Search by keyword, category or pasted links.

**[Open Bic Camera Scraper on Apify](https://apify.com/abotapi/biccamera-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~biccamera-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["カメラ"], "sortBy": "RELEVANCE", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["UNBLOCKER"], "apifyProxyCountry": "JP"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search keywords |
| `category` | string | Category (optional) |
| `brand` | string | Brand (optional) |
| `sortBy` | string | Sort order |
| `includeDiscontinued` | boolean | Include discontinued products |
| `groupVariations` | boolean | Group colour and capacity variations |
| `urls` | array | URLs to scrape |
| `minPrice` | integer | Minimum price (JPY) |
| `maxPrice` | integer | Maximum price (JPY) |
| `inStockOnly` | boolean | In-stock products only |
| `fetchDetails` | boolean | Fetch full product detail |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max result pages per search |
| `maxItems` | integer | Max products total |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/biccamera-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `itemId` | string |
| `title` | string |
| `brand` | string |
| `url` | string |
| `price` | integer |
| `currency` | string |
| `pointAmount` | integer |
| `pointRate` | integer |
| `effectivePrice` | integer |
| `rating` | float |
| `reviewCount` | integer |
| `thumbnail` | string |
| `images` | list |
| `deliveryText` | string |
| `arrivalDate` | string |
| `freeShipping` | boolean |
| `availabilityText` | null |
| `inStock` | boolean |
| `usedPrice` | null |
| `usedOfferCount` | null |
| `isSponsored` | boolean |
| `rank` | integer |
| `variant` | null |
| `source` | string |
| `reviews` | object |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
