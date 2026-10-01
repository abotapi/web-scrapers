# Viagogo Scraper

Scrape Viagogo events by artist, production, venue, city, category, or URL. Extract event names, dates, venues, locations, availability, and links. Track NEW, UPDATED, REAPPEARED, and EXPIRED events with incremental runs, resume, and MCP export.

**[Open Viagogo Scraper on Apify](https://apify.com/abotapi/viagogo-events-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~viagogo-events-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["Coldplay"], "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search terms |
| `urlInputs` | array | Links |
| `urls` | array | Links (alias) |
| `maxItems` | integer | Max items |
| `includeMatches` | boolean | Also return production and venue match |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/viagogo-events-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `eventId` | string |
| `url` | string |
| `title` | string |
| `dayOfWeek` | string |
| `formattedDate` | string |
| `formattedTime` | string |
| `formattedDateWithDayOfWeek` | string |
| `startDateTimeUtc` | string |
| `isDateConfirmed` | boolean |
| `isTimeConfirmed` | boolean |
| `isTbd` | boolean |
| `isMultidayEvent` | boolean |
| `isParkingEvent` | boolean |
| `venueTimeZoneOffsetHours` | integer |
| `eventState` | integer |
| `availabilityState` | integer |
| `hasListings` | boolean |
| `allowPublicPurchase` | boolean |
| `isUnderHundred` | boolean |
| `venueId` | integer |
| `venueName` | string |
| `venueCity` | string |
| `venueLocation` | string |
| `countryCode` | string |
| `countryName` | string |
| `searchKeyword` | string |
| `raw` | object |

---

[← All scrapers](../../README.md)
