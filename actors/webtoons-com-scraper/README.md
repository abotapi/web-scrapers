# WEBTOON Scraper

Scrape the WEBTOON catalog into structured data. Extract series, genres, rankings and complete episode lists, including titles, authors, descriptions, thumbnails and other available series and episode details.

**[Open WEBTOON Scraper on Apify](https://apify.com/abotapi/webtoons-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~webtoons-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchType": "all", "language": "en", "source": "originals", "sortOrder": "MANA", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `keyword` | string | Keyword |
| `searchType` | string | Search type |
| `language` | string | Language |
| `source` | string | Source |
| `genre` | string | Genre |
| `sortOrder` | string | Sort order |
| `weekday` | string | Weekday |
| `urls` | array | Page URLs |
| `fetchDetails` | boolean | Fetch series details |
| `includeEpisodes` | boolean | Include episodes |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per series |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/webtoons-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `titleNo` | integer |
| `title` | string |
| `url` | string |
| `language` | string |
| `genre` | string |
| `webtoonType` | string |
| `sourcePage` | string |
| `badge` | null |
| `likeCountRaw` | string |
| `likeCount` | integer |
| `author` | string |
| `scheduleText` | null |
| `pageSchedule` | null |
| `rank` | null |
| `authors` | null |
| `summary` | null |
| `viewCount` | null |
| `subscribeCount` | null |
| `latestEpisode` | null |
| `imageUrl` | string |
| `referer` | string |

---

[← All scrapers](../../README.md)
