# Padmapper Scraper

Scrape Padmapper apartment rentals across US/CA cities: rent, beds, baths, sqft, location, photos, source-site links, availability. Monitoring (NEW, UPDATED, REAPPEARED, EXPIRED), incremental runs, resume, MCP export.

**[Open Padmapper Scraper on Apify](https://apify.com/abotapi/padmapper-rental-listings-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~padmapper-rental-listings-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Austin, TX"], "listingInputs": ["58574913"], "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Cities |
| `minPrice` | integer | Min rent (/mo) |
| `maxPrice` | integer | Max rent (/mo) |
| `bedrooms` | array | Bedrooms |
| `bathrooms` | integer | Min bathrooms |
| `catsOk` | boolean | Cats allowed |
| `dogsOk` | boolean | Dogs allowed |
| `listingInputs` | array | Listing or building links |
| `urls` | array | Listing or building links (alias) |
| `maxItems` | integer | Max items |
| `currencyHint` | string | Currency hint (optional) |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/padmapper-rental-listings-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `listingId` | string |
| `url` | string |
| `title` | string |
| `description` | null |
| `currency` | string |
| `rentMin` | integer |
| `rentMax` | integer |
| `previousRent` | null |
| `bedrooms` | integer |
| `bedroomsMax` | integer |
| `bathrooms` | integer |
| `bathroomsMax` | integer |
| `squareFeetMin` | null |
| `squareFeetMax` | null |
| `dateAvailable` | null |
| `address` | string |
| `city` | string |
| `state` | string |
| `zipcode` | string |
| `citySlug` | string |
| `neighborhood` | string |
| `latitude` | float |
| `longitude` | float |
| `propertyType` | string |
| `listingType` | integer |
| `leaseType` | integer |
| `sourceFeed` | string |
| `providerUrl` | null |
| `phone` | string |
| `petCodes` | list |
| `petAmenities` | list |
| `buildingAmenities` | list |
| `imageUrl` | string |
| `imageUrls` | list |
| `isFeatured` | boolean |
| `listedOn` | string |
| `createdAt` | string |
| `updatedAt` | string |

---

[← All scrapers](../../README.md)
