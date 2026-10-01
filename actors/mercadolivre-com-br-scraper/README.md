# Mercado Livre Brazil Scraper

Scrape Mercado Livre Brazil by keyword or URL. Filter by category, brand, price, condition, shipping, official store, and seller rating. Extract prices, discounts, instalments, stock, delivery, seller details, variants, specifications, and buyer reviews.

**[Open Mercado Livre Brazil Scraper on Apify](https://apify.com/abotapi/mercadolivre-com-br-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~mercadolivre-com-br-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["notebook"], "condition": "any", "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "BR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `urls` | array | Links or MLB codes |
| `category` | string | Category |
| `brand` | string | Brand |
| `condition` | string | Condition |
| `minPrice` | integer | Minimum price (BRL) |
| `maxPrice` | integer | Maximum price (BRL) |
| `freeShippingOnly` | boolean | Free shipping only |
| `fulfillmentOnly` | boolean | Marketplace-fulfilled only |
| `officialStoresOnly` | boolean | Official brand stores only |
| `bestSellersOnly` | boolean | Top-rated sellers only |
| `minDiscountPercent` | integer | Minimum discount (%) |
| `interestFreeInstallments` | boolean | Interest-free instalments only |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch full details |
| `fetchReviews` | boolean | Fetch buyer opinions |
| `maxReviewsPerProduct` | integer | Max opinions per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max result pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/mercadolivre-com-br-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `itemId` | string |
| `catalogProductId` | string |
| `title` | string |
| `url` | string |
| `categoryId` | string |
| `domainId` | string |
| `sellerName` | string |
| `officialStore` | boolean |
| `price` | integer |
| `originalPrice` | integer |
| `discountPercent` | integer |
| `currency` | string |
| `installments` | object |
| `freeShipping` | boolean |
| `fulfillment` | boolean |
| `shippingText` | string |
| `soldQuantity` | integer |
| `rating` | float |
| `images` | list |
| `scrapedAt` | string |
| `image` | string |
| `installmentsText` | string |

---

[← All scrapers](../../README.md)
