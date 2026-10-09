# Werk.nl Scraper

Scrape job vacancies from werk.nl, the official Dutch government job board by UWV. Uses werk.nl’s vacancy data service for fast, low-cost runs. Returns 40+ fields per job, including title, salary, full description, recruiter contact, application link, and employer profile.

**[Open Werk.nl Scraper on Apify](https://apify.com/abotapi/werk-nl-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~werk-nl-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": ["developer"], "sortBy": "relevance", "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `keywords` | array | Keywords |
| `location` | string | Location |
| `profession` | array | Profession (Beroep) |
| `educationLevels` | array | Education level |
| `hoursPerWeek` | array | Hours per week |
| `workingHours` | array | Working hours type |
| `drivingLicense` | array | Driving licence |
| `language` | array | Language |
| `contractType` | array | Contract type |
| `country` | array | Country |
| `sortBy` | string | Sort by |
| `expandResults` | boolean | Expand results |
| `urls` | array | Vacancy URLs / reference numbers |
| `fetchDetails` | boolean | Fetch full vacancy details |
| `includeRawDetail` | boolean | Include raw detail payload |
| `maxItems` | integer | Max vacancies |
| `maxPagesPerSearch` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/werk-nl-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `referenceNumber` | integer |
| `url` | string |
| `key` | string |
| `externalReferenceId` | string |
| `employerInternalVacatureId` | string |
| `internalReferenceNumber` | null |
| `source` | string |
| `title` | string |
| `profession` | string |
| `relevanceScore` | integer |
| `createdDate` | string |
| `modifiedDate` | string |
| `expirationDate` | string |
| `city` | string |
| `postcode` | string |
| `workLocationType` | string |
| `workLocationTypeCode` | integer |
| `countryCode` | null |
| `foreignCountry` | null |
| `foreignCity` | null |
| `distanceKm` | null |
| `contractType` | string |
| `contractTypeCode` | integer |
| `contractStartDate` | string |
| `contractEndDate` | null |
| `minHours` | integer |
| `maxHours` | integer |
| `workingHoursCode` | integer |
| `studyLevel` | string |
| `salaryTypeCode` | integer |
| `salaryIndication` | string |
| `termsOfEmployment` | null |
| `functionName` | string |
| `functionCode` | string |
| `customDescription` | string |
| `descriptionHtml` | string |
| `description` | string |
| `isApprenticeship` | boolean |
| `isInternship` | boolean |
| `isEuresPriority` | boolean |

---

[← All scrapers](../../README.md)
