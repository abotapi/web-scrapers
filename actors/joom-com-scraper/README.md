# Joom Scraper

Scrape Joom products by keyword or URL. Extract product names, prices, discounts, sellers, ratings and images, with optional detailed descriptions, variants and customer reviews. Supports product, search and category URLs for flexible data collection.

**[Open Joom Scraper on Apify](https://apify.com/abotapi/joom-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~joom-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["headphones"], "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `urls` | array | Marketplace URLs |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `onSaleOnly` | boolean | Discounted rows only |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch reviews with details |
| `maxReviews` | integer | Max reviews per product |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/joom-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `rowType` | string |
| `productId` | string |
| `url` | string |
| `title` | string |
| `price` | float |
| `currency` | string |
| `originalPrice` | null |
| `onSale` | boolean |
| `discountPercent` | integer |
| `imageUrl` | string |
| `imageUrls` | list |
| `inStock` | boolean |
| `averageRating` | null |
| `reviewCountText` | null |
| `isAd` | boolean |
| `storeId` | string |
| `position` | integer |
| `searchTerm` | string |
| `scopeKind` | string |
| `categoryId` | string |
| `description` | string |
| `minPrice` | float |
| `maxPrice` | float |
| `shippingMinPrice` | integer |
| `shippingMaxPrice` | integer |
| `shippingCurrency` | string |
| `category` | string |
| `storeName` | string |
| `storeRating` | null |
| `reviewCount` | integer |
| `ratingDistribution` | object |
| `variantsCount` | integer |
| `variantSizes` | list |
| `variantColors` | list |
| `variantMinPrice` | null |
| `variantMaxPrice` | null |
| `inventoryTotal` | integer |
| `deliveryMinDays` | null |
| `deliveryMaxDays` | null |

---

[← All scrapers](../../README.md)
