# Avito Real Estate Scraper

Scrape Avito real estate: apartments and rooms for sale or rent with rooms, area, floor, price per square metre, mortgage chips and the owner-vs-agent seller signal. City search with the site's own facet filters or paste links. Resume, incremental updates and MCP export included.

**[Open Avito Real Estate Scraper on Apify](https://apify.com/abotapi/avito-real-estate-listings-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~avito-real-estate-listings-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "regions": ["Moscow"], "category": "kvartiry", "dealType": "prodam", "sortBy": "default", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `regions` | array | Cities (search mode) |
| `category` | string | Category |
| `dealType` | string | Deal type |
| `rooms` | integer | Rooms (apartments for sale) |
| `features` | string | Feature facet (apartments for sale) |
| `minPrice` | integer | Min price (RUB) |
| `maxPrice` | integer | Max price (RUB) |
| `query` | string | Keyword |
| `sortBy` | string | Sort |
| `ownerOnly` | boolean | Private owners only |
| `urls` | array | Links (url mode) |
| `maxListings` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `fetchDetails` | boolean | Fetch detail pages |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/avito-real-estate-listings-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

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
| `viewsCount` | integer |
| `todayViews` | integer |
| `postedDateFull` | string |
| `attributes` | object |
| `lat` | float |
| `lng` | float |

---

[← All scrapers](../../README.md)
