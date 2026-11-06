# Miravia Spain Scraper

Scrape Miravia Spain by keyword, seller store or URL. Every row carries the selling price and the original price, the discount, brand, seller and rating. Details, variants and reviews are toggles. Change tracking is first-class.

**[Open Miravia Spain Scraper on Apify](https://apify.com/abotapi/miravia-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~miravia-es-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["lego"], "sortBy": "relevance", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `categoryId` | string | Category (search mode only) |
| `sellerId` | string | Only this seller (minor filter) |
| `urls` | array | Miravia URLs |
| `sortBy` | string | Sort the storefront results by |
| `minPrice` | number | Minimum price (EUR) |
| `maxPrice` | number | Maximum price (EUR) |
| `onSaleOnly` | boolean | Discounted rows only |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviews` | integer | Max reviews per product |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/miravia-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `rowType` | string |
| `productId` | string |
| `skuId` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `brandId` | string |
| `price` | float |
| `priceText` | string |
| `originalPrice` | null |
| `originalPriceText` | string |
| `onSale` | null |
| `discountPercent` | null |
| `discountTag` | null |
| `currency` | string |
| `imageUrl` | string |
| `sellerId` | string |
| `sellerName` | string |
| `officialStore` | boolean |
| `rating` | integer |
| `reviewCount` | integer |
| `soldCount` | null |
| `soldText` | null |
| `inStock` | boolean |
| `isSponsored` | boolean |
| `promotionTags` | list |
| `promotionTagCodes` | list |
| `categoryIds` | list |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
