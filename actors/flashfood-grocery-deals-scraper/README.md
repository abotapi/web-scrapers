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
  -d '{"mode": "search", "locations": ["Detroit, Michigan"], "storeInputs": ["https://app.shopper.flashfood.com/api/v1/stores/629cec56061cc242985326fd", "https://app.shopper.flashfood.com/api/v1/items/?storeIds=629cec56061cc242985326fd", "https://app.shopper.flashfood.com/api/v1/stores?latitude=42.33&longitude=-83.04&maxDistance=10000", "https://flashfood.com/en/locations", "629cec56061cc242985326fd"], "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `radiusKm` | integer | Radius (km) |
| `countries` | array | Countries |
| `banners` | array | Store chains (banners) |
| `keywords` | array | Keywords |
| `departments` | array | Departments |
| `minDiscountPercent` | integer | Minimum discount (%) |
| `maxPrice` | string | Maximum price |
| `expiringWithinDays` | integer | Best before within (days) |
| `maxStores` | integer | Max stores |
| `fullNetwork` | boolean | Network sweep |
| `storesOnly` | boolean | Store records only |
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
| `apiUrl` | string |
| `title` | string |
| `name` | string |
| `gtin` | string |
| `price` | float |
| `originalPrice` | float |
| `discountPercent` | integer |
| `savings` | float |
| `daysToExpiry` | integer |
| `currency` | string |
| `quantityAvailable` | integer |
| `bestBefore` | string |
| `department` | string |
| `departmentFr` | string |
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
| `distanceKm` | integer |
| `scrapedAt` | string |
| `queryLocation` | string |

---

[← All scrapers](../../README.md)
