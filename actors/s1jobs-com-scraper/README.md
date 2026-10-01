# s1jobs Scraper

Scrape jobs from s1jobs.com across Scotland and the UK. Search by keyword, location, or URLs. Returns title, parsed salary band, company, logo, GPS location, skills, contract type, and 90+ fields per job, with optional full description, postcode, and apply links.

**[Open s1jobs Scraper on Apify](https://apify.com/abotapi/s1jobs-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~s1jobs-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Glasgow"], "contractType": "any", "workingHours": "any", "advertiserType": "any", "salaryType": "annual", "sortBy": "relevance", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `keywords` | string | Keywords |
| `contractType` | string | Contract type |
| `workingHours` | string | Hours |
| `advertiserType` | string | Advertiser type |
| `minSalary` | integer | Minimum salary |
| `salaryType` | string | Salary period |
| `publicSectorOnly` | boolean | Public sector only |
| `hasVideoOnly` | boolean | Jobs with video only |
| `sortBy` | string | Sort by |
| `urls` | array | Search URLs |
| `fetchDetails` | boolean | Fetch full job details |
| `maxListings` | integer | Max jobs |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy |
| `maxResidentialRequests` | integer | Residential request cap |
| `maxResidentialMB` | integer | Residential traffic budget (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/s1jobs-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `rowType` | string |
| `source` | string |
| `jobSource` | string |
| `job_source` | string |
| `jobSourceCategory` | string |
| `this_job_from` | string |
| `sourceSearchUrl` | string |
| `scrapedAt` | string |
| `jobId` | string |
| `id` | string |
| `company_id` | integer |
| `companyId` | integer |
| `vacancyId` | string |
| `vacancy_id` | string |
| `vacancyUuid` | string |
| `jobReference` | null |
| `talentPoolId` | integer |
| `companyUrn` | string |
| `url` | string |
| `jobUrl` | string |
| `listingUrl` | string |
| `canonicalUrl` | string |
| `title` | string |
| `description` | string |
| `description_html` | string |
| `description_text` | string |
| `company` | string |
| `companyName` | string |
| `companyLogo` | string |
| `company_logo` | string |
| `logoUrl` | string |
| `companyImages` | list |
| `companyProfileUrl` | string |
| `company_profile_url` | string |
| `companyAccreditations` | list |
| `accreditations` | list |
| `companyConfidential` | integer |
| `companyType` | string |
| `companyInsights` | list |
| `isPublicSector` | boolean |

---

[← All scrapers](../../README.md)
