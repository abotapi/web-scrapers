# Web Scraper For Llms

Stealth web scraping engine built for LLMs. Converts any web page to clean markdown or HTML

**[Open Web Scraper For Llms on Apify](https://apify.com/abotapi/web-scraper-for-llms?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~web-scraper-for-llms/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"urls": ["https://example.com"], "formats": ["markdown"]}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `urls` * | array | URLs |
| `crawl` | boolean | Enable Crawl Mode (follow links and sc |
| `crawlDepth` | integer | Crawl Depth |
| `crawlMaxPages` | integer | Max Pages to Discover |
| `formats` | array | Output Formats |
| `concurrency` | integer | Concurrency |
| `maxRetries` | integer | Max Retries |
| `timeoutMs` | integer | Timeout (ms) |
| `onlyMainContent` | boolean | Only Main Content |
| `removeAds` | boolean | Remove Ads |
| `removeBase64Images` | boolean | Remove Base64 Images |
| `includeTags` | array | Include Tags |
| `excludeTags` | array | Exclude Tags |
| `includePatterns` | array | Include URL Patterns |
| `excludePatterns` | array | Exclude URL Patterns |
| `waitForSelector` | string | Wait For Selector |
| `proxyConfiguration` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/web-scraper-for-llms?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `url` | string |
| `title` | string |
| `description` | null |
| `markdown` | string |
| `html` | null |
| `metadata` | object |
| `duration` | integer |
| `scrapedAt` | string |
| `success` | boolean |
| `error` | null |

---

[← All scrapers](../../README.md)
