# Ticketmaster Scraper

Discover and scrape Ticketmaster events across the US, UK, Australia and Canada. Search by keyword, artist or venue, filter by city and date, or paste URLs directly. Includes incremental monitoring and resume support for ongoing event tracking.

**[Open Ticketmaster Scraper on Apify](https://apify.com/abotapi/ticketmaster-event-discovery?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~ticketmaster-event-discovery/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "query": "concerts", "market": "us", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `query` | string | Search query |
| `market` | string | Market |
| `sort` | string | Sort |
| `city` | string | City filter |
| `dateFrom` | string | Start date from |
| `dateTo` | string | Start date to |
| `urls` | array | Ticketmaster links |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/ticketmaster-event-discovery?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `eventId` | string |
| `discoveryId` | string |
| `market` | string |
| `url` | string |
| `title` | string |
| `startDate` | string |
| `onsaleDate` | string |
| `spanMultipleDays` | boolean |
| `timeZone` | string |
| `cancelled` | boolean |
| `postponed` | boolean |
| `rescheduled` | boolean |
| `soldOut` | boolean |
| `limitedAvailability` | boolean |
| `ticketingStatus` | string |
| `virtual` | boolean |
| `venueName` | string |
| `venueCity` | string |
| `venueState` | string |
| `venueCountry` | string |
| `venueCountryCode` | string |
| `venueAddress` | string |
| `venuePostalCode` | string |
| `venueLatitude` | float |
| `venueLongitude` | float |
| `venueUrl` | string |
| `venueImageUrl` | string |
| `artists` | list |
| `artistNames` | list |
| `presales` | list |
| `seatmapImageUrl` | string |
| `categoryId` | string |
| `raw` | object |

---

[← All scrapers](../../README.md)
