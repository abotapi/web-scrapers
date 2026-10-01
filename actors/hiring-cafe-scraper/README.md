# Hiring.Cafe Jobs Scraper

Unlock powerful Hiring.Cafe job data extraction. Use advanced filters or URLs to get 100+ fields per job, including salary, company insights, and benefits. Fast, scalable, and built for serious data collection. Only $1 for Gold discount.

**[Open Hiring.Cafe Jobs Scraper on Apify](https://apify.com/abotapi/hiring-cafe-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

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
  -d '{"keyword": "software engineer", "workplaceType": "Any", "commitmentType": "Any", "seniorityLevel": "Any", "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
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
| `maxItems` | integer | Maximum jobs |
| `proxy` | object | Proxy configuration |
| `fetchDetails` | boolean | Fetch full job descriptions |

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
| `company_tagline` | string |
| `company_industry` | string |
| `technical_tools` | list |
| `languages` | list |
| `security_clearance` | string |
| `physical_requirements` | object |
| `company_employees` | integer |
| `company_founded` | integer |
| `company_hq_country` | string |
| `views_on_site` | integer |
| `applies_on_site` | integer |
| `description` | string |
| `description_text` | string |

---

[← All scrapers](../../README.md)
