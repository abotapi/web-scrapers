# El Corte Inglés Scraper

Scrape El Corte Inglés elcorteingles.es products across fashion, electronics, home, beauty, jewellery, toys and books. Extract current and was-prices, discounts, brands, categories, images, colour/size variants, availability, ratings and reviews. Supports keyword, category and URL modes.

**[Open El Corte Inglés Scraper on Apify](https://apify.com/abotapi/elcorteingles-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~elcorteingles-es-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerm": "zapatillas running", "sortBy": "RELEVANCE", "maxReviewsPerProduct": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerm` | string | Search keyword |
| `categoryPath` | string | Category path |
| `onSaleOnly` | boolean | On sale only |
| `brands` | array | Brands |
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

Full details on the [scraper page](https://apify.com/abotapi/elcorteingles-es-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `name` | string |
| `brand` | string |
| `category` | string |
| `categoryPath` | list |
| `url` | string |
| `sku` | string |
| `gtin` | string |
| `color` | string |
| `size` | string |
| `price` | float |
| `currency` | string |
| `originalPrice` | float |
| `discountPercent` | integer |
| `isOnSale` | boolean |
| `onlineAvailable` | boolean |
| `isMarketplace` | boolean |
| `seller` | null |
| `image` | string |
| `images` | list |
| `variants` | list |
| `reviews` | object |

---

[← All scrapers](../../README.md)
