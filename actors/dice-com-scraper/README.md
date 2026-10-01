# Dice.com Scraper

Scrape tech job listings from Dice.com by keyword, filters, or URL. Extract job titles, companies, recruiter types, salaries, locations, skills, posted dates, apply links or emails, and full job descriptions. Auto-paginates with pay-per-result pricing and no subscription required.

**[Open Dice.com Scraper on Apify](https://apify.com/abotapi/dice-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~dice-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["python developer"], "radiusUnit": "mi", "countryCode": "US", "postedDate": "any", "employmentType": "any", "workplaceType": "any", "employerType": "any", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `queries` | array | Keywords |
| `location` | string | Location (optional) |
| `radius` | integer | Search radius |
| `radiusUnit` | string | Radius unit |
| `countryCode` | string | Country code |
| `postedDate` | string | Date posted |
| `employmentType` | string | Employment type |
| `workplaceType` | string | Workplace type |
| `employerType` | string | Employer type |
| `easyApply` | boolean | Easy Apply only |
| `willingToSponsor` | boolean | Willing to sponsor only |
| `sortBy` | string | Sort by |
| `urls` | array | Search URLs (URL mode) |
| `fetchDetails` | boolean | Fetch detail pages (richer data) |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (total, default 20, 0  un |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/dice-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `guid` | string |
| `url` | string |
| `title` | string |
| `company` | string |
| `companyLogo` | string |
| `companyProfileId` | string |
| `companyProfileUrl` | string |
| `clientBrandId` | string |
| `city` | string |
| `state` | string |
| `country` | string |
| `region` | string |
| `locationDisplay` | string |
| `street` | null |
| `postalCode` | null |
| `applicantLocationRequirements` | null |
| `salary` | string |
| `salaryMin` | integer |
| `salaryMax` | integer |
| `salaryCurrency` | null |
| `salaryPeriod` | null |
| `employmentType` | string |
| `employerType` | string |
| `easyApply` | boolean |
| `remote` | boolean |
| `workplaceTypes` | list |
| `workFromHomeAvailability` | string |
| `willingToSponsor` | null |
| `skills` | list |
| `positionId` | null |
| `score` | float |
| `summary` | string |
| `description` | null |
| `descriptionText` | null |
| `postedDate` | string |
| `modifiedDate` | string |
| `validThrough` | null |
| `applyType` | null |
| `applyUrl` | null |

---

[← All scrapers](../../README.md)
