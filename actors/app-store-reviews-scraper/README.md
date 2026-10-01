# Apple App Store Reviews Scraper

Scrape Apple App Store reviews across 150+ country storefronts. Search by app name or URL and extract ratings, review titles and text, authors, dates, app versions, and country in clean JSON, with optional app metadata enrichment.

**[Open Apple App Store Reviews Scraper on Apify](https://apify.com/abotapi/app-store-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~app-store-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["Instagram"], "countries": ["us"], "sortBy": "mostRecent", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | App name searches |
| `appsPerQuery` | integer | Apps per search term |
| `urls` | array | App Store URLs |
| `countries` | array | Countries |
| `sortBy` | string | Sort reviews by |
| `minRating` | integer | Minimum rating |
| `maxRating` | integer | Maximum rating |
| `fetchDetails` | boolean | Enrich with app details |
| `maxItems` | integer | Max reviews |
| `maxPages` | integer | Max pages per country |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/app-store-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `reviewId` | string |
| `appId` | string |
| `appName` | null |
| `country` | string |
| `rating` | integer |
| `title` | string |
| `body` | string |
| `author` | string |
| `authorId` | string |
| `authorUri` | string |
| `reviewUrl` | string |
| `appVersion` | string |
| `reviewDate` | string |
| `voteSum` | integer |
| `voteCount` | integer |
| `contentType` | string |

---

[← All scrapers](../../README.md)
