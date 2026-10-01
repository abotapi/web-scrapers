# ASOS Scraper

Scrape ASOS by keyword, category or URL. Every row carries the selling price and the original price, the discount, brand, colour and selling-fast flags. Sizes, per-size stock and reviews are one toggle away. Recurring change tracking is first-class.

**[Open ASOS Scraper on Apify](https://apify.com/abotapi/asos-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~asos-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["midi dress"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `urls` | array | ASOS URLs |
| `brandIds` | array | Brand ids |
| `baseColourIds` | array | Colour ids |
| `sortBy` | string | Sort the store's results by |
| `minPrice` | integer | Minimum price (GBP) |
| `maxPrice` | integer | Maximum price (GBP) |
| `onSaleOnly` | boolean | Discounted rows only |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/asos-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `rowType` | string |
| `productId` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `brandId` | null |
| `colour` | string |
| `colourWayId` | string |
| `price` | integer |
| `priceText` | string |
| `originalPrice` | null |
| `onSale` | null |
| `discountPercent` | null |
| `currency` | string |
| `isNew` | boolean |
| `isSellingFast` | boolean |
| `isRestockingSoon` | boolean |
| `isPromotion` | boolean |
| `hasMultipleColours` | boolean |
| `imageUrl` | string |
| `productCode` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
