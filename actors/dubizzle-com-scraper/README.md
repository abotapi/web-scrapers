# Dubizzle.com Scraper

Scrape dubizzle.com across the UAE for property, motors, and agent listings. Search by filters or URLs with auto pagination. Returns price, beds, baths, area, agent/agency contacts, WhatsApp, email, GPS, photos, amenities, verification, and Dubai Land Department history.

**[Open Dubizzle.com Scraper on Apify](https://apify.com/abotapi/dubizzle-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~dubizzle-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["dubai"], "section": "property-for-sale", "propertyType": "residential", "furnishing": "any", "completionStatus": "any", "sortBy": "popular", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AE"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Cities / areas to search |
| `section` | string | Section to scrape (Search mode) |
| `propertyType` | string | Property type (Search mode, property s |
| `minPrice` | integer | Min price (AED) |
| `maxPrice` | integer | Max price (AED) |
| `minBedrooms` | integer | Min bedrooms |
| `maxBedrooms` | integer | Max bedrooms |
| `minArea` | integer | Min area (sqft) |
| `maxArea` | integer | Max area (sqft) |
| `furnishing` | string | Furnishing (Search mode) |
| `completionStatus` | string | Completion status (Search mode) |
| `sortBy` | string | Sort order (Search mode) |
| `urls` | array | Dubizzle URLs (URL mode) |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max total listings |
| `fetchDetails` | boolean | Include listing details |
| `includeDldHistory` | boolean | Include Dubai Land Department history  |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/dubizzle-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `price` | integer |
| `currency` | string |
| `section` | string |
| `categorySlug` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `area` | integer |
| `areaUnit` | string |
| `city` | string |
| `neighborhood` | list |
| `latitude` | float |
| `longitude` | float |
| `isVerified` | boolean |
| `agentName` | string |
| `agencyName` | null |
| `phoneNumber` | null |
| `whatsapp` | null |
| `addedOn` | integer |
| `furnished` | boolean |
| `completionStatus` | string |
| `hasDldHistory` | boolean |
| `propertyReference` | string |
| `shortUrl` | string |
| `photosCount` | integer |
| `isPremium` | boolean |
| `raw` | object |
| `recordType` | string |
| `detailMissing` | boolean |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
