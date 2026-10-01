# SEEK Company Reviews Scraper

Scrape SEEK Australia and New Zealand company profiles and employee reviews. Choose aggregated company data with top reviews or one row per review for sentiment analysis. Region is auto-detected from each URL, with clean structured output ready for analytics.

**[Open SEEK Company Reviews Scraper on Apify](https://apify.com/abotapi/seek-companies-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~seek-companies-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "companies", "region": "AU", "industry": "Mining, Resources & Energy", "maxReviewsPerCompany": 10, "reviewSort": "helpful", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `region` | string | Region |
| `urls` | array | Company URLs |
| `keywords` | string | Keywords |
| `industry` | string | Industry |
| `maxReviewsPerCompany` | integer | Max reviews per company |
| `reviewSort` | string | Review sort order |
| `includeAISummary` | boolean | Include AI review summary |
| `includeJobs` | boolean | Include open jobs |
| `maxJobsPerCompany` | integer | Max jobs per company |
| `maxItems` | integer | Max items to return |
| `maxTimeSec` | integer | Max run time (seconds) |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/seek-companies-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `slug` | string |
| `url` | string |
| `region` | string |
| `name` | string |
| `isClaimed` | boolean |
| `logoUrl` | string |
| `totalJobs` | integer |
| `ratingOverall` | float |
| `reviewCount` | integer |
| `salaryRating` | integer |
| `recommendedPercent` | integer |
| `ratingBreakdown` | object |
| `categoryRatings` | list |
| `topReviews` | list |
| `topReviewCount` | integer |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
