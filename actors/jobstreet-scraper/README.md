# JobStreet Scraper

Scrape JobStreet listings across Malaysia, Singapore, Indonesia, and the Philippines. Extract titles, companies, salaries, locations, descriptions, company info, and apply details. Search with filters or paste JobStreet URLs directly. Fast and cost-efficient.

**[Open JobStreet Scraper on Apify](https://apify.com/abotapi/jobstreet-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~jobstreet-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"country": "MY", "keywords": "software engineer", "location": "Kuala Lumpur", "salaryType": "monthly", "requireContact": "off", "sortmode": "ListedDate", "urls": ["https://my.jobstreet.com/software-engineer-jobs/in-Kuala-Lumpur", "https://my.jobstreet.com/it-jobs", "https://my.jobstreet.com/jobs/in-Selangor", "https://my.jobstreet.com/jobs-in-information-communication-technology", "https://my.jobstreet.com/jobs-in-information-communication-technology/in-Kuala-Lumpur", "https://my.jobstreet.com/jobs-in-information-communication-technology/developers-programmers", "https://my.jobstreet.com/software-engineer-jobs/remote", "https://my.jobstreet.com/software-engineer-jobs-in-information-communication-technology/in-Kuala-Lumpur/full-time", "https://my.jobstreet.com/jobs?classification=6281&worktype=242&daterange=7&sortmode=ListedDate&page=2", "https://sg.jobstreet.com/jobs-in-accounting/in-Singapore", "https://ph.jobstreet.com/jobs-in-accounting/in-Manila", "https://id.jobstreet.com/jobs-in-accounting/in-Jakarta", "https://my.jobstreet.com/api/jobsearch/v5/search?siteKey=MY-Main&sourcesystem=houston&where=Kuala+Lumpur&keywords=software+engineer&page=1&pageSize=5"], "maxItems": 10, "maxPages": 1, "descriptionFormat": "all", "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `country` | string | Country |
| `keywords` | string | Keywords |
| `location` | string | Location |
| `classification` | array | Classification |
| `workType` | array | Work type |
| `workArrangement` | array | Work arrangement |
| `subClassification` | array | Sub-category IDs |
| `salaryMin` | integer | Minimum salary |
| `salaryMax` | integer | Maximum salary |
| `salaryType` | string | Salary period |
| `daterange` | integer | Listed within N days |
| `includeKeywords` | array | Must mention any of |
| `excludeKeywords` | array | Must mention none of |
| `fromDate` | string | Listed on or after |
| `toDate` | string | Listed on or before |
| `maxAgeMinutes` | integer | Max listing age (minutes) |
| `requireContact` | string | Require contact details |
| `sortmode` | string | Sort order |
| `urls` | array | JobStreet search URLs |
| `includeFullDescription` | boolean | Fetch full job description |
| `maxItems` | integer | Max items to return |
| `maxPages` | integer | Max pages per search |
| `descriptionFormat` | string | Description format |
| `maxTimeSec` | integer | Max run time (seconds) |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/jobstreet-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `jobLink` | string |
| `applyLink` | string |
| `title` | string |
| `teaser` | string |
| `jobHook` | string |
| `content` | string |
| `contentText` | string |
| `contentSections` | list |
| `bulletPoints` | list |
| `companyName` | string |
| `companyId` | string |
| `companyUrl` | string |
| `companyNameSlug` | string |
| `companyOverview` | string |
| `advertiserId` | string |
| `advertiserName` | string |
| `locationLabel` | string |
| `locationSeoHierarchy` | list |
| `countryCode` | string |
| `classifications` | list |
| `classificationInfo` | object |
| `workTypes` | list |
| `workArrangements` | list |
| `workArrangementLabels` | list |
| `salaryLabel` | null |
| `salary` | null |
| `salaryCurrency` | null |
| `phoneNumber` | null |
| `phoneNumbers` | list |
| `phoneNumbersFromBody` | list |
| `emails` | list |
| `shareLink` | string |
| `listingDate` | string |
| `listingDateDisplay` | string |
| `expiresAt` | string |
| `isVerified` | boolean |
| `roleId` | string |
| `tags` | list |

---

[← All scrapers](../../README.md)
