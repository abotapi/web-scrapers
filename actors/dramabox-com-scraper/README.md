# DramaBox Scraper

Scrape DramaBox short-drama series by browsing the catalogue or entering a series ID. Extract series metadata, genres, view counts, follower counts and complete episode lists. Requires a residential proxy connection.

**[Open DramaBox Scraper on Apify](https://apify.com/abotapi/dramabox-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~dramabox-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "browse", "series": ["42000028173"], "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `series` | array | Series IDs or URLs |
| `maxItems` | integer | Max items |
| `maxEpisodesPerSeries` | integer | Max episodes per series |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/dramabox-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `bookId` | string |
| `title` | string |
| `titleEn` | string |
| `author` | null |
| `introduction` | string |
| `cover` | string |
| `chapterCount` | integer |
| `labels` | list |
| `tags` | list |
| `typeOneName` | null |
| `viewCount` | integer |
| `viewCountDisplay` | null |
| `followCount` | integer |
| `lastUpdateTime` | null |
| `shelfTime` | string |
| `language` | string |
| `url` | string |
| `kind` | string |
| `episodeCount` | integer |
| `episodes` | list |
| `episodesTruncated` | boolean |
| `performerIdList` | list |
| `hasCast` | boolean |
| `recommendBookIds` | list |
| `articleUrl` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
