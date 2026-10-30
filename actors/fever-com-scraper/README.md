# Fever Scraper

Scrape Fever events by city, category, keyword or URL. Extract from-prices, venues, dates and ratings, with optional enrichment for event descriptions, venue addresses and available sessions.

**[Open Fever Scraper on Apify](https://apify.com/abotapi/fever-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~fever-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "cities": ["new-york"], "locale": "en", "maxReviewsPerEvent": 10, "maxItems": 10, "proxy": {"useApifyProxy": true}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `cities` | array | Cities |
| `queryType` | string | Query type (alias) |
| `city` | string | City (alias) |
| `locale` | string | Language |
| `category` | string | Category (optional) |
| `query` | string | Keyword filter (optional) |
| `urls` | array | Fever URLs |
| `id` | string | Event ID (alias) |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `fetchDetails` | boolean | Fetch event details |
| `maxReviewsPerEvent` | integer | Guest reviews per event |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |
| `changeScope` | string | Change scope (incremental mode only) |
| `compactUpdates` | boolean | Compact UPDATED rows (incremental mode |
| `expireAfterMissedScans` | integer | Expire after N missed scans (increment |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/fever-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `rowType` | string |
| `eventId` | string |
| `url` | string |
| `title` | string |
| `citySlug` | string |
| `locale` | string |
| `category` | null |
| `priceFrom` | float |
| `priceText` | string |
| `originalPrice` | float |
| `onSale` | boolean |
| `discountPercent` | float |
| `currency` | string |
| `priceType` | string |
| `startDate` | string |
| `endDate` | string |
| `sessionDate` | null |
| `venueName` | string |
| `venueAddress` | null |
| `latitude` | null |
| `longitude` | null |
| `rating` | float |
| `ratingCount` | integer |
| `isNew` | boolean |
| `imageUrl` | string |
| `description` | null |
| `categories` | list |
| `firstSessionDate` | null |
| `lastSessionDate` | null |
| `ticketsAvailable` | null |
| `sessionsText` | null |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
