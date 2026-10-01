# Globo Esporte Scraper

Scrape public sports content from ge.globo.com, including news, videos, matches and feed records. Extract clean, structured data for sports coverage, content monitoring, match tracking and analysis.

**[Open Globo Esporte Scraper on Apify](https://apify.com/abotapi/globo-ge?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~globo-ge/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["flamengo"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Collection mode |
| `queries` | array | Search keywords |
| `urls` | array | GE URLs |
| `fetchDetails` | boolean | Fetch article details |
| `maxItems` | integer | Maximum records |
| `maxPages` | integer | Maximum pages |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/globo-ge?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `summary` | string |
| `publishedAt` | string |
| `modifiedAt` | string |
| `species` | string |
| `recordType` | string |
| `thumbnailUrl` | string |
| `durationSeconds` | integer |

---

[← All scrapers](../../README.md)
