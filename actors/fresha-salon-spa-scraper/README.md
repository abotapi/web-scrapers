# Fresha Scraper

Scrape Fresha salon and spa listings: business profiles, service menus with prices and durations, opening hours, team members, photos, ratings and client reviews. Search by keyword and location or paste venue and professional links. Resume, incremental updates and MCP export included.

**[Open Fresha Scraper on Apify](https://apify.com/abotapi/fresha-salon-spa-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~fresha-salon-spa-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "SEARCH", "searchQuery": "hair", "searchLocation": "Sydney", "maxPages": 1, "sort": "RECOMMENDED", "maxReviewsPerListing": 10, "reviewSorting": "LATEST", "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQuery` | string | Search keyword |
| `searchLocation` | string | Location |
| `latitude` | string | Latitude |
| `longitude` | string | Longitude |
| `maxPages` | integer | Max pages per search |
| `sort` | string | Sort results by |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `hasDeals` | boolean | Only venues with deals |
| `hasGroupAppointments` | boolean | Only group appointments |
| `freshaVerifiedOnly` | boolean | Only Fresha-verified venues |
| `availabilityDate` | string | Available on date |
| `listingUrls` | array | Venue & professional URLs |
| `fetchDetails` | boolean | Full profile enrichment |
| `fetchReviews` | boolean | Collect client reviews |
| `maxReviewsPerListing` | integer | Max reviews per listing |
| `reviewSorting` | string | Review order |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/fresha-salon-spa-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `venueId` | string |
| `slug` | string |
| `name` | string |
| `url` | string |
| `venueType` | string |
| `ownerId` | string |
| `featured` | boolean |
| `isNew` | boolean |
| `hasDeals` | boolean |
| `isFreshaVerified` | boolean |
| `groupingScore` | float |
| `rating` | integer |
| `ratingFormatted` | string |
| `reviewsCount` | integer |
| `ratingLevel` | string |
| `ratingTitle` | string |
| `ratingSubtitle` | string |
| `images` | list |
| `imageKeywords` | list |
| `imageDescriptions` | list |
| `street` | string |
| `apartmentSuite` | string |
| `city` | string |
| `area` | string |
| `state` | string |
| `country` | string |
| `postalCode` | string |
| `fullAddress` | string |
| `shortAddress` | string |
| `servicingAreas` | list |
| `nearbyServicingAreas` | list |
| `latitude` | float |
| `longitude` | float |
| `mapsUrl` | string |
| `directionsUrl` | string |
| `searchQuery` | string |
| `searchLocation` | string |
| `searchSort` | string |

---

[← All scrapers](../../README.md)
