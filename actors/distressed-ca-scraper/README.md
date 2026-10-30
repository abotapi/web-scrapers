# Canada Distressed Property Scraper

Canadian tax-sale properties from taxsales.ca: tender and auction listings across 9 provinces with minimum bid, deadline or auction date, roll number, legal description and the municipality's notice, plus resume and incremental change tracking.

**[Open Canada Distressed Property Scraper on Apify](https://apify.com/abotapi/distressed-ca-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~distressed-ca-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "provinces": ["on"], "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `provinces` | array | Provinces to walk |
| `status` | string | Status |
| `type` | string | Property type |
| `minTender` | integer | Minimum tender amount |
| `maxTender` | integer | Maximum tender amount |
| `closingIn` | integer | Closing within (days) |
| `sort` | string | Sort |
| `urls` | array | URLs |
| `fetchDetails` | boolean | Fetch detail pages |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search (0  unlimited) |
| `proxy` | object | Proxy configuration |
| `changeScope` | string | Change scope (incremental mode only) |
| `compactUpdates` | boolean | Compact updated rows (incremental mode |
| `expireAfterMissedScans` | integer | Expire after N missed scans (increment |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/distressed-ca-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `country` | string |
| `source` | string |
| `title` | string |
| `distressType` | string |
| `url` | string |
| `caseNumber` | string |
| `deadlineAt` | string |
| `location` | object |
| `valueText` | string |
| `valueAmount` | float |
| `valueCurrency` | string |
| `attachments` | list |
| `details` | object |
| `status` | string |

---

[← All scrapers](../../README.md)
