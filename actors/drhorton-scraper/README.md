# DR Horton Scraper

Extract new-home data from drhorton.com, America’s largest homebuilder. Pull communities and quick move-in homes by state with prices, payment estimates, floor plans, square footage, amenities, and map coordinates.

**[Open DR Horton Scraper on Apify](https://apify.com/abotapi/drhorton-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~drhorton-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "states": ["Texas"], "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `states` | array | States |
| `state` | string | State (single, alias) |
| `includeCommunities` | boolean | Include communities |
| `includeQmiHomes` | boolean | Include quick move-in homes |
| `includeFloorPlans` | boolean | Include floor plans (detail crawl) |
| `minPrice` | integer | Min price (USD) |
| `maxPrice` | integer | Max price (USD) |
| `minBedrooms` | integer | Min bedrooms |
| `minBathrooms` | number | Min bathrooms |
| `minSqft` | integer | Min square feet |
| `maxSqft` | integer | Max square feet |
| `minGarages` | integer | Min garage spaces |
| `minStories` | integer | Min stories |
| `propertyType` | string | Property type contains |
| `series` | string | Series / brand contains |
| `startUrls` | array | URLs |
| `maxItems` | integer | Max records |
| `proxy` | object | Proxy |
| `maxResidentialMB` | integer | Residential traffic budget (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/drhorton-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `state` | string |
| `communityName` | string |
| `brand` | string |
| `propertyType` | string |
| `address` | string |
| `city` | string |
| `url` | string |
| `imageUrl` | string |
| `sellingStatus` | string |
| `statusColor` | string |
| `availableHomes` | integer |
| `latitude` | float |
| `longitude` | float |
| `minBeds` | integer |
| `maxBeds` | integer |
| `minBaths` | integer |
| `maxBaths` | float |
| `minCars` | integer |
| `maxCars` | integer |
| `minStories` | integer |
| `maxStories` | integer |
| `minSqft` | integer |
| `maxSqft` | integer |
| `minPrice` | integer |
| `maxPrice` | integer |
| `callForPrice` | boolean |
| `amenities` | list |
| `badges` | null |
| `location` | object |
| `raw` | object |

---

[← All scrapers](../../README.md)
