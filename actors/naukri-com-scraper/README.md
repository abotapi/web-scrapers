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
  -d '{"mode": "search", "keywords": ["python developer"], "sortBy": "relevance", "freshness": "any", "postedBy": "any", "maxItems": 10, "maxPages": 1, "maxReviewsPerJob": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `keywords` | array | Job keywords |
| `location` | string | Location (optional) |
| `urls` | array | Job or search page links |
| `jobIds` | array | Job ids (either mode) |
| `sortBy` | string | Sort by |
| `experience` | integer | Experience (years) |
| `freshness` | string | Posted within |
| `workMode` | array | Work mode |
| `salaryRange` | array | Salary range (INR per year) |
| `cities` | array | Cities |
| `department` | array | Department |
| `roleCategory` | array | Role category |
| `industry` | array | Industry |
| `companyType` | array | Company type |
| `postedBy` | string | Posted by |
| `topCompanies` | array | Companies |
| `walkInOnly` | boolean | Walk-in jobs only |
| `stipend` | array | Internship stipend (per month) |
| `internshipDuration` | array | Internship duration |
| `ugCourse` | array | Graduate (UG) qualification |
| `pgCourse` | array | Postgraduate (PG) qualification |
| `urlParams` | array | Extra site filter parameters (advanced |
| `fetchDetails` | boolean | Fetch full job details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `maxReviewsPerJob` | integer | Max AmbitionBox reviews per job |
| `proxyConfiguration` | object | Proxy configuration |
| `skipReposts` | boolean | Skip reposted jobs (incremental mode o |

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
| `groupId` | integer |
| `isTopGroup` | boolean |
| `listingSource` | string |
| `externalApply` | boolean |
| `diversityTags` | list |
| `companyJobsUrl` | string |
| `roleCategoryId` | string |
| `hasApplyQuestionnaire` | boolean |
| `salaryDetail` | object |
| `companyRating` | object |
| `description` | string |
| `descriptionHtml` | string |
| `descriptionMarkdown` | string |
| `keySkills` | object |
| `locations` | list |
| `locationDetails` | list |
| `locationIds` | list |
| `companyDetails` | object |
| `education` | string |

---

[← All scrapers](../../README.md)
