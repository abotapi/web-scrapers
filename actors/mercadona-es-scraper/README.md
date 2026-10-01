# Mercadona Scraper

Scrape Mercadona products by delivery-area postal code. Search by keyword or category, or paste product and category URLs. Get local availability, current price, site-calculated price per kg, litre or unit, plus original price and discount when an item is on sale.

**[Open Mercadona Scraper on Apify](https://apify.com/abotapi/mercadona-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~mercadona-es-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "postalCode": "28001", "category": "Aceite, vinagre y sal", "searchTerm": "aceite de oliva", "sortBy": "RELEVANCE", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `postalCode` * | string | Postal code |
| `category` | string | Category |
| `urls` | array | URLs to scrape |
| `searchTerm` | string | Search keyword |
| `specialsOnly` | boolean | Discounted only |
| `brands` | array | Brands |
| `minPrice` | number | Minimum price (EUR) |
| `maxPrice` | number | Maximum price (EUR) |
| `sortBy` | string | Sort order |
| `fetchDetails` | boolean | Fetch full product detail |
| `maxPages` | integer | Max categories per search |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/mercadona-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `slug` | string |
| `name` | string |
| `packaging` | string |
| `categoryPath` | list |
| `category` | string |
| `url` | string |
| `image` | string |
| `price` | float |
| `currency` | string |
| `previousPrice` | float |
| `discountAmount` | float |
| `discountPercent` | float |
| `isOnSpecial` | boolean |
| `unitPrice` | float |
| `unitPriceFormat` | string |
| `packageSize` | integer |
| `packageSizeFormat` | string |
| `isPack` | boolean |
| `hasUnitSelector` | boolean |
| `onlineAvailable` | boolean |
| `isWater` | boolean |
| `requiresAgeCheck` | boolean |
| `maxQuantityPerOrder` | integer |
| `isNewArrival` | boolean |
| `reviews` | list |

---

[← All scrapers](../../README.md)
