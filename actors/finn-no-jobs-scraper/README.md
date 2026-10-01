# FINN.no Jobs Scraper

Scrape active FINN.no job listings by search filters or URL. Extract 30+ fields including full descriptions, employer details, deadlines, contacts, languages, sectors, industries, keywords and apply URLs.

**[Open FINN.no Jobs Scraper on Apify](https://apify.com/abotapi/finn-no-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~finn-no-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["developer"], "employmentType": "fulltime", "sector": "any", "workLanguage": "any", "publishedSince": "any", "sortBy": "default", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `queries` | array | Keywords (optional) |
| `location` | string | Location code (optional) |
| `employmentType` | string | Employment type |
| `industry` | string | Industry filter (optional) |
| `occupation` | string | Occupation filter (optional) |
| `sector` | string | Sector filter (optional) |
| `workLanguage` | string | Working language (optional) |
| `publishedSince` | string | Posted since (optional) |
| `sortBy` | string | Sort by |
| `urls` | array | Search URLs (URL mode) |
| `skipSponsored` | boolean | Skip sponsored placements (post-filter |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (total) |
| `fetchDetails` | boolean | Fetch detail pages (richer data) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/finn-no-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `idInt` | integer |
| `url` | string |
| `title` | string |
| `subtitle` | null |
| `employer` | string |
| `employerUrl` | null |
| `employerHomepage` | null |
| `employerLogo` | string |
| `streetAddress` | string |
| `postalCode` | string |
| `city` | string |
| `addressCountry` | string |
| `locationDisplay` | string |
| `locationLink` | string |
| `latitude` | float |
| `longitude` | float |
| `datePosted` | string |
| `datePostedEpochMs` | integer |
| `relativePosted` | string |
| `applicationDeadline` | string |
| `applicationDeadlineEpochMs` | integer |
| `applicationDeadlineRaw` | null |
| `lastModified` | string |
| `lastModifiedEpochMs` | integer |
| `employmentForm` | null |
| `employmentType` | list |
| `employmentTypeRequested` | string |
| `sector` | null |
| `industries` | list |
| `jobFunction` | string |
| `internalJobTitle` | null |
| `workingLanguages` | list |
| `contactPersons` | list |
| `keywords` | list |
| `applyUrl` | null |
| `descriptionHtml` | string |
| `descriptionText` | string |
| `breadcrumb` | list |
| `sponsored` | boolean |

---

[← All scrapers](../../README.md)
