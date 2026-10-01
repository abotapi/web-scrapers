# HiJobs.net Scraper

Scrape hijobs.net job listings via the official mobile API: title, employer, salary range, location, hours, sector, contract, closing date, apply email and full description, plus employer record, industries and geo. Search by keywords, location and filters, or paste hijobs.net URLs. Includes.

**[Open HiJobs.net Scraper on Apify](https://apify.com/abotapi/hijobs-net-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~hijobs-net-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "sort": "added", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Mode |
| `keywords` | string | Keywords |
| `where` | string | Location / area |
| `employerType` | string | Employer type |
| `hours` | string | Hours |
| `contractType` | string | Contract type |
| `sort` | string | Sort order |
| `salaryFrom` | integer | Minimum salary |
| `salaryTo` | integer | Maximum salary |
| `postedWithinHours` | integer | Only jobs posted within the last N hou |
| `urls` | array | hijobs.net URLs |
| `fetchDetails` | boolean | Fetch full job details |
| `maxItems` | integer | Max jobs (total, default 20, 0  unlimi |
| `maxPages` | integer | Max result pages per search (0  unlimi |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/hijobs-net-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `source` | string |
| `sourceProvider` | string |
| `jobId` | string |
| `slug` | string |
| `jobUrl` | string |
| `scrapedAt` | string |
| `title` | string |
| `description` | string |
| `descriptionText` | string |
| `descriptionTeaser` | string |
| `postedDate` | string |
| `postedFriendly` | string |
| `postedRelative` | string |
| `closingDate` | string |
| `companyName` | string |
| `recruiterType` | string |
| `recruiterSlug` | string |
| `companyLogo` | string |
| `companyWebsite` | null |
| `contactName` | string |
| `employer` | object |
| `location` | string |
| `city` | null |
| `country` | null |
| `remote` | boolean |
| `latitude` | float |
| `longitude` | float |
| `salary` | object |
| `salaryRaw` | string |
| `salaryMin` | float |
| `salaryMax` | float |
| `categories` | list |
| `sector` | string |
| `specialism` | string |
| `employmentTypes` | list |
| `contractType` | string |
| `hours` | string |
| `hoursValue` | integer |
| `hoursGeneral` | string |

---

[← All scrapers](../../README.md)
