# OK.ru Scraper

Scrape public OK.ru users, groups, topics, posts, videos, games and greetings by keyword or URL. Extract profiles, feeds, views, likes, comments, players and ratings as clean JSON, with change tracking for recurring monitoring. No account required.

**[Open OK.ru Scraper on Apify](https://apify.com/abotapi/ok-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~ok-ru-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQuery": "котики", "searchTypes": ["users"], "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQuery` | string | Search query |
| `searchTypes` | array | What to search (pick one or more) |
| `links` | array | Links (groups, topics, profiles, video |
| `maxItems` | integer | Max items |
| `includeComments` | boolean | Include comments (videos and topics) |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/ok-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `id` | string |
| `name` | string |
| `firstName` | null |
| `lastName` | null |
| `url` | string |
| `gender` | string |
| `birthday` | string |
| `location` | string |
| `avatar` | string |

---

[← All scrapers](../../README.md)
