# BookMyShow Scraper

Scrape BookMyShow movies and live events by city, category or URL. Extract genres, languages, posters, synopsis, cast, show dates and cinema showtimes. Includes incremental monitoring, resume support and MCP export.

**[Open BookMyShow Scraper on Apify](https://apify.com/abotapi/bookmyshow-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~bookmyshow-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "city": "mumbai", "category": "movies", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "IN"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `city` | string | City |
| `category` | string | Category |
| `languages` | string | Languages |
| `genres` | string | Genres |
| `formats` | string | Formats |
| `urls` | array | BookMyShow links |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per scope |
| `fetchDetails` | boolean | Fetch details |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/bookmyshow-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `eventCode` | string |
| `title` | string |
| `url` | string |
| `posterUrl` | string |
| `languages` | list |
| `genres` | list |
| `category` | null |
| `regionCode` | string |
| `venueName` | null |
| `venueCode` | null |
| `listingSection` | null |
| `tags` | list |
| `synopsis` | string |
| `duration` | string |
| `censor` | string |
| `releaseDate` | string |
| `formats` | list |
| `cast` | list |
| `director` | string |
| `priceDisplay` | null |
| `availability` | null |
| `dateText` | null |
| `timeText` | null |

---

[← All scrapers](../../README.md)
