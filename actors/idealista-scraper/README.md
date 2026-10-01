# Idealista Scraper

Scrape Idealista properties across Spain, Italy, and Portugal. Extract 35+ fields including prices, sizes, rooms, coordinates, advertiser contacts, phone numbers, descriptions, and photos. Supports properties for sale, rent, and rooms.

**[Open Idealista Scraper on Apify](https://apify.com/abotapi/idealista-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~idealista-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "market": "es", "operation": "sale", "locations": ["madrid-madrid"], "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search Mode |
| `market` | string | Market |
| `operation` | string | Operation |
| `locations` | array | Locations |
| `minPrice` | integer | Min Price (EUR) |
| `maxPrice` | integer | Max Price (EUR) |
| `minBedrooms` | integer | Min Bedrooms |
| `maxBedrooms` | integer | Max Bedrooms |
| `urls` | array | Search URLs |
| `maxPages` | integer | Max Pages Per Search |
| `maxListings` | integer | Max Listings |
| `maxConcurrency` | integer | Detail Concurrency |
| `fetchDetails` | boolean | Fetch Detail Pages |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/idealista-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `market` | string |
| `operation` | string |
| `title` | string |
| `propertyType` | string |
| `price` | integer |
| `priceText` | string |
| `previousPrice` | integer |
| `priceDropped` | boolean |
| `currency` | string |
| `size` | integer |
| `rooms` | integer |
| `bathrooms` | integer |
| `floor` | string |
| `hasLift` | boolean |
| `description` | string |
| `thumbnail` | string |
| `photoCount` | integer |
| `isBranded` | boolean |
| `hasVideo` | boolean |
| `has3DTour` | boolean |
| `hasFloorPlan` | boolean |
| `hasHomeStaging` | boolean |
| `source` | string |
| `scrapedAt` | string |
| `address` | string |
| `neighborhood` | string |
| `city` | string |
| `pricePerM2` | integer |
| `energyConsumptionRating` | string |
| `energyEmissionsRating` | string |
| `reference` | string |
| `lastUpdatedText` | string |
| `features` | list |
| `hasTerrace` | boolean |
| `hasAC` | boolean |
| `condition` | string |
| `orientation` | string |
| `heating` | string |

---

[← All scrapers](../../README.md)
