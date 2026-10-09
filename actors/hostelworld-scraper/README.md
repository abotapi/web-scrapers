# Hostelworld Scraper

Scrape Hostelworld hostels, hotels, guesthouses, B&Bs, apartments and campsites by city, property URL or ID. Extract prices, ratings, rooms, facilities, full reviews, Linkups events and attendee details.

**[Open Hostelworld Scraper on Apify](https://apify.com/abotapi/hostelworld-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~hostelworld-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Berlin"], "propertyType": "hostel", "sortBy": "recommended", "maxItems": 10, "maxPages": 1, "maxReviewsPerProperty": 10, "reviewSort": "newest", "currency": "EUR", "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Input mode |
| `locations` | array | Locations |
| `propertyType` | string | Property type |
| `district` | string | District / neighbourhood (optional) |
| `sortBy` | string | Sort listings |
| `startUrls` | array | URLs |
| `propertyIds` | array | Property IDs |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max search pages per location |
| `includeDetails` | boolean | Property details (charged per property |
| `includeReviews` | boolean | Reviews (charged per review) |
| `maxReviewsPerProperty` | integer | Max reviews per property |
| `reviewSort` | string | Review sort order |
| `allLanguages` | boolean | All review languages |
| `includeEvents` | boolean | Linkups events (charged per event) |
| `eventsDaysAhead` | integer | Events window (days ahead) |
| `eventsPageSize` | integer | Max events per property |
| `includePeople` | boolean | Who's going (included with details) |
| `reviewsOnly` | boolean | Output reviews only |
| `currency` | string | Currency |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/hostelworld-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `propertyId` | integer |
| `propertyName` | string |
| `propertyUrl` | string |
| `propertyType` | string |
| `address` | null |
| `city` | string |
| `country` | string |
| `continent` | null |
| `avgRating` | float |
| `numberReviews` | string |
| `cityCenterDistanceKm` | null |
| `latitude` | string |
| `longitude` | string |
| `hasAvailability` | null |
| `isNew` | null |
| `intro` | null |
| `sharedMinPrice` | null |
| `privateMinPrice` | null |
| `currency` | string |
| `sustainability` | null |
| `badges` | list |
| `imageUrls` | list |
| `totalImagesCount` | integer |
| `sourceMode` | string |
| `sourceQuery` | null |
| `sourceUrl` | null |
| `scrapedAt` | string |
| `description` | string |
| `hostelworldSays` | null |
| `addressFull` | string |
| `directions` | string |
| `checkInFrom` | integer |
| `checkInUntil` | integer |
| `latestCheckOut` | string |
| `depositPercentage` | integer |
| `freeCancellation` | object |
| `cancellationPolicy` | object |
| `cancellationPoliciesRaw` | null |
| `paymentMethods` | list |

---

[← All scrapers](../../README.md)
