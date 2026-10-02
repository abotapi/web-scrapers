# Zonaprop Argentina Scraper

Scrape Zonaprop.com.ar property listings across Argentina. Extract 140+ fields including USD/ARS prices, price per m², expenses, area, rooms, bedrooms, bathrooms, GPS, descriptions, photos, agency contacts, phone and WhatsApp. Supports buy, rent, temporary listings, filters, sorting and URLs.

**[Open Zonaprop Argentina Scraper on Apify](https://apify.com/abotapi/zonaprop-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~zonaprop-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Capital Federal"], "operationType": "sale", "propertyType": "all", "currency": "any", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `locations` | array | Locations |
| `operationType` | string | Operation |
| `propertyType` | string | Property type |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `currency` | string | Currency |
| `minArea` | integer | Min area (m2) |
| `maxArea` | integer | Max area (m2) |
| `minRooms` | integer | Min rooms |
| `maxRooms` | integer | Max rooms |
| `minBedrooms` | integer | Min bedrooms |
| `sortBy` | string | Sort order |
| `urls` | array | Search URLs |
| `fetchDetails` | boolean | Fetch full description from each prope |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings |
| `proxy` | object | Proxy configuration |
| `allowProxyDowngrade` | boolean | Allow cheaper proxy when the site perm |
| `residentialCap` | integer | Residential request cap (per run) |
| `trafficBudgetMb` | integer | Traffic budget (MB, per run) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/zonaprop-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `postingId` | string |
| `postingCode` | string |
| `alphanumericKey` | string |
| `url` | string |
| `title` | string |
| `generatedTitle` | string |
| `description` | string |
| `propertyType` | string |
| `propertyTypeId` | string |
| `operationType` | string |
| `status` | string |
| `postingType` | string |
| `premier` | boolean |
| `reserved` | boolean |
| `isDuplicated` | null |
| `price` | integer |
| `priceFormatted` | string |
| `currency` | string |
| `priceUsd` | integer |
| `priceArs` | null |
| `prices` | list |
| `expenses` | integer |
| `expensesCurrency` | string |
| `expensesFormatted` | string |
| `totalArea` | integer |
| `coveredArea` | integer |
| `rooms` | integer |
| `bedrooms` | null |
| `bathrooms` | integer |
| `garages` | null |
| `age` | null |
| `areaUnit` | string |
| `address` | string |
| `addressVisibility` | string |
| `neighborhood` | string |
| `city` | string |
| `province` | string |
| `country` | string |
| `locationId` | string |
| `locationName` | string |

---

[← All scrapers](../../README.md)
