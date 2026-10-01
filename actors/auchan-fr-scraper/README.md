# Auchan France Scraper

Scrape Auchan.fr products: grocery, drinks, household and general merchandise. Real price scoped to your drive/delivery point, genuine was-price and discount % when on offer, unit price, brand, shopper ratings and reviews. Search by keyword or paste product/search/category links.

**[Open Auchan France Scraper on Apify](https://apify.com/abotapi/auchan-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~auchan-fr-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "postalCode": "75001", "deliveryMode": "drive", "searchTerm": "lait", "sortBy": "RELEVANCE", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `postalCode` * | string | Postal code or city |
| `deliveryMode` | string | Delivery mode |
| `searchTerm` | string | Search keyword |
| `brand` | string | Brand |
| `specialsOnly` | boolean | On offer only |
| `sortBy` | string | Sort order |
| `urls` | array | URLs to scrape |
| `fetchDetails` | boolean | Fetch product detail (breadcrumb, EAN, |
| `maxPages` | integer | Max search pages |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/auchan-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `title` | string |
| `brand` | string |
| `packSize` | string |
| `productUrl` | string |
| `price` | float |
| `currency` | string |
| `unitPrice` | float |
| `unitOfMeasure` | string |
| `wasPrice` | null |
| `discountAmount` | null |
| `discountPercent` | null |
| `isOnSpecial` | boolean |
| `loyaltyCashbackPercent` | null |
| `availability` | string |
| `deliveryPromise` | string |
| `deliveryChannel` | string |
| `stock` | integer |
| `averageRating` | float |
| `reviewCount` | integer |
| `images` | list |
| `categoryPath` | null |
| `category` | null |
| `ean` | null |
| `reviews` | object |

---

[← All scrapers](../../README.md)
