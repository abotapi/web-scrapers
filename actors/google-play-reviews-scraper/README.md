# Google Play Reviews Scraper

Collect Google Play reviews and ratings for any app across country storefronts. Search by app name or use a Google Play URL. Returns one row per review with rating, text, author, date, app version, thumbs-up count, developer reply, and storefront country.

**[Open Google Play Reviews Scraper on Apify](https://apify.com/abotapi/google-play-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~google-play-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["Instagram"], "countries": ["us"], "language": "en", "sortBy": "newest", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | App name searches |
| `appsPerQuery` | integer | Apps per search term |
| `urls` | array | Google Play URLs |
| `countries` | array | Countries |
| `language` | string | Language |
| `sortBy` | string | Sort reviews by |
| `minRating` | integer | Minimum rating |
| `maxRating` | integer | Maximum rating |
| `fetchDetails` | boolean | Enrich with app details |
| `maxItems` | integer | Max reviews |
| `maxPages` | integer | Max pages per country |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/google-play-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `reviewId` | string |
| `appId` | string |
| `appName` | null |
| `country` | string |
| `language` | string |
| `rating` | integer |
| `body` | string |
| `author` | string |
| `authorId` | string |
| `authorImage` | string |
| `thumbsUp` | integer |
| `appVersion` | string |
| `reviewDate` | string |
| `reviewTimestamp` | integer |
| `reviewUrl` | string |
| `developerReply` | null |
| `developerReplyDate` | null |

---

[← All scrapers](../../README.md)
