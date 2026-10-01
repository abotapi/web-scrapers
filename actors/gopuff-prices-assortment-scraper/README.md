# Gopuff Scraper

Scrape Gopuff, the US quick-commerce delivery store, by location or product: prices, promotions, stock and availability per fulfillment location across thousands of everyday products. Availability monitoring (NEW, UPDATED, REAPPEARED, EXPIRED), detail enrichment, incremental runs, MCP export.

**[Open Gopuff Scraper on Apify](https://apify.com/abotapi/gopuff-prices-assortment-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~gopuff-prices-assortment-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "categories", "locations": ["78701"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `locations` | array | Locations |
| `locationId` | string | Storefront location id (advanced) |
| `categoryInputs` | array | Collections (optional) |
| `discoverCategories` | boolean | Walk the whole navigation |
| `inStockOnly` | boolean | Only items in stock |
| `productInputs` | array | Product links or ids |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per collection |
| `pageSize` | integer | Page size |
| `fetchDetails` | boolean | Enrich from product documents |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/gopuff-prices-assortment-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `productId` | string |
| `url` | string |
| `title` | string |
| `price` | float |
| `currency` | string |
| `availability` | string |
| `quantityAvailable` | integer |
| `locationId` | string |
| `categoryId` | string |
| `sizeLabel` | string |
| `hasPromotion` | boolean |
| `pricePerUnitUsd` | float |
| `unit` | string |
| `snapEligible` | boolean |
| `imageUrl` | string |
| `priceChannel` | string |

---

[← All scrapers](../../README.md)
