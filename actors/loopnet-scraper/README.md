# LoopNet Scraper

Scrape LoopNet commercial listings across the US, including office, retail, industrial, multifamily, land and hotels. Search by city or URL and extract 25+ fields including price, size, address, broker contacts and photos, with optional detail enrichment.

**[Open LoopNet Scraper on Apify](https://apify.com/abotapi/loopnet-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~loopnet-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "site": "co-uk", "locations": ["united-kingdom"], "listingType": "for-sale", "propertyType": "all-commercial", "sortBy": "default", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `site` | string | Site / region |
| `locations` | array | Locations |
| `listingType` | string | Listing type |
| `propertyType` | string | Property type |
| `urls` | array | LoopNet URLs |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `minSqft` | integer | Minimum size (sq ft) |
| `maxSqft` | integer | Maximum size (sq ft) |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch detail pages |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (total) |
| `proxy` | object | Connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/loopnet-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `listingType` | string |
| `propertyType` | string |
| `propertyTypeName` | null |
| `spaceUse` | null |
| `listingTypeName` | string |
| `exposureLevel` | string |
| `addressRaw` | string |
| `street` | null |
| `city` | string |
| `state` | null |
| `zipCode` | string |
| `country` | string |
| `marketId` | null |
| `propertyId` | null |
| `latitude` | null |
| `longitude` | null |
| `price` | null |
| `priceRaw` | null |
| `priceUnit` | string |
| `priceLabel` | string |
| `listedAt` | null |
| `currency` | string |
| `size` | string |
| `sizeSqft` | integer |
| `sizeSqftMin` | null |
| `sizeSqftMax` | integer |
| `sizeAcres` | null |
| `yearBuilt` | null |
| `buildingClass` | null |
| `capRate` | null |
| `occupancy` | null |
| `brokerNames` | list |
| `brokerCompanyUrl` | null |
| `brokerName` | string |
| `brokerCompany` | null |
| `brokerPhone` | null |
| `description` | string |

---

[← All scrapers](../../README.md)
