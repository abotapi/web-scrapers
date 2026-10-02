# Traveloka Hotel Scraper

Scrape Traveloka hotels across Singapore, Malaysia, Indonesia, Thailand, Vietnam and the Philippines: nightly prices, star ratings, guest scores, coordinates and photos by city. Paste search or hotel links, and monitor price changes with recurring updates.

**[Open Traveloka Hotel Scraper on Apify](https://apify.com/abotapi/traveloka-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~traveloka-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "market": "en-sg", "locations": ["Singapore"], "sortBy": "popularity", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `market` | string | Market (site locale) |
| `locations` | array | Cities or areas |
| `checkInDate` | string | Check-in date |
| `checkOutDate` | string | Check-out date |
| `adults` | integer | Adults |
| `rooms` | integer | Rooms |
| `sortBy` | string | Sort results by |
| `minPrice` | integer | Min nightly price |
| `maxPrice` | integer | Max nightly price |
| `minStarRating` | integer | Min star rating |
| `minGuestRating` | number | Min guest score (0-10) |
| `urls` | array | Traveloka links |
| `fetchDetails` | boolean | Enrich each hotel (facilities, feature |
| `fetchReviews` | boolean | Read guest reviews per hotel |
| `maxReviews` | integer | Max reviews per hotel |
| `maxItems` | integer | Max results |
| `maxPages` | integer | Max pages per location |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/traveloka-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `hotelId` | string |
| `name` | string |
| `url` | string |
| `locationName` | string |
| `region` | string |
| `address` | null |
| `price` | float |
| `priceMinor` | integer |
| `currency` | string |
| `starRating` | integer |
| `guestRating` | float |
| `guestRatingMax` | integer |
| `guestRatingLabel` | string |
| `numReviews` | integer |
| `latitude` | float |
| `longitude` | float |
| `facilities` | list |
| `facilityCodes` | list |
| `imageUrl` | string |
| `imageUrls` | list |
| `market` | string |
| `checkInDate` | string |
| `checkOutDate` | string |
| `changeType` | string |
| `changedFields` | list |
| `firstSeenAt` | string |
| `lastSeenAt` | string |

---

[← All scrapers](../../README.md)
