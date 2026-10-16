# Carrefour Spain Scraper

Scrape Carrefour Spain (carrefour.es) products. Search by keyword, browse a category, or paste product/category links. Returns name, brand, price, unit price, promotion, stock, category, image, and, with details, the barcode (EAN), ingredients, allergens, nutrition, extra images and rating.

**[Open Carrefour Spain Scraper on Apify](https://apify.com/abotapi/carrefour-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~carrefour-es-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["leche"], "categories": ["https://www.carrefour.es/supermercado/lacteos-huevos/leche/cat20093/c", "Vinos"], "sortBy": "relevance", "minRating": "0", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "ES"}, "maxResults": 10}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `categories` | array | Category links |
| `urls` | array | Carrefour Spain links or product ids |
| `products` | array | Product links or ids (legacy) |
| `sortBy` | string | Sort by |
| `minRating` | string | Minimum average rating |
| `onPromotionOnly` | boolean | Only products on promotion |
| `inStockOnly` | boolean | Only products in stock |
| `minPrice` | integer | Minimum price (EUR) |
| `maxPrice` | integer | Maximum price (EUR) |
| `brands` | array | Brands |
| `fetchDetails` | boolean | Fetch product details |
| `maxReviews` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per keyword / category |
| `proxy` | object | Proxy configuration |
| `searchQuery` | string | Search keyword (alternative name) |
| `searchQueries` | array | Search keywords (alternative name) |
| `categoryUrl` | string | Category link (alternative name) |
| `categoryUrls` | array | Category links (alternative name) |
| `startUrls` | array | Start URLs (alternative name) |
| `productUrls` | array | Product links (alternative name) |
| `maxResults` | integer | Max results (alternative name) |
| `maxResultsPerScrape` | integer | Max results per run (alternative name) |
| `promotionsOnly` | boolean | Only promotions (alternative name) |
| `proxyConfiguration` | object | Proxy configuration (alternative name) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/carrefour-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `name` | string |
| `brand` | string |
| `ean` | string |
| `price` | float |
| `currency` | string |
| `measureUnit` | string |
| `categoryId` | string |
| `image` | string |
| `url` | string |
| `source` | string |
| `unitPrice` | float |
| `unitPriceMeasure` | string |
| `packSize` | string |
| `searchMode` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
