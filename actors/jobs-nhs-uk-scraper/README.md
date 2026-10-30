# NHS UK Scraper

Scrape nhs.uk Jobs listings into a flat dataset. Extract 50+ fields, including pay band, salary, full description, essential and desirable criteria, PDFs, sponsorship, DBS, employer details, contacts, and apply URL. Search by filters or use any URL.

**[Open NHS UK Scraper on Apify](https://apify.com/abotapi/jobs-nhs-uk-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~jobs-nhs-uk-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": ["doctor"], "location": "London", "distance": "10", "maxPages": 1, "maxListings": 10, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `keywords` | array | Keywords (optional) |
| `location` | string | Location (optional) |
| `distance` | string | Distance (miles) |
| `payBands` | array | Pay bands (Agenda for Change  Doctor g |
| `staffGroups` | array | Staff group |
| `contractTypes` | array | Contract type |
| `workingPatterns` | array | Working pattern |
| `payRanges` | array | Pay range (k GBP per year) |
| `employerName` | string | Employer name (optional) |
| `covidJobsOnly` | boolean | COVID-related roles only |
| `salaryFrom` | integer | Minimum salary (GBP per year) |
| `salaryTo` | integer | Maximum salary (GBP per year) |
| `jobReference` | string | Job reference |
| `sortBy` | string | Sort by |
| `urls` | array | Search URLs (URL mode) |
| `startUrl` | string | Start URL (alias) |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (total, default 20, 0  un |
| `maxItems` | integer | Max items (alias of Max listings) |
| `proxy` | object | Proxy configuration |
| `fetchDetails` | boolean | Fetch detail pages (richer data) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/jobs-nhs-uk-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `referenceNumber` | string |
| `employer` | string |
| `employerWebsite` | string |
| `employerLogoDataUri` | string |
| `location` | string |
| `postcode` | string |
| `addressLine1` | string |
| `addressLine2` | string |
| `addressTown` | string |
| `addressCounty` | null |
| `addressLines` | list |
| `salary` | string |
| `salaryQualifier` | null |
| `salaryMin` | null |
| `salaryMax` | null |
| `salaryPeriod` | null |
| `payScheme` | string |
| `grade` | string |
| `contractType` | string |
| `contractDuration` | null |
| `workingPattern` | string |
| `datePosted` | string |
| `datePostedIso` | string |
| `closingDate` | string |
| `closingDateIso` | string |
| `interviewDate` | null |
| `applyUrl` | string |
| `contactName` | string |
| `contactJobTitle` | string |
| `contactEmail` | string |
| `contactPhone` | null |
| `contactDetails` | object |
| `employerDetails` | object |
| `jobOverviewHtml` | string |
| `jobOverviewText` | string |
| `mainDutiesHtml` | string |
| `mainDutiesText` | null |

---

[← All scrapers](../../README.md)
