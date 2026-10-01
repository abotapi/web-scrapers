# Property24 Scraper

Extract structured property listings from Property24, South Africa’s largest property portal. Search by location or use Property24 URLs. Get 50+ fields including price, beds, baths, sizes, GPS coordinates, photos, property details, and agent/agency information.

**[Open Property24 Scraper on Apify](https://apify.com/abotapi/property24-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~property24-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "listingType": "for-sale", "locations": ["Cape Town"], "propertyType": "any", "sortBy": "default", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search Mode |
| `listingType` | string | Listing Type |
| `locations` | array | Locations |
| `propertyType` | string | Property Type |
| `minPrice` | integer | Min Price (ZAR) |
| `maxPrice` | integer | Max Price (ZAR) |
| `minBedrooms` | integer | Min Bedrooms |
| `maxBedrooms` | integer | Max Bedrooms |
| `sortBy` | string | Sort By |
| `onShowOnly` | boolean | On Show Only |
| `auctionsOnly` | boolean | Auctions Only |
| `minBathrooms` | integer | Min Bathrooms |
| `parkingSpaces` | integer | Min Parking Spaces |
| `minErfSize` | integer | Min Erf Size (m²) |
| `minFloorSize` | integer | Min Floor Size (m²) |
| `hasPool` | boolean | Has Pool |
| `hasGarden` | boolean | Has Garden |
| `hasFlatlet` | boolean | Has Flatlet |
| `petFriendly` | boolean | Pet Friendly |
| `securityEstate` | boolean | In Security Estate |
| `repossessed` | boolean | Repossessed Only |
| `retirement` | boolean | Retirement Only |
| `urls` | array | Property24 URLs |
| `fetchDetails` | boolean | Fetch Detail Pages |
| `maxPages` | integer | Max Pages Per Search |
| `maxListings` | integer | Max Listings |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/property24-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `listingNumber` | string |
| `url` | string |
| `listingType` | string |
| `title` | string |
| `displayPrice` | string |
| `price` | integer |
| `currency` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `garages` | integer |
| `parkingSpaces` | integer |
| `floorSize` | integer |
| `erfSize` | integer |
| `suburbName` | string |
| `description` | string |
| `mainImage` | string |
| `source` | string |
| `scrapedAt` | string |
| `provinceName` | string |
| `provinceId` | string |
| `cityName` | string |
| `cityId` | string |
| `suburbId` | string |
| `descriptionHeader` | string |
| `priceOnApplication` | boolean |
| `agentName` | string |
| `agentProfileUrl` | string |
| `agentId` | string |
| `agencyName` | string |
| `agencyId` | string |
| `agencyLogoUrl` | string |
| `contacts` | list |
| `isPrivateListing` | boolean |
| `propertyOverview` | object |
| `propertyType` | string |
| `listingDate` | string |
| `details` | list |
| `keyFeatures` | list |
| `photos` | list |

---

[← All scrapers](../../README.md)
