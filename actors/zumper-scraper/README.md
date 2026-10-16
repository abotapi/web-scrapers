# Zumper Scraper

Scrape Zumper.com rental listings: apartments, houses, condos and rooms. Pulls 60+ fields per listing, including monthly rent, beds/baths, square footage, decoded amenities, agent name and phone, ratings, availability and full-resolution photos. Search by location with filters, or paste Zumper URLs.

**[Open Zumper Scraper on Apify](https://apify.com/abotapi/zumper-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~zumper-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["San Francisco, CA"], "propertyCategory": "apartments", "sortBy": "default", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `propertyCategory` | string | Property category |
| `petsAllowed` | array | Pets allowed |
| `urls` | array | Zumper URLs |
| `minPrice` | integer | Minimum rent (USD/mo) |
| `maxPrice` | integer | Maximum rent (USD/mo) |
| `minBedrooms` | integer | Minimum bedrooms |
| `maxBedrooms` | integer | Maximum bedrooms |
| `minBathrooms` | integer | Minimum bathrooms |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch detail pages |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (total) |
| `proxy` | object | Connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/zumper-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `padmapperUrl` | string |
| `title` | string |
| `buildingName` | string |
| `propertyCategory` | string |
| `isBuilding` | boolean |
| `address` | string |
| `formattedAddress` | null |
| `city` | string |
| `state` | string |
| `zipcode` | string |
| `neighborhood` | string |
| `latitude` | float |
| `longitude` | float |
| `minPrice` | integer |
| `maxPrice` | integer |
| `previousPrice` | null |
| `currency` | string |
| `minBedrooms` | integer |
| `maxBedrooms` | integer |
| `minBathrooms` | integer |
| `maxBathrooms` | integer |
| `minSquareFeet` | integer |
| `maxSquareFeet` | integer |
| `floorplanCount` | integer |
| `dateAvailable` | null |
| `minLeaseDays` | null |
| `maxLeaseDays` | null |
| `listedOn` | string |
| `modifiedOn` | string |
| `yearBuilt` | null |
| `yearRemodeled` | null |
| `floors` | null |
| `unitAmenities` | list |
| `buildingAmenities` | list |
| `amenityGroups` | null |
| `petPolicy` | list |
| `parking` | null |
| `deposits` | null |

---

[← All scrapers](../../README.md)
