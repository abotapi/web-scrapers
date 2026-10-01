# Comparably Scraper

Extract rich company data from comparably.com using company names or profile URLs. Get ratings, culture scores, CEO approval, employee reviews, salary insights, awards, revenue, headquarters, and more in structured JSON, CSV, or Excel format.

**[Open Comparably Scraper on Apify](https://apify.com/abotapi/comparably-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~comparably-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "companies": ["Google", "Microsoft"], "maxReviews": 10, "maxCompanies": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Start mode |
| `companies` | array | Company names |
| `urls` | array | Company URLs |
| `includeReviews` | boolean | Include reviews |
| `maxReviews` | integer | Max reviews per company |
| `maxReviewPages` | integer | Max review pages per company |
| `includeSalaries` | boolean | Include salaries |
| `maxCompanies` | integer | Max companies |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/comparably-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `companyId` | integer |
| `slug` | string |
| `url` | string |
| `name` | string |
| `fullName` | string |
| `mission` | string |
| `website` | string |
| `phone` | string |
| `address` | string |
| `revenue` | integer |
| `logo` | string |
| `backgroundUrl` | string |
| `employeeParticipantCount` | integer |
| `totalRatingsCount` | integer |
| `lastModifiedDate` | string |
| `isClaimedCompany` | boolean |
| `isPremiumCompany` | boolean |
| `overallRating` | float |
| `letterGrade` | string |
| `isChoiceEmployer` | boolean |
| `cultureScore` | integer |
| `cultureGrade` | string |
| `cultureScoreLabel` | string |
| `totalAnswers` | integer |
| `lastAnswerLabel` | string |
| `ceoName` | string |
| `ceoScore` | string |
| `ceoTotalScore` | integer |
| `ceoImageUrl` | string |
| `metroName` | string |
| `metroGrade` | string |
| `metroScoreLabel` | string |
| `topDimensions` | list |
| `bottomDimensions` | list |
| `awardsCount` | integer |
| `owner` | object |
| `metro` | object |
| `awards` | list |
| `relatedCompanies` | list |
| `reviews` | list |

---

[← All scrapers](../../README.md)
