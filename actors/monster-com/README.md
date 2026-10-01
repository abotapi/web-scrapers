# Monster Jobs Scraper

Scrape Monster.com job listings from search and direct job URLs. Extract full descriptions, salaries, companies, locations, geo data, application details, classifications, compliance fields, and public email addresses.

**[Open Monster Jobs Scraper on Apify](https://apify.com/abotapi/monster-com?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~monster-com/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "query": "software engineer", "location": "New York, NY", "workplace": "all", "datePosted": "all", "employmentType": "all", "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `query` | string | Keywords |
| `location` | string | Location |
| `radius` | integer | Radius in miles |
| `workplace` | string | Workplace |
| `startUrls` | array | Start URLs |
| `datePosted` | string | Date posted |
| `employmentType` | string | Employment type |
| `company` | string | Company contains |
| `sortBy` | string | Sort |
| `enrichEmails` | boolean | Extract public emails |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/monster-com?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `jobId` | string |
| `seoJobId` | string |
| `title` | string |
| `companyName` | string |
| `companyUrl` | null |
| `companyLogo` | string |
| `companyDescription` | string |
| `location` | string |
| `streetAddress` | string |
| `city` | string |
| `region` | string |
| `postalCode` | string |
| `country` | string |
| `latitude` | float |
| `longitude` | float |
| `datePosted` | string |
| `validThrough` | string |
| `dateRecency` | string |
| `formattedDate` | string |
| `status` | string |
| `jobType` | string |
| `ingestionMethod` | string |
| `industry` | null |
| `occupationalCategory` | null |
| `educationRequirements` | null |
| `employmentTypes` | list |
| `employmentTypesText` | string |
| `salaryMin` | null |
| `salaryMax` | null |
| `salaryCurrency` | string |
| `salaryUnit` | string |
| `remote` | boolean |
| `promoted` | boolean |
| `applyType` | string |
| `applyUrl` | string |
| `jobUrl` | string |
| `descriptionHtml` | string |
| `descriptionText` | string |
| `contactEmail` | null |
| `contactEmails` | list |

---

[← All scrapers](../../README.md)
