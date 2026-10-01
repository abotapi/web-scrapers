# Concert Archives Scraper

Scrape Concert Archives concert and tour history: past and upcoming dates, venues, cities, line-ups, tours, genres, tickets and setlists. Search by band, venue or location, or paste links. Incremental monitoring with NEW, UPDATED, REAPPEARED, EXPIRED, resume and MCP export.

**[Open Concert Archives Scraper on Apify](https://apify.com/abotapi/concert-archives-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~concert-archives-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "query": "the killers", "searchType": "bands", "dateFilter": "all", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `query` | string | Search query |
| `searchType` | string | Search type |
| `urls` | array | Concert Archives links |
| `dateFilter` | string | Upcoming or past concerts |
| `year` | integer | Year (optional) |
| `fetchDetails` | boolean | Fetch concert details |
| `includeSetlists` | boolean | Include setlists |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per scope |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/concert-archives-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `concertId` | string |
| `url` | string |
| `slug` | string |
| `title` | string |
| `startDate` | string |
| `dateText` | string |
| `isUpcoming` | boolean |
| `tourName` | string |
| `lineup` | null |
| `headliner` | string |
| `venueName` | string |
| `venueUrl` | string |
| `locationText` | string |
| `locationUrl` | string |
| `venueCity` | string |
| `venueRegion` | string |
| `venueCountry` | string |
| `ticketUrl` | string |
| `hasSetlist` | boolean |
| `hasPhotos` | boolean |
| `labels` | list |
| `endDate` | null |
| `eventStatus` | null |
| `description` | null |
| `imageUrl` | null |
| `performers` | null |
| `artistGenres` | null |
| `ticketVendor` | null |
| `venueAddress` | null |
| `lineupCount` | null |
| `attendeeCount` | null |
| `photoCount` | null |
| `setlists` | null |
| `setlistCount` | null |

---

[← All scrapers](../../README.md)
