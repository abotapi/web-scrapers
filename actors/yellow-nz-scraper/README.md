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
  -d '{"searchTerms": "Plumbers", "location": "New Zealand", "maxPages": 1, "maxListings": 10}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `searchTerms` * | string | Search Terms |
| `location` * | string | Location |
| `maxPages` | integer | Maximum Pages |
| `maxListings` | integer | Max Listings |
| `scrapeDetails` | boolean | Scrape Detail Pages |
| `maxConcurrency` | integer | Max Concurrency |
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
| `openStatus` | string |
| `description` | string |
| `email` | string |
| `fullAddress` | object |
| `latitude` | float |
| `longitude` | float |
| `rating` | integer |
| `reviewCount` | integer |
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

---

[← All scrapers](../../README.md)
