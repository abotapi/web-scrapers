# Herold.at Scraper

Scrape Herold.at business listings across Austria into clean JSON. Extract names, addresses, GPS, phone numbers, emails, websites, ratings, reviews, opening hours, payment methods, and founding dates by category, city, or region.

**[Open Herold.at Scraper on Apify](https://apify.com/abotapi/herold-at-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~herold-at-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "categories": ["restaurant"], "locations": ["wien"], "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AT"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `categories` | array | Category slugs |
| `locations` | array | Location slugs (optional) |
| `urls` | array | Search URLs (URL mode) |
| `verifiedOnly` | boolean | Verified businesses only (post-filter) |
| `ratedOnly` | boolean | Rated businesses only (post-filter) |
| `minRating` | integer | Minimum average rating (post-filter) |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (total) |
| `fetchDetails` | boolean | Fetch detail pages (richer data, slowe |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/herold-at-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `name` | string |
| `category` | string |
| `regionSlug` | string |
| `position` | integer |
| `isVerified` | boolean |
| `breadcrumb` | null |
| `streetAddress` | string |
| `postalCode` | string |
| `addressLocality` | string |
| `addressRegion` | string |
| `addressCountry` | string |
| `latitude` | null |
| `longitude` | null |
| `telephone` | string |
| `email` | string |
| `website` | string |
| `logoUrl` | string |
| `primaryImage` | string |
| `imageCount` | integer |
| `foundingDate` | null |
| `branchCode` | string |
| `paymentAccepted` | list |
| `openingHours` | list |
| `ratingValue` | float |
| `ratingCount` | integer |
| `reviewCount` | null |
| `bestRating` | integer |
| `worstRating` | integer |
| `reviews` | list |
| `description` | null |
| `services` | list |
| `branchen` | list |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
