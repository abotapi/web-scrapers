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
  -d '{"mode": "search", "queries": ["leche"], "sortBy": "relevance", "minRating": "0", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "ES"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `categories` | array | Category links |
| `urls` | array | Carrefour Spain links or product ids |
| `sortBy` | string | Sort by |
| `minRating` | string | Minimum average rating |
| `onPromotionOnly` | boolean | Only products on promotion |
| `inStockOnly` | boolean | Only products in stock |
| `minPrice` | integer | Minimum price (EUR) |
| `maxPrice` | integer | Maximum price (EUR) |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per keyword / category |
| `proxy` | object | Proxy configuration |

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
| `searchMode` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
