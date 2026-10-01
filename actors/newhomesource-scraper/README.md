# NewHomeSource Scraper

Scrape new homes, floor plans, builders and communities from NewHomeSource.com. Search by US state or city, or paste URLs. Get prices, beds, baths, stories, garage, square footage, builder, location, amenities, community details and available plans.

**[Open NewHomeSource Scraper on Apify](https://apify.com/abotapi/newhomesource-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~newhomesource-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "state": "Alabama", "homeTypes": ["floorplan", "qmi"], "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `state` | string | State |
| `city` | string | City (optional) |
| `urls` | array | NewHomeSource links |
| `homeTypes` | array | Home types to include |
| `minPrice` | integer | Minimum price (USD) |
| `maxPrice` | integer | Maximum price (USD) |
| `minBedrooms` | integer | Minimum bedrooms |
| `minBathrooms` | integer | Minimum bathrooms |
| `minSqft` | integer | Minimum home size (sq ft) |
| `maxSqft` | integer | Maximum home size (sq ft) |
| `fetchDetails` | boolean | Fetch full home details |
| `maxItems` | integer | Max items (per run, 0  unlimited) |
| `maxPages` | integer | Max pages per scope (0  unlimited) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/newhomesource-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `homeId` | integer |
| `planId` | integer |
| `specId` | integer |
| `listingId` | integer |
| `listingNumber` | string |
| `floorPlan` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `halfBathrooms` | integer |
| `garageCount` | integer |
| `stories` | integer |
| `homeSizeSqft` | integer |
| `homePrice` | integer |
| `address` | string |
| `city` | string |
| `county` | string |
| `state` | string |
| `zip` | string |
| `latitude` | string |
| `longitude` | string |
| `moveInDate` | null |
| `dateFirstPublished` | string |
| `status` | string |
| `homeType` | string |
| `isSpec` | boolean |
| `specNumber` | null |
| `isHotHome` | boolean |
| `isLuxury` | boolean |
| `masterBedroomLocation` | integer |
| `numLivingAreas` | integer |
| `communityId` | integer |
| `communityName` | string |
| `communityStatus` | string |
| `communityType` | string |
| `projectType` | string |
| `communityAddress` | string |
| `communityMinHomePrice` | integer |
| `communityMaxHomePrice` | integer |
| `communityMinHomeSize` | integer |
| `communityMaxHomeSize` | integer |

---

[← All scrapers](../../README.md)
