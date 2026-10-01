# Coupang Scraper

Scrape Coupang.com products by keyword, category or URL. Extract 20+ fields including title, brand, price, discount, ratings, reviews, availability, delivery, images, full descriptions, product URLs and image galleries.

**[Open Coupang Scraper on Apify](https://apify.com/abotapi/coupang-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~coupang-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["노트북"], "sortBy": "scoreDesc", "maxReviewsPerProduct": 10, "reviewSortBy": "ORDER_SCORE_ASC", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "KR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Run mode |
| `queries` | array | Search queries |
| `categoryId` | integer | Category ID |
| `sortBy` | string | Sort order |
| `urls` | array | URLs |
| `productIds` | array | Product IDs |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `reviewSortBy` | string | Review sort order |
| `reviewRatingFilter` | integer | Review rating filter |
| `minPrice` | integer | Min price (KRW) |
| `maxPrice` | integer | Max price (KRW) |
| `rocketOnly` | boolean | Rocket Delivery only |
| `minRating` | integer | Minimum average rating |
| `maxPages` | integer | Max pages per query / URL |
| `maxListings` | integer | Max listings (total) |
| `fetchDetails` | boolean | Fetch product detail pages |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/coupang-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `vendorItemId` | string |
| `itemId` | string |
| `title` | string |
| `brand` | null |
| `url` | string |
| `image` | string |
| `images` | null |
| `price` | integer |
| `originalPrice` | integer |
| `discountPercent` | integer |
| `isOnSpecial` | boolean |
| `savingsAmount` | integer |
| `unitPrice` | null |
| `currency` | string |
| `rating` | integer |
| `reviewCount` | integer |
| `rocketDelivery` | boolean |
| `rocketFresh` | boolean |
| `rocketGlobal` | boolean |
| `tomorrowDelivery` | boolean |
| `freeShipping` | null |
| `shippingCost` | null |
| `availability` | null |
| `deliveryInfo` | null |
| `isSponsored` | boolean |
| `usedMinPrice` | null |
| `usedListingCount` | null |
| `categoryId` | null |
| `categoryPath` | null |
| `description` | null |
| `specs` | null |
| `buyableQuantity` | null |
| `almostSoldOut` | null |
| `otherSellerCount` | null |
| `query` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
