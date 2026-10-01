# Cwjobs UK Scraper

Scrape tech and IT jobs from CWJobs.co.uk into clean, structured data. Search by keyword, location, salary, work type, date, and sort order, or use job/listing URLs. Returns salary, GPS location, full description, dates, and rich employer details.

**[Open Cwjobs UK Scraper on Apify](https://apify.com/abotapi/cwjobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~cwjobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": ["javascript"], "locations": ["london"], "workType": "any", "salaryPeriod": "annual", "postedWithin": "any", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "GB"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Start mode |
| `keywords` | array | Keywords |
| `locations` | array | Locations |
| `workType` | string | Work type |
| `minSalary` | integer | Minimum salary |
| `salaryPeriod` | string | Salary period |
| `postedWithin` | string | Posted within |
| `sortBy` | string | Sort by |
| `urls` | array | Job or listing URLs |
| `fetchDetails` | boolean | Fetch full job details |
| `maxPages` | integer | Max listing pages per search |
| `maxListings` | integer | Max jobs |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/cwjobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `rowType` | string |
| `listingUrl` | string |
| `jobId` | string |
| `externalId` | string |
| `jobUrl` | string |
| `title` | string |
| `description` | string |
| `snippet` | null |
| `workType` | string |
| `employmentType` | string |
| `industry` | string |
| `datePosted` | string |
| `validThrough` | string |
| `postedAgo` | string |
| `isPremium` | boolean |
| `isTopJob` | boolean |
| `isFreeListing` | boolean |
| `directApply` | boolean |
| `applyType` | string |
| `jobLocationType` | null |
| `applicantLocationRequirements` | null |
| `salaryText` | string |
| `salaryMin` | integer |
| `salaryMax` | integer |
| `salaryCurrency` | string |
| `salaryPeriod` | string |
| `locationText` | string |
| `locationLocality` | string |
| `locationRegion` | string |
| `locationPostalCode` | string |
| `locationCountry` | string |
| `latitude` | float |
| `longitude` | float |
| `employerName` | string |
| `employerId` | integer |
| `employerLogoUrl` | string |
| `employerProfileUrl` | string |
| `companyEmployees` | null |
| `companyFounded` | null |
| `companyIndustries` | null |

---

[← All scrapers](../../README.md)
