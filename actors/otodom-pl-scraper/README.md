# Otodom.pl Scraper

Scrape Otodom.pl properties for sale and rent, including apartments, houses, plots, commercial spaces, garages, rooms and new developments. Build searches by city, transaction, property type and filters, or paste Otodom URLs directly.

**[Open Otodom.pl Scraper on Apify](https://apify.com/abotapi/otodom-pl-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~otodom-pl-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "transaction": "sprzedaz", "estate": "mieszkanie", "locations": ["Warszawa"], "marketType": "all", "sortBy": "DEFAULT", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "PL"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `transaction` | string | Transaction |
| `estate` | string | Property type |
| `locations` | array | Cities |
| `marketType` | string | Market type |
| `minPrice` | integer | Min price (PLN) |
| `maxPrice` | integer | Max price (PLN) |
| `minArea` | integer | Min area (m²) |
| `maxArea` | integer | Max area (m²) |
| `minRooms` | integer | Min rooms |
| `maxRooms` | integer | Max rooms |
| `sortBy` | string | Sort order |
| `urls` | array | Search URLs (URL mode) |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (total) |
| `fetchDetails` | boolean | Fetch detail pages (richer data, slowe |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/otodom-pl-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `transaction` | string |
| `estate` | string |
| `priceTotal` | integer |
| `priceCurrency` | string |
| `pricePerSquareMeter` | float |
| `rentPrice` | integer |
| `rentAdditional` | integer |
| `deposit` | null |
| `areaInSquareMeters` | float |
| `rooms` | integer |
| `floor` | string |
| `buildingFloors` | integer |
| `buildYear` | integer |
| `marketType` | string |
| `ownership` | string |
| `buildingType` | string |
| `buildingMaterial` | string |
| `heating` | string |
| `windowsType` | string |
| `city` | string |
| `province` | string |
| `district` | string |
| `street` | null |
| `postalCode` | null |
| `latitude` | float |
| `longitude` | float |
| `agencyName` | null |
| `advertiserType` | string |
| `contactName` | string |
| `phone` | string |
| `contactDetails` | object |
| `agency` | null |
| `owner` | object |
| `referenceId` | string |
| `description` | string |
| `features` | list |
| `isPromoted` | boolean |

---

[← All scrapers](../../README.md)
