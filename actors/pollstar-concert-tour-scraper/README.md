# Pollstar Scraper

Scrape Pollstar upcoming concerts and tour dates: play date, venue with full address and coordinates, artist line-up, genres, ticket links and market. Search artists, venues or cities, or paste Pollstar links. Newly-announced filter, incremental monitoring, resume and MCP export.

**[Open Pollstar Scraper on Apify](https://apify.com/abotapi/pollstar-concert-tour-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~pollstar-concert-tour-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "query": "Las Vegas", "searchType": "cities", "sortOrder": "asc", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `query` | string | Search query |
| `searchType` | string | Search type |
| `urls` | array | Pollstar links |
| `fromDate` | string | From date (YYYY-MM-DD) |
| `toDate` | string | To date (YYYY-MM-DD) |
| `newOnly` | boolean | Newly announced only |
| `includeNearbyCities` | boolean | Include nearby cities (city searches o |
| `sortOrder` | string | Date order |
| `fetchArtistProfiles` | boolean | Fetch headline artist profiles |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per scope |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/pollstar-concert-tour-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `eventId` | string |
| `url` | string |
| `title` | string |
| `playDate` | string |
| `playTime` | null |
| `isFestival` | boolean |
| `hasBoxOfficeReport` | boolean |
| `announcedHoursAgo` | integer |
| `note` | null |
| `venueId` | string |
| `venueName` | string |
| `venueUrl` | string |
| `venueTypes` | list |
| `venueMarket` | string |
| `venueStreet` | string |
| `venueCity` | string |
| `venueState` | string |
| `venueStateName` | string |
| `venuePostalCode` | string |
| `venueCountry` | string |
| `venueLatitude` | float |
| `venueLongitude` | float |
| `venuePhone` | null |
| `venueEmail` | null |
| `venueWebsite` | null |
| `headlineArtist` | string |
| `headlineArtistId` | string |
| `headlineArtistUrl` | string |
| `headlineArtistType` | string |
| `genres` | list |
| `supportActs` | list |
| `artists` | list |
| `tickets` | list |
| `ticketUrl` | string |
| `ticketVendors` | list |
| `scopeKind` | string |
| `scopeId` | string |
| `scopeName` | string |

---

[← All scrapers](../../README.md)
