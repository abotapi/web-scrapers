# IrishJobs.ie Scraper

Scrape job listings from IrishJobs.ie by keyword, location, job type, salary, recency, or search URL. Extract titles, employers, GPS locations, parsed EUR salary ranges, employment type, full descriptions, and posting dates.

**[Open IrishJobs.ie Scraper on Apify](https://apify.com/abotapi/irishjobs-ie?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~irishjobs-ie/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "salaryType": "0", "postedWithin": "0", "sortBy": "1", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `keywords` | array | Keywords |
| `locations` | array | Locations |
| `jobType` | string | Job type |
| `minSalary` | integer | Minimum salary |
| `salaryType` | string | Salary type |
| `postedWithin` | string | Posted within |
| `sortBy` | string | Sort by |
| `urls` | array | Start URLs |
| `maxPages` | integer | Max pages |
| `maxListings` | integer | Max jobs |
| `fetchDetails` | boolean | Fetch detail pages |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/irishjobs-ie?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `jobId` | string |
| `jobUrl` | string |
| `title` | string |
| `description` | null |
| `employerName` | string |
| `employerUrl` | string |
| `employerLogoUrl` | string |
| `employerId` | integer |
| `locationText` | string |
| `locationLocality` | null |
| `locationRegion` | null |
| `locationPostalCode` | null |
| `locationCountry` | string |
| `locationLat` | null |
| `locationLng` | null |
| `salaryRaw` | string |
| `salaryMin` | null |
| `salaryMax` | null |
| `salaryCurrency` | string |
| `salaryPeriod` | null |
| `employmentType` | null |
| `skills` | list |
| `datePosted` | string |
| `validThrough` | null |
| `applyUrl` | null |
| `applyType` | null |
| `sourceSearchUrl` | string |
| `isSponsored` | boolean |
| `isHighlighted` | boolean |
| `isTopJob` | boolean |
| `isTrafficFromPartner` | boolean |
| `crossPostedCount` | integer |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
