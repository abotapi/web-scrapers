# Yellow Pages NZ Scraper

Scrapes business listings from Yellow.co.nz (New Zealand Yellow Pages). Extract comprehensive business information, including contact details, emails, ratings, reviews, opening hours, and geo coordinates.

**[Open Yellow Pages NZ Scraper on Apify](https://apify.com/abotapi/yellow-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~yellow-nz-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"startUrls": [{"url": "https://yellow.co.nz/search?search_terms=Plumbers&geo_location_terms=Auckland"}, {"url": "https://yellow.co.nz/auckland/plumbers"}, {"url": "https://yellow.co.nz/auckland/bpp/onehunga-plumbers-579426046"}], "searchTerms": "Plumbers", "location": "New Zealand", "maxListings": 10, "maxPages": 1, "maxReviews": 10}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `startUrls` | array | Start URLs |
| `searchTerms` * | string | Search Terms |
| `location` * | string | Location |
| `searchQueries` | array | Search queries (several keywords) |
| `locations` | array | Locations (several places) |
| `minRating` | number | Minimum rating |
| `hasEmail` | boolean | Only businesses with an email |
| `hasWebsite` | boolean | Only businesses with a website |
| `maxListings` | integer | Max Listings |
| `maxPages` | integer | Maximum Pages |
| `maxConcurrency` | integer | Max Concurrency |
| `scrapeDetails` | boolean | Scrape Detail Pages |
| `maxReviews` | integer | Max Reviews per Business |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/yellow-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `name` | string |
| `detailUrl` | string |
| `phone` | string |
| `address` | string |
| `categories` | list |
| `rating` | integer |
| `reviewCount` | integer |
| `website` | string |
| `description` | string |
| `email` | string |
| `fullAddress` | object |
| `latitude` | float |
| `longitude` | float |
| `openingHours` | list |
| `paymentAccepted` | string |
| `imageUrl` | string |
| `logoUrl` | string |
| `reviews` | list |
| `yearEstablished` | string |
| `slogan` | string |
| `associations` | string |
| `generalInfo` | string |
| `searchTerms` | string |
| `searchLocation` | string |
| `businessId` | string |
| `listingUrl` | string |
| `category` | string |
| `street` | string |
| `city` | string |
| `region` | string |
| `postalCode` | string |
| `country` | string |
| `addressText` | string |
| `allEmails` | list |
| `emailSource` | string |
| `searchQuery` | string |
| `source` | string |
| `observedAt` | string |

---

[← All scrapers](../../README.md)
