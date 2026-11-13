# Magazine Luiza Scraper

Scrape Magazine Luiza (magazineluiza.com.br) by keyword, brand, seller or URL. Extract product names, prices, cash and installment offers, sellers, ratings, stock, badges and attributes. Optional enrichment adds full product details and customer reviews.

**[Open Magazine Luiza Scraper on Apify](https://apify.com/abotapi/magazineluiza-com-br-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~magazineluiza-com-br-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["notebook"], "sortBy": "relevance", "minRating": "any", "maxPages": 1, "maxItems": 10, "maxReviews": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `sortBy` | string | Sort by |
| `minPrice` | number | Minimum price (BRL) |
| `maxPrice` | number | Maximum price (BRL) |
| `brands` | array | Brand |
| `sellers` | array | Sold by (seller) |
| `minRating` | string | Minimum rating |
| `excludeSponsored` | boolean | Skip sponsored placements |
| `availableOnly` | boolean | Available products only |
| `urls` | array | Search or category links |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max items |
| `includeDetails` | boolean | Fetch full product details |
| `maxReviews` | integer | Max reviews per product |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/magazineluiza-com-br-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `sku` | string |
| `title` | string |
| `brand` | string |
| `brandSlug` | string |
| `url` | string |
| `image` | string |
| `price` | integer |
| `listPrice` | integer |
| `discountPercent` | integer |
| `currency` | string |
| `cashPrice` | float |
| `cashPaymentMethod` | string |
| `cashDiscountPercent` | integer |
| `installmentCount` | integer |
| `installmentAmount` | float |
| `installmentTotal` | integer |
| `installmentTerms` | string |
| `installmentInterestFree` | null |
| `sellerId` | string |
| `sellerName` | string |
| `soldByMagalu` | boolean |
| `available` | boolean |
| `rating` | float |
| `reviewCount` | integer |
| `categoryId` | string |
| `category` | string |
| `subcategoryId` | string |
| `subcategory` | string |
| `sponsored` | boolean |
| `isBuyBox` | boolean |
| `minimumOrderQuantity` | integer |
| `maxCheckoutQuantity` | null |
| `promoStartDate` | null |
| `promoEndDate` | null |
| `coupon` | object |
| `badges` | list |
| `tags` | list |
| `magaluRecommends` | boolean |
| `shippingTag` | object |

---

[← All scrapers](../../README.md)
