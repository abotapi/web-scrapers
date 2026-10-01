# AniList Anime & Manga Scraper

Scrape AniList anime and manga: titles (romaji/English/native), scores, popularity, favourites, genres, studios, airing schedule, synopses, charts (trending, popular, top-rated, most-favourited), keyword search and URL/ID lookup.

**[Open AniList Anime & Manga Scraper on Apify](https://apify.com/abotapi/anilist-anime-manga-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~anilist-anime-manga-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "mediaType": "ANIME", "searchTerms": ["frieren"], "chartKind": "TRENDING", "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `mediaType` | string | Media type |
| `searchTerms` | array | Search terms |
| `chartKind` | string | Chart |
| `urls` | array | AniList URLs or ids |
| `maxMedia` | integer | Max records |
| `maxPages` | integer | Max pages per search or chart |
| `includeAdult` | boolean | Include adult media |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/anilist-anime-manga-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `idMal` | integer |
| `url` | string |
| `titleRomaji` | string |
| `titleEnglish` | string |
| `titleNative` | string |
| `format` | string |
| `status` | string |
| `episodes` | integer |
| `chapters` | null |
| `volumes` | null |
| `durationMin` | integer |
| `averageScore` | integer |
| `meanScore` | integer |
| `popularity` | integer |
| `favourites` | integer |
| `genres` | list |
| `countryOfOrigin` | string |
| `isAdult` | boolean |
| `description` | string |
| `season` | string |
| `seasonYear` | integer |
| `startDate` | string |
| `endDate` | string |
| `studios` | list |
| `nextAiringEpisode` | null |
| `nextAiringAt` | null |
| `coverImage` | string |
| `bannerImage` | string |

---

[← All scrapers](../../README.md)
