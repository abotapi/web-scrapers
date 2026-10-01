# Eventim Scraper

Scrape CTS Eventim Germany and EU event catalogue: concerts, festivals, comedy, sports, dates, venues, prices and availability. Search by city, keyword, category and date, or paste event links. Incremental monitoring with NEW, UPDATED, REAPPEARED, EXPIRED, resume and MCP export.

**[Open Eventim Scraper on Apify](https://apify.com/abotapi/eventim-de-event-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~eventim-de-event-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "cities": ["Berlin"], "sort": "DateAsc", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `cities` | array | Cities |
| `query` | string | Keyword |
| `categories` | array | Categories |
| `dateFrom` | string | Events from (YYYY-MM-DD) |
| `dateTo` | string | Events until (YYYY-MM-DD) |
| `inStockOnly` | boolean | Available tickets only |
| `sort` | string | Sort order |
| `urls` | array | Eventim links |
| `fetchDetails` | boolean | Fetch event details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max scopes |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/eventim-de-event-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `eventId` | string |
| `productGroupId` | string |
| `url` | string |
| `title` | string |
| `startDate` | string |
| `endDate` | string |
| `eventStatus` | string |
| `eventType` | string |
| `venueName` | string |
| `venueStreet` | null |
| `venueCity` | string |
| `venueRegion` | null |
| `venuePostalCode` | null |
| `venueCountry` | null |
| `venueUrl` | null |
| `priceFrom` | float |
| `priceHigh` | null |
| `priceCurrency` | string |
| `priceTiers` | null |
| `ticketAvailability` | string |
| `promoterName` | string |
| `categories` | list |
| `tags` | list |
| `description` | null |
| `imageUrl` | null |
| `validFrom` | null |
| `raw` | object |

---

[← All scrapers](../../README.md)
