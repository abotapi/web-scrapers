# Turo Scraper

Collect Turo vehicles by location and trip dates or listing URLs. Get make, model, year, ratings, photos, dated price estimates, vehicle details and public host profiles, with resume and recurring change detection.

**[Open Turo Scraper on Apify](https://apify.com/abotapi/turo-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~turo-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Los Angeles, California"], "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `makes` | array | Makes |
| `minYear` | integer | Minimum model year |
| `maxYear` | integer | Maximum model year |
| `minRating` | number | Minimum rating |
| `urls` | array | Vehicle URLs |
| `startDateTime` | string | Trip start |
| `endDateTime` | string | Trip end |
| `fetchDetails` | boolean | Full vehicle and host details |
| `maxItems` | integer | Maximum vehicles |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/turo-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `make` | string |
| `model` | string |
| `year` | integer |
| `vehicleType` | string |
| `rating` | null |
| `completedTrips` | integer |
| `hostId` | integer |
| `city` | string |
| `state` | string |
| `country` | string |
| `latitude` | float |
| `longitude` | float |
| `location` | object |
| `images` | list |
| `averageDailyPrice` | object |
| `tripTotal` | float |
| `currency` | string |
| `quotedDailyPrice` | float |
| `quote` | object |
| `quoteStatus` | string |
| `startDateTime` | string |
| `endDateTime` | string |
| `searchVehicle` | object |
| `detail` | object |
| `host` | object |
| `detailStatus` | string |
| `hostStatus` | string |
| `scopeId` | string |
| `scrapedAt` | string |
| `description` | null |
| `owner` | object |
| `basicCarDetails` | object |
| `coverage` | object |

---

[← All scrapers](../../README.md)
