# Jora Jobs Scraper

Scrape Jora.com job listings across supported countries by keyword, filters, or URL. Extract full job descriptions, salaries, work types, companies, locations, and structured data ready for connector export.

**[Open Jora Jobs Scraper on Apify](https://apify.com/abotapi/jora-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~jora-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searches": [{"keywords": "software engineer", "location": "Sydney, NSW", "country": "au"}], "postedWithin": "anytime", "workType": "any", "sort": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searches` | array | Searches |
| `postedWithin` | string | Posted within |
| `workType` | string | Work type |
| `quickApply` | boolean | Quick apply only |
| `sort` | string | Sort by |
| `distanceKm` | integer | Search radius (km) |
| `salaryMin` | integer | Minimum salary |
| `urls` | array | Jora URLs |
| `fetchDetails` | boolean | Fetch full job details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/jora-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `jobId` | string |
| `title` | string |
| `company` | string |
| `location` | string |
| `countryCode` | string |
| `url` | string |
| `sourceUrl` | string |
| `salary` | string |
| `salaryMin` | integer |
| `salaryMax` | integer |
| `workType` | string |
| `workArrangement` | null |
| `postedAtText` | string |
| `quickApply` | boolean |
| `isSponsored` | boolean |
| `rank` | integer |
| `page` | integer |
| `abstract` | string |
| `snippetBullets` | list |
| `descriptionHtml` | string |
| `descriptionText` | string |
| `applyUrl` | string |
| `sourceName` | string |
| `searchKeywords` | string |
| `searchLocation` | string |
| `searchTotalCount` | integer |
| `detailFetched` | boolean |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
