# Award Flight Scraper

Scrape award flight availability from Flightpoints.com and Roame.travel by route and date. Compare miles, taxes, available seats, cabins, stops, fare classes, loyalty programs and operating airlines. Includes per-cabin details across dozens of loyalty programs.

**[Open Award Flight Scraper on Apify](https://apify.com/abotapi/flightpoints-award-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

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
| `origin` | string | Origin |
| `destination` | string | Destination |
| `departureDate` | string | Departure date |
| `routes` | array | Bulk routes |
| `sources` | array | Sources |
| `urls` | array | Search links |
| `searchClass` | string | Cabin |
| `daysAround` | integer | days window |
| `directOnly` | boolean | Direct flights only |
| `startDate` | string | Window start date |
| `endDate` | string | Window end date |
| `cabin` | string | Cabin filter |
| `maxMiles` | integer | Max miles |
| `maxCashTaxes` | number | Max cash taxes |
| `minSeats` | integer | Min seats |
| `nonstop` | boolean | Nonstop only |
| `issuers` | array | Programs (issuers) |
| `operatingAirlines` | array | Operating airlines |
| `sortBy` | string | Prioritize cabin |
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
| `economy` | object |
| `premiumEconomy` | object |
| `business` | object |
| `first` | null |
| `stops` | integer |
| `originName` | string |
| `destinationName` | string |
| `coordinates` | object |
| `searchId` | string |
| `flightId` | string |
| `connections` | list |
| `airlines` | list |

---

[← All scrapers](../../README.md)
