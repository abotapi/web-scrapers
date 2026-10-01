# E.Leclerc Scraper

Scrape E.Leclerc France (e.leclerc) grocery and retail products. Search by keyword or category, or paste product and category links. Pick a store by postal code so prices and stock are the real ones for that store. Returns price, unit price, stock, promotions, rating and images.

**[Open E.Leclerc Scraper on Apify](https://apify.com/abotapi/leclerc-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~leclerc-fr-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"postalCode": "75014", "mode": "search", "queries": ["lait"], "sortBy": "relevance", "minRating": "0", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `postalCode` | string | Postal code |
| `storeSignCode` | string | Store sign code (optional override) |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `categories` | array | Category links |
| `urls` | array | E.Leclerc links or EANs |
| `sortBy` | string | Sort by |
| `minRating` | string | Minimum average rating |
| `onPromotionOnly` | boolean | Only products on promotion |
| `inStockOnly` | boolean | Only products in stock |
| `minPrice` | integer | Minimum price (EUR) |
| `maxPrice` | integer | Maximum price (EUR) |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per keyword / category / lin |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/leclerc-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `ean` | string |
| `title` | string |
| `brand` | string |
| `unitPrice` | float |
| `unitPriceUnit` | string |
| `unitPriceDisplay` | string |
| `rating` | float |
| `reviewCount` | integer |
| `canonicalUrl` | string |
| `source` | string |
| `descriptionHtml` | string |
| `description` | string |
| `images` | list |
| `categoryPath` | string |
| `price` | float |
| `currency` | string |
| `availabilityStatus` | string |
| `inStock` | boolean |
| `stock` | integer |
| `warehouse` | string |
| `onPromotion` | boolean |
| `reviews` | list |
| `storeSignCode` | string |
| `storeName` | string |
| `storePostalCode` | string |
| `searchMode` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
