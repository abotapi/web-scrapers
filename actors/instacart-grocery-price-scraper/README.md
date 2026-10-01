# Instacart Scraper

Scrape Instacart grocery catalogs with per-store prices. Run keywords across several stores at once to compare what each banner charges, discover every store serving a US location, or paste Instacart links. Returns name, brand, size, price, regular price, unit price, stock and full store detail.

**[Open Instacart Scraper on Apify](https://apify.com/abotapi/instacart-grocery-price-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~instacart-grocery-price-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["organic milk"], "retailers": ["costco", "safeway"], "postalCode": "10001", "sortBy": "bestMatch", "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `retailers` | array | Stores to search |
| `urls` | array | Instacart links or product ids |
| `includeDepartments` | boolean | Include each store's departments |
| `postalCode` | string | US postal code |
| `latitude` | number | Latitude (optional, advanced) |
| `longitude` | number | Longitude (optional, advanced) |
| `sortBy` | string | Sort by |
| `inStockOnly` | boolean | Only products in stock |
| `onSaleOnly` | boolean | Only products on sale |
| `minPrice` | integer | Minimum price (USD) |
| `maxPrice` | integer | Maximum price (USD) |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max products |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/instacart-grocery-price-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `itemId` | string |
| `productId` | string |
| `name` | string |
| `brand` | string |
| `size` | string |
| `priceString` | string |
| `price` | float |
| `pricingUnit` | string |
| `onSale` | boolean |
| `available` | boolean |
| `stockLevel` | string |
| `stockLevelLabel` | string |
| `image` | string |
| `dietaryAttributes` | string |
| `tags` | list |
| `retailerName` | string |
| `retailerSlug` | string |
| `retailerId` | string |
| `shopId` | string |
| `storeLocationId` | string |
| `serviceType` | string |
| `storeAddress` | string |
| `productUrl` | string |
| `searchQuery` | string |
| `sourceUrl` | string |
| `recordId` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
