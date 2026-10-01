# NoFluffJobs Scraper

Scrape NoFluffJobs IT jobs across Poland, Czechia, Slovakia, Hungary and the Netherlands. Search with filters or URLs and extract salaries, skills, descriptions, tasks, benefits, hiring steps, company size, GPS and office locations.

**[Open NoFluffJobs Scraper on Apify](https://apify.com/abotapi/nofluffjobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~nofluffjobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "region": "pl", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `region` | string | Region |
| `keyword` | string | Keyword |
| `category` | string | Category |
| `seniority` | string | Seniority |
| `employmentType` | string | Employment type |
| `jobLanguage` | string | Job posting language |
| `city` | string | City |
| `technology` | string | Technology / skill |
| `urls` | array | NoFluffJobs URLs |
| `remoteOnly` | boolean | Remote only |
| `sortBy` | string | Sort by |
| `minSalary` | integer | Minimum salary |
| `maxSalary` | integer | Maximum salary |
| `fetchDetails` | boolean | Fetch full job details |
| `maxListings` | integer | Max jobs |
| `maxPages` | integer | Max pages per query |
| `proxy` | object | Connection (proxy) |
| `residentialRequestCap` | integer | Residential request cap |
| `residentialBudgetMb` | integer | Residential traffic budget (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/nofluffjobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `reference` | string |
| `title` | string |
| `url` | string |
| `region` | string |
| `regions` | list |
| `companyName` | string |
| `companyLogo` | string |
| `category` | string |
| `seniority` | list |
| `technology` | string |
| `remote` | boolean |
| `fullyRemote` | boolean |
| `remotePercent` | integer |
| `cities` | list |
| `locations` | list |
| `salaryFrom` | integer |
| `salaryTo` | integer |
| `salaryCurrency` | string |
| `salaryType` | string |
| `salaryDisclosed` | string |
| `salary` | object |
| `posted` | integer |
| `renewed` | integer |
| `lastActivity` | integer |
| `onlineInterviewAvailable` | boolean |
| `highlighted` | boolean |
| `topInSearch` | boolean |
| `companySize` | string |
| `companyVideo` | string |
| `companyProfileUrl` | string |
| `description` | string |
| `position` | string |
| `dailyTasks` | list |
| `requirementsMust` | list |
| `requirementsNice` | list |
| `requirementLanguages` | list |
| `requirementsDescription` | string |
| `benefits` | list |
| `officePerks` | list |

---

[← All scrapers](../../README.md)
