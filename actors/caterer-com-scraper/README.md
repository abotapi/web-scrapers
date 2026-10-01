# Caterer.com Scraper

Scrape UK hospitality jobs from Caterer.com, including chef, hotel, restaurant, bar, and events roles. Search by keyword, location, filters, or URLs. Returns salary, employer, logo, location, skills, and 35+ fields, with optional full description, GPS, and company profile.

**[Open Caterer.com Scraper on Apify](https://apify.com/abotapi/caterer-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~caterer-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["London"], "jobType": "any", "companyType": "any", "salaryType": "annual", "postedWithin": "0", "sortBy": "relevance", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "GB"}}'
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
| `urls` | array | Search URLs |
| `fetchDetails` | boolean | Fetch full job details |
| `maxListings` | integer | Max jobs |
| `maxPages` | integer | Max pages per search |
| `maxResidentialRequests` | integer | Residential request cap |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/caterer-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `rowType` | string |
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
| `company` | null |
| `contactPhones` | list |
| `contactEmails` | list |

---

[← All scrapers](../../README.md)
