# Hepsiemlak Scraper

Scrape hepsiemlak.com sale and rental listings by city or district, or paste listing links. Every row carries price, area, rooms, seller and location. Detail enrichment adds specs, description and contact.

**[Open Hepsiemlak Scraper on Apify](https://apify.com/abotapi/hepsiemlak-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~hepsiemlak-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "listingType": "sale", "propertyType": "any", "sortBy": "default", "locations": ["Istanbul"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "TR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `listingType` | string | Listing type |
| `propertyType` | string | Property type |
| `roomCount` | string | Room plan |
| `ownerOnly` | boolean | Owner listings only |
| `sortBy` | string | Sort by |
| `locations` | array | Locations |
| `minPrice` | integer | Min price (TRY) |
| `maxPrice` | integer | Max price (TRY) |
| `minArea` | integer | Min area (m2) |
| `maxArea` | integer | Max area (m2) |
| `urls` | array | Listing or catalogue links |
| `fetchDetails` | boolean | Fetch details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `maxItemsPerSource` | integer | Max items per location or link |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/hepsiemlak-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `listingId` | string |
| `url` | string |
| `title` | string |
| `price` | integer |
| `currency` | string |
| `grossSqm` | integer |
| `rooms` | integer |
| `bedrooms` | integer |
| `propertyTypes` | list |
| `imageUrl` | string |
| `city` | string |
| `country` | string |
| `descriptionSnippet` | string |
| `sellerName` | string |
| `sellerOfficeUrl` | string |
| `position` | integer |
| `county` | string |
| `district` | string |
| `mainCategory` | string |
| `subCategory` | string |
| `category` | string |
| `createDate` | string |
| `updatedDate` | string |
| `listingUpdatedDate` | string |
| `startDate` | string |
| `buildingAge` | integer |
| `floorName` | string |
| `images` | list |
| `imageCount` | integer |
| `latitude` | float |
| `longitude` | float |
| `mapLocation` | object |
| `roomCount` | integer |
| `livingRoomCount` | integer |
| `roomPlan` | string |
| `sellerType` | string |
| `netAreaSqm` | integer |
| `owner` | object |
| `firm` | object |

---

[← All scrapers](../../README.md)
