# GoodShort Scraper

Scrape the GoodShort short-drama catalog: titles with exact views, follows, genres and trope tags, synopses, covers, full episode lists with prices and stream URLs. Browse trending rails, genres, tags and search, or paste title and listing URLs. Resume, incremental updates and MCP export included.

**[Open GoodShort Scraper on Apify](https://apify.com/abotapi/goodshort-catalog-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~goodshort-catalog-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "TRENDING", "searchQueries": ["billionaire"], "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `genres` | array | Genres |
| `tags` | array | Tags |
| `crawlTagIndex` | boolean | Sweep the whole tag index |
| `maxTags` | integer | Max tags to sweep |
| `searchQueries` | array | Search keywords |
| `listingUrls` | array | GoodShort URLs |
| `fetchDetails` | boolean | Full title enrichment |
| `fetchEpisodes` | boolean | Collect full episode lists |
| `maxEpisodes` | integer | Max episodes per title |
| `maxPages` | integer | Max pages per browse |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/goodshort-catalog-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `platform` | string |
| `recordType` | string |
| `id` | string |
| `slug` | string |
| `title` | string |
| `url` | string |
| `mode` | string |
| `extractionPath` | string |
| `scraperVersion` | string |
| `rail` | string |
| `views` | integer |
| `viewsDisplay` | string |
| `viewsDisplayParsed` | integer |
| `follows` | integer |
| `episodeCount` | integer |
| `genres` | list |
| `tags` | list |
| `tagUrls` | list |
| `description` | string |
| `cover` | string |
| `author` | string |
| `studio` | string |
| `status` | string |
| `praiseCount` | integer |
| `language` | string |
| `statusCode` | string |
| `publishStatus` | string |
| `likeNum` | integer |
| `novelType` | string |
| `period` | string |
| `totalWords` | integer |
| `releaseDate` | string |
| `lastChapterName` | string |
| `lastChapterTime` | string |
| `lastUpdatedAt` | string |
| `freeEpisodes` | integer |
| `hasPaidEpisodes` | boolean |
| `paidFromEpisode` | string |
| `totalPlayTimeSec` | integer |
| `detailFetched` | boolean |

---

[← All scrapers](../../README.md)
