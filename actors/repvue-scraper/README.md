# RepVue Scraper

Scrape RepVue company profiles, RepVue Score, sales-rep reviews, and compensation by role (OTE, base, percentiles) plus jobs and community Q&A. One rich record per company. Search and filter, or paste company links. Fast, reliable, runs on any plan.

**[Open RepVue Scraper on Apify](https://apify.com/abotapi/repvue-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~repvue-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "sortBy": "name_asc", "maxReviews": 10, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `search` | string | Company name contains |
| `industries` | array | Industries |
| `minRepvueScore` | integer | Minimum RepVue Score |
| `companySize` | string | Company size |
| `sortBy` | string | Sort results by |
| `startUrls` | array | Company URLs or slugs |
| `includeReviews` | boolean | Include reviews |
| `includeSalaries` | boolean | Include compensation |
| `includeJobs` | boolean | Include open jobs |
| `includeQuestions` | boolean | Include community Q&A |
| `maxReviews` | integer | Max reviews per company |
| `targetDate` | string | Reviews on or after (YYYY-MM-DD) |
| `maxItems` | integer | Max companies |
| `proxy` | object | Proxy |
| `maxResidentialMB` | integer | Residential traffic budget (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/repvue-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | integer |
| `active_jobs_count` | integer |
| `aged` | boolean |
| `average_rating` | string |
| `benefits_active` | boolean |
| `careers_url` | string |
| `culture_active` | boolean |
| `customer_claimed` | boolean |
| `description` | string |
| `fka` | null |
| `free_preview` | boolean |
| `funding_source` | string |
| `has_active_jobs` | boolean |
| `has_reviews` | boolean |
| `indexable` | boolean |
| `indexable_company_salaries` | boolean |
| `industry` | string |
| `last_headcount` | null |
| `logo` | string |
| `medical` | boolean |
| `name` | string |
| `published` | boolean |
| `published_reviews_count` | integer |
| `published_status` | string |
| `ratings_count` | integer |
| `reference_available` | boolean |
| `repvue_score` | null |
| `show_job_ads` | boolean |
| `show_performance_metrics` | boolean |
| `size` | string |
| `slug` | string |
| `top_percent` | null |
| `verified_ratings_count` | integer |
| `verified_ratings_percent` | integer |
| `website` | string |
| `url` | string |
| `repvueScore` | null |
| `averageRating` | float |
| `sizeLabel` | string |

---

[← All scrapers](../../README.md)
