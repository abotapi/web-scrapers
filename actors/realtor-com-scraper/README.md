# Realtor.com Scraper

Extract property listings from realtor.com. Get comprehensive data, including prices, property details, agent contacts, coordinates, photos, and more. Supports for sale, rental, and recently sold listings across all US markets.

**[Open Realtor.com Scraper on Apify](https://apify.com/abotapi/realtor-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~realtor-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "location", "locations": [{"city": "Portland", "state": "OR"}], "listingType": "for_sale", "propertyType": "any", "maxListings": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | 1. Search mode |
| `locations` | array | Locations to search |
| `listingType` | string | Listing Type |
| `propertyType` | string | Property Type |
| `bedsMin` | integer | Minimum Bedrooms |
| `bathsMin` | integer | Minimum Bathrooms |
| `priceMin` | integer | Minimum Price |
| `priceMax` | integer | Maximum Price |
| `openHouseOnly` | boolean | Open House Only |
| `newConstructionOnly` | boolean | New Construction Only |
| `urls` | array | Search URLs |
| `maxListings` | integer | Max Listings |
| `maxPages` | integer | Max Pages Per Location |
| `proxyConfiguration` | object | Proxy configuration |
| `resumeFromCheckpoint` | boolean | Resume From Checkpoint |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/realtor-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `propertyId` | string |
| `listingId` | string |
| `url` | string |
| `listingType` | string |
| `status` | string |
| `address` | object |
| `coordinates` | object |
| `price` | object |
| `features` | object |
| `streetViewUrl` | string |
| `countyFips` | string |
| `agents` | list |
| `brokerage` | string |
| `mlsId` | string |
| `mlsName` | string |
| `mlsType` | string |
| `mlsSourceId` | string |
| `photos` | list |
| `photoCount` | integer |
| `listDate` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
