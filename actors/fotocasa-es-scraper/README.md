# Fotocasa.es Scraper

Scrape Spain property listings from fotocasa.es. Get price, surface, rooms, baths, address, GPS, agency, phone, energy rating, photos and 140+ fields. Buy and rent, all regions, all property types.

**[Open Fotocasa.es Scraper on Apify](https://apify.com/abotapi/fotocasa-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~fotocasa-es-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["madrid-capital"], "operation": "comprar", "propertyType": "viviendas", "sortBy": "relevance", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "ES"}, "residentialCountries": ["ES"]}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `operation` | string | Operation |
| `propertyType` | string | Property Type |
| `sortBy` | string | Sort By |
| `minPrice` | integer | Min Price (EUR) |
| `maxPrice` | integer | Max Price (EUR) |
| `minRooms` | integer | Min Rooms |
| `maxRooms` | integer | Max Rooms |
| `minBaths` | integer | Min Bathrooms |
| `maxBaths` | integer | Max Bathrooms |
| `minSurface` | integer | Min Surface (m²) |
| `maxSurface` | integer | Max Surface (m²) |
| `urls` | array | Search URLs |
| `fetchDetails` | boolean | Fetch full details |
| `maxListings` | integer | Max items |
| `maxPages` | integer | Max Pages Per Search |
| `proxy` | object | Proxy Configuration |
| `residentialCountries` | array | Residential fallback countries |
| `maxResidentialRequests` | integer | Residential request budget |
| `backupProxyUrl` | string | Backup proxy URL |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/fotocasa-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `propertyId` | string |
| `property_id` | string |
| `listingId` | integer |
| `realEstateAdId` | string |
| `real_estate_ad_id` | string |
| `promotionId` | integer |
| `promotion_id` | integer |
| `userId` | null |
| `user_id` | null |
| `clientId` | integer |
| `client_id` | integer |
| `publisherId` | string |
| `publisher_id` | string |
| `agencyId` | integer |
| `transactionType` | integer |
| `transactionTypeId` | integer |
| `transaction_type` | integer |
| `transaction_type_id` | integer |
| `operation` | string |
| `listingType` | string |
| `propertyType` | integer |
| `property_type` | integer |
| `typeId` | integer |
| `type_id` | integer |
| `propertySubtype` | integer |
| `property_subtype` | integer |
| `subtypeId` | integer |
| `subtype_id` | integer |
| `buildingType` | string |
| `building_type` | string |
| `buildingSubtype` | string |
| `building_subtype` | string |
| `itemType` | string |
| `periodicityId` | integer |
| `periodicity_id` | integer |
| `price` | string |
| `rawPrice` | integer |
| `raw_price` | integer |
| `minPrice` | integer |

---

[← All scrapers](../../README.md)
