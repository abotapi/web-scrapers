# Mercado Livre Brazil Scraper

Scrape Mercado Livre Brazil's best-sellers, category and product-video feeds without login. Extract prices, discounts, instalments, sold counts, shipping, sellers, images and videos. Category mode auto-pages the app's home tabs. Keyword search is sign-in gated.

**[Open Mercado Livre Brazil Scraper on Apify](https://apify.com/abotapi/mercadolivre-com-br-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~mercadolivre-com-br-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "category", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "BR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Pick your mode |
| `category` | array | Category mode tabs to walk |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max result pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/mercadolivre-com-br-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `itemId` | string |
| `title` | string |
| `url` | string |
| `imageUrl` | string |
| `price` | integer |
| `currency` | string |
| `installmentsText` | string |
| `freeShipping` | boolean |
| `rating` | integer |
| `bestSeller` | boolean |
| `soldText` | string |
| `full` | boolean |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
