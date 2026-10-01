# StreetEasy Scraper

Scrape StreetEasy sales, rentals and in-contract listings across NYC and Jersey City. Search with filters or URLs and extract prices, GPS coordinates, photos, amenities, building details, brokerages, agent contacts and price history.

**[Open StreetEasy Scraper on Apify](https://apify.com/abotapi/streeteasy-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~streeteasy-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "saleType": "forSale", "locations": ["nyc"], "sortBy": "RECOMMENDED", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Start here, pick your search mode |
| `saleType` | string | Listing type |
| `locations` | array | Locations (boroughs / neighborhoods) |
| `urls` | array | URLs (paste a StreetEasy search-result |
| `propertyTypes` | array | Property types |
| `minPrice` | integer | Min price (USD) |
| `maxPrice` | integer | Max price (USD) |
| `minBedrooms` | integer | Min bedrooms |
| `maxBedrooms` | integer | Max bedrooms |
| `minBathrooms` | number | Min bathrooms |
| `minSqft` | integer | Min square feet |
| `maxSqft` | integer | Max square feet |
| `amenities` | array | Amenities (must include all selected) |
| `noFee` | boolean | No-fee rentals only |
| `keywords` | string | Keyword search |
| `sortBy` | string | Sort order |
| `maxPages` | integer | Max pages per query (0  unlimited) |
| `perPage` | integer | Listings per page |
| `maxListings` | integer | Max listings (0  unlimited within budg |
| `fetchDetails` | boolean | Fetch detail pages (slower, more field |
| `expandLargeQueries` | boolean | Auto-expand queries above 1050 results |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/streeteasy-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `saleType` | string |
| `status` | string |
| `price` | integer |
| `neighborhood` | string |
| `borough` | string |
| `address` | string |
| `unit` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `halfBathrooms` | integer |
| `squareFeet` | null |
| `pricePerSqft` | null |
| `propertyType` | string |
| `latitude` | float |
| `longitude` | float |
| `imageUrl` | string |
| `images` | list |
| `brokerage` | string |
| `listedAt` | null |
| `daysOnMarket` | null |
| `offMarketAt` | null |
| `furnished` | boolean |
| `noFee` | null |
| `advertisedListing` | boolean |
| `description` | null |
| `amenities` | list |
| `buildingName` | null |
| `buildingYear` | null |
| `schoolDistricts` | list |
| `transit` | list |
| `priceHistory` | list |
| `agents` | list |
| `openHouseDates` | list |
| `virtualTourUrl` | null |
| `sourceUrl` | null |
| `zipCode` | string |
| `state` | string |
| `mediaAssetCount` | integer |

---

[← All scrapers](../../README.md)
