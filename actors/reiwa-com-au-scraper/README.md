# REIWA Scraper

Scrape REIWA.com.au across sale, rental, sold, commercial, business and rural properties. Search with filters or URLs and extract structured listings, agents, agencies and market insights across Western Australia.

**[Open REIWA Scraper on Apify](https://apify.com/abotapi/reiwa-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~reiwa-com-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "channel": "for-sale", "locations": ["perth~region"], "sortBy": "default", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `channel` | string | REIWA section |
| `locations` | array | Suburbs or regions |
| `sortBy` | string | Sort order |
| `urls` | array | REIWA URLs |
| `keywords` | string | Keywords |
| `propertyTypes` | array | Property types |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `minBedrooms` | integer | Min bedrooms |
| `fetchDetails` | boolean | Fetch details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/reiwa-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `type` | string |
| `title` | string |
| `address` | string |
| `suburb` | string |
| `url` | string |
| `sourceUrl` | string |
| `price` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `parkingSpaces` | integer |
| `propertyType` | string |
| `agencyName` | string |
| `agencyUrl` | string |
| `agentNames` | list |
| `agentUrls` | list |
| `phoneNumbers` | list |
| `dateText` | string |
| `imageUrls` | list |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
