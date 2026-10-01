# Booking.com Hotels Scraper

Scrape booking.com hotels, apartments, villas and hostels. Search any destination with the site's own filters (type, stars, review score, budget, meals, cancellation, amenities) or paste links. Live prices in 36 currencies, room-level rates, facilities, house rules and guest reviews.

**[Open Booking.com Hotels Scraper on Apify](https://apify.com/abotapi/booking-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~booking-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "destinations": ["Sydney"], "minReviewScore": "any", "sortBy": "relevance", "currency": "USD", "language": "en-us", "maxReviewsPerProperty": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `destinations` | array | Destinations |
| `propertyTypes` | array | Property type |
| `starRatings` | array | Property rating (stars) |
| `minReviewScore` | string | Minimum guest review score |
| `minPricePerNight` | integer | Min price per night |
| `maxPricePerNight` | integer | Max price per night |
| `mealPlans` | array | Meals |
| `reservationPolicies` | array | Reservation policy |
| `amenities` | array | Property amenities |
| `roomAmenities` | array | Room amenities |
| `bedPreferences` | array | Bed preference |
| `travelGroups` | array | Travel group |
| `sortBy` | string | Sort by |
| `urls` | array | Booking.com links |
| `checkIn` | string | Check-in date |
| `checkOut` | string | Check-out date |
| `adults` | integer | Adults |
| `childrenAges` | array | Children ages |
| `rooms` | integer | Rooms |
| `currency` | string | Currency |
| `language` | string | Language |
| `availableOnly` | boolean | Only properties available for these da |
| `minReviewCount` | integer | Minimum number of reviews |
| `excludeSoldOut` | boolean | Drop sold-out properties |
| `fetchDetails` | boolean | Read each property's own page |
| `maxReviewsPerProperty` | integer | Guest reviews per property |
| `maxItems` | integer | Max results |
| `maxPages` | integer | Max pages per destination |
| `proxy` | object | Connection |
| `maxNotifyProperties` | integer | Max properties to export |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/booking-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `propertyId` | string |
| `propertyName` | string |
| `propertyUrl` | string |
| `pageName` | string |
| `accommodationTypeId` | integer |
| `destinationId` | integer |
| `isClosed` | boolean |
| `isNewlyOpened` | boolean |
| `isSoldOut` | boolean |
| `isAvailableForDates` | boolean |
| `isSponsored` | boolean |
| `hostType` | string |
| `wishlistCount` | integer |
| `summary` | null |
| `starRating` | integer |
| `starRatingSymbol` | string |
| `reviewScore` | float |
| `reviewScoreLabel` | string |
| `reviewCount` | integer |
| `secondaryReviewScore` | float |
| `externalReviewScore` | null |
| `externalReviewCount` | null |
| `address` | string |
| `city` | string |
| `countryCode` | string |
| `latitude` | float |
| `longitude` | float |
| `displayLocation` | string |
| `distanceFromSearchCentre` | string |
| `distanceMetres` | null |
| `isCentrallyLocated` | boolean |
| `publicTransportDistance` | null |
| `beachDistance` | null |
| `mainPhoto` | string |
| `thumbnailPhoto` | string |
| `price` | object |
| `rooms` | list |
| `matchedUnit` | object |
| `mealPlanIncluded` | null |
| `freeCancellation` | boolean |

---

[← All scrapers](../../README.md)
