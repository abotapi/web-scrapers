# Letterboxd Scraper

Scrape Letterboxd films and reviews by search phrase, popular or genre lists, or film URL. Extract ratings, directors, runtimes, review text and star ratings. Includes incremental monitoring, resume support and MCP connectors.

**[Open Letterboxd Scraper on Apify](https://apify.com/abotapi/letterboxd-film-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~letterboxd-film-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["dune"], "browsePath": "/films/popular/", "maxItems": 10, "maxPages": 1, "maxReviewsPerFilm": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["BUYPROXIES94952"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Input mode |
| `queries` | array | Search phrases |
| `startUrls` | array | Start URLs |
| `browsePath` | string | Browse path (URL mode fallback) |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `fetchReviews` | boolean | Fetch reader reviews |
| `maxReviewsPerFilm` | integer | Max reviews per film |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/letterboxd-film-reviews-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `url` | string |
| `slug` | string |
| `title` | string |
| `image` | string |
| `description` | string |
| `genre` | list |
| `directors` | list |
| `averageRating` | float |
| `ratingsCount` | integer |
| `datePublished` | null |
| `releaseYear` | integer |
| `tagline` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
