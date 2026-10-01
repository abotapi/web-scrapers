# Trendyol Scraper

Scrape Trendyol products, prices, ratings, badges, sellers, full reviews and Q&A. Search by keyword with filters, paste search, category, store or product URLs, or use reviews-only mode for a list of products.

**[Open Trendyol Scraper on Apify](https://apify.com/abotapi/trendyol-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~trendyol-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["iphone"], "sortBy": "BEST_SCORE", "maxReviewsPerProduct": 10, "minRating": "0", "maxPages": 1, "maxListings": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "TR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search queries |
| `specialsCategory` | string | Specials / campaign tier |
| `sortBy` | string | Sort by |
| `urls` | array | Trendyol URLs |
| `productInputs` | array | Products to fetch reviews for |
| `maxReviewsPerProduct` | integer | Max reviews per product (reviews mode  |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `minRating` | string | Minimum star rating |
| `freeCargoOnly` | boolean | Free shipping only |
| `fastDeliveryOnly` | boolean | Fast delivery only |
| `officialSellerOnly` | boolean | Official seller only |
| `couponsOnly` | boolean | Has collectable coupon only |
| `inStockOnly` | boolean | In stock only |
| `maxPages` | integer | Max pages per query / URL |
| `maxListings` | integer | Max products total |
| `fetchDetails` | boolean | Pull rich detail-page fields for each  |
| `fetchReviews` | boolean | Also pull review summary for each prod |
| `fetchQna` | boolean | Also pull Q&A for each product |
| `maxQnaPerProduct` | integer | Max Q&A entries per product |
| `proxyConfiguration` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/trendyol-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `contentId` | integer |
| `id` | integer |
| `groupId` | integer |
| `url` | string |
| `name` | string |
| `brand` | string |
| `brandId` | integer |
| `category` | object |
| `price` | object |
| `rating` | object |
| `seller` | object |
| `image` | string |
| `images` | list |
| `stock` | null |
| `inStock` | boolean |
| `boutiqueId` | integer |
| `campaignId` | integer |
| `listingId` | string |
| `itemNumber` | integer |
| `variantValue` | string |
| `variantId` | string |
| `freeCargo` | boolean |
| `fastDelivery` | boolean |
| `officialSeller` | boolean |
| `sameDayShipping` | boolean |
| `rushDelivery` | boolean |
| `hasCoupon` | boolean |
| `hasCodePromo` | boolean |
| `hasFlashSale` | boolean |
| `isInfluencerPreferred` | boolean |
| `hasReviewPhoto` | boolean |
| `dealBadge` | null |
| `stripBadge` | null |
| `promotions` | list |
| `stamps` | object |
| `badges` | list |
| `socialProof` | list |
| `reviews` | null |
| `qna` | null |

---

[← All scrapers](../../README.md)
