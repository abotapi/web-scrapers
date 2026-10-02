# Redfin Scraper

Scrape redfin.com home listings: price, beds, baths, sqft, lot, year built, coordinates, address, MLS, status, days on market, photos, schools, amenities, tax records, agent and brokerage plus 90+ fields. Search any city, ZIP, neighborhood, or county with sort and filters, or paste Redfin URLs.

**[Open Redfin Scraper on Apify](https://apify.com/abotapi/redfin-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~redfin-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Chicago, IL"], "listingType": "for_sale", "sortBy": "recommended", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `listingType` | string | Listing type |
| `sortBy` | string | Sort by |
| `propertyTypes` | array | Property types |
| `minPrice` | integer | Min price (USD) |
| `maxPrice` | integer | Max price (USD) |
| `minBeds` | integer | Min bedrooms |
| `minBaths` | integer | Min bathrooms |
| `minSqft` | integer | Min square feet |
| `urls` | array | URLs |
| `fetchDetails` | boolean | Fetch full listing details |
| `maxItems` | integer | Max listings |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy |
| `maxResidentialMB` | integer | Residential traffic budget (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/redfin-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `propertyId` | integer |
| `listingId` | integer |
| `url` | string |
| `mlsId` | string |
| `mls` | string |
| `showMlsId` | boolean |
| `mlsStatus` | string |
| `dataSourceId` | integer |
| `feedSource` | string |
| `marketId` | integer |
| `businessMarketId` | integer |
| `price` | integer |
| `priceDisplayLevel` | integer |
| `priceType` | string |
| `hideSalePrice` | boolean |
| `pricePerSqFt` | integer |
| `hoa` | null |
| `hoaDues` | null |
| `isHoaFrequencyKnown` | boolean |
| `beds` | integer |
| `baths` | float |
| `bathFull` | integer |
| `bathPartial` | integer |
| `sqFt` | integer |
| `sqft` | integer |
| `lotSize` | integer |
| `stories` | integer |
| `yearBuilt` | integer |
| `streetLine` | string |
| `address` | string |
| `unitNumber` | null |
| `city` | string |
| `state` | string |
| `zip` | string |
| `zipCode` | string |
| `postalCode` | string |
| `countryCode` | string |
| `location` | string |
| `latLong` | object |

---

[← All scrapers](../../README.md)
