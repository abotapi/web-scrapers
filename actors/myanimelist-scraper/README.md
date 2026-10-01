# MyAnimeList Scraper

Scrape MyAnimeList anime and manga by keyword, ranking chart or URL. Extract titles, scores, ranks, members, genres, studios, authors, synonyms and full synopses. Supports top, airing, upcoming, popular and favorite rankings, plus resume and incremental monitoring.

**[Open MyAnimeList Scraper on Apify](https://apify.com/abotapi/myanimelist-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~myanimelist-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "mediaType": "anime", "searchTerms": ["Frieren"], "chartKind": "top", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Collection mode |
| `mediaType` | string | Media type |
| `searchTerms` | array | Search keywords |
| `chartKind` | string | Chart |
| `urls` | array | MyAnimeList URLs |
| `fetchDetails` | boolean | Fetch full details for every record |
| `maxReviews` | integer | Maximum reviews per record |
| `maxItems` | integer | Maximum records |
| `maxPages` | integer | Maximum pages per keyword or chart |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/myanimelist-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `mediaType` | string |
| `url` | string |
| `title` | string |
| `type` | string |
| `episodes` | integer |
| `score` | float |
| `synopsisSnippet` | string |
| `titleJapanese` | string |
| `titleEnglish` | string |
| `synonyms` | list |
| `status` | string |
| `aired` | string |
| `premiered` | string |
| `broadcast` | string |
| `source` | string |
| `duration` | string |
| `rating` | string |
| `ranked` | integer |
| `popularity` | integer |
| `members` | integer |
| `favorites` | integer |
| `genres` | list |
| `themes` | list |
| `demographics` | list |
| `producers` | list |
| `licensors` | list |
| `studios` | list |
| `authors` | list |
| `serialization` | list |
| `synopsis` | string |
| `imageUrl` | string |
| `scoredBy` | integer |
| `reviewCount` | integer |
| `reviewBreakdown` | object |
| `relatedEntries` | list |
| `characters` | list |
| `staff` | list |
| `reviews` | list |
| `openingThemes` | list |

---

[← All scrapers](../../README.md)
