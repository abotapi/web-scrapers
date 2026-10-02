# France Travail Scraper

Scrape job offers from France Travail with titles, companies, locations, salaries, contracts, descriptions, skills, employer details, and apply links. Search by keyword, location, contract, sector, salary, sort options, or paste job/search URLs.

**[Open France Travail Scraper on Apify](https://apify.com/abotapi/francetravail-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~francetravail-fr-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["developpeur"], "location": "Paris", "publishedDate": "Last Week", "contractType": ["Permanent contract (CDI) | CDI"], "contractDuration": ["Full-time | Temps plein"], "jobCategory": ["IT | Informatique, Télécommunication"], "sortBy": "Newest | Date", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Mode |
| `queries` | array | Search keywords |
| `location` | string | Location |
| `radius` | integer | Search radius (km) |
| `publishedDate` | string | Publication recency |
| `contractType` | array | Contract types |
| `contractDuration` | array | Working time |
| `jobCategory` | array | Professional domains |
| `minSalary` | integer | Minimum monthly gross salary (EUR) |
| `experience` | array | Experience levels |
| `seniority` | array | Qualification levels |
| `onlyFranceTravail` | boolean | Keep only France Travail listings |
| `inclusiveEmployer` | boolean | Disability-inclusive employers only |
| `adaptedCompany` | boolean | Adapted companies only |
| `sortBy` | string | Sort results |
| `urls` | array | Search URLs |
| `maxItems` | integer | Max listings (the run cap) |
| `maxPages` | integer | Max pages per search (0  unlimited) |
| `fetchDetails` | boolean | Fetch full job details |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/francetravail-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `id` | string |
| `url` | string |
| `title` | string |
| `seedId` | string |
| `seedType` | string |
| `seedValue` | string |
| `pageIndex` | integer |
| `company` | string |
| `location` | string |
| `postalCode` | string |
| `addressLocality` | string |
| `addressRegion` | null |
| `addressCountry` | string |
| `mapUrl` | string |
| `contractType` | string |
| `workTime` | string |
| `publishedAt` | string |
| `validThrough` | string |
| `description` | string |
| `salary` | integer |
| `salaryCurrency` | string |
| `salaryMin` | integer |
| `salaryMax` | integer |
| `salaryUnit` | string |
| `salaryText` | null |
| `employmentType` | null |
| `workHours` | string |
| `experienceRequirements` | list |
| `skills` | list |
| `softSkills` | list |
| `additionalInformation` | list |
| `companySize` | null |
| `recruiterName` | string |
| `recruiterDescription` | string |
| `employerPageUrl` | null |
| `employerLogoUrl` | null |
| `employerPhone` | null |
| `employerEmail` | null |
| `applyActionUrl` | string |

---

[← All scrapers](../../README.md)
