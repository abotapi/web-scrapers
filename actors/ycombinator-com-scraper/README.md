# Ycombinator Scraper

Pull every ycombinator.com company across every batch, with founders, social URLs, application Q&A, demo-day video, photos, and partner. Filter by 14 dimensions or paste any /companies search URL straight from your browser.

**[Open Ycombinator Scraper on Apify](https://apify.com/abotapi/ycombinator-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~ycombinator-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "batches": ["Winter 2026", "Spring 2026"], "sortBy": "relevance", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `query` | string | Free-text query |
| `batches` | array | Batches |
| `industries` | array | Industries |
| `subindustries` | array | Subindustries |
| `regions` | array | Regions |
| `tags` | array | Tags |
| `statuses` | array | Status |
| `stages` | array | Stage |
| `isHiring` | boolean | Hiring only |
| `topCompany` | boolean | Top companies only |
| `nonprofit` | boolean | Nonprofits only |
| `hasDemoDayVideo` | boolean | Has demo-day video |
| `hasAppVideo` | boolean | Has application video |
| `hasAppAnswers` | boolean | Has application answers |
| `sortBy` | string | Sort order |
| `urls` | array | Search URLs |
| `fetchDetails` | boolean | Fetch full detail page (recommended ON |
| `maxListings` | integer | Max companies |
| `maxPages` | integer | Max search pages |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/ycombinator-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `slug` | string |
| `objectID` | string |
| `name` | string |
| `url` | string |
| `oneLiner` | string |
| `longDescription` | string |
| `website` | string |
| `batch` | string |
| `batchName` | string |
| `status` | string |
| `stage` | string |
| `industry` | string |
| `subindustry` | string |
| `industries` | list |
| `tags` | list |
| `regions` | list |
| `allLocations` | string |
| `teamSize` | integer |
| `yearFounded` | integer |
| `launchedAt` | integer |
| `isHiring` | boolean |
| `topCompany` | boolean |
| `nonprofit` | boolean |
| `hasAppVideo` | boolean |
| `hasDemoDayVideo` | boolean |
| `hasQuestionAnswers` | boolean |
| `formerNames` | list |
| `logoUrl` | string |
| `smallLogoUrl` | string |
| `location` | string |
| `city` | string |
| `cityTag` | string |
| `country` | string |
| `linkedinUrl` | null |
| `twitterUrl` | null |
| `facebookUrl` | null |
| `crunchbaseUrl` | null |
| `githubUrl` | null |
| `demoDayVideoUrl` | null |

---

[← All scrapers](../../README.md)
