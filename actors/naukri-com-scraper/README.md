# Naukri.com Scraper

Scrape Naukri.com jobs by keyword or URL. Extract job title, company, skills, experience, salary, location and posting date, with optional full descriptions, education requirements and company details. Supports incremental monitoring and resume runs.

**[Open Naukri.com Scraper on Apify](https://apify.com/abotapi/naukri-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~naukri-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": ["python developer"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `keywords` | array | Job keywords |
| `location` | string | Location (optional) |
| `urls` | array | Job or search page links |
| `fetchDetails` | boolean | Fetch full job details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/naukri-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `jobId` | string |
| `kind` | string |
| `title` | string |
| `url` | string |
| `companyName` | string |
| `companyId` | integer |
| `companyLogo` | string |
| `skills` | list |
| `experience` | string |
| `minimumExperience` | integer |
| `maximumExperience` | integer |
| `salary` | string |
| `location` | string |
| `descriptionSnippet` | string |
| `vacancy` | integer |
| `postedDaysAgoLabel` | string |
| `postedAt` | string |
| `currency` | string |
| `walkinJob` | boolean |
| `searchScope` | string |
| `salaryDetail` | object |
| `companyRating` | object |
| `description` | string |
| `locations` | list |
| `companyDetails` | object |
| `education` | string |
| `employmentType` | string |
| `jobType` | string |
| `industry` | string |
| `functionalArea` | string |
| `jobRole` | string |
| `roleCategory` | string |
| `viewCount` | integer |
| `applyCount` | integer |

---

[← All scrapers](../../README.md)
