# Bandsintown Scraper

Scrape Bandsintown concert and festival dates: artist tour calendars, venue profiles, ticket links, lineups, RSVP counts and genres. Search by artist name or paste artist, venue or event links. MCP export included.

**[Open Bandsintown Scraper on Apify](https://apify.com/abotapi/bandsintown-concert-event-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~bandsintown-concert-event-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "artistNames": ["Ed Sheeran"], "dateRange": "upcoming", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `artistNames` | array | Artist names |
| `dateRange` | string | Date range |
| `urls` | array | Bandsintown links |
| `fetchDetails` | boolean | Fetch full artist and venue details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per scope |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/bandsintown-concert-event-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `eventId` | string |
| `url` | string |
| `title` | string |
| `datetime` | string |
| `startsAt` | string |
| `endsAt` | null |
| `timezone` | null |
| `datetimeDisplayRule` | string |
| `onSaleDatetime` | string |
| `festivalStartDate` | null |
| `festivalEndDate` | null |
| `lineup` | list |
| `offers` | list |
| `soldOut` | boolean |
| `free` | boolean |
| `presale` | null |
| `bandsintownPlus` | boolean |
| `showMultiTicket` | boolean |
| `imageUrl` | string |
| `thumbUrl` | string |
| `description` | null |
| `rsvpCount` | null |
| `genre` | null |
| `artistId` | string |
| `artistName` | string |
| `artistUrl` | string |
| `artistMbid` | string |
| `artistImageUrl` | string |
| `artistThumbUrl` | string |
| `artistFacebookPageUrl` | string |
| `artistTrackerCount` | integer |
| `artistUpcomingEventCount` | integer |
| `artistGenre` | null |
| `artistBio` | null |
| `artistLocation` | null |
| `artistLinks` | list |
| `artistUpcomingEvents` | null |
| `artistPastEvents` | null |
| `venueId` | null |

---

[← All scrapers](../../README.md)
