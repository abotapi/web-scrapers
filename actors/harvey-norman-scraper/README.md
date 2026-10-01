# Harvey Norman Scraper

Scrape Harvey Norman Australia products: name, brand, price, was-price / discount, specifications, image gallery, GTIN, department, stock, dimensions, rating and customer reviews. Search by keyword with brand, price and rating filters, or paste product / listing URLs.

**[Open Harvey Norman Scraper on Apify](https://apify.com/abotapi/harvey-norman-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~harvey-norman-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["oled tv"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `specialsCategory` | string | Specials / offers category |
| `urls` | array | Harvey Norman URLs |
| `brand` | string | Brand |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `minRating` | integer | Minimum rating |
| `sortBy` | string | Sort by |
| `detailEnrichment` | boolean | Fetch full product detail  reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per listing |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/harvey-norman-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | integer |
| `sku` | string |
| `uid` | null |
| `name` | string |
| `brand` | null |
| `url` | string |
| `imageUrl` | null |
| `rating` | float |
| `reviewCount` | integer |
| `promotion` | null |
| `searchMode` | string |
| `source` | string |
| `price` | integer |
| `currency` | string |
| `wasPrice` | null |
| `discountAmount` | integer |
| `discountPercent` | integer |
| `title` | string |
| `isOnSpecial` | boolean |

---

[← All scrapers](../../README.md)
