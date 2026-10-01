# Naver Shopping Scraper

Scrape Naver Shopping products by Korean or English keyword, or by URL. Returns 190+ fields per product, including prices, discounts, seller, ratings, reviews, category path, brand, shipping, and cross-mall price comparison.

**[Open Naver Shopping Scraper on Apify](https://apify.com/abotapi/naver-brand-store-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~naver-brand-store-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "brandStores": ["marschoco"], "sort": "popular", "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "KR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `brandStores` | array | Brand stores |
| `startUrls` | array | Brand store URLs |
| `sort` | string | Sort by |
| `fetchReviews` | boolean | Fetch review detail |
| `maxItems` | integer | Max products |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/naver-brand-store-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productNo` | string |
| `channelProductId` | string |
| `productName` | string |
| `productUrl` | string |
| `imageUrl` | string |
| `salePrice` | integer |
| `discountedPrice` | integer |
| `mobileDiscountedPrice` | integer |
| `immediateDiscount` | integer |
| `originalPrice` | integer |
| `discountPercent` | integer |
| `isOnSpecial` | boolean |
| `savingsAmount` | integer |
| `stockQuantity` | integer |
| `productStatus` | string |
| `displayStatus` | string |
| `saleType` | string |
| `authenticationType` | string |
| `averageRating` | float |
| `totalReviews` | integer |
| `premiumReviews` | integer |
| `brand` | string |
| `maker` | string |
| `sellerName` | string |
| `sellerId` | string |
| `channelNo` | integer |
| `channelUid` | string |
| `categoryId` | string |
| `categoryName` | string |
| `categoryPath` | list |
| `wholeCategoryId` | string |
| `freeDelivery` | boolean |
| `deliveryFeeType` | string |
| `deliveryBaseFee` | integer |
| `arrivalGuarantee` | boolean |
| `todayDelivery` | boolean |
| `brandSlug` | string |
| `rank` | integer |
| `crawledAt` | string |
| `raw` | object |

---

[← All scrapers](../../README.md)
