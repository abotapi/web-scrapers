# ROSSMANN.de Scraper

Scrape ROSSMANN (rossmann.de) drugstore products: current + original strike-through price with discount, per-unit pricing (per 100ml/kg/piece), brand, stock and promo badges, plus full reviews with rating breakdown. Search by keyword, category or Angebote/online-only specials, or paste links.

**[Open ROSSMANN.de Scraper on Apify](https://apify.com/abotapi/rossmann-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~rossmann-de-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "nivea duschgel", "sortBy": "RELEVANCE", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword |
| `category` | string | Category code (optional) |
| `specialsCategory` | string | Specials category |
| `brands` | array | Brands |
| `minRating` | integer | Minimum rating |
| `sortBy` | string | Sort order |
| `urls` | array | URLs to scrape |
| `fetchDetails` | boolean | Fetch full product detail |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/rossmann-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `ean` | string |
| `sku` | string |
| `name` | string |
| `brand` | string |
| `url` | string |
| `price` | float |
| `currency` | string |
| `originalPrice` | null |
| `originalPriceCurrency` | null |
| `discountAmount` | null |
| `discountPercent` | null |
| `promotionLabel` | null |
| `isOnSpecial` | boolean |
| `badges` | list |
| `disruptors` | list |
| `unitPrice` | float |
| `unitPriceCurrency` | string |
| `unitPriceUnit` | string |
| `unitPriceBasisSize` | integer |
| `packagingAmount` | integer |
| `packagingUnit` | string |
| `rating` | float |
| `reviewCount` | integer |
| `isRateable` | boolean |
| `image` | string |
| `imageAlt` | string |
| `stockLevelStatus` | string |
| `salesChannel` | string |
| `hasPriceHidden` | boolean |
| `minOrderAmount` | integer |
| `maxOrderAmount` | integer |
| `orderIncrement` | integer |
| `variants` | list |
| `legalNotes` | list |
| `reviews` | object |

---

[← All scrapers](../../README.md)
