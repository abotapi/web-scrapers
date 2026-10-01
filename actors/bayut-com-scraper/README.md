# Bayut.com Scraper

Scrape Bayut.com property listings with prices, beds, baths, area, GPS, agent and agency details, phone, WhatsApp, email, RERA/Trakheesi permits, photos, amenities, and TruCheck verification dates.

**[Open Bayut.com Scraper on Apify](https://apify.com/abotapi/bayut-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~bayut-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["dubai"], "purpose": "for-sale", "propertyType": "property", "furnishing": "any", "completionStatus": "any", "rentFrequency": "any", "sortBy": "popular", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AE"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `locations` | array | Cities / areas to search |
| `purpose` | string | Buy or rent (Search mode) |
| `propertyType` | string | Property type (Search mode) |
| `minPrice` | integer | Min price (AED) |
| `maxPrice` | integer | Max price (AED) |
| `minBedrooms` | integer | Min bedrooms |
| `maxBedrooms` | integer | Max bedrooms |
| `minArea` | integer | Min area (sqft) |
| `maxArea` | integer | Max area (sqft) |
| `furnishing` | string | Furnishing (Search mode) |
| `completionStatus` | string | Completion status (Search mode) |
| `rentFrequency` | string | Rent frequency (Rent only) |
| `verifiedOnly` | boolean | TruCheck verified only (Search mode) |
| `sortBy` | string | Sort order (Search mode) |
| `urls` | array | Search URLs (URL mode) |
| `maxPages` | integer | Max result pages per location/URL |
| `maxListings` | integer | Max total listings (default 20, 0  unl |
| `fetchDetails` | boolean | Enrich each listing with full detail ( |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/bayut-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `externalID` | string |
| `id` | integer |
| `objectID` | string |
| `ownerID` | integer |
| `userExternalID` | string |
| `url` | string |
| `slug` | string |
| `purpose` | string |
| `propertyType` | string |
| `title` | string |
| `titleArabic` | null |
| `titleL2` | null |
| `titleL3` | null |
| `price` | integer |
| `currency` | string |
| `priceHidden` | boolean |
| `rentFrequency` | null |
| `rooms` | integer |
| `baths` | integer |
| `area` | float |
| `areaUnit` | string |
| `plotArea` | null |
| `furnishingStatus` | string |
| `completionStatus` | string |
| `isStudio` | null |
| `isDeveloper` | null |
| `country` | string |
| `city` | string |
| `neighbourhood` | string |
| `building` | string |
| `latitude` | float |
| `longitude` | float |
| `geoExact` | null |
| `locationPath` | string |
| `locationDetails` | list |
| `locationPurposeTier` | integer |
| `isVerified` | boolean |
| `verificationStatus` | string |
| `verifiedAt` | integer |
| `trucheckedAt` | integer |

---

[← All scrapers](../../README.md)
