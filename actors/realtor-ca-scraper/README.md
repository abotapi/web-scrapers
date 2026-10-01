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
| `mode` | string | 1. Search mode |
| `locations` | array | Locations to search |
| `listingType` | string | Listing Type |
| `propertySearchCategory` | string | Property Category |
| `buildingTypeFilter` | string | Building Type Filter |
| `priceMin` | integer | Minimum Price |
| `priceMax` | integer | Maximum Price |
| `bedroomsMin` | integer | Minimum Bedrooms |
| `bedroomsMax` | integer | Maximum Bedrooms |
| `bathroomsMin` | integer | Minimum Bathrooms |
| `sortBy` | string | Sort Order |
| `soldWithinDays` | string | Sold in Last |
| `openHouseOnly` | boolean | Open House Only |
| `keywords` | string | Keywords |
| `urls` | array | Search URLs |
| `maxListings` | integer | Maximum Listings |
| `maxPages` | integer | Maximum Pages per Location |
| `proxyConfiguration` | object | Proxy configuration |
| `resumeFromCheckpoint` | boolean | Resume from Checkpoint |

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
