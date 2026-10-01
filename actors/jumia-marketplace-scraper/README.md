# Jumia Marketplace Scraper

Scrape Jumia, Africa's largest marketplace: products with local prices, discounts, ratings, official-store badges and customer reviews across the Nigeria, Egypt, Kenya and Morocco storefronts. Search keywords or paste links, and monitor price changes with recurring updates.

**[Open Jumia Marketplace Scraper on Apify](https://apify.com/abotapi/jumia-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~jumia-marketplace-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "country": "ng", "queries": ["phone"], "sort": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `country` | string | Market |
| `queries` | array | Search terms |
| `sort` | string | Ordering |
| `brands` | array | Brand filter (optional) |
| `officialStoreOnly` | boolean | Only official stores |
| `minDiscount` | integer | Minimum discount % (optional) |
| `urls` | array | Product, vendor or catalogue links |
| `fetchDetails` | boolean | Read product detail pages |
| `fetchReviews` | boolean | Read customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max records |
| `maxPages` | integer | Max pages per source |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/jumia-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `sku` | string |
| `name` | string |
| `displayName` | string |
| `brand` | string |
| `categories` | list |
| `url` | string |
| `imageUrl` | string |
| `currency` | string |
| `price` | float |
| `priceDisplay` | string |
| `oldPrice` | integer |
| `discountPercent` | integer |
| `ratingAverage` | float |
| `ratingCount` | integer |
| `officialStore` | boolean |
| `badges` | list |
| `sellerId` | integer |
| `shopExpress` | boolean |
| `sponsored` | boolean |
| `buyable` | boolean |
| `market` | string |
| `marketHost` | string |
| `lastModified` | integer |
| `gtin` | null |
| `sourceType` | string |
| `sourceId` | string |
| `sourceUrl` | null |
| `position` | integer |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
