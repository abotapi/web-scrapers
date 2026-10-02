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
  -d '{"country": "MY", "keywords": "software engineer", "salaryType": "monthly", "sortmode": "ListedDate", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `country` | string | Country |
| `keywords` | string | Keywords |
| `location` | string | Location |
| `classification` | array | Classification |
| `workType` | array | Work type |
| `salaryMin` | integer | Minimum salary |
| `salaryMax` | integer | Maximum salary |
| `salaryType` | string | Salary period |
| `daterange` | integer | Listed within N days |
| `sortmode` | string | Sort order |
| `urls` | array | JobStreet search URLs |
| `includeFullDescription` | boolean | Fetch full job description |
| `maxItems` | integer | Max items to return |
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
| `companyId` | null |
| `companyUrl` | null |
| `companyNameSlug` | null |
| `companyOverview` | null |
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
| `salaryLabel` | string |
| `salary` | string |
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
