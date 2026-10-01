# Americanas Brazil Scraper

Scrape Americanas Brazil (americanas.com.br) by keyword, department or pasted link. Returns SKU, title, brand, seller (store or marketplace), price, PIX price, discount, instalments in BRL, stock, images, variants, specs and reviews. Incremental mode tracks changes.

**[Open Americanas Brazil Scraper on Apify](https://apify.com/abotapi/americanas-com-br-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~americanas-com-br-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["notebook dell"], "sellerType": "any", "sortBy": "relevance", "deliveryPostalCode": "01310100", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `urls` | array | Store links |
| `categories` | array | Department |
| `brands` | array | Brand |
| `sellerType` | string | Sold by |
| `minPrice` | integer | Minimum price (BRL) |
| `maxPrice` | integer | Maximum price (BRL) |
| `minInterestFreeInstallments` | integer | Minimum interest free instalments |
| `inStockOnly` | boolean | Only products that can be ordered |
| `onSaleOnly` | boolean | Only reduced price products |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch delivery details |
| `deliveryPostalCode` | string | Delivery postal code (CEP) |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max result pages per keyword or link |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/americanas-com-br-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `skuId` | string |
| `name` | string |
| `slug` | string |
| `url` | string |
| `brand` | string |
| `brandId` | string |
| `ean` | string |
| `referenceId` | string |
| `categories` | list |
| `breadcrumb` | list |
| `categoryPath` | string |
| `categoryName` | string |
| `department` | string |
| `sellerId` | string |
| `sellerName` | string |
| `sellerType` | string |
| `otherSellers` | list |
| `sellerCount` | integer |
| `currency` | string |
| `price` | integer |
| `listPrice` | integer |
| `originalPrice` | integer |
| `discountAmount` | integer |
| `discountPercent` | float |
| `onSale` | boolean |
| `pixPrice` | float |
| `pixDiscountAmount` | float |
| `pixDiscountPercent` | integer |
| `maxInterestFreeInstallments` | integer |
| `interestFreeInstallmentValue` | float |
| `maxInstallments` | integer |
| `installmentPlans` | list |
| `inStock` | boolean |
| `availableQuantity` | integer |
| `priceValidUntil` | string |
| `description` | string |
| `shortDescription` | string |
| `specifications` | object |
| `specificationGroups` | list |

---

[← All scrapers](../../README.md)
