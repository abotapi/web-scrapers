# Totaljobs Scraper

Scrape UK job listings from Totaljobs.com by keyword, location, filters, or URL. Extract 40+ fields including title, parsed salary range and period, employer, logo, GPS location, skills, employment type, full description, posting date, and apply link.

**[Open Totaljobs Scraper on Apify](https://apify.com/abotapi/totaljobs-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~totaljobs-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["London"], "jobType": "any", "companyType": "any", "salaryType": "annual", "postedWithin": "0", "sortBy": "relevance", "maxListings": 10, "maxPages": 1, "maxResults": 10, "descriptionFormat": "html", "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "GB"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `keywords` | string | Keywords |
| `jobType` | string | Job type |
| `companyType` | string | Advertiser type |
| `minSalary` | integer | Minimum salary |
| `salaryType` | string | Salary period |
| `postedWithin` | string | Posted within (days) |
| `sortBy` | string | Sort by |
| `remote` | boolean | Remote only |
| `contractType` | string | Contract type |
| `excludeSponsored` | boolean | Exclude sponsored jobs |
| `urls` | array | Search URLs |
| `fetchDetails` | boolean | Fetch full job details |
| `maxListings` | integer | Max jobs |
| `maxPages` | integer | Max pages per search |
| `query` | string | Query (alias of Keywords) |
| `location` | string | Location (alias of Locations) |
| `startUrls` | array | Start URLs (alias of URLs) |
| `age` | integer | Age in days (alias of Posted within) |
| `sort` | string | Sort (alias of Sort by) |
| `maxResults` | integer | Max results (alias of Max jobs) |
| `includeDetails` | boolean | Include details (alias of Fetch detail |
| `descriptionFormat` | string | Description format |
| `descriptionMaxLength` | integer | Description max length |
| `outputFields` | array | Output fields |
| `compact` | boolean | Compact rows |
| `excludeEmptyFields` | boolean | Exclude empty fields |
| `proxy` | object | Proxy |
| `proxyConfiguration` | object | Proxy (alias) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/totaljobs-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `rowType` | string |
| `brand` | string |
| `backend` | string |
| `sourceSearchUrl` | string |
| `scrapedAt` | string |
| `jobId` | integer |
| `harmonisedId` | string |
| `jobUrl` | string |
| `applyUrl` | string |
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
| `labels` | list |
| `topLabels` | list |
| `section` | string |
| `metaData` | object |
| `description` | null |
| `descriptionText` | null |
| `validThrough` | null |
| `employmentType` | null |
| `industry` | null |
| `directApply` | null |
| `applyType` | null |
| `jobLocationType` | null |
| `applicantLocationRequirements` | null |

---

[← All scrapers](../../README.md)
