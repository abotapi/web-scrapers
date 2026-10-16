# SEEK Jobs Scraper

Scrape SEEK.com.au and SEEK.co.nz jobs by keyword, location, or filters. Extract full descriptions, companies, salaries, locations, classifications, listing dates, and more across Australia and New Zealand.

**[Open SEEK Jobs Scraper on Apify](https://apify.com/abotapi/seek-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~seek-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "auto", "region": "AU", "location": "All-Australia", "salaryType": "annual", "sortmode": "ListedDate", "requireContact": "off", "descriptionFormat": "html_text", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `region` | string | Region |
| `keywords` | string | Keywords |
| `keywordsList` | array | More keyword searches (optional) |
| `companyName` | string | Company (exact employer name) |
| `location` | string | Location |
| `locationsList` | array | More locations (optional) |
| `radius` | integer | Search radius (km) |
| `classification` | array | Classification |
| `subclassification` | array | Subclassification |
| `workType` | array | Work type |
| `workArrangement` | array | Work arrangement |
| `salaryType` | string | Salary type |
| `salaryMin` | integer | Minimum salary |
| `salaryMax` | integer | Maximum salary |
| `daterange` | integer | Listed within N days |
| `sortmode` | string | Sort order |
| `urls` | array | SEEK search URLs |
| `includeKeywords` | array | Include keywords |
| `excludeKeywords` | array | Exclude keywords |
| `keywordMatchFields` | array | Match keywords in |
| `fromDate` | string | Listed on or after |
| `toDate` | string | Listed on or before |
| `maxAgeMinutes` | integer | Listed within the last N minutes |
| `minApplicants` | integer | Minimum applicants |
| `maxApplicants` | integer | Maximum applicants |
| `requireContact` | string | Require contact details |
| `skipReposts` | boolean | Skip reposts |
| `customFilters` | array | Custom filter rules (post-filter) |
| `includeFullDescription` | boolean | Fetch full job description |
| `descriptionFormat` | string | Description format |
| `descriptionMaxLength` | integer | Max description length (characters) |
| `compact` | boolean | Compact output (core fields for AI age |
| `excludeEmptyFields` | boolean | Leave out empty fields |
| `maxItems` | integer | Max items to return |
| `maxTimeSec` | integer | Max run time (seconds) |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/seek-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

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
| `abstract` | string |
| `content` | string |
| `contentText` | string |
| `contentSections` | list |
| `bulletPoints` | list |
| `companyName` | string |
| `companyId` | string |
| `companyUrl` | string |
| `companyNameSlug` | string |
| `companyProfileId` | integer |
| `companyOverview` | string |
| `companyIndustry` | string |
| `companySize` | string |
| `companyWebsite` | string |
| `companySpecialities` | list |
| `companyPrimaryLocation` | string |
| `companyLogo` | string |
| `companyCoverImage` | string |
| `companyRating` | float |
| `companyReviewCount` | integer |
| `companySalaryRating` | integer |
| `companyPerks` | list |
| `companyAwards` | list |
| `advertiserId` | string |
| `advertiserName` | string |
| `locationLabel` | string |
| `locationSeoHierarchy` | list |
| `countryCode` | string |
| `classifications` | list |
| `classificationInfo` | object |
| `workTypes` | list |
| `workTypeIds` | list |
| `workArrangements` | list |

---

[← All scrapers](../../README.md)
