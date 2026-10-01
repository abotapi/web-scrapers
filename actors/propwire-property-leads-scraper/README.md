# Propwire Scraper

Scrape Propwire.com: 157M+ US MLS & off-market properties with owner names, mailing addresses, equity, foreclosure and auction details, mortgages, transfers, owner portfolios, tax and full MLS records. Filter by lead type, property type, value, year built, sale date and MLS status.

**[Open Propwire Scraper on Apify](https://apify.com/abotapi/propwire-property-leads-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~propwire-property-leads-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"addressMatchMode": "first", "startUrls": ["https://propwire.com/realestate/4055-Britt-Rd/51608674/property-details"], "searchStates": ["FL"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `addresses` | array | Addresses or APNs (address lookup mode |
| `addressMatchMode` | string | When several properties match one addr |
| `startUrls` | array | Links (links mode) |
| `searchStates` | array | States |
| `searchLocations` | array | Cities, ZIPs or counties (optional) |
| `searchLeadTypes` | array | Lead types |
| `searchPropertyTypes` | array | Property types |
| `searchEstimatedValueMin` | integer | Min estimated value () |
| `searchEstimatedValueMax` | integer | Max estimated value () |
| `searchYearBuiltMin` | integer | Year built from |
| `searchYearBuiltMax` | integer | Year built to |
| `searchSoldSince` | string | Last sold on or after |
| `searchOwnerType` | array | Owner type |
| `searchMlsStatus` | string | MLS status |
| `fetchDetails` | boolean | Full property records |
| `maxItems` | integer | Max records |
| `maxPages` | integer | Max pages per search |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/propwire-property-leads-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | integer |
| `address` | string |
| `city` | string |
| `state` | string |
| `zip` | string |
| `county` | string |
| `propertyType` | string |
| `bedrooms` | null |
| `bathrooms` | null |
| `buildingAreaSf` | integer |
| `livingAreaSf` | null |
| `lotSizeSf` | integer |
| `yearBuilt` | integer |
| `stories` | null |
| `units` | null |
| `estimatedValue` | integer |
| `estimatedEquity` | integer |
| `estimatedEquityPercentage` | integer |
| `lastSoldDate` | string |
| `lastSoldPrice` | integer |
| `daysOnMarket` | null |
| `mlsListPrice` | null |
| `mlsListDate` | null |
| `mlsStatus` | null |
| `imageUrl` | null |
| `imageUrls` | null |
| `photoCount` | null |
| `leadTypes` | list |
| `ownerNames` | list |
| `ownerTypes` | list |
| `ownerOccupied` | boolean |
| `ownershipYears` | null |
| `ownerMailingAddress` | string |
| `portfolioPropertiesOwned` | integer |
| `portfolioValue` | integer |
| `foreclosureActive` | boolean |
| `auctionDate` | null |
| `apn` | string |
| `zoning` | null |

---

[← All scrapers](../../README.md)
