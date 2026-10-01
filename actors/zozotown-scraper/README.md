# ZOZOTOWN Scraper

Scrape ZOZOTOWN (zozo.jp), Japan's largest fashion marketplace: name, brand, JPY price with was-price and discount, per-size and per-colour stock, materials, size charts, shipping, images and reviews with star breakdown. Search by keyword, brand, shop or category, or paste product and listing links.

**[Open ZOZOTOWN Scraper on Apify](https://apify.com/abotapi/zozotown-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~zozotown-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["ワンピース"], "sort": "popular", "gender": "any", "color": "any", "priceType": "any", "condition": "any", "sellType": "any", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "JP"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `queries` | array | Keywords |
| `brandSlug` | string | Brand |
| `shopSlug` | string | Shop |
| `categoryPath` | string | Category |
| `urls` | array | Start URLs |
| `sort` | string | Sort by |
| `gender` | string | Department |
| `color` | string | Colour |
| `priceType` | string | Price type |
| `condition` | string | Condition |
| `sellType` | string | Availability type |
| `includeOutOfStock` | boolean | Include sold-out products |
| `giftWrappingOnly` | boolean | Gift wrapping available only |
| `couponOnly` | boolean | Coupon eligible only |
| `minPrice` | integer | Minimum price (JPY) |
| `maxPrice` | integer | Maximum price (JPY) |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/zozotown-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `goodsId` | integer |
| `goodsCode` | string |
| `goodsDetailId` | integer |
| `name` | string |
| `url` | string |
| `category` | null |
| `brandId` | integer |
| `brand` | string |
| `brandNameJp` | string |
| `shopId` | integer |
| `shopName` | string |
| `shopNameJp` | null |
| `shopSlug` | string |
| `price` | integer |
| `originalPrice` | integer |
| `discountPercent` | integer |
| `currency` | string |
| `isOnSale` | boolean |
| `isTimeSale` | boolean |
| `isSoldOut` | boolean |
| `isPromoted` | boolean |
| `colorId` | integer |
| `colorName` | string |
| `colorCount` | integer |
| `colorVariants` | list |
| `image` | string |
| `thumbnail` | string |
| `hasMultipleSizes` | boolean |
| `hasCoupon` | boolean |

---

[← All scrapers](../../README.md)
