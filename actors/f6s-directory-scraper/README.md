# F6S Scraper

Extract structured data from F6S.com. Scrape funding programs, startup accelerators, events, and jobs from a single tool. Supports both filter-based searches and F6S URLs, returns 25+ fields per record, and works on all Apify plans.

**[Open F6S Scraper on Apify](https://apify.com/abotapi/f6s-directory-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~f6s-directory-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "listType": "programs", "programType": "any", "sortBy": "open", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `listType` | string | List type |
| `location` | string | Location |
| `keyword` | string | Keyword |
| `programType` | string | Program type |
| `sortBy` | string | Sort by |
| `minInvestment` | integer | Min investment (USD) |
| `maxInvestment` | integer | Max investment (USD) |
| `maxEquity` | integer | Max equity (%) |
| `urls` | array | F6S list URLs |
| `fetchDetails` | boolean | Fetch full details (richer records, ex |
| `maxPages` | integer | Max pages per list |
| `maxListings` | integer | Max records |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/f6s-directory-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `listType` | string |
| `name` | string |
| `slug` | string |
| `profileUrl` | string |
| `aboutUrl` | string |
| `applyUrl` | string |
| `image` | string |
| `location` | string |
| `tags` | string |
| `verified` | boolean |
| `deadline` | string |
| `investmentRaw` | null |
| `investmentAmount` | null |
| `investmentCurrency` | null |
| `equityRaw` | null |
| `equityPercent` | null |
| `sourceUrl` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
