# Realtor.ca Scraper

Scrape Realtor.ca property listings with prices, descriptions, images, agent and brokerage details, coordinates, open house times, building features, and more.

**[Open Realtor.ca Scraper on Apify](https://apify.com/abotapi/realtor-ca-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~realtor-ca-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "location", "locations": [{"city": "Toronto", "province": "ON"}], "listingType": "buy", "propertySearchCategory": "residential", "sortBy": "6-D", "soldWithinDays": "1year", "maxListings": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "CA"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Search mode |
| `locations` | array | Locations to search |
| `listingType` | string | Listing type (buy / rent) |
| `propertySearchCategory` | string | Property category |
| `buildingTypeFilter` | string | Building type |
| `priceMin` | integer | Minimum price |
| `priceMax` | integer | Maximum price |
| `bedroomsMin` | integer | Minimum bedrooms |
| `bedroomsMax` | integer | Maximum bedrooms |
| `bathroomsMin` | integer | Minimum bathrooms |
| `sortBy` | string | Sort order |
| `soldWithinDays` | string | Sold within last |
| `openHouseOnly` | boolean | Open houses only |
| `keywords` | string | Keywords |
| `urls` | array | Search page URLs |
| `maxListings` | integer | Maximum listings |
| `maxPages` | integer | Maximum pages per location |
| `simplifyOutput` | boolean | Flat output (simplify) |
| `resumeFromCheckpoint` | boolean | Resume from checkpoint |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/realtor-ca-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `scrapedAt` | string |
| `propertyId` | string |
| `mlsNumber` | string |
| `url` | string |
| `listingType` | string |
| `propertyType` | string |
| `buildingType` | string |
| `ownershipType` | string |
| `dateListed` | string |
| `timeOnRealtor` | string |
| `communityName` | string |
| `statusId` | integer |
| `uploadedBy` | string |
| `urlFr` | string |
| `photosUpdatedAt` | string |
| `address` | object |
| `coordinates` | object |
| `price` | object |
| `features` | object |
| `propertyFeatures` | list |
| `tags` | list |
| `media` | object |
| `agents` | list |

---

[← All scrapers](../../README.md)
