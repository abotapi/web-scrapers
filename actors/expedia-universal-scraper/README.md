# Expedia Hotels Scraper

Scrape Expedia.com hotel listings and reviews for any destination. Extract prices, ratings, review text, photos, location details, hotel information, and more in clean, structured data.

**[Open Expedia Hotels Scraper on Apify](https://apify.com/abotapi/expedia-universal-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~expedia-universal-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "destination": "Paris", "destinationId": "2734", "checkIn": "1 day", "checkOut": "2 days", "sortBy": "RECOMMENDED", "maxReviewsPerHotel": 10, "currency": "USD", "locale": "en_US", "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Scraping mode |
| `destination` | string | Destination |
| `destinationId` | string | Destination ID (optional) |
| `startUrls` | array | Hotel URLs |
| `checkIn` * | string | Check in Date |
| `checkOut` * | string | Check out Date |
| `adults` | integer | Adults |
| `children` | array | Children Ages |
| `rooms` | integer | Rooms |
| `minPrice` | integer | Min Price per Night |
| `maxPrice` | integer | Max Price per Night |
| `starRatings` | array | Star Ratings Filter |
| `sortBy` | string | Sort |
| `reviewsOnly` | boolean | Scrape reviews only |
| `includeReviews` | boolean | Include reviews in hotel cards |
| `maxReviewsPerHotel` | integer | Max Reviews per Hotel |
| `reviewsFrom` | string | Reviews From Date |
| `includeCategoryRatings` | boolean | Include Category Ratings |
| `currency` | string | Currency |
| `locale` | string | Locale |
| `maxItems` | integer | Max Items |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/expedia-universal-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `mode` | string |
| `placeName` | string |
| `hotelId` | string |
| `hotelUrl` | string |
| `hotelOverallRating` | float |
| `hotelRatingLabel` | string |
| `hotelTotalReviews` | integer |
| `provider` | string |
| `scrapedAt` | string |
| `extra` | object |

---

[← All scrapers](../../README.md)
