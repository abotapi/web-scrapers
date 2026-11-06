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
  -d '{"mode": "search", "salaryType": "0", "postedWithin": "0", "sortBy": "1", "maxPages": 1, "maxListings": 10, "maxResults": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
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
| `searchQuery` | string | Search query (alias) |
| `searchQueries` | array | Search queries (alias) |
| `location` | string | Location (alias) |
| `daysOld` | integer | Days old (alias) |
| `urls` | array | Start URLs |
| `startUrls` | array | Start URLs (alias) |
| `maxPages` | integer | Max pages |
| `maxListings` | integer | Max jobs |
| `maxResults` | integer | Max results (alias) |
| `compact` | boolean | Compact output |
| `fetchDetails` | boolean | Fetch detail pages |
| `proxy` | object | Proxy configuration |
| `skipReposts` | boolean | Skip reposts (new jobs only) |

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
| `salaryMin` | integer |
| `salaryMax` | integer |
| `salaryCurrency` | string |
| `salaryPeriod` | string |
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
| `remote` | boolean |
| `labels` | list |
| `isAnonymous` | boolean |
| `snippet` | string |
| `postCode` | null |
| `industry` | null |
| `directApply` | null |

---

[← All scrapers](../../README.md)
