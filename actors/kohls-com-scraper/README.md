# Kohl's Scraper

Scrape Kohl's (kohls.com) products by keyword search or category browsing. Extract product names, brands, prices, descriptions, ratings, customer reviews and detailed product information. Ideal for price comparison, competitor analysis, product research and retail market intelligence.

**[Open Kohl's Scraper on Apify](https://apify.com/abotapi/kohls-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~kohls-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "urls", "searchTerms": ["womens jeans"], "urls": [{"url": "https://www.kohls.com/search.jsp?search=womens+jeans&PPP=120"}, {"url": "https://www.kohls.com/catalog/mens-clothing.jsp"}, {"url": "https://www.kohls.com/product/prd-7327369/nike-v5-rnr-womens-running-shoes.jsp"}], "proxyConfiguration": {"useApifyProxy": true, "apifyProxyCountry": "US"}, "maxReviews": 10, "changeScope": "all", "maxItems": 10}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `searchTerms` | array | Search terms |
| `urls` | array | Storefront links |
| `proxyConfiguration` | object | Proxy configuration |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviews` | integer | Max reviews per product |
| `expireAfterMissedScans` | integer | Expire after missed scans |
| `changeScope` | string | Change scope (incremental mode only) |
| `compactUpdates` | boolean | Compact UPDATED and EXPIRED rows (incr |
| `maxItems` | integer | Max items |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/kohls-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `productId` | string |
| `webId` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `priceLabel` | null |
| `price` | float |
| `priceMax` | float |
| `wasPrice` | null |
| `wasPriceMax` | null |
| `discountPercent` | null |
| `currency` | string |
| `imageUrl` | string |
| `rating` | float |
| `reviewsCount` | integer |
| `badges` | list |
| `colors` | list |
| `position` | integer |
| `description` | string |
| `sku` | string |
| `skus` | list |
| `availability` | string |
| `sellers` | list |
| `imageUrls` | list |
| `breadcrumbs` | list |
| `categoryPath` | list |
| `department` | string |
| `category` | string |
| `subcategory` | string |
| `colorsOutOfStock` | list |
| `sizes` | list |
| `specs` | list |
| `reviewsAverage` | float |
| `reviewsRecommended` | integer |
| `ratingDistribution` | list |
| `reviews` | list |
| `reviewsTotal` | integer |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
