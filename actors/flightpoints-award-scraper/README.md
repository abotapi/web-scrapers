# Flightpoints & Roame Award Flight Scraper

Multi-source award flight availability from Flightpoints.com + Roame.travel. Search any route and date for miles, taxes, available seats, cabins, stops, loyalty program and operating airline per itinerary — across dozens of loyalty programs. Per-cabin miles/taxes/seats/stops, fare-class.

**[Open Flightpoints & Roame Award Flight Scraper on Apify](https://apify.com/abotapi/flightpoints-award-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~flightpoints-award-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "origin": "JFK", "destination": "LHR", "sources": ["flightpoints", "roame"], "searchClass": "ECON", "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `origin` | string | Origin (IATA) |
| `destination` | string | Destination (IATA) |
| `departureDate` | string | Departure date |
| `routes` | array | Bulk routes |
| `sources` | array | Sources |
| `urls` | array | Search links |
| `searchClass` | string | Cabin |
| `daysAround` | integer | days window |
| `directOnly` | boolean | Direct flights only |
| `maxItems` | integer | Max itineraries |
| `fetchDetails` | boolean | Add flight detail (billed per enriched |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/flightpoints-award-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `source` | string |
| `origin` | string |
| `destination` | string |
| `departureDate` | string |
| `program` | string |
| `programName` | string |
| `airline` | string |
| `alliance` | string |
| `durationMinutes` | null |
| `numStops` | integer |
| `cabins` | object |
| `lastSeen` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
