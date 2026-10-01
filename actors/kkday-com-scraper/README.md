# KKday Scraper

Scrape KKday travel activities by keyword, city or URL. Every row carries prices, discount, ratings, booking counts, destinations and images. Full details (description, address, coordinates, price tiers) are one toggle away, with recurring change tracking built in.

**[Open KKday Scraper on Apify](https://apify.com/abotapi/kkday-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~kkday-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "query": "Taipei", "language": "en", "currency": "USD", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "SG"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `query` | string | Search query |
| `language` | string | Language |
| `currency` | string | Currency |
| `urls` | array | KKday URLs |
| `fetchDetails` | boolean | Fetch activity details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max search pages |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/kkday-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `name` | string |
| `url` | string |
| `minPrice` | float |
| `maxPrice` | float |
| `officialPrice` | float |
| `currency` | string |
| `discountPercent` | null |
| `ratingStar` | integer |
| `ratingCount` | integer |
| `bookedCount` | string |
| `destinations` | list |
| `displayTags` | list |
| `imageUrl` | string |
| `supplierName` | null |
| `introduction` | string |
| `description` | string |
| `address` | string |
| `latitude` | float |
| `longitude` | float |
| `imageUrls` | list |
| `detailStatus` | string |
| `scrapedAt` | string |
| `changeType` | string |
| `changedFields` | list |
| `firstSeenAt` | string |
| `lastSeenAt` | string |

---

[← All scrapers](../../README.md)
