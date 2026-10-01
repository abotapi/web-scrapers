# Rumah123 Scraper

Pull structured property listings from Rumah123.com, Indonesia’s largest property portal. Search by location with advanced filters or paste Rumah123 URLs directly. Returns pricing, specs, GPS, agent contacts, galleries, instalment estimates, and 50+ fields, plus the full raw listing record.

**[Open Rumah123 Scraper on Apify](https://apify.com/abotapi/rumah123-indonesia-property-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~rumah123-indonesia-property-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["dki-jakarta"], "listingType": "sale", "propertyType": "residential", "sortBy": "recommended", "furnishing": "any", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "ID"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `locations` | array | Locations |
| `listingType` | string | Listing type |
| `propertyType` | string | Property type |
| `minPrice` | integer | Min price (IDR) |
| `maxPrice` | integer | Max price (IDR) |
| `minBedrooms` | integer | Min bedrooms |
| `minBathrooms` | integer | Min bathrooms |
| `minLandSize` | integer | Min land size (m2) |
| `maxLandSize` | integer | Max land size (m2) |
| `minBuildingSize` | integer | Min building size (m2) |
| `maxBuildingSize` | integer | Max building size (m2) |
| `urls` | array | Direct URLs |
| `sortBy` | string | Sort by |
| `furnishing` | string | Furnishing |
| `fetchDetails` | boolean | Fetch full details |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (0  unlimited) |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/rumah123-indonesia-property-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `uuid` | string |
| `url` | string |
| `slug` | string |
| `title` | string |
| `shortDescription` | string |
| `description` | null |
| `listingType` | string |
| `listingTypeLabel` | string |
| `propertyType` | string |
| `propertyTypeCode` | string |
| `price` | integer |
| `priceDisplay` | string |
| `priceMin` | integer |
| `priceMax` | integer |
| `pricePerMeterDisplay` | string |
| `currency` | string |
| `isPriceDrop` | boolean |
| `installmentMonthly` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `carports` | null |
| `garages` | null |
| `floors` | integer |
| `landSize` | integer |
| `buildingSize` | integer |
| `maidBedrooms` | null |
| `maidBathrooms` | null |
| `certificate` | string |
| `electricity` | string |
| `furnishing` | string |
| `paymentMethod` | string |
| `isStudioType` | string |
| `locationText` | string |
| `province` | string |
| `city` | string |
| `district` | string |
| `fullAddress` | null |
| `latitude` | float |
| `longitude` | float |

---

[← All scrapers](../../README.md)
