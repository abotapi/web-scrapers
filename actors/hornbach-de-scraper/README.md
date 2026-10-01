# HORNBACH Products Scraper

Scrape HORNBACH (hornbach.de) DIY, building & garden products: current + strike-through price with discount, per-unit pricing (m2/kg/piece), full technical specs, category path, online & in-store availability, and complete product reviews with rating breakdown.

**[Open HORNBACH Products Scraper on Apify](https://apify.com/abotapi/hornbach-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~hornbach-de-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "akkuschrauber", "sortBy": "SCORE", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword |
| `category` | string | Category ID (optional) |
| `brands` | array | Brands |
| `sellers` | array | Sellers |
| `minPrice` | integer | Minimum price (EUR) |
| `maxPrice` | integer | Maximum price (EUR) |
| `availability` | string | Availability filter |
| `sortBy` | string | Sort order |
| `urls` | array | URLs to scrape |
| `fetchDetails` | boolean | Fetch full product detail |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/hornbach-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `sku` | string |
| `concreteProductId` | string |
| `name` | string |
| `url` | string |
| `brand` | string |
| `brandLogoUrl` | string |
| `price` | float |
| `currency` | string |
| `priceUnit` | string |
| `originalPrice` | float |
| `discountAmount` | integer |
| `discountPercent` | float |
| `packPrice` | null |
| `packPriceUnit` | null |
| `badges` | list |
| `rating` | float |
| `reviewCount` | integer |
| `variantCount` | null |
| `image` | string |
| `thumbnailUrl` | string |
| `onlineAvailable` | boolean |
| `onlineAvailabilityText` | string |
| `storePickupAvailable` | boolean |
| `storePickupAvailabilityText` | string |
| `onlineMerchant` | object |
| `storeMerchant` | object |
| `searchTerm` | string |
| `reviews` | object |

---

[← All scrapers](../../README.md)
