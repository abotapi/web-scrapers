# PagesJaunes FR Scraper

Scrapes business listings from PagesJaunes.fr (French Yellow Pages). Extract comprehensive business information, including contact details, ratings, reviews, opening hours, payment methods, and category hierarchy across all of France.

**[Open PagesJaunes FR Scraper on Apify](https://apify.com/abotapi/pagesjaunes-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~pagesjaunes-fr-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": "plombier", "location": "Paris", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | string | Search Terms (quoiqui) |
| `location` | string | Location (ou) |
| `urls` | array | PagesJaunes search URLs |
| `maxPages` | integer | Maximum Pages |
| `maxListings` | integer | Max listings total |
| `scrapeDetails` | boolean | Scrape Detail Pages |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/pagesjaunes-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `clientId` | string |
| `name` | string |
| `detailUrl` | string |
| `activities` | list |
| `address` | string |
| `phone` | string |
| `description` | string |
| `paymentAccepted` | string |
| `businessType` | string |
| `fullAddress` | object |
| `rating` | integer |
| `reviewCount` | integer |
| `imageUrl` | string |
| `reviews` | list |
| `breadcrumb` | list |
| `services` | list |
| `website` | string |
| `facebook` | string |
| `photos` | list |
| `searchTerms` | string |
| `searchLocation` | string |

---

[← All scrapers](../../README.md)
