# Veepee Scraper

Scrape Veepee flash sales: live campaigns with brands, dates and discounts plus per-sale items with price, was-price, discount %, sizes and availability across FR, IT, ES, BE and NL markets. Campaign discovery is anonymous; sale item detail uses a member session lane.

**[Open Veepee Scraper on Apify](https://apify.com/abotapi/veepee-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~veepee-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "market": "fr", "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `market` | string | Market |
| `urls` | array | Sale ids or Veepee links |
| `searchQueries` | array | Search queries (optional) |
| `includeItems` | boolean | Sale item detail |
| `includeItemDetails` | boolean | Per-item extra detail |
| `maxItems` | integer | Max items |
| `maxConcurrency` | integer | Max concurrency |
| `requestDelaySecs` | number | Delay between requests (seconds) |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/veepee-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `id` | string |
| `saleId` | integer |
| `brand` | string |
| `name` | string |
| `brands` | list |
| `brandIds` | list |
| `operationCode` | string |
| `beginDate` | string |
| `endDate` | string |
| `saleTypeId` | integer |
| `url` | string |
| `saleUrl` | string |
| `logo` | string |
| `logos` | object |
| `image` | string |
| `webImage` | string |
| `mobileImage` | string |
| `description` | string |
| `tagline` | string |
| `categoryId` | integer |
| `saleBusinessId` | integer |
| `saleSectorId` | integer |
| `saleSubSectorId` | integer |
| `businessUnit` | integer |
| `isBrandAlert` | boolean |
| `isShareable` | boolean |
| `isNewCatalog` | boolean |
| `isPreopening` | boolean |
| `market` | string |
| `source` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
