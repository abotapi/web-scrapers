# OneFootball Scraper

Scrape public OneFootball data including football news, upcoming fixtures, match results and league tables. Get clean, structured data for teams, competitions and matches in one place.

**[Open OneFootball Scraper on Apify](https://apify.com/abotapi/onefootball-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~onefootball-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "competitions": ["premier-league-9"], "language": "en", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `competitions` | array | Competitions |
| `teams` | array | Teams (optional) |
| `includeGlobalNews` | boolean | Global news feed |
| `urls` | array | OneFootball links |
| `language` | string | Content language |
| `includeNews` | boolean | News |
| `includeFixtures` | boolean | Fixtures |
| `includeResults` | boolean | Results |
| `includeTable` | boolean | League table |
| `fetchDetails` | boolean | Read full article text |
| `maxItems` | integer | Max records |
| `maxPages` | integer | Max pages per source |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/onefootball-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `title` | string |
| `url` | string |
| `publisher` | string |
| `publisherImageUrl` | string |
| `publisherIsVerified` | boolean |
| `publishedAt` | string |
| `publishTime` | string |
| `preview` | string |
| `imageUrl` | string |
| `isVideo` | boolean |
| `language` | string |
| `articleText` | null |
| `articleChars` | null |
| `sourceType` | string |
| `sourceId` | string |
| `sourceUrl` | string |
| `position` | integer |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
