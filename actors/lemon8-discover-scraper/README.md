# Lemon8 Search Scraper

Scrape Lemon8 posts by keyword across multiple regions. Extract posts, images, videos, comments, engagement metrics, and detailed post analytics, with support for high-quality media downloads. Ideal for market research, content analysis, and trend monitoring.

**[Open Lemon8 Search Scraper on Apify](https://apify.com/abotapi/lemon8-discover-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~lemon8-discover-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"searchTerm": "fashion", "region": "us", "limit": 10, "proxy": {"useApifyProxy": true, "apifyProxyCountry": "US"}, "dev_dataset_name": "default"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `searchTerm` * | string | Search Term |
| `startUrls` | array | Start URLs |
| `region` | string | Region |
| `limit` | integer | Post Limit |
| `getDetails` | boolean | Get Detailed Post Data |
| `detailsLimit` | integer | Details Post Limit |
| `commentExpansionTimeout` | integer | Comment Expansion Timeout (seconds) |
| `saveImages` | boolean | Save Images |
| `saveVideos` | boolean | Save Videos |
| `proxy` | object | Proxy Configuration |
| `dev_transform_fields` | array | Transform Fields |
| `dev_dataset_name` | string | Custom Dataset Name |
| `dev_dataset_clear` | boolean | Clear Dataset Before Insert |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/lemon8-discover-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `author` | object |
| `title` | string |
| `content` | string |
| `postUrl` | string |
| `statistics` | object |
| `images` | list |
| `comments` | list |
| `isVideo` | boolean |
| `videoData` | null |
| `searchQuery` | string |
| `details` | object |
| `allComments` | list |
| `commentStats` | object |

---

[← All scrapers](../../README.md)
