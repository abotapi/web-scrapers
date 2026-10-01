# Stocktwits Scraper

Scrape Stocktwits message streams with bull/bear sentiment labels, bodies, likes, replies, cashtags and author stats for any symbol. Trending symbols, user profiles and full reply threads. Incremental monitoring, resume and MCP export.

**[Open Stocktwits Scraper on Apify](https://apify.com/abotapi/stocktwits-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~stocktwits-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "symbols", "symbols": ["AAPL"], "sort": "all", "usernames": ["Stocktwits"], "sentiment": "all", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `symbols` | array | Symbols (tickers) |
| `sort` | string | Stream order |
| `usernames` | array | Usernames |
| `messageUrls` | array | Message links or IDs |
| `startUrls` | array | Stocktwits links |
| `sentiment` | string | Sentiment filter |
| `fetchReplies` | boolean | Fetch reply threads |
| `maxItems` | integer | Max items |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/stocktwits-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `messageId` | integer |
| `url` | string |
| `body` | string |
| `createdAt` | string |
| `sentiment` | string |
| `likes` | integer |
| `repliesCount` | integer |
| `reshares` | integer |
| `cashtags` | list |
| `symbols` | list |
| `mentionedUsers` | list |
| `authorUsername` | string |
| `authorName` | string |
| `authorFollowers` | integer |
| `authorIdentity` | string |
| `authorOfficial` | boolean |
| `sourceLabel` | object |
| `symbolContext` | string |

---

[← All scrapers](../../README.md)
