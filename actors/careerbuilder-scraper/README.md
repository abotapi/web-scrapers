# CareerBuilder Scraper

Scrape CareerBuilder.com job listings by search or URL. Returns title, company profile, location with coordinates, salary range, employment type, apply link, posting dates, and full job description, with date sorting and optional detail enrichment.

**[Open CareerBuilder Scraper on Apify](https://apify.com/abotapi/careerbuilder-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~careerbuilder-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["software engineer"], "location": ["New York, NY"], "sortBy": "relevance", "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Job keywords |
| `location` | array | Locations |
| `startUrls` | array | URLs |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch full job details |
| `maxItems` | integer | Max jobs |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/careerbuilder-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `mode` | string |
| `jobId` | string |
| `seoJobId` | string |
| `title` | string |
| `url` | string |
| `status` | string |
| `jobType` | string |
| `promoted` | boolean |
| `provider` | null |
| `industry` | null |
| `company` | string |
| `companyLogo` | string |
| `companyWebsite` | null |
| `companyDescription` | string |
| `companySize` | null |
| `companyFoundingDate` | null |
| `companyLocation` | null |
| `location` | string |
| `city` | string |
| `state` | string |
| `country` | string |
| `latitude` | string |
| `longitude` | string |
| `isRemote` | boolean |
| `jobLocationType` | string |
| `employmentType` | string |
| `salary` | null |
| `salaryMin` | null |
| `salaryMax` | null |
| `salaryCurrency` | string |
| `salaryUnit` | string |
| `isSalaryExtracted` | null |
| `snippet` | string |
| `description` | null |
| `datePosted` | string |
| `dateRecency` | string |
| `formattedDate` | string |
| `createdDate` | float |
| `modifiedDate` | float |
| `applyType` | string |

---

[← All scrapers](../../README.md)
