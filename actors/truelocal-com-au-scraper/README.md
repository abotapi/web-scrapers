# TrueLocal AU Directory Listings & Reviews Scraper

Scrape TrueLocal.com.au business listings by keyword, location, or URL. Extract names, addresses, GPS coordinates, phones, emails, websites, ratings, and review counts. Optional review mode exports individual reviews with author, rating, text, and date. Automatic pagination included.

**[Open TrueLocal AU Directory Listings & Reviews Scraper on Apify](https://apify.com/abotapi/truelocal-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~truelocal-com-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["restaurants"], "locations": ["Sydney NSW"], "maxReviews": 10, "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Mode |
| `searchTerms` | array | Search terms (what) |
| `locations` | array | Locations (where) |
| `urls` | array | TrueLocal URLs |
| `fetchDetails` | boolean | Fetch profile pages (richer data) |
| `fetchReviews` | boolean | Include reviews (Search/URL modes) |
| `maxReviews` | integer | Max reviews per listing |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (total, default 20, 0  un |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/truelocal-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `name` | string |
| `description` | null |
| `categories` | list |
| `primaryCategory` | null |
| `categoryCodes` | list |
| `categoryId` | string |
| `phone` | null |
| `secondaryPhone` | null |
| `email` | null |
| `website` | null |
| `image` | null |
| `street` | null |
| `suburb` | null |
| `state` | null |
| `postcode` | null |
| `country` | null |
| `fullAddress` | null |
| `latitude` | null |
| `longitude` | null |
| `openingHours` | null |
| `holidayHours` | null |
| `permanentlyClosed` | boolean |
| `ratingValue` | null |
| `reviewCount` | null |
| `reviewsReturned` | integer |
| `reviews` | list |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
