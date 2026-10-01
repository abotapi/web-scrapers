# Naver Land Scraper

Scrape structured property listings from Naver Land map URLs. Extract listing titles, prices, areas, addresses, GPS coordinates, property types, transaction types and source links for clean real estate datasets.

**[Open Naver Land Scraper on Apify](https://apify.com/abotapi/naver-land-listings?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~naver-land-listings/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"searchKeywords": ["잠실"], "startUrls": ["https://new.land.naver.com/complexes?ms=2AM2Zq,3zhF96,16&a=APT:ABYG:JGC&e=RETAIL", "https://new.land.naver.com/complexes/111380", "https://new.land.naver.com/article/2651481309"], "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "KR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `searchKeywords` | array | Search keywords |
| `startUrls` | array | Naver Land URLs |
| `maxItems` | integer | Maximum listings |
| `fetchDetails` | boolean | Fetch listing details |
| `proxy` | object | Connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/naver-land-listings?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `articleNo` | null |
| `complexNo` | string |
| `title` | string |
| `propertyType` | string |
| `tradeType` | null |
| `price` | null |
| `area` | string |
| `floor` | null |
| `direction` | null |
| `address` | string |
| `latitude` | float |
| `longitude` | float |
| `thumbnailUrl` | null |
| `articleUrl` | string |
| `sourceUrl` | string |
| `detailFetched` | boolean |
| `raw` | object |
| `crawledAt` | string |
| `rank` | integer |

---

[← All scrapers](../../README.md)
