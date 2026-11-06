# Hiring.Cafe Scraper

Scrape Hiring.Cafe jobs from $1/1K results. Search with advanced filters or URLs and extract 100+ fields per job, including salaries, company insights, benefits and job details. Fast, scalable job data extraction with Gold discounts starting at $1.

**[Open Hiring.Cafe Scraper on Apify](https://apify.com/abotapi/hiring-cafe-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~hiring-cafe-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"startUrls": [{"url": "https://hiringcafe.com/classic"}, {"url": "https://hiringcafe.com/classic?searchState=%7B%22searchQuery%22%3A%22software%20engineer%22%7D"}, {"url": "https://hiringcafe.com/classic?searchState=%7B%22searchQuery%22%3A%22software%20engineer%22%7D&page=2"}, {"url": "https://hiringcafe.com/?searchState=%7B%22searchQuery%22%3A%22software%20engineer%22%7D"}, {"url": "https://hiringcafe.com/?searchState=eyJzZWFyY2hRdWVyeSI6InNvZnR3YXJlIGVuZ2luZWVyIn0%3D"}, {"url": "https://hiringcafe.com/job/bt38fz2pqe76nimr"}], "workplaceType": "Any", "commitmentType": "Any", "seniorityLevel": "Any", "sortBy": "default", "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `startUrls` | array | Start URLs |
| `keyword` | string | Search keyword |
| `location` | string | Location |
| `workplaceType` | string | Workplace Type |
| `commitmentType` | string | Employment Type |
| `seniorityLevel` | string | Seniority Level |
| `postedWithinDays` | integer | Posted within (days) |
| `salaryTransparentOnly` | boolean | Salary transparent only |
| `sortBy` | string | Sort by |
| `workplaceTypes` | array | Workplace types (multi) |
| `commitmentTypes` | array | Commitment types (multi) |
| `seniorityLevels` | array | Seniority levels (multi) |
| `jobTitleQuery` | string | Job title contains |
| `companyNames` | array | Only these companies |
| `excludedCompanyNames` | array | Exclude companies |
| `industries` | array | Only these industries |
| `excludedIndustries` | array | Exclude industries |
| `minSalary` | integer | Minimum salary |
| `maxSalary` | integer | Maximum salary |
| `minYoe` | integer | Min years of experience |
| `maxYoe` | integer | Max years of experience |
| `maxItems` | integer | Maximum jobs |
| `fetchDetails` | boolean | Fetch full job descriptions |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/hiring-cafe-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `board_token` | string |
| `source` | string |
| `source_and_board_token` | string |
| `apply_url` | string |
| `objectID` | string |
| `requisition_id` | string |
| `job_url` | string |
| `is_expired` | boolean |
| `job_information` | object |
| `v5_processed_job_data` | object |
| `v5_processed_company_data` | object |
| `_geoloc` | list |
| `job_title` | string |
| `employment_types` | list |
| `role_type` | string |
| `job_category` | string |
| `seniority` | string |
| `workplace_type` | string |
| `location` | string |
| `employer_type` | string |
| `salary_currency` | string |
| `posted_at` | string |
| `company_name` | string |
| `company_website` | string |
| `company_tagline` | string |
| `company_industry` | string |
| `languages` | list |
| `security_clearance` | string |
| `physical_requirements` | object |
| `company_employees` | integer |
| `company_founded` | integer |
| `company_hq_country` | string |
| `company_funding` | object |
| `company_stock` | object |
| `workplace_cities` | list |
| `workplace_states` | list |
| `workplace_countries` | list |
| `workplace_continents` | list |
| `workplace_counties` | list |

---

[← All scrapers](../../README.md)
