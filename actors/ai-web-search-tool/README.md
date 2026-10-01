# AI Search Tool Scraper

Give your AI agents real-world knowledge. This Actor provides high-quality web, news, image, video, and book search results using a multi-backend DuckDuckGo–powered infrastructure, with automatic fallbacks to Brave, Bing, Yahoo, Google (where available).

**[Open AI Search Tool Scraper on Apify](https://apify.com/abotapi/ai-web-search-tool?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~ai-web-search-tool/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"query": "Tesla", "maxResults": 10, "region": "us-en", "safeSearch": "moderate", "resultType": "web", "proxy": {"useApifyProxy": false, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": ""}, "dev_dataset_name": "default"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `query` * | string | Search Query |
| `maxResults` | integer | Maximum Results |
| `region` | string | Region |
| `safeSearch` | string | Safe Search |
| `timeRange` | string | Time Range |
| `resultType` | string | Result Type |
| `proxy` | object | Proxy Configuration |
| `dev_transform_fields` | array | Transform Fields (Advanced) |
| `dev_dataset_name` | string | Custom Dataset Name (Advanced) |
| `dev_dataset_clear` | boolean | Clear Dataset Before Insert (Advanced) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/ai-web-search-tool?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `position` | integer |
| `title` | string |
| `link` | string |
| `snippet` | string |
| `domain` | string |
| `query` | string |

---

[← All scrapers](../../README.md)
