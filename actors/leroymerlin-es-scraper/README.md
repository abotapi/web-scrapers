# LeroyMerlin.es Scraper

Scrape Leroy Merlin Spain (leroymerlin.es) DIY and home-improvement products: price, strike-through original price and discount, seller identity (Leroy Merlin vs marketplace) with every competing offer, stock, rating and individual reviews. Search by keyword/category or paste product/listing links.

**[Open LeroyMerlin.es Scraper on Apify](https://apify.com/abotapi/leroymerlin-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~leroymerlin-es-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "taladro", "sortBy": "relevance", "sellerFilter": "any", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "ES"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword |
| `category` | string | Category path |
| `sortBy` | string | Sort order |
| `minPrice` | number | Minimum price (EUR) |
| `maxPrice` | number | Maximum price (EUR) |
| `minRating` | number | Minimum rating |
| `onPromotionOnly` | boolean | Only products on promotion |
| `sellerFilter` | string | Seller |
| `urls` | array | leroymerlin.es links |
| `fetchDetails` | boolean | Fetch product detail |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search/category/URL |
| `maxItems` | integer | Max products |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/leroymerlin-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `sku` | string |
| `name` | string |
| `brand` | string |
| `url` | string |
| `price` | integer |
| `priceExclTax` | float |
| `currency` | string |
| `originalPrice` | null |
| `discountPercent` | null |
| `discountAmount` | null |
| `isOnSpecial` | boolean |
| `sellerId` | string |
| `sellerName` | string |
| `sellerType` | string |
| `offerType` | string |
| `rating` | float |
| `totalOfferCount` | integer |
| `sellersComposition` | string |
| `sponsored` | boolean |
| `ean` | string |
| `description` | string |
| `image` | string |
| `numberOfImages` | integer |
| `numberOfReviews` | integer |
| `categoryPath` | list |
| `category` | string |
| `stock` | integer |
| `stockStatus` | string |
| `deliveryTime` | string |
| `reviews` | object |
| `searchMode` | string |

---

[← All scrapers](../../README.md)
