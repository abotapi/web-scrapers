# JB Hi-Fi AU Scraper

Scrape JB Hi-Fi Australia (jbhifi.com.au) products from the public storefront. Extract product listings, categories, prices, stock availability and customer reviews. Supports product search and category browsing.

**[Open JB Hi-Fi AU Scraper on Apify](https://apify.com/abotapi/jbhifi-com-au-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~jbhifi-com-au-product-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "query": "iphone", "sortBy": "relevance", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `query` | string | Search keyword |
| `category` | string | Category handle |
| `sortBy` | string | Sort |
| `facets` | array | Facet filters |
| `minPrice` | integer | Minimum price (AUD) |
| `maxPrice` | integer | Maximum price (AUD) |
| `onPromotionOnly` | boolean | On promotion only |
| `startUrls` | array | Links |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviews` | integer | Max reviews per product |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per scope |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/jbhifi-com-au-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `recordId` | string |
| `sku` | string |
| `objectID` | string |
| `handle` | string |
| `url` | string |
| `title` | string |
| `secondaryTitle` | null |
| `brand` | string |
| `brandLogoUrl` | null |
| `category` | string |
| `categoryHierarchy` | list |
| `department` | string |
| `productGroup` | string |
| `collectionHandles` | list |
| `collectionHierarchy` | null |
| `currency` | string |
| `price` | integer |
| `priceExGst` | integer |
| `taxGst` | integer |
| `wasPrice` | null |
| `saveAmount` | integer |
| `cashbackAmount` | integer |
| `coreTicketPrice` | integer |
| `perksPrice` | null |
| `availability` | string |
| `canBuyOnline` | boolean |
| `canPreOrder` | boolean |
| `deliveryStatus` | string |
| `clickNCollectStatus` | string |
| `inStockStoreCount` | integer |
| `rating` | float |
| `reviewCount` | integer |
| `releaseDate` | string |
| `publishedAt` | string |
| `updatedAt` | string |
| `imageUrl` | string |
| `imageUrls` | list |
| `onPromotion` | boolean |
| `promoTags` | list |

---

[← All scrapers](../../README.md)
