# GasBuddy Scraper

Scrape GasBuddy station by station across the US and Canada. Returns brand, address, coordinates, phone, amenities, open status, ratings and reviews, plus the current cash and credit price for every fuel grade with who reported it and when. Incremental mode tracks price changes between runs.

**[Open GasBuddy Scraper on Apify](https://apify.com/abotapi/gasbuddy-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~gasbuddy-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["78701"], "fuelType": "regular", "maxPriceAgeHours": "0", "maxReviewsPerStation": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | What do you want to scrape |
| `locations` | array | Locations |
| `urls` | array | Station or search links |
| `brands` | array | Fuel brands |
| `fuelType` | string | Fuel grade |
| `maxPriceAgeHours` | string | Maximum price age (hours) |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `minStarRating` | integer | Minimum star rating |
| `amenities` | array | Required amenities |
| `openNowOnly` | boolean | Open right now only |
| `withPricesOnly` | boolean | Only stations with a reported price |
| `maxDistanceMiles` | integer | Max distance (miles) |
| `fetchReviews` | boolean | Include member reviews |
| `maxReviewsPerStation` | integer | Max reviews per station |
| `maxStations` | integer | Max stations |
| `maxPages` | integer | Max pages per location |
| `proxy` | object | Connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/gasbuddy-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `stationId` | string |
| `name` | string |
| `url` | string |
| `brand` | string |
| `brandId` | string |
| `brandLogoUrl` | string |
| `allBrands` | list |
| `addressLine1` | string |
| `addressLine2` | null |
| `city` | string |
| `state` | string |
| `postalCode` | string |
| `country` | string |
| `latitude` | float |
| `longitude` | float |
| `phone` | string |
| `distance` | null |
| `distanceMiles` | null |
| `openStatus` | string |
| `openingHours` | null |
| `nextOpenAt` | null |
| `nextCloseAt` | null |
| `amenities` | list |
| `amenityIds` | list |
| `fuels` | list |
| `prices` | list |
| `lowestPrice` | float |
| `lowestPriceFuelType` | string |
| `lastPriceReportedAt` | string |
| `lastPriceReportedBy` | string |
| `priceUnit` | string |
| `currency` | string |
| `starRating` | float |
| `ratingsCount` | integer |
| `reviewCount` | null |
| `reviews` | list |
| `topSpotters` | list |
| `priceTrend` | list |
| `offers` | list |
| `cardPaymentAvailable` | null |

---

[← All scrapers](../../README.md)
