# GetYourGuide Scraper

Scrape GetYourGuide tours and activities by keyword, city or link. Get prices, discounts, ratings, review counts, duration, languages, activity provider, categories, badges, highlights, meeting-point coordinates, images and traveler reviews with provider replies and photos.

**[Open GetYourGuide Scraper on Apify](https://apify.com/abotapi/getyourguide-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~getyourguide-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["paris"], "sortBy": "popularity", "minRating": "0", "maxPages": 1, "maxItems": 10, "maxReviewsPerActivity": 10, "minReviewRating": "0", "currency": "USD", "language": "en-US", "proxy": {"useApifyProxy": true}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search queries |
| `sortBy` | string | Sort by |
| `minRating` | string | Minimum rating |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `languages` | array | Tour languages |
| `durations` | array | Duration |
| `freeCancellationOnly` | boolean | Free cancellation only |
| `skipTheLineOnly` | boolean | Skip-the-line only |
| `urls` | array | Links |
| `fetchDetails` | boolean | Fetch full activity details |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max items |
| `maxReviewsPerActivity` | integer | Max reviews per activity |
| `minReviewRating` | string | Minimum review rating |
| `reviewLanguages` | array | Review languages |
| `reviewTravelerTypes` | array | Traveler types |
| `reviewsWithTextOnly` | boolean | Only reviews with written text |
| `currency` | string | Currency |
| `language` | string | Site language |
| `proxy` | object | Proxy configuration |
| `changeScope` | string | What counts as a change (incremental m |
| `compactUpdates` | boolean | Slim UPDATED and EXPIRED rows (increme |
| `expireAfterMissedScans` | integer | Missed scans before EXPIRED (increment |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/getyourguide-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `source` | string |
| `activityId` | integer |
| `title` | string |
| `url` | string |
| `description` | string |
| `priceFrom` | float |
| `originalPrice` | float |
| `priceFromFormatted` | string |
| `discountPercent` | float |
| `priceCurrency` | string |
| `priceUnit` | string |
| `rating` | float |
| `reviewCount` | integer |
| `duration` | string |
| `durationText` | string |
| `freeCancellation` | boolean |
| `skipTheLine` | boolean |
| `mustBookOnline` | boolean |
| `badges` | list |
| `categories` | list |
| `highlights` | list |
| `languages` | null |
| `supplier` | string |
| `availability` | string |
| `nextAvailableAt` | string |
| `imageUrl` | string |
| `images` | list |
| `city` | string |
| `cityId` | integer |
| `position` | integer |
| `isBestseller` | boolean |
| `bookedIn24Hours` | integer |
| `bookedYesterdayText` | string |
| `audioGuide` | null |
| `pickupAvailable` | boolean |
| `wheelchairAccessible` | null |
| `privateGroup` | boolean |
| `searchQuery` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
