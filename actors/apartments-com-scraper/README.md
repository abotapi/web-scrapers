# Apartments.com Scraper

Scrape Apartments.com rentals by city, ZIP, neighborhood, address or URL. Extract rent, floorplans, available units, amenities, fees, schools, transit, ratings, reviews, photos, phone numbers and GPS coordinates.

**[Open Apartments.com Scraper on Apify](https://apify.com/abotapi/apartments-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~apartments-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Austin, TX"], "propertyType": "any", "bedrooms": "any", "lifestyle": "none", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `propertyType` | string | Property type |
| `bedrooms` | string | Bedrooms |
| `minRent` | integer | Min rent (USD/month) |
| `maxRent` | integer | Max rent (USD/month) |
| `lifestyle` | string | Lifestyle / amenity |
| `urls` | array | URLs |
| `fetchDetails` | boolean | Fetch full property details |
| `maxPages` | integer | Max result pages per location/URL |
| `maxListings` | integer | Max properties (default 20, 0  unlimit |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/apartments-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `error` | boolean |
| `code` | string |
| `message` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
