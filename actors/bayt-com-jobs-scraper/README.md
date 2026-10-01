# Bayt.com Scraper

Scrape Bayt.com job listings by keyword, country, or URL. Extract structured data including job title, company, location, salary, experience, career level, posting date, work style, and full job description. Built for recruitment, job aggregation, market research, and workforce analytics.

**[Open Bayt.com Scraper on Apify](https://apify.com/abotapi/bayt-com-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~bayt-com-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "country": "uae", "keyword": "accountant", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Mode |
| `country` | string | Country |
| `keyword` | string | Keyword / job title |
| `urls` | array | Search URLs |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (total, default 20, 0  un |
| `fetchDetails` | boolean | Fetch full job details |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/bayt-com-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `jobId` | string |
| `url` | string |
| `title` | string |
| `company` | null |
| `companyUrl` | null |
| `city` | null |
| `country` | null |
| `countrySlug` | string |
| `logo` | string |
| `salary` | string |
| `careerLevel` | string |
| `experience` | null |
| `workStyle` | null |
| `postedDate` | string |
| `postedTimestamp` | integer |
| `isExternal` | boolean |
| `isAggregated` | boolean |
| `easyApply` | boolean |
| `aiSummary` | string |
| `description` | string |
| `descriptionHtml` | string |
| `employmentType` | string |
| `datePosted` | string |
| `validThrough` | string |
| `vacancies` | integer |
| `companySize` | string |
| `companyIndustry` | null |
| `jobCountryCode` | string |
| `directApply` | boolean |
| `residenceLocation` | null |
| `nationality` | null |
| `gender` | null |
| `age` | null |
| `degree` | null |
| `major` | null |
| `preferredCandidate` | object |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
