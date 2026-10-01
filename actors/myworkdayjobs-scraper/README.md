# Workday Jobs Scraper

Scrape job postings from any Workday-hosted careers site on Myworkdayjobs.com. Paste careers-page or job URLs and get structured job data, including title, full description, locations, time type, posting dates, employer, apply URL, country, and geo data.

**[Open Workday Jobs Scraper on Apify](https://apify.com/abotapi/myworkdayjobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~myworkdayjobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "maxItems": 10, "proxy": {"useApifyProxy": true}, "residentialCountries": ["US", "GB", "DE", "CA", "AU", "FR", "NL", "SG"]}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Start mode |
| `companyUrls` | array | Company careers sites |
| `keyword` | string | Keyword |
| `jobCategory` | string | Job category |
| `jobType` | string | Job type |
| `timeType` | string | Time type |
| `location` | string | Location |
| `urls` | array | Workday URLs |
| `fetchDetails` | boolean | Fetch full job details |
| `maxItems` | integer | Max jobs |
| `proxy` | object | Proxy configuration |
| `residentialCountries` | array | Residential country rotation |
| `residentialBudgetGb` | string | Residential traffic budget (GB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/myworkdayjobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `rowType` | string |
| `source` | object |
| `jobReqId` | string |
| `postingInternalId` | string |
| `jobPostingId` | string |
| `jobPostingSiteId` | string |
| `questionnaireId` | string |
| `title` | string |
| `jobUrl` | string |
| `externalPath` | string |
| `postedOn` | string |
| `startDate` | string |
| `timeType` | string |
| `posted` | boolean |
| `canApply` | boolean |
| `includeResumeParsing` | boolean |
| `locationText` | string |
| `country` | string |
| `employerName` | string |
| `description` | string |
| `descriptionText` | string |
| `salary` | object |
| `applyUrl` | string |
| `applyType` | string |
| `externalUrl` | string |
| `location` | object |
| `employer` | object |
| `hiringOrganization` | object |
| `similarJobs` | list |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
