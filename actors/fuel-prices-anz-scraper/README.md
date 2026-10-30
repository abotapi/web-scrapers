# Fuel Price Scraper

Scrape current petrol and fuel prices across Australia and New Zealand. Search by address or GPS coordinates to find nearby fuel stations, compare prices and collect station locations and fuel price data.

**[Open Fuel Price Scraper on Apify](https://apify.com/abotapi/fuel-prices-anz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

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
  -d '{"suburb": "Sydney", "searchMode": "location", "startUrls": [{"url": "https://petrolspy.com.au/map/location/au/nsw/2000/sydney"}, {"url": "https://petrolspy.com.au/map/latlng/-33.8688/151.2093"}], "sortOrder": "asc", "maxItems": 10, "proxy": {"useApifyProxy": false}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `suburb` | string | Suburb or City |
| `lat` | number | Latitude |
| `lng` | number | Longitude |
| `latitude` | number | Latitude (alias) |
| `longitude` | number | Longitude (alias) |
| `searchMode` | string | Search mode |
| `startUrls` | array | Start URLs |
| `radiusKm` | number | Search Radius (km) |
| `fuelType` | string | Fuel Type Filter |
| `brands` | array | Brands (optional) |
| `sortBy` | string | Sort by |
| `sortOrder` | string | Sort order |
| `maxItems` | integer | Max stations |
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
| `id` | string |
| `url` | string |
| `imageUrl` | string |
| `address` | string |
| `suburb` | string |
| `state` | string |
| `postalCode` | string |
| `latitude` | float |
| `longitude` | float |
| `u91Price` | float |
| `e10Price` | null |
| `u95Price` | float |
| `u98Price` | null |
| `dieselPrice` | null |
| `lpgPrice` | null |
| `distanceKm` | float |
| `currency` | string |

---

[← All scrapers](../../README.md)
