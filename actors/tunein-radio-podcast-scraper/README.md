# TuneIn Scraper

Scrape TuneIn by keyword, category, genre, location or URL. Extract stations and podcasts with artwork, genre, bitrate, frequency, location, language, contact details, playable stream URLs and episodes. Incremental mode tracks changes over time.

**[Open TuneIn Scraper on Apify](https://apify.com/abotapi/tunein-radio-podcast-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~tunein-radio-podcast-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["jazz"], "browseCategories": ["local"], "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `browseCategories` | array | Categories |
| `browseIds` | array | Genre, category or region ids |
| `localeLatLon` | string | Locale coordinates for Local radio |
| `urls` | array | Links or ids |
| `itemTypes` | array | Result types |
| `minBitrateKbps` | integer | Minimum stream bitrate (kbps) |
| `minReliabilityPercent` | integer | Minimum reliability score |
| `streamFormats` | array | Stream formats |
| `genreIds` | array | Genre ids |
| `fetchDetails` | boolean | Fetch full profiles |
| `fetchStreams` | boolean | Fetch playable stream URLs |
| `fetchEpisodes` | boolean | Fetch podcast episodes |
| `maxEpisodesPerPodcast` | integer | Max episodes per podcast |
| `maxItems` | integer | Max results |
| `maxPages` | integer | Max result pages per category or link |
| `maxBrowseDepth` | integer | Sub-category depth |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/tunein-radio-podcast-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `itemType` | string |
| `guideId` | string |
| `name` | string |
| `subtitle` | string |
| `description` | null |
| `slogan` | null |
| `hosts` | null |
| `image` | string |
| `url` | string |
| `profileUrl` | string |
| `websiteUrl` | null |
| `shareUrl` | null |
| `callSign` | null |
| `frequency` | null |
| `band` | null |
| `genreId` | string |
| `genreName` | null |
| `secondaryGenreName` | null |
| `location` | null |
| `latitude` | null |
| `longitude` | null |
| `regionId` | null |
| `countryRegionId` | null |
| `timezone` | null |
| `timezoneOffsetMinutes` | null |
| `language` | null |
| `bitrateKbps` | integer |
| `reliabilityPercent` | integer |
| `streamFormats` | list |
| `isPlayable` | boolean |
| `streamType` | null |
| `nowPlaying` | null |
| `nowPlayingImage` | null |
| `currentSong` | null |
| `currentArtist` | null |
| `currentAlbum` | null |
| `durationSeconds` | null |
| `publishedLabel` | null |
| `publishedAt` | null |
| `showStartsAt` | null |

---

[← All scrapers](../../README.md)
