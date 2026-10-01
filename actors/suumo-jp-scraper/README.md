# Suumo.jp Scraper

Scrape Suumo, Japan's largest property portal: rental rooms with rent, management fees, deposits, layout, floor area, station access, photos and the listing agency's name. Search by prefecture and city or paste links, and monitor price changes with recurring updates.

**[Open Suumo.jp Scraper on Apify](https://apify.com/abotapi/suumo-jp-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~suumo-jp-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "prefecture": "13", "cityCodes": ["13101"], "layouts": ["02"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `prefecture` | string | Prefecture |
| `cityCodes` | array | City codes (optional) |
| `layouts` | array | Layout codes (optional) |
| `urls` | array | Suumo links |
| `fetchDetails` | boolean | Read each room's own page |
| `maxItems` | integer | Max rooms |
| `maxPages` | integer | Max pages per source |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/suumo-jp-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `buildingId` | string |
| `buildingName` | string |
| `buildingType` | string |
| `address` | string |
| `stations` | list |
| `buildingAge` | string |
| `buildingFloors` | string |
| `imageUrl` | string |
| `floor` | string |
| `rentYen` | integer |
| `rentDisplay` | string |
| `mgmtFeeYen` | integer |
| `depositYen` | integer |
| `keyMoneyYen` | integer |
| `layout` | string |
| `areaSqm` | float |
| `url` | string |
| `sourceType` | string |
| `sourceId` | string |
| `sourceUrl` | null |
| `position` | integer |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
