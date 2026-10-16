# EdJoin.org Scraper

Scrape EdJoin.org K-12 and higher-ed jobs by keyword, location, filters or URL. Extract districts, locations, salaries, openings, deadlines, requirements and full descriptions, with optional contact and address details.

**[Open EdJoin.org Scraper on Apify](https://apify.com/abotapi/edjoin-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~edjoin-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": "teacher", "sortBy": "newest", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `keywords` | string | Keywords |
| `location` | string | Location |
| `jobTypeIds` | array | Job type IDs |
| `categoryId` | integer | Category ID |
| `stateId` | integer | State ID |
| `onlineApplicationOnly` | boolean | Online application only |
| `postedWithinDays` | integer | Posted within (days) |
| `urls` | array | URLs |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch full job details |
| `maxListings` | integer | Max jobs (0  unlimited) |
| `maxPages` | integer | Max pages per search (0  unlimited) |
| `proxy` | object | Proxy |
| `maxResidentialRequests` | integer | Residential request budget (0  unlimit |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/edjoin-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `url` | string |
| `title` | string |
| `districtName` | string |
| `city` | string |
| `countyName` | string |
| `countyFullName` | string |
| `countyId` | integer |
| `stateName` | string |
| `stateId` | integer |
| `zip` | null |
| `location` | string |
| `jobType` | string |
| `jobTypeId` | integer |
| `categoryName` | string |
| `categoryId` | integer |
| `salaryInfo` | string |
| `salaryDisplay` | string |
| `beginningSalary` | null |
| `endingSalary` | null |
| `salaryType` | string |
| `payRangeFrom` | string |
| `payRangeTo` | string |
| `payRangeUnit` | string |
| `singleRate` | null |
| `singleRateUnit` | null |
| `employmentType` | string |
| `numberOpenings` | integer |
| `onlineApp` | boolean |
| `isRecruitmentCenter` | boolean |
| `isAdminJob` | boolean |
| `isSummerSchool` | boolean |
| `datePosted` | string |
| `creationDate` | string |
| `applicationDeadline` | string |
| `displayFlag` | string |
| `districtLogo` | null |
| `portalUrl` | null |
| `searchQuery` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
