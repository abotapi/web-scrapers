# JobStreet Scraper

Pull JobStreet company profiles and employee reviews across Malaysia, Singapore, Indonesia, and the Philippines. Search by company, industry, or URL. Returns rich company records with embedded reviews or flat review datasets, with optional open job listings included.

**[Open JobStreet Scraper on Apify](https://apify.com/abotapi/jobstreet-companies-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~jobstreet-companies-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "companies", "country": "MY", "industry": "Information & Communication Technology", "maxReviewsPerCompany": 10, "reviewSort": "helpful", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `country` | string | Country |
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

Full details on the [scraper page](https://apify.com/abotapi/jobstreet-companies-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

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
| `coverImageUrl` | string |
| `industry` | string |
| `totalJobs` | integer |
| `ratingOverall` | integer |
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
