# Yandex Maps Scraper

Scrape businesses and places from Yandex Maps by search term or URL for research, leads and market analysis. Парсер Яндекс Карт: собирайте данные о компаниях и местах по запросу или ссылке для поиска клиентов, исследований и анализа рынка.

**[Open Yandex Maps Scraper on Apify](https://apify.com/abotapi/yandex-maps-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~yandex-maps-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"searchStringsArray": ["restaurants"], "startUrls": [{"url": "https://yandex.com/maps/org/no_plates_coffee/124606085044/"}], "location": "New York, NY", "maxReviews": 10, "language": "en-US", "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `searchStringsArray` | array | Search Terms |
| `startUrls` | array | Start URLs |
| `location` | string | Location |
| `maxResultsPerSearch` | integer | Max Results Per Search |
| `maxPagesPerSearch` | integer | Max Pages Per Search |
| `includeRaw` | boolean | Include Raw Payload |
| `fetchDetails` | boolean | Business details & reviews |
| `maxReviews` | integer | Max reviews per business |
| `language` | string | Language / Locale |
| `proxyConfiguration` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/yandex-maps-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `source` | string |
| `id` | string |
| `title` | string |
| `scrapedAt` | string |
| `searchString` | string |
| `rank` | integer |
| `url` | string |
| `address` | string |
| `addressParts` | object |
| `country` | string |
| `categories` | list |
| `phone` | string |
| `phones` | list |
| `totalScore` | float |
| `reviewsCount` | integer |
| `photosCount` | integer |
| `photoUrls` | list |
| `seoname` | string |
| `reviews` | list |
| `location` | object |
| `workingTime` | object |

---

[← All scrapers](../../README.md)
