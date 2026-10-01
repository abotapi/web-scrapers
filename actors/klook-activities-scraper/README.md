# Klook Scraper

Scrape Klook activities, tours, attractions and travel experiences from search pages or activity URLs. Extract structured data for destinations, prices, ratings, availability, images, package details and more.

**[Open Klook Scraper on Apify](https://apify.com/abotapi/klook-activities-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~klook-activities-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"operation": "activities", "mode": "search", "query": "Tokyo", "currency": "USD", "checkIn": "30 days", "hotelSort": "recommended", "minHotelRating": "0", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `operation` | string | Klook data type |
| `mode` * | string | Mode |
| `query` | string | Search query |
| `currency` | string | Currency |
| `urls` | array | Klook URLs |
| `checkIn` | string | Check-in date |
| `checkOut` | string | Check-out date |
| `adults` | integer | Adults |
| `rooms` | integer | Rooms |
| `childrenAges` | array | Children ages |
| `hotelSort` | string | Sort hotels by |
| `starRatings` | array | Hotel star ratings |
| `minHotelRating` | string | Minimum hotel review score |
| `minNightlyPrice` | integer | Minimum nightly price |
| `maxNightlyPrice` | integer | Maximum nightly price |
| `freeCancellation` | boolean | Free cancellation |
| `breakfastIncluded` | boolean | Breakfast included |
| `fetchDetails` | boolean | Fetch activity details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max search pages |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/klook-activities-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `activityId` | string |
| `recordType` | string |
| `title` | string |
| `url` | string |
| `price` | float |
| `currency` | string |
| `marketPrice` | null |
| `rating` | float |
| `reviewCount` | integer |
| `location` | string |
| `category` | string |
| `imageUrls` | list |
| `promotions` | list |
| `booked` | string |
| `description` | string |
| `country` | string |
| `address` | string |
| `detailStatus` | string |
| `operation` | string |
| `sourceMode` | string |
| `changeType` | string |

---

[← All scrapers](../../README.md)
