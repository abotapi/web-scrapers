# Sutochno.ru Scraper

Scrape Sutochno.ru short-term rentals, apartments and hotels by city, dates, guests or URL. Extract property details, stay prices, availability, ratings, guest reviews, amenities and owner information. Supports listing, hotel and search URLs for rental research and price comparison.

**[Open Sutochno.ru Scraper on Apify](https://apify.com/abotapi/sutochno-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~sutochno-ru-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "location": "Санкт-Петербург", "sortings": "relevance", "maxItems": 10, "maxPages": 1, "maxReviews": 10, "proxyConfiguration": {"useApifyProxy": true}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `location` | string | Location |
| `checkIn` | string | Check-in |
| `checkOut` | string | Check-out |
| `guestsAdults` | integer | Adults |
| `guestsChildrens` | array | Children ages |
| `pets` | boolean | Pets welcome |
| `sortings` | string | Sort |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per scope |
| `housingTypes` | array | Housing types |
| `stars` | array | Hotel stars |
| `minReviewScores` | array | Minimum review score |
| `bookingNow` | boolean | Instant booking only |
| `priceMin` | integer | Min price per night |
| `priceMax` | integer | Max price per night |
| `urls` | array | sutochno.ru links |
| `fetchDetails` | boolean | Fetch listing details |
| `fetchReviews` | boolean | Fetch guest reviews |
| `maxReviews` | integer | Max reviews per listing |
| `fetchAvailability` | boolean | Fetch stay pricing & availability |
| `availabilityDays` | integer | Availability window (nights) |
| `proxyConfiguration` | object | Proxy configuration |
| `changeScope` | string | Change scope (incremental mode only) |
| `compactUpdates` | boolean | Compact updates (incremental mode only |
| `expireAfterMissedScans` | integer | Expire after missed scans (incremental |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/sutochno-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `kind` | string |
| `objectId` | integer |
| `hotelId` | null |
| `hotelTitle` | null |
| `hotelType` | null |
| `hotelStars` | null |
| `title` | string |
| `typeTitle` | string |
| `url` | string |
| `pricePerNight` | integer |
| `priceFull` | integer |
| `priceWithoutDiscounts` | integer |
| `currency` | string |
| `rating` | float |
| `countReviews` | integer |
| `bookingNow` | boolean |
| `mediaUrls` | list |
| `photoCount` | integer |
| `address` | string |
| `cityId` | integer |
| `cityTitle` | string |
| `lat` | float |
| `lng` | float |
| `area` | integer |
| `bedrooms` | integer |
| `beds` | integer |
| `countBeds` | integer |
| `guests` | integer |
| `isChildrenAllowed` | boolean |
| `partyAllowed` | boolean |
| `forCouple` | boolean |
| `ownerId` | integer |
| `metroStations` | list |
| `hotSale` | boolean |
| `externalReviews` | list |
| `wifi` | boolean |
| `parking` | null |
| `airConditioning` | null |
| `washmachine` | boolean |

---

[← All scrapers](../../README.md)
