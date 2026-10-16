# Boulanger.com Scraper

Scrape Boulanger (boulanger.com) electronics and home-appliance products: current price plus strike-through was-price, specials, colour/capacity variant matrix, brand, category, full spec sheet and customer reviews with ratings. Search by keyword or paste links.

**[Open Boulanger.com Scraper on Apify](https://apify.com/abotapi/boulanger-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~boulanger-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "aspirateur robot", "sortBy": "RELEVANCE", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword |
| `category` | string | Category |
| `sortBy` | string | Sort order |
| `urls` | array | URLs to scrape |
| `brands` | array | Brands |
| `minPrice` | number | Minimum price (EUR) |
| `maxPrice` | number | Maximum price (EUR) |
| `specialsOnly` | boolean | Discounted / specials items only |
| `fetchDetails` | boolean | Fetch full product detail |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max products total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/boulanger-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `sku` | null |
| `ean` | null |
| `name` | string |
| `brand` | string |
| `category` | string |
| `breadcrumbPath` | list |
| `url` | string |
| `price` | integer |
| `currency` | string |
| `priceExclTax` | float |
| `originalPrice` | float |
| `discountAmount` | float |
| `discountPercent` | integer |
| `isOnSpecial` | boolean |
| `promoLabel` | null |
| `unitPrice` | null |
| `image` | string |
| `rating` | float |
| `reviewCount` | integer |
| `onlineAvailable` | boolean |
| `storePickupAvailable` | null |
| `condition` | string |
| `sellerName` | string |
| `isBundle` | boolean |
| `reviews` | object |

---

[← All scrapers](../../README.md)
