# US Distressed Property Scraper

Scrape US distressed property leads from Socrata open data across Chicago, New York, Seattle and New Orleans. Extract building violations, vacant properties, tax sales and foreclosure records. Supports resume and incremental change tracking for ongoing property monitoring.

**[Open US Distressed Property Scraper on Apify](https://apify.com/abotapi/distressed-us-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~distressed-us-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "metros": ["chicago"], "sortOrder": "newest", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `metros` | array | Metro areas |
| `datasetId` | string | Dataset override (optional) |
| `datasetDomain` | string | Dataset domain (optional) |
| `sinceDays` | integer | Only rows newer than N days |
| `soqlWhere` | string | Raw SoQL filter (where) |
| `dateFrom` | string | Date from (YYYY-MM-DD) |
| `dateTo` | string | Date to (YYYY-MM-DD) |
| `sortOrder` | string | Sort order |
| `maxItemsPerDataset` | integer | Max items per dataset (0  no cap) |
| `urls` | array | URLs |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per dataset (0  unlimited) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/distressed-us-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

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
| `portalId` | string |
| `publishedAt` | string |
| `location` | object |
| `status` | string |
| `description` | string |
| `sourceDomain` | string |
| `datasetId` | string |
| `sourceRecordId` | string |
| `latitude` | float |
| `longitude` | float |
| `city` | string |
| `state` | string |
| `details` | object |
| `raw` | object |

---

[← All scrapers](../../README.md)
