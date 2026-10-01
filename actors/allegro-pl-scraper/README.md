# Allegro Scraper

Scrape Allegro by keyword or URL. Extract offers, prices, delivery, seller details, and product reviews. Includes incremental change monitoring, resume support, and MCP connectors for automated workflows.

**[Open Allegro Scraper on Apify](https://apify.com/abotapi/allegro-pl-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~allegro-pl-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["iphone"], "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "PL"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Input mode |
| `queries` | array | Search phrases |
| `startUrls` | array | Start URLs |
| `keywords` | array | Keywords |
| `fetchDetails` | boolean | Fetch full offer details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/allegro-pl-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `offerId` | string |
| `title` | string |
| `url` | string |
| `price` | integer |
| `currency` | string |
| `originalPrice` | null |
| `deliveryInfo` | string |
| `sponsored` | boolean |
| `bestPriceGuarantee` | boolean |
| `sellerName` | string |
| `sellerBusiness` | boolean |
| `sellerFeedbackPercent` | float |
| `superSeller` | boolean |
| `category` | string |
| `parameters` | object |
| `image` | string |
| `sourceUrl` | string |
| `sourceLabel` | string |

---

[← All scrapers](../../README.md)
