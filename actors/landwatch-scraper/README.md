# LandWatch Scraper

Scrape land, farm, ranch, and rural property listings from LandWatch.com. Search by location, price, acreage filters, or URLs. Returns price, acreage, coordinates, description, amenities, price history, photos, seller name, phone, company, and 90+ fields.

**[Open LandWatch Scraper on Apify](https://apify.com/abotapi/landwatch-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~landwatch-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Texas"], "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `propertyTypes` | array | Property types |
| `minPrice` | integer | Min price (USD) |
| `maxPrice` | integer | Max price (USD) |
| `minAcres` | integer | Min acres |
| `maxAcres` | integer | Max acres |
| `minBeds` | integer | Min bedrooms |
| `hasHouse` | boolean | Has a house |
| `urls` | array | URLs |
| `fetchDetails` | boolean | Fetch full listing details |
| `maxItems` | integer | Max listings |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy |
| `maxResidentialMB` | integer | Residential traffic budget (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/landwatch-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `lwPropertyId` | integer |
| `listingId` | integer |
| `siteListingId` | integer |
| `url` | string |
| `canonicalUrl` | string |
| `title` | string |
| `h1` | string |
| `price` | integer |
| `priceDisplay` | string |
| `shortPrice` | string |
| `pricePerAcre` | float |
| `priceChangeAmount` | integer |
| `priceChangeDate` | null |
| `priceChangePercentage` | float |
| `shortPriceChangeAmount` | string |
| `acres` | float |
| `acreage` | float |
| `acresDisplay` | string |
| `beds` | integer |
| `bedsDisplay` | string |
| `baths` | integer |
| `bathsDisplay` | string |
| `halfBaths` | integer |
| `halfBathsDisplay` | null |
| `homesqft` | integer |
| `homesqftDisplay` | string |
| `latitude` | float |
| `longitude` | float |
| `address` | string |
| `city` | string |
| `county` | string |
| `countyLabel` | string |
| `state` | string |
| `stateAbbreviation` | string |
| `stateCode` | string |
| `zip` | string |
| `description` | string |
| `descriptionText` | string |
| `executiveSummary` | string |

---

[← All scrapers](../../README.md)
