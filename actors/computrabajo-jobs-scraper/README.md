# Computrabajo Scraper

Scrape Computrabajo jobs across 17 Latin American country portals by keyword or URL. Extract salaries, requirements, skills and apply links. Collect company profiles, employee ratings, reviews and comments. Supports job, company and evaluation URLs with incremental tracking.

**[Open Computrabajo Scraper on Apify](https://apify.com/abotapi/computrabajo-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~computrabajo-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQueries": ["ventas"], "countries": ["mx", "co", "pe", "ar", "cl", "ec"], "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "MX"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQueries` | array | Search keywords |
| `countries` | array | Country portals |
| `urls` | array | Links |
| `fetchDetails` | boolean | Fetch offer details |
| `fetchReviews` | boolean | Fetch company reviews |
| `maxReviews` | integer | Max reviews per company |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/computrabajo-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `kind` | string |
| `jobId` | string |
| `title` | string |
| `url` | string |
| `company` | string |
| `companyUrl` | string |
| `companyRating` | null |
| `location` | string |
| `postedText` | string |
| `salaryText` | null |
| `workMode` | string |
| `isUrgent` | boolean |
| `isFeatured` | boolean |
| `applyUrl` | string |
| `countryCode` | string |
| `country` | string |
| `sourceUrl` | string |
| `sourceMode` | string |
| `detailFetched` | boolean |
| `description` | string |
| `descriptionHtml` | string |
| `industry` | string |
| `datePosted` | string |
| `validThrough` | string |
| `employmentType` | string |
| `directApply` | boolean |
| `salaryCurrency` | string |
| `salaryValue` | integer |
| `salaryUnit` | string |
| `city` | string |
| `region` | string |
| `addressCountry` | string |
| `companyLogoUrl` | string |
| `employerId` | string |
| `education` | string |
| `experience` | string |
| `ageRange` | string |
| `otherRequirements` | list |
| `skills` | list |

---

[← All scrapers](../../README.md)
