# Jobsite UK Scraper

Scrape Jobsite.co.uk job listings at scale by keyword, location, filters or URL. Extract 35+ structured fields per job, including titles, salaries and company details. Optional enrichment adds full descriptions, GPS coordinates, employment types and company profiles.

**[Open Jobsite UK Scraper on Apify](https://apify.com/abotapi/jobsite-co-uk-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~jobsite-co-uk-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["London"], "jobType": "any", "companyType": "any", "salaryType": "annual", "postedWithin": "0", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `keywords` | string | Keywords |
| `jobType` | string | Job type |
| `companyType` | string | Advertiser type |
| `advertiserType` | string | Advertiser type (alias) |
| `minSalary` | integer | Minimum salary |
| `salaryType` | string | Salary period |
| `salaryPeriod` | string | Salary period (alias) |
| `postedWithin` | string | Posted within (days) |
| `postedWithinDays` | string | Posted within days (alias) |
| `sortBy` | string | Sort by |
| `radiusMiles` | integer | Search radius (miles) |
| `urls` | array | Search URLs |
| `startUrls` | array | Start URLs (alias) |
| `fetchDetails` | boolean | Fetch full job details |
| `detailMode` | string | Detail mode (alias) |
| `includeContactHints` | boolean | Include contact hints |
| `maxPages` | integer | Max pages per search |
| `maxPagesPerSearch` | integer | Max pages per search (alias) |
| `maxListings` | integer | Max jobs |
| `maxItems` | integer | Max items (alias) |
| `maxResidentialRequests` | integer | Residential request cap |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/jobsite-co-uk-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `rowType` | string |
| `sourceSearchUrl` | string |
| `detailStatus` | string |
| `apply` | object |
| `details` | object |
| `contacts` | object |
| `source` | object |
| `jobId` | integer |
| `harmonisedId` | string |
| `jobUrl` | string |
| `sourceSite` | string |
| `title` | string |
| `datePosted` | string |
| `publishFromDate` | string |
| `publishToDate` | string |
| `employer` | object |
| `location` | object |
| `salary` | object |
| `workFromHome` | null |
| `skills` | list |
| `textSnippet` | string |
| `crossPostedCount` | integer |
| `isSponsored` | boolean |
| `isHighlighted` | boolean |
| `isTopJob` | boolean |
| `isTrafficFromPartner` | boolean |
| `partnership` | object |
| `travelTime` | null |
| `description` | null |
| `descriptionText` | null |
| `validThrough` | null |
| `employmentType` | null |
| `industry` | null |
| `directApply` | null |
| `applyType` | null |
| `jobLocationType` | null |
| `applicantLocationRequirements` | null |
| `externalId` | string |
| `contractType` | null |
| `workType` | null |

---

[← All scrapers](../../README.md)
