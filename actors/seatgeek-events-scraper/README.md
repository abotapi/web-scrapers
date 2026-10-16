# SeatGeek Scraper

Scrape SeatGeek events with ticket price ranges (lowest, highest, average, median), venues, performers, dates and availability. Search by keyword, category, team, venue or date, or paste event links. Incremental monitoring, resume and MCP export.

**[Open SeatGeek Scraper on Apify](https://apify.com/abotapi/seatgeek-events-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~seatgeek-events-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "query": "coldplay", "searchType": "events", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `query` | string | Search query |
| `searchType` | string | Search type |
| `taxonomy` | string | Category |
| `performerIds` | array | Performer IDs |
| `venueId` | string | Venue ID |
| `dateFrom` | string | Date from |
| `dateTo` | string | Date to |
| `sort` | string | Sort |
| `urls` | array | SeatGeek links |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per scope |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/seatgeek-events-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `eventId` | integer |
| `url` | string |
| `title` | string |
| `shortTitle` | string |
| `eventType` | string |
| `startDateTimeUtc` | string |
| `startDateTimeLocal` | string |
| `dateTbd` | boolean |
| `timeTbd` | boolean |
| `status` | string |
| `announcedAt` | string |
| `venueId` | integer |
| `venueName` | string |
| `venueCity` | string |
| `venueState` | string |
| `venueCountry` | string |
| `venueAddress` | string |
| `venuePostalCode` | string |
| `venueTimezone` | string |
| `venueCapacity` | integer |
| `venueLatitude` | float |
| `venueLongitude` | float |
| `venueUrl` | string |
| `headliner` | string |
| `performers` | list |
| `performerIds` | list |
| `taxonomies` | list |
| `lowestPrice` | integer |
| `highestPrice` | integer |
| `averagePrice` | integer |
| `medianPrice` | integer |
| `goodDealLowestPrice` | null |
| `listingCount` | integer |
| `ticketCount` | integer |
| `popularity` | float |
| `score` | float |
| `raw` | object |

---

[← All scrapers](../../README.md)
