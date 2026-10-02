# Casas Bahia Brazil Electronics & Home Goods Scraper

Scrape products from Casas Bahia Brazil by keyword, department, or URL. Filter by brand, price, discount, rating, and instalment terms. Extract SKUs, titles, brands, current and original prices, Pix offers, BRL instalment plans, stock, pickup options, images, variants, specifications, and reviews.

**[Open Casas Bahia Brazil Electronics & Home Goods Scraper on Apify](https://apify.com/abotapi/casasbahia-com-br-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~casasbahia-com-br-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["geladeira"], "minRating": "0", "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `urls` | array | Store links or product codes |
| `categories` | array | Department |
| `brands` | array | Brand |
| `minPrice` | integer | Minimum price (BRL) |
| `maxPrice` | integer | Maximum price (BRL) |
| `minDiscountPercent` | integer | Minimum discount (%) |
| `minRating` | string | Minimum average rating |
| `minInstallments` | integer | Minimum interest-free-eligible instalm |
| `interestFreeInstallmentsOnly` | boolean | Only interest-free instalments |
| `inStockOnly` | boolean | Only products that can be ordered |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch product details |
| `includeReviews` | boolean | Include customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max result pages per keyword or link |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/casasbahia-com-br-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `productGroupId` | string |
| `title` | string |
| `brand` | string |
| `brandId` | string |
| `url` | string |
| `categoryName` | string |
| `categoryPath` | list |
| `categoryIds` | list |
| `price` | integer |
| `originalPrice` | float |
| `discountPercent` | integer |
| `discountAmount` | float |
| `listPrice` | integer |
| `currency` | string |
| `onSale` | boolean |
| `cashPrice` | null |
| `cashPriceLabel` | null |
| `cashDiscountPercent` | null |
| `hasPixDiscount` | boolean |
| `hasBoletoDiscount` | boolean |
| `installmentText` | string |
| `installmentCount` | integer |
| `installmentValue` | float |
| `installmentInterestFree` | boolean |
| `installmentOptions` | list |
| `inStock` | boolean |
| `availability` | object |
| `pickupInStore` | boolean |
| `deliveryEstimate` | null |
| `shippingCost` | null |
| `sellerId` | string |
| `sellerName` | string |
| `sellerCount` | integer |
| `offerCount` | integer |
| `minOfferPrice` | integer |
| `maxOfferPrice` | integer |
| `image` | string |
| `images` | list |
| `videos` | list |

---

[← All scrapers](../../README.md)
