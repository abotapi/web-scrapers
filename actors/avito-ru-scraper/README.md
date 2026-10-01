# Avito.ru Scraper

Scrape structured listings from Avito.ru by region, category, filters, or direct URL. Automatically paginate through results and extract 25+ fields per listing, including price, full address, metro information, images, posting date, seller type, and verification badges.

**[Open Avito.ru Scraper on Apify](https://apify.com/abotapi/avito-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~avito-ru-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "regions": ["moskva"], "category": "kvartiry", "dealType": "prodam", "sortBy": "default", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `regions` | array | Regions |
| `category` | string | Category |
| `dealType` | string | Deal type |
| `query` | string | Free text search |
| `minPrice` | integer | Min price () |
| `maxPrice` | integer | Max price () |
| `sortBy` | string | Sort order |
| `ownerOnly` | boolean | Private sellers only |
| `urls` | array | Direct URLs |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings |
| `fetchDetails` | boolean | Fetch detail pages |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/avito-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `price` | integer |
| `currency` | string |
| `priceText` | string |
| `availability` | string |
| `category` | string |
| `subcategory` | string |
| `region` | string |
| `city` | string |
| `address` | string |
| `street` | string |
| `house` | string |
| `developmentName` | string |
| `metro` | string |
| `metroId` | integer |
| `metroDistanceMin` | integer |
| `rooms` | integer |
| `areaSqm` | float |
| `floor` | integer |
| `totalFloors` | integer |
| `postedDate` | string |
| `description` | string |
| `photoUrls` | list |
| `photoCount` | integer |
| `badges` | list |
| `isVerified` | boolean |
| `realtyBenefit` | string |
| `sellerName` | string |
| `sellerType` | string |
| `sellerRating` | null |
| `sellerReviewsCount` | null |
| `sellerSince` | string |
| `viewsCount` | null |
| `todayViews` | null |
| `postedDateFull` | string |
| `attributes` | object |
| `lat` | null |
| `lng` | null |

---

[← All scrapers](../../README.md)
