# Dealroom Startup & Market Map Scraper

Scrape Dealroom.net market maps, company lookup results, live signals, and newly founded startup records. Supports Dealroom URLs, company names, market-map ids, sorting, capped runs, rich normalized company fields, and optional MCP connector export.

**[Open Dealroom Startup & Market Map Scraper on Apify](https://apify.com/abotapi/dealroom-co-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~dealroom-co-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "marketmaps", "searchQuery": "AI", "companyNames": ["OpenAI", "Anthropic"], "sortBy": "source", "maxItems": 10, "limit": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `startUrls` | array | Start URLs |
| `searchQuery` | string | Search query |
| `marketmapIds` | array | Market-map ids |
| `companyNames` | array | Company names |
| `includeNews` | boolean | Include news metadata |
| `includeSentiment` | boolean | Include sentiment metadata |
| `sortBy` | string | Sort order |
| `maxItems` | integer | Max items |
| `limit` | integer | Limit |
| `maxPages` | integer | Max pages |
| `pageSize` | integer | Page size |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/dealroom-co-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `id` | string |
| `url` | string |
| `record_id` | string |
| `company_name` | string |
| `company_website` | string |
| `scrape_metadata` | object |
| `company_identity` | object |
| `market_and_product_profile` | object |
| `growth_and_traction` | object |
| `funding_and_financials` | object |
| `investors_and_ownership` | object |
| `locations_and_operations` | object |
| `web_and_social_presence` | object |
| `news_and_signals` | object |
| `source_record` | object |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
