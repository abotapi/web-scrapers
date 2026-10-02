# Rightmove Scraper

Fast, reliable Rightmove.co.uk scraper for sale, rent, and sold-price listings. Search by location or direct URL and extract 80+ structured fields per property.

**[Open Rightmove Scraper on Apify](https://apify.com/abotapi/rightmove-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~rightmove-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "channel": "BUY", "locations": ["London"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `channel` | string | Channel |
| `locations` | array | Locations |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `minBedrooms` | integer | Min bedrooms |
| `maxBedrooms` | integer | Max bedrooms |
| `propertyTypes` | array | Property types |
| `radius` | string | Search radius (miles) |
| `sortType` | string | Sort order |
| `includeLetAgreed` | boolean | Include Let Agreed (RENT) |
| `includeSSTC` | boolean | Include SSTC / Under Offer (BUY) |
| `startUrls` | array | Start URLs |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `includeDetails` | boolean | Scrape full property details |
| `monitoringMode` | boolean | Monitoring mode (new only) |
| `proxyConfiguration` | object | Proxy configuration |
| `proxyCountry` | string | Proxy country |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/rightmove-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `url` | string |
| `channel` | string |
| `transactionType` | string |
| `displayStatus` | string |
| `propertySubType` | string |
| `propertyTypeFullDescription` | string |
| `bedrooms` | integer |
| `bathrooms` | null |
| `displayAddress` | string |
| `summary` | string |
| `price` | integer |
| `pricePerMonth` | null |
| `pricePerWeek` | null |
| `currency` | string |
| `priceFrequency` | string |
| `displayPrice` | string |
| `priceQualifier` | string |
| `latitude` | float |
| `longitude` | float |
| `addedOrReduced` | string |
| `listingUpdateReason` | string |
| `listingUpdateDate` | string |
| `firstVisibleDate` | string |
| `premiumListing` | boolean |
| `featuredProperty` | boolean |
| `isRecent` | boolean |
| `onlineViewingsAvailable` | boolean |
| `displaySize` | string |
| `distance` | null |
| `formattedDistance` | string |
| `tenure` | null |
| `numberOfImages` | integer |
| `numberOfFloorplans` | integer |
| `numberOfVirtualTours` | integer |
| `images` | list |
| `letAvailableDate` | null |
| `keywords` | list |
| `tags` | list |
| `feesApply` | boolean |

---

[← All scrapers](../../README.md)
