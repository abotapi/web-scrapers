# Reed.co.uk Scraper

Scrape Reed.co.uk jobs, companies, courses and reviews by keyword, location, filters or URL. Extract 80+ fields including salary, company, GPS, sector, contract type, skills, descriptions, postcodes, company profiles, courses and reviews.

**[Open Reed.co.uk Scraper on Apify](https://apify.com/abotapi/reed-co-uk-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~reed-co-uk-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "jobs", "keywords": "data engineer", "locations": ["london"], "postedDate": "anytime", "sortBy": "relevance", "courseQueries": ["python"], "maxReviewsPerCourse": 10, "reviewsSort": "MostRecent", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | What to scrape |
| `urls` | array | Job URLs (optional) |
| `keywords` | string | Keywords |
| `locations` | array | Locations |
| `proximity` | integer | Distance (miles) |
| `salaryFrom` | integer | Minimum salary () |
| `salaryTo` | integer | Maximum salary () |
| `postedDate` | string | Posted within |
| `sortBy` | string | Sort by |
| `fullTime` | boolean | Full-time only |
| `partTime` | boolean | Part-time only |
| `permanent` | boolean | Permanent only |
| `temporary` | boolean | Temporary only |
| `contract` | boolean | Contract only |
| `agency` | boolean | Posted by agency |
| `direct` | boolean | Posted by employer |
| `graduate` | boolean | Graduate roles |
| `easyApply` | boolean | Easy apply |
| `visaSponsorship` | boolean | Visa sponsorship |
| `earlyBird` | boolean | Early bird |
| `fetchDetails` | boolean | Fetch full job details |
| `companies` | array | Companies |
| `courseQueries` | array | Course search keywords |
| `courseUrls` | array | Course URLs or IDs |
| `fetchReviews` | boolean | Fetch course reviews |
| `maxReviewsPerCourse` | integer | Max reviews per course |
| `reviewsSort` | string | Reviews sort order |
| `maxListings` | integer | Max results |
| `maxPages` | integer | Max pages per search |
| `maxResidentialRequests` | integer | Residential request budget |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/reed-co-uk-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `jobId` | integer |
| `url` | string |
| `title` | string |
| `companyName` | string |
| `logoImage` | string |
| `description` | string |
| `skills` | list |
| `statuses` | list |
| `location` | string |
| `latitude` | float |
| `longitude` | float |
| `remoteWorkingOption` | null |
| `displaySalary` | string |
| `shortDisplaySalary` | string |
| `salaryFrom` | integer |
| `salaryTo` | integer |
| `salaryCurrencyId` | integer |
| `salaryType` | integer |
| `jobType` | integer |
| `isPartTime` | boolean |
| `isFullTime` | boolean |
| `postedOn` | string |
| `createdOn` | string |
| `updatedOn` | string |
| `expiryOn` | string |
| `scrapedAt` | string |
| `isExternal` | boolean |
| `externalLink` | null |
| `isEasyApply` | boolean |
| `emailForApplications` | null |
| `applicationStatus` | null |
| `isApplicationWithdrawn` | boolean |
| `sourceListUrl` | string |
| `rawListData` | object |
| `jobTypeName` | string |
| `taxonomyLevel1` | string |
| `taxonomyLevel2` | string |
| `isFeatured` | boolean |
| `isPromoted` | boolean |

---

[← All scrapers](../../README.md)
