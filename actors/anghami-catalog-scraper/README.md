# Anghami Scraper

Scrape Anghami's public catalog by keyword or player URL. Rows carry their kind (song, album, artist, playlist, tag) with title, artist, plays, followers, podcast flags and artwork. Detail views add the description and a podcast episode list, one per-record toggle.

**[Open Anghami Scraper on Apify](https://apify.com/abotapi/anghami-catalog-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~anghami-catalog-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["Sherine"], "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `urls` | array | Anghami URLs |
| `kinds` | array | Kinds to keep |
| `excludePodcasts` | boolean | Exclude podcasts |
| `fetchDetails` | boolean | Fetch record details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/anghami-catalog-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `kind` | string |
| `id` | string |
| `url` | string |
| `coverArt` | string |
| `name` | string |
| `verified` | boolean |
| `isPodcaster` | boolean |
| `artist_plays` | integer |
| `artist_followers` | integer |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
