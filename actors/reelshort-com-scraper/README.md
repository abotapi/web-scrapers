# ReelShort Scraper

Scrape the ReelShort vertical short-drama catalog: titles, synopses, themes and full tag taxonomy, episode counts, cast with IMDb links, view and collect counts. Search, curated shelves, genres or paste title links. Resume, incremental updates and MCP export included.

**[Open ReelShort Scraper on Apify](https://apify.com/abotapi/reelshort-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~reelshort-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "SHELF", "searchQueries": ["billionaire"], "genres": ["Affair", "Billionaire"], "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `searchQueries` | array | Search keywords |
| `shelves` | array | Shelves |
| `genres` | array | Genres / tags |
| `crawlTagIndex` | boolean | Walk the whole tag index |
| `maxTags` | integer | Max tags to walk |
| `listingUrls` | array | ReelShort URLs |
| `fetchDetails` | boolean | Enrich each title |
| `maxPages` | integer | Max pages per scope |
| `maxItems` | integer | Max titles |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/reelshort-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `bookId` | string |
| `transportId` | string |
| `chapterId` | string |
| `title` | string |
| `url` | string |
| `cover` | string |
| `synopsis` | string |
| `themes` | list |
| `tags` | list |
| `chapterCount` | integer |
| `collectCount` | integer |
| `collectCountDisplay` | string |
| `language` | string |
| `bookType` | integer |
| `mode` | string |
| `extractionPath` | string |
| `readCount` | integer |
| `readCountDisplay` | string |
| `paidStart` | integer |
| `screenMode` | integer |
| `hasTrailer` | integer |
| `shelf` | string |
| `shelfRank` | null |
| `resultsReturned` | integer |
| `chapterDescription` | string |
| `durationSec` | integer |
| `hasDub` | boolean |
| `firstChapterId` | string |
| `firstSerialNumber` | integer |
| `videoUrl` | string |
| `videoPic` | string |
| `releaseDate` | string |
| `onlineAtDate` | string |
| `updateStatus` | integer |
| `bookSource` | integer |
| `cast` | list |
| `hasCast` | boolean |
| `imdbId` | null |

---

[← All scrapers](../../README.md)
