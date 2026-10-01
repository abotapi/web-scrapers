# JioHotstar Scraper

Scrape the JioHotstar catalog by content type or URL. Extract shows, movies, episodes, sports, clips and live content, with one structured record per catalog URL including title, show name, content IDs and source URL.

**[Open JioHotstar Scraper on Apify](https://apify.com/abotapi/hotstar-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~hotstar-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "sitemap", "mapType": "EPISODE", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "IN"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `mapType` | string | Catalog type |
| `urls` | array | Hotstar catalog URLs |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max maps per run |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/hotstar-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `url` | string |
| `kind` | string |
| `title` | string |
| `showTitle` | string |
| `showId` | string |
| `contentId` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
