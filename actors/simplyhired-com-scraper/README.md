# SimplyHired Scraper

Scrape active SimplyHired jobs across the US, UK, Canada, Australia, Ireland and India from $1/1K listings. Search by filters or URL. Extract 40+ fields including job titles, companies, salary ranges, full HTML descriptions, qualifications, coordinates and apply URLs.

**[Open SimplyHired Scraper on Apify](https://apify.com/abotapi/simplyhired-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~simplyhired-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["software engineer"], "location": "Remote", "country": "us", "jobType": "any", "datePosted": "any", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `queries` | array | Keywords |
| `location` | string | Location (optional) |
| `country` | string | Country site |
| `jobType` | string | Job type |
| `skipSponsored` | boolean | Skip sponsored placements |
| `datePosted` | string | Date posted |
| `minSalary` | integer | Minimum salary (per year) |
| `remoteOnly` | boolean | Remote jobs only |
| `sortBy` | string | Sort within each page |
| `keyword` | string | Keyword (alias of Keywords) |
| `results_wanted` | integer | Results wanted (alias of Max listings) |
| `max_pages` | integer | Max pages (alias of Max pages per sear |
| `urls` | array | Search URLs (URL mode) |
| `startUrls` | array | Start URLs (alias of Search URLs) |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (total) |
| `fetchDetails` | boolean | Fetch detail pages (richer data) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/simplyhired-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `displayTitle` | string |
| `normalizedTitle` | string |
| `company` | string |
| `companyRating` | float |
| `companyPageUrl` | null |
| `employerLogoUrl` | string |
| `employerHomepage` | null |
| `location` | string |
| `formattedLocation` | string |
| `city` | string |
| `state` | string |
| `latitude` | float |
| `longitude` | float |
| `country` | string |
| `jobTypes` | list |
| `workSettings` | list |
| `remoteAttributes` | list |
| `salary` | string |
| `salaryMin` | integer |
| `salaryMax` | integer |
| `salaryCurrency` | string |
| `salaryPeriod` | string |
| `compensation` | null |
| `snippet` | string |
| `descriptionHtml` | string |
| `descriptionText` | string |
| `requirements` | list |
| `qualifications` | list |
| `benefits` | list |
| `skillsAll` | list |
| `datePosted` | string |
| `datePostedEpochMs` | integer |
| `dateOnIndeed` | integer |
| `applyUrl` | string |
| `mobileApplyUrl` | string |
| `indeedApply` | boolean |
| `sponsored` | boolean |

---

[← All scrapers](../../README.md)
