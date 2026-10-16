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
  -d '{"resultType": "web", "query": "Tesla", "region": "us-en", "safeSearch": "moderate", "maxResults": 10, "maxItems": 10, "proxy": {"useApifyProxy": true}, "dev_dataset_name": "default"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `resultType` | string | Result Type |
| `query` | string | Search Query |
| `searchMode` | string | Search mode (alias of Result Type) |
| `search` | string | Search (alias of Search Query) |
| `region` | string | Region |
| `safeSearch` | string | Safe Search |
| `timeRange` | string | Time Range |
| `maxResults` | integer | Maximum Results |
| `maxItems` | integer | Max items (alias of Maximum Results) |
| `endPage` | integer | End page |
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
| `url` | string |
| `description` | string |
| `rawDescription` | string |
| `hostname` | string |
| `icon` | string |
| `excerpt` | string |
| `publishedOn` | null |
| `viewCount` | null |
| `image_token` | null |
| `height` | null |
| `image` | null |

---

[← All scrapers](../../README.md)
