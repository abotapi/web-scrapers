# Mudah.my Cars Scraper

Scrape Mudah.my listings across every category: cars, motorcycles, property, mobiles, electronics, home, hobbies, jobs and services. Search by keyword, filter by category, state and price, or paste URLs. Rich records with seller, store verification, images and category-specific specs.

**[Open Mudah.my Cars Scraper on Apify](https://apify.com/abotapi/mudah-my-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~mudah-my-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["iphone"], "category": "all", "state": "all", "listingType": "all", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `category` | string | Category |
| `state` | string | State |
| `listingType` | string | Listing type |
| `startUrls` | array | Start URLs |
| `minPrice` | integer | Minimum price (RM) |
| `maxPrice` | integer | Maximum price (RM) |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/mudah-my-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `adId` | string |
| `url` | string |
| `title` | string |
| `price` | integer |
| `priceLabel` | string |
| `priceAlias` | integer |
| `currency` | string |
| `category` | object |
| `listingType` | string |
| `condition` | object |
| `location` | object |
| `seller` | object |
| `sellerVerified` | boolean |
| `images` | object |
| `timestamps` | object |
| `highlights` | null |
| `rank` | object |
| `bundle` | null |
| `reviews` | list |
| `scrapedAt` | string |
| `categoryId` | string |
| `categoryName` | string |
| `categoryLevel1Name` | string |
| `regionId` | string |
| `regionName` | string |
| `subarea` | string |
| `sellerName` | string |
| `raw` | object |

---

[← All scrapers](../../README.md)
