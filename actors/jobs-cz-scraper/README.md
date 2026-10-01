# Jobs.cz Scraper

Scrape Czech job listings from Jobs.cz. Search builder (keyword, location, field, salary, employment type) or paste any Jobs.cz URL. Title, company, salary range with currency and period, benefits, GPS coordinates, required education and languages, employer contact info, remote/hybrid flag,.

**[Open Jobs.cz Scraper on Apify](https://apify.com/abotapi/jobs-cz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~jobs-cz-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keyword": "python", "location": "Praha", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `keyword` | string | Keyword / job title |
| `location` | string | Location |
| `field` | string | Field (obor) |
| `minSalary` | integer | Minimum gross salary (CZK/month) |
| `employmentType` | string | Employment type |
| `education` | string | Required education |
| `arrangement` | string | Work arrangement |
| `urls` | array | Jobs.cz URLs |
| `maxItems` | integer | Max items (total) |
| `maxPages` | integer | Max pages per search |
| `fetchDetails` | boolean | Fetch full job details |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/jobs-cz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `source` | string |
| `jobId` | string |
| `jobUrl` | string |
| `title` | string |
| `companyName` | string |
| `companyLogo` | string |
| `location` | string |
| `country` | string |
| `arrangementTags` | list |
| `arrangement` | string |
| `remote` | boolean |
| `status` | string |
| `teaser` | null |
| `detailSource` | null |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
