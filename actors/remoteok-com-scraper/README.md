# RemoteOK Jobs Scraper

Scrape RemoteOK jobs by keyword or job URL. Extract title, company, location, remote details, tags, salary when available, listing URL, description, and metadata into clean structured dataset rows.

**[Open RemoteOK Jobs Scraper on Apify](https://apify.com/abotapi/remoteok-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~remoteok-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["all jobs"], "sortBy": "posted-desc", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Input mode |
| `searchTerms` | array | Search terms |
| `startUrls` | array | RemoteOK URLs |
| `tags` | array | Require tags |
| `companies` | array | Company filters |
| `locations` | array | Location filters |
| `minSalary` | integer | Minimum salary |
| `maxSalary` | integer | Maximum salary |
| `postedWithinDays` | integer | Posted within days |
| `sortBy` | string | Sort order |
| `requireSalary` | boolean | Require salary |
| `includeDescriptionText` | boolean | Include cleaned description text |
| `includeRawFields` | boolean | Include raw source fields |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages |
| `proxy` | object | Proxy configuration |
| `maxNotifyJobs` | integer | Max jobs to export per connector |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/remoteok-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `slug` | string |
| `id` | string |
| `epoch` | integer |
| `date` | string |
| `company` | string |
| `company_logo` | null |
| `position` | string |
| `tags` | list |
| `description` | string |
| `location` | null |
| `salary_min` | integer |
| `salary_max` | integer |
| `apply_url` | string |
| `original` | boolean |
| `logo` | string |
| `url` | string |
| `jobId` | string |
| `title` | string |
| `companyName` | string |
| `locationText` | null |
| `rawLocation` | null |
| `descriptionText` | string |
| `tagCount` | integer |
| `applyUrl` | string |
| `sourceUrl` | string |
| `sourceType` | string |
| `searchTerm` | null |
| `postedAt` | string |
| `postedEpoch` | integer |
| `postedAgeDays` | integer |
| `salaryMid` | integer |
| `hasSalary` | boolean |
| `companyLogoUrl` | null |
| `scrapedAt` | string |
| `matchedSearchTokens` | list |
| `matchedTagFilters` | list |
| `raw` | object |

---

[← All scrapers](../../README.md)
