# EmploymentHero Scraper

Scrape Employment Hero's job marketplace: roles with pay ranges, full descriptions, locations and work types; employer profiles with websites and open roles; webinars and events; partner directory and customer case studies. Search with filters, paste links, or target employers directly.

**[Open EmploymentHero Scraper on Apify](https://apify.com/abotapi/employmenthero-jobs-employers-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~employmenthero-jobs-employers-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locationRadiusKm": "25", "countries": ["AU", "CA", "GB", "NZ"], "sortBy": "relevance", "resourceTypes": ["webinars"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `query` | string | Keywords |
| `locations` | array | Locations |
| `locationRadiusKm` | string | Location radius |
| `countries` | array | Countries |
| `sectors` | array | Sectors |
| `workplaceTypes` | array | Workplace types |
| `employmentTypes` | array | Employment types |
| `experienceLevels` | array | Experience levels |
| `datePostedDays` | string | Posted within (days) |
| `sortBy` | string | Sort |
| `organisationSlugs` | array | Employers |
| `resourceTypes` | array | Resource types |
| `resourceSearch` | string | Resource keywords |
| `urls` | array | URLs |
| `fetchOrgDetails` | boolean | Add employer details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/employmenthero-jobs-employers-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `id` | string |
| `jobId` | null |
| `friendlyId` | string |
| `url` | string |
| `title` | string |
| `description` | string |
| `companyOverview` | null |
| `postedAt` | string |
| `employmentType` | string |
| `employmentTerm` | string |
| `experienceLevel` | string |
| `workplaceType` | string |
| `remote` | boolean |
| `salaryMin` | null |
| `salaryMax` | null |
| `salaryCurrency` | string |
| `salaryRate` | string |
| `payHidden` | boolean |
| `location` | string |
| `countryCode` | string |
| `sectorId` | integer |
| `sectorName` | string |
| `teamName` | null |
| `eoi` | boolean |
| `organisationId` | string |
| `organisationName` | string |
| `organisationSlug` | string |
| `organisationUrl` | string |
| `organisationLogo` | null |
| `recruiterLogoUrl` | null |
| `isDemoJob` | boolean |
| `attachmentUrl` | null |
| `locationCity` | string |
| `locationRegion` | string |
| `locationPostcode` | string |
| `salaryDisplay` | null |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
