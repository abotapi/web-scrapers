# Netshoes Brazil Scraper

Scrape sportswear and footwear from netshoes.com.br. Search by keyword with the store's own brand, size, colour and gender filters, or paste product and category links. Returns BRL price, was-price, discount, instalments, stock per size, colour variants, media, specs and reviews with fit feedback.

**[Open Netshoes Brazil Scraper on Apify](https://apify.com/abotapi/netshoes-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~netshoes-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["tenis adidas"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `urls` | array | Netshoes links |
| `brand` | string | Brand |
| `category` | string | Department |
| `productType` | string | Product type |
| `size` | string | Size |
| `color` | string | Colour |
| `gender` | string | Gender |
| `minPrice` | integer | Minimum price (BRL) |
| `maxPrice` | integer | Maximum price (BRL) |
| `inStockOnly` | boolean | Only products in stock |
| `onSaleOnly` | boolean | Only discounted products |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Read each product's page |
| `fetchReviews` | boolean | Fetch customer reviews and fit feedbac |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max result pages per keyword or link |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/netshoes-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `sku` | string |
| `variantSku` | null |
| `productCode` | string |
| `title` | string |
| `brand` | string |
| `brandSlug` | null |
| `department` | string |
| `productType` | string |
| `genders` | list |
| `categoryPath` | list |
| `breadcrumb` | list |
| `url` | string |
| `currency` | string |
| `price` | float |
| `originalPrice` | float |
| `priceBeforePaymentDiscount` | float |
| `paymentMethod` | null |
| `paymentMethodPrice` | null |
| `discountAmount` | null |
| `discountPercent` | null |
| `onSale` | boolean |
| `installments` | null |
| `installmentPlans` | list |
| `sellerName` | null |
| `soldByStore` | null |
| `inStock` | boolean |
| `sizes` | list |
| `sizesInStock` | null |
| `variants` | null |
| `color` | null |
| `colorVariants` | list |
| `freeShipping` | null |
| `fastFulfilment` | boolean |
| `additionalDeliveryDays` | null |
| `preSale` | null |
| `badges` | list |
| `featuredImage` | string |
| `images` | list |
| `videos` | list |
| `rating` | integer |

---

[← All scrapers](../../README.md)
