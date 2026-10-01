# Jobsite UK Scraper

Collect UK job listings from Jobsite.co.uk at scale. Search by keyword, location, filters, or paste search URLs. Returns 35+ clean fields per job from search pages. Optional detail mode adds full description, GPS coordinates, employment type, and company profile.

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
  -d '{"mode": "search", "locations": ["London"], "jobType": "any", "companyType": "any", "salaryType": "annual", "postedWithin": "0", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
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
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max jobs |
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
| `company` | null |
| `contactPhones` | list |
| `contactEmails` | list |
| `detailFetched` | boolean |

---

[← All scrapers](../../README.md)
