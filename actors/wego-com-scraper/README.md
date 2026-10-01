# Wego Scraper

Scrape Wego hotels by city or search URL. Get rates, providers, booking links, coordinates, scores, images and property details. Optionally fetch guest review text, ratings, dates and public author details.

**[Open Wego Scraper on Apify](https://apify.com/abotapi/wego-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~wego-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Dubai"], "currency": "USD", "sortBy": "popularity", "maxReviewsPerHotel": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Cities |
| `checkIn` | string | Check-in date |
| `checkOut` | string | Check-out date |
| `rooms` | integer | Rooms |
| `adults` | integer | Adults per room |
| `currency` | string | Currency |
| `urls` | array | Wego hotels search URLs |
| `starRatings` | array | Star ratings |
| `minPriceUsd` | integer | Minimum total price (USD) |
| `maxPriceUsd` | integer | Maximum total price (USD) |
| `freeCancellationOnly` | boolean | Free cancellation only |
| `sortBy` | string | Order the returned rows by |
| `fetchDetails` | boolean | Fetch hotel details |
| `fetchReviews` | boolean | Fetch guest reviews |
| `maxReviewsPerHotel` | integer | Max reviews per hotel |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max feed polls per city |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/wego-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `hotelId` | integer |
| `rowType` | string |
| `name` | string |
| `url` | string |
| `star` | integer |
| `propertyTypeId` | integer |
| `brandId` | integer |
| `chainId` | integer |
| `cityCode` | string |
| `cityName` | string |
| `countryCode` | null |
| `districtId` | integer |
| `latitude` | float |
| `longitude` | float |
| `distanceToCityCentreKm` | float |
| `distanceToNearestAirportKm` | float |
| `reviewScore` | integer |
| `reviewCount` | integer |
| `reviewBreakdown` | list |
| `latestPositiveComment` | string |
| `aiReviewHighlights` | list |
| `badges` | list |
| `imageUrl` | string |
| `imageUrls` | list |
| `images` | list |
| `imagesCount` | integer |
| `amenityIds` | list |
| `tagIds` | list |
| `roomAmenityIds` | list |
| `themeIds` | list |
| `capacity` | integer |
| `bedroomsCount` | integer |
| `bedsCount` | integer |
| `bathroomsCount` | integer |
| `newHotel` | boolean |
| `newlyRenovated` | boolean |
| `priceAmount` | integer |
| `priceCurrency` | string |
| `priceUsd` | float |

---

[← All scrapers](../../README.md)
