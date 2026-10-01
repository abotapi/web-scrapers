# Yandex SERP Scraper

Scrape Yandex web, image and video results with URLs, snippets and organic rankings for SEO and competitor research. Парсер Яндекс Поиска, картинок и видео: ссылки, сниппеты и позиции для SEO, мониторинга выдачи и анализа конкурентов.

**[Open Yandex SERP Scraper on Apify](https://apify.com/abotapi/yandex-serp-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~yandex-serp-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"searchType": "web", "queries": ["best coffee grinder"], "maxPages": 1, "maxItems": 10, "proxySettings": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `searchType` | string | Search type |
| `queries` * | array | Search queries |
| `maxPages` | integer | Max pages per query |
| `lr` | integer | Region ID (lr) |
| `maxItems` | integer | Max results |
| `proxySettings` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/yandex-serp-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `query` | string |
| `page` | integer |
| `position` | integer |
| `title` | string |
| `url` | string |
| `domain` | string |
| `breadcrumb` | string |
| `snippet` | string |

---

[← All scrapers](../../README.md)
