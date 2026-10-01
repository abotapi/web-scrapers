# MediaMarkt.es Scraper

Scrape MediaMarkt Spain (mediamarkt.es) products: current price, strike-through original price + discount on offers, brand, EAN, category path, availability, image gallery, full spec sheet, other-seller offers, and reviews with ratings. Search keywords or paste links.

**[Open MediaMarkt.es Scraper on Apify](https://apify.com/abotapi/mediamarkt-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~mediamarkt-es-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "portatil", "sortBy": "RELEVANCE", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "ES"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword |
| `categoryId` | string | Category id |
| `brands` | array | Brands |
| `minRating` | integer | Minimum rating |
| `minPrice` | number | Minimum price (EUR) |
| `maxPrice` | number | Maximum price (EUR) |
| `sortBy` | string | Sort order |
| `urls` | array | URLs to scrape |
| `fetchDetails` | boolean | Fetch full product detail |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/mediamarkt-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `sku` | string |
| `ean` | string |
| `name` | string |
| `brand` | string |
| `categoryPath` | list |
| `category` | string |
| `url` | string |
| `rating` | float |
| `reviewCount` | integer |
| `isMarketplace` | boolean |
| `price` | integer |
| `currency` | string |
| `discountAmount` | integer |
| `discountPercent` | integer |
| `originalPrice` | integer |
| `isOnSpecial` | boolean |
| `strikePriceType` | string |
| `shippingCost` | float |
| `installment` | object |
| `image` | string |
| `images` | list |
| `onlineAvailable` | boolean |
| `availabilityStatus` | string |
| `reviews` | object |

---

[← All scrapers](../../README.md)
