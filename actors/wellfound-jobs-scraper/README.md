# Wellfound Jobs Scraper

Scrape startup jobs from Wellfound.com by keyword, location, role, or remote status. Extract job details, compensation, company badges, and other listing data, with MCP connector export support.

**[Open Wellfound Jobs Scraper on Apify](https://apify.com/abotapi/wellfound-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~wellfound-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["san-francisco"], "keywords": ["python"], "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Input mode |
| `locations` | array | Locations |
| `startUrls` | array | Wellfound URLs |
| `keywords` | array | Keywords |
| `roleKeywords` | array | Role keywords |
| `remoteOnly` | boolean | Remote only |
| `requireCompensation` | boolean | Require compensation |
| `activelyHiringOnly` | boolean | Actively hiring only |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/wellfound-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `jobId` | string |
| `jobUrl` | string |
| `jobSlug` | string |
| `jobTitle` | string |
| `descriptionText` | string |
| `descriptionLength` | integer |
| `jobType` | string |
| `primaryRoleTitle` | string |
| `compensation` | string |
| `compensationMin` | integer |
| `compensationMax` | integer |
| `compensationCurrency` | string |
| `hasCompensation` | boolean |
| `hasEquity` | boolean |
| `locations` | list |
| `acceptedRemoteLocations` | list |
| `remote` | boolean |
| `remoteKind` | string |
| `yearsExperienceMin` | null |
| `yearsExperienceMax` | null |
| `postedAtUnix` | integer |
| `postedAt` | string |
| `companyId` | string |
| `companyName` | string |
| `companySlug` | string |
| `companyUrl` | string |
| `companyLogoUrl` | string |
| `companySize` | string |
| `companyHighConcept` | string |
| `allBadgeLabels` | list |
| `activelyHiring` | boolean |
| `hasTopInvestors` | boolean |
| `quickResponder` | boolean |
| `topResponder` | boolean |
| `autoPosted` | boolean |
| `atsSource` | string |
| `sourceUrl` | string |
| `sourceLabel` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
