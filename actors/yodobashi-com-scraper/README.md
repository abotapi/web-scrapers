# Yodobashi Scraper

Scrape yodobashi.com electronics and appliances: JPY price, list price and discount, reward points, stock and delivery, images, specifications, variants and customer reviews. Search by keyword with the store's own category, brand, price and sort filters, or paste product, category and search URLs.

**[Open Yodobashi Scraper on Apify](https://apify.com/abotapi/yodobashi-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~yodobashi-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["カメラ"], "maxItems": 10, "maxPages": 1, "maxReviewsPerProduct": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `queries` | array | Search keywords |
| `categoryPath` | string | Category branch |
| `makerId` | string | Brand / maker id |
| `minPrice` | integer | Minimum price (JPY) |
| `maxPrice` | integer | Maximum price (JPY) |
| `sortBy` | string | Sort results by |
| `includeDiscontinued` | boolean | Include discontinued products |
| `urls` | array | Yodobashi URLs |
| `maxItems` | integer | Maximum products |
| `maxPages` | integer | Maximum pages per search or URL |
| `fetchDetails` | boolean | Fetch full product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Maximum reviews per product |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/yodobashi-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `sku` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `makerName` | string |
| `makerId` | string |
| `currency` | string |
| `price` | integer |
| `goldPoints` | integer |
| `goldPointRatePercent` | integer |
| `availability` | string |
| `inStock` | boolean |
| `deliveryMessage` | string |
| `deliveryBadge` | string |
| `rating` | integer |
| `reviewCount` | integer |
| `storeStockCount` | null |
| `categoryBreadcrumb` | list |
| `categoryUrl` | string |
| `releaseDate` | string |
| `thumbnail` | string |
| `images` | list |
| `sponsored` | boolean |
| `isDiscontinued` | boolean |
| `scrapedAt` | string |
| `reviews` | list |
| `reviewsReturned` | integer |
| `ratingBreakdown` | null |
| `familyReviewCount` | null |
| `unratedReviewCount` | null |

---

[← All scrapers](../../README.md)
