# Flightradar24 Scraper

Live aircraft positions by map area (callsign, lat/lng, altitude, speed, vertical speed, heading, squawk, registration, aircraft type, route, airline), airport departure and arrival boards, and aircraft or flight number history with times, delays and status, in one unified schema.

**[Open Flightradar24 Scraper on Apify](https://apify.com/abotapi/flightradar24-live-flight-tracker?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~flightradar24-live-flight-tracker/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "live", "bounds": ["55.0,45.0,-6.0,10.0"], "airports": ["LHR"], "boardMode": "departures", "historyQueries": ["G-TUKR"], "fetchBy": "reg", "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `bounds` | array | Map areas (bounding boxes) |
| `airports` | array | Airports (IATA codes) |
| `boardMode` | string | Board type |
| `historyQueries` | array | Registrations or flight numbers |
| `fetchBy` | string | Look up by |
| `urls` | array | Flightradar24 links |
| `flightNumbers` | array | Flight numbers or callsigns |
| `registrations` | array | Aircraft registrations |
| `airlines` | array | Airlines (ICAO or IATA) |
| `originAirports` | array | Origin airports |
| `destinationAirports` | array | Destination airports |
| `minAltitudeFt` | integer | Minimum altitude (feet) |
| `maxAltitudeFt` | integer | Maximum altitude (feet) |
| `includeOnGround` | boolean | Include aircraft on the ground |
| `includeGliders` | boolean | Include gliders |
| `maxItems` | integer | Max flights |
| `fetchDetails` | boolean | Add full flight detail (billed per enr |
| `includeTrail` | boolean | Include the recorded position trail |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/flightradar24-live-flight-tracker?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `recordType` | string |
| `fr24Id` | string |
| `callsign` | string |
| `flightNumber` | null |
| `registration` | null |
| `icao24` | null |
| `squawk` | null |
| `radarCode` | string |
| `aircraftCode` | string |
| `aircraftModel` | null |
| `airlineName` | null |
| `airlineIata` | null |
| `airlineIcao` | null |
| `originIata` | null |
| `originIcao` | null |
| `originName` | null |
| `originCity` | null |
| `originCountry` | null |
| `originLatitude` | null |
| `originLongitude` | null |
| `originTerminal` | null |
| `originGate` | null |
| `destinationIata` | null |
| `destinationIcao` | null |
| `destinationName` | null |
| `destinationCity` | null |
| `destinationCountry` | null |
| `destinationLatitude` | null |
| `destinationLongitude` | null |
| `destinationTerminal` | null |
| `destinationGate` | null |
| `latitude` | float |
| `longitude` | float |
| `altitudeFt` | integer |
| `groundSpeedKts` | integer |
| `verticalSpeedFpm` | integer |
| `headingDeg` | integer |
| `onGround` | boolean |
| `isGlider` | boolean |

---

[← All scrapers](../../README.md)
