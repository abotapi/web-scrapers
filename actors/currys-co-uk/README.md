# Currys UK Scraper

Scrape Currys UK electronics by keyword or URL. Extract prices, brands, stock status, EANs, descriptions, full image galleries and customer reviews. Supports automatic forward pagination for efficient catalogue scraping.

**[Open Currys UK Scraper on Apify](https://apify.com/abotapi/currys-co-uk?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~currys-co-uk/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["tv"], "sortBy": "Relevance", "maxReviewsPerProduct": 10, "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "GB"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `queries` | array | Search keywords (Search mode) |
| `minPrice` | integer | Min price (GBP) |
| `maxPrice` | integer | Max price (GBP) |
| `inStockOnly` | boolean | In-stock only |
| `sortBy` | string | Sort order |
| `urls` | array | Search URLs (URL mode) |
| `fetchDetails` | boolean | Visit each product's detail page |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max total products |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/currys-co-uk?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `sku` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `price` | float |
| `wasPrice` | float |
| `discount` | integer |
| `discountPercent` | integer |
| `currency` | string |
| `availabilityStatus` | string |
| `categories` | list |
| `ean` | string |
| `rating` | float |
| `reviewCount` | integer |
| `description` | string |
| `images` | list |
| `priceValidUntil` | string |
| `carePlans` | list |
| `financeOptions` | list |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
