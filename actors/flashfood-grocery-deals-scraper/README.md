# Flashfood Scraper

Scrape Flashfood discounted groceries and stores by location or store. Extract current and original prices, savings, quantity, best-before date, department, and store details. Track NEW, UPDATED, REAPPEARED, and EXPIRED items with incremental runs, resume, and MCP export.

**[Open Flashfood Scraper on Apify](https://apify.com/abotapi/flashfood-grocery-deals-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~flashfood-grocery-deals-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Detroit, Michigan"], "storeInputs": ["629cec56061cc242985326fd"], "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `radiusKm` | integer | Radius (km) |
| `storeInputs` | array | Store links or ids |
| `urls` | array | Store links or ids (alias) |
| `maxItems` | integer | Max items |
| `includeStores` | boolean | Also return store records |
| `countryHint` | string | Currency hint (optional) |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/flashfood-grocery-deals-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `itemId` | string |
| `url` | string |
| `title` | string |
| `price` | float |
| `originalPrice` | integer |
| `discountPercent` | integer |
| `currency` | string |
| `quantityAvailable` | integer |
| `bestBefore` | string |
| `department` | string |
| `legacyDepartment` | string |
| `imageUrl` | string |
| `imageGallery` | list |
| `listedAt` | string |
| `isSnapEligible` | boolean |
| `storageTreatment` | string |
| `raw` | object |
| `storeId` | string |
| `storeName` | string |
| `banner` | string |
| `street` | string |
| `city` | string |
| `stateCode` | string |
| `country` | string |
| `countryCode` | string |
| `latitude` | float |
| `longitude` | float |

---

[← All scrapers](../../README.md)
