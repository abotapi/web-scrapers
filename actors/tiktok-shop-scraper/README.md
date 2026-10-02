# TikTok Shop Scraper

Scrape TikTok Shop listings by keyword search, category, or direct product links. Returns title, price, discount, sold count, rating, review count, images, shop name and variations, plus with details enabled: description, rating breakdown and item-level reviews. Supports incremental monitoring.

**[Open TikTok Shop Scraper on Apify](https://apify.com/abotapi/tiktok-shop-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~tiktok-shop-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "category", "queries": ["phone case"], "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `categoryUrls` | array | Category links |
| `includeSubcategories` | boolean | Include subcategories |
| `queries` | array | Search keywords |
| `productUrls` | array | Product links |
| `maxItems` | integer | Max listings |
| `maxPages` | integer | Max pages (optional) |
| `fetchDetails` | boolean | Fetch product details |
| `includeReviews` | boolean | Include item reviews |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/tiktok-shop-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `title` | string |
| `url` | string |
| `categoryPath` | list |
| `price` | integer |
| `currency` | string |
| `originalPrice` | null |
| `discountPercent` | null |
| `soldCount` | integer |
| `rating` | float |
| `reviewCount` | integer |
| `ratingHistogram` | object |
| `images` | list |
| `shopName` | string |
| `description` | string |
| `variations` | list |
| `reviews` | list |
| `searchMode` | string |
| `shopId` | string |
| `sellerRating` | float |
| `sellerProductCount` | integer |
| `sellerFollowers` | integer |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
