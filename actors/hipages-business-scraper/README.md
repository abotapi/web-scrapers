# HiPages Scraper

Scrape business listings from HiPages Australia by category, location, or URL. Extract business names, contact details, ratings, customer reviews, images, service areas, and other structured business information.

**[Open HiPages Scraper on Apify](https://apify.com/abotapi/hipages-business-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~hipages-business-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "category": "excavation", "state": "vic", "suburb": "clayton", "proxy": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `category` | string | Category |
| `state` | string | State |
| `suburb` | string | Suburb |
| `urls` | array | HiPages search URLs |
| `maxBusinesses` | integer | Maximum Businesses |
| `pageLimit` | integer | Page Limit |
| `scrapeDetails` | boolean | Scrape Business Details |
| `scrapeRecommendations` | boolean | Scrape All Recommendations |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/hipages-business-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `businessId` | string |
| `name` | string |
| `title` | string |
| `key` | string |
| `phone` | string |
| `mobile` | string |
| `serviceArea` | string |
| `highlights` | list |
| `hasLicense` | boolean |
| `hasValidAbn` | boolean |
| `starRating` | object |
| `totalRecommendations` | integer |
| `brandColor` | string |
| `theme` | string |
| `thumbnailUrl` | string |
| `galleryImages` | list |
| `profilePageUrl` | string |
| `profilePagePath` | string |
| `listingType` | string |
| `position` | integer |
| `distance` | integer |
| `searchContext` | object |

---

[← All scrapers](../../README.md)
