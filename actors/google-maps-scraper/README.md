# Google Maps Scraper

Extract business data from Google Maps at scale. Get names, addresses, phone numbers, websites, ratings, reviews, opening hours, popular times, photos, and 40+ data points per listing.

**[Open Google Maps Scraper on Apify](https://apify.com/abotapi/google-maps-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~google-maps-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"searchStringsArray": ["restaurants"], "location": "New York, NY", "maxReviews": 10, "reviewsSort": "relevant", "language": "en", "proxyConfiguration": {"useApifyProxy": false}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `searchStringsArray` | array | Search Terms |
| `startUrls` | array | Start URLs |
| `location` | string | Location |
| `lat` | number | Latitude |
| `lng` | number | Longitude |
| `country` | string | Country |
| `state` | string | State/Region |
| `city` | string | City |
| `postalCode` | string | Postal Code |
| `customGeolocation` | object | Custom Geolocation (GeoJSON) |
| `zoom` | integer | Zoom Level |
| `maxResultsPerSearch` | integer | Max Results Per Search |
| `maxReviews` | integer | Max Reviews Per Business |
| `maxImages` | integer | Max Images Per Business |
| `reviewsSort` | string | Reviews Sort Order |
| `oneReviewPerRow` | boolean | One Review Per Row |
| `skipClosedPlaces` | boolean | Skip Closed Places |
| `language` | string | Language |
| `maxConcurrency` | integer | Max Concurrency |
| `proxyConfiguration` | object | Proxy Configuration |
| `resumeRunId` | string | Resume From Run ID (deprecated alias) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/google-maps-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `placeId` | string |
| `title` | string |
| `url` | string |
| `scrapedAt` | string |
| `categoryName` | string |
| `address` | string |
| `street` | string |
| `phone` | string |
| `totalScore` | float |
| `reviewsCount` | integer |
| `priceLevel` | string |
| `plusCode` | string |
| `imageUrls` | list |
| `openingHours` | list |
| `orderLinks` | list |
| `searchString` | string |
| `rank` | integer |
| `isAdvertisement` | boolean |
| `reviews` | list |

---

[← All scrapers](../../README.md)
