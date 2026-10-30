# Fashion Nova Scraper

Scrape Fashion Nova products by keyword, collection or URL. Extract product names, current and original prices, available sizes, size-level stock status, full image galleries and customer reviews.

**[Open Fashion Nova Scraper on Apify](https://apify.com/abotapi/fashionnova-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~fashionnova-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["dresses"], "collections": ["new"], "sortBy": "relevance", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `collections` | array | Collections to browse (handles) |
| `urls` | array | Fashion Nova URLs |
| `sortBy` | string | Sort results by |
| `minPrice` | number | Minimum price |
| `maxPrice` | number | Maximum price |
| `onSaleOnly` | boolean | Only sale items |
| `availableOnly` | boolean | Only in-stock items |
| `fetchDetails` | boolean | Fetch customer reviews |
| `maxReviews` | integer | Max reviews per product |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/fashionnova-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `handle` | string |
| `baseHandle` | string |
| `url` | string |
| `title` | string |
| `baseTitle` | string |
| `color` | string |
| `colorFamily` | string |
| `brand` | string |
| `category` | string |
| `description` | string |
| `currency` | string |
| `price` | integer |
| `maxPrice` | null |
| `compareAtPrice` | float |
| `onSale` | boolean |
| `discountPercent` | integer |
| `availableForSale` | boolean |
| `isGiftCard` | boolean |
| `options` | list |
| `colorValues` | null |
| `sizeValues` | list |
| `variantCount` | integer |
| `inStockVariantCount` | integer |
| `sizesAvailable` | list |
| `sizesUnavailable` | null |
| `variants` | list |
| `imageUrl` | string |
| `imageUrls` | list |
| `imageCount` | integer |
| `tags` | list |
| `seoTitle` | string |
| `seoDescription` | string |
| `publishedAt` | string |
| `updatedAt` | string |
| `source` | string |
| `searchQuery` | string |
| `reviewCount` | integer |
| `reviewsRating` | float |
| `reviewsFit` | string |

---

[← All scrapers](../../README.md)
