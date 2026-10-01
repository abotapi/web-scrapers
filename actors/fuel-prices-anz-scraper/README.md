# Fuel Prices AU Scraper

Scrapes petrol and fuel prices data across Australia and New Zealand. Search by address or coordinates to find nearby stations with current fuel prices.

**[Open Fuel Prices AU Scraper on Apify](https://apify.com/abotapi/fuel-prices-anz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~fuel-prices-anz-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"suburb": "Sydney", "proxy": {"useApifyProxy": false}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `suburb` | string | Suburb or City |
| `lat` | number | Latitude |
| `lng` | number | Longitude |
| `radiusKm` | number | Search Radius (km) |
| `fuelType` | string | Fuel Type Filter |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/fuel-prices-anz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `stationId` | string |
| `name` | string |
| `brand` | string |
| `location` | object |
| `phone` | string |
| `prices` | object |
| `tradingHours` | list |
| `isAdBlueAvailable` | boolean |
| `verified` | boolean |
| `icon` | null |
| `brandIcon` | string |
| `searchContext` | object |

---

[← All scrapers](../../README.md)
