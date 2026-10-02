# Viator Scraper

Collect Viator.com tour and activity results from destinations, categories, search pages, or pasted URLs. Returns product codes, prices, ratings, reviews, images, availability, source context, and optional detail fields.

**[Open Viator Scraper on Apify](https://apify.com/abotapi/viator-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~viator-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "destination": "boston", "category": "tours_sightseeing", "sortBy": "source", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `destination` | string | Destination |
| `category` | string | Category |
| `urls` | array | URLs |
| `keyword` | string | Keyword |
| `minPrice` | number | Min price |
| `maxPrice` | number | Max price |
| `currency` | string | Currency |
| `minRating` | number | Min rating |
| `minReviews` | integer | Min reviews |
| `availability` | string | Availability |
| `sortBy` | string | Sort |
| `fetchDetails` | boolean | Fetch details |
| `maxItems` * | integer | Max items |
| `maxPages` | integer | Max pages |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/viator-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `name` | string |
| `productCode` | string |
| `url` | string |
| `image` | string |
| `locationName` | string |
| `addressLocality` | string |
| `addressCountryName` | string |
| `offerPrice` | float |
| `offerCurrency` | string |
| `availability` | string |
| `priceValidUntil` | string |
| `ratingValue` | float |
| `exactRating` | float |
| `bestRating` | integer |
| `worstRating` | integer |
| `reviewCount` | integer |
| `position` | integer |
| `sourceUrl` | string |
| `sourcePage` | integer |
| `sourceName` | string |
| `sourceDescription` | string |
| `breadcrumbs` | list |
| `detailStatus` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
