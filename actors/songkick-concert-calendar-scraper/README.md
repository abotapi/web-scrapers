# Songkick Scraper

Scrape Songkick concert and event calendars: upcoming and past dates, venues, cities, artists, ticket availability and tour info across 100+ countries. Search by artist, venue or location, or paste event links. Incremental monitoring with NEW, UPDATED, REAPPEARED, EXPIRED, resume and MCP export.

**[Open Songkick Scraper on Apify](https://apify.com/abotapi/songkick-concert-calendar-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~songkick-concert-calendar-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "query": "the killers", "searchType": "events", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `query` | string | Search query |
| `searchType` | string | Search type |
| `urls` | array | Songkick links |
| `fetchDetails` | boolean | Fetch event details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per scope |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/songkick-concert-calendar-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `eventId` | string |
| `url` | string |
| `title` | string |
| `startDate` | string |
| `endDate` | string |
| `eventStatus` | string |
| `eventType` | string |
| `headliner` | string |
| `performers` | list |
| `artistName` | string |
| `artistUrl` | string |
| `artistGenres` | list |
| `venueName` | string |
| `venueStreet` | string |
| `venueCity` | string |
| `venueRegion` | string |
| `venuePostalCode` | string |
| `venueCountry` | string |
| `venueLatitude` | float |
| `venueLongitude` | float |
| `description` | string |
| `imageUrl` | string |
| `ticketAvailability` | string |
| `ticketVendors` | list |
| `ticketUrl` | string |
| `tourName` | null |
| `doorsTime` | string |
| `venueCapacity` | null |
| `venueUrl` | null |
| `metroAreaName` | null |
| `metroAreaUrl` | null |
| `locationText` | string |
| `supportActs` | string |
| `organizerName` | string |
| `organizerUrl` | string |
| `eventAttendanceMode` | string |
| `ticketPriceMin` | null |
| `ticketPriceMax` | null |

---

[← All scrapers](../../README.md)
