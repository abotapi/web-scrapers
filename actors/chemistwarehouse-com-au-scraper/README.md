# Chemist Warehouse AU Scraper

Scrape chemistwarehouse.com.au products with prices, RRP, discounts, stock, images, ingredients, directions, warnings, categories, and full customer reviews. Search by keyword or product URLs, with brand, category, price, in-stock filters, and price sorting.

**[Open Chemist Warehouse AU Scraper on Apify](https://apify.com/abotapi/chemistwarehouse-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~chemistwarehouse-com-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["vitamin c"], "sort": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `queries` | array | Search keywords |
| `brand` | string | Brand |
| `category` | string | Category |
| `specialsCategory` | string | Specials / offers |
| `productUrls` | array | Product URLs |
| `minPrice` | integer | Minimum price (AUD) |
| `maxPrice` | integer | Maximum price (AUD) |
| `inStockOnly` | boolean | In-stock only |
| `sort` | string | Sort |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/chemistwarehouse-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `productKey` | string |
| `objectId` | string |
| `sku` | string |
| `epid` | integer |
| `name` | string |
| `title` | string |
| `slug` | string |
| `url` | string |
| `brand` | string |
| `manufacturer` | string |
| `productType` | string |
| `price` | float |
| `rrp` | float |
| `wasPrice` | float |
| `savingsAmount` | integer |
| `savingsPercent` | float |
| `discountPercent` | float |
| `isOnSpecial` | boolean |
| `promoLabel` | string |
| `currency` | string |
| `isInStock` | boolean |
| `isClickAndCollect` | boolean |
| `isFastDelivery` | boolean |
| `isInternationalShipping` | boolean |
| `isMarketplace` | boolean |
| `isShippable` | boolean |
| `isExpressDeliveryOnly` | boolean |
| `prescriptionType` | string |
| `schedule` | string |
| `isAppendixH` | boolean |
| `isInstantConsult` | null |
| `purchaseLimit` | null |
| `transactionLimit` | null |
| `isAdultProduct` | boolean |
| `isGenericBrand` | boolean |
| `quantity` | integer |
| `multipackQty` | integer |
| `rating` | float |
| `reviewCount` | integer |

---

[← All scrapers](../../README.md)
