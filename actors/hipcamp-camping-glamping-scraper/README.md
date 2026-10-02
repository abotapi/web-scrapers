# Hipcamp Scraper

Scrape Hipcamp campgrounds, RV parks, glamping and unique stays by US or AU region or listing link: price per night, rating, reviews, host, amenities, sites, photos, coordinates. Incremental monitoring, resume, MCP export.

**[Open Hipcamp Scraper on Apify](https://apify.com/abotapi/hipcamp-camping-glamping-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~hipcamp-camping-glamping-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "regions": ["california"], "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `regions` | array | Regions |
| `listingInputs` | array | Listing links |
| `urls` | array | Listing links (alias) |
| `maxItems` | integer | Max items |
| `fetchDetails` | boolean | Read full detail for front-page listin |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/hipcamp-camping-glamping-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `listingId` | string |
| `maskedId` | string |
| `url` | string |
| `title` | string |
| `pricePerNight` | float |
| `totalPricePerNight` | float |
| `currency` | string |
| `recommendsPercentage` | integer |
| `recommendsCount` | integer |
| `bookingsCount` | integer |
| `favoritesCount` | integer |
| `campsitesCount` | integer |
| `landCategory` | string |
| `latitude` | float |
| `longitude` | float |
| `cityName` | string |
| `countyName` | string |
| `stateName` | string |
| `stateAbbrvName` | string |
| `countryCode` | string |
| `accommodationTypes` | list |
| `isStarHost` | boolean |
| `summary` | string |
| `tileSummary` | string |
| `imageUrl` | string |
| `photoFilenames` | list |
| `detailLoaded` | boolean |
| `raw` | object |

---

[← All scrapers](../../README.md)
