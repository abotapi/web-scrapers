# TIDAL Scraper

Scrape TIDAL tracks, albums, artists, playlists and public mixes by search phrase or URL. Extract structured catalogue metadata with optional track lists, recurring change detection and app exports for ongoing music data workflows.

**[Open TIDAL Scraper on Apify](https://apify.com/abotapi/tidal-catalog-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~tidal-catalog-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["Daft Punk"], "searchType": "tracks", "countryCode": "US", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Collection mode |
| `queries` | array | Search phrases |
| `urls` | array | TIDAL links |
| `searchType` | string | Search result type |
| `countryCode` | string | Catalogue country |
| `maxItems` | integer | Maximum records |
| `maxPages` | integer | Maximum pages per source |
| `fetchDetails` | boolean | Include catalogue details and track li |
| `maxTracks` | integer | Maximum nested tracks |
| `proxy` | object | Connection configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/tidal-catalog-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `entityId` | string |
| `recordType` | string |
| `title` | string |
| `url` | string |
| `countryCode` | string |
| `artists` | list |
| `album` | object |
| `duration` | integer |
| `releaseDate` | null |
| `explicit` | boolean |
| `popularity` | integer |
| `numberOfTracks` | null |
| `audioQuality` | string |
| `audioModes` | list |
| `isrc` | string |
| `upc` | null |
| `copyright` | string |
| `description` | null |
| `imageUrl` | null |
| `creator` | null |
| `mixes` | object |
| `mixType` | null |
| `trackNumber` | integer |
| `volumeNumber` | integer |
| `sourceUrl` | null |
| `query` | string |
| `sourceSection` | null |
| `tracks` | list |
| `tracksTotal` | null |
| `tracksComplete` | null |
| `raw` | object |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
