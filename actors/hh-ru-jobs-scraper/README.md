# HH.ru Jobs Scraper

Scrape HH.ru job listings with 50+ structured fields. Search by filters or URLs and extract salary, experience, schedule, employment type, and role. Detail enrichment adds full descriptions, key skills, contact information, and employer logos.

**[Open HH.ru Jobs Scraper on Apify](https://apify.com/abotapi/hh-ru-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~hh-ru-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["AI"], "searchField": "name", "areas": ["1"], "experience": "any", "orderBy": "relevance", "vacancyInput": ["https://hh.ru/vacancy/123456789", "123456790"], "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | 1. Search mode |
| `queries` | array | Search keywords (Search mode) |
| `searchField` | string | Where to match the keyword (Search mod |
| `areas` | array | Areas / regions to search (Search mode |
| `experience` | string | Work experience (Search mode) |
| `employment` | array | Employment type (Search mode) |
| `schedule` | array | Work schedule (Search mode) |
| `salaryMin` | integer | Minimum salary (Search mode) |
| `onlyWithSalary` | boolean | Only listings with salary (Search mode |
| `orderBy` | string | Sort order (Search mode) |
| `professionalRole` | array | Professional role IDs (Search mode) |
| `industry` | array | Industry IDs (Search mode) |
| `urls` | array | Search URLs (URL mode) |
| `vacancyInput` | array | Vacancy URLs or IDs (Vacancy mode) |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max total listings |
| `fetchDetails` | boolean | Visit each listing's detail page |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/hh-ru-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `vacancyId` | string |
| `url` | string |
| `name` | string |
| `publicationDate` | string |
| `creationDate` | string |
| `lastChangeTime` | string |
| `isAdv` | boolean |
| `searchUrl` | string |
| `searchSessionId` | string |
| `company` | object |
| `salaryFrom` | null |
| `salaryTo` | null |
| `salaryCurrency` | null |
| `salaryGross` | null |
| `salaryMode` | null |
| `salaryFrequency` | null |
| `compensation` | object |
| `area` | object |
| `address` | object |
| `workExperience` | string |
| `employment` | string |
| `employmentForm` | string |
| `workSchedule` | string |
| `workScheduleByDays` | list |
| `workingHours` | list |
| `workFormats` | list |
| `workingDays` | list |
| `workingTimeIntervals` | list |
| `workingTimeModes` | list |
| `flyInFlyOutDurations` | list |
| `nightShifts` | boolean |
| `internship` | boolean |
| `acceptHandicapped` | null |
| `acceptTemporary` | boolean |
| `acceptIncompleteResumes` | boolean |
| `acceptLaborContract` | boolean |
| `ageRestriction` | null |
| `responseLetterRequired` | boolean |
| `showContact` | boolean |
| `inboxPossibility` | boolean |

---

[← All scrapers](../../README.md)
