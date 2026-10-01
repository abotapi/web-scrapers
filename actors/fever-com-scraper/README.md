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
  -d '{"mode": "search", "cities": ["new-york"], "locale": "en", "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `cities` | array | Cities |
| `locale` | string | Language |
| `category` | string | Category (optional) |
| `query` | string | Keyword filter (optional) |
| `urls` | array | Fever URLs |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `fetchDetails` | boolean | Fetch event details |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |

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
| `priceText` | null |
| `originalPrice` | null |
| `onSale` | null |
| `discountPercent` | null |
| `currency` | string |
| `priceType` | string |
| `startDate` | string |
| `endDate` | null |
| `sessionDate` | null |
| `venueName` | null |
| `venueAddress` | null |
| `latitude` | null |
| `longitude` | null |
| `rating` | null |
| `ratingCount` | null |
| `isNew` | boolean |
| `imageUrl` | null |
| `description` | null |
| `categories` | list |
| `firstSessionDate` | null |
| `lastSessionDate` | null |
| `ticketsAvailable` | null |
| `sessionsText` | null |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
