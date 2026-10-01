# Gupy Jobs Scraper

Scrape public jobs from Gupy.io by keyword, state, city, workplace type, job type, company, PWD, and feedback badge. Extract rich job details, company information, locations, application deadlines, and badge data.

**[Open Gupy Jobs Scraper on Apify](https://apify.com/abotapi/gupy-io-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~gupy-io-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "developer", "sortBy": "newest", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `searchTerm` | string | Search keyword |
| `state` | string | State |
| `cities` | array | Cities |
| `workplaceTypes` | array | Workplace types |
| `jobTypes` | array | Job types |
| `companies` | array | Companies |
| `pwdOnly` | boolean | Only PWD-accessible jobs |
| `friendlyBadgeOnly` | boolean | Only feedback-badge companies |
| `urls` | array | URLs |
| `fetchDetails` | boolean | Fetch details |
| `sortBy` | string | Sort order |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages |
| `pageSize` | integer | Page size |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/gupy-io-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `code` | string |
| `name` | string |
| `jobUrl` | string |
| `description` | string |
| `descriptionPlainText` | string |
| `prerequisites` | null |
| `responsibilities` | null |
| `benefits` | null |
| `addressLine` | null |
| `addressComplements` | null |
| `addressDistrict` | null |
| `city` | string |
| `state` | null |
| `stateCode` | null |
| `country` | string |
| `countryCode` | string |
| `jobType` | string |
| `workplaceType` | string |
| `isRemoteWork` | boolean |
| `publicationType` | string |
| `status` | string |
| `reason` | null |
| `handicapped` | boolean |
| `disabilities` | boolean |
| `skills` | list |
| `isJobPostedOnGoogle` | null |
| `jobLanguage` | string |
| `publishedAt` | string |
| `publishedDate` | string |
| `expiresAt` | string |
| `expireDays` | integer |
| `registerEndDate` | string |
| `applicationDeadline` | string |
| `quickApply` | null |
| `jobSteps` | null |
| `jobRatingCriterias` | null |
| `companyId` | integer |
| `companySubdomain` | string |
| `companyTimezone` | string |

---

[← All scrapers](../../README.md)
