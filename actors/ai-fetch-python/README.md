# AI Agent Web Fetcher Scraper

An advanced web fetcher that can fetch almost all websites and convert them to LLM-friendly Markdown format. Perfect for AI agents, RAG systems, and integration with search actors.

**[Open AI Agent Web Fetcher Scraper on Apify](https://apify.com/abotapi/ai-fetch-python?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~ai-fetch-python/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://www.google.com", "urlField": "link", "waitUntil": "domcontentloaded"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `url` | string | URL to fetch |
| `datasetId` | string | Dataset ID (Integration Mode) |
| `urlField` | string | URL Field Name |
| `maxUrls` | integer | Maximum URLs to Fetch |
| `proxy` | object | Proxy Configuration |
| `waitUntil` | string | Wait Until |
| `debug` | boolean | Debug Mode |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/ai-fetch-python?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `url` | string |
| `markdown` | string |
| `metadata` | object |

---

[← All scrapers](../../README.md)
