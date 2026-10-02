# Trip.com Hotels Scraper

Pull structured hotel listings from trip.com with prices, room types, amenities, policies, nearby places, and full guest reviews with ratings breakdown and an AI review summary. Search by destination or paste trip.com URLs directly.

**[Open Trip.com Hotels Scraper on Apify](https://apify.com/abotapi/trip-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~trip-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["228|Tokyo"], "currency": "USD", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Destinations |
| `checkIn` | string | Check-in date |
| `checkOut` | string | Check-out date |
| `adults` | integer | Adults per room |
| `children` | integer | Children per room |
| `rooms` | integer | Number of rooms |
| `currency` | string | Currency |
| `minStarRating` | integer | Minimum star rating |
| `minReviewScore` | integer | Minimum guest review score |
| `urls` | array | Trip.com URLs |
| `fetchDetails` | boolean | Fetch hotel detail pages (rooms, polic |
| `maxPages` | integer | Max pages per destination |
| `maxListings` | integer | Max listings (total) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/trip-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `hotelId` | string |
| `name` | string |
| `starRating` | integer |
| `reviewScore` | float |
| `reviewScoreLabel` | string |
| `reviewCount` | integer |
| `reviewTags` | list |
| `address` | string |
| `lat` | float |
| `lng` | float |
| `priceCurrent` | integer |
| `priceOriginal` | integer |
| `priceTotalWithTaxes` | integer |
| `discountPercent` | integer |
| `discountLabel` | string |
| `currency` | string |
| `images` | list |
| `image` | string |
| `badges` | list |
| `medal` | null |
| `propertyTag` | string |
| `detailUrl` | string |
| `amenities` | list |
| `policies` | object |
| `nearbyPlaces` | list |
| `contactPhone` | string |
| `contactEmail` | string |
| `nearbyHotels` | list |
| `description` | string |
| `rooms` | list |
| `roomCount` | integer |
| `roomImages` | null |
| `confirmInfo` | null |
| `reviews` | list |
| `reviewCount_pushed` | integer |
| `aggregateTotalReviewCount` | integer |
| `aggregateRatingBreakdown` | object |
| `aggregateCommentTags` | list |
| `aggregateAiSummary` | string |
| `cityId` | integer |

---

[← All scrapers](../../README.md)
