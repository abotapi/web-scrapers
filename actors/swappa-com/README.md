# Swappa Scraper

Scrape Swappa used-tech listings by device, carrier, storage, condition or color. Extract prices, seller details, battery health and full listing data, plus price guides, trade-in values and monthly price history.

**[Open Swappa Scraper on Apify](https://apify.com/abotapi/swappa-com?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~swappa-com/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "resultType": "both", "queries": ["iPhone 15 Pro"], "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `resultType` | string | What to return |
| `queries` | array | Devices |
| `condition` | string | Condition |
| `carrier` | string | Carrier |
| `storage` | string | Storage size |
| `color` | string | Colour |
| `modeln` | string | Model number |
| `sort` | string | Sort order |
| `withWarranty` | boolean | One-year warranty only |
| `acceptsCreditCards` | boolean | Accepts credit cards |
| `carrierUnlockedOnly` | boolean | Carrier unlocked only |
| `excludeBusinesses` | boolean | Exclude enterprise sellers |
| `phoneCheckCertified` | boolean | Certified devices only |
| `internationalShipping` | boolean | Ships internationally |
| `urls` | array | Addresses |
| `minPrice` | integer | Minimum price (USD) |
| `maxPrice` | integer | Maximum price (USD) |
| `minBatteryHealth` | integer | Minimum battery health (%) |
| `fetchDetails` | boolean | Open each device page |
| `deepSoldHistory` | boolean | Deep sold-price history |
| `maxPages` | integer | Maximum catalogue pages per device |
| `maxListings` | integer | Maximum devices |
| `proxy` | object | Connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/swappa-com?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `slug` | string |
| `name` | string |
| `url` | string |
| `minPrice` | integer |
| `currency` | string |
| `imageUrl` | string |
| `platform` | string |
| `searchTerm` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
