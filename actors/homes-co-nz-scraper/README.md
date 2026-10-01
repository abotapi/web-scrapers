# Homes.co.nz Scraper

Scrape Homes.co.nz listings by location or URL with pagination. Extract property details, valuations, agents, branch information, media and open homes. Search multiple locations per run with filters for status, price, bedrooms and bathrooms.

**[Open Homes.co.nz Scraper on Apify](https://apify.com/abotapi/homes-co-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~homes-co-nz-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Wellington", "Auckland Central"], "listingStatus": "for_sale", "sortBy": "default", "maxListings": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Collection Mode |
| `locations` | array | Locations |
| `urls` | array | Homes URLs |
| `listingStatus` | string | Listing Status |
| `minBedrooms` | integer | Min Bedrooms |
| `minBathrooms` | integer | Min Bathrooms |
| `minPrice` | integer | Min Price (NZD) |
| `maxPrice` | integer | Max Price (NZD) |
| `sortBy` | string | Sort By |
| `maxListings` | integer | Max Listings (global cap) |
| `maxPages` | integer | Max Pages Per Search |
| `pageSize` | integer | Listings Per Page |
| `fetchPropertyCards` | boolean | Fetch Property Cards (extra cost) |
| `includeRawApiResponses` | boolean | Include Raw Structured Payloads (debug |
| `proxyConfiguration` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/homes-co-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `id` | string |
| `listingId` | string |
| `propertyId` | string |
| `url` | string |
| `canonicalUrl` | string |
| `listingDetailUrl` | string |
| `title` | string |
| `headline` | string |
| `description` | string |
| `price` | string |
| `displayPrice` | string |
| `currency` | string |
| `publishedAt` | string |
| `createdAt` | string |
| `updatedAt` | string |
| `featuredAt` | string |
| `seedId` | string |
| `seedType` | string |
| `seedValue` | string |
| `pageIndex` | integer |
| `status` | integer |
| `urlSlug` | string |
| `address` | string |
| `addressParts` | object |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `carSpaces` | integer |
| `floorArea` | integer |
| `landArea` | integer |
| `latitude` | float |
| `longitude` | float |
| `imageUrl` | string |
| `coverImageUrl` | string |
| `imageUrls` | list |
| `canUseImages` | boolean |
| `images` | list |
| `media` | list |
| `mediaCount` | integer |
| `openHomes` | list |

---

[← All scrapers](../../README.md)
