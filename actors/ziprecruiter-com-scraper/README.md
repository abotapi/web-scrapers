# ZipRecruiter Scraper

Scrape ZipRecruiter jobs with titles, companies, salaries, locations, benefits, apply URLs and full descriptions. Search with filters or paste ZipRecruiter URLs directly, with automatic pagination and simple pay-per-result pricing.

**[Open ZipRecruiter Scraper on Apify](https://apify.com/abotapi/ziprecruiter-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~ziprecruiter-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["software engineer"], "location": "Remote", "datePosted": "any", "employmentType": "any", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `queries` | array | Keywords |
| `location` | string | Location (optional) |
| `datePosted` | string | Date posted |
| `employmentType` | string | Employment type |
| `remoteOnly` | boolean | Remote jobs only |
| `minSalary` | integer | Minimum annual salary (USD) |
| `radius` | integer | Search radius (miles) |
| `skipSponsored` | boolean | Skip sponsored placements |
| `urls` | array | Search URLs (URL mode) |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (total) |
| `fetchDetails` | boolean | Fetch detail pages (richer data) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/ziprecruiter-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `listingKey` | string |
| `url` | string |
| `title` | string |
| `company` | string |
| `companyId` | string |
| `companyUrl` | string |
| `companyWebsite` | null |
| `companyLogo` | string |
| `location` | string |
| `city` | string |
| `state` | string |
| `county` | string |
| `postalCode` | null |
| `streetAddress` | null |
| `country` | string |
| `latitude` | null |
| `longitude` | null |
| `locationType` | string |
| `remote` | boolean |
| `salary` | string |
| `salaryMin` | integer |
| `salaryMax` | integer |
| `salaryCurrency` | string |
| `salaryPeriod` | string |
| `employmentTypes` | list |
| `employmentType` | string |
| `industry` | null |
| `occupationalCategory` | null |
| `benefits` | list |
| `benefitsText` | null |
| `snippet` | string |
| `descriptionHtml` | null |
| `descriptionText` | null |
| `emails` | list |
| `phoneNumbers` | list |
| `datePosted` | string |
| `postedAt` | string |
| `validThrough` | null |
| `isActive` | boolean |

---

[← All scrapers](../../README.md)
