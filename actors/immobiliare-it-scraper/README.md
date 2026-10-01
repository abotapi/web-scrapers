# Immobiliare.it Scraper

Extract property listings from Immobiliare.it with clean structured data including prices, descriptions, GPS coordinates, agency details, photos, and property attributes such as condition, heating, garage, floor, and features. Search by city, filters, or URL. Blazing fast, reliable.

**[Open Immobiliare.it Scraper on Apify](https://apify.com/abotapi/immobiliare-it-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~immobiliare-it-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Roma"], "contract": "sale", "category": "all", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `locations` | array | Cities |
| `contract` | string | Buy or rent |
| `category` | string | Property type |
| `minPrice` | integer | Min price (EUR) |
| `maxPrice` | integer | Max price (EUR) |
| `minSurface` | integer | Min surface (m²) |
| `maxSurface` | integer | Max surface (m²) |
| `minRooms` | integer | Min rooms |
| `maxRooms` | integer | Max rooms |
| `excludeAuctions` | boolean | Exclude auctions |
| `sortBy` | string | Sort order |
| `urls` | array | Search URLs |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (0  unlimited) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/immobiliare-it-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `uuid` | string |
| `url` | string |
| `title` | string |
| `contract` | string |
| `propertyType` | string |
| `propertyTypeId` | integer |
| `category` | string |
| `price` | integer |
| `priceFormatted` | string |
| `priceRange` | string |
| `priceVisible` | boolean |
| `currency` | string |
| `surface` | integer |
| `surfaceLabel` | string |
| `surfaceMin` | integer |
| `surfaceMax` | integer |
| `rooms` | integer |
| `roomsMin` | integer |
| `roomsMax` | integer |
| `isProject` | boolean |
| `unitCount` | integer |
| `bathrooms` | integer |
| `bedrooms` | integer |
| `floor` | string |
| `floorAbbreviation` | string |
| `elevator` | null |
| `condition` | string |
| `heating` | string |
| `garage` | null |
| `features` | list |
| `views` | list |
| `latitude` | float |
| `longitude` | float |
| `address` | string |
| `region` | string |
| `province` | string |
| `city` | string |
| `macrozone` | string |
| `microzone` | string |

---

[← All scrapers](../../README.md)
