# NIJobs Scraper

Scrape NIJobs.com listings across Northern Ireland by keyword, location, salary, posted date, or URL. Extract 60+ fields including title, company, salary, skills, description, employment type, industry, GPS, address, dates, and apply URL.

**[Open NIJobs Scraper on Apify](https://apify.com/abotapi/nijobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~nijobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": ["Software Developer"], "postedWithin": "any", "salaryPeriod": "annual", "sortBy": "relevance", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "GB"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `keywords` | array | Keywords |
| `location` | string | Location |
| `postedWithin` | string | Posted within |
| `minSalary` | integer | Minimum salary |
| `salaryPeriod` | string | Salary period |
| `sortBy` | string | Sort order |
| `urls` | array | Results-page URLs |
| `fetchDetails` | boolean | Fetch full detail from each job page |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/nijobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `jobId` | integer |
| `harmonisedId` | string |
| `url` | string |
| `from_url` | string |
| `source` | string |
| `title` | string |
| `jobTitle` | string |
| `companyId` | integer |
| `companyName` | string |
| `company` | string |
| `companyUrl` | string |
| `companyLogoUrl` | string |
| `companyLogo` | string |
| `isAnonymous` | boolean |
| `location` | string |
| `postCode` | null |
| `workFromHome` | null |
| `latitude` | float |
| `longitude` | float |
| `addressCountry` | string |
| `addressLocality` | string |
| `addressRegion` | string |
| `streetAddress` | null |
| `postalCode` | null |
| `salary` | string |
| `salaryText` | string |
| `unifiedSalary` | null |
| `baseSalaryMin` | null |
| `baseSalaryMax` | null |
| `baseSalaryCurrency` | null |
| `baseSalaryUnit` | null |
| `datePosted` | string |
| `publishFromDate` | string |
| `publishToDate` | string |
| `periodPostedDate` | string |
| `validThrough` | string |
| `hasFuturePosting` | boolean |
| `employmentType` | string |
| `workType` | null |

---

[← All scrapers](../../README.md)
