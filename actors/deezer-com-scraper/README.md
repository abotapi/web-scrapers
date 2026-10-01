# Deezer Scraper

Scrape Deezer by keyword or URL. Extract tracks, albums, artists, playlists, lyrics, radios, charts and public profiles. Get BPM, ISRC, contributors, release dates, availability, full tracklists, artist top tracks and discographies.

**[Open Deezer Scraper on Apify](https://apify.com/abotapi/deezer-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~deezer-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["daft punk"], "searchType": "track", "source": "search", "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `searchType` | string | Entity type |
| `source` | string | Source |
| `chartGenreId` | integer | Chart genre id |
| `urls` | array | Deezer URLs |
| `includeArtistReleases` | boolean | Artist also return their albums |
| `includeUserCollections` | boolean | User also return their public playlist |
| `excludeExplicit` | boolean | Exclude explicit tracks |
| `minDurationSec` | integer | Min duration (seconds) |
| `maxDurationSec` | integer | Max duration (seconds) |
| `sortBy` | string | Sort results by |
| `fetchDetails` | boolean | Fetch full track detail (search mode) |
| `includeLyrics` | boolean | Include lyrics (any mode) |
| `lyricsWordTiming` | boolean | Lyrics word-level timing (karaoke) |
| `maxItems` | integer | Max records |
| `maxPages` | integer | Max result pages per keyword or link |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/deezer-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `deezerType` | string |
| `title` | string |
| `url` | string |
| `durationSec` | integer |
| `explicitLyrics` | boolean |
| `rank` | integer |
| `isrc` | string |
| `previewUrl` | string |
| `releaseDate` | null |
| `bpm` | null |
| `gain` | null |
| `diskNumber` | null |
| `trackPosition` | null |
| `artistId` | integer |
| `artistName` | string |
| `artistUrl` | string |
| `artistFans` | null |
| `artistAlbumCount` | null |
| `albumId` | integer |
| `albumTitle` | string |
| `albumUrl` | string |
| `label` | null |
| `copyright` | null |
| `albumTrackCount` | null |
| `genres` | list |
| `contributorNames` | list |
| `availableCountries` | list |
| `collectionContext` | null |
| `trackIds` | list |
| `trackTitles` | list |
| `description` | null |
| `fans` | null |
| `creatorId` | null |
| `creatorName` | null |
| `playlistPublic` | null |
| `collaborative` | null |
| `userName` | null |
| `userCountry` | null |
| `sourceQuery` | string |

---

[← All scrapers](../../README.md)
